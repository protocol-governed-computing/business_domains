# CC_APPEND_MODEL_OPERATION_V0

## Machine

```yaml
fqdn: causal_language_model::CC_APPEND_MODEL_OPERATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Append a durable account of a performed operation to the subdomain's own trail
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
    store: MODEL_OPERATIONS
    inputs:
      record: $.inputs.record
      stream_id: MODEL_OPERATIONS
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

---

## Intent

Append a durable account of a performed operation to the subdomain's own trail
