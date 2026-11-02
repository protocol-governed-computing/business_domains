# WF_LIST_FOLDER_V0

## Machine

```yaml
fqdn: webmail::WF_LIST_FOLDER_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: mailbox
runtime_binding: webmail::RB_MAILBOX_BINDINGS_V0
subdomain: mailbox
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Chooses which messages make the page of a folder the person asked for, newest received first
  actor_context: webmail::AC_MAIL_HOST_V0
  start_node: IN_LIST_FOLDER_V0
  nodes:
    IN_LIST_FOLDER_V0:
      type: IN
      code: IN_LIST_FOLDER_V0
      next:
        ACK: CONFIRM_ANSWERED
        NACK: EXIT_REJECTED
    CONFIRM_ANSWERED:
      type: CC
      code: CC_CONFIRM_PROVIDER_ANSWERED_V0
      inputs:
        provider_answer: $.payload.provider_answer
      next:
        SUCCESS: CC_CHOOSE_FOLDER_PAGE_V0
        VIOLATION: RECORD_REFUSED
    CC_CHOOSE_FOLDER_PAGE_V0:
      type: CC
      code: CC_CHOOSE_FOLDER_PAGE_V0
      inputs:
        message_ids: $.payload.message_ids
        page: $.payload.page
      next:
        SUCCESS: RECORD_LISTED
        VIOLATION: RECORD_REPORT_REFUSED
    RECORD_LISTED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: LIST_FOLDER
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: ANSWERED
          provider_answer: $.payload.provider_answer
          page: $.payload.page
          page_ids: $.results.CC_CHOOSE_FOLDER_PAGE_V0.page_ids
          more_exist: $.results.CC_CHOOSE_FOLDER_PAGE_V0.more_exist
          folder_empty: $.results.CC_CHOOSE_FOLDER_PAGE_V0.folder_empty
          message_count: $.results.CC_CHOOSE_FOLDER_PAGE_V0.message_count
      next:
        SUCCESS: EXIT_LISTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: LIST_FOLDER
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: REFUSED
          provider_answer: $.payload.provider_answer
          reason: $.payload.provider_answer
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REPORT_REFUSED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: LIST_FOLDER
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: REFUSED
          provider_answer: $.payload.provider_answer
          reason: REPORT_NOT_VALID
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_LISTED:
      type: EXIT
      emit: webmail::EV_FOLDER_LISTED_V0
    EXIT_REFUSED:
      type: EXIT
      emit: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Chooses which messages make the page of a folder the person asked for, newest received first
