# TEST_DATA_CT_PURE_ASSEMBLE_MODEL_READING_V0

## Machine

```yaml
fqdn: causal_language_model::TEST_DATA_CT_PURE_ASSEMBLE_MODEL_READING_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V2
authority: pgc.platform
concern: model_response
target: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
cases:
- case_id: assembles_what_fits
  expected_outcome: SUCCESS
  bindings:
    system_prompt: Answer briefly.
    question: What is my balance?
    supporting_material: Account 12345678 balance 40.
    reading_capacity: 20
  expected:
    reading:
      system_prompt: Answer briefly.
      question: What is my balance?
      supporting_material: Account 12345678 balance 40.
    reading_length: 10
- case_id: refuses_reading_too_long
  expected_outcome: VIOLATION
  bindings:
    system_prompt: Answer briefly.
    question: What is my balance?
    supporting_material: Account 12345678 balance 40.
    reading_capacity: 5
```

---

## Intent


