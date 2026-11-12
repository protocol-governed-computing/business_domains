# EV_LICENSE_PROVISIONED_V1

## Machine

```yaml
fqdn: ai_governance::EV_LICENSE_PROVISIONED_V1
artifact_kind: EVENT
version: v1
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::EV_LICENSE_PROVISIONED_V0
core:
  summary: A license provisioned
  description: A license provisioned
  subdomain: ai_licensing
  schema:
    employee_id:
      type: string
      required: true
    license_id:
      type: string
      required: true
    tier:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```

---

## Intent

A license provisioned
