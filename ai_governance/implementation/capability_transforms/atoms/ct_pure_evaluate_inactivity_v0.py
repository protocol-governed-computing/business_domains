"""
CT_PURE_EVALUATE_INACTIVITY_V0

Pure Capability Transform (Atom)

Purpose:
    Evaluate whether a license has been dormant past its reclamation threshold.

Implementation:
    - Parses last_active_date and evaluation_date as ISO-8601
    - Computes whole days elapsed between them
    - Compares against threshold_days
    - Raises CTExecutionError when the license is still active — the protocol's VIOLATION
      signal for a validating CT; returns the dormancy verdict otherwise

    evaluation_date is a declared input, never a clock read: a pure CT that consulted the
    system clock would be non-deterministic and its trace unreplayable.

Purity Class: ct_pure
"""

from datetime import date, datetime
from typing import Any, Dict

from runtime.ct_executor import CTExecutionError


def _parse_iso_date(inputs: Dict[str, Any], key: str) -> date:
    if key not in inputs:
        raise CTExecutionError(
            f"CT_PURE_EVALUATE_INACTIVITY_V0: missing required input '{key}'"
        )
    raw = inputs[key]
    if not isinstance(raw, str):
        raise CTExecutionError(
            f"CT_PURE_EVALUATE_INACTIVITY_V0: '{key}' must be an ISO-8601 string, "
            f"got {type(raw).__name__}"
        )
    # Accept both date and date-time forms; a trailing Z is ISO-8601 but not accepted by
    # fromisoformat before 3.11, so normalize it.
    normalized = raw[:-1] + "+00:00" if raw.endswith("Z") else raw
    try:
        return datetime.fromisoformat(normalized).date()
    except ValueError:
        raise CTExecutionError(
            f"CT_PURE_EVALUATE_INACTIVITY_V0: '{key}' is not a valid ISO-8601 date: {raw!r}"
        ) from None


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """
    Execute CT_PURE_EVALUATE_INACTIVITY_V0.

    Inputs:
        last_active_date (str): ISO-8601 date/date-time of last recorded activity
        evaluation_date (str): ISO-8601 date/date-time the evaluation is made as of
        threshold_days (int): Inactivity threshold in days

    Outputs:
        is_inactive (bool): True when days_inactive >= threshold_days
        days_inactive (int): Whole days elapsed between the two dates
    """
    last_active = _parse_iso_date(inputs, "last_active_date")
    evaluated_on = _parse_iso_date(inputs, "evaluation_date")

    if "threshold_days" not in inputs:
        raise CTExecutionError(
            "CT_PURE_EVALUATE_INACTIVITY_V0: missing required input 'threshold_days'"
        )
    threshold_days = inputs["threshold_days"]
    if isinstance(threshold_days, bool) or not isinstance(threshold_days, int):
        raise CTExecutionError(
            "CT_PURE_EVALUATE_INACTIVITY_V0: 'threshold_days' must be an int, "
            f"got {type(threshold_days).__name__}"
        )
    if threshold_days < 0:
        raise CTExecutionError(
            f"CT_PURE_EVALUATE_INACTIVITY_V0: 'threshold_days' must be non-negative, "
            f"got {threshold_days}"
        )

    if evaluated_on < last_active:
        raise CTExecutionError(
            "CT_PURE_EVALUATE_INACTIVITY_V0: 'evaluation_date' precedes 'last_active_date' "
            f"({evaluated_on.isoformat()} < {last_active.isoformat()})"
        )

    days_inactive = (evaluated_on - last_active).days

    if days_inactive < threshold_days:
        raise CTExecutionError(
            f"CT_PURE_EVALUATE_INACTIVITY_V0: license is still active "
            f"(days_inactive={days_inactive} < threshold_days={threshold_days})"
        )

    return {"result_status": "SUCCESS", "is_inactive": True, "days_inactive": days_inactive}
