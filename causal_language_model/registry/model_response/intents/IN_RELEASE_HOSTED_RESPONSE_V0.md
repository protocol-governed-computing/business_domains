# IN_RELEASE_HOSTED_RESPONSE_V0

## Machine

```yaml
fqdn: causal_language_model::IN_RELEASE_HOSTED_RESPONSE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: A request to release a completed hosted response
  workflow: WF_RELEASE_HOSTED_RESPONSE_V0
  inputs:
    user_prompt_id:
      type: string
      required: true
    host_id:
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

A request to release a completed hosted response
