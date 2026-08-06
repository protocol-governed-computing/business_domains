# CC_APPEND_CATALOG_OPERATION_V0

## Header (Mandatory)

- **Artifact Code:** CC_APPEND_CATALOG_OPERATION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Append a durable account of a performed operation to the catalog's own trail

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Append a durable account of a performed operation to the catalog's own trail
  inputs:
    record:
      type: object
      required: true
    staff_id:
      type: string
      required: true
    operation:
      type: string
      required: true
  outputs:
    record_id:
      type: string
      required: true
    sequence_number:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: append_operation
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: CATALOG_OPERATIONS
    inputs:
      record: $.inputs.record
      stream_id: CATALOG_OPERATIONS
      actor_id: $.inputs.staff_id
    outputs:
      record_id: $.capability_result.record_id
      sequence_number: $.capability_result.sequence_number
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```
