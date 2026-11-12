# CC_FORM_ACTION_REQUEST_IDENTITY_V0

## Machine

```yaml
fqdn: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: Form a action's request identity
  inputs:
    tool_name:
      type: string
      required: true
    requesting_user_id:
      type: string
      required: true
    domain_context:
      type: string
      required: true
  outputs:
    request_identity:
      type: string
      required: true
  result_status_contract:
    allowed:
    - SUCCESS
    - VIOLATION
    on_input_failure: VIOLATION
  pipeline:
  - step: form_request_identity
    transform: capability_transforms::CT_PURE_GENERATE_ID_V0
    inputs:
      data:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
      prefix: AREQ
    outputs:
      request_identity: $.capability_result.id
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: exit
      VIOLATION: exit
```

---

## Intent

Form a action's request identity
