"""
CT_PURE_READ_HOSTED_STATE_V0

Pure Capability Transform (Atom)

Purpose:
    Reduce a hosted request's record trail to the state of its response. The trail is the only
    account of a hosted request: its opening entry holds what the model reads, the rules in force,
    the limits and the fingerprint of the admitted model; each step entry holds an offer and the
    token chosen from it; a closing entry ends it. There is no second copy of the state to disagree
    with the trail.

    A request with no opening entry was never admitted, and one with a closing entry is no longer
    being written; both are refused, because nothing may be offered for them or released from them.

Inputs:
    entries — array; the request's trail as the store returns it, each entry carrying its record

Outputs:
    state — object; opening (the opening record), position (steps taken), text (the response as
            built), finished (whether the end was chosen), limit (the permitted length in tokens:
            the smaller of the model's registered maximum and the rules' longest response)
"""

from typing import Any, Dict, List

END = "<end>"
OPENING, STEP = "WRITING", "STEP"
CLOSING = ("RESPONDED", "REFUSED", "FAILED")


class CTExecutionError(RuntimeError):
    """The trail holds no request being written."""


def _records(entries: List[Any]) -> List[Dict[str, Any]]:
    ordered = sorted((e for e in entries if isinstance(e, dict)), key=lambda e: e.get("sequence_number", 0))
    return [e.get("record") for e in ordered if isinstance(e.get("record"), dict)]


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    if not isinstance(inputs.get("entries"), list):
        raise CTExecutionError("CT_PURE_READ_HOSTED_STATE_V0: requires input 'entries' as an array")
    records = _records(inputs["entries"])
    opening = next((r for r in records if r.get("outcome") == OPENING), None)
    if opening is None:
        raise CTExecutionError("CT_PURE_READ_HOSTED_STATE_V0: the request was never admitted as a hosted request")
    if any(r.get("outcome") in CLOSING for r in records):
        raise CTExecutionError("CT_PURE_READ_HOSTED_STATE_V0: the request is closed; nothing is written for it")

    steps = [r for r in records if r.get("outcome") == STEP]
    chosen = [s.get("chosen") for s in steps]
    text = "".join(c for c in chosen if isinstance(c, str) and c != END)
    limit = min(int(opening["maximum_response_length"]), int(opening["longest_response"]))
    return {"state": {"opening": opening, "position": len(steps), "text": text,
                      "finished": END in chosen, "limit": limit}}
