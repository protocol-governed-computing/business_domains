# STRUCTURE_MODEL_RESPONSE_STORAGE_V0

## Machine

```yaml
fqdn: causal_language_model::STRUCTURE_MODEL_RESPONSE_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: model_response
core:
  summary: Declares the seven stores the subdomain owns and the paths they occupy
  layer: DOMAINS
  domain: causal_language_model
  subdomain: model_response
  entity_stores:
    MODELS:
      path: causal_language_model/model_response/models.json
    MODEL_IDENTITY_REGISTRY:
      path: causal_language_model/model_response/model_identity_registry.jsonl
    TIME_IN_SERVICE_REGISTRY:
      path: causal_language_model/model_response/time_in_service_registry.jsonl
    USER_PROMPT_REGISTRY:
      path: causal_language_model/model_response/user_prompt_registry.jsonl
    TIMES_IN_SERVICE:
      path: causal_language_model/model_response/times_in_service.json
    USER_PROMPT_RECORDS:
      path: causal_language_model/model_response/user_prompt_records.jsonl
    MODEL_OPERATIONS:
      path: causal_language_model/model_response/model_operations.jsonl
```

---

## Intent

Declares the seven stores the subdomain owns and the paths they occupy
