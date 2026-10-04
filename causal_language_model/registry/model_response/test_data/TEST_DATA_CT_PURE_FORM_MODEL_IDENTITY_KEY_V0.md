# TEST_DATA_CT_PURE_FORM_MODEL_IDENTITY_KEY_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
cases:
- case_id: forms_key_from_description_and_fingerprint
  expected_outcome: SUCCESS
  bindings:
    description:
      reading_capacity: 64
      layers: 2
    fingerprint: sha256:ab12
  expected:
    identity_key: '{"layers":2,"reading_capacity":64}|sha256:ab12'
- case_id: refuses_blank_fingerprint
  expected_outcome: VIOLATION
  bindings:
    description:
      reading_capacity: 64
      layers: 2
    fingerprint: ' '
```

---

## Intent


