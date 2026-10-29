# CC_MOVE_ACTOR_FROM_UNVERIFIED_V0

## Machine

```yaml
fqdn: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Move a actor from unverified to a state the business admits
  inputs:
    contact_address:
      type: string
      required: true
    to_state:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
    grounds:
      type: string
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
  - step: compare_verifying_authority_to_actor
    transform: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    inputs:
      left: $.inputs.verifying_authority
      right: $.inputs.contact_address
    outputs:
      is_self: $.capability_result.is_equal
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_self_decision
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        is_self: $.results.compare_verifying_authority_to_actor.is_self
      rules:
      - field: is_self
        op: eq
        value: false
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: read_outcome_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.to_state
      allowed_set:
      - ACCEPTED
      - REJECTED
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
    store: ACTORS
    inputs:
      filter:
        contact_address: $.inputs.contact_address
        state: UNVERIFIED
      updates:
        state: $.inputs.to_state
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
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

Move a actor from unverified to a state the business admits
