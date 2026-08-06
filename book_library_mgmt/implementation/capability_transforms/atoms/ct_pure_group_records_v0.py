"""
CT_PURE_GROUP_RECORDS_V0

Pure Capability Transform (Atom)

Purpose:
    Group records by the value of a named attribute, so that a search can answer once per work
    rather than once per matching edition.

    Selection already exists as a transform and returns the records that match. Grouping is a
    different operation on the same records: three editions of one work are three matches and one
    answer, and the library's stated complaint is seeing the three. The two are kept apart because
    a filter that also grouped would have to be told, at every call site that does not want groups,
    not to.

    Records missing the attribute are grouped under the empty key rather than dropped. A search that
    silently discarded a record because one field was absent would under-report the collection, and
    under-reporting is the failure this whole change is trying to remove.

Inputs:
    source    — list of records to group
    attribute — string; the attribute whose value decides which group a record belongs to

Outputs:
    grouped — list of `{"key": <value>, "records": [...]}`, one entry per distinct value, in the
              order each value was first seen
"""

from typing import Any, Dict, List

MISSING = ""


class CTExecutionError(RuntimeError):
    """The inputs cannot be grouped."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    if "source" not in inputs:
        raise CTExecutionError("CT_PURE_GROUP_RECORDS_V0: requires input 'source'")
    if "attribute" not in inputs:
        raise CTExecutionError("CT_PURE_GROUP_RECORDS_V0: requires input 'attribute'")

    source = inputs["source"]
    attribute = inputs["attribute"]

    if not isinstance(source, list):
        raise CTExecutionError(
            f"CT_PURE_GROUP_RECORDS_V0: 'source' must be a list of records, "
            f"got {type(source).__name__}"
        )
    if not isinstance(attribute, str) or not attribute:
        raise CTExecutionError(
            "CT_PURE_GROUP_RECORDS_V0: 'attribute' must be a non-empty string naming the "
            "attribute to group by"
        )

    # Insertion-ordered, so the answer is stable: two runs over the same store must return the same
    # groups in the same order, or a caller comparing results sees a change that never happened.
    groups: Dict[Any, List[Any]] = {}
    for record in source:
        if not isinstance(record, dict):
            raise CTExecutionError(
                f"CT_PURE_GROUP_RECORDS_V0: every record must be an object, "
                f"got {type(record).__name__}"
            )
        groups.setdefault(record.get(attribute, MISSING), []).append(record)

    return {
        "result_status": "SUCCESS",
        "grouped": [{"key": key, "records": records} for key, records in groups.items()],
    }
