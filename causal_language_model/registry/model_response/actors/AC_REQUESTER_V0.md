# AC_REQUESTER_V0

## Machine

```yaml
fqdn: causal_language_model::AC_REQUESTER_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: model_response
core:
  summary: The actor who submits a user prompt for one customer
  type: ENDUSER
  attributes:
    requester_id:
      type: string
      required: true
    permitted_customers:
      type: array
      default: '[]'
```

---

## Intent

The actor who submits a user prompt for one customer
