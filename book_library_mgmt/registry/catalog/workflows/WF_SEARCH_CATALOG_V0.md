# WF_SEARCH_CATALOG_V0

## Header (Mandatory)

- **Artifact Code:** WF_SEARCH_CATALOG_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Searching the catalog for current records.

Authorization is confirmed first and the operation is journalled last, so every catalog operation
is performed by someone entitled to and leaves an account of itself.

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_SEARCH_CATALOG_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0

runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0

core:
  summary: Search the catalog and record that it happened
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0

  start_node: IN_SEARCH_CATALOG_V0

  nodes:
    IN_SEARCH_CATALOG_V0:
      type: IN
      code: IN_SEARCH_CATALOG_V0
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED

    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_id: $.payload.staff_id
      next:
        SUCCESS: CC_SEARCH_CATALOG_V0
        DENIED: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED

    CC_SEARCH_CATALOG_V0:
      type: CC
      code: CC_SEARCH_CATALOG_V0
      inputs:
        search_terms: $.payload.search_terms
      next:
        SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED

    CC_APPEND_CATALOG_OPERATION_V0:
      type: CC
      code: CC_APPEND_CATALOG_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: SEARCH_CATALOG
        subject: CATALOG
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
