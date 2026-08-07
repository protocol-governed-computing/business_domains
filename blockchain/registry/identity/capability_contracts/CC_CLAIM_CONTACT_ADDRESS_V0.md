# CC_CLAIM_CONTACT_ADDRESS_V0

## Header (Mandatory)

- **Artifact Code:** CC_CLAIM_CONTACT_ADDRESS_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Claims a contact address so that two registrations of one person do not produce two actors

---

## Machine

```yaml
fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Claims a contact address so that two registrations of one person do not produce two actors
  inputs:
    actor_record:
      type: object
      required: true
    address_path:
      type: string
      required: true
    address_type:
      type: string
      required: true
  outputs:
    result:
      type: string
      required: true
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - ALREADY_EXISTS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: extract_address
    transform: capability_transforms::CT_PURE_EXTRACT_V0
    inputs:
      from: $.inputs.actor_record
      path: $.inputs.address_path
      type: $.inputs.address_type
    outputs:
      result: $.results.result
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_address
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: CONTACT_ADDRESS_REGISTRY
    inputs:
      key: $.results.result
    outputs:
      address: $.results.address
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
```
