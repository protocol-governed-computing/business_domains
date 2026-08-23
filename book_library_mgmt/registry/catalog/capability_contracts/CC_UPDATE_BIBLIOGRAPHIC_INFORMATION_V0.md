# CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

## 1. Intent

Changes a registered edition's descriptive content and refuses a change that would duplicate another edition

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Changes a registered edition's descriptive content and refuses a change that would duplicate
    another edition
  inputs:
    identity_key:
      type: string
      required: true
    updated_fields:
      type: object
      required: true
  outputs:
    book_record:
      type: object
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
  - step: form_updated_identity_key
    transform: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    inputs:
      title: $.inputs.updated_fields.title
      author: $.inputs.updated_fields.author
      publication_year: $.inputs.updated_fields.publication_year
    outputs:
      updated_identity_key: $.capability_result.identity_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: compare_identity
    transform: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    inputs:
      left: $.inputs.identity_key
      right: $.results.form_updated_identity_key.updated_identity_key
    outputs:
      identity_unchanged: $.capability_result.is_equal
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: require_identity_unchanged
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        identity_unchanged: $.results.compare_identity.identity_unchanged
      rules:
      - field: identity_unchanged
        op: eq
        value: true
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: assemble_updated_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        identity_key: $.inputs.identity_key
        title: $.inputs.updated_fields.title
        author: $.inputs.updated_fields.author
        publication_year: $.inputs.updated_fields.publication_year
        subject: $.inputs.updated_fields.subject
        state: $.inputs.updated_fields.state
        work_key: $.results.read_book_record.book_record.work_key
    outputs:
      updated_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_updated_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: BOOKS
    inputs:
      key: $.inputs.identity_key
      value: $.results.assemble_updated_record.updated_record
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
