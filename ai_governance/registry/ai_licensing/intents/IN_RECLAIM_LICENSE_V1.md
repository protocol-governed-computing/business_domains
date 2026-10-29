# IN_RECLAIM_LICENSE_V1

## Machine

```yaml
fqdn: ai_governance::IN_RECLAIM_LICENSE_V1
artifact_kind: INTENT
version: v1
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::IN_RECLAIM_LICENSE_V0
core:
  summary: A request to reclaim license
  workflow: WF_RECLAIM_LICENSE_V1
  inputs:
    employee_id:
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

A request to reclaim license
