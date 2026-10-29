# CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0

## Machine

```yaml
fqdn: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Claim a actor's contact address
  inputs:
    contact_address:
      type: string
      required: true
  outputs:
    contact_address:
      type: string
      required: true
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: claim_contact_address
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: CONTACT_ADDRESS_REGISTRY
    inputs:
      key: $.inputs.contact_address
      target_cs: capability_side_effects::CS_MUTABLE_JSON_V0
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
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claim a actor's contact address
