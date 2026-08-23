# EV_EMPLOYEE_REGISTERED_V0

## 1. Fact

An employee has been registered in the system.

---

## 2. Rationale

Employee registration is a fact declaration:
- Injected from HR system
- Creates subject for protocol governance
- Enables downstream provisioning workflows

---

## 3. Emitted By

| Source | Description |
|--------|-------------|
| Fact Injection | HR system declares employee existence |

---

## 4. Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_id | string | true | Unique employee identifier |
| timestamp | string (date-time) | true | When registration occurred |

---

## Machine

```yaml
fqdn: ai_governance::EV_EMPLOYEE_REGISTERED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: Employee Registered
  description: Emitted when an employee is registered in the system

  schema:
    employee_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```
