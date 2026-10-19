# CC_REQUIRE_REJECTION_GROUNDS_V0

## Machine

```yaml
fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Refuses a rejection stating no grounds, before anything is recorded
  inputs:
    grounds:
      type: string
  outputs:
    valid:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: require_grounds_stated
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        grounds: $.inputs.grounds
      rules:
      - field: grounds
        op: not_null
      - field: grounds
        op: neq
        value: ''
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```

---

## Intent

Refuses a rejection stating no grounds, before anything is recorded
