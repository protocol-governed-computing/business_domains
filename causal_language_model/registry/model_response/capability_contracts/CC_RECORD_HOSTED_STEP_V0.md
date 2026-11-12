# CC_RECORD_HOSTED_STEP_V0

## Machine

```yaml
fqdn: causal_language_model::CC_RECORD_HOSTED_STEP_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Record an offer and the choice made from it in the request's trail
  inputs:
    user_prompt_id:
      type: string
      required: true
    host_id:
      type: string
      required: true
    fingerprint:
      type: string
      required: true
    reported_reading_size:
      type: integer
      required: true
    step:
      type: object
      required: true
  outputs:
    step_record:
      type: object
      required: true
    record_id:
      type: string
      required: true
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
  - step: assemble_step_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        user_prompt_id: $.inputs.user_prompt_id
        outcome: STEP
        host_id: $.inputs.host_id
        fingerprint: $.inputs.fingerprint
        reported_reading_size: $.inputs.reported_reading_size
        position: $.inputs.step.position
        candidates: $.inputs.step.candidates
        chosen: $.inputs.step.chosen
        stopped: $.inputs.step.stopped
        stopped_by: $.inputs.step.stopped_by
        finished: $.inputs.step.finished
        within_length: $.inputs.step.within_length
    outputs:
      step_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_step_record
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: USER_PROMPT_RECORDS
    inputs:
      record: $.results.assemble_step_record.step_record
      stream_id: $.inputs.user_prompt_id
      actor_id: $.inputs.host_id
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

Record an offer and the choice made from it in the request's trail
