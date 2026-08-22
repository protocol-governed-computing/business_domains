# CC_RECLAIM_UNUSED_LICENSE_V0

## Header (Mandatory)

- **Artifact Code:** CC_RECLAIM_UNUSED_LICENSE_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CT_PURE_EVALUATE_INACTIVITY_V0, CS_REGISTRY_V0

---

## 1. Intent

Reclaim a license from an inactive user.

---

## 2. Rationale

Autonomous reclamation enforces use-it-or-lose-it:
- Evaluates inactivity against threshold
- Deregisters license if inactive
- Returns license to pool without human intervention

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_EVALUATE_INACTIVITY_V0 | CT | Evaluate |
| 2 | CS_REGISTRY_V0 | CS | DEREGISTER |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| license_id | string | true | License to evaluate |
| employee_id | string | true | Employee holding license |
| last_active_date | string (date-time) | true | Last usage date |
| threshold_days | integer | true | Inactivity threshold (default: 30) |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| result_status | string | Operation result |
| is_inactive | boolean | Whether user is inactive |
| days_inactive | integer | Number of days inactive |

---

## 6. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | License reclaimed successfully |
| ACTIVE | User is still active, no reclamation |
| NOT_FOUND | License not in registry |
| BACKEND_ERROR | Registry unavailable |

---

## Machine

```yaml
fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: ai_licensing

core:
  summary: Reclaim license from inactive user

  inputs:
    license_id:
      type: string
      required: true
    employee_id:
      type: string
      required: true
    last_active_date:
      type: string
      format: date-time
      required: true
    evaluation_date:
      type: string
      format: date-time
      required: true
    threshold_days:
      type: integer
      required: true
      default: 30

  outputs:
    result_status:
      type: string
    is_inactive:
      type: boolean
    days_inactive:
      type: integer

  result_status_contract:
    allowed: [SUCCESS, VIOLATION, NOT_FOUND, BACKEND_ERROR]
    on_input_failure: VIOLATION

  pipeline:
    - step: evaluate_inactivity
      transform: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
      inputs:
        last_active_date: $.inputs.last_active_date
        evaluation_date: $.inputs.evaluation_date
        threshold_days: $.inputs.threshold_days
      outputs:
        is_inactive: $.capability_result.is_inactive
        days_inactive: $.capability_result.days_inactive
      result_surface: [SUCCESS, VIOLATION]
      on_result:
        SUCCESS: continue
        VIOLATION: exit

    - step: deregister_license
      side_effect: capability_side_effects::CS_REGISTRY_V0
      op: DEREGISTER
      inputs:
        key_or_address: $.inputs.employee_id
      outputs:
        result_status: $.result_status
      result_surface: [SUCCESS, NOT_FOUND, BACKEND_ERROR]
      on_result:
        SUCCESS: exit
        NOT_FOUND: exit
        BACKEND_ERROR: exit

extensions:
  description: Evaluates inactivity and reclaims license if threshold exceeded
```
