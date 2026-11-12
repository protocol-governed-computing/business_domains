# CC_CHOOSE_PERMITTED_TOKEN_V0

## Machine

```yaml
fqdn: causal_language_model::CC_CHOOSE_PERMITTED_TOKEN_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Choose a permitted token from an offer under the rules in force
  inputs:
    state:
      type: object
      required: true
    candidates:
      type: array
      required: true
  outputs:
    step:
      type: object
      required: true
    text:
      type: string
      required: true
    finished:
      type: boolean
      required: true
    stopped_by:
      type: string
      required: true
    within_length:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: choose_token
    transform: causal_language_model::CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    inputs:
      state: $.inputs.state
      candidates: $.inputs.candidates
    outputs:
      step: $.capability_result.step
      text: $.capability_result.text
      finished: $.capability_result.finished
      stopped_by: $.capability_result.stopped_by
      within_length: $.capability_result.within_length
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Choose a permitted token from an offer under the rules in force
