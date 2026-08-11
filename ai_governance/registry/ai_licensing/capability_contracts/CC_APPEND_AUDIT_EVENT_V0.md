# CC_APPEND_AUDIT_EVENT_V0

## Header (Mandatory)

- **Artifact Code:** CC_APPEND_AUDIT_EVENT_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CS_APPENDONLY_JSONL_V0

---

## 1. Intent

Append a decision event to the immutable audit log.

---

## 2. Rationale

Audit logging is a protocol requirement:
- Every denial path must invoke this contract
- Creates immutable compliance record
- Proves "nothing happened" is provable

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CS_APPENDONLY_JSONL_V0 | CS | APPEND |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| event_type | string | true | Event type code |
| employee_id | string | true | Subject of the decision |
| decision | string | true | Decision made (PROVISIONED, DENIED, RECLAIMED) |
| reason_code | string | false | Reason for decision |
| license_id | string | false | License ID to record in event |
| data | object | false | Additional event data |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| result_status | string | Operation result |

---

## 6. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | Event appended successfully |
| VIOLATION | Invalid input format |
| BACKEND_ERROR | Audit log unavailable |

---

## Machine

```yaml
fqdn: ai_governance::CC_APPEND_AUDIT_EVENT_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: fb.capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0

core:
  summary: Append decision event to audit log

  inputs:
    event_type:
      type: string
      required: true
    employee_id:
      type: string
      required: true
    decision:
      type: string
      enum:
        - PROVISIONED
        - DENIED
        - RECLAIMED
      required: true
    reason_code:
      type: string
    license_id:
      type: string
    data:
      type: object

  outputs:
    result_status:
      type: string

  result_status_contract:
    allowed: [SUCCESS, VIOLATION, BACKEND_ERROR]
    on_input_failure: VIOLATION

  pipeline:
    - step: read_now
      side_effect: capability_side_effects::CS_CLOCK_V0
      op: NOW
      inputs: {}
      outputs:
        timestamp: $.capability_result.timestamp
      result_surface: [SUCCESS, BACKEND_ERROR]
      on_result:
        SUCCESS: continue
        BACKEND_ERROR: exit

    - step: append_audit_event
      side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
      op: APPEND
      store: LICENSE_AUDIT
      inputs:
        record:
          event_type: $.inputs.event_type
          employee_id: $.inputs.employee_id
          decision: $.inputs.decision
          reason_code: $.inputs.reason_code
          license_id: $.inputs.license_id
          payload: $.inputs.data
          timestamp: $.results.read_now.timestamp
      outputs:
        result_status: $.result_status
      result_surface: [SUCCESS, VIOLATION, BACKEND_ERROR]
      on_result:
        SUCCESS: exit
        VIOLATION: exit
        BACKEND_ERROR: exit

extensions:
  description: Appends audit event for compliance and provability
```
