# CC_RECORD_DENIED_ACTION_V0

## Header (Mandatory)

- **Artifact Code:** CC_RECORD_DENIED_ACTION_V0
- **Artifact Kind:** capability_contract
- **Governed By:** CONSTITUTION_CAPABILITY_CONTRACT_V0
- **Version:** v0
- **Status:** draft
- **Supersedes:** NONE
- **Dependencies:** CT_PURE_GENERATE_ID_V0, CS_APPENDONLY_JSONL_V0

---

## 1. Intent

Record a denied governance decision and emit an audit trail.

---

## 2. Rationale

Denial recording is symmetric with authorization:
- Every governance denial produces an audit record
- Denial reason is deterministic and classified
- Enforces Invariant I-A6 (Deterministic Trace)
- Used by four WF node instances — one per denial path

---

## 3. Pipeline

| Step | Capability | Type | Operation |
|------|------------|------|-----------|
| 1 | CT_PURE_GENERATE_ID_V0 | CT | GENERATE_ID |
| 2 | CS_APPENDONLY_JSONL_V0 | CS | APPEND |

---

## 4. Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| tool_name | string | true | Requested tool |
| requesting_user_id | string | true | User the agent acts for |
| domain_context | string | true | Domain context |
| denial_reason | string | true | Structural denial reason code |

---

## 5. Outputs

| Field | Type | Description |
|-------|------|-------------|
| action_id | string | Generated governance action identifier |
| result_status | string | Operation result |

---

## 6. Result Status Contract

| Status | Condition |
|--------|-----------|
| SUCCESS | Denial recorded and audited |
| VIOLATION | Invalid input |
| BACKEND_ERROR | Storage unavailable |

---

## Machine

```yaml
fqdn: ai_governance::CC_RECORD_DENIED_ACTION_V0
artifact_kind: CAPABILITY_CONTRACT
version: v0
governed_by: capability_contracts::CONSTITUTION_CAPABILITY_CONTRACT_V0
authority: pgc.platform
concern: agent_governance

core:
  summary: Record denied governance decision and emit audit trail

  inputs:
    tool_name:
      type: string
      required: true
    requesting_user_id:
      type: string
      required: true
    domain_context:
      type: string
      required: true
    denial_reason:
      type: string
      required: true

  outputs:
    action_id:
      type: string
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

    - step: generate_action_id
      transform: capability_transforms::CT_PURE_GENERATE_ID_V0
      inputs:
        prefix: "AGOV"
        data:
          tool_name: $.inputs.tool_name
          requesting_user_id: $.inputs.requesting_user_id
          domain_context: $.inputs.domain_context
      outputs:
        action_id: $.capability_result.id
      result_surface: [SUCCESS, VIOLATION]
      on_result:
        SUCCESS: continue
        VIOLATION: exit

    - step: append_denial_record
      side_effect: capability_side_effects::CS_APPENDONLY_JSONL_V0
      op: APPEND
      store: GOVERNANCE_AUDIT
      inputs:
        record:
          event_code: "EV_AGENT_ACTION_DENIED_V0"
          action_id: $.results.generate_action_id.action_id
          tool_name: $.inputs.tool_name
          requesting_user_id: $.inputs.requesting_user_id
          denial_reason: $.inputs.denial_reason
          decision: "DENIED"
          timestamp: $.results.read_now.timestamp
      outputs:
        result_status: $.capability_result.result_status
        action_id: $.results.generate_action_id.action_id
      result_surface: [SUCCESS, VIOLATION, BACKEND_ERROR]
      on_result:
        SUCCESS: continue
        VIOLATION: exit
        BACKEND_ERROR: exit

extensions:
  description: Records denied governance decision with symmetric audit — used by four denial path node instances
```
