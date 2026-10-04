# AC_MODEL_STAFF_V0

## Machine

```yaml
fqdn: causal_language_model::AC_MODEL_STAFF_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: model_response
core:
  summary: The actor whose authorization every model staff operation binds
  type: ENDUSER
  attributes:
    staff_id:
      type: string
      required: true
    authorized:
      type: boolean
      default: false
```

---

## Intent

The actor whose authorization every model staff operation binds
