# AC_SYSTEM_GOVERNOR_V0

## 1. Identity

The governance execution authority that mediates agent-proposed actions.

---

## 2. Rationale

The system governor enforces protocol governance:
- Evaluates agent requests against declared policy
- Binds license authority to tool surfaces
- Records all governance decisions (authorization and denial)

---

## 3. Type

| Property | Value |
|----------|-------|
| Type | system |

---

## 4. Attributes

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| governor_id | string | true | Governance authority identifier |

---

## Machine

```yaml
fqdn: ai_governance::AC_SYSTEM_GOVERNOR_V0
artifact_kind: ACTOR
version: v0
governed_by: governance::CONSTITUTION_GOVERNANCE_V0
authority: pgc.platform
concern: agent_governance

core:
  summary: Governance execution authority
  description: Mediates agent-proposed actions with constitutional policy enforcement
  type: system

  attributes:
    governor_id:
      type: string
      required: true
```
