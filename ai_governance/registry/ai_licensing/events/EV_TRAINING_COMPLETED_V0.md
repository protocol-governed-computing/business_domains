# EV_TRAINING_COMPLETED_V0

## 1. Fact

An employee has completed required training.

---

## 2. Rationale

Training completion is a protocol gate:
- Injected from LMS system
- Enables previously blocked provisioning
- Protocol responds automatically (self-healing)

---

## 3. Emitted By

| Source | Description |
|--------|-------------|
| Fact Injection | LMS system declares training completion |

---

## 4. Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_id | string | true | Employee who completed training |
| completion_date | string (date-time) | true | When training was completed |

---

## Machine

```yaml
fqdn: ai_governance::EV_TRAINING_COMPLETED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: Training Completed
  description: Emitted when an employee completes required training

  schema:
    employee_id:
      type: string
      required: true
    completion_date:
      type: string
      format: date-time
      required: true
```
