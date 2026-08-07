# CC_RECORD_VERIFICATION_DECISION_V0

## Header (Mandatory)

- **Artifact Code:** CC_RECORD_VERIFICATION_DECISION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Refuses every declared refusal and moves the actor to its decided state

---

## Machine

```yaml
fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Refuses every declared refusal and moves the actor to its decided state
  inputs:
    current_state:
      type: string
      required: true
    states_admitting_a_decision:
      type: array
      required: true
    decision:
      type: string
      required: true
    admitted_outcomes:
      type: array
      required: true
    verifying_authority:
      type: string
      required: true
    contact_address:
      type: string
      required: true
    decided_actor_fields:
      type: object
      required: true
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
      allowed_set: $.inputs.states_admitting_a_decision
    outputs:
      is_member: $.results.state_admits_decision
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
      allowed_set: $.inputs.admitted_outcomes
    outputs:
      is_member: $.results.outcome_admitted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_self_verification
    transform: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    inputs:
      left: $.inputs.verifying_authority
      right: $.inputs.contact_address
    outputs:
      is_equal: $.results.authority_is_the_subject
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: assemble_decided_actor
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.decided_actor_fields
    outputs:
      record: $.results.decided_actor_record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_decided_actor
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: ACTORS
    inputs:
      key: $.inputs.contact_address
      value: $.results.decided_actor_record
    outputs:
      result_status: $.results.write_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
```
