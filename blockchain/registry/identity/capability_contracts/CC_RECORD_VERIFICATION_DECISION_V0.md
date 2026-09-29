# CC_RECORD_VERIFICATION_DECISION_V0

## Machine

```yaml
fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Refuses a decision about a person not unverified, a decision other than an acceptance or a
    rejection, or an authority deciding about themselves, and records the decision it checked
  inputs:
    current_state:
      type: string
      required: true
    decision:
      type: string
      required: true
    verifying_authority:
      type: string
      required: true
    contact_address:
      type: string
      required: true
    grounds:
      type: string
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: read_state_admits_decision
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.current_state
      allowed_set:
      - UNVERIFIED
    outputs:
      is_member: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: read_outcome_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.decision
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
  - step: compare_authority_to_person
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
        is_self: $.results.compare_authority_to_person.is_self
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
  - step: assemble_decided_actor
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        contact_address: $.inputs.contact_address
        state: $.inputs.decision
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_decided_actor
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE
    store: ACTORS
    inputs:
      key: $.inputs.contact_address
      updates: $.results.assemble_decided_actor.record
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked
