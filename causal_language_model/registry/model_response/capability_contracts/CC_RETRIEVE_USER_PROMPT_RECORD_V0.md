# CC_RETRIEVE_USER_PROMPT_RECORD_V0

## Machine

```yaml
fqdn: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Read the record of a user prompt
  inputs:
    user_prompt_id:
      type: string
      required: true
  outputs:
    user_prompt_record:
      type: array
      required: true
  result_status_contract:
    allowed:
    - BACKEND_ERROR
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: read_user_prompt_entries
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
  - step: select_user_prompt_record
    transform: capability_transforms::CT_PURE_FILTER_RECORDS_V0
    inputs:
      source: $.results.read_user_prompt_entries.entries
      filter:
        stream_id: $.inputs.user_prompt_id
    outputs:
      user_prompt_record: $.capability_result.extracted
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Read the record of a user prompt
