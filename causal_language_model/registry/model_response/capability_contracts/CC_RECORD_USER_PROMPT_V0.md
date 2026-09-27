# CC_RECORD_USER_PROMPT_V0

## Machine

```yaml
fqdn: causal_language_model::CC_RECORD_USER_PROMPT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Append the user prompt record with what the model read, the rules in force and the outcome
  inputs:
    user_prompt_id:
      type: string
      required: true
    requester_id:
      type: string
      required: true
    customer_id:
      type: string
      required: true
    identity_key:
      type: string
      required: true
    kind:
      type: string
      required: true
    question:
      type: string
      required: true
    supporting_material:
      type: string
      required: true
    outcome:
      type: string
      required: true
    time_in_service_id:
      type: string
    reading:
      type: object
    rules_in_force:
      type: object
    response:
      type: string
    reason:
      type: string
  outputs:
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
  - step: assemble_user_prompt_record
    transform: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    inputs:
      fields:
        user_prompt_id: $.inputs.user_prompt_id
        requester_id: $.inputs.requester_id
        customer_id: $.inputs.customer_id
        identity_key: $.inputs.identity_key
        kind: $.inputs.kind
        question: $.inputs.question
        supporting_material: $.inputs.supporting_material
        outcome: $.inputs.outcome
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        rules_in_force: $.inputs.rules_in_force
        response: $.inputs.response
        reason: $.inputs.reason
    outputs:
      user_prompt_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_user_prompt_record
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: USER_PROMPT_RECORDS
    inputs:
      record: $.results.assemble_user_prompt_record.user_prompt_record
      stream_id: $.inputs.user_prompt_id
      actor_id: $.inputs.requester_id
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

Append the user prompt record with what the model read, the rules in force and the outcome
