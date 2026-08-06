# WF_REGISTER_PHYSICAL_COPY_V0

## Header (Mandatory)

- **Artifact Code:** WF_REGISTER_PHYSICAL_COPY_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Registering a further copy against a registered book

---

## Machine

```yaml
fqdn: book_library_mgmt::WF_REGISTER_PHYSICAL_COPY_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Registering a further copy against a registered book
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
        authorization_rules: $.payload.authorization_rules
      next:
        SUCCESS: CC_CLAIM_COPY_BARCODE_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_COPY_BARCODE_V0:
      type: CC
      code: CC_CLAIM_COPY_BARCODE_V0
      inputs:
        barcode: $.payload.barcode
      next:
        SUCCESS: CC_REGISTER_PHYSICAL_COPY_V0
        ALREADY_EXISTS: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REGISTER_PHYSICAL_COPY_V0:
      type: CC
      code: CC_REGISTER_PHYSICAL_COPY_V0
      inputs:
        identity_key: $.payload.identity_key
        barcode: $.payload.barcode
        copy_fields: $.payload.copy_fields
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
        operation: REGISTER_PHYSICAL_COPY
        record:
          operation: REGISTER_PHYSICAL_COPY
          staff_id: $.payload.staff_id
          subject: $.payload.barcode
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
