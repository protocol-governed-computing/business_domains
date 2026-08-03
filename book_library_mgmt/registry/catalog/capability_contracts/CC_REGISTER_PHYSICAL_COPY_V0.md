# CC_REGISTER_PHYSICAL_COPY_V0

## Header (Mandatory)

- **Artifact Code:** CC_REGISTER_PHYSICAL_COPY_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Record a copy against exactly one bibliographic work.

The one-work rule is the invariant the business states most firmly, so the work is confirmed to
exist before the copy is written; a copy naming no registered work is refused.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_REGISTER_PHYSICAL_COPY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Register a physical copy against exactly one work
  inputs:
    copy_id:
      type: string
      required: true
    work_id:
      type: string
      required: true
  outputs:
    result_status:
      type: string
  result_status_contract:
    allowed:
    - VIOLATION
    - BACKEND_ERROR
    - NOT_FOUND
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_work_registered
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: EXISTS
    store: BIBLIOGRAPHIC_WORKS
    inputs:
      key: $.inputs.work_id
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
  - step: require_work_registered
    transform: book_library_mgmt::CT_PURE_REQUIRE_CONDITION_V0
    inputs:
      condition: $.results.confirm_work_registered.capability_result.exists
      expected: true
    outputs:
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - NOT_FOUND
    - VIOLATION
    on_result:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
  - step: write_copy_record
    side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
    op: WRITE
    store: PHYSICAL_COPIES
    inputs:
      key: $.inputs.copy_id
      value:
        copy_id: $.inputs.copy_id
        work_id: $.inputs.work_id
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
