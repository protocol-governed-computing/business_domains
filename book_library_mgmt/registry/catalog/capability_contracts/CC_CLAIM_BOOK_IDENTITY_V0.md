# CC_CLAIM_BOOK_IDENTITY_V0

## Header (Mandatory)

- **Artifact Code:** CC_CLAIM_BOOK_IDENTITY_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Claim a book's identity so a second registration of the same book is refused

---

## Machine

```yaml
fqdn: book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
core:
  summary: Claim a book's identity so a second registration of the same book is refused
  inputs:
    title:
      type: string
      required: true
    author:
      type: string
      required: true
    publication_year:
      type: integer
      required: true
  outputs:
    identity_key:
      type: string
      required: true
    address:
      type: string
      required: true
  result_status_contract:
    allowed:
    - VIOLATION
    - SUCCESS
    - ALREADY_EXISTS
    - BACKEND_ERROR
    on_input_failure: VIOLATION
  pipeline:
  - step: form_identity_key
    transform: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    inputs:
      title: $.inputs.title
      author: $.inputs.author
      publication_year: $.inputs.publication_year
    outputs:
      identity_key: $.capability_result.identity_key
    result_surface:
    - SUCCESS
    - VIOLATION
    on_result:
      SUCCESS: continue
      VIOLATION: exit
  - step: claim_identity
    side_effect: capability_side_effects::CS_REGISTRY_V0
    op: REGISTER
    store: BOOK_IDENTITY_REGISTRY
    inputs:
      key: $.results.form_identity_key.identity_key
      target_cs: CS_MUTABLE_JSON_V0
      target_ref: BOOKS
    outputs:
      address: $.capability_result.address
      result_status: $.result_status
    result_surface:
    - SUCCESS
    - ALREADY_EXISTS
    - VIOLATION
    - BACKEND_ERROR
    on_result:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
```
