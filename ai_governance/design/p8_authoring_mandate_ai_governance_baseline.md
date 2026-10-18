# Authoring Mandate — ai_governance, baseline

## Machine

```yaml
document:
  phase: p8
  domain: ai_governance
  subdomain:
  - agent_governance
  - ai_licensing
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P8_V0
registers:
  build_order:
  - wave: '1'
    step: '1'
    code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '2'
    code: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '3'
    code: ai_governance::VOCAB_AI_LICENSING_STATES_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '4'
    code: ai_governance::AC_AGENT_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '5'
    code: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '6'
    code: ai_governance::AC_SYSTEM_GOVERNOR_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '7'
    code: ai_governance::AC_EMPLOYEE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '8'
    code: ai_governance::AC_SYSTEM_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '9'
    code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '10'
    code: ai_governance::EV_AGENT_ACTION_DENIED_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '11'
    code: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '12'
    code: ai_governance::EV_LICENSE_CAP_SET_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '13'
    code: ai_governance::EV_LICENSE_PROVISIONED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '14'
    code: ai_governance::EV_LICENSE_REVOKED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '15'
    code: ai_governance::EV_PROVISION_DENIED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '16'
    code: ai_governance::EV_TRAINING_COMPLETED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '17'
    code: ai_governance::EV_USAGE_RECORDED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '18'
    code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '19'
    code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '20'
    code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '21'
    code: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '22'
    code: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '23'
    code: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '24'
    code: ai_governance::CC_RECORD_DENIED_ACTION_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '25'
    code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '26'
    code: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '27'
    code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '28'
    code: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '29'
    code: ai_governance::CC_PROVISION_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '30'
    code: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '31'
    code: ai_governance::IN_DENY_PROVISION_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '32'
    code: ai_governance::IN_PROVISION_AI_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '33'
    code: ai_governance::IN_RECLAIM_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '2'
    step: '34'
    code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
  - wave: '2'
    step: '35'
    code: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    - ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
  - wave: '2'
    step: '36'
    code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    action: NEW
    subdomain: agent_governance
    depends_on:
    - ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - wave: '2'
    step: '37'
    code: ai_governance::RB_LICENSE_BINDINGS_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - wave: '3'
    step: '38'
    code: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    action: NEW
    subdomain: agent_governance
    depends_on:
    - ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    - ai_governance::AC_SYSTEM_GOVERNOR_V0
    - ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
    - ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    - ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    - ai_governance::CC_CHECK_TOOL_DECLARED_V0
    - ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    - ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    - ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    - ai_governance::CC_RECORD_GOVERNED_ACTION_V0
  - wave: '3'
    step: '39'
    code: ai_governance::WF_AUTO_RECLAIM_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V0
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_LICENSE_REVOKED_V0
    - ai_governance::IN_RECLAIM_LICENSE_V0
    - ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
  - wave: '3'
    step: '40'
    code: ai_governance::WF_DENY_PROVISION_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V0
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_PROVISION_DENIED_V0
    - ai_governance::IN_DENY_PROVISION_V0
    - ai_governance::CC_APPEND_AUDIT_EVENT_V0
  - wave: '3'
    step: '41'
    code: ai_governance::WF_PROVISION_AI_LICENSING_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V0
    - ai_governance::AC_EMPLOYEE_V0
    - ai_governance::EV_LICENSE_PROVISIONED_V0
    - ai_governance::EV_PROVISION_DENIED_V0
    - ai_governance::IN_PROVISION_AI_LICENSE_V0
    - ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    - ai_governance::CC_PROVISION_LICENSE_V0
  critical_path:
  - position: '1'
    code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - position: '2'
    code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
  - position: '3'
    code: ai_governance::WF_GOVERN_AGENT_ACTION_V0
  mandate_artifact_summary:
  - action: NEW
    count: '41'
    description: 2 STRUCTURE, 1 VOCAB, 5 AC, 9 EV, 3 CT, 11 CC, 4 IN, 4 WF, 2 RB
  field_declarations:
  - code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    subdomain_field: agent_governance
  - code: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::VOCAB_AI_LICENSING_STATES_V0
    subdomain_field: ai_licensing
  - code: ai_governance::AC_AGENT_V0
    subdomain_field: agent_governance
  - code: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    subdomain_field: agent_governance
  - code: ai_governance::AC_SYSTEM_GOVERNOR_V0
    subdomain_field: agent_governance
  - code: ai_governance::AC_EMPLOYEE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::AC_SYSTEM_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    subdomain_field: agent_governance
  - code: ai_governance::EV_AGENT_ACTION_DENIED_V0
    subdomain_field: agent_governance
  - code: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_CAP_SET_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_PROVISIONED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_REVOKED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_PROVISION_DENIED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_TRAINING_COMPLETED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_USAGE_RECORDED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_RECORD_DENIED_ACTION_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_PROVISION_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    subdomain_field: agent_governance
  - code: ai_governance::IN_DENY_PROVISION_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_PROVISION_AI_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_RECLAIM_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    subdomain_field: agent_governance
  - code: ai_governance::RB_LICENSE_BINDINGS_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    subdomain_field: agent_governance
  - code: ai_governance::WF_AUTO_RECLAIM_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_DENY_PROVISION_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_PROVISION_AI_LICENSING_V0
    subdomain_field: ai_licensing
  new_capabilities:
  - code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    purpose: Evaluate whether license quota remains available under the declared cap
    inputs: assigned_count:integer, quota:integer
    outputs: quota_available:boolean, remaining:integer
  - code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    purpose: Evaluate whether required training has been completed
    inputs: training_completed:boolean
    outputs: training_eligible:boolean
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    purpose: Evaluate license inactivity against a declared threshold
    inputs: last_active_date:string, evaluation_date:string, threshold_days:integer
    outputs: is_inactive:boolean, days_inactive:integer
  new_intents:
  - code: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    purpose: Request governance mediation of agent-proposed action
    workflow: WF_GOVERN_AGENT_ACTION_V0
    inputs: tool_name:string, parameters:object, requesting_user_id:string, domain_context:string, request_id:string
  - code: ai_governance::IN_DENY_PROVISION_V0
    purpose: Handle provision denial
    workflow: WF_DENY_PROVISION_V0
    inputs: employee_id:string, reason_code:string
  - code: ai_governance::IN_PROVISION_AI_LICENSE_V0
    purpose: Request AI license provisioning
    workflow: WF_PROVISION_AI_LICENSING_V0
    inputs: employee_id:string, context:object, generated:object
  - code: ai_governance::IN_RECLAIM_LICENSE_V0
    purpose: Request license reclamation evaluation
    workflow: WF_AUTO_RECLAIM_V0
    inputs: license_id:string, threshold_days:integer, context:object
  cross_subdomain_notes: []
```

The 41 artifacts of `ai_governance`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
