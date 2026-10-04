"""
CT_PURE_FORM_MODEL_IDENTITY_KEY_V0

Pure Capability Transform (Atom)

Purpose:
    Form the single key that identifies a model, from the two things the business says identify one:
    its description and its training fingerprint. Two registrations whose descriptions and
    fingerprints both match are the same model, and model_response claims this key in a registry before
    it writes a model record, so a second registration of the same model fails with ALREADY_EXISTS.

    The key is readable rather than hashed, for the reason the catalog gives: a store whose keys are
    digests can be audited only by re-deriving every key.

Form:
    The description as canonical JSON — keys sorted, no whitespace — then `|`, then the fingerprint
    with surrounding whitespace removed and any literal `|` escaped. Canonical JSON makes two
    descriptions that differ only in key order or spacing the same description, which they are.

Inputs:
    description — object; how the model is built
    fingerprint — string; the training fingerprint, the provider's claim

Outputs:
    identity_key — string
"""

import json
from typing import Any, Dict

SEPARATOR = "|"
ESCAPED = "\\|"

# The registry declares `max_key_length: 256`. A longer key is refused rather than truncated:
# truncation is a silent collision between two different models.
MAX_KEY_LENGTH = 256


class CTExecutionError(RuntimeError):
    """The inputs do not form a model identity."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("description", "fingerprint"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_FORM_MODEL_IDENTITY_KEY_V0: requires input {field!r}")

    description = inputs["description"]
    if not isinstance(description, dict) or not description:
        raise CTExecutionError(
            "CT_PURE_FORM_MODEL_IDENTITY_KEY_V0: 'description' must be a non-empty object"
        )
    fingerprint = inputs["fingerprint"]
    if not isinstance(fingerprint, str) or not fingerprint.strip():
        raise CTExecutionError(
            "CT_PURE_FORM_MODEL_IDENTITY_KEY_V0: 'fingerprint' is empty — a model is registered "
            "with the fingerprint its provider supplied"
        )

    canonical = json.dumps(description, sort_keys=True, separators=(",", ":"))
    identity_key = canonical + SEPARATOR + fingerprint.strip().replace(SEPARATOR, ESCAPED)
    if len(identity_key) > MAX_KEY_LENGTH:
        raise CTExecutionError(
            f"CT_PURE_FORM_MODEL_IDENTITY_KEY_V0: identity key is {len(identity_key)} characters, "
            f"over the {MAX_KEY_LENGTH} a registry key may carry — refused rather than truncated"
        )
    return {"identity_key": identity_key}
