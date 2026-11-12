# WF_REGISTER_ADDITIONAL_EDITION_V1

## Machine

```yaml
fqdn: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: catalog
supersedes: book_library_mgmt::WF_REGISTER_ADDITIONAL_EDITION_V0
runtime_binding: book_library_mgmt::RB_CATALOG_BINDINGS_V0
subdomain: catalog
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: register additional edition'
  actor_context: book_library_mgmt::AC_LIBRARY_STAFF_V0
  start_node: IN_REGISTER_ADDITIONAL_EDITION_V0
  nodes:
    IN_REGISTER_ADDITIONAL_EDITION_V0:
      type: IN
      code: IN_REGISTER_ADDITIONAL_EDITION_V0
      next:
        ACK: CC_CONFIRM_STAFF_AUTHORIZED_V0
        NACK: EXIT_REJECTED
    CC_CONFIRM_STAFF_AUTHORIZED_V0:
      type: CC
      code: CC_CONFIRM_STAFF_AUTHORIZED_V0
      inputs:
        staff_credentials: $.payload.staff_credentials
      next:
        SUCCESS: CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
        VIOLATION: EXIT_REJECTED
    CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0:
      type: CC
      code: CC_CHECK_REGISTER_ADDITIONAL_EDITION_SUBMISSION_V0
      inputs:
        submission:
          title: $.payload.title
          author: $.payload.author
          publication_year: $.payload.publication_year
          subject: $.payload.subject
      next:
        SUCCESS: CC_RESOLVE_WORK_V1
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_WORK_V1:
      type: CC
      code: CC_RESOLVE_WORK_V1
      inputs:
        title: $.payload.title
        author: $.payload.author
      next:
        SUCCESS: CC_CLAIM_BOOK_IDENTITY_V1
        VIOLATION: EXIT_REJECTED
        NOT_FOUND: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_CLAIM_BOOK_IDENTITY_V1:
      type: CC
      code: CC_CLAIM_BOOK_IDENTITY_V1
      inputs:
        title: $.payload.title
        author: $.payload.author
        publication_year: $.payload.publication_year
      next:
        SUCCESS: CC_WRITE_BOOK_V0
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_BOOK_V0:
      type: CC
      code: CC_WRITE_BOOK_V0
      inputs:
        identity_key: $.results.CC_CLAIM_BOOK_IDENTITY_V1.identity_key
        submission:
          title: $.payload.title
          author: $.payload.author
          publication_year: $.payload.publication_year
          subject: $.payload.subject
      next:
        SUCCESS: CC_RECORD_CATALOG_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_CATALOG_MOMENT_V0:
      type: CC
      code: CC_RECORD_CATALOG_MOMENT_V0
      inputs:
        occurrence: REGISTER_ADDITIONAL_EDITION
        staff_id: $.payload.staff_id
        subject: $.results.CC_CLAIM_BOOK_IDENTITY_V1.identity_key
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: book_library_mgmt::EV_BOOK_REGISTERED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: register additional edition
