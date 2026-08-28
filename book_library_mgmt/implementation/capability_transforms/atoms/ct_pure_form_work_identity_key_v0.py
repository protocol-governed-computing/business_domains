"""
CT_PURE_FORM_WORK_IDENTITY_KEY_V0

Pure Capability Transform (Atom)

Purpose:
    Form the single key that identifies a *work*, from the two attributes the business says identify
    one: title and author.

    A work is what several editions are editions of. The previous change identified a book by title,
    author and publication year, and that identity turned out to identify an edition — editions of
    one work share a title and an author and differ by the year. So the work's key is the edition's
    key with the year removed, and the two keys are formed by two transforms rather than one with a
    switch: the edition key is reached by every catalog operation, and widening it to serve a second
    purpose would make one identity's meaning depend on how it was called.

    The catalog claims this key in a registry before it writes a work record. Unlike every other
    claim in this subdomain, a second claim on a work key is *not* a refusal — it means the work is
    already held, which is exactly the case registering a further edition exists to serve.

Normalization:
    Title and author are compared case-insensitively with surrounding and repeated whitespace
    collapsed, identically to the edition key. The same two strings must produce the same work
    whichever transform sees them first, or one edition would join a work its sibling does not.

Inputs:
    title  — string; the title the work is published under
    author — string; the author the work is published under

Outputs:
    work_key — string; `title|author`, normalized, with any literal separator escaped
"""

from typing import Any, Dict

SEPARATOR = "|"
ESCAPED = "\\|"

# The registry declares `max_key_length: 256`, and the same reasoning applies as for an edition: a
# key over that is refused rather than truncated, because a truncated key silently merges two works.
MAX_KEY_LENGTH = 256


class CTExecutionError(RuntimeError):
    """The inputs do not form a work identity."""


def _text(inputs: Dict[str, Any], field: str) -> str:
    if field not in inputs:
        raise CTExecutionError(
            f"CT_PURE_FORM_WORK_IDENTITY_KEY_V0: requires input {field!r}"
        )
    value = inputs[field]
    if not isinstance(value, str):
        raise CTExecutionError(
            f"CT_PURE_FORM_WORK_IDENTITY_KEY_V0: {field!r} must be a string, "
            f"got {type(value).__name__}"
        )
    normalized = " ".join(value.split()).casefold()
    if not normalized:
        raise CTExecutionError(
            f"CT_PURE_FORM_WORK_IDENTITY_KEY_V0: {field!r} is empty — a work carries a "
            f"title and an author"
        )
    return normalized.replace(SEPARATOR, ESCAPED)


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    work_key = SEPARATOR.join((_text(inputs, "title"), _text(inputs, "author")))
    if len(work_key) > MAX_KEY_LENGTH:
        raise CTExecutionError(
            f"CT_PURE_FORM_WORK_IDENTITY_KEY_V0: work key is {len(work_key)} characters, over the "
            f"{MAX_KEY_LENGTH} a registry key may carry — refused rather than truncated, because a "
            f"truncated key silently merges two different works into one"
        )

    return {"result_status": "SUCCESS", "work_key": work_key}
