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
    code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '2'
    code: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '3'
    code: ai_governance::AC_AGENT_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '4'
    code: ai_governance::AC_EMPLOYEE_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '5'
    code: ai_governance::AC_SYSTEM_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '6'
    code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '7'
    code: ai_governance::EV_AGENT_ACTION_DENIED_V1
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '8'
    code: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '9'
    code: ai_governance::EV_LICENSE_CAP_SET_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '10'
    code: ai_governance::EV_LICENSE_PROVISIONED_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '11'
    code: ai_governance::EV_LICENSE_REVOKED_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '12'
    code: ai_governance::EV_PROVISION_DENIED_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '13'
    code: ai_governance::EV_TRAINING_COMPLETED_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '14'
    code: ai_governance::EV_USAGE_RECORDED_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '15'
    code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '16'
    code: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '17'
    code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '18'
    code: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '19'
    code: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '20'
    code: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '21'
    code: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '22'
    code: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '23'
    code: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '24'
    code: ai_governance::CC_WRITE_ACTION_V0
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '25'
    code: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '26'
    code: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '27'
    code: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '28'
    code: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '29'
    code: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '30'
    code: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '31'
    code: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '32'
    code: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '33'
    code: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '34'
    code: ai_governance::CC_REQUIRE_CAP_SET_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '35'
    code: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '36'
    code: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '37'
    code: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '38'
    code: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '39'
    code: ai_governance::CC_RESOLVE_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '40'
    code: ai_governance::CC_WRITE_EMPLOYEE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '41'
    code: ai_governance::CC_WRITE_LICENSE_CAP_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '42'
    code: ai_governance::CC_WRITE_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '43'
    code: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    action: NEW
    subdomain: agent_governance
    depends_on: null
  - wave: '1'
    step: '44'
    code: ai_governance::IN_PROVISION_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '45'
    code: ai_governance::IN_RECLAIM_LICENSE_V1
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '46'
    code: ai_governance::IN_RECORD_LICENSE_USAGE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '47'
    code: ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '48'
    code: ai_governance::IN_REGISTER_EMPLOYEE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '1'
    step: '49'
    code: ai_governance::IN_SET_LICENSE_CAP_V0
    action: NEW
    subdomain: ai_licensing
    depends_on: null
  - wave: '2'
    step: '50'
    code: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
  - wave: '2'
    step: '51'
    code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    action: NEW
    subdomain: agent_governance
    depends_on:
    - ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - wave: '2'
    step: '52'
    code: ai_governance::RB_LICENSE_BINDINGS_V1
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - wave: '3'
    step: '53'
    code: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    action: NEW
    subdomain: agent_governance
    depends_on:
    - ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_AGENT_V0
    - ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    - ai_governance::EV_AGENT_ACTION_DENIED_V1
    - ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    - ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    - ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    - ai_governance::CC_RESOLVE_LICENSE_V0
    - ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    - ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    - ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    - ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    - ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    - ai_governance::CC_WRITE_ACTION_V0
    - ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - wave: '3'
    step: '54'
    code: ai_governance::WF_PROVISION_LICENSE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_EMPLOYEE_V1
    - ai_governance::EV_LICENSE_PROVISIONED_V1
    - ai_governance::EV_PROVISION_DENIED_V1
    - ai_governance::IN_PROVISION_LICENSE_V0
    - ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    - ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    - ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    - ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    - ai_governance::CC_REQUIRE_CAP_SET_V0
    - ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    - ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    - ai_governance::CC_WRITE_LICENSE_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  - wave: '3'
    step: '55'
    code: ai_governance::WF_RECLAIM_LICENSE_V1
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_LICENSE_REVOKED_V1
    - ai_governance::IN_RECLAIM_LICENSE_V1
    - ai_governance::CC_RESOLVE_LICENSE_V0
    - ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    - ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    - ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  - wave: '3'
    step: '56'
    code: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_EMPLOYEE_V1
    - ai_governance::EV_USAGE_RECORDED_V1
    - ai_governance::IN_RECORD_LICENSE_USAGE_V0
    - ai_governance::CC_RESOLVE_LICENSE_V0
    - ai_governance::CC_RECORD_LICENSE_USAGE_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  - wave: '3'
    step: '57'
    code: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_TRAINING_COMPLETED_V1
    - ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    - ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    - ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  - wave: '3'
    step: '58'
    code: ai_governance::WF_REGISTER_EMPLOYEE_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_EMPLOYEE_REGISTERED_V0
    - ai_governance::IN_REGISTER_EMPLOYEE_V0
    - ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    - ai_governance::CC_WRITE_EMPLOYEE_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  - wave: '3'
    step: '59'
    code: ai_governance::WF_SET_LICENSE_CAP_V0
    action: NEW
    subdomain: ai_licensing
    depends_on:
    - ai_governance::RB_LICENSE_BINDINGS_V1
    - ai_governance::AC_SYSTEM_V0
    - ai_governance::EV_LICENSE_CAP_SET_V1
    - ai_governance::IN_SET_LICENSE_CAP_V0
    - ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    - ai_governance::CC_WRITE_LICENSE_CAP_V0
    - ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
  critical_path:
  - position: '1'
    code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - position: '2'
    code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
  - position: '3'
    code: ai_governance::WF_GOVERN_AGENT_ACTION_V1
  mandate_artifact_summary:
  - action: NEW
    count: '59'
    description: 2 STRUCTURE, 3 AC, 9 EV, 1 CT, 28 CC, 7 IN, 7 WF, 2 RB
  field_declarations:
  - code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    subdomain_field: agent_governance
  - code: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    subdomain_field: ai_licensing
  - code: ai_governance::AC_AGENT_V0
    subdomain_field: agent_governance
  - code: ai_governance::AC_EMPLOYEE_V1
    subdomain_field: ai_licensing
  - code: ai_governance::AC_SYSTEM_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    subdomain_field: agent_governance
  - code: ai_governance::EV_AGENT_ACTION_DENIED_V1
    subdomain_field: agent_governance
  - code: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_CAP_SET_V1
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_PROVISIONED_V1
    subdomain_field: ai_licensing
  - code: ai_governance::EV_LICENSE_REVOKED_V1
    subdomain_field: ai_licensing
  - code: ai_governance::EV_PROVISION_DENIED_V1
    subdomain_field: ai_licensing
  - code: ai_governance::EV_TRAINING_COMPLETED_V1
    subdomain_field: ai_licensing
  - code: ai_governance::EV_USAGE_RECORDED_V1
    subdomain_field: ai_licensing
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_WRITE_ACTION_V0
    subdomain_field: agent_governance
  - code: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_REQUIRE_CAP_SET_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_RESOLVE_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_WRITE_EMPLOYEE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_WRITE_LICENSE_CAP_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_WRITE_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    subdomain_field: agent_governance
  - code: ai_governance::IN_PROVISION_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_RECLAIM_LICENSE_V1
    subdomain_field: ai_licensing
  - code: ai_governance::IN_RECORD_LICENSE_USAGE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_REGISTER_EMPLOYEE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::IN_SET_LICENSE_CAP_V0
    subdomain_field: ai_licensing
  - code: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    subdomain_field: ai_licensing
  - code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    subdomain_field: agent_governance
  - code: ai_governance::RB_LICENSE_BINDINGS_V1
    subdomain_field: ai_licensing
  - code: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    subdomain_field: agent_governance
  - code: ai_governance::WF_PROVISION_LICENSE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_RECLAIM_LICENSE_V1
    subdomain_field: ai_licensing
  - code: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_REGISTER_EMPLOYEE_V0
    subdomain_field: ai_licensing
  - code: ai_governance::WF_SET_LICENSE_CAP_V0
    subdomain_field: ai_licensing
  new_capabilities:
  - code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    purpose: Evaluate license inactivity against a declared threshold
    inputs: last_active_date:string, evaluation_date:string, threshold_days:integer
    outputs: is_inactive:boolean, days_inactive:integer
  new_intents:
  - code: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    purpose: A request to govern agent action
    workflow: WF_GOVERN_AGENT_ACTION_V1
    inputs: tool_name:string, parameters:object, requesting_user_id:string, domain_context:string, request_id:string
  - code: ai_governance::IN_PROVISION_LICENSE_V0
    purpose: A request to provision license
    workflow: WF_PROVISION_LICENSE_V0
    inputs: employee_id:string, tier:string
  - code: ai_governance::IN_RECLAIM_LICENSE_V1
    purpose: A request to reclaim license
    workflow: WF_RECLAIM_LICENSE_V1
    inputs: employee_id:string
  - code: ai_governance::IN_RECORD_LICENSE_USAGE_V0
    purpose: A request to record license usage
    workflow: WF_RECORD_LICENSE_USAGE_V0
    inputs: employee_id:string
  - code: ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    purpose: A request to record training completed
    workflow: WF_RECORD_TRAINING_COMPLETED_V0
    inputs: employee_id:string
  - code: ai_governance::IN_REGISTER_EMPLOYEE_V0
    purpose: A request to register employee
    workflow: WF_REGISTER_EMPLOYEE_V0
    inputs: employee_id:string
  - code: ai_governance::IN_SET_LICENSE_CAP_V0
    purpose: A request to set license cap
    workflow: WF_SET_LICENSE_CAP_V0
    inputs: cap:integer
  cross_subdomain_notes: []
```

The 59 artifacts of `ai_governance`'s design of record, scheduled in dependency order. Written by
`python -m transformation.record` from the P7 beside it. The mandate orders the build; it decides
nothing.
