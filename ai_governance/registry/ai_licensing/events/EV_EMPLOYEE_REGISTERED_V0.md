# EV_EMPLOYEE_REGISTERED_V0

## Machine

```yaml
fqdn: ai_governance::EV_EMPLOYEE_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing
core:
  summary: A employee registered
  description: A employee registered
  subdomain: ai_licensing
  schema:
    employee_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A employee registered
