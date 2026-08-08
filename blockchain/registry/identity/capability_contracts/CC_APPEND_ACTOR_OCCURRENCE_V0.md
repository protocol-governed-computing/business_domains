# CC_APPEND_ACTOR_OCCURRENCE_V0

## Header (Mandatory)

- **Artifact Code:** CC_APPEND_ACTOR_OCCURRENCE_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Appends one occurrence to the trail

---

## Machine

```yaml
fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Appends one occurrence to the trail
  inputs:
    occurrence_fields:
      type: object
      required: true
    stream_id:
      type: string
      required: true
    contact_address:
      type: string
      required: true
  outputs:
    sequence_number:
      type: integer
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: assemble_occurrence
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields: $.inputs.occurrence_fields
    outputs:
      record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_occurrence
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: ACTOR_OCCURRENCES
    inputs:
      record: $.results.assemble_occurrence.record
      stream_id: $.inputs.stream_id
      actor_id: $.inputs.contact_address
    outputs:
      sequence_number: $.capability_result.sequence_number
    result_surface:
    - SUCCESS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
```
