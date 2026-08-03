# CC_CONFIRM_STAFF_AUTHORIZED_V0

## Header (Mandatory)

- **Artifact Code:** CC_CONFIRM_STAFF_AUTHORIZED_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Confirm the staff member may perform catalog operations.

The catalog reads authorization; it never grants it. Deciding who is authorized belongs to the
patron subdomain and is deferred to a future change request.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Confirm the staff member is authorized
  inputs:
    staff_id:
      type: string
      required: true
  outputs:
    result_status:
      type: string
    authorized:
      type: boolean
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    - DENIED
    on_input_failure: VIOLATION
  pipeline:
  - step: read_authorization
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: CATALOG_STAFF
    inputs:
      key: $.inputs.staff_id
    outputs:
      staff_record: $.capability_result.value
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
  - step: require_authorized
    transform: book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0
    inputs:
      condition: $.results.read_authorization.capability_result.value.authorized
      expected: true
    outputs:
      authorized: $.capability_result.condition_held
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - DENIED
    - VIOLATION
    on_result:
      SUCCESS: exit
      DENIED: exit
      VIOLATION: exit
```
