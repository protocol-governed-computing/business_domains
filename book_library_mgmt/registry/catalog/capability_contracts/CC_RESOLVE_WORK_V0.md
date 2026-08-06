# CC_RESOLVE_WORK_V0

## Header (Mandatory)

- **Artifact Code:** CC_RESOLVE_WORK_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Forms the work key, resolves it against the registry, and reads the work record it names

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_RESOLVE_WORK_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Forms the work key, resolves it against the registry, and reads the work record it names
  inputs:
    title:
      type: string
      required: true
    author:
      type: string
      required: true
  outputs:
    work_key:
      type: string
      required: true
    work_record:
      type: object
  result_status_contract:
    allowed:
    - VIOLATION
    - NOT_FOUND
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
  - step: resolve_work_claim
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: RESOLVE
    store: WORK_IDENTITY_REGISTRY
    inputs:
      key_or_address: $.results.form_work_key.work_key
    outputs:
      target_ref: $.capability_result.target_ref
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
  - step: read_work_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: READ
    store: WORKS
    inputs:
      key: $.results.form_work_key.work_key
    outputs:
      value: $.capability_result.value
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```
