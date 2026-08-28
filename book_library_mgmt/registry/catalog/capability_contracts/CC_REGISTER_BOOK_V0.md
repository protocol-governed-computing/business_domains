# CC_REGISTER_BOOK_V0

## 1. Intent

Validates, assembles and writes an edition record against the work it belongs to

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_REGISTER_BOOK_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Validates, assembles and writes an edition record against the work it belongs to
  inputs:
    book_fields:
      type: object
      required: true
    identity_key:
      type: string
      required: true
    book_schema:
      type: object
      required: true
  outputs:
    book_record:
      type: object
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: form_work_key
    transform: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    inputs:
      title: $.inputs.book_fields.title
      author: $.inputs.book_fields.author
    outputs:
      work_key: $.capability_result.work_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: validate_book_fields
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.book_fields
      schema: $.inputs.book_schema
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: assemble_book_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        identity_key: $.inputs.identity_key
        title: $.inputs.book_fields.title
        author: $.inputs.book_fields.author
        publication_year: $.inputs.book_fields.publication_year
        subject: $.inputs.book_fields.subject
        state: $.inputs.book_fields.state
        work_key: $.results.form_work_key.work_key
    outputs:
      book_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_book_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: BOOKS
    inputs:
      key: $.inputs.identity_key
      value: $.results.assemble_book_record.book_record
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
