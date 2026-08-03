# CC_REGISTER_BIBLIOGRAPHIC_WORK_V0

## Header (Mandatory)

- **Artifact Code:** CC_REGISTER_BIBLIOGRAPHIC_WORK_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Record a work as the catalog's authoritative description of it.

Registering the same work twice must not produce two records, so existence is checked before the
write and a duplicate is a governed outcome rather than an overwrite.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_REGISTER_BIBLIOGRAPHIC_WORK_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Register a bibliographic work as an authoritative record
  inputs:
    work_id:
      type: string
      required: true
    bibliographic_information:
      type: object
      required: true
  outputs:
    result_status:
      type: string
  result_status_contract:
    allowed:
    - VIOLATION
    - BACKEND_ERROR
    - ALREADY_EXISTS
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: check_existing
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: EXISTS
    store: BIBLIOGRAPHIC_WORKS
    inputs:
      key: $.inputs.work_id
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
  - step: require_absent
    transform: book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0
    inputs:
      condition: $.results.check_existing.capability_result.exists
      expected: false
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
  - step: write_work_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: BIBLIOGRAPHIC_WORKS
    inputs:
      key: $.inputs.work_id
      value:
        work_id: $.inputs.work_id
        bibliographic_information: $.inputs.bibliographic_information
        retired: false
    outputs:
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
