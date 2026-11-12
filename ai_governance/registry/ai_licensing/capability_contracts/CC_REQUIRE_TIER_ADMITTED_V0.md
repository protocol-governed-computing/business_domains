# CC_REQUIRE_TIER_ADMITTED_V0

## Machine

```yaml
fqdn: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: Refuse a tier the business does not admit
  inputs:
    tier:
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
  - step: require_tier_admitted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.tier
      allowed_set:
      - standard
      - enterprise
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

Refuse a tier the business does not admit
