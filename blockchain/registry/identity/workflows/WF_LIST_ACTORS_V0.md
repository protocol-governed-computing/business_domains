# WF_LIST_ACTORS_V0

## Machine

```yaml
fqdn: blockchain::WF_LIST_ACTORS_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: identity
runtime_binding: blockchain::RB_IDENTITY_BINDINGS_V0
subdomain: identity
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: list actors'
  actor_context: blockchain::AC_PARTICIPANT_V0
  start_node: IN_LIST_ACTORS_V0
  nodes:
    IN_LIST_ACTORS_V0:
      type: IN
      code: IN_LIST_ACTORS_V0
      next:
        ACK: CC_RECORD_IDENTITY_MOMENT_V0
        NACK: EXIT_REJECTED
    CC_RECORD_IDENTITY_MOMENT_V0:
      type: CC
      code: CC_RECORD_IDENTITY_MOMENT_V0
      inputs:
        occurrence: LIST_ACTORS
      next:
        SUCCESS: CC_LIST_ACTORS_V0
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_LIST_ACTORS_V0:
      type: CC
      code: CC_LIST_ACTORS_V0
      inputs:
        state: $.payload.state
      next:
        SUCCESS: EXIT_COMPLETED
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: list actors
