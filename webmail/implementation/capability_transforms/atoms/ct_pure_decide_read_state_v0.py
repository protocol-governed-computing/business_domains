"""
CT_PURE_DECIDE_READ_STATE_V0

Pure Capability Transform (Atom)

Purpose:
    Decide the change a message's read state needs. The provider holds the state; the business
    decides the change and the host carries it out. A message that already has the state asked for
    needs no change, which is an answer and not a refusal.

Inputs:
    seen        — boolean; whether the provider holds the message as read
    wanted_read — boolean; whether the message is to be read

Outputs:
    change   — string; SET_READ, SET_UNREAD or NONE
    read_now — boolean; whether the message is read once the decision is carried out
"""

from typing import Any, Dict


class CTExecutionError(RuntimeError):
    """A state that is not true or false cannot be decided on."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    seen, wanted = inputs.get("seen"), inputs.get("wanted_read")
    if not isinstance(seen, bool) or not isinstance(wanted, bool):
        raise CTExecutionError("CT_PURE_DECIDE_READ_STATE_V0: seen and wanted_read must be true or false")
    if seen == wanted:
        change = "NONE"
    else:
        change = "SET_READ" if wanted else "SET_UNREAD"
    return {"change": change, "read_now": wanted}
