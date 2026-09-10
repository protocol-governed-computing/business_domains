# CC_VALIDATE_REGISTRATION_V0

## 1. Intent

Confirms a registration carries a name and an address of the form asked for

---

## Machine

```yaml
fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: identity
core:
  summary: Confirms a registration carries a name and an address of the form asked for
  inputs:
    actor_record:
      type: object
      required: true
    registration_schema:
      type: object
      required: true
  outputs:
    violations:
      type: array
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: read_registration
    transform: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    inputs:
      record: $.inputs.actor_record
      schema: $.inputs.registration_schema
    outputs:
      violations: $.capability_result.violations
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
