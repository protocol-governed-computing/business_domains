# AC_PARTICIPANT_V0

## Header (Mandatory)

- **Artifact Code:** AC_PARTICIPANT_V0
- **Artifact Kind:** actor
- **Governed By:** CONSTITUTION_GOVERNANCE_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The ordinary participant who registers themselves and is decided about

---

## Machine

```yaml
fqdn: blockchain::AC_PARTICIPANT_V0
artifact_kind: ACTOR
version: v0
governed_by: fb.governance::CONSTITUTION_GOVERNANCE_V0
core:
  summary: The ordinary participant who registers themselves and is decided about
  type: ENDUSER
  attributes:
    contact_address:
      type: string
      required: true
    name:
      type: string
      required: true
    currency_preference:
      type: string
      default: BACHI
    language:
      type: string
      default: en
```
