# CC_RESOLVE_BOOK_IDENTITY_V1

## Machine

```yaml
fqdn: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0
core:
  summary: Answer which book its identity names, and refuse when none does
  inputs:
    identity_key:
      type: string
      required: true
  outputs:
    book_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
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
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: read_book_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: BOOKS
    inputs:
      key: $.inputs.identity_key
    outputs:
      book_record: $.capability_result.value
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

---

## Intent

Answer which book its identity names, and refuse when none does
