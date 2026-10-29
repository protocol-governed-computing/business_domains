# CC_REQUIRE_ACCEPTED_ACTOR_V0

## Machine

```yaml
fqdn: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Refuse a wallet for a actor who is not accepted
  inputs:
    state:
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
  - step: require_actor_accepted
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.state
      allowed_set:
      - ACCEPTED
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

Refuse a wallet for a actor who is not accepted
