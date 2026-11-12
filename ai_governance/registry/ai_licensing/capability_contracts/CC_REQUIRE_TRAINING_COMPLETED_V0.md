# CC_REQUIRE_TRAINING_COMPLETED_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Refuse to provision license unless the employee holds what the business requires
  inputs:
    training_completed:
      type: string
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: require_training_completed
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        training_completed: $.inputs.training_completed
      rules:
      - field: training_completed
        op: eq
        value: true
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse to provision license unless the employee holds what the business requires
