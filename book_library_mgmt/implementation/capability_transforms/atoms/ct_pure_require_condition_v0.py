"""
CT_PURE_REQUIRE_CONDITION_V0

Pure Capability Transform (Atom)

Purpose:
    Interpret an observation as a required condition — the governed step between a capability's
    raw output and a workflow branch.

    A side effect that reads state reports whether the read succeeded, not what it found. Routing
    on that status routes on "the store answered", which is always true. This transform asserts
    that an observation matches what the design requires, and raises when it does not, because
    raising is the only way the execution contract lets a transform yield anything but SUCCESS.

    `expected` is what keeps it one transform rather than two: "the work must already exist" and
    "the work must not already exist" are the same interpretation in opposite directions.

Inputs:
    condition — boolean; the observation being interpreted
    expected  — boolean; the value the observation must hold

Outputs:
    condition_held — boolean; always True when the transform returns
"""

from typing import Any, Dict


class CTExecutionError(RuntimeError):
    """The observation did not match what the design required."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("condition", "expected"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_REQUIRE_CONDITION_V0: requires input {field!r}")
        if not isinstance(inputs[field], bool):
            raise CTExecutionError(
                f"CT_PURE_REQUIRE_CONDITION_V0: {field!r} must be a bool, "
                f"got {type(inputs[field]).__name__}"
            )

    if inputs["condition"] != inputs["expected"]:
        raise CTExecutionError(
            "CT_PURE_REQUIRE_CONDITION_V0: observation "
            f"{inputs['condition']!r} did not match the required {inputs['expected']!r}"
        )

    return {"result_status": "SUCCESS", "condition_held": True}
