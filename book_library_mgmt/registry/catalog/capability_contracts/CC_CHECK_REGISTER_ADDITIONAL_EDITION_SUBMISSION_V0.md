# CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0

## Machine

```yaml
fqdn: book_library_mgmt::CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
core:
  summary: Refuse a request to register additional edition that lacks what it requires
  inputs:
    submission:
      type: object
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
  - step: check_book_fields
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.submission
      schema:
        title:
          type: string
          required: true
        author:
          type: string
          required: true
        publication_year:
          type: integer
          required: true
        subject:
          type: array
          required: true
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_incomplete_submission
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        book_violations: $.results.check_book_fields.violations
        subject: $.inputs.submission.subject
      rules:
      - field: book_violations
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

Refuse a request to register additional edition that lacks what it requires
