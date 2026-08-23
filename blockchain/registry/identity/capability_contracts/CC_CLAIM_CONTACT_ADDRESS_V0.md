# CC_CLAIM_CONTACT_ADDRESS_V0

## 1. Intent

Claims a contact address so that two registrations of one person do not produce two actors

---

## Machine

```yaml
fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
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
      result: $.capability_result.result
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
      key: $.results.extract_address.result
      target_cs: CS_MUTABLE_JSON_V0
      target_ref: ACTORS
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
```
