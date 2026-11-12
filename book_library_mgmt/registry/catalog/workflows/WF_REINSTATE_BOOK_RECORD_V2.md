# WF_REINSTATE_BOOK_RECORD_V2

## Machine

```yaml
fqdn: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V2
artifact_kind: WORKFLOW
version: v2
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_REINSTATE_BOOK_RECORD_V1
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: reinstate book record'
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_REINSTATE_BOOK_RECORD_V1
  nodes:
    IN_REINSTATE_BOOK_RECORD_V1:
      type: IN
      code: IN_REINSTATE_BOOK_RECORD_V1
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
      next:
        SUCCESS: CC_MOVE_BOOK_FROM_RETIRED_V0
        VIOLATION: EXIT_REJECTED
    CC_MOVE_BOOK_FROM_RETIRED_V0:
      type: CC
      code: CC_MOVE_BOOK_FROM_RETIRED_V0
      inputs:
        to_state: REGISTERED
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: REINSTATE_BOOK_RECORD
        staff_id: $.payload.staff_id
        subject: $.payload.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: book_library_mgmt::EV_BOOK_REINSTATED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: reinstate book record
