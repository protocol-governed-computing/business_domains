# CC_CONFIRM_READING_FITS_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_READING_FITS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Assemble exactly what the model reads and refuse it before the model sees it when it is too
    long
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
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_reading
    transform: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    inputs:
      system_prompt: $.inputs.system_prompt
      question: $.inputs.question
      supporting_material: $.inputs.supporting_material
      reading_capacity: $.inputs.reading_capacity
    outputs:
      reading: $.capability_result.reading
      reading_length: $.capability_result.reading_length
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Assemble exactly what the model reads and refuse it before the model sees it when it is too long
