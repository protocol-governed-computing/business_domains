# RB_MAILBOX_BINDINGS_V0

## Machine

```yaml
fqdn: webmail::RB_MAILBOX_BINDINGS_V0
artifact_kind: RUNTIME_BINDING
version: v0
governed_by: runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Binds every mailbox act to the record it appends to
  storage_structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
  bindings:
    capability_side_effects::CS_APPENDONLY_JSONL_V0:
      policy:
        structure: webmail::STRUCTURE_MAILBOX_STORAGE_V0
```

---

## Intent

Binds every mailbox act to the record it appends to
