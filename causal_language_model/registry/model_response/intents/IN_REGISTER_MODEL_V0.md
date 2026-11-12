# IN_REGISTER_MODEL_V0

## Machine

```yaml
fqdn: causal_language_model::IN_REGISTER_MODEL_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: A request to register a model with its description and fingerprint
  workflow: WF_REGISTER_MODEL_V0
  inputs:
    staff_credentials:
      type: object
      required: true
    staff_id:
      type: string
      required: true
    description:
      type: object
      required: true
    fingerprint:
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

A request to register a model with its description and fingerprint
