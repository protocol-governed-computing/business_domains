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
  existing_inventory: []
  new_artifacts:
  - family: AC
    code: ai_governance::AC_AGENT_V0
    summary: Probabilistic intent emitter
    owner_subdomain: agent_governance
    status: NEW
  - family: AC
    code: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    summary: Isolated side-effect executor
    owner_subdomain: agent_governance
    status: NEW
  - family: AC
    code: ai_governance::AC_SYSTEM_GOVERNOR_V0
    summary: Governance execution authority
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    summary: Map license tier to allowed tool set and verify tool authorization
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    summary: Verify requested tool exists in closed tool registry
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    summary: Validate request schema and generate deterministic intent hash
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_RECORD_DENIED_ACTION_V0
    summary: Record denied governance decision and emit audit trail
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    summary: Record authorized governance decision and emit audit trail
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    summary: Read license facts for requesting user and validate license is active
    owner_subdomain: agent_governance
    status: NEW
  - family: CC
    code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    summary: Enforce declared parameter constraints for an authorized tool
    owner_subdomain: agent_governance
    status: NEW
  - family: EV
    code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    summary: Agent action authorized by governance
    owner_subdomain: agent_governance
    status: NEW
  - family: EV
    code: ai_governance::EV_AGENT_ACTION_DENIED_V0
    summary: Agent action denied by governance
    owner_subdomain: agent_governance
    status: NEW
  - family: IN
    code: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    summary: Request governance mediation of agent-proposed action
    owner_subdomain: agent_governance
    status: NEW
  - family: STRUCTURE
    code: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    summary: Agent governance domain storage topology
    owner_subdomain: agent_governance
    status: NEW
  - family: RB
    code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    summary: Runtime binding of agent governance capability side effects
    owner_subdomain: agent_governance
    status: NEW
  - family: WF
    code: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    summary: Constitutional mediation of agent-proposed actions with license-tier authority binding
    owner_subdomain: agent_governance
    status: NEW
  - family: AC
    code: ai_governance::AC_EMPLOYEE_V0
    summary: Employee Actor
    owner_subdomain: ai_licensing
    status: NEW
  - family: AC
    code: ai_governance::AC_SYSTEM_V0
    summary: System Authority Actor
    owner_subdomain: ai_licensing
    status: NEW
  - family: CC
    code: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    summary: Append decision event to audit log
    owner_subdomain: ai_licensing
    status: NEW
  - family: CC
    code: ai_governance::CC_PROVISION_LICENSE_V0
    summary: Register license assignment for employee
    owner_subdomain: ai_licensing
    status: NEW
  - family: CC
    code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    summary: Reclaim license from inactive user
    owner_subdomain: ai_licensing
    status: NEW
  - family: CC
    code: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    summary: Validate employee eligibility for license provisioning
    owner_subdomain: ai_licensing
    status: NEW
  - family: CT
    code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    summary: Evaluate whether license quota remains available under the declared cap
    owner_subdomain: ai_licensing
    status: NEW
  - family: CT
    code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    summary: Evaluate whether required training has been completed
    owner_subdomain: ai_licensing
    status: NEW
  - family: CT
    code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    summary: Evaluate license inactivity against a declared threshold
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_EMPLOYEE_REGISTERED_V0
    summary: Employee Registered
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_LICENSE_CAP_SET_V0
    summary: License Cap Set
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_LICENSE_PROVISIONED_V0
    summary: License Provisioned
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_LICENSE_REVOKED_V0
    summary: License Revoked
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_PROVISION_DENIED_V0
    summary: Provision Denied
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_TRAINING_COMPLETED_V0
    summary: Training Completed
    owner_subdomain: ai_licensing
    status: NEW
  - family: EV
    code: ai_governance::EV_USAGE_RECORDED_V0
    summary: Usage Recorded
    owner_subdomain: ai_licensing
    status: NEW
  - family: IN
    code: ai_governance::IN_DENY_PROVISION_V0
    summary: Handle provision denial
    owner_subdomain: ai_licensing
    status: NEW
  - family: IN
    code: ai_governance::IN_PROVISION_AI_LICENSE_V0
    summary: Request AI license provisioning
    owner_subdomain: ai_licensing
    status: NEW
  - family: IN
    code: ai_governance::IN_RECLAIM_LICENSE_V0
    summary: Request license reclamation evaluation
    owner_subdomain: ai_licensing
    status: NEW
  - family: STRUCTURE
    code: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    summary: AI licensing subdomain storage topology
    owner_subdomain: ai_licensing
    status: NEW
  - family: RB
    code: ai_governance::RB_LICENSE_BINDINGS_V0
    summary: Runtime binding of license management capability side effects
    owner_subdomain: ai_licensing
    status: NEW
  - family: VOCAB
    code: ai_governance::VOCAB_AI_LICENSING_STATES_V0
    summary: ''
    owner_subdomain: ai_licensing
    status: NEW
  - family: WF
    code: ai_governance::WF_AUTO_RECLAIM_V0
    summary: Autonomous license reclamation
    owner_subdomain: ai_licensing
    status: NEW
  - family: WF
    code: ai_governance::WF_DENY_PROVISION_V0
    summary: Handle provisioning denial
    owner_subdomain: ai_licensing
    status: NEW
  - family: WF
    code: ai_governance::WF_PROVISION_AI_LICENSING_V0
    summary: Process AI license provisioning request
    owner_subdomain: ai_licensing
    status: NEW
  rb_declarations:
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    binds_wf: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    binds_wf: ai_governance::WF_AUTO_RECLAIM_V0
    cs_bindings:
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    binds_wf: ai_governance::WF_DENY_PROVISION_V0
    cs_bindings:
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    binds_wf: ai_governance::WF_PROVISION_AI_LICENSING_V0
    cs_bindings:
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  execution_topology:
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: IN_AGENT_ACTION_REQUESTED_V0
    node_type: IN
    routing:
      ACK: CC_NORMALIZE_AGENT_REQUEST_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_NORMALIZE_AGENT_REQUEST_V0
    node_type: CC
    routing:
      SUCCESS: CC_CHECK_TOOL_DECLARED_V0
      VIOLATION: EXIT_ERROR
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_CHECK_TOOL_DECLARED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_LICENSE_TIER_V0
      VIOLATION: CC_AUDIT_UNDECLARED_TOOL
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_RESOLVE_LICENSE_TIER_V0
    node_type: CC
    routing:
      SUCCESS: CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
      NOT_FOUND: CC_AUDIT_UNAUTHORIZED_ACTOR
      VIOLATION: CC_AUDIT_UNAUTHORIZED_ACTOR
      BACKEND_ERROR: EXIT_ERROR
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    node_type: CC
    routing:
      SUCCESS: CC_VALIDATE_TOOL_PARAMETERS_V0
      VIOLATION: CC_AUDIT_UNAUTHORIZED_TOOL
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_VALIDATE_TOOL_PARAMETERS_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_GOVERNED_ACTION_V0
      VIOLATION: CC_AUDIT_PARAMETER_VIOLATION
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_RECORD_GOVERNED_ACTION_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      ALREADY_EXISTS: EXIT_SUCCESS
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_AUDIT_UNDECLARED_TOOL
    node_type: CC
    routing:
      SUCCESS: EXIT_UNDECLARED_TOOL
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_RECORD_DENIED_ACTION_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_AUDIT_UNAUTHORIZED_ACTOR
    node_type: CC
    routing:
      SUCCESS: EXIT_UNAUTHORIZED_ACTOR
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_RECORD_DENIED_ACTION_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_AUDIT_UNAUTHORIZED_TOOL
    node_type: CC
    routing:
      SUCCESS: EXIT_UNAUTHORIZED_TOOL
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_RECORD_DENIED_ACTION_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: CC_AUDIT_PARAMETER_VIOLATION
    node_type: CC
    routing:
      SUCCESS: EXIT_PARAMETER_VIOLATION
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_RECORD_DENIED_ACTION_V0
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_UNDECLARED_TOOL
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_UNAUTHORIZED_ACTOR
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_UNAUTHORIZED_TOOL
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_PARAMETER_VIOLATION
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_ERROR
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: IN_RECLAIM_LICENSE_V0
    node_type: IN
    routing:
      ACK: CC_RECLAIM_UNUSED_LICENSE_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: CC_RECLAIM_UNUSED_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_AUDIT_EVENT_RECLAIMED
      VIOLATION: EXIT_ACTIVE
      NOT_FOUND: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: CC_APPEND_AUDIT_EVENT_RECLAIMED
    node_type: CC
    routing:
      SUCCESS: EXIT_RECLAIMED
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_APPEND_AUDIT_EVENT_V0
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: EXIT_RECLAIMED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: EXIT_ACTIVE
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_AUTO_RECLAIM_V0
    node: EXIT_ERROR
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_DENY_PROVISION_V0
    node: IN_DENY_PROVISION_V0
    node_type: IN
    routing:
      ACK: CC_APPEND_AUDIT_EVENT_V0
      NACK: EXIT_ERROR
  - workflow: ai_governance::WF_DENY_PROVISION_V0
    node: CC_APPEND_AUDIT_EVENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
  - workflow: ai_governance::WF_DENY_PROVISION_V0
    node: EXIT_DENIED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_DENY_PROVISION_V0
    node: EXIT_ERROR
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: IN_PROVISION_AI_LICENSE_V0
    node_type: IN
    routing:
      ACK: CC_VALIDATE_ELIGIBILITY_V0
      NACK: EXIT_REJECTED
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: CC_VALIDATE_ELIGIBILITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_PROVISION_LICENSE_V0
      VIOLATION: CC_APPEND_AUDIT_EVENT_DENIED
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: CC_PROVISION_LICENSE_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_AUDIT_EVENT_SUCCESS
      ALREADY_EXISTS: EXIT_ERROR
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: CC_APPEND_AUDIT_EVENT_SUCCESS
    node_type: CC
    routing:
      SUCCESS: EXIT_PROVISIONED
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_APPEND_AUDIT_EVENT_V0
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: CC_APPEND_AUDIT_EVENT_DENIED
    node_type: CC
    routing:
      SUCCESS: EXIT_DENIED
      VIOLATION: EXIT_ERROR
      BACKEND_ERROR: EXIT_ERROR
    runs: CC_APPEND_AUDIT_EVENT_V0
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: EXIT_PROVISIONED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: EXIT_DENIED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: ai_governance::WF_PROVISION_AI_LICENSING_V0
    node: EXIT_ERROR
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: '1'
    step_name: lookup_tier_tools
    capability: capability_transforms::CT_PURE_LOOKUP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - key
    - map
    produces:
    - allowed_tools
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        map: map
      out:
        allowed_tools: allowed_tools
  - cc_code: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: '2'
    step_name: validate_tool_membership
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_authorized
    - allowed_tools
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
        is_authorized: is_authorized
        allowed_tools: allowed_tools
  - cc_code: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    step: '1'
    step_name: check_tool_declared
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_declared
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
        is_declared: is_declared
  - cc_code: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    step: '1'
    step_name: generate_intent_hash
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - prefix
    - data
    produces:
    - intent_hash
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prefix: prefix
        data: data
      out:
        intent_hash: intent_hash
  - cc_code: ai_governance::CC_RECORD_DENIED_ACTION_V0
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
  - cc_code: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: '2'
    step_name: generate_action_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - prefix
    - data
    produces:
    - action_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prefix: prefix
        data: data
      out:
        action_id: action_id
  - cc_code: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: '3'
    step_name: append_denial_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: GOVERNANCE_AUDIT
    consumes:
    - record
    produces:
    - result_status
    - action_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
      out:
        result_status: result_status
        action_id: action_id
  - cc_code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
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
  - cc_code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: '2'
    step_name: generate_action_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - prefix
    - data
    produces:
    - action_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        prefix: prefix
        data: data
      out:
        action_id: action_id
  - cc_code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: '3'
    step_name: register_action
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: null
    consumes:
    - key
    - target_ref
    - metadata
    produces:
    - result_status
    routing:
      SUCCESS: continue
      ALREADY_EXISTS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        target_ref: target_ref
        metadata: metadata
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: '4'
    step_name: append_audit_record
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: GOVERNANCE_AUDIT
    consumes:
    - record
    produces:
    - result_status
    - action_id
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
      out:
        result_status: result_status
        action_id: action_id
  - cc_code: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: '1'
    step_name: read_license_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: LICENSE_FACTS
    consumes:
    - key
    produces:
    - license_status
    - license_tier
    - org_unit
    routing:
      SUCCESS: continue
      NOT_FOUND: exit
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
      out:
        license_status: license_status
        license_tier: license_tier
        org_unit: org_unit
  - cc_code: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: '2'
    step_name: validate_active_status
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_active
    - license_status
    - license_tier
    - org_unit
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
        is_active: is_active
        license_status: license_status
        license_tier: license_tier
        org_unit: org_unit
  - cc_code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: '1'
    step_name: lookup_parameter_rules
    capability: capability_transforms::CT_PURE_LOOKUP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - key
    - map
    produces:
    - rules
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        map: map
      out:
        rules: rules
  - cc_code: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: '2'
    step_name: validate_parameters
    capability: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - parameters
    - rules
    produces:
    - validation_result
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        validation_result: validation_result
  - cc_code: ai_governance::CC_APPEND_AUDIT_EVENT_V0
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
  - cc_code: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    step: '2'
    step_name: append_audit_event
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: LICENSE_AUDIT
    consumes:
    - record
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
        record: record
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_PROVISION_LICENSE_V0
    step: '1'
    step_name: register_license
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: null
    consumes:
    - key
    - target_cs
    - target_ref
    produces:
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
        result_status: result_status
  - cc_code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: '1'
    step_name: evaluate_inactivity
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
    - days_inactive
    routing:
      SUCCESS: continue
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
        days_inactive: days_inactive
  - cc_code: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: '2'
    step_name: deregister_license
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: DEREGISTER
    store: LICENSE_REGISTRY
    consumes:
    - key_or_address
    produces:
    - result_status
    routing:
      SUCCESS: exit
      NOT_FOUND: exit
      BACKEND_ERROR: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_or_address: key_or_address
      out:
        result_status: result_status
  - cc_code: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: '1'
    step_name: check_training_status
    capability: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - training_completed
    produces:
    - is_eligible
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        training_completed: training_completed
      out:
        is_eligible: is_eligible
  - cc_code: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: '2'
    step_name: check_quota_available
    capability: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - assigned_count
    - quota
    produces:
    - quota_available
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        assigned_count: assigned_count
        quota: quota
      out:
        quota_available: quota_available
  step_bindings:
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: lookup_tier_tools
    direction: INPUT
    field: key
    bound_to: inputs.license_tier
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: lookup_tier_tools
    direction: INPUT
    field: map
    bound_to:
      literal:
        none:
        - READ_RECORD
        standard:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        enterprise:
        - READ_RECORD
        - PROVISION_STANDARD_LICENSE
        - PROVISION_PREMIUM_LICENSE
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: lookup_tier_tools
    direction: OUTPUT
    field: allowed_tools
    bound_to: capability_result.result
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: validate_tool_membership
    direction: INPUT
    field: value
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: validate_tool_membership
    direction: INPUT
    field: allowed_set
    bound_to: results.lookup_tier_tools.allowed_tools
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: validate_tool_membership
    direction: OUTPUT
    field: is_authorized
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    step: validate_tool_membership
    direction: OUTPUT
    field: allowed_tools
    bound_to: results.lookup_tier_tools.allowed_tools
  - owner: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    step: check_tool_declared
    direction: INPUT
    field: value
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    step: check_tool_declared
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - READ_RECORD
      - PROVISION_STANDARD_LICENSE
      - PROVISION_PREMIUM_LICENSE
  - owner: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    step: check_tool_declared
    direction: OUTPUT
    field: is_declared
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    step: generate_intent_hash
    direction: INPUT
    field: prefix
    bound_to:
      literal: AREQ
  - owner: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    step: generate_intent_hash
    direction: INPUT
    field: data
    bound_to:
      literal:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
  - owner: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    step: generate_intent_hash
    direction: OUTPUT
    field: intent_hash
    bound_to: capability_result.id
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: generate_action_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: AGOV
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: generate_action_id
    direction: INPUT
    field: data
    bound_to:
      literal:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        domain_context: $.inputs.domain_context
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: generate_action_id
    direction: OUTPUT
    field: action_id
    bound_to: capability_result.id
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: append_denial_record
    direction: INPUT
    field: record
    bound_to:
      literal:
        event_code: ai_governance::EV_AGENT_ACTION_DENIED_V0
        action_id: $.results.generate_action_id.action_id
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        denial_reason: $.inputs.denial_reason
        decision: DENIED
        timestamp: $.results.read_now.timestamp
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: append_denial_record
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: ai_governance::CC_RECORD_DENIED_ACTION_V0
    step: append_denial_record
    direction: OUTPUT
    field: action_id
    bound_to: results.generate_action_id.action_id
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: generate_action_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: AGOV
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: generate_action_id
    direction: INPUT
    field: data
    bound_to:
      literal:
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        intent_hash: $.inputs.intent_hash
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: generate_action_id
    direction: OUTPUT
    field: action_id
    bound_to: capability_result.id
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: register_action
    direction: INPUT
    field: key
    bound_to: results.generate_action_id.action_id
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: register_action
    direction: INPUT
    field: target_ref
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: register_action
    direction: INPUT
    field: metadata
    bound_to:
      literal:
        requesting_user_id: $.inputs.requesting_user_id
        license_tier: $.inputs.license_tier
        parameters: $.inputs.parameters
        domain_context: $.inputs.domain_context
        intent_hash: $.inputs.intent_hash
        decision: AUTHORIZED
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: register_action
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: append_audit_record
    direction: INPUT
    field: record
    bound_to:
      literal:
        event_code: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
        action_id: $.results.generate_action_id.action_id
        tool_name: $.inputs.tool_name
        requesting_user_id: $.inputs.requesting_user_id
        license_tier: $.inputs.license_tier
        parameters: $.inputs.parameters
        decision: AUTHORIZED
        timestamp: $.results.read_now.timestamp
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: append_audit_record
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    step: append_audit_record
    direction: OUTPUT
    field: action_id
    bound_to: results.generate_action_id.action_id
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: read_license_record
    direction: INPUT
    field: key
    bound_to: inputs.requesting_user_id
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: read_license_record
    direction: OUTPUT
    field: license_status
    bound_to: capability_result.value.license_status
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: read_license_record
    direction: OUTPUT
    field: license_tier
    bound_to: capability_result.value.license_tier
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: read_license_record
    direction: OUTPUT
    field: org_unit
    bound_to: capability_result.value.org_unit
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: INPUT
    field: value
    bound_to: results.read_license_record.license_status
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - active
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: OUTPUT
    field: is_active
    bound_to: capability_result.is_member
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: OUTPUT
    field: license_status
    bound_to: results.read_license_record.license_status
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: OUTPUT
    field: license_tier
    bound_to: results.read_license_record.license_tier
  - owner: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    step: validate_active_status
    direction: OUTPUT
    field: org_unit
    bound_to: results.read_license_record.org_unit
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: lookup_parameter_rules
    direction: INPUT
    field: key
    bound_to: inputs.tool_name
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: lookup_parameter_rules
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
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: lookup_parameter_rules
    direction: OUTPUT
    field: rules
    bound_to: capability_result.result
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: validate_parameters
    direction: INPUT
    field: parameters
    bound_to: inputs.parameters
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: validate_parameters
    direction: INPUT
    field: rules
    bound_to: results.lookup_parameter_rules.rules
  - owner: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    step: validate_parameters
    direction: OUTPUT
    field: validation_result
    bound_to: capability_result.valid
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_CHECK_TOOL_DECLARED_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RESOLVE_LICENSE_TIER_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: INPUT
    field: license_tier
    bound_to: results.CC_RESOLVE_LICENSE_TIER_V0.license_tier
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: INPUT
    field: parameters
    bound_to: payload.parameters
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: parameters
    bound_to: payload.parameters
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: license_tier
    bound_to: results.CC_RESOLVE_LICENSE_TIER_V0.license_tier
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: intent_hash
    bound_to: results.CC_NORMALIZE_AGENT_REQUEST_V0.intent_hash
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNDECLARED_TOOL
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNDECLARED_TOOL
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNDECLARED_TOOL
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNDECLARED_TOOL
    direction: INPUT
    field: denial_reason
    bound_to:
      literal: UNDECLARED_TOOL
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_ACTOR
    direction: INPUT
    field: denial_reason
    bound_to:
      literal: UNAUTHORIZED_ACTOR
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_TOOL
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_TOOL
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_TOOL
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_UNAUTHORIZED_TOOL
    direction: INPUT
    field: denial_reason
    bound_to:
      literal: UNAUTHORIZED_TOOL
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_PARAMETER_VIOLATION
    direction: INPUT
    field: tool_name
    bound_to: payload.tool_name
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_PARAMETER_VIOLATION
    direction: INPUT
    field: requesting_user_id
    bound_to: payload.requesting_user_id
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_PARAMETER_VIOLATION
    direction: INPUT
    field: domain_context
    bound_to: payload.domain_context
  - owner: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    step: CC_AUDIT_PARAMETER_VIOLATION
    direction: INPUT
    field: denial_reason
    bound_to:
      literal: PARAMETER_VIOLATION
  - owner: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    step: append_audit_event
    direction: INPUT
    field: record
    bound_to:
      literal:
        event_type: $.inputs.event_type
        employee_id: $.inputs.employee_id
        decision: $.inputs.decision
        reason_code: $.inputs.reason_code
        license_id: $.inputs.license_id
        payload: $.inputs.data
        timestamp: $.results.read_now.timestamp
  - owner: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    step: append_audit_event
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_PROVISION_LICENSE_V0
    step: register_license
    direction: INPUT
    field: key
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_PROVISION_LICENSE_V0
    step: register_license
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_REGISTRY_V0
  - owner: ai_governance::CC_PROVISION_LICENSE_V0
    step: register_license
    direction: INPUT
    field: target_ref
    bound_to: inputs.license_id
  - owner: ai_governance::CC_PROVISION_LICENSE_V0
    step: register_license
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: evaluate_inactivity
    direction: INPUT
    field: last_active_date
    bound_to: inputs.last_active_date
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: evaluate_inactivity
    direction: INPUT
    field: evaluation_date
    bound_to: inputs.evaluation_date
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: evaluate_inactivity
    direction: INPUT
    field: threshold_days
    bound_to: inputs.threshold_days
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: evaluate_inactivity
    direction: OUTPUT
    field: is_inactive
    bound_to: capability_result.is_inactive
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: evaluate_inactivity
    direction: OUTPUT
    field: days_inactive
    bound_to: capability_result.days_inactive
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: deregister_license
    direction: INPUT
    field: key_or_address
    bound_to: inputs.employee_id
  - owner: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    step: deregister_license
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: check_training_status
    direction: INPUT
    field: training_completed
    bound_to: inputs.training_completed
  - owner: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: check_training_status
    direction: OUTPUT
    field: is_eligible
    bound_to: capability_result.training_eligible
  - owner: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: check_quota_available
    direction: INPUT
    field: assigned_count
    bound_to: inputs.assigned_count
  - owner: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: check_quota_available
    direction: INPUT
    field: quota
    bound_to: inputs.cap
  - owner: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    step: check_quota_available
    direction: OUTPUT
    field: quota_available
    bound_to: capability_result.quota_available
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: license_id
    bound_to: payload.license_id
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.context.employee_id
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: last_active_date
    bound_to: payload.context.last_active_date
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: evaluation_date
    bound_to: payload.context.evaluation_date
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: threshold_days
    bound_to: payload.threshold_days
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_APPEND_AUDIT_EVENT_RECLAIMED
    direction: INPUT
    field: event_type
    bound_to:
      literal: ai_governance::EV_LICENSE_REVOKED_V0
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_APPEND_AUDIT_EVENT_RECLAIMED
    direction: INPUT
    field: employee_id
    bound_to: payload.context.employee_id
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_APPEND_AUDIT_EVENT_RECLAIMED
    direction: INPUT
    field: decision
    bound_to:
      literal: RECLAIMED
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_APPEND_AUDIT_EVENT_RECLAIMED
    direction: INPUT
    field: reason_code
    bound_to:
      literal: INACTIVITY
  - owner: ai_governance::WF_AUTO_RECLAIM_V0
    step: CC_APPEND_AUDIT_EVENT_RECLAIMED
    direction: INPUT
    field: data
    bound_to:
      literal:
        license_id: $.payload.license_id
        days_inactive: $.payload.context.days_inactive
  - owner: ai_governance::WF_DENY_PROVISION_V0
    step: CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: event_type
    bound_to:
      literal: ai_governance::EV_PROVISION_DENIED_V0
  - owner: ai_governance::WF_DENY_PROVISION_V0
    step: CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_DENY_PROVISION_V0
    step: CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: DENIED
  - owner: ai_governance::WF_DENY_PROVISION_V0
    step: CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: reason_code
    bound_to: payload.reason_code
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: training_completed
    bound_to: payload.context.training_completed
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: assigned_count
    bound_to: payload.context.assigned_count
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: cap
    bound_to: payload.context.cap
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_PROVISION_LICENSE_V0
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_PROVISION_LICENSE_V0
    direction: INPUT
    field: license_id
    bound_to: payload.generated.license_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: event_type
    bound_to:
      literal: ai_governance::EV_LICENSE_PROVISIONED_V0
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: decision
    bound_to:
      literal: PROVISIONED
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: reason_code
    bound_to:
      literal: ''
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: license_id
    bound_to: payload.generated.license_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_SUCCESS
    direction: INPUT
    field: data
    bound_to:
      literal: {}
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_DENIED
    direction: INPUT
    field: event_type
    bound_to:
      literal: ai_governance::EV_PROVISION_DENIED_V0
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_DENIED
    direction: INPUT
    field: employee_id
    bound_to: payload.employee_id
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_DENIED
    direction: INPUT
    field: decision
    bound_to:
      literal: DENIED
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_DENIED
    direction: INPUT
    field: reason_code
    bound_to: payload.context.reason_code
  - owner: ai_governance::WF_PROVISION_AI_LICENSING_V0
    step: CC_APPEND_AUDIT_EVENT_DENIED
    direction: INPUT
    field: data
    bound_to:
      literal: {}
  interface_fields:
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
  - artifact: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    direction: ATTRIBUTE
    field: runtime_id
    type: string
    required: 'YES'
    default: null
    meaning: runtime id
  - artifact: ai_governance::AC_SYSTEM_GOVERNOR_V0
    direction: ATTRIBUTE
    field: governor_id
    type: string
    required: 'YES'
    default: null
    meaning: governor id
  - artifact: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: INPUT
    field: license_tier
    type: string
    required: 'YES'
    default: null
    meaning: license tier
  - artifact: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: OUTPUT
    field: allowed_tools
    type: array
    required: 'NO'
    default: null
    meaning: allowed tools
  - artifact: ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0
    direction: OUTPUT
    field: is_authorized
    type: boolean
    required: 'NO'
    default: null
    meaning: is authorized
  - artifact: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_CHECK_TOOL_DECLARED_V0
    direction: OUTPUT
    field: is_declared
    type: boolean
    required: 'NO'
    default: null
    meaning: is declared
  - artifact: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0
    direction: OUTPUT
    field: intent_hash
    type: string
    required: 'NO'
    default: null
    meaning: intent hash
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: INPUT
    field: denial_reason
    type: string
    required: 'YES'
    default: null
    meaning: denial reason
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: OUTPUT
    field: action_id
    type: string
    required: 'NO'
    default: null
    meaning: action id
  - artifact: ai_governance::CC_RECORD_DENIED_ACTION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: null
    meaning: parameters
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: license_tier
    type: string
    required: 'YES'
    default: null
    meaning: license tier
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: domain context
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: INPUT
    field: intent_hash
    type: string
    required: 'YES'
    default: null
    meaning: intent hash
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: OUTPUT
    field: action_id
    type: string
    required: 'NO'
    default: null
    meaning: action id
  - artifact: ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    direction: OUTPUT
    field: license_status
    type: string
    required: 'NO'
    default: null
    meaning: license status
  - artifact: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    direction: OUTPUT
    field: license_tier
    type: string
    required: 'NO'
    default: null
    meaning: license tier
  - artifact: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    direction: OUTPUT
    field: org_unit
    type: string
    required: 'NO'
    default: null
    meaning: org unit
  - artifact: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    direction: OUTPUT
    field: is_active
    type: boolean
    required: 'NO'
    default: null
    meaning: is active
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: null
    meaning: parameters
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: OUTPUT
    field: rules
    type: array
    required: 'NO'
    default: null
    meaning: rules
  - artifact: ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0
    direction: OUTPUT
    field: validation_result
    type: boolean
    required: 'NO'
    default: null
    meaning: validation result
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: action_id
    type: string
    required: 'YES'
    default: null
    meaning: action id
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: license_tier
    type: string
    required: 'YES'
    default: null
    meaning: license tier
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: decision
    type: string
    required: 'YES'
    default: null
    meaning: decision
  - artifact: ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: action_id
    type: string
    required: 'YES'
    default: null
    meaning: action id
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: tool name
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: requesting user id
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: denial_reason
    type: string
    required: 'YES'
    default: null
    meaning: denial reason
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: decision
    type: string
    required: 'YES'
    default: null
    meaning: decision
  - artifact: ai_governance::EV_AGENT_ACTION_DENIED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    direction: INPUT
    field: tool_name
    type: string
    required: 'YES'
    default: null
    meaning: Requested tool identifier from closed registry
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    direction: INPUT
    field: parameters
    type: object
    required: 'YES'
    default: null
    meaning: Tool-specific parameter key-value map
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    direction: INPUT
    field: requesting_user_id
    type: string
    required: 'YES'
    default: null
    meaning: Identifier of the user the agent acts on behalf of
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    direction: INPUT
    field: domain_context
    type: string
    required: 'YES'
    default: null
    meaning: Domain context for the request
  - artifact: ai_governance::IN_AGENT_ACTION_REQUESTED_V0
    direction: INPUT
    field: request_id
    type: string
    required: 'NO'
    default: null
    meaning: Client-provided request correlation ID
  - artifact: ai_governance::AC_EMPLOYEE_V0
    direction: ATTRIBUTE
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::AC_EMPLOYEE_V0
    direction: ATTRIBUTE
    field: training_completed
    type: boolean
    required: 'NO'
    default: false
    meaning: training completed
  - artifact: ai_governance::AC_SYSTEM_V0
    direction: ATTRIBUTE
    field: role
    type: string
    required: 'YES'
    default: null
    meaning: role
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: event_type
    type: string
    required: 'YES'
    default: null
    meaning: event type
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: null
    meaning: decision
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: reason_code
    type: string
    required: 'NO'
    default: null
    meaning: reason code
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'NO'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: INPUT
    field: data
    type: object
    required: 'NO'
    default: null
    meaning: data
  - artifact: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_PROVISION_LICENSE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_PROVISION_LICENSE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_PROVISION_LICENSE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: last_active_date
    type: string
    required: 'YES'
    default: null
    meaning: last active date
    format: date-time
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: evaluation_date
    type: string
    required: 'YES'
    default: null
    meaning: evaluation date
    format: date-time
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: INPUT
    field: threshold_days
    type: integer
    required: 'YES'
    default: 30
    meaning: threshold days
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'NO'
    default: null
    meaning: result status
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: OUTPUT
    field: is_inactive
    type: boolean
    required: 'NO'
    default: null
    meaning: is inactive
  - artifact: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    direction: OUTPUT
    field: days_inactive
    type: integer
    required: 'NO'
    default: null
    meaning: days inactive
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: training_completed
    type: boolean
    required: 'YES'
    default: null
    meaning: training completed
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: assigned_count
    type: integer
    required: 'YES'
    default: null
    meaning: assigned count
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: INPUT
    field: cap
    type: integer
    required: 'YES'
    default: null
    meaning: cap
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: OUTPUT
    field: is_eligible
    type: boolean
    required: 'NO'
    default: null
    meaning: is eligible
  - artifact: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    direction: OUTPUT
    field: quota_available
    type: boolean
    required: 'NO'
    default: null
    meaning: quota available
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: INPUT
    field: assigned_count
    type: integer
    required: 'YES'
    default: null
    meaning: Number of licenses currently assigned
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: INPUT
    field: quota
    type: integer
    required: 'YES'
    default: null
    meaning: Declared license cap
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: OUTPUT
    field: quota_available
    type: boolean
    required: 'YES'
    default: null
    meaning: True when at least one license remains under the cap
  - artifact: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    direction: OUTPUT
    field: remaining
    type: integer
    required: 'YES'
    default: null
    meaning: Licenses remaining under the cap, floored at zero
  - artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    direction: INPUT
    field: training_completed
    type: boolean
    required: 'YES'
    default: null
    meaning: Whether the employee has completed required AI-use training
  - artifact: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    direction: OUTPUT
    field: training_eligible
    type: boolean
    required: 'YES'
    default: null
    meaning: True when training is complete and the employee clears this gate
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
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V0
    direction: OUTPUT
    field: cap_count
    type: integer
    required: 'YES'
    default: null
    meaning: cap count
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V0
    direction: OUTPUT
    field: effective_date
    type: string
    required: 'YES'
    default: null
    meaning: effective date
    format: date-time
  - artifact: ai_governance::EV_LICENSE_CAP_SET_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V0
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V0
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_LICENSE_PROVISIONED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::EV_LICENSE_REVOKED_V0
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_LICENSE_REVOKED_V0
    direction: OUTPUT
    field: reason
    type: string
    required: 'YES'
    default: null
    meaning: reason
  - artifact: ai_governance::EV_LICENSE_REVOKED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::EV_PROVISION_DENIED_V0
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_PROVISION_DENIED_V0
    direction: OUTPUT
    field: reason_code
    type: string
    required: 'YES'
    default: null
    meaning: reason code
  - artifact: ai_governance::EV_PROVISION_DENIED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: timestamp
    format: date-time
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V0
    direction: OUTPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: employee id
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V0
    direction: OUTPUT
    field: completion_date
    type: string
    required: 'YES'
    default: null
    meaning: completion date
    format: date-time
  - artifact: ai_governance::EV_TRAINING_COMPLETED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::EV_USAGE_RECORDED_V0
    direction: OUTPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: license id
  - artifact: ai_governance::EV_USAGE_RECORDED_V0
    direction: OUTPUT
    field: last_active_date
    type: string
    required: 'YES'
    default: null
    meaning: last active date
    format: date-time
  - artifact: ai_governance::EV_USAGE_RECORDED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: ai_governance::IN_DENY_PROVISION_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: Employee whose provision was denied
  - artifact: ai_governance::IN_DENY_PROVISION_V0
    direction: INPUT
    field: reason_code
    type: string
    required: 'YES'
    default: null
    meaning: Reason for denial
  - artifact: ai_governance::IN_PROVISION_AI_LICENSE_V0
    direction: INPUT
    field: employee_id
    type: string
    required: 'YES'
    default: null
    meaning: Employee requesting license
  - artifact: ai_governance::IN_PROVISION_AI_LICENSE_V0
    direction: INPUT
    field: context
    type: object
    required: 'NO'
    default: null
    meaning: Runtime context data (training_completed, assigned_count, cap, reason_code)
  - artifact: ai_governance::IN_PROVISION_AI_LICENSE_V0
    direction: INPUT
    field: generated
    type: object
    required: 'NO'
    default: null
    meaning: Generated data (license_id)
  - artifact: ai_governance::IN_RECLAIM_LICENSE_V0
    direction: INPUT
    field: license_id
    type: string
    required: 'YES'
    default: null
    meaning: License to evaluate
  - artifact: ai_governance::IN_RECLAIM_LICENSE_V0
    direction: INPUT
    field: threshold_days
    type: integer
    required: 'NO'
    default: 30
    meaning: Inactivity threshold in days
  - artifact: ai_governance::IN_RECLAIM_LICENSE_V0
    direction: INPUT
    field: context
    type: object
    required: 'NO'
    default: null
    meaning: Runtime context data (employee_id, last_active_date, evaluation_date, days_inactive)
  implementation_bindings:
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    callable: execute
    operation: PURE_CHECK_QUOTA_AVAILABLE
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    callable: execute
    operation: PURE_CHECK_TRAINING_STATUS
    kind: atom
    purity: ct_pure
    refusal: raises
  - ct_code: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    callable: execute
    operation: PURE_EVALUATE_INACTIVITY
    kind: atom
    purity: ct_pure
    refusal: raises
  vocabulary_extensions:
  - vocabulary_code: ai_governance::VOCAB_AI_LICENSING_STATES_V0
    extends: vocabulary::VOCAB_EXECUTION_STATES_V0
    group: result_status
    casing: UPPER_SNAKE
    names_kind: null
    value: CAP_REACHED
    meaning: CAP_REACHED
  runtime_policies:
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: null
    value: null
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: path
    value: '{{module_data_root}}/ai_governance/agent_governance/governance_actions.json'
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: strict
    value: true
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: null
    value: null
  - rb_code: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: path
    value: '{{module_data_root}}/ai_governance/ai_licensing/license_registry.json'
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: null
    value: null
  - rb_code: ai_governance::RB_LICENSE_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
  artifact_properties:
  - artifact: ai_governance::AC_AGENT_V0
    property: description
    value: Autonomous agent that proposes actions through governance protocol
  - artifact: ai_governance::AC_AGENT_V0
    property: type
    value: agent
  - artifact: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    property: description
    value: Executes authorized actions within isolated capability boundaries
  - artifact: ai_governance::AC_ENTERPRISE_RUNTIME_V0
    property: type
    value: system
  - artifact: ai_governance::AC_SYSTEM_GOVERNOR_V0
    property: description
    value: Mediates agent-proposed actions with constitutional policy enforcement
  - artifact: ai_governance::AC_SYSTEM_GOVERNOR_V0
    property: type
    value: system
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    property: description
    value: Maps entity types to storage implementations and paths
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    property: storage_roots
    value:
      base_path: '{{module_data_root}}'
      description: Root path for all agent governance storage (resolved at runtime)
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    property: resolution
    value:
      description: Runtime path resolution strategy
      algorithm: base_path / entity_stores[entity_type].path
      example: '{{module_data_root}}/ai_governance/ai_licensing/license_facts.json'
  - artifact: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
    property: isolation
    value:
      description: Entity storage isolation constraints
      rules:
      - Each entity type has dedicated storage
      - LICENSE_FACTS is read-only — agent governance may not mutate license facts
      - GOVERNANCE_AUDIT is append-only — agent governance audit records are immutable
      - GOVERNANCE_ACTIONS registers each authorized action once — a key is never re-registered
      - Storage paths resolved via STRUCTURE only
  - artifact: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0
    property: parameters
    value:
    - module_data_root
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_GOVERNOR_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: emit.EXIT_SUCCESS
    value:
    - ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: emit.EXIT_UNDECLARED_TOOL
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: emit.EXIT_UNAUTHORIZED_ACTOR
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: emit.EXIT_UNAUTHORIZED_TOOL
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
  - artifact: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    property: emit.EXIT_PARAMETER_VIOLATION
    value:
    - ai_governance::EV_AGENT_ACTION_DENIED_V0
  - artifact: ai_governance::AC_EMPLOYEE_V0
    property: description
    value: Represents a person eligible for AI license provisioning
  - artifact: ai_governance::AC_EMPLOYEE_V0
    property: type
    value: human
  - artifact: ai_governance::AC_SYSTEM_V0
    property: description
    value: Represents a protocol authority for fact injection and automation
  - artifact: ai_governance::AC_SYSTEM_V0
    property: type
    value: system
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    property: description
    value: Maps licensing entity stores to paths under the instance data root.
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    property: storage_roots
    value:
      base_path: '{{module_data_root}}'
      description: Root path for all ai_licensing storage (resolved at runtime)
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    property: resolution
    value:
      description: Runtime path resolution strategy
      algorithm: base_path / entity_stores[entity_type].path
      example: '{{module_data_root}}/ai_governance/ai_licensing/audit_log.jsonl'
  - artifact: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
    property: isolation
    value:
      description: Entity storage isolation constraints
      rules:
      - Each entity type has dedicated storage
      - LICENSE_AUDIT is append-only — license audit records are immutable
      - All paths are scoped under ai_governance/ai_licensing — no cross-subdomain writes
      - Storage paths resolved via STRUCTURE only
  - artifact: ai_governance::RB_LICENSE_BINDINGS_V0
    property: parameters
    value:
    - module_data_root
  - artifact: ai_governance::WF_AUTO_RECLAIM_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_AUTO_RECLAIM_V0
    property: emit.EXIT_RECLAIMED
    value:
    - ai_governance::EV_LICENSE_REVOKED_V0
  - artifact: ai_governance::WF_DENY_PROVISION_V0
    property: actor_context
    value: ai_governance::AC_SYSTEM_V0
  - artifact: ai_governance::WF_DENY_PROVISION_V0
    property: emit.EXIT_DENIED
    value:
    - ai_governance::EV_PROVISION_DENIED_V0
  - artifact: ai_governance::WF_PROVISION_AI_LICENSING_V0
    property: actor_context
    value: ai_governance::AC_EMPLOYEE_V0
  - artifact: ai_governance::WF_PROVISION_AI_LICENSING_V0
    property: emit.EXIT_PROVISIONED
    value:
    - ai_governance::EV_LICENSE_PROVISIONED_V0
  - artifact: ai_governance::WF_PROVISION_AI_LICENSING_V0
    property: emit.EXIT_DENIED
    value:
    - ai_governance::EV_PROVISION_DENIED_V0
  structure_stores:
  - store_name: LICENSE_FACTS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/ai_licensing/license_facts.json
    used_by: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - store_name: GOVERNANCE_AUDIT
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: ai_governance/agent_governance/governance_audit.jsonl
    used_by: ai_governance::CC_RECORD_DENIED_ACTION_V0, ai_governance::CC_RECORD_GOVERNED_ACTION_V0
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - store_name: GOVERNANCE_ACTIONS
    storage_type: null
    proposed_path: ai_governance/agent_governance/governance_actions.json
    used_by: null
    structure: ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0
  - store_name: LICENSE_FACTS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: ai_governance/ai_licensing/license_facts.json
    used_by: ai_governance::CC_RESOLVE_LICENSE_TIER_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - store_name: LICENSE_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: ai_governance/ai_licensing/license_registry.json
    used_by: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  - store_name: LICENSE_AUDIT
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: ai_governance/ai_licensing/audit_log.jsonl
    used_by: ai_governance::CC_APPEND_AUDIT_EVENT_V0
    structure: ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0
  transport_bindings: []
  declared_reach: []
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    expected_outcome: SUCCESS
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    expected_outcome: VIOLATION
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    expected_outcome: SUCCESS
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: refuses_untrained
    expected_outcome: VIOLATION
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
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: INPUT
    field: assigned_count
    value: 5
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: INPUT
    field: quota
    value: 10
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: EXPECTED
    field: quota_available
    value: true
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: available_under_cap
    role: EXPECTED
    field: remaining
    value: 5
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    role: INPUT
    field: assigned_count
    value: 10
  - ct_code: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    case: refuses_at_cap
    role: INPUT
    field: quota
    value: 10
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    role: INPUT
    field: training_completed
    value: true
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: eligible_once_trained
    role: EXPECTED
    field: training_eligible
    value: true
  - ct_code: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    case: refuses_untrained
    role: INPUT
    field: training_completed
    value: false
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
    count: '16'
    artifacts: ai_governance::AC_AGENT_V0, ai_governance::AC_ENTERPRISE_RUNTIME_V0, ai_governance::AC_SYSTEM_GOVERNOR_V0,
      ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0, ai_governance::CC_CHECK_TOOL_DECLARED_V0, ai_governance::CC_NORMALIZE_AGENT_REQUEST_V0,
      ai_governance::CC_RECORD_DENIED_ACTION_V0, ai_governance::CC_RECORD_GOVERNED_ACTION_V0, ai_governance::CC_RESOLVE_LICENSE_TIER_V0,
      ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0, ai_governance::EV_AGENT_ACTION_AUTHORIZED_V0, ai_governance::EV_AGENT_ACTION_DENIED_V0,
      ai_governance::IN_AGENT_ACTION_REQUESTED_V0, ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V0,
      ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V0, ai_governance::WF_GOVERN_AGENT_ACTION_V0
  - action: NEW
    subdomain: ai_licensing
    count: '25'
    artifacts: ai_governance::AC_EMPLOYEE_V0, ai_governance::AC_SYSTEM_V0, ai_governance::CC_APPEND_AUDIT_EVENT_V0,
      ai_governance::CC_PROVISION_LICENSE_V0, ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0, ai_governance::CC_VALIDATE_ELIGIBILITY_V0,
      ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0,
      ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, ai_governance::EV_EMPLOYEE_REGISTERED_V0, ai_governance::EV_LICENSE_CAP_SET_V0,
      ai_governance::EV_LICENSE_PROVISIONED_V0, ai_governance::EV_LICENSE_REVOKED_V0, ai_governance::EV_PROVISION_DENIED_V0,
      ai_governance::EV_TRAINING_COMPLETED_V0, ai_governance::EV_USAGE_RECORDED_V0, ai_governance::IN_DENY_PROVISION_V0,
      ai_governance::IN_PROVISION_AI_LICENSE_V0, ai_governance::IN_RECLAIM_LICENSE_V0, ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0,
      ai_governance::RB_LICENSE_BINDINGS_V0, ai_governance::VOCAB_AI_LICENSING_STATES_V0, ai_governance::WF_AUTO_RECLAIM_V0,
      ai_governance::WF_DENY_PROVISION_V0, ai_governance::WF_PROVISION_AI_LICENSING_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `ai_governance`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`ai_governance` is a dossier designed against the composition.
