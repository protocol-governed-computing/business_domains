# CC_ASSEMBLE_BOOK_DETAILS_V0

## Header (Mandatory)

- **Artifact Code:** CC_ASSEMBLE_BOOK_DETAILS_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Assemble a book's record with the copies recorded against it

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Assemble a book's record with the copies recorded against it
  inputs:
    identity_key:
      type: string
      required: true
    copy_criteria:
      type: object
      required: true
  outputs:
    book_record:
      type: object
      required: true
    copies_held:
      type: array
      required: true
  result_status_contract:
    allowed:
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
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
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: select_copy_records
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: SELECT
    store: PHYSICAL_COPIES
    inputs: {}
    outputs:
      records: $.capability_result.records
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: select_copies_of_book
    transform: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    inputs:
      source: $.results.select_copy_records.records
      filter: $.inputs.copy_criteria
    outputs:
      copies_held: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```
