# CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

## Header (Mandatory)

- **Artifact Code:** CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Replace the descriptive content of a registered work's record.

The record is authoritative, so an update to a work nobody registered is refused rather than
creating one by accident.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Update the bibliographic information of a registered work
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
  - step: write_updated_record
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
