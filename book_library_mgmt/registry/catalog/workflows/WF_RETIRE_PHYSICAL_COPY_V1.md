# WF_RETIRE_PHYSICAL_COPY_V1

## Machine

```yaml
fqdn: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_RETIRE_PHYSICAL_COPY_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: retire physical copy'
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_RETIRE_PHYSICAL_COPY_V0
  nodes:
    IN_RETIRE_PHYSICAL_COPY_V0:
      type: IN
      code: IN_RETIRE_PHYSICAL_COPY_V0
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
      next:
        SUCCESS: CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0
        VIOLATION: EXIT_REJECTED
    CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0:
      type: CC
      code: CC_MOVE_PHYSICAL_COPY_FROM_REGISTERED_V0
      inputs:
        to_state: RETIRED
        barcode: $.payload.barcode
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: RETIRE_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: book_library_mgmt::EV_PHYSICAL_COPY_RETIRED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: retire physical copy
