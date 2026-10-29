# Design Intent — ai_governance, baseline

## Machine

```yaml
document:
  phase: p7
  domain: ai_governance
  subdomain:
  - agent_governance
  - ai_licensing
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory:
  - fqdn: ai_governance::AC_AGENT_V0
    action: EXTEND
    summary: An AI agent proposing an action on a user's behalf
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: AC_AGENT_V0
  - fqdn: ai_governance::AC_EMPLOYEE_V1
    action: EXTEND
    summary: A person the business may license for AI tools
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: AC_EMPLOYEE_V1
  - fqdn: ai_governance::AC_SYSTEM_V0
    action: EXTEND
    summary: The business's own authority, which registers, trains, sets the cap and reclaims
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: AC_SYSTEM_V0
  - fqdn: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    action: EXTEND
    summary: Refuse a request to govern agent action that lacks what it requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
  - fqdn: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    action: EXTEND
    summary: Refuse a request to provision license that lacks what it requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
  - fqdn: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    action: EXTEND
    summary: Refuse a request to set license cap that lacks what it requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
  - fqdn: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    action: EXTEND
    summary: Claim a action's action id
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_ACTION_IDENTITY_V0
  - fqdn: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    action: EXTEND
    summary: Claim a employee's employee id
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_EMPLOYEE_ID_V0
  - fqdn: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    action: EXTEND
    summary: Claim a license's license id
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_LICENSE_IDENTITY_V0
  - fqdn: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    action: EXTEND
    summary: Form a action's request identity
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_FORM_ACTION_REQUEST_IDENTITY_V0
  - fqdn: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    action: EXTEND
    summary: Move a license from active to a state the business admits
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_MOVE_LICENSE_FROM_ACTIVE_V0
  - fqdn: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    action: EXTEND
    summary: Record a moment on the agent_governance's own trail
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - fqdn: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    action: EXTEND
    summary: Record a moment on the ai_licensing's own trail
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_AI_LICENSING_MOMENT_V0
  - fqdn: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    action: EXTEND
    summary: Set what record license usage records on the license
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_LICENSE_USAGE_V0
  - fqdn: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    action: EXTEND
    summary: Set what record training completed records on the employee
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_TRAINING_COMPLETED_V0
  - fqdn: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    action: EXTEND
    summary: Release a license's identity
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RELEASE_LICENSE_IDENTITY_V0
  - fqdn: ai_governance::CC_REQUIRE_CAP_SET_V0
    action: EXTEND
    summary: Refuse to provision license before the license cap is set
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_CAP_SET_V0
  - fqdn: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    action: EXTEND
    summary: Refuse to govern agent action unless the license holds what the business requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_LICENSE_ACTIVE_V0
  - fqdn: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    action: EXTEND
    summary: Refuse to reclaim license until the condition holds
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
  - fqdn: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    action: EXTEND
    summary: Refuse to govern agent action unless parameters satisfy rules
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
  - fqdn: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    action: EXTEND
    summary: Refuse a tier the business does not admit
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_TIER_ADMITTED_V0
  - fqdn: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    action: EXTEND
    summary: Refuse to govern agent action unless tier grants tool
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_TIER_GRANTS_TOOL_V0
  - fqdn: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    action: EXTEND
    summary: Refuse a tool name the business does not admit
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_TOOL_DECLARED_V0
  - fqdn: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    action: EXTEND
    summary: Refuse to provision license unless the employee holds what the business requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_TRAINING_COMPLETED_V0
  - fqdn: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    action: EXTEND
    summary: Refuse to provision license when the licenses held reach the cap
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_UNDER_THE_CAP_V0
  - fqdn: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    action: EXTEND
    summary: Answer which employee its identity names, and refuse when none does
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
  - fqdn: ai_governance::CC_RESOLVE_LICENSE_V0
    action: EXTEND
    summary: Answer which license its identity names, and refuse when none does
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RESOLVE_LICENSE_V0
  - fqdn: ai_governance::CC_WRITE_ACTION_V0
    action: EXTEND
    summary: Write a new action in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_ACTION_V0
  - fqdn: ai_governance::CC_WRITE_EMPLOYEE_V0
    action: EXTEND
    summary: Write a new employee in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_EMPLOYEE_V0
  - fqdn: ai_governance::CC_WRITE_LICENSE_CAP_V0
    action: EXTEND
    summary: Write a new license cap in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_LICENSE_CAP_V0
  - fqdn: ai_governance::CC_WRITE_LICENSE_V0
    action: EXTEND
    summary: Write a new license in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_LICENSE_V0
  - fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    action: EXTEND
    summary: Evaluate license inactivity against a declared threshold
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CT_PURE_EVALUATE_INACTIVITY_V0
  - fqdn: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    action: EXTEND
    summary: A agent action authorized
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_AGENT_ACTION_AUTHORIZED_V1
  - fqdn: ai_governance::EV_AGENT_ACTION_DENIED_V1
    action: EXTEND
    summary: A agent action denied
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_AGENT_ACTION_DENIED_V1
  - fqdn: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    action: EXTEND
    summary: A employee registered
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_EMPLOYEE_REGISTERED_V0
  - fqdn: ai_governance::EV_LICENSE_CAP_SET_V1
    action: EXTEND
    summary: A license cap set
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_LICENSE_CAP_SET_V1
  - fqdn: ai_governance::EV_LICENSE_PROVISIONED_V1
    action: EXTEND
    summary: A license provisioned
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_LICENSE_PROVISIONED_V1
  - fqdn: ai_governance::EV_LICENSE_REVOKED_V1
    action: EXTEND
    summary: A license revoked
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_LICENSE_REVOKED_V1
  - fqdn: ai_governance::EV_PROVISION_DENIED_V1
    action: EXTEND
    summary: A provision denied
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_PROVISION_DENIED_V1
  - fqdn: ai_governance::EV_TRAINING_COMPLETED_V1
    action: EXTEND
    summary: A training completed
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_TRAINING_COMPLETED_V1
  - fqdn: ai_governance::EV_USAGE_RECORDED_V1
    action: EXTEND
    summary: A usage recorded
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_USAGE_RECORDED_V1
  - fqdn: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    action: EXTEND
    summary: A request to govern agent action
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_AGENT_ACTION_REQUESTED_V1
  - fqdn: ai_governance::IN_PROVISION_LICENSE_V0
    action: EXTEND
    summary: A request to provision license
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_PROVISION_LICENSE_V0
  - fqdn: ai_governance::IN_RECLAIM_LICENSE_V1
    action: EXTEND
    summary: A request to reclaim license
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_RECLAIM_LICENSE_V1
  - fqdn: ai_governance::IN_RECORD_LICENSE_USAGE_V0
    action: EXTEND
    summary: A request to record license usage
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_RECORD_LICENSE_USAGE_V0
  - fqdn: ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    action: EXTEND
    summary: A request to record training completed
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_RECORD_TRAINING_COMPLETED_V0
  - fqdn: ai_governance::IN_REGISTER_EMPLOYEE_V0
    action: EXTEND
    summary: A request to register employee
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_REGISTER_EMPLOYEE_V0
  - fqdn: ai_governance::IN_SET_LICENSE_CAP_V0
    action: EXTEND
    summary: A request to set license cap
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_SET_LICENSE_CAP_V0
  - fqdn: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    action: EXTEND
    summary: Binds the agent_governance's workflows to the stores and mechanisms they use
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: RB_AGENT_GOVERNANCE_BINDINGS_V1
  - fqdn: ai_governance::RB_LICENSE_BINDINGS_V1
    action: EXTEND
    summary: Binds the ai_licensing's workflows to the stores and mechanisms they use
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: RB_LICENSE_BINDINGS_V1
  - fqdn: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    action: EXTEND
    summary: Declares the stores the agent_governance owns and the paths they occupy
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - fqdn: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    action: EXTEND
    summary: Declares the stores the ai_licensing owns and the paths they occupy
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: STRUCTURE_AI_LICENSING_STORAGE_V1
  - fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    action: EXTEND
    summary: 'The governed sequence that performs: govern agent action'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_GOVERN_AGENT_ACTION_V1
  - fqdn: ai_governance::WF_PROVISION_LICENSE_V0
    action: EXTEND
    summary: 'The governed sequence that performs: provision license'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_PROVISION_LICENSE_V0
  - fqdn: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    action: EXTEND
    summary: 'The governed sequence that performs: record license usage'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_RECORD_LICENSE_USAGE_V0
  - fqdn: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    action: EXTEND
    summary: 'The governed sequence that performs: record training completed'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_RECORD_TRAINING_COMPLETED_V0
  - fqdn: ai_governance::WF_REGISTER_EMPLOYEE_V0
    action: EXTEND
    summary: 'The governed sequence that performs: register employee'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_REGISTER_EMPLOYEE_V0
  - fqdn: ai_governance::WF_SET_LICENSE_CAP_V0
    action: EXTEND
    summary: 'The governed sequence that performs: set license cap'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_SET_LICENSE_CAP_V0
  - fqdn: ai_governance::WF_RECLAIM_LICENSE_V0
    action: REPLACE
    summary: ''
    reason: The ledger derives it with a changed meaning at 1 place(s); WF_RECLAIM_LICENSE_V1 succeeds
      it.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_RECLAIM_LICENSE_V0
  new_artifacts:
  - family: WF
    code: ai_governance::WF_RECLAIM_LICENSE_V1
    summary: 'The governed sequence that performs: reclaim license'
    owner_subdomain: ai_licensing
    status: NEW
  rb_declarations:
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_REGISTER_EMPLOYEE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_SET_LICENSE_CAP_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_PROVISION_LICENSE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    binds_wf: ai_governance::WF_RECLAIM_LICENSE_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    binds_wf: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  execution_topology:
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: IN_REGISTER_EMPLOYEE_V0
    node_type: IN
    routing:
      ACK: CC_CLAIM_EMPLOYEE_ID_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: CC_CLAIM_EMPLOYEE_ID_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_EMPLOYEE_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: CC_WRITE_EMPLOYEE_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_REGISTER_EMPLOYEE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: IN_RECORD_TRAINING_COMPLETED_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_TRAINING_COMPLETED_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: CC_RECORD_TRAINING_COMPLETED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: IN_SET_LICENSE_CAP_V0
    node_type: IN
    routing:
      ACK: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_LICENSE_CAP_V0
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: CC_WRITE_LICENSE_CAP_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_SET_LICENSE_CAP_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: IN_PROVISION_LICENSE_V0
    node_type: IN
    routing:
      ACK: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_TRAINING_COMPLETED_V0
      NOT_FOUND: CC_DENY_TRAINING_COMPLETED
      VIOLATION: CC_DENY_TRAINING_COMPLETED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_REQUIRE_TRAINING_COMPLETED_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_TIER_ADMITTED_V0
      VIOLATION: CC_DENY_TRAINING_COMPLETED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_REQUIRE_TIER_ADMITTED_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_CAP_SET_V0
      VIOLATION: CC_DENY_TIER_ADMITTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_REQUIRE_CAP_SET_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_UNDER_THE_CAP_V0
      NOT_FOUND: CC_DENY_CAP_SET
      VIOLATION: CC_DENY_CAP_SET
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_REQUIRE_UNDER_THE_CAP_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_LICENSE_IDENTITY_V0
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: CC_DENY_UNDER_THE_CAP
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_CLAIM_LICENSE_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_LICENSE_V0
      VIOLATION: EXIT_REJECTED
      ALREADY_EXISTS: CC_DENY_LICENSE_ALREADY_HELD
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_WRITE_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_DENY_TRAINING_COMPLETED
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AI_LICENSING_MOMENT_V0
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_DENY_TIER_ADMITTED
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AI_LICENSING_MOMENT_V0
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_DENY_CAP_SET
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AI_LICENSING_MOMENT_V0
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_DENY_UNDER_THE_CAP
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AI_LICENSING_MOMENT_V0
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: CC_DENY_LICENSE_ALREADY_HELD
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AI_LICENSING_MOMENT_V0
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_LICENSE_V0
    node: EXIT_DENIED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: IN_RECORD_LICENSE_USAGE_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_LICENSE_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: CC_RESOLVE_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_LICENSE_USAGE_V0
      VIOLATION: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: CC_RECORD_LICENSE_USAGE_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: IN_RECLAIM_LICENSE_V1
    node_type: IN
    routing:
      ACK: CC_RESOLVE_LICENSE_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: CC_RESOLVE_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
      VIOLATION: EXIT_REJECTED
      NOT_FOUND: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    node_type: CC
    routing:
      SUCCESS: CC_RELEASE_LICENSE_IDENTITY_V0
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_STILL_ACTIVE
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: CC_RELEASE_LICENSE_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_MOVE_LICENSE_FROM_ACTIVE_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_STILL_ACTIVE
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: CC_MOVE_LICENSE_FROM_ACTIVE_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AI_LICENSING_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: CC_RECORD_AI_LICENSING_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_RECLAIM_LICENSE_V1
    node: EXIT_STILL_ACTIVE
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: IN_AGENT_ACTION_REQUESTED_V1
    node_type: IN
    routing:
      ACK: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_TOOL_DECLARED_V0
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_REQUIRE_TOOL_DECLARED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_LICENSE_V0
      VIOLATION: CC_DENY_UNDECLARED_TOOL
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_RESOLVE_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_LICENSE_ACTIVE_V0
      VIOLATION: CC_DENY_UNAUTHORIZED_ACTOR
      NOT_FOUND: CC_DENY_UNAUTHORIZED_ACTOR
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_REQUIRE_LICENSE_ACTIVE_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_TIER_GRANTS_TOOL_V0
      VIOLATION: CC_DENY_UNAUTHORIZED_ACTOR
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_REQUIRE_TIER_GRANTS_TOOL_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
      VIOLATION: CC_DENY_UNAUTHORIZED_TOOL
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    node_type: CC
    routing:
      SUCCESS: CC_FORM_ACTION_REQUEST_IDENTITY_V0
      VIOLATION: CC_DENY_PARAMETER_VIOLATION
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_FORM_ACTION_REQUEST_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_ACTION_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_CLAIM_ACTION_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_ACTION_V0
      VIOLATION: EXIT_REJECTED
      ALREADY_EXISTS: CC_WRITE_ACTION_V0
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_WRITE_ACTION_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_DENY_UNDECLARED_TOOL
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_DENY_UNAUTHORIZED_ACTOR
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_DENY_UNAUTHORIZED_TOOL
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: CC_DENY_PARAMETER_VIOLATION
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    runs: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    node: EXIT_DENIED
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: '1'
    step_name: claim_id
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: EMPLOYEE_EMPLOYEE_ID_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: '1'
    step_name: assemble_employee_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - employee_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        employee_record: employee_record
  - cc_code: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: '2'
    step_name: write_employee_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: EMPLOYEES
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: '1'
    step_name: assemble_occurrence
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: '2'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: LICENSE_AUDIT
    consumes:
    - record
    - stream_id
    produces:
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
      out:
        sequence_number: sequence_number
  - cc_code: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: '1'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: EMPLOYEE_EMPLOYEE_ID_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        target_ref: target_ref
        result_status: result_status
  - cc_code: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: '2'
    step_name: read_employee_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: EMPLOYEES
    consumes:
    - key
    produces:
    - employee_record
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        employee_record: employee_record
        result_status: result_status
  - cc_code: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: '1'
    step_name: set_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: EMPLOYEES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: '1'
    step_name: check_cap_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: '2'
    step_name: refuse_incomplete_submission
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: '1'
    step_name: assemble_cap_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - cap_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        cap_record: cap_record
  - cc_code: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: '2'
    step_name: write_cap_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: LICENSE_CAPS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: '1'
    step_name: check_license_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: '2'
    step_name: refuse_incomplete_submission
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    step: '1'
    step_name: require_training_completed
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    step: '1'
    step_name: require_tier_admitted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: ai_governance::CC_REQUIRE_CAP_SET_V0
    step: '1'
    step_name: read_cap_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: LICENSE_CAPS
    consumes:
    - key
    produces:
    - cap_record
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        cap_record: cap_record
        result_status: result_status
  - cc_code: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: '1'
    step_name: count_licenses
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: COUNT
    store: LICENSE_IDENTITY_REGISTRY
    consumes: null
    produces:
    - count
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        count: count
        result_status: result_status
  - cc_code: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: '2'
    step_name: require_below_cap
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: '1'
    step_name: form_license_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - license_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        data: data
        prefix: prefix
      out:
        license_id: license_id
  - cc_code: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: '2'
    step_name: claim_id
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: LICENSE_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: exit
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: ai_governance::CC_WRITE_LICENSE_V0
    step: '1'
    step_name: read_now
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: null
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        timestamp: timestamp
  - cc_code: ai_governance::CC_WRITE_LICENSE_V0
    step: '2'
    step_name: assemble_license_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - license_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        license_record: license_record
  - cc_code: ai_governance::CC_WRITE_LICENSE_V0
    step: '3'
    step_name: write_license_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: LICENSES
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_RESOLVE_LICENSE_V0
    step: '1'
    step_name: form_license_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - license_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        data: data
        prefix: prefix
      out:
        license_id: license_id
  - cc_code: ai_governance::CC_RESOLVE_LICENSE_V0
    step: '2'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: LICENSE_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        target_ref: target_ref
        result_status: result_status
  - cc_code: ai_governance::CC_RESOLVE_LICENSE_V0
    step: '3'
    step_name: read_license_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: LICENSES
    consumes:
    - key
    produces:
    - license_record
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        license_record: license_record
        result_status: result_status
  - cc_code: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: '1'
    step_name: read_now
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: null
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        timestamp: timestamp
  - cc_code: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: '2'
    step_name: set_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: LICENSES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: '1'
    step_name: read_now
    capability: capability_side_effects::CS_CLOCK_V0
    kind: CS
    operation: NOW
    store: null
    consumes: null
    produces:
    - timestamp
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        timestamp: timestamp
  - cc_code: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: '2'
    step_name: evaluate_unused_for_days
    capability: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - last_active_date
    - evaluation_date
    - threshold_days
    produces:
    - is_inactive
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        last_active_date: last_active_date
        evaluation_date: evaluation_date
        threshold_days: threshold_days
      out:
        is_inactive: is_inactive
  - cc_code: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    step: '1'
    step_name: release_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: DEREGISTER
    store: LICENSE_IDENTITY_REGISTRY
    consumes:
    - key_or_address
    produces:
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: '1'
    step_name: read_outcome_admitted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: '2'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: LICENSES
    consumes:
    - filter
    - updates
    produces:
    - matched_keys
    - updated_count
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        filter: filter
        updates: updates
      out:
        matched_keys: matched_keys
        updated_count: updated_count
        result_status: result_status
  - cc_code: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: '1'
    step_name: check_action_fields
    capability: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - record
    - schema
    produces:
    - violations
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        schema: schema
      out:
        violations: violations
  - cc_code: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: '2'
    step_name: refuse_incomplete_submission
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    step: '1'
    step_name: require_tool_name_admitted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    step: '1'
    step_name: require_license_active
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: '1'
    step_name: look_up_tier_tools
    capability: capability_transforms::CT_PURE_LOOKUP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - map
    - key
    produces:
    - tier_tools
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        map: map
        key: key
      out:
        tier_tools: tier_tools
  - cc_code: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: '2'
    step_name: require_tool_name_in_tier_tools
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_member
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        value: value
        allowed_set: allowed_set
      out:
        is_member: is_member
  - cc_code: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: '1'
    step_name: look_up_tool_rules
    capability: capability_transforms::CT_PURE_LOOKUP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - map
    - key
    produces:
    - tool_rules
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        map: map
        key: key
      out:
        tool_rules: tool_rules
  - cc_code: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: '2'
    step_name: require_parameters_hold
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - valid
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    step: '1'
    step_name: form_request_identity
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - request_identity
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        data: data
        prefix: prefix
      out:
        request_identity: request_identity
  - cc_code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: '1'
    step_name: form_action_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - action_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        data: data
        prefix: prefix
      out:
        action_id: action_id
  - cc_code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: '2'
    step_name: claim_id
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: ACTION_IDENTITY_REGISTRY
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
    - address
    - result_status
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_cs: target_cs
        target_ref: target_ref
      out:
        address: address
        result_status: result_status
  - cc_code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: '3'
    step_name: assemble_action_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - action_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        action_record: action_record
  - cc_code: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: '4'
    step_name: write_action_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: ACTIONS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_WRITE_ACTION_V0
    step: '1'
    step_name: assemble_action_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - action_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        action_record: action_record
  - cc_code: ai_governance::CC_WRITE_ACTION_V0
    step: '2'
    step_name: write_action_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: ACTIONS
    consumes:
    - key
    - value
    produces:
    - result_status
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        value: value
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: '1'
    step_name: assemble_occurrence
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        record: record
  - cc_code: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: '2'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: GOVERNANCE_AUDIT
    consumes:
    - record
    - stream_id
    produces:
    - sequence_number
    routing:
      SUCCESS: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
      out:
        sequence_number: sequence_number
  step_bindings:
  - owner: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: claim_id
    direction: INPUT
    field: key
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: claim_id
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: claim_id
    direction: INPUT
    field: target_ref
    bound_to:
      literal: EMPLOYEES
  - owner: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: claim_id
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    step: claim_id
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: assemble_employee_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        employee_id: $.inputs.employee_id
        training_completed: false
  - owner: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: assemble_employee_record
    direction: OUTPUT
    field: employee_record
    bound_to: capability_result.record
  - owner: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: write_employee_record
    direction: INPUT
    field: key
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: write_employee_record
    direction: INPUT
    field: value
    bound_to: results.assemble_employee_record.employee_record
  - owner: ai_governance::CC_WRITE_EMPLOYEE_V0
    step: write_employee_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence
        employee_id: $.inputs.employee_id
        license_id: $.inputs.license_id
        tier: $.inputs.tier
        reason: $.inputs.reason
  - owner: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to:
      literal: LICENSE_AUDIT
  - owner: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: read_employee_record
    direction: INPUT
    field: key
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: read_employee_record
    direction: OUTPUT
    field: employee_record
    bound_to: capability_result.value
  - owner: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    step: read_employee_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: set_record
    direction: INPUT
    field: filter
    bound_to:
      literal:
        employee_id: $.inputs.employee_id
  - owner: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: set_record
    direction: INPUT
    field: updates
    bound_to:
      literal:
        training_completed: true
  - owner: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: set_record
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: set_record
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    step: set_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: check_cap_fields
    direction: INPUT
    field: record
    bound_to: inputs.submission
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: check_cap_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        cap:
          type: integer
          required: true
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: check_cap_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        cap_violations: $.results.check_cap_fields.violations
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: cap_violations
        op: eq
        value: []
  - owner: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: assemble_cap_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        cap: $.inputs.submission.cap
  - owner: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: assemble_cap_record
    direction: OUTPUT
    field: cap_record
    bound_to: capability_result.record
  - owner: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: write_cap_record
    direction: INPUT
    field: key
    bound_to:
      literal: current
  - owner: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: write_cap_record
    direction: INPUT
    field: value
    bound_to: results.assemble_cap_record.cap_record
  - owner: ai_governance::CC_WRITE_LICENSE_CAP_V0
    step: write_cap_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: check_license_fields
    direction: INPUT
    field: record
    bound_to: inputs.submission
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: check_license_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        employee_id:
          type: string
          required: true
        tier:
          type: string
          required: true
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: check_license_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        license_violations: $.results.check_license_fields.violations
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: license_violations
        op: eq
        value: []
  - owner: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    step: require_training_completed
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        training_completed: $.inputs.training_completed
  - owner: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    step: require_training_completed
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: training_completed
        op: eq
        value: true
  - owner: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    step: require_training_completed
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    step: require_tier_admitted
    direction: INPUT
    field: value
    bound_to: inputs.tier
  - owner: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    step: require_tier_admitted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - standard
      - enterprise
  - owner: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    step: require_tier_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_REQUIRE_CAP_SET_V0
    step: read_cap_record
    direction: INPUT
    field: key
    bound_to: inputs.cap_key
  - owner: ai_governance::CC_REQUIRE_CAP_SET_V0
    step: read_cap_record
    direction: OUTPUT
    field: cap_record
    bound_to: capability_result.value
  - owner: ai_governance::CC_REQUIRE_CAP_SET_V0
    step: read_cap_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: count_licenses
    direction: OUTPUT
    field: count
    bound_to: capability_result.count
  - owner: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: count_licenses
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: require_below_cap
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        count: $.results.count_licenses.count
  - owner: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: require_below_cap
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: count
        op: lt
        value: $.inputs.cap
  - owner: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    step: require_below_cap
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: form_license_id
    direction: INPUT
    field: data
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: form_license_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: lic
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: form_license_id
    direction: OUTPUT
    field: license_id
    bound_to: capability_result.id
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: key
    bound_to: results.form_license_id.license_id
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: target_ref
    bound_to:
      literal: LICENSES
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: claim_id
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    step: claim_id
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: assemble_license_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        license_id: $.inputs.license_id
        last_used_at: $.results.read_now.timestamp
        employee_id: $.inputs.submission.employee_id
        tier: $.inputs.submission.tier
        state: ACTIVE
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: assemble_license_record
    direction: OUTPUT
    field: license_record
    bound_to: capability_result.record
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: write_license_record
    direction: INPUT
    field: key
    bound_to: inputs.license_id
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: write_license_record
    direction: INPUT
    field: value
    bound_to: results.assemble_license_record.license_record
  - owner: ai_governance::CC_WRITE_LICENSE_V0
    step: write_license_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: form_license_id
    direction: INPUT
    field: data
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: form_license_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: lic
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: form_license_id
    direction: OUTPUT
    field: license_id
    bound_to: capability_result.id
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: results.form_license_id.license_id
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: read_license_record
    direction: INPUT
    field: key
    bound_to: results.form_license_id.license_id
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: read_license_record
    direction: OUTPUT
    field: license_record
    bound_to: capability_result.value
  - owner: ai_governance::CC_RESOLVE_LICENSE_V0
    step: read_license_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: set_record
    direction: INPUT
    field: filter
    bound_to:
      literal:
        license_id: $.inputs.license_id
        state: ACTIVE
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: set_record
    direction: INPUT
    field: updates
    bound_to:
      literal:
        last_used_at: $.results.read_now.timestamp
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: set_record
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: set_record
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    step: set_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: evaluate_unused_for_days
    direction: INPUT
    field: last_active_date
    bound_to: inputs.last_used_at
  - owner: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: evaluate_unused_for_days
    direction: INPUT
    field: evaluation_date
    bound_to: results.read_now.timestamp
  - owner: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: evaluate_unused_for_days
    direction: INPUT
    field: threshold_days
    bound_to:
      literal: 30
  - owner: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    step: evaluate_unused_for_days
    direction: OUTPUT
    field: is_inactive
    bound_to: capability_result.is_inactive
  - owner: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    step: release_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.license_id
  - owner: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    step: release_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: read_outcome_admitted
    direction: INPUT
    field: value
    bound_to: inputs.to_state
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: read_outcome_admitted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - RECLAIMED
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        license_id: $.inputs.license_id
        state: ACTIVE
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: $.inputs.to_state
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: check_action_fields
    direction: INPUT
    field: record
    bound_to: inputs.submission
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: check_action_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        tool_name:
          type: string
          required: true
        requesting_user_id:
          type: string
          required: true
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: check_action_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        action_violations: $.results.check_action_fields.violations
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: action_violations
        op: eq
        value: []
  - owner: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    step: require_tool_name_admitted
    direction: INPUT
    field: value
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    step: require_tool_name_admitted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - READ_RECORD
      - PROVISION_STANDARD_LICENSE
      - PROVISION_PREMIUM_LICENSE
  - owner: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    step: require_tool_name_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    step: require_license_active
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        state: $.inputs.state
  - owner: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    step: require_license_active
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: state
        op: eq
        value: ACTIVE
  - owner: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    step: require_license_active
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: look_up_tier_tools
    direction: INPUT
    field: map
    bound_to:
      literal:
        standard:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        enterprise:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        - PROVISION_PREMIUM_LICENSE
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: look_up_tier_tools
    direction: INPUT
    field: key
    bound_to: inputs.key
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: look_up_tier_tools
    direction: OUTPUT
    field: tier_tools
    bound_to: capability_result.result
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: require_tool_name_in_tier_tools
    direction: INPUT
    field: value
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: require_tool_name_in_tier_tools
    direction: INPUT
    field: allowed_set
    bound_to: results.look_up_tier_tools.tier_tools
  - owner: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    step: require_tool_name_in_tier_tools
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: look_up_tool_rules
    direction: INPUT
    field: map
    bound_to:
      literal:
        READ_RECORD:
        - field: record_type
          op: in
          allowed:
          - license_pool
          - user_profile
        - field: id
          op: not_null
        PROVISION_STANDARD_LICENSE:
        - field: tier
          op: eq
          value: standard
        - field: quantity
          op: lte
          value: 100
        PROVISION_PREMIUM_LICENSE:
        - field: tier
          op: eq
          value: premium
        - field: quantity
          op: lte
          value: 50
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: look_up_tool_rules
    direction: INPUT
    field: key
    bound_to: inputs.key
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: look_up_tool_rules
    direction: OUTPUT
    field: tool_rules
    bound_to: capability_result.result
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: require_parameters_hold
    direction: INPUT
    field: parameters
    bound_to: inputs.parameters
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: require_parameters_hold
    direction: INPUT
    field: rules
    bound_to: results.look_up_tool_rules.tool_rules
  - owner: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    step: require_parameters_hold
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    step: form_request_identity
    direction: INPUT
    field: data
    bound_to:
      literal:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
  - owner: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    step: form_request_identity
    direction: INPUT
    field: prefix
    bound_to:
      literal: AREQ
  - owner: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    step: form_request_identity
    direction: OUTPUT
    field: request_identity
    bound_to: capability_result.id
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: form_action_id
    direction: INPUT
    field: data
    bound_to:
      literal:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: form_action_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: AGOV
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: form_action_id
    direction: OUTPUT
    field: action_id
    bound_to: capability_result.id
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: key
    bound_to: results.form_action_id.action_id
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: claim_id
    direction: INPUT
    field: target_ref
    bound_to:
      literal: ACTIONS
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: claim_id
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: claim_id
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: assemble_action_record
    direction: INPUT
    field: fields
    bound_to: inputs.action_fields
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: assemble_action_record
    direction: OUTPUT
    field: action_record
    bound_to: capability_result.record
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: write_action_record
    direction: INPUT
    field: key
    bound_to: results.form_action_id.action_id
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: write_action_record
    direction: INPUT
    field: value
    bound_to: results.assemble_action_record.action_record
  - owner: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    step: write_action_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_WRITE_ACTION_V0
    step: assemble_action_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        action_id: $.inputs.action_id
        tool_name: $.inputs.submission.tool_name
        requesting_user_id: $.inputs.submission.requesting_user_id
        request_identity: $.inputs.request_identity
  - owner: ai_governance::CC_WRITE_ACTION_V0
    step: assemble_action_record
    direction: OUTPUT
    field: action_record
    bound_to: capability_result.record
  - owner: ai_governance::CC_WRITE_ACTION_V0
    step: write_action_record
    direction: INPUT
    field: key
    bound_to: inputs.action_id
  - owner: ai_governance::CC_WRITE_ACTION_V0
    step: write_action_record
    direction: INPUT
    field: value
    bound_to: results.assemble_action_record.action_record
  - owner: ai_governance::CC_WRITE_ACTION_V0
    step: write_action_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        decision: $.inputs.occurrence
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        reason: $.inputs.reason
  - owner: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to:
      literal: GOVERNANCE_AUDIT
  - owner: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: ai_governance::WF_REGISTER_EMPLOYEE_V0
    step: CC_CLAIM_EMPLOYEE_ID_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_REGISTER_EMPLOYEE_V0
    step: CC_WRITE_EMPLOYEE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_REGISTER_EMPLOYEE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: EMPLOYEE_REGISTERED
  - owner: ai_governance::WF_REGISTER_EMPLOYEE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    step: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    step: CC_RECORD_TRAINING_COMPLETED_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: TRAINING_COMPLETED
  - owner: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_SET_LICENSE_CAP_V0
    step: CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        cap: $.payload.cap
  - owner: ai_governance::WF_SET_LICENSE_CAP_V0
    step: CC_WRITE_LICENSE_CAP_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        cap: $.payload.cap
  - owner: ai_governance::WF_SET_LICENSE_CAP_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: LICENSE_CAP_SET
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        employee_id: $.payload.employee_id
        tier: $.payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_REQUIRE_TRAINING_COMPLETED_V0
    direction: INPUT
    field: training_completed
    bound_to: results.CC_RESOLVE_EMPLOYEE_IDENTITY_V0.employee_record.training_completed
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_REQUIRE_TIER_ADMITTED_V0
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_REQUIRE_CAP_SET_V0
    direction: INPUT
    field: cap_key
    bound_to:
      literal: current
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_REQUIRE_UNDER_THE_CAP_V0
    direction: INPUT
    field: cap
    bound_to: results.CC_REQUIRE_CAP_SET_V0.cap_record.cap
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_CLAIM_LICENSE_IDENTITY_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_WRITE_LICENSE_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_WRITE_LICENSE_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        employee_id: $.payload.employee_id
        tier: $.payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: LICENSE_PROVISIONED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TRAINING_COMPLETED
    direction: INPUT
    field: occurrence
    bound_to:
      literal: PROVISION_DENIED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TRAINING_COMPLETED
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TRAINING_COMPLETED
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TRAINING_COMPLETED
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TRAINING_COMPLETED
    direction: INPUT
    field: reason
    bound_to:
      literal: TRAINING_COMPLETED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TIER_ADMITTED
    direction: INPUT
    field: occurrence
    bound_to:
      literal: PROVISION_DENIED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TIER_ADMITTED
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TIER_ADMITTED
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TIER_ADMITTED
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_TIER_ADMITTED
    direction: INPUT
    field: reason
    bound_to:
      literal: TIER_ADMITTED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_CAP_SET
    direction: INPUT
    field: occurrence
    bound_to:
      literal: PROVISION_DENIED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_CAP_SET
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_CAP_SET
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_CAP_SET
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_CAP_SET
    direction: INPUT
    field: reason
    bound_to:
      literal: CAP_SET
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_UNDER_THE_CAP
    direction: INPUT
    field: occurrence
    bound_to:
      literal: PROVISION_DENIED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_UNDER_THE_CAP
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_UNDER_THE_CAP
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_UNDER_THE_CAP
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_UNDER_THE_CAP
    direction: INPUT
    field: reason
    bound_to:
      literal: UNDER_THE_CAP
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_LICENSE_ALREADY_HELD
    direction: INPUT
    field: occurrence
    bound_to:
      literal: PROVISION_DENIED
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_LICENSE_ALREADY_HELD
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_LICENSE_ALREADY_HELD
    direction: INPUT
    field: license_id
    bound_to: results.CC_CLAIM_LICENSE_IDENTITY_V0.license_id
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_LICENSE_ALREADY_HELD
    direction: INPUT
    field: tier
    bound_to: payload.tier
  - owner: ai_governance::WF_PROVISION_LICENSE_V0
    step: CC_DENY_LICENSE_ALREADY_HELD
    direction: INPUT
    field: reason
    bound_to:
      literal: LICENSE_ALREADY_HELD
  - owner: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    step: CC_RESOLVE_LICENSE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    step: CC_RECORD_LICENSE_USAGE_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.license_id
  - owner: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: USAGE_RECORDED
  - owner: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.license_id
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_RESOLVE_LICENSE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    direction: INPUT
    field: last_used_at
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.last_used_at
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_RELEASE_LICENSE_IDENTITY_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.license_id
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_MOVE_LICENSE_FROM_ACTIVE_V0
    direction: INPUT
    field: to_state
    bound_to:
      literal: RECLAIMED
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_MOVE_LICENSE_FROM_ACTIVE_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.license_id
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: LICENSE_REVOKED
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_RECLAIM_LICENSE_V1
    step: CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: license_id
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.license_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_TOOL_DECLARED_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_RESOLVE_LICENSE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_LICENSE_ACTIVE_V0
    direction: INPUT
    field: state
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.state
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_TIER_GRANTS_TOOL_V0
    direction: INPUT
    field: key
    bound_to: results.CC_RESOLVE_LICENSE_V0.license_record.tier
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_TIER_GRANTS_TOOL_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    direction: INPUT
    field: key
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    direction: INPUT
    field: parameters
    bound_to: payload.parameters
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: action_fields
    bound_to:
      literal:
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_WRITE_ACTION_V0
    direction: INPUT
    field: action_id
    bound_to: results.CC_CLAIM_ACTION_IDENTITY_V0.action_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_WRITE_ACTION_V0
    direction: INPUT
    field: submission
    bound_to:
      literal:
        tool_name: $.payload.tool_name
        requesting_user_id: $.payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_WRITE_ACTION_V0
    direction: INPUT
    field: request_identity
    bound_to: results.CC_FORM_ACTION_REQUEST_IDENTITY_V0.request_identity
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: AGENT_ACTION_AUTHORIZED
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: reason
    bound_to: payload.parameters.reason
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNDECLARED_TOOL
    direction: INPUT
    field: occurrence
    bound_to:
      literal: AGENT_ACTION_DENIED
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNDECLARED_TOOL
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNDECLARED_TOOL
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNDECLARED_TOOL
    direction: INPUT
    field: reason
    bound_to:
      literal: UNDECLARED_TOOL
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: occurrence
    bound_to:
      literal: AGENT_ACTION_DENIED
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: reason
    bound_to:
      literal: UNAUTHORIZED_ACTOR
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_TOOL
    direction: INPUT
    field: occurrence
    bound_to:
      literal: AGENT_ACTION_DENIED
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_TOOL
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_TOOL
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_UNAUTHORIZED_TOOL
    direction: INPUT
    field: reason
    bound_to:
      literal: UNAUTHORIZED_TOOL
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_PARAMETER_VIOLATION
    direction: INPUT
    field: occurrence
    bound_to:
      literal: AGENT_ACTION_DENIED
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_PARAMETER_VIOLATION
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_PARAMETER_VIOLATION
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    step: CC_DENY_PARAMETER_VIOLATION
    direction: INPUT
    field: reason
    bound_to:
      literal: PARAMETER_VIOLATION
  interface_fields:
  - artifact: ai_governance::AC_EMPLOYEE_V1
    direction: ATTRIBUTE
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::AC_SYSTEM_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: null
    meaning: role
  - artifact: ai_governance::AC_AGENT_V0
    direction: ATTRIBUTE
    field: agent_id
    type: string
    required: 'YES'
    default: null
    meaning: agent id
  - artifact: ai_governance::AC_AGENT_V0
    direction: ATTRIBUTE
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: ai_governance::CC_WRITE_EMPLOYEE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_WRITE_EMPLOYEE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: occurrence
    type: string
    required: 'YES'
    default: null
    meaning: occurrence
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'NO'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'NO'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: tier
    type: string
    required: 'NO'
    default: null
    meaning: tier
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: INPUT
    field: reason
    type: string
    required: 'NO'
    default: null
    meaning: reason
  - artifact: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    direction: OUTPUT
    field: employee_record
    type: object
    required: 'YES'
    default: null
    meaning: employee record
  - artifact: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_CHECK_SET_LICENSE_CAP_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_WRITE_LICENSE_CAP_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_WRITE_LICENSE_CAP_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_CHECK_PROVISION_LICENSE_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    direction: INPUT
    field: training_completed
    type: string
    required: 'YES'
    default: null
    meaning: training completed
  - artifact: ai_governance::CC_REQUIRE_TRAINING_COMPLETED_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    direction: INPUT
    field: tier
    type: string
    required: 'YES'
    default: null
    meaning: tier
  - artifact: ai_governance::CC_REQUIRE_TIER_ADMITTED_V0
    direction: OUTPUT
    field: is_member
    type: boolean
    required: 'YES'
    default: null
    meaning: is member
  - artifact: ai_governance::CC_REQUIRE_CAP_SET_V0
    direction: INPUT
    field: cap_key
    type: string
    required: 'YES'
    default: null
    meaning: cap key
  - artifact: ai_governance::CC_REQUIRE_CAP_SET_V0
    direction: OUTPUT
    field: cap_record
    type: object
    required: 'YES'
    default: null
    meaning: cap record
  - artifact: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    direction: INPUT
    field: cap
    type: integer
    required: 'YES'
    default: null
    meaning: cap
  - artifact: ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_WRITE_LICENSE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_WRITE_LICENSE_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_WRITE_LICENSE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RESOLVE_LICENSE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_RESOLVE_LICENSE_V0
    direction: OUTPUT
    field: license_record
    type: object
    required: 'YES'
    default: null
    meaning: license record
  - artifact: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_RECORD_LICENSE_USAGE_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    direction: INPUT
    field: last_used_at
    type: string
    required: 'YES'
    default: null
    meaning: last used at
  - artifact: ai_governance::CC_REQUIRE_LICENSE_UNUSED_FOR_DAYS_V0
    direction: OUTPUT
    field: is_inactive
    type: boolean
    required: 'YES'
    default: null
    meaning: is inactive
  - artifact: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    direction: INPUT
    field: to_state
    type: string
    required: 'YES'
    default: null
    meaning: to state
  - artifact: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_CHECK_GOVERN_AGENT_ACTION_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_REQUIRE_TOOL_DECLARED_V0
    direction: OUTPUT
    field: is_member
    type: boolean
    required: 'YES'
    default: null
    meaning: is member
  - artifact: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    direction: INPUT
    field: state
    type: string
    required: 'YES'
    default: null
    meaning: state
  - artifact: ai_governance::CC_REQUIRE_LICENSE_ACTIVE_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    direction: INPUT
    field: key
    type: string
    required: 'YES'
    default: null
    meaning: key
  - artifact: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_REQUIRE_TIER_GRANTS_TOOL_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    direction: INPUT
    field: key
    type: string
    required: 'YES'
    default: null
    meaning: key
  - artifact: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: null
    meaning: parameters
  - artifact: ai_governance::CC_REQUIRE_PARAMETERS_SATISFY_RULES_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::CC_FORM_ACTION_REQUEST_IDENTITY_V0
    direction: OUTPUT
    field: request_identity
    type: string
    required: 'YES'
    default: null
    meaning: request identity
  - artifact: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    direction: INPUT
    field: action_fields
    type: object
    required: 'YES'
    default: null
    meaning: action fields
  - artifact: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    direction: OUTPUT
    field: action_id
    type: string
    required: 'YES'
    default: null
    meaning: action id
  - artifact: ai_governance::CC_WRITE_ACTION_V0
    direction: INPUT
    field: action_id
    type: string
    required: 'YES'
    default: null
    meaning: action id
  - artifact: ai_governance::CC_WRITE_ACTION_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: ai_governance::CC_WRITE_ACTION_V0
    direction: INPUT
    field: request_identity
    type: string
    required: 'YES'
    default: null
    meaning: request identity
  - artifact: ai_governance::CC_WRITE_ACTION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: occurrence
    type: string
    required: 'YES'
    default: null
    meaning: occurrence
  - artifact: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'NO'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'NO'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: INPUT
    field: reason
    type: string
    required: 'NO'
    default: null
    meaning: reason
  - artifact: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: ai_governance::IN_REGISTER_EMPLOYEE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::IN_RECORD_TRAINING_COMPLETED_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::IN_SET_LICENSE_CAP_V0
    direction: INPUT
    field: cap
    type: integer
    required: 'YES'
    default: null
    meaning: cap
  - artifact: ai_governance::IN_PROVISION_LICENSE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::IN_PROVISION_LICENSE_V0
    direction: INPUT
    field: tier
    type: string
    required: 'YES'
    default: null
    meaning: tier
  - artifact: ai_governance::IN_RECORD_LICENSE_USAGE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::IN_RECLAIM_LICENSE_V1
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: null
    meaning: parameters
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    direction: INPUT
    field: request_id
    type: string
    required: 'NO'
    default: null
    meaning: request id
  - artifact: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V1
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V1
    direction: OUTPUT
    field: cap
    type: integer
    required: 'YES'
    default: null
    meaning: cap
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_PROVISION_DENIED_V1
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_PROVISION_DENIED_V1
    direction: OUTPUT
    field: reason
    type: string
    required: 'YES'
    default: null
    meaning: reason
  - artifact: ai_governance::EV_PROVISION_DENIED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V1
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V1
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V1
    direction: OUTPUT
    field: tier
    type: string
    required: 'YES'
    default: null
    meaning: tier
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_USAGE_RECORDED_V1
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_USAGE_RECORDED_V1
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_USAGE_RECORDED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_LICENSE_REVOKED_V1
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_LICENSE_REVOKED_V1
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_LICENSE_REVOKED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V1
    direction: OUTPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V1
    direction: OUTPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V1
    direction: OUTPUT
    field: reason
    type: string
    required: 'YES'
    default: null
    meaning: reason
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    direction: OUTPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    direction: OUTPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: last_active_date
    type: string
    required: 'YES'
    default: null
    meaning: ISO-8601 date or date-time of last recorded license activity
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: evaluation_date
    type: string
    required: 'YES'
    default: null
    meaning: ISO-8601 date or date-time the evaluation is made as of — declared, never a clock read
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: INPUT
    field: threshold_days
    type: integer
    required: 'YES'
    default: null
    meaning: Inactivity threshold in days
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: OUTPUT
    field: is_inactive
    type: boolean
    required: 'YES'
    default: null
    meaning: True when days_inactive meets or exceeds threshold_days
  - artifact: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    direction: OUTPUT
    field: days_inactive
    type: integer
    required: 'YES'
    default: null
    meaning: Whole days elapsed between last_active_date and evaluation_date
  implementation_bindings:
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    callable: execute
    operation: PURE_EVALUATE_INACTIVITY
    kind: atom
    purity: ct_pure
    refusal: raises
  vocabulary_extensions: []
  runtime_policies:
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V1
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  artifact_properties:
  - artifact: ai_governance::AC_EMPLOYEE_V1
    property: type
    value: human
  - artifact: ai_governance::AC_SYSTEM_V0
    property: type
    value: system
  - artifact: ai_governance::AC_AGENT_V0
    property: type
    value: agent
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    property: layer
    value: DOMAINS
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    property: layer
    value: DOMAINS
  - artifact: ai_governance::WF_REGISTER_EMPLOYEE_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_REGISTER_EMPLOYEE_V0
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_EMPLOYEE_REGISTERED_V0
  - artifact: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_RECORD_TRAINING_COMPLETED_V0
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_TRAINING_COMPLETED_V1
  - artifact: ai_governance::WF_SET_LICENSE_CAP_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_SET_LICENSE_CAP_V0
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_LICENSE_CAP_SET_V1
  - artifact: ai_governance::WF_PROVISION_LICENSE_V0
    property: actor_context
    value: ai_governance::AC_EMPLOYEE_V1
  - artifact: ai_governance::WF_PROVISION_LICENSE_V0
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_LICENSE_PROVISIONED_V1
  - artifact: ai_governance::WF_PROVISION_LICENSE_V0
    property: emit.EXIT_DENIED
    value:
    - ai_governance::EV_PROVISION_DENIED_V1
  - artifact: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    property: actor_context
    value: ai_governance::AC_EMPLOYEE_V1
  - artifact: ai_governance::WF_RECORD_LICENSE_USAGE_V0
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_USAGE_RECORDED_V1
  - artifact: ai_governance::WF_RECLAIM_LICENSE_V1
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_RECLAIM_LICENSE_V1
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_LICENSE_REVOKED_V1
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    property: actor_context
    value: ai_governance::AC_AGENT_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    property: emit.EXIT_COMPLETED
    value:
    - ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    property: emit.EXIT_DENIED
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V1
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V1
    property: supersedes
    value:
    - ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V1
    property: supersedes
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V1
    property: supersedes
    value:
    - ai_governance::IN_AGENT_ACTION_REQUESTED_V0
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    property: supersedes
    value:
    - ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - artifact: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1
    property: supersedes
    value:
    - ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    property: supersedes
    value:
    - ai_governance::WF_GOVERN_AGENT_ACTION_V0
  - artifact: ai_governance::AC_EMPLOYEE_V1
    property: supersedes
    value:
    - ai_governance::AC_EMPLOYEE_V0
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V1
    property: supersedes
    value:
    - ai_governance::EV_LICENSE_CAP_SET_V0
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V1
    property: supersedes
    value:
    - ai_governance::EV_LICENSE_PROVISIONED_V0
  - artifact: ai_governance::EV_LICENSE_REVOKED_V1
    property: supersedes
    value:
    - ai_governance::EV_LICENSE_REVOKED_V0
  - artifact: ai_governance::EV_PROVISION_DENIED_V1
    property: supersedes
    value:
    - ai_governance::EV_PROVISION_DENIED_V0
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V1
    property: supersedes
    value:
    - ai_governance::EV_TRAINING_COMPLETED_V0
  - artifact: ai_governance::EV_USAGE_RECORDED_V1
    property: supersedes
    value:
    - ai_governance::EV_USAGE_RECORDED_V0
  - artifact: ai_governance::IN_PROVISION_LICENSE_V0
    property: supersedes
    value:
    - ai_governance::IN_PROVISION_AI_LICENSE_V0
  - artifact: ai_governance::IN_RECLAIM_LICENSE_V1
    property: supersedes
    value:
    - ai_governance::IN_RECLAIM_LICENSE_V0
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    property: supersedes
    value:
    - ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - artifact: ai_governance::RB_LICENSE_BINDINGS_V1
    property: supersedes
    value:
    - ai_governance::RB_LICENSE_BINDINGS_V0
  - artifact: ai_governance::WF_PROVISION_LICENSE_V0
    property: supersedes
    value:
    - ai_governance::WF_PROVISION_AI_LICENSING_V0
  - artifact: ai_governance::WF_RECLAIM_LICENSE_V1
    property: supersedes
    value:
    - ai_governance::WF_RECLAIM_LICENSE_V0
  structure_stores:
  - store_name: EMPLOYEE_EMPLOYEE_ID_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: ai_governance/ai_licensing/employee_employee_id_registry.jsonl
    used_by: ai_governance::CC_CLAIM_EMPLOYEE_ID_V0, ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: EMPLOYEES
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/ai_licensing/employees.json
    used_by: ai_governance::CC_RECORD_TRAINING_COMPLETED_V0, ai_governance::CC_RESOLVE_EMPLOYEE_IDENTITY_V0,
      ai_governance::CC_WRITE_EMPLOYEE_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: LICENSE_AUDIT
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: ai_governance/ai_licensing/audit_log.jsonl
    used_by: ai_governance::CC_RECORD_AI_LICENSING_MOMENT_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: LICENSE_CAPS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/ai_licensing/license_caps.json
    used_by: ai_governance::CC_REQUIRE_CAP_SET_V0, ai_governance::CC_WRITE_LICENSE_CAP_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: LICENSE_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: ai_governance/ai_licensing/license_identity_registry.jsonl
    used_by: ai_governance::CC_CLAIM_LICENSE_IDENTITY_V0, ai_governance::CC_RELEASE_LICENSE_IDENTITY_V0,
      ai_governance::CC_REQUIRE_UNDER_THE_CAP_V0, ai_governance::CC_RESOLVE_LICENSE_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: LICENSES
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/ai_licensing/licenses.json
    used_by: ai_governance::CC_MOVE_LICENSE_FROM_ACTIVE_V0, ai_governance::CC_RECORD_LICENSE_USAGE_V0,
      ai_governance::CC_RESOLVE_LICENSE_V0, ai_governance::CC_WRITE_LICENSE_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
  - store_name: ACTION_IDENTITY_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: ai_governance/agent_governance/action_identity_registry.jsonl
    used_by: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - store_name: ACTIONS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/agent_governance/actions.json
    used_by: ai_governance::CC_CLAIM_ACTION_IDENTITY_V0, ai_governance::CC_WRITE_ACTION_V0
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  - store_name: GOVERNANCE_AUDIT
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: ai_governance/agent_governance/governance_audit.jsonl
    used_by: ai_governance::CC_RECORD_AGENT_GOVERNANCE_MOMENT_V0
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
  transport_bindings: []
  declared_reach:
  - act: ai_governance::WF_GOVERN_AGENT_ACTION_V1
    consults:
    - ai_governance::RB_LICENSE_BINDINGS_V1
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    expected_outcome: SUCCESS
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    expected_outcome: SUCCESS
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    expected_outcome: VIOLATION
  test_case_values:
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: last_active_date
    value: '2024-01-01T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: INPUT
    field: threshold_days
    value: 30
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: EXPECTED
    field: is_inactive
    value: true
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_past_threshold
    role: EXPECTED
    field: days_inactive
    value: 45
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: last_active_date
    value: '2024-01-16T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: INPUT
    field: threshold_days
    value: 30
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: EXPECTED
    field: is_inactive
    value: true
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: inactive_at_threshold
    role: EXPECTED
    field: days_inactive
    value: 30
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: last_active_date
    value: '2024-02-10T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: evaluation_date
    value: '2024-02-15T00:00:00Z'
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    case: refuses_recently_used
    role: INPUT
    field: threshold_days
    value: 30
  generation_provenance: []
  artifact_summary:
  - action: NEW
    subdomain: agent_governance
    count: '1'
    artifacts: ai_governance::WF_RECLAIM_LICENSE_V1
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `ai_governance`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`ai_governance` is a dossier designed against the composition.
