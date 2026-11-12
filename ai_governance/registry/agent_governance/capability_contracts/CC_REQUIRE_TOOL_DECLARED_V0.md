# CC_REQUIRE_TOOL_DECLARED_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Refuse a tool name the business does not admit
  inputs:
    tool_name:
      type: string
      required: true
  outputs:
    is_member:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: require_tool_name_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.tool_name
      allowed_set:
      - READ_RECORD
      - PROVISION_STANDARD_LICENSE
      - PROVISION_PREMIUM_LICENSE
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

Refuse a tool name the business does not admit
