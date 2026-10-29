# CC_REKEY_BOOK_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_REKEY_BOOK_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Move a book to its new identity, with its physical copies
  inputs:
    identity_key:
      type: string
      required: true
    updated_identity_key:
      type: string
      required: true
    updated_record:
      type: object
      required: true
  outputs:
    updated_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - BACKEND_ERROR
    - NOT_FOUND
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: write_book_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: BOOKS
    inputs:
      key: $.inputs.updated_identity_key
      value: $.inputs.updated_record
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
  - step: move_copy_records
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: PHYSICAL_COPIES
    inputs:
      filter:
        identity_key: $.inputs.identity_key
      updates:
        identity_key: $.inputs.updated_identity_key
    outputs:
      matched_keys: $.capability_result.matched_keys
      updated_count: $.capability_result.updated_count
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: continue
      BACKEND_ERROR: exit
  - step: remove_old_book_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: DELETE
    store: BOOKS
    inputs:
      key: $.inputs.identity_key
    outputs:
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
  - step: release_old_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: DEREGISTER
    store: BOOK_IDENTITY_REGISTRY
    inputs:
      key_or_address: $.inputs.identity_key
    outputs:
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

Move a book to its new identity, with its physical copies
