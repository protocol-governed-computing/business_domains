# IN_OFFER_NEXT_TOKENS_V0

## Machine

```yaml
fqdn: causal_language_model::IN_OFFER_NEXT_TOKENS_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: The candidates a hosted model could write next, naming its fingerprint and the size of what
    it reads
  workflow: WF_OFFER_NEXT_TOKENS_V0
  inputs:
    user_prompt_id:
      type: string
      required: true
    host_id:
      type: string
      required: true
    fingerprint:
      type: string
      required: true
    reported_reading_size:
      type: integer
      required: true
    candidates:
      type: array
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

The candidates a hosted model could write next, naming its fingerprint and the size of what it reads
