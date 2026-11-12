# Design Intent — blockchain, baseline

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: baseline
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution: []
  existing_inventory:
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: EXTEND
    summary: The participant who acts for themselves
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: AC_PARTICIPANT_V0
  - fqdn: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    action: EXTEND
    summary: Refuse a request to register actor that lacks what it requires
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
  - fqdn: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    action: EXTEND
    summary: Claim a actor's contact address
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
  - fqdn: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    action: EXTEND
    summary: Claim a wallet's address
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_WALLET_ADDRESS_V0
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    action: EXTEND
    summary: Claim a wallet's wallet id
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_CLAIM_WALLET_IDENTITY_V1
  - fqdn: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    action: EXTEND
    summary: Derive a wallet's address from the key material supplied
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_DERIVE_WALLET_ADDRESS_V0
  - fqdn: blockchain::CC_LIST_ACTORS_V0
    action: EXTEND
    summary: Answer the actors matching the criteria named
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_LIST_ACTORS_V0
  - fqdn: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    action: EXTEND
    summary: Move a actor from unverified to a state the business admits
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
  - fqdn: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    action: EXTEND
    summary: Record a moment on the identity's own trail
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_IDENTITY_MOMENT_V0
  - fqdn: blockchain::CC_RECORD_WALLET_MOMENT_V0
    action: EXTEND
    summary: Record a moment on the wallet's own trail
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RECORD_WALLET_MOMENT_V0
  - fqdn: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    action: EXTEND
    summary: Refuse a wallet for a actor who is not accepted
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_ACCEPTED_ACTOR_V0
  - fqdn: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    action: EXTEND
    summary: Refuse to reject actor without grounds
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
  - fqdn: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    action: EXTEND
    summary: Refuse when a wallet's address is already held, before any is claimed
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
  - fqdn: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    action: EXTEND
    summary: Answer which actor its identity names, and refuse when none does
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_RESOLVE_ACTOR_IDENTITY_V0
  - fqdn: blockchain::CC_WRITE_ACTOR_V0
    action: EXTEND
    summary: Write a new actor in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_ACTOR_V0
  - fqdn: blockchain::CC_WRITE_WALLET_V0
    action: EXTEND
    summary: Write a new wallet in its first state
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CC_WRITE_WALLET_V0
  - fqdn: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    action: EXTEND
    summary: Derives an address from supplied key material; the same material always yields the same address
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: CT_PURE_DERIVE_WALLET_ADDRESS_V0
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V1
    action: EXTEND
    summary: A actor accepted
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_ACTOR_ACCEPTED_V1
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: EXTEND
    summary: A actor registered unverified
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_ACTOR_REGISTERED_UNVERIFIED_V0
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    action: EXTEND
    summary: A actor rejected
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_ACTOR_REJECTED_V0
  - fqdn: blockchain::EV_WALLET_CREATED_V0
    action: EXTEND
    summary: A wallet created
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: EV_WALLET_CREATED_V0
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: EXTEND
    summary: A request to accept actor
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_ACTOR_ACCEPTANCE_V0
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: EXTEND
    summary: A request to register actor
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_ACTOR_REGISTERED_V0
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    action: EXTEND
    summary: A request to reject actor
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_ACTOR_REJECTION_V0
  - fqdn: blockchain::IN_LIST_ACTORS_V0
    action: EXTEND
    summary: A request to list actors
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_LIST_ACTORS_V0
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    action: EXTEND
    summary: A request to create wallet
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: IN_WALLET_CREATION_V0
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: EXTEND
    summary: Binds the identity's workflows to the stores and mechanisms they use
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: RB_IDENTITY_BINDINGS_V0
  - fqdn: blockchain::RB_WALLET_BINDINGS_V1
    action: EXTEND
    summary: Binds the wallet's workflows to the stores and mechanisms they use
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: RB_WALLET_BINDINGS_V1
  - fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: EXTEND
    summary: Declares the stores the identity owns and the paths they occupy
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: STRUCTURE_IDENTITY_STORAGE_V0
  - fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V1
    action: EXTEND
    summary: Declares the stores the wallet owns and the paths they occupy
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: STRUCTURE_WALLET_STORAGE_V1
  - fqdn: blockchain::TE_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: Classifies the endings of accepting an actor, including the actor that does not exist, and
      projects what was recorded.
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TE_ACCEPT_ACTOR_V0
  - fqdn: blockchain::TE_REGISTER_ACTOR_V0
    action: EXTEND
    summary: Classifies the endings of registering an actor and projects the contact address, the occurrence,
      its time and its position.
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TE_REGISTER_ACTOR_V0
  - fqdn: blockchain::TE_REJECT_ACTOR_V0
    action: EXTEND
    summary: Classifies the endings of rejecting an actor, including the actor that does not exist, and
      projects what was recorded.
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TE_REJECT_ACTOR_V0
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to accept a registered actor, and sends the act only what the caller supplies
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TI_ACCEPT_ACTOR_V0
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    action: EXTEND
    summary: Admits a request to register an actor, and sends the act only what the caller supplies and
      the person's preferences
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TI_REGISTER_ACTOR_V0
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: EXTEND
    summary: Admits a request to reject a registered actor, and sends the act only what the caller supplies
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: TI_REJECT_ACTOR_V0
  - fqdn: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    action: EXTEND
    summary: The classification values the business names for a wallet
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: VOCAB_WALLET_CLASSIFICATION_V1
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V1
    action: EXTEND
    summary: 'The governed sequence that performs: accept actor'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_ACCEPT_ACTOR_V1
  - fqdn: blockchain::WF_CREATE_WALLET_V1
    action: EXTEND
    summary: 'The governed sequence that performs: create wallet'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_CREATE_WALLET_V1
  - fqdn: blockchain::WF_LIST_ACTORS_V0
    action: EXTEND
    summary: 'The governed sequence that performs: list actors'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_LIST_ACTORS_V0
  - fqdn: blockchain::WF_REJECT_ACTOR_V1
    action: EXTEND
    summary: 'The governed sequence that performs: reject actor'
    reason: The ledger derives it with the meaning the composition holds.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_REJECT_ACTOR_V1
  - fqdn: blockchain::WF_REGISTER_ACTOR_V1
    action: REPLACE
    summary: ''
    reason: The ledger derives it with a changed meaning at 14 place(s); WF_REGISTER_ACTOR_V2 succeeds
      it.
    source_finding:
      phase: p7
      register: existing_inventory
      key: WF_REGISTER_ACTOR_V1
  new_artifacts:
  - family: CC
    code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    summary: Record a moment on the identity's own trail
    owner_subdomain: identity
    status: NEW
  - family: WF
    code: blockchain::WF_REGISTER_ACTOR_V2
    summary: 'The governed sequence that performs: register actor'
    owner_subdomain: identity
    status: NEW
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V2
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_LIST_ACTORS_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_WALLET_BINDINGS_V1
    binds_wf: blockchain::WF_CREATE_WALLET_V1
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: IN_ACTOR_REGISTERED_V0
    node_type: IN
    routing:
      ACK: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_ACTOR_V0
      ALREADY_EXISTS: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: CC_WRITE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_IDENTITY_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: CC_RECORD_IDENTITY_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_REPEATED
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: EXIT_REPEATED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: IN_ACTOR_ACCEPTANCE_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_ACTOR_IDENTITY_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: CC_RESOLVE_ACTOR_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_IDENTITY_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: CC_RECORD_IDENTITY_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_ACCEPT_ACTOR_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: IN_ACTOR_REJECTION_V0
    node_type: IN
    routing:
      ACK: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_ACTOR_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: CC_RESOLVE_ACTOR_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_IDENTITY_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: CC_RECORD_IDENTITY_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REJECT_ACTOR_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_LIST_ACTORS_V0
    node: IN_LIST_ACTORS_V0
    node_type: IN
    routing:
      ACK: CC_RECORD_IDENTITY_MOMENT_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_LIST_ACTORS_V0
    node: CC_RECORD_IDENTITY_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: CC_LIST_ACTORS_V0
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_LIST_ACTORS_V0
    node: CC_LIST_ACTORS_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      BACKEND_ERROR: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_LIST_ACTORS_V0
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_LIST_ACTORS_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: IN_WALLET_CREATION_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_ACTOR_IDENTITY_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_RESOLVE_ACTOR_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_ACCEPTED_ACTOR_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_REQUIRE_ACCEPTED_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_DERIVE_WALLET_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_DERIVE_WALLET_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_WALLET_IDENTITY_V1
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_CLAIM_WALLET_IDENTITY_V1
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_WALLET_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
      ALREADY_EXISTS: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_CLAIM_WALLET_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: CC_WRITE_WALLET_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_WRITE_WALLET_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_WALLET_MOMENT_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: CC_RECORD_WALLET_MOMENT_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_COMPLETED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: EXIT_COMPLETED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_CREATE_WALLET_V1
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: '1'
    step_name: check_actor_fields
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
  - cc_code: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
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
  - cc_code: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: '1'
    step_name: claim_contact_address
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: CONTACT_ADDRESS_REGISTRY
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
  - cc_code: blockchain::CC_WRITE_ACTOR_V0
    step: '1'
    step_name: assemble_actor_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - actor_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        actor_record: actor_record
  - cc_code: blockchain::CC_WRITE_ACTOR_V0
    step: '2'
    step_name: write_actor_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: ACTORS
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: '2'
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: ACTOR_OCCURRENCES
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: '2'
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
  - cc_code: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: ACTOR_OCCURRENCES
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
  - cc_code: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: '1'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: CONTACT_ADDRESS_REGISTRY
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
  - cc_code: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: '2'
    step_name: read_actor_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: ACTORS
    consumes:
    - key
    produces:
    - actor_record
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
        actor_record: actor_record
        result_status: result_status
  - cc_code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: '1'
    step_name: compare_verifying_authority_to_actor
    capability: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - left
    - right
    produces:
    - is_self
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        left: left
        right: right
      out:
        is_self: is_self
  - cc_code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: '2'
    step_name: refuse_self_decision
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
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        parameters: parameters
        rules: rules
      out:
        valid: valid
  - cc_code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: '3'
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
  - cc_code: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: '4'
    step_name: set_record_state
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE_WHERE
    store: ACTORS
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
  - cc_code: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    step: '1'
    step_name: require_grounds_stated
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
  - cc_code: blockchain::CC_LIST_ACTORS_V0
    step: '1'
    step_name: select_actor_records
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: SELECT
    store: ACTORS
    consumes: null
    produces:
    - records
    - result_status
    routing:
      SUCCESS: continue
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in: {}
      out:
        records: records
        result_status: result_status
  - cc_code: blockchain::CC_LIST_ACTORS_V0
    step: '2'
    step_name: select_matching_actors
    capability: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - source
    - filter
    produces:
    - matching_actors
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        source: source
        filter: filter
      out:
        matching_actors: matching_actors
  - cc_code: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    step: '1'
    step_name: require_actor_accepted
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
  - cc_code: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    step: '1'
    step_name: derive_address
    capability: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - key_material
    produces:
    - address
    routing:
      SUCCESS: exit
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_material: key_material
      out:
        address: address
  - cc_code: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: '1'
    step_name: resolve_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: WALLET_ADDRESS_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
    - result_status
    routing:
      SUCCESS: continue
      NOT_FOUND: continue
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
  - cc_code: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: '2'
    step_name: require_unheld
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
  - cc_code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: '1'
    step_name: form_wallet_id
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - wallet_id
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
        wallet_id: wallet_id
  - cc_code: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: '2'
    step_name: claim_id
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WALLET_IDENTITIES
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
  - cc_code: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: '1'
    step_name: claim_address
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WALLET_ADDRESS_REGISTRY
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
  - cc_code: blockchain::CC_WRITE_WALLET_V0
    step: '1'
    step_name: assemble_wallet_record
    capability: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - fields
    produces:
    - wallet_record
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        fields: fields
      out:
        wallet_record: wallet_record
  - cc_code: blockchain::CC_WRITE_WALLET_V0
    step: '2'
    step_name: write_wallet_record
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: WRITE
    store: WALLETS
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
  - cc_code: blockchain::CC_RECORD_WALLET_MOMENT_V0
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
  - cc_code: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: '2'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: WALLET_OCCURRENCES
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
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: check_actor_fields
    direction: INPUT
    field: record
    bound_to: inputs.submission
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: check_actor_fields
    direction: INPUT
    field: schema
    bound_to:
      literal:
        name:
          type: string
          required: true
        contact_address:
          type: string
          required: true
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: check_actor_fields
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        actor_violations: $.results.check_actor_fields.violations
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: actor_violations
        op: eq
        value: []
  - owner: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    step: refuse_incomplete_submission
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: claim_contact_address
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: claim_contact_address
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: claim_contact_address
    direction: INPUT
    field: target_ref
    bound_to:
      literal: ACTORS
  - owner: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: claim_contact_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    step: claim_contact_address
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_WRITE_ACTOR_V0
    step: assemble_actor_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        contact_address: $.inputs.submission.contact_address
        name: $.inputs.submission.name
        currency_preference: $.inputs.submission.currency_preference
        language: $.inputs.submission.language
        state: UNVERIFIED
  - owner: blockchain::CC_WRITE_ACTOR_V0
    step: assemble_actor_record
    direction: OUTPUT
    field: actor_record
    bound_to: capability_result.record
  - owner: blockchain::CC_WRITE_ACTOR_V0
    step: write_actor_record
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_WRITE_ACTOR_V0
    step: write_actor_record
    direction: INPUT
    field: value
    bound_to: results.assemble_actor_record.actor_record
  - owner: blockchain::CC_WRITE_ACTOR_V0
    step: write_actor_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence
        contact_address: $.inputs.contact_address
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
        occurred_at: $.results.read_now.timestamp
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
  - owner: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence
        contact_address: $.inputs.contact_address
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
        name: $.inputs.name
        currency_preference: $.inputs.currency_preference
        language: $.inputs.language
        occurred_at: $.results.read_now.timestamp
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
  - owner: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: read_actor_record
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: read_actor_record
    direction: OUTPUT
    field: actor_record
    bound_to: capability_result.value
  - owner: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    step: read_actor_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: compare_verifying_authority_to_actor
    direction: INPUT
    field: left
    bound_to: inputs.verifying_authority
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: compare_verifying_authority_to_actor
    direction: INPUT
    field: right
    bound_to: inputs.contact_address
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: compare_verifying_authority_to_actor
    direction: OUTPUT
    field: is_self
    bound_to: capability_result.is_equal
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: refuse_self_decision
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        is_self: $.results.compare_verifying_authority_to_actor.is_self
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: refuse_self_decision
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: is_self
        op: eq
        value: false
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: refuse_self_decision
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: read_outcome_admitted
    direction: INPUT
    field: value
    bound_to: inputs.to_state
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: read_outcome_admitted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: set_record_state
    direction: INPUT
    field: filter
    bound_to:
      literal:
        contact_address: $.inputs.contact_address
        state: UNVERIFIED
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: set_record_state
    direction: INPUT
    field: updates
    bound_to:
      literal:
        state: $.inputs.to_state
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: set_record_state
    direction: OUTPUT
    field: matched_keys
    bound_to: capability_result.matched_keys
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: set_record_state
    direction: OUTPUT
    field: updated_count
    bound_to: capability_result.updated_count
  - owner: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    step: set_record_state
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    step: require_grounds_stated
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        grounds: $.inputs.grounds
  - owner: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    step: require_grounds_stated
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: grounds
        op: not_null
      - field: grounds
        op: neq
        value: ''
  - owner: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    step: require_grounds_stated
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_LIST_ACTORS_V0
    step: select_actor_records
    direction: OUTPUT
    field: records
    bound_to: capability_result.records
  - owner: blockchain::CC_LIST_ACTORS_V0
    step: select_actor_records
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_LIST_ACTORS_V0
    step: select_matching_actors
    direction: INPUT
    field: source
    bound_to: results.select_actor_records.records
  - owner: blockchain::CC_LIST_ACTORS_V0
    step: select_matching_actors
    direction: INPUT
    field: filter
    bound_to:
      literal:
        state: $.inputs.state
  - owner: blockchain::CC_LIST_ACTORS_V0
    step: select_matching_actors
    direction: OUTPUT
    field: matching_actors
    bound_to: capability_result.extracted
  - owner: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    step: require_actor_accepted
    direction: INPUT
    field: value
    bound_to: inputs.state
  - owner: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    step: require_actor_accepted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - ACCEPTED
  - owner: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    step: require_actor_accepted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    step: derive_address
    direction: INPUT
    field: key_material
    bound_to: inputs.key_material
  - owner: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    step: derive_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: resolve_identity
    direction: INPUT
    field: key_or_address
    bound_to: inputs.address
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: resolve_identity
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: resolve_identity
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: require_unheld
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        held: $.results.resolve_identity.result_status
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: require_unheld
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: held
        op: eq
        value: NOT_FOUND
  - owner: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    step: require_unheld
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: form_wallet_id
    direction: INPUT
    field: data
    bound_to: inputs.holder
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: form_wallet_id
    direction: INPUT
    field: prefix
    bound_to:
      literal: wal
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: form_wallet_id
    direction: OUTPUT
    field: wallet_id
    bound_to: capability_result.id
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_id
    direction: INPUT
    field: key
    bound_to: results.form_wallet_id.wallet_id
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_id
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_id
    direction: INPUT
    field: target_ref
    bound_to:
      literal: WALLETS
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_id
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    step: claim_id
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: key
    bound_to: inputs.address
  - owner: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_cs
    bound_to:
      literal: capability_side_effects::CS_MUTABLE_JSON_V0
  - owner: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_ref
    bound_to:
      literal: WALLETS
  - owner: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_WRITE_WALLET_V0
    step: assemble_wallet_record
    direction: INPUT
    field: fields
    bound_to:
      literal:
        holder: $.inputs.holder
        balance: 0
        denomination: BACHI
        classification: DEFAULT
        state: ACTIVE
  - owner: blockchain::CC_WRITE_WALLET_V0
    step: assemble_wallet_record
    direction: OUTPUT
    field: wallet_record
    bound_to: capability_result.record
  - owner: blockchain::CC_WRITE_WALLET_V0
    step: write_wallet_record
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
  - owner: blockchain::CC_WRITE_WALLET_V0
    step: write_wallet_record
    direction: INPUT
    field: value
    bound_to: results.assemble_wallet_record.wallet_record
  - owner: blockchain::CC_WRITE_WALLET_V0
    step: write_wallet_record
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence
        holder: $.inputs.holder
  - owner: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.wallet_id
  - owner: blockchain::CC_RECORD_WALLET_MOMENT_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    direction: INPUT
    field: submission
    bound_to: payload.actor_record
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.actor_record.contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_WRITE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.actor_record.contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_WRITE_ACTOR_V0
    direction: INPUT
    field: submission
    bound_to: payload.actor_record
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: ACTOR_REGISTERED_UNVERIFIED
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.actor_record.contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.actor_record.verifying_authority
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: grounds
    bound_to: payload.actor_record.grounds
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: ACTOR_REGISTERED_UNVERIFIED
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.actor_record.contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.actor_record.verifying_authority
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: grounds
    bound_to: payload.actor_record.grounds
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: name
    bound_to: payload.actor_record.name
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: currency_preference
    bound_to: payload.actor_record.currency_preference
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: language
    bound_to: payload.actor_record.language
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_RESOLVE_ACTOR_IDENTITY_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: to_state
    bound_to:
      literal: ACCEPTED
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: ACTOR_ACCEPTED
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_ACCEPT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_RESOLVE_ACTOR_IDENTITY_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: to_state
    bound_to:
      literal: REJECTED
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: ACTOR_REJECTED
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_REJECT_ACTOR_V1
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_LIST_ACTORS_V0
    step: CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: LIST_ACTORS
  - owner: blockchain::WF_LIST_ACTORS_V0
    step: CC_LIST_ACTORS_V0
    direction: INPUT
    field: state
    bound_to: payload.state
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_RESOLVE_ACTOR_IDENTITY_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_REQUIRE_ACCEPTED_ACTOR_V0
    direction: INPUT
    field: state
    bound_to: results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.state
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_DERIVE_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    bound_to: payload.key_material
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    direction: INPUT
    field: address
    bound_to: results.CC_DERIVE_WALLET_ADDRESS_V0.address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_CLAIM_WALLET_IDENTITY_V1
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_CLAIM_WALLET_ADDRESS_V0
    direction: INPUT
    field: address
    bound_to: results.CC_DERIVE_WALLET_ADDRESS_V0.address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_WRITE_WALLET_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_CLAIM_WALLET_IDENTITY_V1.wallet_id
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_WRITE_WALLET_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: occurrence
    bound_to:
      literal: WALLET_CREATED
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_IDENTITY_V0.actor_record.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V1
    step: CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_CLAIM_WALLET_IDENTITY_V1.wallet_id
  interface_fields:
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: name
    type: string
    required: 'YES'
    default: null
    meaning: name
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: currency_preference
    type: string
    required: 'NO'
    default: BACHI
    meaning: currency preference
  - artifact: blockchain::AC_PARTICIPANT_V0
    direction: ATTRIBUTE
    field: language
    type: string
    required: 'NO'
    default: en
    meaning: language
  - artifact: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_WRITE_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_WRITE_ACTOR_V0
    direction: INPUT
    field: submission
    type: object
    required: 'YES'
    default: null
    meaning: submission
  - artifact: blockchain::CC_WRITE_ACTOR_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: occurrence
    type: string
    required: 'YES'
    default: null
    meaning: occurrence
  - artifact: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'NO'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'NO'
    default: null
    meaning: verifying authority
  - artifact: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_RECORD_IDENTITY_MOMENT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: occurrence
    type: string
    required: 'YES'
    default: null
    meaning: occurrence
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'NO'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'NO'
    default: null
    meaning: verifying authority
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: name
    type: string
    required: 'NO'
    default: null
    meaning: name
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: currency_preference
    type: string
    required: 'NO'
    default: null
    meaning: currency preference
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: INPUT
    field: language
    type: string
    required: 'NO'
    default: null
    meaning: language
  - artifact: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    direction: OUTPUT
    field: actor_record
    type: object
    required: 'YES'
    default: null
    meaning: actor record
  - artifact: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: to_state
    type: string
    required: 'YES'
    default: null
    meaning: to state
  - artifact: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0
    direction: OUTPUT
    field: updated_count
    type: integer
    required: 'YES'
    default: null
    meaning: updated count
  - artifact: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_REQUIRE_GROUNDS_TO_REJECT_ACTOR_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: blockchain::CC_LIST_ACTORS_V0
    direction: INPUT
    field: state
    type: string
    required: 'YES'
    default: null
    meaning: state
  - artifact: blockchain::CC_LIST_ACTORS_V0
    direction: OUTPUT
    field: matching_actors
    type: array
    required: 'YES'
    default: null
    meaning: matching actors
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    direction: INPUT
    field: state
    type: string
    required: 'YES'
    default: null
    meaning: state
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_ACTOR_V0
    direction: OUTPUT
    field: is_member
    type: boolean
    required: 'YES'
    default: null
    meaning: is member
  - artifact: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: null
    meaning: key material
  - artifact: blockchain::CC_DERIVE_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    direction: INPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    direction: INPUT
    field: holder
    type: string
    required: 'YES'
    default: null
    meaning: holder
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    direction: OUTPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    direction: INPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_CLAIM_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_WRITE_WALLET_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::CC_WRITE_WALLET_V0
    direction: INPUT
    field: holder
    type: string
    required: 'YES'
    default: null
    meaning: holder
  - artifact: blockchain::CC_WRITE_WALLET_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: occurrence
    type: string
    required: 'YES'
    default: null
    meaning: occurrence
  - artifact: blockchain::CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: holder
    type: string
    required: 'NO'
    default: null
    meaning: holder
  - artifact: blockchain::CC_RECORD_WALLET_MOMENT_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::CC_RECORD_WALLET_MOMENT_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: null
    meaning: actor record
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::IN_ACTOR_REJECTION_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: null
    meaning: grounds
  - artifact: blockchain::IN_LIST_ACTORS_V0
    direction: INPUT
    field: state
    type: string
    required: 'YES'
    default: null
    meaning: state
  - artifact: blockchain::IN_WALLET_CREATION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::IN_WALLET_CREATION_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: null
    meaning: key material
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: null
    meaning: occurred at
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    direction: OUTPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    direction: OUTPUT
    field: grounds
    type: string
    required: 'YES'
    default: null
    meaning: grounds
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: null
    meaning: occurred at
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: OUTPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: OUTPUT
    field: grounds
    type: string
    required: 'YES'
    default: null
    meaning: grounds
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: null
    meaning: occurred at
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: OUTPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: OUTPUT
    field: holder
    type: string
    required: 'YES'
    default: null
    meaning: holder
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: null
    meaning: occurred at
  - artifact: blockchain::EV_WALLET_CREATED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: name
    type: string
    required: 'YES'
    default: null
    meaning: name
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: null
    meaning: grounds
  - artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: null
    meaning: key material
  - artifact: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  implementation_bindings:
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    callable: execute
    operation: DERIVE_WALLET_ADDRESS
    kind: atom
    purity: ct_pure
    refusal: never
  vocabulary_extensions:
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    names_kind: null
    value: DEFAULT
    meaning: DEFAULT
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    names_kind: null
    value: PRIVATE
    meaning: PRIVATE
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    names_kind: null
    value: BUSINESS
    meaning: BUSINESS
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    names_kind: null
    value: SAVINGS
    meaning: SAVINGS
  runtime_policies:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
  - rb_code: blockchain::RB_WALLET_BINDINGS_V1
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: blockchain::STRUCTURE_WALLET_STORAGE_V1
  - rb_code: blockchain::RB_WALLET_BINDINGS_V1
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: blockchain::STRUCTURE_WALLET_STORAGE_V1
  - rb_code: blockchain::RB_WALLET_BINDINGS_V1
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: blockchain::STRUCTURE_WALLET_STORAGE_V1
  artifact_properties:
  - artifact: blockchain::AC_PARTICIPANT_V0
    property: type
    value: human
  - artifact: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: blockchain::STRUCTURE_WALLET_STORAGE_V1
    property: layer
    value: DOMAINS
  - artifact: blockchain::WF_REGISTER_ACTOR_V2
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_REGISTER_ACTOR_V2
    property: emit.EXIT_COMPLETED
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    property: emit.EXIT_COMPLETED
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V1
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    property: emit.EXIT_COMPLETED
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
  - artifact: blockchain::WF_LIST_ACTORS_V0
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_CREATE_WALLET_V1
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_CREATE_WALLET_V1
    property: emit.EXIT_COMPLETED
    value:
    - blockchain::EV_WALLET_CREATED_V0
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    property: evidence_policy
    value: reference_only
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    property: evidence_policy
    value: reference_only
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.SUCCESS
    value: SUCCESS
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.VIOLATION
    value: VIOLATION
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: result_class.NOT_FOUND
    value: NOT_FOUND
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: default_result_class
    value: EXECUTION_FAILURE
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    property: evidence_policy
    value: reference_only
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V1
    property: supersedes
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::WF_ACCEPT_ACTOR_V0
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::WF_REJECT_ACTOR_V0
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    property: supersedes
    value:
    - blockchain::CC_CLAIM_WALLET_IDENTITY_V0
  - artifact: blockchain::STRUCTURE_WALLET_STORAGE_V1
    property: supersedes
    value:
    - blockchain::STRUCTURE_WALLET_STORAGE_V0
  - artifact: blockchain::RB_WALLET_BINDINGS_V1
    property: supersedes
    value:
    - blockchain::RB_WALLET_BINDINGS_V0
  - artifact: blockchain::VOCAB_WALLET_CLASSIFICATION_V1
    property: supersedes
    value:
    - blockchain::VOCAB_WALLET_CLASSIFICATION_V0
  - artifact: blockchain::WF_CREATE_WALLET_V1
    property: supersedes
    value:
    - blockchain::WF_CREATE_WALLET_V0
  - artifact: blockchain::WF_REGISTER_ACTOR_V2
    property: supersedes
    value:
    - blockchain::WF_REGISTER_ACTOR_V1
  structure_stores:
  - store_name: CONTACT_ADDRESS_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/identity/contact_address_registry.jsonl
    used_by: blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0, blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: ACTORS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/identity/actors.json
    used_by: blockchain::CC_LIST_ACTORS_V0, blockchain::CC_MOVE_ACTOR_FROM_UNVERIFIED_V0, blockchain::CC_RESOLVE_ACTOR_IDENTITY_V0,
      blockchain::CC_WRITE_ACTOR_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: ACTOR_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/identity/actor_occurrences.jsonl
    used_by: blockchain::CC_RECORD_IDENTITY_MOMENT_V0, blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: WALLET_ADDRESS_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/wallet/wallet_address_registry.jsonl
    used_by: blockchain::CC_CLAIM_WALLET_ADDRESS_V0, blockchain::CC_REQUIRE_WALLET_ADDRESS_FREE_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  - store_name: WALLET_IDENTITIES
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/wallet/wallet_identity_registry.jsonl
    used_by: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  - store_name: WALLETS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/wallet/wallets.json
    used_by: blockchain::CC_WRITE_WALLET_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  - store_name: WALLET_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/wallet/wallet_occurrences.jsonl
    used_by: blockchain::CC_RECORD_WALLET_MOMENT_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V1
  transport_bindings:
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.name
    bound_to: ${input.name}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.currency_preference
    bound_to: BACHI
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.language
    bound_to: en
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: blockchain.register_actor
    handler_kind: null
    handler_target: null
    field: contact_address
    bound_to: surface.contact_address
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurrence
    bound_to: surface.record.occurrence
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurred_at
    bound_to: surface.record.occurred_at
  - artifact: blockchain::TE_REGISTER_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: sequence_number
    bound_to: surface.sequence_number
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V1
    field: contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V1
    field: verifying_authority
    bound_to: ${input.verifying_authority}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V1
    field: grounds
    bound_to: ${input.grounds}
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.accept_actor
    handler_kind: null
    handler_target: null
    field: contact_address
    bound_to: surface.contact_address
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurrence
    bound_to: surface.record.occurrence
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: verifying_authority
    bound_to: surface.record.verifying_authority
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: grounds
    bound_to: surface.record.grounds
    required: false
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurred_at
    bound_to: surface.record.occurred_at
  - artifact: blockchain::TE_ACCEPT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: sequence_number
    bound_to: surface.sequence_number
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V1
    field: contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V1
    field: verifying_authority
    bound_to: ${input.verifying_authority}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V1
    field: grounds
    bound_to: ${input.grounds}
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: blockchain.reject_actor
    handler_kind: null
    handler_target: null
    field: contact_address
    bound_to: surface.contact_address
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurrence
    bound_to: surface.record.occurrence
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: verifying_authority
    bound_to: surface.record.verifying_authority
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: grounds
    bound_to: surface.record.grounds
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: occurred_at
    bound_to: surface.record.occurred_at
  - artifact: blockchain::TE_REJECT_ACTOR_V0
    direction: EGRESS
    operation: null
    handler_kind: null
    handler_target: null
    field: sequence_number
    bound_to: surface.sequence_number
  declared_reach:
  - act: blockchain::WF_CREATE_WALLET_V1
    consults:
    - blockchain::RB_IDENTITY_BINDINGS_V0
  molecule_steps: []
  molecule_step_bindings: []
  test_cases:
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: derives_the_address_of_the_generator_key
    expected_outcome: SUCCESS
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: prefix_and_tag_derive_the_same_address
    expected_outcome: SUCCESS
  test_case_values:
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: derives_the_address_of_the_generator_key
    role: INPUT
    field: key_material
    value: 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: derives_the_address_of_the_generator_key
    role: EXPECTED
    field: address
    value: '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: prefix_and_tag_derive_the_same_address
    role: INPUT
    field: key_material
    value: '0x0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8'
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    case: prefix_and_tag_derive_the_same_address
    role: EXPECTED
    field: address
    value: '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
  generation_provenance: []
  artifact_summary:
  - action: NEW
    subdomain: identity
    count: '2'
    artifacts: blockchain::CC_RECORD_IDENTITY_REPEATED_MOMENT_V0, blockchain::WF_REGISTER_ACTOR_V2
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `blockchain`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`blockchain` is a dossier designed against the composition.
