# WF_RECLAIM_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::WF_RECLAIM_LICENSE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::WF_AUTO_RECLAIM_V0
runtime_binding: ai_governance::RB_LICENSE_BINDINGS_V1
subdomain: ai_licensing
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: reclaim license'
  actor_context: ai_governance::AC_SYSTEM_V0
  start_node: IN_RECLAIM_LICENSE_V1
  nodes:
    IN_RECLAIM_LICENSE_V1:
      type: IN
      code: IN_RECLAIM_LICENSE_V1
      next:
        ACK: CC_RESOLVE_LICENSE_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_LICENSE_V0:
      type: CC
      code: CC_RESOLVE_LICENSE_V0
      inputs:
        employee_id: $.payload.employee_id
      next:
        SUCCESS: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
        VIOLATION: EXIT_REJECTED
        NOT_FOUND: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0:
      type: CC
      code: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
      inputs:
        last_used_at: $.results.CC_RESOLVE_LICENSE_V0.license_record.last_used_at
      next:
        SUCCESS: CC_RELEASE_LICENSE_IDENTITY_V0
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_STILL_ACTIVE
    CC_RELEASE_LICENSE_IDENTITY_V0:
      type: CC
      code: CC_RELEASE_LICENSE_IDENTITY_V0
      inputs:
        license_id: $.results.CC_RESOLVE_LICENSE_V0.license_record.license_id
      next:
        SUCCESS: CC_MOVE_LICENSE_FROM_ACTIVE_V0
        NOT_FOUND: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_MOVE_LICENSE_FROM_ACTIVE_V0:
      type: CC
      code: CC_MOVE_LICENSE_FROM_ACTIVE_V0
      inputs:
        to_state: RECLAIMED
        license_id: $.results.CC_RESOLVE_LICENSE_V0.license_record.license_id
      next:
        SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_AI_LICENSING_MOMENT_V0:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: LICENSE_REVOKED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_RESOLVE_LICENSE_V0.license_record.license_id
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: ai_governance::EV_LICENSE_REVOKED_V1
    EXIT_REJECTED:
      type: EXIT
    EXIT_STILL_ACTIVE:
      type: EXIT
```

---

## Intent

The governed sequence that performs: reclaim license
