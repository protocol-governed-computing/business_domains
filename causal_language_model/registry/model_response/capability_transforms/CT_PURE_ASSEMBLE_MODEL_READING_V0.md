# CT_PURE_ASSEMBLE_MODEL_READING_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Assembles exactly what the model reads and decides whether it fits what the model can read
    at once
  refusal: raises
  inputs:
    system_prompt:
      type: string
      required: true
    question:
      type: string
      required: true
    supporting_material:
      type: string
      required: true
    reading_capacity:
      type: integer
      required: true
  outputs:
    reading:
      type: object
      required: true
    reading_length:
      type: integer
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: ASSEMBLE_MODEL_READING
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_assemble_model_reading_v0
    callable: execute
```

---

## Intent

Assembles exactly what the model reads and decides whether it fits what the model can read at once
