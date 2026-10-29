# AC_AGENT_V0

## Machine

```yaml
fqdn: ai_governance::AC_AGENT_V0
artifact_kind: ACTOR
version: v0
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: agent_governance
core:
  summary: An AI agent proposing an action on a user's behalf
  type: agent
  attributes:
    agent_id:
      type: string
      required: true
    requesting_user_id:
      type: string
      required: true
  description: Autonomous agent that proposes actions through governance protocol
```

---

## Intent

An AI agent proposing an action on a user's behalf
