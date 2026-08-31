"""
CT_PURE_SELECT_RECORDS_V0

Pure Capability Transform (Atom)

Purpose:
    Select the records matching stated criteria, and return none when none match.

    The platform's filter refuses an empty result: `CT_PURE_FILTER_RECORDS_V0` raises when nothing
    matched, which is right where the caller expected to find something — the same convention as
    `UPDATE_WHERE`, which refuses rather than reporting that it changed nothing. It is wrong for a
    read. An edition the library holds no copies of is a true answer about the catalog, not a failed
    lookup, and until this existed retrieving such an edition failed outright.

    That case became reachable with the edition change: registering a further edition of a work
    requires no copy, so an edition with no copies is an ordinary state rather than an impossible
    one. The platform transform is untouched — a domain extends the platform by adding artifacts in
    its own namespace, never by amending one in place — and callers that mean "nothing matched is a
    refusal" keep it.

Inputs:
    source — list of records to select from
    filter — object of field/value criteria a record must match on every key

Outputs:
    extracted — the records that matched, possibly none
"""

from typing import Any, Dict, List


class CTExecutionError(RuntimeError):
    """The inputs cannot be selected from."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    if "source" not in inputs:
        raise CTExecutionError("CT_PURE_SELECT_RECORDS_V0: missing required input 'source'")
    if "filter" not in inputs:
        raise CTExecutionError("CT_PURE_SELECT_RECORDS_V0: missing required input 'filter'")

    source = inputs["source"]
    criteria = inputs["filter"]

    if not isinstance(source, list):
        raise CTExecutionError(
            f"CT_PURE_SELECT_RECORDS_V0: 'source' must be a list of records, "
            f"got {type(source).__name__}"
        )
    if not isinstance(criteria, dict):
        raise CTExecutionError(
            f"CT_PURE_SELECT_RECORDS_V0: 'filter' must be an object of criteria, "
            f"got {type(criteria).__name__}"
        )

    def matches(record: Any) -> bool:
        if not isinstance(record, dict):
            return False
        return all(record.get(field) == value for field, value in criteria.items())

    extracted: List[Any] = [record for record in source if matches(record)]

    # No refusal on an empty result. Whether nothing matching is a problem is the caller's
    # judgement, and a read has no business making it on the caller's behalf.
    return {"result_status": "SUCCESS", "extracted": extracted}
