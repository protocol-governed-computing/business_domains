"""
CT_PURE_COMPARE_SENSITIVITY_V0

Pure Capability Transform (Atom)

Purpose:
    Decide whether a kind of information is no more sensitive than a ceiling, by the declared order
    of the kinds, least sensitive first. A kind above the ceiling is refused, and that refusal is how
    a user prompt carrying information the model may not read is stopped before the model sees it.

    Membership is confirmed before this runs; a kind or ceiling outside the declared kinds is still
    refused here, because an order cannot be read for a value it does not contain.

Inputs:
    kind    — string; the most sensitive kind the user prompt states it contains
    ceiling — string; the most sensitive kind the model may read
    kinds   — array; the declared kinds, least sensitive first

Outputs:
    within_ceiling — boolean; true whenever the transform returns
"""

from typing import Any, Dict


class CTExecutionError(RuntimeError):
    """The kind is above the ceiling, or the order cannot be read."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("kind", "ceiling", "kinds"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_COMPARE_SENSITIVITY_V0: requires input {field!r}")
    kind, ceiling, kinds = inputs["kind"], inputs["ceiling"], inputs["kinds"]
    if not isinstance(kinds, list) or not kinds:
        raise CTExecutionError("CT_PURE_COMPARE_SENSITIVITY_V0: 'kinds' must be a non-empty array")
    for name, value in (("kind", kind), ("ceiling", ceiling)):
        if value not in kinds:
            raise CTExecutionError(
                f"CT_PURE_COMPARE_SENSITIVITY_V0: {name} {value!r} is not a declared kind {kinds}"
            )
    if kinds.index(kind) > kinds.index(ceiling):
        raise CTExecutionError(
            f"CT_PURE_COMPARE_SENSITIVITY_V0: {kind!r} is more sensitive than the ceiling "
            f"{ceiling!r} — the model may not read it"
        )
    return {"within_ceiling": True}
