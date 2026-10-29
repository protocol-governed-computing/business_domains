# WF_REJECT_ACTOR_V1

## Machine

```yaml
fqdn: blockchain::WF_REJECT_ACTOR_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: identity
supersedes: blockchain::WF_REJECT_ACTOR_V0
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: reject actor'
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_ACTOR_REJECTION_V0
  nodes:
    IN_ACTOR_REJECTION_V0:
      type: IN
      code: IN_ACTOR_REJECTION_V0
      next:
        ACK: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
        NACK: EXIT_REJECTED
    CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0:
      type: CC
      code: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
      inputs:
        grounds: $.payload.grounds
      next:
        SUCCESS: CC_RESOLVE_ACTOR_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_ACTOR_IDENTITY_V0:
      type: CC
      code: CC_RESOLVE_ACTOR_IDENTITY_V0
      inputs:
        contact_address: $.payload.contact_address
      next:
        SUCCESS: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_MOVE_ACTOR_FROM_UNVERIFIED_V0:
      type: CC
      code: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
      inputs:
        to_state: REJECTED
        contact_address: $.payload.contact_address
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
      next:
        SUCCESS: CC_RECORD_IDENTITY_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_IDENTITY_MOMENT_V0:
      type: CC
      code: CC_RECORD_IDENTITY_MOMENT_V0
      inputs:
        occurrence: ACTOR_REJECTED
        contact_address: $.payload.contact_address
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
      next:
        SUCCESS: EXIT_COMPLETED
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: blockchain::EV_ACTOR_REJECTED_V0
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: reject actor
