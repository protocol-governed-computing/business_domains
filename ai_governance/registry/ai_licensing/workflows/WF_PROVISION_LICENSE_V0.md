# WF_PROVISION_LICENSE_V0

## Machine

```yaml
fqdn: ai_governance::WF_PROVISION_LICENSE_V0
artifact_kind: WORKFLOW
version: v0
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: ai_licensing
supersedes: ai_governance::WF_PROVISION_AI_LICENSING_V0
runtime_binding: ai_governance::RB_LICENSE_BINDINGS_V1
subdomain: ai_licensing
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: provision license'
  actor_context: ai_governance::AC_EMPLOYEE_V1
  start_node: IN_PROVISION_LICENSE_V0
  nodes:
    IN_PROVISION_LICENSE_V0:
      type: IN
      code: IN_PROVISION_LICENSE_V0
      next:
        ACK: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
        NACK: EXIT_REJECTED
    CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0:
      type: CC
      code: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
      inputs:
        submission:
          employee_id: $.payload.employee_id
          tier: $.payload.tier
      next:
        SUCCESS: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_RESOLVE_EMPLOYEE_IDENTITY_V0:
      type: CC
      code: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
      inputs:
        employee_id: $.payload.employee_id
      next:
        SUCCESS: CC_REQUIRE_TRAINING_COMPLETED_V0
        NOT_FOUND: CC_DENY_TRAINING_COMPLETED
        VIOLATION: CC_DENY_TRAINING_COMPLETED
        BACKEND_ERROR: EXIT_REJECTED
    CC_REQUIRE_TRAINING_COMPLETED_V0:
      type: CC
      code: CC_REQUIRE_TRAINING_COMPLETED_V0
      inputs:
        training_completed: $.results.CC_RESOLVE_EMPLOYEE_IDENTITY_V0.employee_record.training_completed
      next:
        SUCCESS: CC_REQUIRE_TIER_ADMITTED_V0
        VIOLATION: CC_DENY_TRAINING_COMPLETED
    CC_REQUIRE_TIER_ADMITTED_V0:
      type: CC
      code: CC_REQUIRE_TIER_ADMITTED_V0
      inputs:
        tier: $.payload.tier
      next:
        SUCCESS: CC_REQUIRE_CAP_SET_V0
        VIOLATION: CC_DENY_TIER_ADMITTED
    CC_REQUIRE_CAP_SET_V0:
      type: CC
      code: CC_REQUIRE_CAP_SET_V0
      inputs:
        cap_key: current
      next:
        SUCCESS: CC_REQUIRE_UNDER_THE_CAP_V0
        NOT_FOUND: CC_DENY_CAP_SET
        VIOLATION: CC_DENY_CAP_SET
        BACKEND_ERROR: EXIT_REJECTED
    CC_REQUIRE_UNDER_THE_CAP_V0:
      type: CC
      code: CC_REQUIRE_UNDER_THE_CAP_V0
      inputs:
        cap: $.results.CC_REQUIRE_CAP_SET_V0.cap_record.cap
      next:
        SUCCESS: CC_CLAIM_LICENSE_IDENTITY_V0
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: CC_DENY_UNDER_THE_CAP
    CC_CLAIM_LICENSE_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_LICENSE_IDENTITY_V0
      inputs:
        employee_id: $.payload.employee_id
      next:
        SUCCESS: CC_WRITE_LICENSE_V0
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: CC_DENY_LICENSE_ALREADY_HELD
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_LICENSE_V0:
      type: CC
      code: CC_WRITE_LICENSE_V0
      inputs:
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        submission:
          employee_id: $.payload.employee_id
          tier: $.payload.tier
      next:
        SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
        BACKEND_ERROR: EXIT_REJECTED
        VIOLATION: EXIT_REJECTED
    CC_RECORD_AI_LICENSING_MOMENT_V0:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: LICENSE_PROVISIONED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_TRAINING_COMPLETED:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: PROVISION_DENIED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
        reason: TRAINING_COMPLETED
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_TIER_ADMITTED:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: PROVISION_DENIED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
        reason: TIER_ADMITTED
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_CAP_SET:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: PROVISION_DENIED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
        reason: CAP_SET
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_UNDER_THE_CAP:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: PROVISION_DENIED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
        reason: UNDER_THE_CAP
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_LICENSE_ALREADY_HELD:
      type: CC
      code: CC_RECORD_AI_LICENSING_MOMENT_V0
      inputs:
        occurrence: PROVISION_DENIED
        employee_id: $.payload.employee_id
        license_id: $.results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
        tier: $.payload.tier
        reason: LICENSE_ALREADY_HELD
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: ai_governance::EV_LICENSE_PROVISIONED_V1
    EXIT_REJECTED:
      type: EXIT
    EXIT_DENIED:
      type: EXIT
      emit: ai_governance::EV_PROVISION_DENIED_V1
```

---

## Intent

The governed sequence that performs: provision license
