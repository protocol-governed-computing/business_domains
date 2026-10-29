# IN_SET_LICENSE_CAP_V0

## Machine

```yaml
fqdn: ai_governance::IN_SET_LICENSE_CAP_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: A request to set license cap
  workflow: WF_SET_LICENSE_CAP_V0
  inputs:
    cap:
      type: integer
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to set license cap
