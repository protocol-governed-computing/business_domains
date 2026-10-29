# WF_RECORD_LICENSE_USAGE_V0

## Machine

```yaml
fqdn: ai_governance::WF_RECORD_LICENSE_USAGE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: ai_licensing
runtime_binding: ai_governance::RB_LICENSE_BINDINGS_V1
subdomain: ai_licensing
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: record license usage'
  actor_context: ai_governance::AC_EMPLOYEE_V1
  start_node: IN_RECORD_LICENSE_USAGE_V0
  nodes:
    IN_RECORD_LICENSE_USAGE_V0:
      type: IN
      code: IN_RECORD_LICENSE_USAGE_V0
      next:
        ACK: CC_RESOLVE_LICENSE_V0
        NACK: EXIT_REJECTED
    CC_RESOLVE_LICENSE_V0:
      type: CC
      code: CC_RESOLVE_LICENSE_V0
      inputs:
        employee_id: $.payload.employee_id
      next:
        SUCCESS: CC_RECORD_LICENSE_USAGE_V0
        VIOLATION: EXIT_REJECTED
        NOT_FOUND: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_LICENSE_USAGE_V0:
      type: CC
      code: CC_RECORD_LICENSE_USAGE_V0
      inputs:
        license_id: $.results.CC_RESOLVE_LICENSE_V0.license_record.license_id
      next:
        SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_RECORD_AI_LICENSING_MOMENT_V0:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: USAGE_RECORDED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_RESOLVE_LICENSE_V0.license_record.license_id
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: ai_governance::EV_USAGE_RECORDED_V1
    EXIT_REJECTED:
      type: EXIT
```

---

## Intent

The governed sequence that performs: record license usage
