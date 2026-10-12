# Stage 7 — Design Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p7
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P7_V0
registers:
  design_resolution:
  - decision: Each act states, in its bindings, every value only the business may decide
    business_fact: A value only the business may decide is never taken from a request
    resolution: blockchain::WF_REGISTER_ACTOR_V2, blockchain::WF_ACCEPT_ACTOR_V2 and blockchain::WF_REJECT_ACTOR_V2
      state their moment and ACTOR_OCCURRENCES; registration states contact_address as a string; blockchain::WF_CREATE_WALLET_V2
      states the prefix wal, the wallet's record and WALLET_CREATED
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - decision: The wallet's holder is read from the person the act resolved
    business_fact: A wallet's holder is the person identity accepted
    resolution: The wallet's record and its moment take the holder from what blockchain::CC_RESOLVE_ACTOR_V1
      resolved, as the wallet's identity already does
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - decision: The wallet entry point stops declaring the prefix
    business_fact: The prefix of a wallet's identity is the business's
    resolution: blockchain::IN_WALLET_CREATION_V1 declares the contact address and the key material only
    source_finding:
      phase: p4
      register: design_decisions
      row: 3
  - decision: Each identity entrance keeps its input contract and stops sending what its act states
    business_fact: Callers send the same inputs through each entrance as before
    resolution: blockchain::TI_REGISTER_ACTOR_V1, blockchain::TI_ACCEPT_ACTOR_V1 and blockchain::TI_REJECT_ACTOR_V1
      send no moment, trail or address place
    source_finding:
      phase: p4
      register: design_decisions
      row: 4
  - decision: Each act, entrance and entry point whose meaning changes is stated under its next version
    business_fact: A change of meaning is a new identity
    resolution: The eight successors each supersede their predecessor, which is retired by record
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - decision: The identity entry points are re-pointed
    business_fact: Every caller starts the same act as today
    resolution: blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0 and blockchain::IN_ACTOR_REJECTION_V0
      name the next version of the act they start
    source_finding:
      phase: p4
      register: design_decisions
      row: 6
  - decision: Records made before this change are left as they are
    business_fact: The record is added to and never rewritten
    resolution: No backfill or repair step is designed
    source_finding:
      phase: p4
      register: design_decisions
      row: 7
  existing_inventory:
  - fqdn: blockchain::WF_REGISTER_ACTOR_V1
    action: REPLACE
    summary: The governed sequence that admits a person as an unverified actor, and announces that it
      did
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 1
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V1
    action: REPLACE
    summary: The governed sequence that records an acceptance and announces it
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 2
  - fqdn: blockchain::WF_REJECT_ACTOR_V1
    action: REPLACE
    summary: The governed sequence that records a rejection, with grounds required, and announces it
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 3
  - fqdn: blockchain::WF_CREATE_WALLET_V1
    action: REPLACE
    summary: The governed sequence that gives an accepted person a wallet and records that it did
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 4
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    action: REPLACE
    summary: Admits a request to register an actor, declaring the name and contact address a caller sends
      and holding the address path, stream, preferences and occurrence label the act requires
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    action: REPLACE
    summary: Admits a request to accept a registered actor, declaring the contact address, authority and
      optional grounds a caller sends and holding the stream and the acceptance occurrence label
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    action: REPLACE
    summary: Admits a request to reject a registered actor, declaring the contact address, authority and
      required grounds a caller sends and holding the stream and the rejection occurrence label
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    action: REPLACE
    summary: Admits a request naming the person a wallet is for, and refuses one that names nobody
    reason: Takes from the request what only the business may decide. Retired by record for its next version.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    action: REPOINT
    summary: A request to admit a person as an actor
    reason: Names the act this change replaces; it names the act's next version, and nothing else in it
      changes.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 9
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    action: REPOINT
    summary: Admits a request to accept a person, with the grounds the authority chooses to state, and
      refuses one that names nobody
    reason: Names the act this change replaces; it names the act's next version, and nothing else in it
      changes.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 10
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    action: REPOINT
    summary: Admits a request to reject a person, and refuses one that states no grounds
    reason: Names the act this change replaces; it names the act's next version, and nothing else in it
      changes.
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 11
  - fqdn: blockchain::AC_PARTICIPANT_V0
    action: REUSE
    summary: The ordinary participant who registers themselves and is decided about
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::AC_PARTICIPANT_V0
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    action: REUSE
    summary: Appends one occurrence to the trail
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p4
      register: dependency_graph
      key: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    action: REUSE
    summary: Records the moment on the wallet's trail
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    action: REUSE
    summary: Records the moment on the wallet's trail
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p4
      register: dependency_graph
      key: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    action: REUSE
    summary: Claims a contact address so that two registrations of one person do not produce two actors
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p4
      register: dependency_graph
      key: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    action: REUSE
    summary: Claims the identity, and refuses when the person already holds a wallet
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    action: REUSE
    summary: Claims the identity, and refuses when the person already holds a wallet
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
    action: REUSE
    summary: Records the wallet with a balance of zero, its denomination and its classification
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_CREATE_WALLET_RECORD_V0
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V1
    action: REUSE
    summary: Records the wallet with a balance of zero, its denomination and its classification
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p4
      register: dependency_graph
      key: blockchain::CC_CREATE_WALLET_RECORD_V1
  - fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    action: REUSE
    summary: Derives the wallet's identity from the person who holds it
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p4
      register: dependency_graph
      key: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
  - fqdn: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    action: REUSE
    summary: Establishes the address from key material supplied with the request
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    action: REUSE
    summary: Refuses a decision about a person not unverified, a decision other than an acceptance or
      a rejection, or an authority deciding about themselves, and records the decision it checked
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    action: REUSE
    summary: Writes the actor unverified after its address is claimed
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_REGISTER_ACTOR_V0
  - fqdn: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    action: REUSE
    summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or
      recorded
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  - fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    action: REUSE
    summary: Refuses a rejection stating no grounds, before anything is recorded
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    action: REUSE
    summary: Answers which actor a contact address denotes, and reports when none does
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_RESOLVE_ACTOR_V0
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V1
    action: REUSE
    summary: Answers which actor a contact address denotes, and reports when none does
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_RESOLVE_ACTOR_V1
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    action: REUSE
    summary: Refuses a registration lacking the person's name or their address
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::CC_VALIDATE_REGISTRATION_V0
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    action: REUSE
    summary: The moment an authority records a decision to trust an actor
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::EV_ACTOR_ACCEPTED_V0
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    action: REUSE
    summary: The moment a person is admitted and trusted with nothing
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    action: REUSE
    summary: The moment an authority records a decision not to trust an actor
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::EV_ACTOR_REJECTED_V0
  - fqdn: blockchain::EV_WALLET_CREATED_V0
    action: REUSE
    summary: Announces that a wallet was created, for whom, and when
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::EV_WALLET_CREATED_V0
  - fqdn: blockchain::RB_IDENTITY_BINDINGS_V0
    action: REUSE
    summary: The bindings identity's workflows resolve their capabilities and stores through
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::RB_IDENTITY_BINDINGS_V0
  - fqdn: blockchain::RB_WALLET_BINDINGS_V0
    action: REUSE
    summary: Binds the wallet workflow to the capabilities and stores it uses
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::RB_WALLET_BINDINGS_V0
  - fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    action: REUSE
    summary: Declares the three stores identity owns and the paths they occupy
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
  - fqdn: blockchain::STRUCTURE_WALLET_STORAGE_V0
    action: REUSE
    summary: Declares the three stores wallet owns
    reason: Reused as it stands; the act decides what it is handed.
    source_finding:
      phase: p2
      register: pps_baseline_fqdns
      key: blockchain::STRUCTURE_WALLET_STORAGE_V0
  new_artifacts:
  - capability: Register a person
    family: WF
    code: blockchain::WF_REGISTER_ACTOR_V2
    summary: The governed sequence that admits a person as an unverified actor, records that moment as
      its own, and announces it
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: State the moment and the trail of each identity act
  - capability: Accept a person
    family: WF
    code: blockchain::WF_ACCEPT_ACTOR_V2
    summary: The governed sequence that records an acceptance, records that moment as its own, and announces
      it
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: State the moment and the trail of each identity act
  - capability: Reject a person
    family: WF
    code: blockchain::WF_REJECT_ACTOR_V2
    summary: The governed sequence that records a rejection, with grounds required, records that moment
      as its own, and announces it
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: State the moment and the trail of each identity act
  - capability: Create a wallet
    family: WF
    code: blockchain::WF_CREATE_WALLET_V2
    summary: The governed sequence that gives an accepted person a wallet holding nothing, and records
      that it did
    owner_subdomain: wallet
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: State a new wallet's record, prefix and moment
  - capability: Offer registering an actor to a caller outside the business
    family: TI
    code: blockchain::TI_REGISTER_ACTOR_V1
    summary: Admits a request to register an actor, and sends the act only what the caller supplies and
      the person's preferences
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Stop the entrances sending what the acts state
  - capability: Offer accepting an actor to a caller outside the business
    family: TI
    code: blockchain::TI_ACCEPT_ACTOR_V1
    summary: Admits a request to accept a registered actor, and sends the act only what the caller supplies
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Stop the entrances sending what the acts state
  - capability: Offer rejecting an actor to a caller outside the business
    family: TI
    code: blockchain::TI_REJECT_ACTOR_V1
    summary: Admits a request to reject a registered actor, and sends the act only what the caller supplies
    owner_subdomain: identity
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: Stop the entrances sending what the acts state
  - capability: Admit a request for a wallet
    family: IN
    code: blockchain::IN_WALLET_CREATION_V1
    summary: Admits a request naming the person a wallet is for and the key it is made from, and refuses
      one that names nobody
    owner_subdomain: wallet
    status: NEW
    source_finding:
      phase: p6
      register: governance_outcome
      key: State a new wallet's record, prefix and moment
  rb_declarations:
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REGISTER_ACTOR_V2
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_ACCEPT_ACTOR_V2
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - rb_code: blockchain::RB_IDENTITY_BINDINGS_V0
    binds_wf: blockchain::WF_REJECT_ACTOR_V2
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - rb_code: blockchain::RB_WALLET_BINDINGS_V0
    binds_wf: blockchain::WF_CREATE_WALLET_V2
    cs_bindings:
    - capability_side_effects::CS_MUTABLE_JSON_V0
    - capability_side_effects::CS_APPENDONLY_JSONL_V0
    - capability_side_effects::CS_REGISTRY_V0
    - capability_side_effects::CS_CLOCK_V0
    storage_structure: blockchain::STRUCTURE_WALLET_STORAGE_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  execution_topology:
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: blockchain::IN_ACTOR_REGISTERED_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_VALIDATE_REGISTRATION_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: blockchain::CC_VALIDATE_REGISTRATION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REGISTER_ACTOR_V0
      ALREADY_EXISTS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: blockchain::CC_REGISTER_ACTOR_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_REGISTER_ACTOR_V2
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: blockchain::IN_ACTOR_ACCEPTANCE_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_ACCEPT_ACTOR_V2
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: blockchain::IN_ACTOR_REJECTION_V0
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RESOLVE_ACTOR_V0
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_REJECT_ACTOR_V2
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::IN_WALLET_CREATION_V1
    runs: ''
    node_type: IN
    routing:
      ACK: blockchain::CC_RESOLVE_ACTOR_V0
      NACK: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_RESOLVE_ACTOR_V0
    runs: blockchain::CC_RESOLVE_ACTOR_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
      NOT_FOUND: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    runs: blockchain::CC_CLAIM_WALLET_IDENTITY_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
      ALREADY_EXISTS: EXIT_REJECTED
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    runs: ''
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_CREATE_WALLET_RECORD_V0
      VIOLATION: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_CREATE_WALLET_RECORD_V0
    runs: blockchain::CC_CREATE_WALLET_RECORD_V1
    node_type: CC
    routing:
      SUCCESS: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    runs: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    node_type: CC
    routing:
      SUCCESS: EXIT_SUCCESS
      VIOLATION: EXIT_REJECTED
      BACKEND_ERROR: EXIT_REJECTED
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: EXIT_SUCCESS
    runs: ''
    node_type: EXIT_SUCCESS
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - workflow: blockchain::WF_CREATE_WALLET_V2
    node: EXIT_REJECTED
    runs: ''
    node_type: EXIT
    routing: null
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  cc_composition: []
  step_bindings:
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_VALIDATE_REGISTRATION_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_VALIDATE_REGISTRATION_V0
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: actor_record
    bound_to: payload.actor_record
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_path
    bound_to:
      literal: contact_address
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    direction: INPUT
    field: address_type
    bound_to:
      literal: string
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: actor_fields
    bound_to:
      literal:
        name: $.payload.actor_record.name
        contact_address: $.payload.actor_record.contact_address
        state: UNVERIFIED
        currency_preference: $.payload.actor_record.currency_preference
        language: $.payload.actor_record.language
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_REGISTER_ACTOR_V0
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_REGISTER_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_REGISTER_ACTOR_V0
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_REGISTERED_UNVERIFIED
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REGISTER_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: results.CC_CLAIM_CONTACT_ADDRESS_V0.result
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RESOLVE_ACTOR_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: ACCEPTED
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_ACCEPTED
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_ACCEPT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RESOLVE_ACTOR_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: current_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: decision
    bound_to:
      literal: REJECTED
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: verifying_authority
    bound_to: payload.verifying_authority
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    direction: INPUT
    field: grounds
    bound_to: payload.grounds
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: ACTOR_REJECTED
        verifying_authority: $.payload.verifying_authority
        grounds: $.payload.grounds
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to:
      literal: ACTOR_OCCURRENCES
    source_finding:
      phase: p4
      register: design_decisions
      row: 1
  - owner: blockchain::WF_REJECT_ACTOR_V2
    step: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: holder_state
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.state
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
    direction: INPUT
    field: states_admitting_a_wallet
    bound_to:
      literal:
      - ACCEPTED
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: holder
    bound_to: results.CC_RESOLVE_ACTOR_V0.value.contact_address
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id_prefix
    bound_to:
      literal: wal
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
    direction: INPUT
    field: key_material
    bound_to: payload.key_material
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_ESTABLISH_WALLET_ADDRESS_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_CREATE_WALLET_RECORD_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_CREATE_WALLET_RECORD_V0
    direction: INPUT
    field: wallet_fields
    bound_to:
      literal:
        holder: $.results.CC_RESOLVE_ACTOR_V0.value.contact_address
        balance: 0
        denomination: BACHI
        classification: DEFAULT
        state: ACTIVE
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: stream_id
    bound_to: results.CC_DETERMINE_WALLET_IDENTITY_V0.id
    source_finding:
      phase: p7
      register: execution_topology
      key: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    direction: INPUT
    field: occurrence_fields
    bound_to:
      literal:
        occurrence: WALLET_CREATED
        holder: $.results.CC_RESOLVE_ACTOR_V0.value.contact_address
    source_finding:
      phase: p4
      register: design_decisions
      row: 2
  - owner: blockchain::WF_CREATE_WALLET_V2
    step: blockchain::CC_RESOLVE_ACTOR_V0
    direction: INPUT
    field: contact_address
    bound_to: payload.contact_address
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  interface_fields:
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INPUT
    field: name
    type: string
    required: 'YES'
    default: ''
    meaning: Name the caller sends.
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: Contact address the caller sends.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: Contact address the caller sends.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: Verifying authority the caller sends.
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INPUT
    field: grounds
    type: string
    required: 'NO'
    default: ''
    meaning: Grounds the caller sends.
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: Contact address the caller sends.
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INPUT
    field: verifying_authority
    type: string
    required: 'YES'
    default: ''
    meaning: Verifying authority the caller sends.
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INPUT
    field: grounds
    type: string
    required: 'YES'
    default: ''
    meaning: Grounds the caller sends.
  - artifact: blockchain::IN_WALLET_CREATION_V1
    direction: INPUT
    field: contact_address
    type: string
    required: 'YES'
    default: ''
    meaning: The person the wallet is for.
  - artifact: blockchain::IN_WALLET_CREATION_V1
    direction: INPUT
    field: key_material
    type: string
    required: 'YES'
    default: ''
    meaning: The key material the address is worked out from.
  artifact_properties:
  - artifact: blockchain::WF_REGISTER_ACTOR_V2
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - artifact: blockchain::WF_ACCEPT_ACTOR_V2
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_ACCEPTED_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - artifact: blockchain::WF_ACCEPT_ACTOR_V2
    property: supersedes
    value:
    - blockchain::WF_ACCEPT_ACTOR_V1
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::WF_REJECT_ACTOR_V2
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_ACTOR_REJECTED_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - artifact: blockchain::WF_REJECT_ACTOR_V2
    property: supersedes
    value:
    - blockchain::WF_REJECT_ACTOR_V1
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::WF_CREATE_WALLET_V2
    property: emit.EXIT_SUCCESS
    value:
    - blockchain::EV_WALLET_CREATED_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  - artifact: blockchain::WF_REGISTER_ACTOR_V2
    property: supersedes
    value:
    - blockchain::WF_REGISTER_ACTOR_V1
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::WF_CREATE_WALLET_V2
    property: supersedes
    value:
    - blockchain::WF_CREATE_WALLET_V1
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    property: supersedes
    value:
    - blockchain::TI_REGISTER_ACTOR_V0
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::TI_ACCEPT_ACTOR_V0
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    property: supersedes
    value:
    - blockchain::TI_REJECT_ACTOR_V0
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  - artifact: blockchain::IN_WALLET_CREATION_V1
    property: supersedes
    value:
    - blockchain::IN_WALLET_CREATION_V0
    source_finding:
      phase: p4
      register: design_decisions
      row: 5
  structure_stores: []
  artifact_summary:
  - action: NEW
    subdomain: identity
    count: '6'
    artifacts: blockchain::WF_REGISTER_ACTOR_V2, blockchain::WF_ACCEPT_ACTOR_V2, blockchain::WF_REJECT_ACTOR_V2,
      blockchain::TI_REGISTER_ACTOR_V1, blockchain::TI_ACCEPT_ACTOR_V1, blockchain::TI_REJECT_ACTOR_V1
  - action: NEW
    subdomain: wallet
    count: '2'
    artifacts: blockchain::WF_CREATE_WALLET_V2, blockchain::IN_WALLET_CREATION_V1
  - action: REPLACE
    subdomain: identity
    count: '6'
    artifacts: blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1,
      blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0
  - action: REPLACE
    subdomain: wallet
    count: '2'
    artifacts: blockchain::WF_CREATE_WALLET_V1, blockchain::IN_WALLET_CREATION_V0
  declared_reach:
  - act: blockchain::WF_CREATE_WALLET_V2
    consults:
    - blockchain::RB_IDENTITY_BINDINGS_V0
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 8
  implementation_bindings: null
  vocabulary_extensions: null
  runtime_policies: null
  transport_bindings:
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.name
    bound_to: ${input.name}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.contact_address
    bound_to: ${input.contact_address}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.currency_preference
    bound_to:
      literal: BACHI
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - artifact: blockchain::TI_REGISTER_ACTOR_V1
    direction: INGRESS
    operation: blockchain.register_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REGISTER_ACTOR_V2
    field: actor_record.language
    bound_to:
      literal: en
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 5
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V2
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V2
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - artifact: blockchain::TI_ACCEPT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.accept_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_ACCEPT_ACTOR_V2
    field: grounds
    bound_to: ${input.grounds}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 6
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V2
    field: contact_address
    bound_to: ${input.contact_address}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V2
    field: verifying_authority
    bound_to: ${input.verifying_authority}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  - artifact: blockchain::TI_REJECT_ACTOR_V1
    direction: INGRESS
    operation: blockchain.reject_actor
    handler_kind: WF_INVOCATION
    handler_target: blockchain::WF_REJECT_ACTOR_V2
    field: grounds
    bound_to: ${input.grounds}
    source_finding:
      phase: p6
      register: pps_artifacts_requiring_action
      row: 7
  generation_provenance: null
  refusal_discharge: []
  refusal_deferrals: null
  refusal_governance_discharge: null
  molecule_steps: null
  molecule_step_bindings: null
  test_cases: null
  test_case_values: null
  withdrawn_facts: null
```

The four acts are carried from cr_06_routing_closure's design under their next versions, and each
binding that took a value only the business may decide now states it. The three entrances and the
wallet entry point are restated as they stand, less what this change removes. Every row was written by
`.github/process/notes/cr07-generators/gen_cr07_p7.py`.

---

## 1. Design Resolution

## 2. Existing Inventory

## 3. New Artifacts

## 4. Execution Topology

## 5. Step Bindings

## 6. Interface Fields

## 7. Artifact Properties

## 8. Transport Bindings

## 9. Artifact Summary
