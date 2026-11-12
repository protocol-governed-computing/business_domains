# IN_PROVISION_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::IN_PROVISION_LICENSE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::IN_PROVISION_AI_LICENSE_V0
core:
  summary: A request to provision license
  workflow: WF_PROVISION_LICENSE_V0
  inputs:
    employee_id:
      type: string
      required: true
    tier:
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

A request to provision license
