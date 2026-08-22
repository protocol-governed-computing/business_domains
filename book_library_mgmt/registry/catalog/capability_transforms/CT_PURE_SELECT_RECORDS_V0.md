# CT_PURE_SELECT_RECORDS_V0

## 1. Intent

Selects the records matching stated criteria and returns none when none match

---

## Machine

```yaml
fqdn: book_library_mgmt::CT_PURE_SELECT_RECORDS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: catalog
core:
  summary: Selects the records matching stated criteria and returns none when none match
  refusal: never
  inputs:
    source:
      type: array
      required: true
    filter:
      type: object
      required: true
  outputs:
    extracted:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_SELECT_RECORDS
  implementation:
    module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_select_records_v0
    callable: execute
```
