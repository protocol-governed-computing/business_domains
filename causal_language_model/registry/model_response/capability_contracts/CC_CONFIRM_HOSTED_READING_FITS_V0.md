# CC_CONFIRM_HOSTED_READING_FITS_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_HOSTED_READING_FITS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Refuse an offer whose reported reading size exceeds the model's capacity
  inputs:
    reported_reading_size:
      type: integer
      required: true
    reading_capacity:
      type: integer
      required: true
  outputs:
    reading_fits:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_reported_reading_fits
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        reported_reading_size: $.inputs.reported_reading_size
      rules:
      - field: reported_reading_size
        op: lte
        value: $.inputs.reading_capacity
    outputs:
      reading_fits: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse an offer whose reported reading size exceeds the model's capacity
