# WF_SEARCH_CATALOG_V3

## Machine

```yaml
fqdn: book_library_mgmt::WF_SEARCH_CATALOG_V3
artifact_kind: WORKFLOW
version: v3
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_SEARCH_CATALOG_V2
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: search catalog'
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_SEARCH_CATALOG_V2
  nodes:
    IN_SEARCH_CATALOG_V2:
      type: IN
      code: IN_SEARCH_CATALOG_V2
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
        occurrence: SEARCH_CATALOG
        staff_id: $.payload.staff_id
        subject: $.payload.search_criteria
      next:
        SUCCESS: CC_SEARCH_CATALOG_V3
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_SEARCH_CATALOG_V3:
      type: CC
      code: CC_SEARCH_CATALOG_V3
      inputs:
        search_criteria: $.payload.search_criteria
      next:
        SUCCESS: EXIT_COMPLETED
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: search catalog
