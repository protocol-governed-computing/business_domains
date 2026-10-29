# WF_SET_LICENSE_CAP_V0

## Machine

```yaml
fqdn: ai_governance::WF_SET_LICENSE_CAP_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: ai_licensing
runtime_binding: ai_governance::RB_LICENSE_BINDINGS_V1
subdomain: ai_licensing
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: set license cap'
  actor_context: ai_governance::AC_SYSTEM_V0
  start_node: IN_SET_LICENSE_CAP_V0
  nodes:
    IN_SET_LICENSE_CAP_V0:
      type: IN
      code: IN_SET_LICENSE_CAP_V0
      next:
        ACK: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
        NACK: EXIT_REJECTED
    CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0:
      type: CC
      code: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
      inputs:
        submission:
          cap: $.payload.cap
      next:
        SUCCESS: CC_WRITE_LICENSE_CAP_V0
        VIOLATION: EXIT_REJECTED
    CC_WRITE_LICENSE_CAP_V0:
      type: CC
      code: CC_WRITE_LICENSE_CAP_V0
      inputs:
        submission:
          cap: $.payload.cap
      next:
        SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_AI_LICENSING_MOMENT_V0:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: LICENSE_CAP_SET
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: ai_governance::EV_LICENSE_CAP_SET_V1
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: set license cap
