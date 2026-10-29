# CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0

## Machine

```yaml
fqdn: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Refuse a request to register actor that lacks what it requires
  inputs:
    submission:
      type: object
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: check_actor_fields
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.submission
      schema:
        name:
          type: string
          required: true
        contact_address:
          type: string
          required: true
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_incomplete_submission
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        actor_violations: $.results.check_actor_fields.violations
      rules:
      - field: actor_violations
        op: eq
        value: []
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

Refuse a request to register actor that lacks what it requires
