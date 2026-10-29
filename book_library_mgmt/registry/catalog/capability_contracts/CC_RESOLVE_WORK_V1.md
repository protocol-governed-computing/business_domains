# CC_RESOLVE_WORK_V1

## Machine

```yaml
fqdn: book_library_mgmt::CC_RESOLVE_WORK_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::CC_RESOLVE_WORK_V0
core:
  summary: Answer which work its identity names, and refuse when none does
  inputs:
    title:
      type: string
      required: true
    author:
      type: string
      required: true
  outputs:
    work_record:
      type: object
      required: true
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
  - step: resolve_identity
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
      work_record: $.capability_result.value
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

---

## Intent

Answer which work its identity names, and refuse when none does
