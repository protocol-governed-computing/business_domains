# IN_LIST_ACTORS_V0

## Machine

```yaml
fqdn: blockchain::IN_LIST_ACTORS_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: identity
core:
  summary: A request to list actors
  workflow: WF_LIST_ACTORS_V0
  inputs:
    state:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to list actors
