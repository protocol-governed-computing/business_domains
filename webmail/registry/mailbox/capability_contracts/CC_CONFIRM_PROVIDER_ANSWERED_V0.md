# CC_CONFIRM_PROVIDER_ANSWERED_V0

## Machine

```yaml
fqdn: webmail::CC_CONFIRM_PROVIDER_ANSWERED_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Confirms the provider answered, refusing otherwise
  inputs:
    provider_answer:
      type: string
      required: true
  outputs:
    answered:
      type: boolean
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: confirm_answered
    transform: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    inputs:
      value: $.inputs.provider_answer
      allowed_set:
      - ANSWERED
    outputs:
      answered: $.capability_result.is_member
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Confirms the provider answered, refusing otherwise
