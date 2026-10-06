# WF_ACCEPT_ACTOR_V1

## Machine

```yaml
fqdn: blockchain::WF_ACCEPT_ACTOR_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::WF_ACCEPT_ACTOR_V0
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that records an acceptance and announces it
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_ACCEPTANCE_V0
  nodes:
    IN_ACTOR_ACCEPTANCE_V0:
      type: IN
      code: IN_ACTOR_ACCEPTANCE_V0
      next:
        ACK: CC_RESOLVE_ACTOR_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_ACTOR_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_V1
      inputs:
        contact_address: $.payload.contact_address
      next:
        SUCCESS: CC_RECORD_VERIFICATION_DECISION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_VERIFICATION_DECISION_V0:
      type: CC
      code: CC_RECORD_VERIFICATION_DECISION_V0
      inputs:
        current_state: $.results.CC_RESOLVE_ACTOR_V0.value.state
        decision: ACCEPTED
        verifying_authority: $.payload.verifying_authority
        contact_address: $.payload.contact_address
        grounds: $.payload.grounds
      next:
        SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
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
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_SUCCESS:
      type: EXIT
      emit: blockchain::EV_ACTOR_ACCEPTED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that records an acceptance and announces it
