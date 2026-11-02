# IN_REPORT_CHANGE_OUTCOME_V0

## Machine

```yaml
fqdn: webmail::IN_REPORT_CHANGE_OUTCOME_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: A host's report of whether the provider accepted a decided change
  workflow: WF_REPORT_CHANGE_OUTCOME_V0
  inputs:
    host_id:
      type: string
      required: true
    mailbox:
      type: string
      required: true
    folder:
      type: string
      required: true
    provider_answer:
      type: string
      required: true
    message_id:
      type: integer
      required: true
    change:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A host's report of whether the provider accepted a decided change
