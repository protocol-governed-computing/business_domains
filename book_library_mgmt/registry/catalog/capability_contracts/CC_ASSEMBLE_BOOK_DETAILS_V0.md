# CC_ASSEMBLE_BOOK_DETAILS_V0

## 1. Intent

Assembles an edition, the physical copies of it, and the record of the work it belongs to

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Assembles an edition, the physical copies of it, and the record of the work it belongs to
  inputs:
    identity_key:
      type: string
      required: true
    copy_criteria:
      type: object
      required: true
  outputs:
    work_record:
      type: object
      required: true
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
      value: $.capability_result.value
      result_status: $.result_status
      book_record: $.capability_result.value
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
  - step: form_work_key
    transform: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    inputs:
      title: $.results.read_book_record.value.title
      author: $.results.read_book_record.value.author
    outputs:
      work_key: $.capability_result.work_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: read_work_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: WORKS
    inputs:
      key: $.results.form_work_key.work_key
    outputs:
      work_record: $.capability_result.value
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      NOT_FOUND: continue
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
    transform: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
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
