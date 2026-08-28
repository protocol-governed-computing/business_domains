# WF_REINSTATE_BOOK_RECORD_V0

## 1. Intent

Returning a retired book record to the registered state

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Returning a retired book record to the registered state
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_REINSTATE_BOOK_RECORD_V0
  nodes:
    IN_REINSTATE_BOOK_RECORD_V0:
      type: IN
      code: IN_REINSTATE_BOOK_RECORD_V0
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
        SUCCESS: CC_REINSTATE_BOOK_RECORD_V0
        VIOLATION: EXIT_REJECTED
    CC_REINSTATE_BOOK_RECORD_V0:
      type: CC
      code: CC_REINSTATE_BOOK_RECORD_V0
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_APPEND_CATALOG_OPERATION_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_APPEND_CATALOG_OPERATION_V0:
      type: CC
      code: CC_APPEND_CATALOG_OPERATION_V0
      inputs:
        staff_id: $.payload.staff_id
        operation: REINSTATE_BOOK_RECORD
        record:
          operation: REINSTATE_BOOK_RECORD
          staff_id: $.payload.staff_id
          subject: $.payload.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```
