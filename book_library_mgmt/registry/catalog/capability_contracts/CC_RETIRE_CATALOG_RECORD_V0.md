# CC_RETIRE_CATALOG_RECORD_V0

## Header (Mandatory)

- **Artifact Code:** CC_RETIRE_CATALOG_RECORD_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Mark a record retired so it is no longer offered as current.

Retirement does not delete. The record remains for audit and is withheld from current results,
because a record retired for being obsolete would mislead if it kept appearing.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_RETIRE_CATALOG_RECORD_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Retire a catalog record without deleting it
  inputs:
    work_id:
      type: string
      required: true
  outputs:
    result_status:
      type: string
    retired_record:
      type: object
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_work_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: BIBLIOGRAPHIC_WORKS
    inputs:
      key: $.inputs.work_id
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
  - step: mark_retired
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: BIBLIOGRAPHIC_WORKS
    inputs:
      key: $.inputs.work_id
      value:
        work_id: $.inputs.work_id
        retired: true
    outputs:
      retired_record: $.capability_result.value
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
