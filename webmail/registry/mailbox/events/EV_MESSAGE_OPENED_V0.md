# EV_MESSAGE_OPENED_V0

## Machine

```yaml
fqdn: webmail::EV_MESSAGE_OPENED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: A message was opened for the person
  description: A message was opened for the person
  subdomain: mailbox
  schema:
    entry:
      type: object
      required: true
    sequence_number:
      type: integer
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
      description: When the moment occurred
```

---

## Intent

A message was opened for the person
