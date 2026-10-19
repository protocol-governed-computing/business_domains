# EV_USER_PROMPT_RESPONDED_V0

## Machine

```yaml
fqdn: causal_language_model::EV_USER_PROMPT_RESPONDED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: The moment a model response is released
  description: The moment a model response is released
  subdomain: model_response
  schema:
    user_prompt_id:
      type: string
      required: true
    identity_key:
      type: string
      required: true
    requester_id:
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

The moment a model response is released
