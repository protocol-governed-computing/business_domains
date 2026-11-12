# CC_REQUIRE_TIER_GRANTS_TOOL_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Refuse to govern agent action unless tier grants tool
  inputs:
    key:
      type: string
      required: true
    tool_name:
      type: string
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
  - step: look_up_tier_tools
    transform: capability_transforms::CT_PURE_LOOKUP_V0
    inputs:
      map:
        standard:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        enterprise:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        - PROVISION_PREMIUM_LICENSE
      key: $.inputs.key
    outputs:
      tier_tools: $.capability_result.result
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: require_tool_name_in_tier_tools
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.tool_name
      allowed_set: $.results.look_up_tier_tools.tier_tools
    outputs:
      is_member: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Refuse to govern agent action unless tier grants tool
