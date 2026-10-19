# IN_PLACE_MODEL_IN_SERVICE_V0

## Machine

```yaml
fqdn: causal_language_model::IN_PLACE_MODEL_IN_SERVICE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: A request to place a registered model in service with its ceiling, system prompt and response
    rules
  workflow: WF_PLACE_MODEL_IN_SERVICE_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    staff_id:
      type: string
      required: true
    identity_key:
      type: string
      required: true
    time_in_service_id:
      type: string
      required: true
    ceiling:
      type: string
      required: true
    system_prompt:
      type: string
      required: true
    response_rules:
      type: object
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to place a registered model in service with its ceiling, system prompt and response rules
