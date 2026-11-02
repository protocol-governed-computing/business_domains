# CT_PURE_CHOOSE_FOLDER_PAGE_V0

## Machine

```yaml
fqdn: webmail::CT_PURE_CHOOSE_FOLDER_PAGE_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_DETERMINISTIC_ATOMS_V0
authority: pgc.platform
concern: mailbox
core:
  summary: Orders identifiers newest received first and cuts the page asked for
  refusal: raises
  inputs:
    message_ids:
      type: array
      required: true
    page:
      type: integer
      required: true
    page_size:
      type: integer
      required: true
  outputs:
    page_ids:
      type: array
      required: true
    more_exist:
      type: boolean
      required: true
    folder_empty:
      type: boolean
      required: true
    message_count:
      type: integer
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: CHOOSE_FOLDER_PAGE
  implementation:
    module: webmail.implementation.capability_transforms.atoms.ct_pure_choose_folder_page_v0
    callable: execute
```

---

## Intent

Orders identifiers newest received first and cuts the page asked for
