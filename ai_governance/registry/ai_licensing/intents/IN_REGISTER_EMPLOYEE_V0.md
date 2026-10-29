# IN_REGISTER_EMPLOYEE_V0

## Machine

```yaml
fqdn: ai_governance::IN_REGISTER_EMPLOYEE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: A request to register employee
  workflow: WF_REGISTER_EMPLOYEE_V0
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

A request to register employee
