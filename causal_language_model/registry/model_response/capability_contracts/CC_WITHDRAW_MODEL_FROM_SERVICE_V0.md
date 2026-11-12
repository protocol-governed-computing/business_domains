# CC_WITHDRAW_MODEL_FROM_SERVICE_V0

## Machine

```yaml
fqdn: causal_language_model::CC_WITHDRAW_MODEL_FROM_SERVICE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Close the time in service and mark the model registered
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
      SUCCESS: continue
      VIOLATION: exit
  - step: mark_registered
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: MODELS
    inputs:
      filter:
        identity_key: $.inputs.identity_key
        state: IN_SERVICE
      updates:
        state: REGISTERED
        time_in_service_id: ''
    outputs:
      matched_keys: $.capability_result.matched_keys
      updated_count: $.capability_result.updated_count
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: require_transition
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        updated_count: $.results.mark_registered.updated_count
      rules:
      - field: updated_count
        op: eq
        value: 1
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: close_time_in_service
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE
    store: TIMES_IN_SERVICE
    inputs:
      key: $.results.read_model_record.model_record.time_in_service_id
      updates:
        state: CLOSED
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Close the time in service and mark the model registered
