# CC_REGISTER_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** CC_REGISTER_ACTOR_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Writes the actor unverified after its address is claimed

---

## Machine

```yaml
fqdn: blockchain::CC_REGISTER_ACTOR_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
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
      record: $.results.actor_record
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
      value: $.results.actor_record
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
