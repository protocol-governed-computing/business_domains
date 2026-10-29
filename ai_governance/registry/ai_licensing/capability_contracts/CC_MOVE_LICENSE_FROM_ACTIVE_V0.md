# CC_MOVE_LICENSE_FROM_ACTIVE_V0

## Machine

```yaml
fqdn: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Move a license from active to a state the business admits
  inputs:
    license_id:
      type: string
      required: true
    to_state:
      type: string
      required: true
  outputs:
    updated_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: read_outcome_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.to_state
      allowed_set:
      - RECLAIMED
    outputs:
      is_member: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: set_record_state
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: LICENSES
    inputs:
      filter:
        license_id: $.inputs.license_id
        state: ACTIVE
      updates:
        state: $.inputs.to_state
    outputs:
      matched_keys: $.capability_result.matched_keys
      updated_count: $.capability_result.updated_count
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

Move a license from active to a state the business admits
