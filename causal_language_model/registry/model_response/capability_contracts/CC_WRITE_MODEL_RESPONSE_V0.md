# CC_WRITE_MODEL_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: model_response
core:
  summary: Form the rules in force and write the response word by word under them
  inputs:
    response_rules:
      type: object
      required: true
    account_numbers:
      type: array
      required: true
    seed:
      type: integer
      required: true
    reading:
      type: object
      required: true
  outputs:
    rules_in_force:
      type: object
      required: true
    written_response:
      type: object
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
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
  - step: write_response
    transform: causal_language_model::CT_WRITE_RESPONSE_V0
    inputs:
      reading: $.inputs.reading
      rules_in_force: $.results.form_rules_in_force.rules_in_force
      positions: $.results.form_rules_in_force.positions
    outputs:
      written_response: $.capability_result.result
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Form the rules in force and write the response word by word under them
