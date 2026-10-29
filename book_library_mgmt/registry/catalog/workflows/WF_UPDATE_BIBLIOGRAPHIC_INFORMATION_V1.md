# WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1

## Machine

```yaml
fqdn: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: update bibliographic information'
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
      next:
        SUCCESS: CC_RESOLVE_BOOK_IDENTITY_V1
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_BOOK_IDENTITY_V1:
      type: CC
      code: CC_RESOLVE_BOOK_IDENTITY_V1
      inputs:
        identity_key: $.payload.identity_key
      next:
        SUCCESS: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1:
      type: CC
      code: CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1
      inputs:
        identity_key: $.payload.identity_key
        updated_fields: $.payload.updated_fields
      next:
        SUCCESS: CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0:
      type: CC
      code: CC_CONFIRM_BOOK_IDENTITY_UNCHANGED_V0
      inputs:
        identity_key: $.payload.identity_key
        updated_identity_key: $.results.CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1.updated_identity_key
      next:
        SUCCESS: CC_WRITE_CORRECTED_BOOK_RECORD_V0
        VIOLATION: CC_CLAIM_BOOK_IDENTITY_V1
    CC_WRITE_CORRECTED_BOOK_RECORD_V0:
      type: CC
      code: CC_WRITE_CORRECTED_BOOK_RECORD_V0
      inputs:
        identity_key: $.payload.identity_key
        updated_record: $.results.CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1.updated_record
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_BOOK_IDENTITY_V1:
      type: CC
      code: CC_CLAIM_BOOK_IDENTITY_V1
      inputs:
        title: $.payload.updated_fields.title
        author: $.payload.updated_fields.author
        publication_year: $.payload.updated_fields.publication_year
      next:
        SUCCESS: CC_CLAIM_WORK_IDENTITY_V1
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_WORK_IDENTITY_V1:
      type: CC
      code: CC_CLAIM_WORK_IDENTITY_V1
      inputs:
        title: $.payload.updated_fields.title
        author: $.payload.updated_fields.author
        work_fields:
          title: $.payload.updated_fields.title
          author: $.payload.updated_fields.author
      next:
        SUCCESS: CC_REKEY_BOOK_V0
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: CC_REKEY_BOOK_V0
        BACKEND_ERROR: EXIT_REJECTED
    CC_REKEY_BOOK_V0:
      type: CC
      code: CC_REKEY_BOOK_V0
      inputs:
        identity_key: $.payload.identity_key
        updated_identity_key: $.results.CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1.updated_identity_key
        updated_record: $.results.CC_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1.updated_record
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
        NOT_FOUND: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: UPDATE_BIBLIOGRAPHIC_INFORMATION
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

---

## Intent

The governed sequence that performs: update bibliographic information
