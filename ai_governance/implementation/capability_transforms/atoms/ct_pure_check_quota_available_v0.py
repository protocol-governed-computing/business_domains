"""
CT_PURE_CHECK_QUOTA_AVAILABLE_V0

Pure Capability Transform (Atom)

Purpose:
    Determine whether license quota remains under a declared cap.

Implementation:
    - Compares assigned_count against quota
    - Raises CTExecutionError when the cap is reached — the protocol's VIOLATION signal
      for a validating CT; returns the remaining count otherwise

Purity Class: ct_pure
"""

from typing import Any, Dict

from runtime.ct_executor import CTExecutionError


def _require_int(inputs: Dict[str, Any], key: str) -> int:
    if key not in inputs:
        raise CTExecutionError(
            f"CT_PURE_CHECK_QUOTA_AVAILABLE_V0: missing required input '{key}'"
        )
    value = inputs[key]
    # bool is a subclass of int — reject it explicitly rather than silently coercing.
    if isinstance(value, bool) or not isinstance(value, int):
        raise CTExecutionError(
            f"CT_PURE_CHECK_QUOTA_AVAILABLE_V0: '{key}' must be an int, "
            f"got {type(value).__name__}"
        )
    if value < 0:
        raise CTExecutionError(
            f"CT_PURE_CHECK_QUOTA_AVAILABLE_V0: '{key}' must be non-negative, got {value}"
        )
    return value


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_CHECK_QUOTA_AVAILABLE_V0.

    Inputs:
        assigned_count (int): Licenses currently assigned
        quota (int): Declared license cap

    Outputs:
        quota_available (bool): True when assigned_count is below quota
        remaining (int): Licenses remaining under the cap, floored at zero
    """
    assigned_count = _require_int(inputs, "assigned_count")
    quota = _require_int(inputs, "quota")

    remaining = quota - assigned_count

    if remaining <= 0:
        raise CTExecutionError(
            f"CT_PURE_CHECK_QUOTA_AVAILABLE_V0: license cap reached "
            f"(assigned_count={assigned_count}, quota={quota})"
        )

    return {"result_status": "SUCCESS", "quota_available": True, "remaining": remaining}
