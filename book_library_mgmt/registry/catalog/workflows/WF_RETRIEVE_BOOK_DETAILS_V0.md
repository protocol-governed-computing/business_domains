# WF_RETRIEVE_BOOK_DETAILS_V0

## Header (Mandatory)

- **Artifact Code:** WF_RETRIEVE_BOOK_DETAILS_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Assembling a book with the copies the library holds of it

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Assembling a book with the copies the library holds of it
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_RETRIEVE_BOOK_DETAILS_V0
  nodes:
    IN_RETRIEVE_BOOK_DETAILS_V0:
      type: IN
      code: IN_RETRIEVE_BOOK_DETAILS_V0
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
        SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
        VIOLATION: EXIT_REJECTED
    CC_ASSEMBLE_BOOK_DETAILS_V0:
      type: CC
      code: CC_ASSEMBLE_BOOK_DETAILS_V0
      inputs:
        identity_key: $.payload.identity_key
        copy_criteria:
          identity_key: $.payload.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_CATALOG_OPERATION_V0:
      type: CC
      code: CC_APPEND_CATALOG_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: RETRIEVE_BOOK_DETAILS
        record:
          operation: RETRIEVE_BOOK_DETAILS
          staff_id: $.payload.staff_id
          subject: $.payload.identity_key
      next:
        SUCCESS: CC_ASSEMBLE_BOOK_DETAILS_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```
