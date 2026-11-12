# EV_LICENSE_CAP_SET_V1

## Machine

```yaml
fqdn: ai_governance::EV_LICENSE_CAP_SET_V1
artifact_kind: EVENT
version: v1
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::EV_LICENSE_CAP_SET_V0
core:
  summary: A license cap set
  description: A license cap set
  subdomain: ai_licensing
  schema:
    cap:
      type: integer
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A license cap set
