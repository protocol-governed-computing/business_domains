# IN_AGENT_ACTION_REQUESTED_V1

## Machine

```yaml
fqdn: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
artifact_kind: INTENT
version: v1
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: agent_governance
supersedes: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
core:
  summary: A request to govern agent action
  workflow: WF_GOVERN_AGENT_ACTION_V1
  inputs:
    tool_name:
      type: string
      required: true
    parameters:
      type: object
      required: true
    requesting_user_id:
      type: string
      required: true
    domain_context:
      type: string
      required: true
    request_id:
      type: string
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to govern agent action
