# AC_LIBRARY_STAFF_V0

## Header (Mandatory)

- **Artifact Code:** AC_LIBRARY_STAFF_V0
- **Artifact Kind:** actor
- **Governed By:** CONSTITUTION_GOVERNANCE_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The library staff member who performs a catalog operation. Whether a given member is authorized is
read, never decided here: granting authorization belongs to the patron subdomain.

---

## Machine

```yaml
fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
artifact_kind: ACTOR
version: v0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0

core:
  summary: Library Staff Actor
  description: Represents a library staff member performing catalog operations
  type: person

  attributes:
    staff_id:
      type: string
      required: true
    authorized:
      type: boolean
      default: false
```
