# CC_VALIDATE_TOOL_PARAMETERS_V1

## Machine

```yaml
fqdn: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1
artifact_kind: CAPABILITY_CONTRACT
version: v1
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
supersedes: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
core:
  summary: Enforce declared parameter constraints for an authorized tool
  inputs:
    tool_name:
      type: string
      required: true
    parameters:
      type: object
      required: true
  outputs:
    rules:
      type: array
    validation_result:
      type: boolean
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: lookup_parameter_rules
    transform: capability_transforms::CT_PURE_LOOKUP_V0
    inputs:
      key: $.inputs.tool_name
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
    outputs:
      rules: $.capability_result.result
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: validate_parameters
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters: $.inputs.parameters
      rules: $.results.lookup_parameter_rules.rules
    outputs:
      validation_result: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```

---

## Intent

Enforce declared parameter constraints for an authorized tool
