# IN_WITHDRAW_MODEL_FROM_SERVICE_V0

## Machine

```yaml
fqdn: causal_language_model::IN_WITHDRAW_MODEL_FROM_SERVICE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: A request to withdraw a model from service
  workflow: WF_WITHDRAW_MODEL_FROM_SERVICE_V0
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
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A request to withdraw a model from service
