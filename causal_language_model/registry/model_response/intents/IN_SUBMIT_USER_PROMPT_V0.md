# IN_SUBMIT_USER_PROMPT_V0

## Machine

```yaml
fqdn: causal_language_model::IN_SUBMIT_USER_PROMPT_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: model_response
core:
  summary: A user prompt submitted on behalf of a customer
  workflow: WF_SUBMIT_USER_PROMPT_V0
  inputs:
    user_prompt_id:
      type: string
      required: true
    requester_id:
      type: string
      required: true
    permitted_customers:
      type: array
      required: true
    customer_id:
      type: string
      required: true
    account_numbers:
      type: array
      required: true
    identity_key:
      type: string
      required: true
    kind:
      type: string
      required: true
    question:
      type: string
      required: true
    supporting_material:
      type: string
      required: true
    seed:
      type: integer
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A user prompt submitted on behalf of a customer
