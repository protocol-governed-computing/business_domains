"""
CT_PURE_CHOOSE_PERMITTED_WORD_V0

Pure Capability Transform (Atom)

Purpose:
    The rules' step. Stop the forbidden words among those the model offered, and choose one permitted
    word under the freedom of word choice and a stated seed. Given the same offer, rules, seed and
    response so far it chooses the same word, which is what lets anyone re-derive a response from its
    record.

Stopping:
    A rule reads the response so far joined to the candidate by one space, not the candidate alone, so
    a pattern written across several words — an account number split in two — is stopped at the word
    that completes it. A match counts only if it reaches into the candidate; the response so far was
    already checked. A match whose characters, with spaces and dashes removed, are among the rule's
    exceptions — the customer's own account numbers — is not a stop.

Choosing:
    The permitted candidates, most likely first and ties in offered order, are narrowed to the first
    freedom-plus-one; the one at (seed + position) modulo their count is chosen. Freedom zero always
    chooses the most likely permitted word. `<end>` finishes the response; any other word is appended
    after one space.

    When no candidate is permitted, the rule that stopped the most likely one is named and the response
    is left as it stood. Once the response has finished or been stopped, nothing changes.

Inputs:
    candidates     — array of {word, likelihood}
    rules_in_force — object; forbidden [{rule, pattern, except?}], freedom, seed
    position       — integer; which word this is
    text           — string; the response so far
    finished       — boolean
    stopped_by     — string; the rule that stopped the response, or `none`
    stopped        — array; the words stopped so far

Outputs:
    text, finished, stopped_by, stopped — the same, after this word
"""

import re
from typing import Any, Dict, List, Optional

END = "<end>"
NOT_STOPPED = "none"
_SEPARATORS = re.compile(r"[ -]")


class CTExecutionError(RuntimeError):
    """The inputs cannot be judged."""


def _normalized(value: str) -> str:
    return _SEPARATORS.sub("", value)


def _stopping_rule(text: str, word: str, forbidden: List[Dict[str, Any]]) -> Optional[str]:
    joined = f"{text} {word}" if text else word
    candidate_start = len(joined) - len(word)
    for rule in forbidden:
        exceptions = {_normalized(e) for e in rule.get("except") or []}
        for match in re.finditer(rule["pattern"], joined):
            if match.end() <= candidate_start:
                continue
            if _normalized(match.group()) in exceptions:
                continue
            return rule["rule"]
    return None


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("candidates", "rules_in_force", "position", "text", "finished", "stopped_by", "stopped"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_CHOOSE_PERMITTED_WORD_V0: requires input {field!r}")
    text, finished, stopped_by = inputs["text"], inputs["finished"], inputs["stopped_by"]
    stopped = list(inputs["stopped"])
    if finished or stopped_by != NOT_STOPPED:
        return {"text": text, "finished": finished, "stopped_by": stopped_by, "stopped": stopped}

    rules = inputs["rules_in_force"]
    forbidden = rules.get("forbidden") or []
    freedom, seed, position = rules.get("freedom", 0), rules.get("seed", 0), inputs["position"]

    offered = [c for c in inputs["candidates"] if isinstance(c, dict) and isinstance(c.get("word"), str)]
    ordered = sorted(offered, key=lambda c: -float(c.get("likelihood", 0)))  # stable: ties keep offered order

    permitted, first_stop = [], None
    for candidate in ordered:
        rule = _stopping_rule(text, candidate["word"], forbidden)
        if rule is None:
            permitted.append(candidate["word"])
            continue
        stopped.append({"position": position, "word": candidate["word"], "rule": rule})
        first_stop = first_stop or rule

    if not permitted:
        return {"text": text, "finished": False, "stopped_by": first_stop or NOT_STOPPED, "stopped": stopped}

    window = permitted[: freedom + 1]
    word = window[(seed + position) % len(window)]
    if word == END:
        return {"text": text, "finished": True, "stopped_by": NOT_STOPPED, "stopped": stopped}
    return {"text": f"{text} {word}" if text else word, "finished": False,
            "stopped_by": NOT_STOPPED, "stopped": stopped}
