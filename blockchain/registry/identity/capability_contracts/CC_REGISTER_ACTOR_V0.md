# CC_REGISTER_ACTOR_V0

## 1. Intent

Writes the actor unverified after its address is claimed

---

## Machine

```yaml
fqdn: blockchain::CC_REGISTER_ACTOR_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Writes the actor unverified after its address is claimed
  inputs:
    actor_fields:
      type: object
      required: true
    contact_address:
      type: string
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
  - step: assemble_actor
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.actor_fields
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_actor
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: ACTORS
    inputs:
      key: $.inputs.contact_address
      value: $.results.assemble_actor.record
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
