# CC_ASSEMBLE_BOOK_DETAILS_V0

## Header (Mandatory)

- **Artifact Code:** CC_ASSEMBLE_BOOK_DETAILS_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Assemble a work's record together with the copies belonging to it.

Complete details are the work and its copies read together; neither store holds the whole answer,
which is why this is a composition rather than a single read.

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_ASSEMBLE_BOOK_DETAILS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0

core:
  summary: Assemble a work with the copies belonging to it

  inputs:
    work_id:
      type: string
      required: true

  outputs:
    result_status:
      type: string
    book_details:
      type: object
    copies:
      type: array

  result_status_contract:
    allowed: [SUCCESS, NOT_FOUND, VIOLATION, BACKEND_ERROR]
    on_input_failure: VIOLATION

  pipeline:
    - step: read_work_record
      side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
      op: READ
      store: BIBLIOGRAPHIC_WORKS
      inputs:
        key: $.inputs.work_id
      outputs:
        book_details: $.capability_result.value
        result_status: $.result_status
      result_surface: [SUCCESS, NOT_FOUND, VIOLATION, BACKEND_ERROR]
      on_result:
        SUCCESS: continue
        NOT_FOUND: exit
        VIOLATION: exit
        BACKEND_ERROR: exit

    - step: read_copies
      side_effect: capability_side_effects::CS_MUTABLE_JSON_V0
      op: LIST
      store: PHYSICAL_COPIES
      inputs:
        filter:
          work_id: $.inputs.work_id
      outputs:
        copies: $.capability_result.keys
        result_status: $.result_status
      result_surface: [SUCCESS, VIOLATION, BACKEND_ERROR]
      on_result:
        SUCCESS: exit
        VIOLATION: exit
        BACKEND_ERROR: exit

```
