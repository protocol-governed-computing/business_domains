# CC_CLAIM_WORK_IDENTITY_V0

## Header (Mandatory)

- **Artifact Code:** CC_CLAIM_WORK_IDENTITY_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Forms the work key, claims it, and writes the work record when the claim is new

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_CLAIM_WORK_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Forms the work key, claims it, and writes the work record when the claim is new
  inputs:
    title:
      type: string
      required: true
    author:
      type: string
      required: true
    work_fields:
      type: object
      required: true
  outputs:
    work_key:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - ALREADY_EXISTS
    - BACKEND_ERROR
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: form_work_key
    transform: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
    inputs:
      title: $.inputs.title
      author: $.inputs.author
    outputs:
      work_key: $.capability_result.work_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_work
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: WORK_IDENTITY_REGISTRY
    inputs:
      key: $.results.form_work_key.work_key
      target_cs: CS_MUTABLE_JSON_V0
      target_ref: WORKS
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: assemble_work_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.work_fields
    outputs:
      work_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: write_work_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: WORKS
    inputs:
      key: $.results.form_work_key.work_key
      value: $.results.assemble_work_record.work_record
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
