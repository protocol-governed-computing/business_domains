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
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
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
    self_check_parameters:
      type: object
      required: true
    self_check_rules:
      type: array
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
      allowed_set: $.inputs.admitted_outcomes
    outputs:
      is_member: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_self_verification
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters: $.inputs.self_check_parameters
      rules: $.inputs.self_check_rules
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
      fields: $.inputs.decided_actor_fields
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
