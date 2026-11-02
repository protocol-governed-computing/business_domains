"""
CT_PURE_CHOOSE_FOLDER_PAGE_V0

Pure Capability Transform (Atom)

Purpose:
    Choose which messages make the page of a folder a person asked for. The host reports a folder's
    message identifiers in the order the provider received them; newest means most recently
    received, so the order is reversed and never re-sorted by identifier. The page is cut from that
    order, and the answer says whether more messages exist beyond it and whether the folder is empty.

Inputs:
    message_ids — array of integers; the folder's identifiers, in received order
    page        — integer; the page asked for, counting from 1
    page_size   — integer; how many messages make one page

Outputs:
    page_ids      — array; the identifiers of the page, newest received first
    more_exist    — boolean; whether messages exist beyond this page
    folder_empty  — boolean; whether the folder holds no messages
    message_count — integer; how many messages the folder holds
"""

from typing import Any, Dict


class CTExecutionError(RuntimeError):
    """The report cannot be paged."""


def _whole(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    ids, page, size = inputs.get("message_ids"), inputs.get("page"), inputs.get("page_size")
    if not isinstance(ids, list) or not all(_whole(i) for i in ids):
        raise CTExecutionError("CT_PURE_CHOOSE_FOLDER_PAGE_V0: message_ids must be an array of integers")
    if not _whole(page) or page < 1:
        raise CTExecutionError("CT_PURE_CHOOSE_FOLDER_PAGE_V0: page must be an integer of at least 1")
    if not _whole(size) or size < 1:
        raise CTExecutionError("CT_PURE_CHOOSE_FOLDER_PAGE_V0: page_size must be an integer of at least 1")

    newest_first = list(reversed(ids))
    start = (page - 1) * size
    return {
        "page_ids": newest_first[start:start + size],
        "more_exist": len(newest_first) > start + size,
        "folder_empty": not ids,
        "message_count": len(ids),
    }
