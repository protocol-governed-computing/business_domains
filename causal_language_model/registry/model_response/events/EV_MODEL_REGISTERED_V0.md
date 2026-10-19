# EV_MODEL_REGISTERED_V0

## Machine

```yaml
fqdn: causal_language_model::EV_MODEL_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: The moment the business records a model
  description: The moment the business records a model
  subdomain: model_response
  schema:
    identity_key:
      type: string
      required: true
    staff_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```

---

## Intent

The moment the business records a model
