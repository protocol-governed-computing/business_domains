# CC_ADMIT_USER_PROMPT_V0

## Machine

```yaml
fqdn: causal_language_model::CC_ADMIT_USER_PROMPT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Refuse a user prompt before the model sees it when its model is not registered or not in service
  inputs:
    identity_key:
      type: string
      required: true
  outputs:
    model_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_model_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: MODELS
    inputs:
      key: $.inputs.identity_key
    outputs:
      model_record: $.capability_result.value
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: require_in_service
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        state: $.results.read_model_record.model_record.state
      rules:
      - field: state
        op: eq
        value: IN_SERVICE
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

Refuse a user prompt before the model sees it when its model is not registered or not in service
