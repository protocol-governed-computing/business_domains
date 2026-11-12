# CC_MOVE_BOOK_FROM_RETIRED_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_MOVE_BOOK_FROM_RETIRED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Move a book from retired to a state the business admits
  inputs:
    identity_key:
      type: string
      required: true
    to_state:
      type: string
      required: true
  outputs:
    updated_count:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: read_outcome_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.to_state
      allowed_set:
      - REGISTERED
    outputs:
      is_member: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: set_record_state
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: UPDATE_WHERE
    store: BOOKS
    inputs:
      filter:
        identity_key: $.inputs.identity_key
        state: RETIRED
      updates:
        state: $.inputs.to_state
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

---

## Intent

Move a book from retired to a state the business admits
