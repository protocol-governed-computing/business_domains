# CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1

## Machine

```yaml
fqdn: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
core:
  summary: Prepare a corrected book under the identity its correction names
  inputs:
    identity_key:
      type: string
      required: true
    updated_fields:
      type: object
      required: true
  outputs:
    updated_record:
      type: object
      required: true
    updated_identity_key:
      type: string
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
  - step: form_work_key
    transform: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    inputs:
      title: $.inputs.updated_fields.title
      author: $.inputs.updated_fields.author
    outputs:
      work_key: $.capability_result.work_key
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
        identity_key: $.results.form_updated_identity_key.updated_identity_key
        title: $.inputs.updated_fields.title
        author: $.inputs.updated_fields.author
        publication_year: $.inputs.updated_fields.publication_year
        subject: $.inputs.updated_fields.subject
        state: $.results.read_book_record.book_record.state
        work_key: $.results.form_work_key.work_key
    outputs:
      updated_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: check_corrected_record
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.results.assemble_updated_record.updated_record
      schema:
        title:
          required: true
          type: string
        author:
          required: true
          type: string
        publication_year:
          required: true
          type: integer
        subject:
          required: true
          type: array
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_incomplete_correction
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        violations: $.results.check_corrected_record.violations
        subject: $.results.assemble_updated_record.updated_record.subject
      rules:
      - field: violations
        op: eq
        value: []
      - field: subject
        op: neq
        value: []
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Prepare a corrected book under the identity its correction names
