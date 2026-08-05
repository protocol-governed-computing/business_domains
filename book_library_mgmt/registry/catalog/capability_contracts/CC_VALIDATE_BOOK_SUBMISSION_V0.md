# CC_VALIDATE_BOOK_SUBMISSION_V0

## Header (Mandatory)

- **Artifact Code:** CC_VALIDATE_BOOK_SUBMISSION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Validate a book submission is complete

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_VALIDATE_BOOK_SUBMISSION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Validate a book submission is complete
  inputs:
    book_fields:
      type: object
      required: true
    book_schema:
      type: object
      required: true
    barcode:
      type: string
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
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
  - step: require_submission_complete
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        barcode: $.inputs.barcode
        subject: $.inputs.book_fields.subject
      rules:
      - field: barcode
        op: neq
        value: ''
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
