# AC_MODEL_HOST_V0

## Machine

```yaml
fqdn: causal_language_model::AC_MODEL_HOST_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: model_response
core:
  summary: The host of a model in service, which proposes and holds no authority
  type: ENDUSER
  attributes:
    host_id:
      type: string
      required: true
```

---

## Intent

The host of a model in service, which proposes and holds no authority
