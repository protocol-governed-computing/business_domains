# CC_CLAIM_USER_PROMPT_IDENTITY_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Claim a user prompt's identity so a second submission under it is refused
  inputs:
    user_prompt_id:
      type: string
      required: true
  outputs:
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: claim_user_prompt
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: USER_PROMPT_REGISTRY
    inputs:
      key: $.inputs.user_prompt_id
      target_cs: CS_APPENDONLY_JSONL_V0
      target_ref: USER_PROMPT_RECORDS
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```

---

## Intent

Claim a user prompt's identity so a second submission under it is refused
