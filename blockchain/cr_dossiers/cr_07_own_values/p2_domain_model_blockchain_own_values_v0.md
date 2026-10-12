# Stage 2 — Domain Model Verification: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Trail
    description: The moments in a person's or a wallet's history, each on a named trail.
    store_model: Append-only, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: The Claimed Address
    description: The contact address a person holds, which no one else may hold.
    store_model: One registry, one entry per address, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: The Wallet
    description: The wallet an accepted person is given, its claimed identity and its record.
    store_model: One keyed store and one registry, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  - entity: The Request
    description: What a caller sends to start an act, directly or through an entrance.
    store_model: Not stored; it is handed to the act.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 6}
  entity_attributes:
  - entity: The Trail
    attribute: The moment
    meaning: 'What occurred: ACTOR_REGISTERED_UNVERIFIED, ACTOR_ACCEPTED, ACTOR_REJECTED or WALLET_CREATED. Read today from the request.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: The Trail
    attribute: The trail's name
    meaning: ACTOR_OCCURRENCES for every identity moment; the wallet's own identity for a wallet's. Identity reads it today from the request.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: The Claimed Address
    attribute: Where it sits
    meaning: The contact_address field of the person's record, a string. Read today from the request.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: The Wallet
    attribute: Its record
    meaning: Holder, balance, denomination, classification and state. Taken whole from the request today.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: The Wallet
    attribute: Its identity's prefix
    meaning: The prefix of the identity a wallet is given. Declared today as a request value.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  business_processes:
  - process: Register a person
    initiator: The person
    outcome: A complete registration is recorded unverified, with its moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Accept a person
    initiator: An authority
    outcome: An unverified person is recorded accepted, with its moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Reject a person
    initiator: An authority
    outcome: An unverified person is recorded rejected, with grounds and its moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Create a wallet
    initiator: An accepted person
    outcome: A wallet is recorded for an accepted person, with its moment on the wallet's trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  process_steps:
  - process: Register a person
    step: '1'
    action: Check the registration.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 3}
  - process: Register a person
    step: '2'
    action: Claim the contact address, at the place the request names.
    record_produced: The claimed address.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - process: Register a person
    step: '3'
    action: Record the person unverified.
    record_produced: The person's record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 5}
  - process: Register a person
    step: '4'
    action: Record the moment the request names, on the trail the request names.
    record_produced: A moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Accept or reject a person
    step: '1'
    action: Look the person up, and record the decision.
    record_produced: The person's record, in its decided parts.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  - process: Accept or reject a person
    step: '2'
    action: Record the moment the request names, on the trail the request names.
    record_produced: A moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Create a wallet
    step: '1'
    action: Look the person up, and require them accepted.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 8}
  - process: Create a wallet
    step: '2'
    action: Determine and claim the wallet's identity, with the prefix the request names.
    record_produced: The claimed wallet identity.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 4}
  - process: Create a wallet
    step: '3'
    action: Record the wallet as the request states it.
    record_produced: The wallet.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 7}
  - process: Create a wallet
    step: '4'
    action: Record the moment the request names, on the wallet's trail.
    record_produced: A moment on the wallet's trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 9}
  belief_verification:
  - belief: Each identity act takes the moment it records and the trail it records it on from the request.
    result: VERIFIED
    evidence: blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1 and blockchain::WF_REJECT_ACTOR_V1 each bind blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0's occurrence_fields and stream_id to $.payload.occurrence_fields and $.payload.stream_id. The contract reads the moment from occurrence_fields.occurrence. Acceptance and rejection also read verifying_authority and grounds from occurrence_fields, a second copy of what their entry points already declare.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: Registration takes where the contact address sits, and what kind of value it is, from the request.
    result: VERIFIED
    evidence: blockchain::WF_REGISTER_ACTOR_V1 binds blockchain::CC_CLAIM_CONTACT_ADDRESS_V0's address_path and address_type to $.payload.address_path and $.payload.address_type. The contract extracts the address from the person's record at that path, as that type.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: Wallet's record is whatever the request supplies.
    result: VERIFIED
    evidence: blockchain::WF_CREATE_WALLET_V1 binds blockchain::CC_CREATE_WALLET_RECORD_V1's wallet_fields to $.payload.wallet_fields, and the contract writes them as the wallet's record. It also binds the wallet trail's occurrence_fields to the request. Run against the pinned composition with the act stating these values instead, a request naming another holder and a balance of 1000000 left a wallet held by the accepted person with a balance of zero.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: The wallet entry point declares the prefix of the wallet's identity as a request value.
    result: VERIFIED
    evidence: blockchain::IN_WALLET_CREATION_V0 declares wallet_id_prefix, required, and blockchain::WF_CREATE_WALLET_V1 binds blockchain::CC_DETERMINE_WALLET_IDENTITY_V0's wallet_id_prefix to it.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The three identity entrances send the moment, the trail and the address's place on every request.
    result: VERIFIED
    evidence: blockchain::TI_REGISTER_ACTOR_V0's payload_template states address_path, address_type, stream_id and occurrence_fields. blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 each state stream_id and occurrence_fields. No entrance starts the wallet act.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: The business's check of its entry points reports ten undeclared request values on identity and wallet acts.
    result: VERIFIED
    evidence: 'admission_contract_fidelity over the pinned composition reports ten UNDER-DECLARED findings on blockchain: occurrence_fields and stream_id on each identity entry point, address_path and address_type on blockchain::IN_ACTOR_REGISTERED_V0, and occurrence_fields and wallet_fields on blockchain::IN_WALLET_CREATION_V0.'
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  - belief: Entrances, entry points and runtime bindings name the acts they start or bind.
    result: VERIFIED
    evidence: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 name their act in handler.workflow. blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0 name it in workflow, by short code. blockchain::WF_CREATE_WALLET_V1 starts at blockchain::IN_WALLET_CREATION_V0. No runtime binding names an act. The stood-down blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0 name the V1 acts in superseded_by. The stood-down blockchain::WF_RECORD_VERIFICATION_DECISION_V0 names blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 in superseded_by, and the stood-down blockchain::IN_ACTOR_VERIFIED_V0 starts it. Nothing names an entrance. Outside the composition, the identity, wallet and routing-closure validations and the RUNBOOK run the acts by full name.
    source_finding: {phase: p1, register: system_beliefs, row: 7}
  pps_baseline_fqdns:
  - capability: Recording a moment on a person's trail
    fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    what_it_does: Appends the moment it is handed, on the trail it is handed, with the time it reads.
    fit: EXACT
    cannot_do: Nothing for this purpose; the act decides what it is handed.
  - capability: Claiming a contact address
    fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    what_it_does: Extracts the address at the place it is handed, and claims it.
    fit: EXACT
    cannot_do: Nothing for this purpose; the act decides the place.
  - capability: Checking a registration
    fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    what_it_does: Refuses an incomplete registration.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Determining a wallet's identity
    fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    what_it_does: Forms a wallet's identity from its holder and the prefix it is handed.
    fit: EXACT
    cannot_do: Nothing for this purpose; the act decides the prefix.
  - capability: Recording a person
    fqdn: blockchain::CC_REGISTER_ACTOR_V0
    what_it_does: Writes the person's record.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Recording a decision
    fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    what_it_does: Records the decision it checked.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Recording a wallet
    fqdn: blockchain::CC_CREATE_WALLET_RECORD_V1
    what_it_does: Writes the record it is handed as the wallet's.
    fit: EXACT
    cannot_do: Nothing for this purpose; the act decides the record.
  - capability: Looking a person up
    fqdn: blockchain::CC_RESOLVE_ACTOR_V1
    what_it_does: Resolves a contact address to the person's record, and reads it.
    fit: EXACT
    cannot_do: Nothing for this purpose; the wallet act reads the holder from its result.
  - capability: Recording a moment on a wallet's trail
    fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    what_it_does: Appends the moment it is handed to the wallet's trail.
    fit: EXACT
    cannot_do: Nothing for this purpose; the act decides the moment.
  - capability: Registration act
    fqdn: blockchain::WF_REGISTER_ACTOR_V1
    what_it_does: Checks, claims, records and announces a registration.
    fit: PARTIAL
    cannot_do: Takes the moment, the trail and the address's place from the request.
  - capability: Acceptance act
    fqdn: blockchain::WF_ACCEPT_ACTOR_V1
    what_it_does: Looks the person up, records the acceptance and announces it.
    fit: PARTIAL
    cannot_do: Takes the moment and the trail from the request.
  - capability: Rejection act
    fqdn: blockchain::WF_REJECT_ACTOR_V1
    what_it_does: Requires grounds, looks the person up, records the rejection and announces it.
    fit: PARTIAL
    cannot_do: Takes the moment and the trail from the request.
  - capability: Wallet act
    fqdn: blockchain::WF_CREATE_WALLET_V1
    what_it_does: Looks the person up, claims and records a wallet, and announces it.
    fit: PARTIAL
    cannot_do: Takes the wallet's record, its identity's prefix and its moment from the request.
  - capability: Registration entrance
    fqdn: blockchain::TI_REGISTER_ACTOR_V0
    what_it_does: Admits a caller's registration and starts the act.
    fit: PARTIAL
    cannot_do: Sends the moment, the trail and the address's place.
  - capability: Acceptance entrance
    fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    what_it_does: Admits a caller's acceptance and starts the act.
    fit: PARTIAL
    cannot_do: Sends the moment and the trail.
  - capability: Rejection entrance
    fqdn: blockchain::TI_REJECT_ACTOR_V0
    what_it_does: Admits a caller's rejection and starts the act.
    fit: PARTIAL
    cannot_do: Sends the moment and the trail.
  - capability: Wallet entry point
    fqdn: blockchain::IN_WALLET_CREATION_V0
    what_it_does: Admits a request naming the person a wallet is for.
    fit: PARTIAL
    cannot_do: Declares the prefix of the wallet's identity as a request value.
  - capability: Registration entry point
    fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    what_it_does: Admits a registration and starts the act.
    fit: PARTIAL
    cannot_do: Names the act this change replaces.
  - capability: Acceptance entry point
    fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    what_it_does: Admits an acceptance and starts the act.
    fit: PARTIAL
    cannot_do: Names the act this change replaces.
  - capability: Rejection entry point
    fqdn: blockchain::IN_ACTOR_REJECTION_V0
    what_it_does: Admits a rejection and starts the act.
    fit: PARTIAL
    cannot_do: Names the act this change replaces.
  gaps:
  - gap: Each identity act records the moment and the trail the request names.
    severity: CRITICAL
    impact: A direct caller can record a moment that did not happen, or put it on another trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Registration claims the address at the place the request names.
    severity: MAJOR
    impact: A caller can claim another field of the person's record as their contact address.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Wallet records whatever the request states.
    severity: CRITICAL
    impact: A caller can create a wallet for another holder, with any balance.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: A caller chooses the prefix of a wallet's identity.
    severity: MINOR
    impact: Part of a wallet's identity is the caller's, not the business's.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - gap: The entrances send values their acts will state.
    severity: MINOR
    impact: Once the acts state them, the entrances would send values nothing reads.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Entry points, entrances and stood-down acts name the acts this change replaces.
    severity: MAJOR
    impact: Once the acts are retired, they would still be started or named.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  architectural_observations:
  - observation: Every contract already does what it is handed. Only the acts and the entrances decide what they hand it.
    evidence: Every contract the acts run reads its values from its inputs. Each act binds those inputs; only the bindings change.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: A binding may state its value outright.
    evidence: blockchain::WF_REGISTER_ACTOR_V1 already states state UNVERIFIED in a binding, and blockchain::WF_CREATE_WALLET_V1 states the states admitting a wallet. The runtime hands a stated value as it is.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - observation: The wallet act already holds the accepted person.
    evidence: blockchain::WF_CREATE_WALLET_V1 reads the holder's contact address from blockchain::CC_RESOLVE_ACTOR_V1's result to determine the wallet's identity.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - observation: An entry point admits a request carrying values it does not declare.
    evidence: Every entrance and validation sends the values today, and every entry point admits them undeclared. A caller still sending them after this change is admitted, and the act ignores them.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  - observation: The stood-down published acts name the acts this change retires.
    evidence: Each of the four stood-down V0 acts names its V1 in superseded_by. Retiring a V1 leaves its V0 naming nothing, so the V0 is retired by record with it. blockchain::WF_RECORD_VERIFICATION_DECISION_V0 names two of those V0 acts, and blockchain::IN_ACTOR_VERIFIED_V0 starts it, so both are retired by record with them.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  - observation: An acceptance stating no grounds records none.
    evidence: An act reading grounds from the request leaves it out when the request has none, and the trail records the acceptance without it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  discovery_concerns:
  - concern: Records made before this change carry moments and values the request named.
    evidence: The business adds to its record and does not rewrite it, so those records stay as they were made.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 2}
  - concern: Four other blockchain artifacts stay stood down.
    evidence: blockchain::CC_RESOLVE_ACTOR_V0 and three wallet contracts' V0s are stood down, name nothing this change retires, and are untouched by it.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 7}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is where each identity and wallet act takes the values it records. Each act's bindings
were read for what they take from the request, and each contract for what it does with what it is
handed. The wallet belief was run against the pinned composition, with the act stating its values, on
a scratch data root.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
