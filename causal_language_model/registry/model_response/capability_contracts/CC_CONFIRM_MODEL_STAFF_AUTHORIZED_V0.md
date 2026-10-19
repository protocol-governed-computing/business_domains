# CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Confirm the staff member is model staff
  inputs:
    staff_credentials:
      type: object
      required: true
    authorization_rules:
      type: array
      required: true
  outputs:
    is_authorized:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_authorization
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters: $.inputs.staff_credentials
      rules: $.inputs.authorization_rules
    outputs:
      is_authorized: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Confirm the staff member is model staff
