# CC_REINSTATE_BOOK_RECORD_V0

## 1. Intent

Mark a retired book record registered again

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Mark a retired book record registered again
  inputs:
    identity_key:
      type: string
      required: true
  outputs:
    updated_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: set_record_state
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: BOOKS
    inputs:
      filter:
        identity_key: $.inputs.identity_key
      updates:
        state: REGISTERED
    outputs:
      matched_keys: $.capability_result.matched_keys
      updated_count: $.capability_result.updated_count
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```
