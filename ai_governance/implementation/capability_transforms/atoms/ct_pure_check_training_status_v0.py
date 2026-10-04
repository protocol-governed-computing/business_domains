"""
CT_PURE_CHECK_TRAINING_STATUS_V0

Pure Capability Transform (Atom)

Purpose:
    Evaluate whether an employee has completed the training required for AI license
    provisioning.

Implementation:
    - Reads the declared training_completed fact
    - Raises CTExecutionError when training is incomplete — the protocol's VIOLATION
      signal for a validating CT; returns the eligibility flag otherwise

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_CHECK_TRAINING_STATUS_V0.

    Inputs:
        training_completed (bool): Whether required training is complete

    Outputs:
        training_eligible (bool): True when training is complete
    """
    if "training_completed" not in inputs:
        raise CTExecutionError(
            "CT_PURE_CHECK_TRAINING_STATUS_V0: missing required input 'training_completed'"
        )

    training_completed = inputs["training_completed"]

    if not isinstance(training_completed, bool):
        raise CTExecutionError(
            "CT_PURE_CHECK_TRAINING_STATUS_V0: 'training_completed' must be a bool, "
            f"got {type(training_completed).__name__}"
        )

    if not training_completed:
        raise CTExecutionError(
            "CT_PURE_CHECK_TRAINING_STATUS_V0: required training is not complete"
        )

    return {"result_status": "SUCCESS", "training_eligible": True}
