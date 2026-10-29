# CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Refuse to govern agent action unless parameters satisfy rules
  inputs:
    key:
      type: string
      required: true
    parameters:
      type: object
      required: true
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: look_up_tool_rules
    transform: capability_transforms::CT_PURE_LOOKUP_V0
    inputs:
      map:
        READ_RECORD:
        - field: record_type
          op: in
          allowed:
          - license_pool
          - user_profile
        - field: id
          op: not_null
        PROVISION_STANDARD_LICENSE:
        - field: tier
          op: eq
          value: standard
        - field: quantity
          op: lte
          value: 100
        PROVISION_PREMIUM_LICENSE:
        - field: tier
          op: eq
          value: premium
        - field: quantity
          op: lte
          value: 50
      key: $.inputs.key
    outputs:
      tool_rules: $.capability_result.result
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: require_parameters_hold
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters: $.inputs.parameters
      rules: $.results.look_up_tool_rules.tool_rules
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse to govern agent action unless parameters satisfy rules
