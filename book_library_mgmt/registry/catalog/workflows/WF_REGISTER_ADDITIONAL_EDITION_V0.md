# WF_REGISTER_ADDITIONAL_EDITION_V0

## Header (Mandatory)

- **Artifact Code:** WF_REGISTER_ADDITIONAL_EDITION_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The governed sequence that registers a further edition of an existing work

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that registers a further edition of an existing work
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_REGISTER_ADDITIONAL_EDITION_V0
  nodes:
    IN_REGISTER_ADDITIONAL_EDITION_V0:
      type: IN
      code: IN_REGISTER_ADDITIONAL_EDITION_V0
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
        authorization_rules: $.payload.authorization_rules
      next:
        SUCCESS: CC_VALIDATE_BOOK_SUBMISSION_V0
        VIOLATION: EXIT_REJECTED
    CC_VALIDATE_BOOK_SUBMISSION_V0:
      type: CC
      code: CC_VALIDATE_BOOK_SUBMISSION_V0
      inputs:
        book_fields: $.payload.edition_fields
        book_schema: $.payload.edition_schema
        work_fields: $.payload.work_fields
        work_schema: $.payload.work_schema
      next:
        SUCCESS: CC_RESOLVE_WORK_V0
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_WORK_V0:
      type: CC
      code: CC_RESOLVE_WORK_V0
      inputs:
        title: $.payload.title
        author: $.payload.author
      next:
        SUCCESS: CC_CLAIM_BOOK_IDENTITY_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_BOOK_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_BOOK_IDENTITY_V0
      inputs:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
      next:
        SUCCESS: CC_REGISTER_ADDITIONAL_EDITION_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REGISTER_ADDITIONAL_EDITION_V0:
      type: CC
      code: CC_REGISTER_ADDITIONAL_EDITION_V0
      inputs:
        identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
        edition_schema: $.payload.edition_schema
        edition_fields:
          identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
          title: $.payload.title
          author: $.payload.author
          publication_year: $.payload.publication_year
          subject: $.payload.subject
          state: REGISTERED
          work_key: $.results.CC_RESOLVE_WORK_V0.work_key
      next:
        SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_CATALOG_OPERATION_V0:
      type: CC
      code: CC_APPEND_CATALOG_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: REGISTER_ADDITIONAL_EDITION
        record:
          operation: REGISTER_ADDITIONAL_EDITION
          staff_id: $.payload.staff_id
          subject: $.results.CC_CLAIM_BOOK_IDENTITY_V0.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      outcome: SUCCESS
    EXIT_REJECTED:
      type: EXIT
      outcome: VIOLATION
```
