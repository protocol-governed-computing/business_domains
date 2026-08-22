# WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0

## Header (Mandatory)

- **Artifact Code:** WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The governed sequence that corrects what the library publishes about a book

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that corrects what the library publishes about a book
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
  nodes:
    IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0:
      type: IN
      code: IN_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
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
        SUCCESS: CC_RESOLVE_BOOK_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_BOOK_IDENTITY_V0:
      type: CC
      code: CC_RESOLVE_BOOK_IDENTITY_V0
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0:
      type: CC
      code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
      inputs:
        identity_key: $.payload.identity_key
        updated_fields: $.payload.updated_fields
      next:
        SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_CATALOG_OPERATION_V0:
      type: CC
      code: CC_APPEND_CATALOG_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
        record:
          operation: UPDATE_BIBLIOGRAPHIC_INFORMATION
          staff_id: $.payload.staff_id
          subject: $.payload.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: book_library_mgmt::EV_BIBLIOGRAPHIC_INFORMATION_UPDATED_V0
    EXIT_REJECTED:
      type: EXIT
```
