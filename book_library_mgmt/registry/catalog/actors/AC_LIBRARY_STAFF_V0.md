# AC_LIBRARY_STAFF_V0

## 1. Intent

The actor whose authorization every catalog operation binds

---

## Machine

```yaml
fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: catalog
core:
  summary: The actor whose authorization every catalog operation binds
  type: ENDUSER
  attributes:
    staff_id:
      type: string
      required: true
    authorized:
      type: boolean
      default: false
```
