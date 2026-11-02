"""
CT_PURE_CHOOSE_MESSAGE_TEXT_V0

Pure Capability Transform (Atom)

Purpose:
    Choose what of a message is shown. Only plain text is shown, so the first part whose kind is
    text/plain, in the order the message lists its parts, is the text. A message with no such part
    has no text that can be displayed yet. The transform sees the parts' numbers and kinds, never
    their content: the host shows the part this names.

Inputs:
    parts — array; the message's parts, each {part, kind}

Outputs:
    text_part        — string; the part number of the plain text, or empty when there is none
    text_displayable — boolean; whether the message has plain text to show
    shown_headers    — array; the headers shown with the message
"""

from typing import Any, Dict

SHOWN_HEADERS = ["from", "to", "cc", "subject", "date"]
PLAIN_TEXT = "text/plain"


class CTExecutionError(RuntimeError):
    """The parts cannot be read."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    parts = inputs.get("parts")
    if not isinstance(parts, list):
        raise CTExecutionError("CT_PURE_CHOOSE_MESSAGE_TEXT_V0: parts must be an array")
    for p in parts:
        if not (isinstance(p, dict) and isinstance(p.get("part"), str) and isinstance(p.get("kind"), str)):
            raise CTExecutionError("CT_PURE_CHOOSE_MESSAGE_TEXT_V0: every part must carry a part number and a kind")

    text = next((p["part"] for p in parts if p["kind"].strip().lower() == PLAIN_TEXT), "")
    return {"text_part": text, "text_displayable": bool(text), "shown_headers": list(SHOWN_HEADERS)}
