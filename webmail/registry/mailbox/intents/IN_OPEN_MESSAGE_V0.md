# IN_OPEN_MESSAGE_V0

## Machine

```yaml
fqdn: webmail::IN_OPEN_MESSAGE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: A host's report of the read state and the parts of a message the person asked to open
  workflow: WF_OPEN_MESSAGE_V0
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
    seen:
      type: boolean
      required: true
    parts:
      type: array
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A host's report of the read state and the parts of a message the person asked to open
