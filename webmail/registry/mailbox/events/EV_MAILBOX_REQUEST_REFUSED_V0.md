# EV_MAILBOX_REQUEST_REFUSED_V0

## Machine

```yaml
fqdn: webmail::EV_MAILBOX_REQUEST_REFUSED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: A request was refused
  description: A request was refused
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
  moment: refusal
```

---

## Intent

A request was refused
