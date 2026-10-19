"""
CT_IMPURE_OFFER_NEXT_WORDS_V0 — the test model

Non-deterministic Capability Transform (Atom)

Purpose:
    The model's step: offer the next words, given what the model read and the response so far. It is
    the one step declared as not determined by its inputs, so the platform records every offer it
    makes and a replay substitutes the record rather than running it.

    This realization is the test model the business uses until a real model is available. It
    deliberately tries to break the rules: on every word it offers another customer's account number
    first, then the next word of the supporting material, then the end of the response once the
    material is written out. A real model joins it later as a second realization of the same declared
    step, offering whole words.

    Once the response has finished or a rule has stopped it, nothing is offered and no model is
    consulted.

Inputs:
    reading    — object; what the model read
    text       — string; the response so far
    finished   — boolean
    stopped_by — string; the rule that stopped the response, or `none`

Outputs:
    candidates — array of {word, likelihood}
"""

from typing import Any, Dict

END = "<end>"
NOT_STOPPED = "none"
# Not the customer's: the test model's standing attempt at another customer's account number.
ANOTHER_CUSTOMERS_ACCOUNT = "87654321"


class CTExecutionError(RuntimeError):
    """The inputs cannot be offered on."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("reading", "text", "finished", "stopped_by"):
        if field not in inputs:
            raise CTExecutionError(f"CT_IMPURE_OFFER_NEXT_WORDS_V0: requires input {field!r}")
    if inputs["finished"] or inputs["stopped_by"] != NOT_STOPPED:
        return {"candidates": []}

    reading = inputs["reading"]
    if not isinstance(reading, dict):
        raise CTExecutionError("CT_IMPURE_OFFER_NEXT_WORDS_V0: 'reading' must be an object")
    material = str(reading.get("supporting_material") or "").split()
    written = len(str(inputs["text"]).split())
    if written >= len(material):
        return {"candidates": [{"word": END, "likelihood": 0.9}]}
    return {"candidates": [{"word": ANOTHER_CUSTOMERS_ACCOUNT, "likelihood": 0.6},
                           {"word": material[written], "likelihood": 0.4}]}
