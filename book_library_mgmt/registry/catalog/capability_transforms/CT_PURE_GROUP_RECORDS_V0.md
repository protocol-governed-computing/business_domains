# CT_PURE_GROUP_RECORDS_V0

## 1. Intent

Groups records by the value of a named attribute, returning one group per distinct value

---

## Machine

```yaml
fqdn: book_library_mgmt::CT_PURE_GROUP_RECORDS_V0
artifact_kind: CAPABILITY_TRANSFORM
version: v0
governed_by: capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0
authority: pgc.platform
concern: catalog
core:
  summary: Groups records by the value of a named attribute, returning one group per distinct value
  refusal: never
  inputs:
    source:
      type: array
      required: true
    attribute:
      type: string
      required: true
  outputs:
    grouped:
      type: array
      required: true
machine:
  ct_kind: atom
  ct_purity: ct_pure
  operation: PURE_GROUP_RECORDS
  implementation:
    module: book_library_mgmt.implementation.capability_transforms.atoms.ct_pure_group_records_v0
    callable: execute
```
