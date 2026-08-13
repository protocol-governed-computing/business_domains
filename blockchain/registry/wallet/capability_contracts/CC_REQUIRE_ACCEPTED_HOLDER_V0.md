# CC_REQUIRE_ACCEPTED_HOLDER_V0

## Header (Mandatory)

- **Artifact Code:** CC_REQUIRE_ACCEPTED_HOLDER_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded

---

## Machine

```yaml
fqdn: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or
    recorded
  inputs:
    holder_state:
      type: string
      required: true
    states_admitting_a_wallet:
      type: array
      required: true
  outputs:
    is_accepted:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: require_holder_accepted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.holder_state
      allowed_set: $.inputs.states_admitting_a_wallet
    outputs:
      is_accepted: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
