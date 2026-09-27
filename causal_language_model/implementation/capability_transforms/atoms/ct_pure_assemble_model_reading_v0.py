"""
CT_PURE_ASSEMBLE_MODEL_READING_V0

Pure Capability Transform (Atom)

Purpose:
    Assemble exactly what the model reads — the system prompt, the question and the supporting
    material, and nothing else — and refuse it when it is longer than the model can read at once.
    The reading is returned whole, because the user prompt record keeps what the model read, not a
    summary of it.

Length:
    Counted in words: whitespace-separated, across all three parts. That is exact for the test model
    and a simulation for a real one, whose capacity is in tokens; the design says so.

Inputs:
    system_prompt       — string
    question            — string
    supporting_material — string
    reading_capacity    — integer; how many words the model can read at once

Outputs:
    reading        — object; the three parts, as the model reads them
    reading_length — integer; how many words they are
"""

from typing import Any, Dict

PARTS = ("system_prompt", "question", "supporting_material")


class CTExecutionError(RuntimeError):
    """What the model would read is longer than it can read at once."""


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in (*PARTS, "reading_capacity"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_ASSEMBLE_MODEL_READING_V0: requires input {field!r}")
    for field in PARTS:
        if not isinstance(inputs[field], str):
            raise CTExecutionError(f"CT_PURE_ASSEMBLE_MODEL_READING_V0: {field!r} must be a string")
    capacity = inputs["reading_capacity"]
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 1:
        raise CTExecutionError("CT_PURE_ASSEMBLE_MODEL_READING_V0: 'reading_capacity' must be a positive integer")

    reading = {field: inputs[field] for field in PARTS}
    length = sum(len(inputs[field].split()) for field in PARTS)
    if length > capacity:
        raise CTExecutionError(
            f"CT_PURE_ASSEMBLE_MODEL_READING_V0: what the model would read is {length} words, "
            f"longer than the {capacity} it can read at once"
        )
    return {"reading": reading, "reading_length": length}
