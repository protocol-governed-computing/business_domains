# CC_OPEN_HOSTED_RECORD_V0

## Machine

```yaml
fqdn: causal_language_model::CC_OPEN_HOSTED_RECORD_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Form the rules in force and open the record of a hosted request
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
    time_in_service_id:
      type: string
      required: true
    reading:
      type: object
      required: true
    response_rules:
      type: object
      required: true
    account_numbers:
      type: array
      required: true
    seed:
      type: integer
      required: true
    fingerprint:
      type: string
      required: true
    reading_capacity:
      type: integer
      required: true
    maximum_response_length:
      type: integer
      required: true
  outputs:
    rules_in_force:
      type: object
      required: true
    positions:
      type: array
      required: true
    opening_record:
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
  - step: form_rules_in_force
    transform: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    inputs:
      response_rules: $.inputs.response_rules
      account_numbers: $.inputs.account_numbers
      seed: $.inputs.seed
    outputs:
      rules_in_force: $.capability_result.rules_in_force
      positions: $.capability_result.positions
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: assemble_opening_record
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
        time_in_service_id: $.inputs.time_in_service_id
        reading: $.inputs.reading
        fingerprint: $.inputs.fingerprint
        reading_capacity: $.inputs.reading_capacity
        maximum_response_length: $.inputs.maximum_response_length
        rules_in_force: $.results.form_rules_in_force.rules_in_force
        ground_numbers: $.inputs.response_rules.ground_numbers
        longest_response: $.inputs.response_rules.longest_response
        outcome: WRITING
    outputs:
      opening_record: $.capability_result.record
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: append_opening_record
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: APPEND
    store: USER_PROMPT_RECORDS
    inputs:
      record: $.results.assemble_opening_record.opening_record
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

Form the rules in force and open the record of a hosted request
