# VOCAB_CATALOG_STATES_V0

## Header (Mandatory)

- **Artifact Code:** VOCAB_CATALOG_STATES_V0
- **Artifact Kind:** vocabulary
- **Governed By:** CONSTITUTION_VOCABULARY_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The result statuses the catalog yields that the platform vocabulary does not already declare.

`DENIED` is the one. Authorization failure is not a `VIOLATION` — the request was well formed and
the caller simply may not perform it — and it is not `NOT_FOUND`, because the record may exist
perfectly well. Collapsing it into either would leave an audit unable to distinguish a malformed
request from an unauthorized one, which is exactly the distinction the journal exists to record.

Every other status the catalog uses is already declared by the platform: `NOT_FOUND` covers a work
that was never registered, and `ALREADY_EXISTS` covers a duplicate registration.

---

## Machine

```yaml
fqdn: book_library_mgmt::VOCAB_CATALOG_STATES_V0
artifact_kind: VOCABULARY
version: v0
governed_by: fb.vocabulary::CONSTITUTION_VOCABULARY_V0
extends: fb.vocabulary::VOCAB_EXECUTION_STATES_V0

result_status:
  casing: UPPER_SNAKE
  entries:
    - DENIED
```
