# WF_MARK_MESSAGE_V0

## Machine

```yaml
fqdn: webmail::WF_MARK_MESSAGE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: mailbox
runtime_binding: webmail::RB_MAILBOX_BINDINGS_V0
subdomain: mailbox
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: Decides a change of a message's read state, or that nothing changes
  actor_context: webmail::AC_MAIL_HOST_V0
  start_node: IN_MARK_MESSAGE_V0
  nodes:
    IN_MARK_MESSAGE_V0:
      type: IN
      code: IN_MARK_MESSAGE_V0
      next:
        ACK: CONFIRM_ANSWERED
        NACK: EXIT_REJECTED
    CONFIRM_ANSWERED:
      type: CC
      code: CC_CONFIRM_PROVIDER_ANSWERED_V0
      inputs:
        provider_answer: $.payload.provider_answer
      next:
        SUCCESS: CC_DECIDE_READ_STATE_V0
        VIOLATION: RECORD_REFUSED
    CC_DECIDE_READ_STATE_V0:
      type: CC
      code: CC_DECIDE_READ_STATE_V0
      inputs:
        seen: $.payload.seen
        wanted_read: $.payload.wanted_read
      next:
        SUCCESS: RECORD_MARKED
        VIOLATION: RECORD_REPORT_REFUSED
    RECORD_MARKED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: MARK_MESSAGE
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: ANSWERED
          provider_answer: $.payload.provider_answer
          message_id: $.payload.message_id
          wanted_read: $.payload.wanted_read
          change: $.results.CC_DECIDE_READ_STATE_V0.change
          read_now: $.results.CC_DECIDE_READ_STATE_V0.read_now
      next:
        SUCCESS: EXIT_MARKED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    RECORD_REFUSED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: MARK_MESSAGE
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
    RECORD_REPORT_REFUSED:
      type: CC
      code: CC_RECORD_MAILBOX_REQUEST_V0
      inputs:
        host_id: $.payload.host_id
        entry:
          request: MARK_MESSAGE
          mailbox: $.payload.mailbox
          folder: $.payload.folder
          outcome: REFUSED
          provider_answer: $.payload.provider_answer
          reason: REPORT_NOT_VALID
          message_id: $.payload.message_id
      next:
        SUCCESS: EXIT_REFUSED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_MARKED:
      type: EXIT
    EXIT_REFUSED:
      type: EXIT
      emit: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

Decides a change of a message's read state, or that nothing changes
