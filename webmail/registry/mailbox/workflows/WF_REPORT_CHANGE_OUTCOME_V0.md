# WF_REPORT_CHANGE_OUTCOME_V0

## Machine

```yaml
fqdn: webmail::WF_REPORT_CHANGE_OUTCOME_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: mailbox
runtime_binding: webmail::RB_MAILBOX_BINDINGS_V0
subdomain: mailbox
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Records whether the provider accepted a change the business decided
  actor_context: webmail::AC_MAIL_HOST_V0
  start_node: IN_REPORT_CHANGE_OUTCOME_V0
  nodes:
    IN_REPORT_CHANGE_OUTCOME_V0:
      type: IN
      code: IN_REPORT_CHANGE_OUTCOME_V0
      next:
        ACK: CONFIRM_ANSWERED
        NACK: EXIT_REJECTED
    CONFIRM_ANSWERED:
      type: CC
      code: CC_CONFIRM_PROVIDER_ANSWERED_V0
      inputs:
        provider_answer: $.payload.provider_answer
      next:
        SUCCESS: RECORD_CHANGED
        VIOLATION: RECORD_REFUSED
    RECORD_CHANGED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: REPORT_CHANGE_OUTCOME
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: ANSWERED
          provider_answer: $.payload.provider_answer
          message_id: $.payload.message_id
          change: $.payload.change
      next:
        SUCCESS: EXIT_CHANGED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: REPORT_CHANGE_OUTCOME
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: REFUSED
          provider_answer: $.payload.provider_answer
          reason: $.payload.provider_answer
          message_id: $.payload.message_id
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_CHANGED:
      type: EXIT
      emit: webmail::EV_READ_STATE_CHANGED_V0
    EXIT_REFUSED:
      type: EXIT
      emit: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Records whether the provider accepted a change the business decided
