# AC_ENTERPRISE_RUNTIME_V0

## 1. Identity

The isolated side-effect executor that performs authorized actions.

---

## 2. Rationale

The enterprise runtime executes governed side effects:
- Receives only authorized actions from the governance pipeline
- Executes within isolated capability boundaries
- Produces auditable persistence records

---

## 3. Type

| Property | Value |
|----------|-------|
| Type | system |

---

## 4. Attributes

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| runtime_id | string | true | Runtime executor identifier |

---

## Machine

```yaml
fqdn: ai_governance::AC_ENTERPRISE_RUNTIME_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: agent_governance

core:
  summary: Isolated side-effect executor
  description: Executes authorized actions within isolated capability boundaries
  type: system

  attributes:
    runtime_id:
      type: string
      required: true
```
