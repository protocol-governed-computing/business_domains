# WF_REJECT_ACTOR_V0

## Header (Mandatory)

- **Artifact Code:** WF_REJECT_ACTOR_V0
- **Artifact Kind:** workflow
- **Governed By:** CONSTITUTION_WORKFLOW_V0
- **Version:** V0
- **Status:** draft
- **Supersedes:** WF_RECORD_VERIFICATION_DECISION_V0

---

## 1. Intent

The governed sequence that records a rejection, with grounds required, and announces it

---

## Machine

```yaml
fqdn: blockchain::WF_REJECT_ACTOR_V0
artifact_kind: WORKFLOW
version: v0
governed_by: fb.workflow::CONSTITUTION_WORKFLOW_V0
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: fb.execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: The governed sequence that records a rejection, with grounds required, and announces it
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_REJECTION_V0
  nodes:
    IN_ACTOR_REJECTION_V0:
      type: IN
      code: IN_ACTOR_REJECTION_V0
      next:
        ACK: CC_REQUIRE_REJECTION_GROUNDS_V0
        NACK: EXIT_REJECTED
    CC_REQUIRE_REJECTION_GROUNDS_V0:
      type: CC
      code: CC_REQUIRE_REJECTION_GROUNDS_V0
      inputs:
        grounds: $.payload.grounds
        grounds_rules: $.payload.grounds_rules
      next:
        SUCCESS: CC_RESOLVE_ACTOR_V0
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_ACTOR_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_V0
      next:
        SUCCESS: CC_RECORD_VERIFICATION_DECISION_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_RECORD_VERIFICATION_DECISION_V0:
      type: CC
      code: CC_RECORD_VERIFICATION_DECISION_V0
      next:
        SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
        VIOLATION: EXIT_REJECTED
    CC_APPEND_ACTOR_OCCURRENCE_V0:
      type: CC
      code: CC_APPEND_ACTOR_OCCURRENCE_V0
      next:
        SUCCESS: EXIT_SUCCESS
        VIOLATION: EXIT_REJECTED
    EXIT_SUCCESS:
      type: EXIT
      emit: blockchain::EV_ACTOR_REJECTED_V0
    EXIT_REJECTED:
      type: EXIT
```
