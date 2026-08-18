# CC_REQUIRE_REJECTION_GROUNDS_V0

## Header (Mandatory)

- **Artifact Code:** CC_REQUIRE_REJECTION_GROUNDS_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Refuses a rejection stating no grounds, before anything is recorded

---

## Machine

```yaml
fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Refuses a rejection stating no grounds, before anything is recorded
  inputs:
    grounds_parameters:
      type: object
      required: true
    grounds_rules:
      type: array
      required: true
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
      parameters: $.inputs.grounds_parameters
      rules: $.inputs.grounds_rules
    outputs:
      valid: $.capability_result.valid
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
```
