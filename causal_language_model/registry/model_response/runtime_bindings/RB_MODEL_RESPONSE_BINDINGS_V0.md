# RB_MODEL_RESPONSE_BINDINGS_V0

## Machine

```yaml
fqdn: causal_language_model::RB_MODEL_RESPONSE_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: model_response
core:
  summary: Binds every model response workflow to the mechanisms and stores it uses
  storage_structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
  bindings:
    capability_side_effects::CS_MUTABLE_JSON_V0:
      policy:
        structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    capability_side_effects::CS_REGISTRY_V0:
      policy:
        structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        structure: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
```

---

## Intent

Binds every model response workflow to the mechanisms and stores it uses
