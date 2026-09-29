# CC_VALIDATE_REGISTRATION_V0

## Machine

```yaml
fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Refuses a registration lacking the person's name or their address
  inputs:
    actor_record:
      type: object
      required: true
  outputs:
    violations:
      type: array
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    on_input_failure: VIOLATION
  pipeline:
  - step: read_registration
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.actor_record
      schema:
        name:
          type: string
          required: true
        contact_address:
          type: string
          required: true
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: refuse_incomplete_registration
    transform: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    inputs:
      parameters:
        violations: $.results.read_registration.violations
      rules:
      - field: violations
        op: eq
        value: []
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

Refuses a registration lacking the person's name or their address
