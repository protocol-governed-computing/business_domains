# EV_AGENT_ACTION_AUTHORIZED_V1

## Machine

```yaml
fqdn: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
artifact_kind: EVENT
version: v1
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: agent_governance
supersedes: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
core:
  summary: A agent action authorized
  description: A agent action authorized
  subdomain: agent_governance
  schema:
    tool_name:
      type: string
      required: true
    requesting_user_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A agent action authorized
