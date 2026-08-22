# EV_LICENSE_PROVISIONED_V0

## 1. Fact

A license has been successfully provisioned to an employee.

---

## 2. Rationale

License provisioning is a protocol-governed transition:
- Only occurs when all prerequisites satisfied
- Records assignment for audit trail
- Increments assigned count toward cap

---

## 3. Emitted By

| Workflow | Capability Contract |
|----------|---------------------|
| WF_PROVISION_AI_LICENSING_V0 | CC_PROVISION_LICENSE_V0 |

---

## 4. Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_id | string | true | Employee who received license |
| license_id | string | true | Unique license identifier |
| timestamp | string (date-time) | true | When provisioning occurred |

---

## Machine

```yaml
fqdn: ai_governance::EV_LICENSE_PROVISIONED_V0
artifact_kind: EVENT
version: v0
governed_by: event::CONSTITUTION_EVENT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: License Provisioned
  description: Emitted when a license is successfully provisioned

  schema:
    employee_id:
      type: string
      required: true
    license_id:
      type: string
      required: true
    timestamp:
      type: string
      format: date-time
      required: true
```
