# CT_PURE_CHOOSE_MESSAGE_TEXT_V0

## Machine

```yaml
fqdn: webmail::CT_PURE_CHOOSE_MESSAGE_TEXT_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Chooses a message's plain-text part from its parts, or says its text cannot be displayed yet
  refusal: raises
  inputs:
    parts:
      type: array
      required: true
  outputs:
    text_part:
      type: string
      required: true
    text_displayable:
      type: boolean
      required: true
    shown_headers:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: CHOOSE_MESSAGE_TEXT
  implementation:
    module: webmail.implementation.capability_transforms.atoms.ct_pure_choose_message_text_v0
    callable: execute
```

---

## Intent

Chooses a message's plain-text part from its parts, or says its text cannot be displayed yet
