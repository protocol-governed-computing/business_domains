# VOCAB_AI_LICENSING_STATES_V0

## 1. Intent

Authorized extension of the outcome space for the `ai_licensing` subdomain.

Licence provisioning has one outcome the platform does not model: the request was well-formed and
the actor eligible, but the licence cap is already met. That is neither `VIOLATION` (nothing was
violated) nor `NOT_FOUND` (everything was found) — it is a governed refusal with its own audit
meaning, so it is declared here rather than mapped onto a platform status that would lose it.

`CAP_REACHED` is consumed by `CC_ENFORCE_LICENSE_CAP_V0` and routed by the provisioning workflow.

---

## 2. Extension Contract

This artifact `extends` the reserving declaration `vocabulary::VOCAB_EXECUTION_STATES_V0`, and
contributes only to `result_status` — the one category that declaration marks
`domain_extensible: true`. The compiler folds these entries into the build's **vocabulary
closure**; they are not visible to any other domain
(`CONSTITUTION_VOCABULARY_V0` §9.2, domain isolation).

---

## Machine

```yaml
fqdn: ai_governance::VOCAB_AI_LICENSING_STATES_V0
artifact_kind: VOCABULARY
version: v0
governed_by: vocabulary::CONSTITUTION_VOCABULARY_V0
authority: pgc.platform
concern: ai_licensing
extends: vocabulary::VOCAB_EXECUTION_STATES_V0
result_status:
  casing: UPPER_SNAKE
  entries:
  - CAP_REACHED
```

