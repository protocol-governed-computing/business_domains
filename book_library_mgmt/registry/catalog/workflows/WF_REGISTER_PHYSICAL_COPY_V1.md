# WF_REGISTER_PHYSICAL_COPY_V1

## Machine

```yaml
fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: register physical copy'
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_REGISTER_PHYSICAL_COPY_V0
  nodes:
    IN_REGISTER_PHYSICAL_COPY_V0:
      type: IN
      code: IN_REGISTER_PHYSICAL_COPY_V0
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
      next:
        SUCCESS: CC_RESOLVE_BOOK_IDENTITY_V1
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_BOOK_IDENTITY_V1:
      type: CC
      code: CC_RESOLVE_BOOK_IDENTITY_V1
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_CLAIM_COPY_BARCODE_V1
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_COPY_BARCODE_V1:
      type: CC
      code: CC_CLAIM_COPY_BARCODE_V1
      inputs:
        barcode: $.payload.barcode
      next:
        SUCCESS: CC_WRITE_PHYSICAL_COPY_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_PHYSICAL_COPY_V0:
      type: CC
      code: CC_WRITE_PHYSICAL_COPY_V0
      inputs:
        barcode: $.payload.barcode
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: REGISTER_PHYSICAL_COPY
        staff_id: $.payload.staff_id
        subject: $.payload.barcode
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: book_library_mgmt::EV_PHYSICAL_COPY_REGISTERED_V1
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: register physical copy
