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
  existing_inventory: []
  new_artifacts:
  - family: AC
    code: blockchain::AC_PARTICIPANT_V0
    summary: The ordinary participant who registers themselves and is decided about
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    summary: Appends one occurrence to the trail
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    summary: Claims a contact address so that two registrations of one person do not produce two actors
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    summary: Refuses a decision about a person not unverified, a decision other than an acceptance or
      a rejection, or an authority deciding about themselves, and records the decision it checked
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_REGISTER_ACTOR_V0
    summary: Writes the actor unverified after its address is claimed
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    summary: Refuses a rejection stating no grounds, before anything is recorded
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_RESOLVE_ACTOR_V0
    summary: Answers which actor a contact address denotes, and reports when none does
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_VALIDATE_REGISTRATION_V0
    summary: Refuses a registration lacking the person's name or their address
    owner_subdomain: identity
    status: NEW
  - family: EV
    code: blockchain::EV_ACTOR_ACCEPTED_V0
    summary: The moment an authority records a decision to trust an actor
    owner_subdomain: identity
    status: NEW
  - family: EV
    code: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    summary: The moment a person is admitted and trusted with nothing
    owner_subdomain: identity
    status: NEW
  - family: EV
    code: blockchain::EV_ACTOR_REJECTED_V0
    summary: The moment an authority records a decision not to trust an actor
    owner_subdomain: identity
    status: NEW
  - family: IN
    code: blockchain::IN_ACTOR_ACCEPTANCE_V0
    summary: Admits a request to accept a person, with the grounds the authority chooses to state, and
      refuses one that names nobody
    owner_subdomain: identity
    status: NEW
  - family: IN
    code: blockchain::IN_ACTOR_REGISTERED_V0
    summary: A request to admit a person as an actor
    owner_subdomain: identity
    status: NEW
  - family: IN
    code: blockchain::IN_ACTOR_REJECTION_V0
    summary: Admits a request to reject a person, and refuses one that states no grounds
    owner_subdomain: identity
    status: NEW
  - family: STRUCTURE
    code: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    summary: Declares the three stores identity owns and the paths they occupy
    owner_subdomain: identity
    status: NEW
  - family: RB
    code: blockchain::RB_IDENTITY_BINDINGS_V0
    summary: The bindings identity's workflows resolve their capabilities and stores through
    owner_subdomain: identity
    status: NEW
  - family: TI
    code: blockchain::TI_ACCEPT_ACTOR_V0
    summary: Admits a request to accept a registered actor, and sends the act only what the caller supplies
    owner_subdomain: identity
    status: NEW
  - family: TI
    code: blockchain::TI_REGISTER_ACTOR_V0
    summary: Admits a request to register an actor, and sends the act only what the caller supplies and
      the person's preferences
    owner_subdomain: identity
    status: NEW
  - family: TI
    code: blockchain::TI_REJECT_ACTOR_V0
    summary: Admits a request to reject a registered actor, and sends the act only what the caller supplies
    owner_subdomain: identity
    status: NEW
  - family: TE
    code: blockchain::TE_ACCEPT_ACTOR_V0
    summary: Classifies the endings of accepting an actor, including the actor that does not exist, and
      projects what was recorded.
    owner_subdomain: identity
    status: NEW
  - family: TE
    code: blockchain::TE_REGISTER_ACTOR_V0
    summary: Classifies the endings of registering an actor and projects the contact address, the occurrence,
      its time and its position.
    owner_subdomain: identity
    status: NEW
  - family: TE
    code: blockchain::TE_REJECT_ACTOR_V0
    summary: Classifies the endings of rejecting an actor, including the actor that does not exist, and
      projects what was recorded.
    owner_subdomain: identity
    status: NEW
  - family: WF
    code: blockchain::WF_ACCEPT_ACTOR_V0
    summary: The governed sequence that records an acceptance, records that moment as its own, and announces
      it
    owner_subdomain: identity
    status: NEW
  - family: WF
    code: blockchain::WF_REGISTER_ACTOR_V0
    summary: The governed sequence that admits a person as an unverified actor, records that moment as
      its own, and announces it
    owner_subdomain: identity
    status: NEW
  - family: WF
    code: blockchain::WF_REJECT_ACTOR_V0
    summary: The governed sequence that records a rejection, with grounds required, records that moment
      as its own, and announces it
    owner_subdomain: identity
    status: NEW
  - family: CC
    code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    summary: Records the moment on the wallet's trail
    owner_subdomain: wallet
    status: NEW
  - family: CC
    code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    summary: Claims the identity, and refuses when the person already holds a wallet
    owner_subdomain: wallet
    status: NEW
  - family: CC
    code: blockchain::CC_CREATE_WALLET_RECORD_V0
    summary: Records the wallet with a balance of zero, its denomination and its classification
    owner_subdomain: wallet
    status: NEW
  - family: CC
    code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    summary: Derives the wallet's identity from the person who holds it
    owner_subdomain: wallet
    status: NEW
  - family: CC
    code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    summary: Establishes the address from key material supplied with the request
    owner_subdomain: wallet
    status: NEW
  - family: CC
    code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or
      recorded
    owner_subdomain: wallet
    status: NEW
  - family: CT
    code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    summary: Derives an address from supplied key material; the same material always yields the same address
    owner_subdomain: wallet
    status: NEW
  - family: EV
    code: blockchain::EV_WALLET_CREATED_V0
    summary: Announces that a wallet was created, for whom, and when
    owner_subdomain: wallet
    status: NEW
  - family: IN
    code: blockchain::IN_WALLET_CREATION_V0
    summary: Admits a request naming the person a wallet is for and the key it is made from, and refuses
      one that names nobody
    owner_subdomain: wallet
    status: NEW
  - family: STRUCTURE
    code: blockchain::STRUCTURE_WALLET_STORAGE_V0
    summary: Declares the three stores wallet owns
    owner_subdomain: wallet
    status: NEW
  - family: RB
    code: blockchain::RB_WALLET_BINDINGS_V0
    summary: Binds the wallet workflow to the capabilities and stores it uses
    owner_subdomain: wallet
    status: NEW
  - family: VOCAB
    code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    summary: ''
    owner_subdomain: wallet
    status: NEW
  - family: WF
    code: blockchain::WF_CREATE_WALLET_V0
    summary: The governed sequence that gives an accepted person a wallet holding nothing, and records
      that it did
    owner_subdomain: wallet
    status: NEW
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    binds_wf: blockchain::WF_CREATE_WALLET_V0
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
  execution_topology:
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: IN_ACTOR_ACCEPTANCE_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_ACCEPT_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: IN_ACTOR_REGISTERED_V0
    node_type: IN
    routing:
      ACK: CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: CC_VALIDATE_REGISTRATION_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: CC_CLAIM_CONTACT_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: CC_REGISTER_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REGISTER_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: IN_ACTOR_REJECTION_V0
    node_type: IN
    routing:
      ACK: CC_REQUIRE_REJECTION_GROUNDS_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: CC_REQUIRE_REJECTION_GROUNDS_V0
    node_type: CC
    routing:
      SUCCESS: CC_RESOLVE_ACTOR_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: CC_RECORD_VERIFICATION_DECISION_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: CC_APPEND_ACTOR_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_REJECT_ACTOR_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: IN_WALLET_CREATION_V0
    node_type: IN
    routing:
      ACK: CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_RESOLVE_ACTOR_V0
    node_type: CC
    routing:
      SUCCESS: CC_REQUIRE_ACCEPTED_HOLDER_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_REQUIRE_ACCEPTED_HOLDER_V0
    node_type: CC
    routing:
      SUCCESS: CC_DETERMINE_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_DETERMINE_WALLET_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_CLAIM_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_CLAIM_WALLET_IDENTITY_V0
    node_type: CC
    routing:
      SUCCESS: CC_ESTABLISH_WALLET_ADDRESS_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_ESTABLISH_WALLET_ADDRESS_V0
    node_type: CC
    routing:
      SUCCESS: CC_CREATE_WALLET_RECORD_V0
      VIOLATION: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_CREATE_WALLET_RECORD_V0
    node_type: CC
    routing:
      SUCCESS: CC_APPEND_WALLET_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: CC_APPEND_WALLET_OCCURRENCE_V0
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: EXIT_SUCCESS
    node_type: EXIT
    routing: null
  - workflow: blockchain::WF_CREATE_WALLET_V0
    node: EXIT_REJECTED
    node_type: EXIT
    routing: null
  cc_composition:
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
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
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
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
  - cc_code: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: ACTOR_OCCURRENCES
    consumes:
    - record
    - stream_id
    - actor_id
    produces:
    - sequence_number
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        record: record
        stream_id: stream_id
        actor_id: actor_id
      out:
        sequence_number: sequence_number
  - cc_code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: '1'
    step_name: extract_address
    capability: capability_transforms::CT_PURE_EXTRACT_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - from
    - path
    - type
    produces:
    - result
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        from: from
        path: path
        type: type
      out:
        result: result
  - cc_code: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: '2'
    step_name: claim_address
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '1'
    step_name: read_state_admits_decision
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '2'
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '3'
    step_name: compare_authority_to_person
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '4'
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '5'
    step_name: assemble_decided_actor
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
  - cc_code: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: '6'
    step_name: write_decided_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: UPDATE
    store: ACTORS
    consumes:
    - key
    - updates
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key: key
        updates: updates
      out:
        result_status: result_status
  - cc_code: blockchain::CC_REGISTER_ACTOR_V0
    step: '1'
    step_name: assemble_actor
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
  - cc_code: blockchain::CC_REGISTER_ACTOR_V0
    step: '2'
    step_name: write_actor
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
      SUCCESS: continue
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
  - cc_code: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
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
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    step: '1'
    step_name: resolve_address
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: RESOLVE
    store: CONTACT_ADDRESS_REGISTRY
    consumes:
    - key_or_address
    produces:
    - target_ref
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
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    step: '2'
    step_name: read_actor
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    kind: CS
    operation: READ
    store: ACTORS
    consumes:
    - key
    produces:
    - value
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
        value: value
  - cc_code: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: '1'
    step_name: read_registration
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
  - cc_code: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: '2'
    step_name: refuse_incomplete_registration
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: '1'
    step_name: read_occurred_at
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
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
  - cc_code: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: '3'
    step_name: append_occurrence
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    kind: CS
    operation: APPEND
    store: WALLET_OCCURRENCES
    consumes:
    - stream_id
    - record
    produces:
    - result_status
    routing:
      SUCCESS: continue
      VIOLATION: exit
      BACKEND_ERROR: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        stream_id: stream_id
        record: record
      out:
        result_status: result_status
  - cc_code: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: '1'
    step_name: claim_wallet_identity
    capability: capability_side_effects::CS_REGISTRY_V0
    kind: CS
    operation: REGISTER
    store: WALLET_IDENTITIES
    consumes:
    - key
    produces:
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
      out:
        result_status: result_status
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '1'
    step_name: read_created_at
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
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '2'
    step_name: assemble_wallet
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
  - cc_code: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: '3'
    step_name: write_wallet
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
      SUCCESS: continue
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
  - cc_code: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: '1'
    step_name: derive_wallet_identity
    capability: capability_transforms::CT_PURE_GENERATE_ID_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - data
    - prefix
    produces:
    - id
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
        id: id
  - cc_code: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: '1'
    step_name: derive_wallet_address
    capability: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - key_material
    produces:
    - address
    routing:
      SUCCESS: continue
      VIOLATION: exit
    interpreted_by: null
    semantic_status: SUCCESS
    interface:
      in:
        key_material: key_material
      out:
        address: address
  - cc_code: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: '1'
    step_name: require_holder_accepted
    capability: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    kind: CT
    operation: null
    store: null
    consumes:
    - value
    - allowed_set
    produces:
    - is_accepted
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
        is_accepted: is_accepted
  step_bindings:
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: read_now
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to:
      literal:
        occurrence: $.inputs.occurrence_fields.occurrence
        contact_address: $.inputs.contact_address
        verifying_authority: $.inputs.occurrence_fields.verifying_authority
        grounds: $.inputs.occurrence_fields.grounds
        occurred_at: $.results.read_now.timestamp
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.stream_id
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: actor_id
    bound_to: inputs.contact_address
  - owner: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    step: append_occurrence
    direction: OUTPUT
    field: sequence_number
    bound_to: capability_result.sequence_number
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: from
    bound_to: inputs.actor_record
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: path
    bound_to: inputs.address_path
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: INPUT
    field: type
    bound_to: inputs.address_type
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: extract_address
    direction: OUTPUT
    field: result
    bound_to: capability_result.result
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: key
    bound_to: results.extract_address.result
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_cs
    bound_to:
      literal: CS_MUTABLE_JSON_V0
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: INPUT
    field: target_ref
    bound_to:
      literal: ACTORS
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    step: claim_address
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: value
    bound_to: inputs.current_state
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - UNVERIFIED
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_state_admits_decision
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: value
    bound_to: inputs.decision
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: INPUT
    field: allowed_set
    bound_to:
      literal:
      - ACCEPTED
      - REJECTED
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: read_outcome_admitted
    direction: OUTPUT
    field: is_member
    bound_to: capability_result.is_member
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: INPUT
    field: left
    bound_to: inputs.verifying_authority
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: INPUT
    field: right
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: compare_authority_to_person
    direction: OUTPUT
    field: is_self
    bound_to: capability_result.is_equal
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        is_self: $.results.compare_authority_to_person.is_self
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: is_self
        op: eq
        value: false
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: refuse_self_decision
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: INPUT
    field: fields
    bound_to:
      literal:
        contact_address: $.inputs.contact_address
        state: $.inputs.decision
        verifying_authority: $.inputs.verifying_authority
        grounds: $.inputs.grounds
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: assemble_decided_actor
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: INPUT
    field: updates
    bound_to: results.assemble_decided_actor.record
  - owner: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    step: write_decided_actor
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: assemble_actor
    direction: INPUT
    field: fields
    bound_to: inputs.actor_fields
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: assemble_actor
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: INPUT
    field: value
    bound_to: results.assemble_actor.record
  - owner: blockchain::CC_REGISTER_ACTOR_V0
    step: write_actor
    direction: OUTPUT
    field: result_status
    bound_to: result_status
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        grounds: $.inputs.grounds
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
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
  - owner: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    step: require_grounds_stated
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: resolve_address
    direction: INPUT
    field: key_or_address
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: resolve_address
    direction: OUTPUT
    field: target_ref
    bound_to: capability_result.target_ref
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: read_actor
    direction: INPUT
    field: key
    bound_to: inputs.contact_address
  - owner: blockchain::CC_RESOLVE_ACTOR_V0
    step: read_actor
    direction: OUTPUT
    field: value
    bound_to: capability_result.value
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: INPUT
    field: record
    bound_to: inputs.actor_record
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
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
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: read_registration
    direction: OUTPUT
    field: violations
    bound_to: capability_result.violations
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: INPUT
    field: parameters
    bound_to:
      literal:
        violations: $.results.read_registration.violations
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: INPUT
    field: rules
    bound_to:
      literal:
      - field: violations
        op: eq
        value: []
  - owner: blockchain::CC_VALIDATE_REGISTRATION_V0
    step: refuse_incomplete_registration
    direction: OUTPUT
    field: valid
    bound_to: capability_result.valid
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: ACCEPTED
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_ACCEPTED
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
  - owner: blockchain::WF_ACCEPT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to:
      literal: contact_address
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to:
      literal: string
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    bound_to:
      literal:
        name: $.payload.actor_record.name
        contact_address: $.payload.actor_record.contact_address
        state: UNVERIFIED
        currency_preference: $.payload.actor_record.currency_preference
        language: $.payload.actor_record.language
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_REGISTERED_UNVERIFIED
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
  - owner: blockchain::WF_REGISTER_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: REJECTED
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_REJECTED
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
  - owner: blockchain::WF_REJECT_ACTOR_V0
    step: CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: read_occurred_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: assemble_occurrence
    direction: INPUT
    field: fields
    bound_to: inputs.occurrence_fields
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: assemble_occurrence
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: stream_id
    bound_to: inputs.stream_id
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: INPUT
    field: record
    bound_to: results.assemble_occurrence.record
  - owner: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    step: append_occurrence
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: claim_wallet_identity
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
  - owner: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    step: claim_wallet_identity
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: read_created_at
    direction: OUTPUT
    field: timestamp
    bound_to: capability_result.timestamp
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: assemble_wallet
    direction: INPUT
    field: fields
    bound_to: inputs.wallet_fields
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: assemble_wallet
    direction: OUTPUT
    field: record
    bound_to: capability_result.record
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: INPUT
    field: key
    bound_to: inputs.wallet_id
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: INPUT
    field: value
    bound_to: results.assemble_wallet.record
  - owner: blockchain::CC_CREATE_WALLET_RECORD_V0
    step: write_wallet
    direction: OUTPUT
    field: result_status
    bound_to: capability_result.result_status
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: INPUT
    field: data
    bound_to: inputs.holder
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: INPUT
    field: prefix
    bound_to: inputs.wallet_id_prefix
  - owner: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    step: derive_wallet_identity
    direction: OUTPUT
    field: id
    bound_to: capability_result.id
  - owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: derive_wallet_address
    direction: INPUT
    field: key_material
    bound_to: inputs.key_material
  - owner: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    step: derive_wallet_address
    direction: OUTPUT
    field: address
    bound_to: capability_result.address
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: INPUT
    field: value
    bound_to: inputs.holder_state
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: INPUT
    field: allowed_set
    bound_to: inputs.states_admitting_a_wallet
  - owner: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    step: require_holder_accepted
    direction: OUTPUT
    field: is_accepted
    bound_to: capability_result.is_member
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    bound_to:
      literal:
      - ACCEPTED
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.contact_address
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    bound_to:
      literal: wal
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    bound_to: payload.key_material
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    bound_to:
      literal:
        holder: $.results.CC_RESOLVE_ACTOR_V0.value.contact_address
        balance: 0
        denomination: BACHI
        classification: DEFAULT
        state: ACTIVE
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
  - owner: blockchain::WF_CREATE_WALLET_V0
    step: CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: WALLET_CREATED
        holder: $.results.CC_RESOLVE_ACTOR_V0.value.contact_address
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
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    type: object
    required: 'YES'
    default: null
    meaning: occurrence fields
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    type: string
    required: 'YES'
    default: null
    meaning: stream id
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: OUTPUT
    field: sequence_number
    type: integer
    required: 'YES'
    default: null
    meaning: sequence number
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: null
    meaning: actor record
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    type: string
    required: 'YES'
    default: null
    meaning: address path
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    type: string
    required: 'YES'
    default: null
    meaning: address type
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: result
    type: string
    required: 'YES'
    default: null
    meaning: result
  - artifact: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    type: string
    required: 'YES'
    default: null
    meaning: current state
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    type: string
    required: 'YES'
    default: null
    meaning: decision
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    type: object
    required: 'YES'
    default: null
    meaning: actor fields
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_REGISTER_ACTOR_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: OUTPUT
    field: valid
    type: boolean
    required: 'YES'
    default: null
    meaning: valid
  - artifact: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::CC_RESOLVE_ACTOR_V0
    direction: OUTPUT
    field: value
    type: object
    required: 'YES'
    default: null
    meaning: value
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: null
    meaning: actor record
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: OUTPUT
    field: violations
    type: array
    required: 'YES'
    default: null
    meaning: violations
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: OUTPUT
    field: contact_address
    type: string
    required: 'YES'
    default: null
    meaning: contact address
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: OUTPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: null
    meaning: verifying authority
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: OUTPUT
    field: grounds
    type: string
    required: 'NO'
    default: null
    meaning: grounds
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: OUTPUT
    field: occurred_at
    type: string
    required: 'YES'
    default: null
    meaning: occurred at
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    direction: OUTPUT
    field: timestamp
    type: string
    required: 'YES'
    default: null
    meaning: When the moment occurred
    format: date-time
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
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    direction: INPUT
    field: actor_record
    type: object
    required: 'YES'
    default: null
    meaning: actor record
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
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    type: string
    required: 'YES'
    default: null
    meaning: stream id
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    type: object
    required: 'YES'
    default: null
    meaning: occurrence fields
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    type: string
    required: 'YES'
    default: null
    meaning: wallet id
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    type: object
    required: 'YES'
    default: null
    meaning: wallet fields
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: OUTPUT
    field: result_status
    type: string
    required: 'YES'
    default: null
    meaning: result status
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    type: string
    required: 'YES'
    default: null
    meaning: holder
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    type: string
    required: 'YES'
    default: null
    meaning: wallet id prefix
  - artifact: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: OUTPUT
    field: id
    type: string
    required: 'YES'
    default: null
    meaning: id
  - artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: null
    meaning: key material
  - artifact: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: OUTPUT
    field: address
    type: string
    required: 'YES'
    default: null
    meaning: address
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    type: string
    required: 'YES'
    default: null
    meaning: holder state
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    type: array
    required: 'YES'
    default: null
    meaning: states admitting a wallet
  - artifact: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: OUTPUT
    field: is_accepted
    type: boolean
    required: 'YES'
    default: null
    meaning: is accepted
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
  implementation_bindings:
  - ct_code: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
    callable: execute
    operation: DERIVE_WALLET_ADDRESS
    kind: atom
    purity: ct_pure
    refusal: never
  vocabulary_extensions:
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: DEFAULT
    meaning: DEFAULT
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: PRIVATE
    meaning: PRIVATE
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: BUSINESS
    meaning: BUSINESS
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: SAVINGS
    meaning: SAVINGS
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: INVESTMENT
    meaning: INVESTMENT
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: MINT
    meaning: MINT
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: BURN
    meaning: BURN
  - vocabulary_code: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    extends: null
    group: result_status
    casing: UPPER_SNAKE
    value: POOL
    meaning: POOL
  runtime_policies:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: structure
    value: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: precision
    value: seconds
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_MUTABLE_JSON_V0
    key: store
    value: WALLETS
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_APPENDONLY_JSONL_V0
    key: store
    value: WALLET_OCCURRENCES
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_REGISTRY_V0
    key: store
    value: WALLET_IDENTITIES
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    capability: capability_side_effects::CS_CLOCK_V0
    key: policy
    value: utc
  artifact_properties:
  - artifact: blockchain::AC_PARTICIPANT_V0
    property: type
    value: ENDUSER
  - artifact: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    property: layer
    value: DOMAINS
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
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
  - artifact: blockchain::STRUCTURE_WALLET_STORAGE_V0
    property: layer
    value: DOMAINS
  - artifact: blockchain::WF_CREATE_WALLET_V0
    property: actor_context
    value: blockchain::AC_PARTICIPANT_V0
  - artifact: blockchain::WF_CREATE_WALLET_V0
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_WALLET_CREATED_V0
  structure_stores:
  - store_name: ACTORS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/identity/actors.json
    used_by: blockchain::CC_RECORD_VERIFICATION_DECISION_V0, blockchain::CC_REGISTER_ACTOR_V0, blockchain::CC_RESOLVE_ACTOR_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: CONTACT_ADDRESS_REGISTRY
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/identity/contact_address_registry.jsonl
    used_by: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_RESOLVE_ACTOR_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: ACTOR_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/identity/actor_occurrences.jsonl
    used_by: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - store_name: WALLETS
    storage_type: CS_MUTABLE_JSON_V0
    proposed_path: blockchain/wallet/wallets.json
    used_by: blockchain::CC_CREATE_WALLET_RECORD_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
  - store_name: WALLET_OCCURRENCES
    storage_type: CS_APPENDONLY_JSONL_V0
    proposed_path: blockchain/wallet/wallet_occurrences.jsonl
    used_by: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
  - store_name: WALLET_IDENTITIES
    storage_type: CS_REGISTRY_V0
    proposed_path: blockchain/wallet/wallet_identity_registry.jsonl
    used_by: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
  transport_bindings:
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V0
    field: grounds
    bound_to: ${input.grounds}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.name
    bound_to: ${input.name}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.currency_preference
    bound_to: BACHI
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V0
    field: actor_record.language
    bound_to: en
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: contact_address
    bound_to: ${input.contact_address}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
    field: verifying_authority
    bound_to: ${input.verifying_authority}
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V0
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
  - act: blockchain::WF_CREATE_WALLET_V0
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
    count: '25'
    artifacts: blockchain::AC_PARTICIPANT_V0, blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0, blockchain::CC_CLAIM_CONTACT_ADDRESS_V0,
      blockchain::CC_RECORD_VERIFICATION_DECISION_V0, blockchain::CC_REGISTER_ACTOR_V0, blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0,
      blockchain::CC_RESOLVE_ACTOR_V0, blockchain::CC_VALIDATE_REGISTRATION_V0, blockchain::EV_ACTOR_ACCEPTED_V0,
      blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0, blockchain::EV_ACTOR_REJECTED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0,
      blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_REJECTION_V0, blockchain::STRUCTURE_IDENTITY_STORAGE_V0,
      blockchain::RB_IDENTITY_BINDINGS_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REGISTER_ACTOR_V0,
      blockchain::TI_REJECT_ACTOR_V0, blockchain::TE_ACCEPT_ACTOR_V0, blockchain::TE_REGISTER_ACTOR_V0,
      blockchain::TE_REJECT_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REGISTER_ACTOR_V0,
      blockchain::WF_REJECT_ACTOR_V0
  - action: NEW
    subdomain: wallet
    count: '13'
    artifacts: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0,
      blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0, blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0,
      blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0, blockchain::EV_WALLET_CREATED_V0, blockchain::IN_WALLET_CREATION_V0,
      blockchain::STRUCTURE_WALLET_STORAGE_V0, blockchain::RB_WALLET_BINDINGS_V0, blockchain::VOCAB_WALLET_CLASSIFICATION_V0,
      blockchain::WF_CREATE_WALLET_V0
  refusal_discharge: []
  refusal_deferrals: []
  refusal_governance_discharge: []
  withdrawn_facts: null
```

The design of record of `blockchain`: every artifact its registry holds, stated in the design language.
Written by `python -m transformation.record` from the registry. Construction of this design and its
mandate reproduces the registry, and `construction_acceptance` asks whether it does. A change to
`blockchain` is a dossier designed against the composition.
