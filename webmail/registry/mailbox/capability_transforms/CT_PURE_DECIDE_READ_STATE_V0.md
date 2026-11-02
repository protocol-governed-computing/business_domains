# CT_PURE_DECIDE_READ_STATE_V0

## Machine

```yaml
fqdn: webmail::CT_PURE_DECIDE_READ_STATE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Decides a change of read state from the state held and the state asked for
  refusal: raises
  inputs:
    seen:
      type: boolean
      required: true
    wanted_read:
      type: boolean
      required: true
  outputs:
    change:
      type: string
      required: true
    read_now:
      type: boolean
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: DECIDE_READ_STATE
  implementation:
    module: webmail.implementation.capability_transforms.atoms.ct_pure_decide_read_state_v0
    callable: execute
```

---

## Intent

Decides a change of read state from the state held and the state asked for
