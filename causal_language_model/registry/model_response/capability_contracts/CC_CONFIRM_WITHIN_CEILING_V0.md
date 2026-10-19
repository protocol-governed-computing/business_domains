# CC_CONFIRM_WITHIN_CEILING_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Refuse a user prompt before the model sees it when it states a kind more sensitive than the
    ceiling
  inputs:
    time_in_service_id:
      type: string
      required: true
    kind:
      type: string
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
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_time_in_service
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: TIMES_IN_SERVICE
    inputs:
      key: $.inputs.time_in_service_id
    outputs:
      time_in_service: $.capability_result.value
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
  - step: confirm_kind_declared
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.kind
      allowed_set:
      - public
      - internal
      - confidential
      - restricted
    outputs:
      kind_declared: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: compare_sensitivity
    transform: causal_language_model::CT_PURE_COMPARE_SENSITIVITY_V0
    inputs:
      kind: $.inputs.kind
      ceiling: $.results.read_time_in_service.time_in_service.ceiling
      kinds:
      - public
      - internal
      - confidential
      - restricted
    outputs:
      within_ceiling: $.capability_result.within_ceiling
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling
