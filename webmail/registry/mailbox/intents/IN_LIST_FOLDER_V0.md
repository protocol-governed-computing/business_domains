# IN_LIST_FOLDER_V0

## Machine

```yaml
fqdn: webmail::IN_LIST_FOLDER_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: A host's report of a folder's message identifiers and the page asked for
  workflow: WF_LIST_FOLDER_V0
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
    message_ids:
      type: array
      required: true
    page:
      type: integer
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```

---

## Intent

A host's report of a folder's message identifiers and the page asked for
