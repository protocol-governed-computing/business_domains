# WF_RECORD_VERIFICATION_DECISION_V0

## Header (Mandatory)

- **Artifact Code:** WF_RECORD_VERIFICATION_DECISION_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** NONE

---

## 1. Intent

The governed sequence that records a decision against a registered actor

---

## Machine

```yaml
fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that records a decision against a registered actor
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_VERIFIED_V0
  nodes:
    IN_ACTOR_VERIFIED_V0:
      type: IN
      code: IN_ACTOR_VERIFIED_V0
      next:
        ACK: CC_RESOLVE_ACTOR_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_ACTOR_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_V0
      inputs:
        contact_address: $.payload.contact_address
      next:
        SUCCESS: CC_RECORD_VERIFICATION_DECISION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_RECORD_VERIFICATION_DECISION_V0:
      type: CC
      code: CC_RECORD_VERIFICATION_DECISION_V0
      inputs:
        current_state: $.results.CC_RESOLVE_ACTOR_V0.value.state
        states_admitting_a_decision: $.payload.states_admitting_a_decision
        decision: $.payload.decision
        admitted_outcomes: $.payload.admitted_outcomes
        verifying_authority: $.payload.verifying_authority
        contact_address: $.payload.contact_address
        decided_actor_fields: $.payload.decided_actor_fields
      next:
        SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
    CC_APPEND_ACTOR_OCCURRENCE_V0:
      type: CC
      code: CC_APPEND_ACTOR_OCCURRENCE_V0
      inputs:
        occurrence_fields: $.payload.occurrence_fields
        stream_id: $.payload.stream_id
        contact_address: $.payload.contact_address
      next:
        SUCCESS: EXIT_SUCCESS
        VIOLATION: EXIT_REJECTED
    EXIT_REJECTED:
      type: EXIT
    EXIT_SUCCESS:
      type: EXIT
```
