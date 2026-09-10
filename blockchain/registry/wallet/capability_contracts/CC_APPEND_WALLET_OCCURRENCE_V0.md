# CC_APPEND_WALLET_OCCURRENCE_V0

## 1. Intent

Records the moment on the wallet's trail

---

## Machine

```yaml
fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Records the moment on the wallet's trail
  inputs:
    stream_id:
      type: string
      required: true
    occurrence_fields:
      type: object
      required: true
  outputs:
    result_status:
      type: string
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_occurred_at
    side_effect: capability_side_effects::CS_CLOCK_V0
    op: NOW
    inputs: {}
    outputs:
      timestamp: $.capability_result.timestamp
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
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
    store: WALLET_OCCURRENCES
    inputs:
      stream_id: $.inputs.stream_id
      record: $.results.assemble_occurrence.record
    outputs:
      result_status: $.capability_result.result_status
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
