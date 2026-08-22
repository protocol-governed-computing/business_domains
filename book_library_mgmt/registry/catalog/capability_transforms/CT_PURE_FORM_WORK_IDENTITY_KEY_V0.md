# CT_PURE_FORM_WORK_IDENTITY_KEY_V0

## Header (Mandatory)

- **Artifact Code:** CT_PURE_FORM_WORK_IDENTITY_KEY_V0
- **Artifact Kind:** capability_transform
- **Governed By:** CONSTITUTION_CAPABILITY_TRANSFORMS_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

Forms the single key claimed for a work from its title and author

---

## Machine

```yaml
fqdn: book_library_mgmt::CT_PURE_FORM_WORK_IDENTITY_KEY_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: catalog
core:
  summary: Forms the single key claimed for a work from its title and author
  refusal: never
  inputs:
    title:
      type: string
      required: true
    author:
      type: string
      required: true
  outputs:
    work_key:
      type: string
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_FORM_WORK_IDENTITY_KEY
  implementation:
    module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_form_work_identity_key_v0
    callable: execute
```
