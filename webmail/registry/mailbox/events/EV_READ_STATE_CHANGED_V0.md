# EV_READ_STATE_CHANGED_V0

## Machine

```yaml
fqdn: webmail::EV_READ_STATE_CHANGED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: mailbox
core:
  summary: The provider accepted a decided change of read state
  description: The provider accepted a decided change of read state
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

The provider accepted a decided change of read state
