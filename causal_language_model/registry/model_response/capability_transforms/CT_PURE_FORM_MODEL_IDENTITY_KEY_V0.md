# CT_PURE_FORM_MODEL_IDENTITY_KEY_V0

## Machine

```yaml
fqdn: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: model_response
core:
  summary: Forms the single key claimed for a model from its description and fingerprint
  refusal: never
  inputs:
    description:
      type: object
      required: true
    fingerprint:
      type: string
      required: true
  outputs:
    identity_key:
      type: string
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: FORM_MODEL_IDENTITY_KEY
  implementation:
    module: causal_language_model.implementation.capability_transforms.atoms.ct_pure_form_model_identity_key_v0
    callable: execute
```

---

## Intent

Forms the single key claimed for a model from its description and fingerprint
