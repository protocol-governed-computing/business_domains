# CC_RESOLVE_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** CC_RESOLVE_ACTOR_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Answers which actor a contact address denotes, and reports when none does

---

## Machine

```yaml
fqdn: blockchain::CC_RESOLVE_ACTOR_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Answers which actor a contact address denotes, and reports when none does
  inputs:
    contact_address:
      type: string
      required: true
  outputs:
    value:
      type: object
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: resolve_address
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: CONTACT_ADDRESS_REGISTRY
    inputs:
      key_or_address: $.inputs.contact_address
    outputs:
      target_ref: $.capability_result.target_ref
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
  - step: read_actor
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: ACTORS
    inputs:
      key: $.inputs.contact_address
    outputs:
      value: $.capability_result.value
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
```
