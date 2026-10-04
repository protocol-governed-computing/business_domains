# CC_PLACE_MODEL_IN_SERVICE_V0

## Machine

```yaml
fqdn: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Open a time in service with its ceiling, system prompt and response rules, and mark the model
    in service
  inputs:
    identity_key:
      type: string
      required: true
    time_in_service_id:
      type: string
      required: true
    ceiling:
      type: string
      required: true
    system_prompt:
      type: string
      required: true
    response_rules:
      type: object
      required: true
  outputs:
    time_in_service:
      type: object
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - ALREADY_EXISTS
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
  - step: require_registered
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        state: $.results.read_model_record.model_record.state
      rules:
      - field: state
        op: eq
        value: REGISTERED
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: confirm_ceiling_declared
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.ceiling
      allowed_set:
      - public
      - internal
      - confidential
      - restricted
    outputs:
      ceiling_declared: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_time_in_service
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: TIME_IN_SERVICE_REGISTRY
    inputs:
      key: $.inputs.time_in_service_id
      target_cs: CS_MUTABLE_JSON_V0
      target_ref: TIMES_IN_SERVICE
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: mark_in_service
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: MODELS
    inputs:
      filter:
        identity_key: $.inputs.identity_key
        state: REGISTERED
      updates:
        state: IN_SERVICE
        time_in_service_id: $.inputs.time_in_service_id
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
        updated_count: $.results.mark_in_service.updated_count
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
  - step: assemble_time_in_service
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        time_in_service_id: $.inputs.time_in_service_id
        identity_key: $.inputs.identity_key
        ceiling: $.inputs.ceiling
        system_prompt: $.inputs.system_prompt
        response_rules: $.inputs.response_rules
        state: OPEN
    outputs:
      time_in_service: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_time_in_service
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: TIMES_IN_SERVICE
    inputs:
      key: $.inputs.time_in_service_id
      value: $.results.assemble_time_in_service.time_in_service
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

Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
