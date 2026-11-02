# AC_MAIL_HOST_V0

## Machine

```yaml
fqdn: webmail::AC_MAIL_HOST_V0
artifact_kind: ACTOR
version: v0
governed_by: actor::CONSTITUTION_ACTOR_IDENTITY_V0
authority: pgc.platform
concern: mailbox
core:
  summary: The program that reaches a person's mail provider; it reports and carries out, and holds no
    authority
  type: system
  attributes:
    host_id:
      type: string
      required: true
```

---

## Intent

The program that reaches a person's mail provider; it reports and carries out, and holds no authority
