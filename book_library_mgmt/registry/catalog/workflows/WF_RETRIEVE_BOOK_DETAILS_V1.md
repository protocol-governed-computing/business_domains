# WF_RETRIEVE_BOOK_DETAILS_V1

## Machine

```yaml
fqdn: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_RETRIEVE_BOOK_DETAILS_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: retrieve book details'
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
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: RETRIEVE_BOOK_DETAILS
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
      next:
        SUCCESS: CC_RETRIEVE_BOOK_DETAILS_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RETRIEVE_BOOK_DETAILS_V0:
      type: CC
      code: CC_RETRIEVE_BOOK_DETAILS_V0
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: retrieve book details
