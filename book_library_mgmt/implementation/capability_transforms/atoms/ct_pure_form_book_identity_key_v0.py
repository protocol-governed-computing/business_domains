"""
CT_PURE_FORM_BOOK_IDENTITY_KEY_V0

Pure Capability Transform (Atom)

Purpose:
    Form the single key that identifies a book, from the three attributes the business says identify
    one: title, author and publication year.

    The catalog claims this key in a registry before it writes a book record, and a second claim on
    the same key fails with ALREADY_EXISTS. That is how duplicate prevention becomes atomic: the
    uniqueness guarantee belongs to the registry, and forming the key from three attributes belongs
    here, because a registry keys on one value and the business identifies a book by three.

    The key is readable rather than hashed. A store whose keys are digests can be audited only by
    re-deriving every key, and this record is the library's authoritative statement of what it holds.

Normalization:
    Title and author are compared case-insensitively with surrounding and repeated whitespace
    collapsed, so that `"The  Odyssey"` and `"the odyssey"` claim the same key. This is a stated
    business fact, not an interpretation: case and spacing do not change which book is meant, so they
    must not produce two records. A key that treated those two as different books would reintroduce
    duplicate entries at the one point that exists to prevent them.

Inputs:
    title            — string; the title the book is published under
    author           — string; the author the book is published under
    publication_year — integer; the year this edition was published

Outputs:
    identity_key — string; `title|author|year`, normalized, with any literal separator escaped
"""

from typing import Any, Dict

SEPARATOR = "|"
ESCAPED = "\\|"

# The registry declares `max_key_length: 256`. A key over that is refused rather than truncated:
# truncation is silent collision, and collision here means two different books sharing one record.
MAX_KEY_LENGTH = 256


class CTExecutionError(RuntimeError):
    """The inputs do not form a book identity."""


def _text(inputs: Dict[str, Any], field: str) -> str:
    value = inputs.get(field)
    if field not in inputs:
        raise CTExecutionError(
            f"CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: requires input {field!r}"
        )
    if not isinstance(value, str):
        raise CTExecutionError(
            f"CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: {field!r} must be a string, "
            f"got {type(value).__name__}"
        )
    normalized = " ".join(value.split()).casefold()
    if not normalized:
        raise CTExecutionError(
            f"CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: {field!r} is empty — a book carries a "
            f"title and an author"
        )
    return normalized.replace(SEPARATOR, ESCAPED)


def _year(inputs: Dict[str, Any]) -> int:
    if "publication_year" not in inputs:
        raise CTExecutionError(
            "CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: requires input 'publication_year'"
        )
    value = inputs["publication_year"]
    # `bool` is a subclass of `int`, and `True` is not a year.
    if isinstance(value, bool) or not isinstance(value, int):
        raise CTExecutionError(
            "CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: 'publication_year' must be an integer, "
            f"got {type(value).__name__}"
        )
    return value


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    title = _text(inputs, "title")
    author = _text(inputs, "author")
    year = _year(inputs)

    identity_key = SEPARATOR.join((title, author, str(year)))
    if len(identity_key) > MAX_KEY_LENGTH:
        raise CTExecutionError(
            f"CT_PURE_FORM_BOOK_IDENTITY_KEY_V0: identity key is {len(identity_key)} characters, "
            f"over the {MAX_KEY_LENGTH} a registry key may carry — refused rather than truncated, "
            f"because a truncated key is a silent collision between two different books"
        )

    return {"result_status": "SUCCESS", "identity_key": identity_key}
