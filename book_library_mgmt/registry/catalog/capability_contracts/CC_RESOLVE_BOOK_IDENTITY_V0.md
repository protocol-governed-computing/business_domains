# CC_RESOLVE_BOOK_IDENTITY_V0

## 1. Intent

Resolve a registered book's identity key

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Resolve a registered book's identity key
  inputs:
    identity_key:
      type: string
      required: true
  outputs:
    target_ref:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: resolve_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: BOOK_IDENTITY_REGISTRY
    inputs:
      key_or_address: $.inputs.identity_key
    outputs:
      target_ref: $.capability_result.target_ref
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```
