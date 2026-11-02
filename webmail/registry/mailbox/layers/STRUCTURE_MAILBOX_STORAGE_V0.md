# STRUCTURE_MAILBOX_STORAGE_V0

## Machine

```yaml
fqdn: webmail::STRUCTURE_MAILBOX_STORAGE_V0
artifact_kind: STRUCTURE
version: v0
governed_by: structure::CONSTITUTION_STRUCTURE_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Declares the mailbox record and the path it occupies
  layer: DOMAINS
  domain: webmail
  subdomain: mailbox
  entity_stores:
    MAILBOX_RECORDS:
      path: webmail/mailbox/mailbox_records.jsonl
```

---

## Intent

Declares the mailbox record and the path it occupies
