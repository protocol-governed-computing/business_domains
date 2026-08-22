# IN_PROVISION_AI_LICENSE_V0

## 1. Intent

Request to provision an AI license for an employee.

---

## 2. Rationale

License provisioning intent is a protocol entry point:
- Declares desired outcome (employee gets license)
- Protocol evaluates eligibility
- Outcome is deterministic (PROVISIONED or DENIED)

---

## 3. Workflow Binding

| Target | Description |
|--------|-------------|
| WF_PROVISION_AI_LICENSING_V0 | Workflow that processes this intent |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_id | string | true | Employee requesting license |
| context | object | false | Runtime context data (training_completed, assigned_count, cap, reason_code) |
| generated | object | false | Generated data (license_id) |

---

## 5. Outcomes

| Outcome | Description |
|---------|-------------|
| ACK | Provisioning request accepted for processing |
| NACK | Provisioning request rejected |

---

## 6. Domain

- **Domain:** pgs.ai_licensing

---

## Machine

```yaml
fqdn: ai_governance::IN_PROVISION_AI_LICENSE_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: Request AI license provisioning
  workflow: WF_PROVISION_AI_LICENSING_V0

  inputs:
    employee_id:
      type: string
      required: true
      description: Employee requesting license
    context:
      type: object
      required: false
      description: Runtime context data (training_completed, assigned_count, cap, reason_code)
    generated:
      type: object
      required: false
      description: Generated data (license_id)

  outcomes:
    ACK:
      description: Provisioning request accepted for processing
    NACK:
      description: Provisioning request rejected

extensions:
  domain: pgs.testbed
```
