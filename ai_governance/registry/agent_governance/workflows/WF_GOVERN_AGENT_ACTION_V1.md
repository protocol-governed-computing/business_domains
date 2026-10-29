# WF_GOVERN_AGENT_ACTION_V1

## Machine

```yaml
fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V1
artifact_kind: WORKFLOW
version: v1
governed_by: workflow::CONSTITUTION_WORKFLOW_V0
authority: pgc.platform
concern: agent_governance
supersedes: ai_governance::WF_GOVERN_AGENT_ACTION_V0
runtime_binding: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
consults:
- ai_governance::RB_LICENSE_BINDINGS_V1
subdomain: agent_governance
structure: execution::STRUCTURE_RUNTIME_EXECUTION_V0
core:
  summary: 'The governed sequence that performs: govern agent action'
  actor_context: ai_governance::AC_AGENT_V0
  start_node: IN_AGENT_ACTION_REQUESTED_V1
  nodes:
    IN_AGENT_ACTION_REQUESTED_V1:
      type: IN
      code: IN_AGENT_ACTION_REQUESTED_V1
      next:
        ACK: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
        NACK: EXIT_REJECTED
    CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0:
      type: CC
      code: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
      inputs:
        submission:
          tool_name: $.payload.tool_name
          requesting_user_id: $.payload.requesting_user_id
      next:
        SUCCESS: CC_REQUIRE_TOOL_DECLARED_V0
        VIOLATION: EXIT_REJECTED
    CC_REQUIRE_TOOL_DECLARED_V0:
      type: CC
      code: CC_REQUIRE_TOOL_DECLARED_V0
      inputs:
        tool_name: $.payload.tool_name
      next:
        SUCCESS: CC_RESOLVE_LICENSE_V0
        VIOLATION: CC_DENY_UNDECLARED_TOOL
    CC_RESOLVE_LICENSE_V0:
      type: CC
      code: CC_RESOLVE_LICENSE_V0
      inputs:
        employee_id: $.payload.requesting_user_id
      next:
        SUCCESS: CC_REQUIRE_LICENSE_ACTIVE_V0
        VIOLATION: CC_DENY_UNAUTHORIZED_ACTOR
        NOT_FOUND: CC_DENY_UNAUTHORIZED_ACTOR
        BACKEND_ERROR: EXIT_REJECTED
    CC_REQUIRE_LICENSE_ACTIVE_V0:
      type: CC
      code: CC_REQUIRE_LICENSE_ACTIVE_V0
      inputs:
        state: $.results.CC_RESOLVE_LICENSE_V0.license_record.state
      next:
        SUCCESS: CC_REQUIRE_TIER_GRANTS_TOOL_V0
        VIOLATION: CC_DENY_UNAUTHORIZED_ACTOR
    CC_REQUIRE_TIER_GRANTS_TOOL_V0:
      type: CC
      code: CC_REQUIRE_TIER_GRANTS_TOOL_V0
      inputs:
        key: $.results.CC_RESOLVE_LICENSE_V0.license_record.tier
        tool_name: $.payload.tool_name
      next:
        SUCCESS: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
        VIOLATION: CC_DENY_UNAUTHORIZED_TOOL
    CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0:
      type: CC
      code: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
      inputs:
        key: $.payload.tool_name
        parameters: $.payload.parameters
      next:
        SUCCESS: CC_FORM_ACTION_REQUEST_IDENTITY_V0
        VIOLATION: CC_DENY_PARAMETER_VIOLATION
    CC_FORM_ACTION_REQUEST_IDENTITY_V0:
      type: CC
      code: CC_FORM_ACTION_REQUEST_IDENTITY_V0
      inputs:
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        domain_context: $.payload.domain_context
      next:
        SUCCESS: CC_CLAIM_ACTION_IDENTITY_V0
        VIOLATION: EXIT_REJECTED
    CC_CLAIM_ACTION_IDENTITY_V0:
      type: CC
      code: CC_CLAIM_ACTION_IDENTITY_V0
      inputs:
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        domain_context: $.payload.domain_context
        action_fields:
          tool_name: $.payload.tool_name
          requesting_user_id: $.payload.requesting_user_id
      next:
        SUCCESS: CC_WRITE_ACTION_V0
        VIOLATION: EXIT_REJECTED
        ALREADY_EXISTS: CC_WRITE_ACTION_V0
        BACKEND_ERROR: EXIT_REJECTED
    CC_WRITE_ACTION_V0:
      type: CC
      code: CC_WRITE_ACTION_V0
      inputs:
        action_id: $.results.CC_CLAIM_ACTION_IDENTITY_V0.action_id
        submission:
          tool_name: $.payload.tool_name
          requesting_user_id: $.payload.requesting_user_id
        request_identity: $.results.CC_FORM_ACTION_REQUEST_IDENTITY_V0.request_identity
      next:
        SUCCESS: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0:
      type: CC
      code: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      inputs:
        occurrence: AGENT_ACTION_AUTHORIZED
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        reason: $.payload.parameters.reason
      next:
        SUCCESS: EXIT_COMPLETED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_UNDECLARED_TOOL:
      type: CC
      code: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      inputs:
        occurrence: AGENT_ACTION_DENIED
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        reason: UNDECLARED_TOOL
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_UNAUTHORIZED_ACTOR:
      type: CC
      code: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      inputs:
        occurrence: AGENT_ACTION_DENIED
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        reason: UNAUTHORIZED_ACTOR
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_UNAUTHORIZED_TOOL:
      type: CC
      code: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      inputs:
        occurrence: AGENT_ACTION_DENIED
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        reason: UNAUTHORIZED_TOOL
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    CC_DENY_PARAMETER_VIOLATION:
      type: CC
      code: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      inputs:
        occurrence: AGENT_ACTION_DENIED
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
        reason: PARAMETER_VIOLATION
      next:
        SUCCESS: EXIT_DENIED
        VIOLATION: EXIT_REJECTED
        BACKEND_ERROR: EXIT_REJECTED
    EXIT_COMPLETED:
      type: EXIT
      emit: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    EXIT_REJECTED:
      type: EXIT
    EXIT_DENIED:
      type: EXIT
      emit: ai_governance::EV_AGENT_ACTION_DENIED_V1
```

---

## Intent

The governed sequence that performs: govern agent action
