# CC_READ_HOSTED_STATE_V0

## Machine

```yaml
fqdn: causal_language_model::CC_READ_HOSTED_STATE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Read a hosted request's trail and reduce it to the response as built
  inputs:
    user_prompt_id:
      type: string
      required: true
  outputs:
    entries:
      type: array
      required: true
    state:
      type: object
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: read_trail
    side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
    op: GET_ALL
    store: USER_PROMPT_RECORDS
    inputs:
      stream_id: $.inputs.user_prompt_id
    outputs:
      entries: $.capability_result.entries
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - BACKEND_ERROR
    on_result:
      SUCCESS: continue
      BACKEND_ERROR: exit
  - step: reduce_trail
    transform: causal_language_model::CT_PURE_READ_HOSTED_STATE_V0
    inputs:
      entries: $.results.read_trail.entries
    outputs:
      state: $.capability_result.state
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Read a hosted request's trail and reduce it to the response as built
