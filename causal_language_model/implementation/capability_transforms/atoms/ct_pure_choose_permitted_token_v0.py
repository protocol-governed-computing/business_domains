"""
CT_PURE_CHOOSE_PERMITTED_TOKEN_V0

Pure Capability Transform (Atom)

Purpose:
    The rules' step for a hosted model. Stop the forbidden tokens among those the host offered, and
    choose one permitted token under the freedom of choice and the seed in force. The test model's
    word choice, with one difference: a token carries its own spacing, so it is joined to the
    response exactly as it is, and a pattern spread across several tokens is judged on the text as
    built. Given the same state and offer it chooses the same token.

Stopping:
    A rule reads the response so far joined to the candidate, and a match counts only if it reaches
    into the candidate; the response so far was already judged. A match whose characters, with spaces
    and dashes removed, are among the rule's exceptions — the customer's own account numbers — is not
    a stop.

    Text is judged in its compatibility form (NFKC), so a lookalike — a subscript or full-width
    digit — is the character it looks like.

    A number is judged on its digits; spaces, commas, dots and dashes between digits are
    separators. A number the model read is not begun unless it could be a permitted one: when the
    candidate writes digits that begin a number some rule forbids in what the model read, and
    begin no other number the model read, it is stopped by that rule.

    Grounding, when the opening sets `ground_numbers`: a number may not be begun unless a number
    the model read begins with its digits, nor ended unless it is one — ended by a candidate that
    follows it with anything but a digit or a lone separator, or by the end marker. Such a
    candidate is stopped by `numbers_from_the_reading`. Without grounding, a number the model did
    not read is judged by the rules when it is complete.

Choosing:
    The permitted candidates, most likely first and ties in offered order, are narrowed to the first
    freedom-plus-one; the one at (seed + position) modulo their count is chosen. `<end>` ends the
    response. When no candidate is permitted, nothing is chosen and the rule that stopped the most
    likely candidate is named.

Length:
    A response may be at most `limit` tokens; the end marker is not one of them. A token that would
    take the response past its limit leaves it outside its length, and the step says so.

Inputs:
    state      — object; opening (with reading, rules_in_force and ground_numbers), position, text,
                 finished, limit
    candidates — array of {token, likelihood}

Outputs:
    step         — object; position, candidates, chosen, stopped, stopped_by, finished, within_length
    text         — string; the response with the chosen token
    finished     — boolean
    stopped_by   — string; the rule that left no permitted token, or `none`
    within_length — boolean; false when the response reached its limit unfinished
"""

import re
import unicodedata
from typing import Any, Dict, List, Optional, Tuple

END = "<end>"
NOT_STOPPED = "none"
_SEPARATORS = re.compile(r"[ -]")
_NUMBER = re.compile(r"[0-9](?:[ ,.-]?[0-9])*")
_OPEN_TAIL = re.compile(r"[ ,.-]?")
_NOT_DIGIT = re.compile(r"[^0-9]")
GROUNDING_RULE = "numbers_from_the_reading"


class CTExecutionError(RuntimeError):
    """The offer cannot be judged."""


def _normalized(value: str) -> str:
    return _SEPARATORS.sub("", value)


def _compatible(value: str) -> str:
    return unicodedata.normalize("NFKC", value)


def _digits(value: str) -> str:
    return _NOT_DIGIT.sub("", value)


def _read_numbers(reading: Dict[str, Any], forbidden: List[Dict[str, Any]]) -> Tuple[Dict[str, str], set]:
    """The numbers the model read, by their digits: those a rule forbids, by rule, and all of them."""
    read = _compatible(" ".join(str(v) for v in reading.values() if isinstance(v, str)))
    barred: Dict[str, str] = {}
    for rule in forbidden:
        exceptions = {_digits(e) for e in rule.get("except") or []}
        for match in re.finditer(rule["pattern"], read):
            number = _digits(match.group())
            if number and number not in exceptions:
                barred.setdefault(number, rule["rule"])
    return barred, {_digits(m.group()) for m in _NUMBER.finditer(read)}


def _stopping_rule(text: str, token: str, forbidden: List[Dict[str, Any]], barred: Dict[str, str],
                   read: set, grounded: bool) -> Optional[str]:
    ending = token == END
    judged = _compatible(text)
    joined = judged if ending else _compatible(text + token)
    if not ending:
        for rule in forbidden:
            exceptions = {_normalized(e) for e in rule.get("except") or []}
            for match in re.finditer(rule["pattern"], joined):
                if match.end() <= len(judged):
                    continue
                if _normalized(match.group()) in exceptions:
                    continue
                return rule["rule"]
    for match in _NUMBER.finditer(joined):
        still_open = _OPEN_TAIL.fullmatch(joined[match.end():]) is not None
        if match.end() < len(judged) and not still_open:
            continue  # closed before this candidate, and judged then
        digits = _digits(match.group())
        if match.end() > len(judged) and not any(n.startswith(digits) for n in read - set(barred)):
            for number, rule in barred.items():
                if number.startswith(digits):
                    return rule
        if grounded:
            if still_open and not ending:
                if not any(n.startswith(digits) for n in read):
                    return GROUNDING_RULE
            elif digits not in read:
                return GROUNDING_RULE
    return None


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    state, offered = inputs.get("state"), inputs.get("candidates")
    if not isinstance(state, dict) or not isinstance(offered, list):
        raise CTExecutionError("CT_PURE_CHOOSE_PERMITTED_TOKEN_V0: requires 'state' and 'candidates'")
    if state.get("finished"):
        raise CTExecutionError("CT_PURE_CHOOSE_PERMITTED_TOKEN_V0: the response is complete; nothing more is offered")

    rules = state["opening"]["rules_in_force"]
    forbidden = rules.get("forbidden") or []
    barred, read = _read_numbers(state["opening"]["reading"], forbidden)
    grounded = state["opening"]["ground_numbers"] is True
    freedom, seed = rules.get("freedom", 0), rules.get("seed", 0)
    position, text, limit = state["position"] + 1, state["text"], state["limit"]

    candidates = [c for c in offered if isinstance(c, dict) and isinstance(c.get("token"), str)]
    ordered = sorted(candidates, key=lambda c: -float(c.get("likelihood", 0)))  # stable: ties keep offered order

    permitted, stopped, first_stop = [], [], None
    for candidate in ordered:
        rule = _stopping_rule(text, candidate["token"], forbidden, barred, read, grounded)
        if rule is None:
            permitted.append(candidate["token"])
            continue
        stopped.append({"token": candidate["token"], "rule": rule})
        first_stop = first_stop or rule

    chosen, finished, stopped_by = None, False, NOT_STOPPED
    if permitted:
        window = permitted[: freedom + 1]
        chosen = window[(seed + position) % len(window)]
        finished = chosen == END
        if not finished:
            text = text + chosen
    else:
        stopped_by = first_stop or NOT_STOPPED
    within_length = finished or not permitted or position <= limit

    step = {"position": position, "candidates": candidates, "chosen": chosen, "stopped": stopped,
            "stopped_by": stopped_by, "finished": finished, "within_length": within_length}
    return {"step": step, "text": text, "finished": finished, "stopped_by": stopped_by,
            "within_length": within_length}
