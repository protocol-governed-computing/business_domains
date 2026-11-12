# Stage 2 — Domain Model — blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_09_list_actors_by_state
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Actor
    description: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    store_model: One durable record per actor, addressed by its contact address, updated in place, carrying its own state (unverified, accepted and rejected).
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Wallet
    description: The business must know where a person it has accepted holds value, one wallet to each such person.
    store_model: One durable record per wallet, addressed by its holder, carrying its own state (active).
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  entity_attributes:
  - entity: Actor
    attribute: Contact address
    meaning: What identifies an actor.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Actor
    attribute: Name
    meaning: Required when an actor is recorded, as a string.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Wallet
    attribute: Holder
    meaning: What identifies a wallet.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  business_processes:
  - process: Register actor
    initiator: Participant
    outcome: Records a new actor.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Accept actor
    initiator: Participant
    outcome: Moves an actor from unverified to accepted.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Reject actor
    initiator: Participant
    outcome: Moves an actor from unverified to rejected.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: List actors
    initiator: Participant
    outcome: Returns the actors that match.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Create wallet
    initiator: Participant
    outcome: Records a new wallet.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  process_steps:
  - process: Register actor
    step: '1'
    action: Records a new actor
    record_produced: The actor record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register actor
    step: '2'
    action: Record the operation on the identity trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Accept actor
    step: '1'
    action: Refuse when the actor is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Accept actor
    step: '2'
    action: Refuse when the actor is not unverified
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Accept actor
    step: '3'
    action: Moves an actor from unverified to accepted
    record_produced: The actor record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Accept actor
    step: '4'
    action: Record the operation on the identity trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Reject actor
    step: '1'
    action: Refuse when the actor is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Reject actor
    step: '2'
    action: Refuse when the actor is not unverified
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Reject actor
    step: '3'
    action: Moves an actor from unverified to rejected
    record_produced: The actor record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Reject actor
    step: '4'
    action: Record the operation on the identity trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: List actors
    step: '1'
    action: Returns the actors that match
    record_produced: The actor record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: List actors
    step: '2'
    action: Record the operation on the identity trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Create wallet
    step: '1'
    action: Refuse when a wallet that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Create wallet
    step: '2'
    action: Refuse when the actor who would hold it is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 6}
  - process: Create wallet
    step: '3'
    action: Refuse when the actor who would hold it is not accepted
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Create wallet
    step: '4'
    action: Records a new wallet
    record_produced: The wallet record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Create wallet
    step: '5'
    action: Record the operation on the wallet trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  belief_verification:
  - belief: The current identity design names the records, entrances and requests its callers use today.
    result: VERIFIED
    evidence: The baseline design names blockchain::RB_IDENTITY_BINDINGS_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0 and blockchain::IN_ACTOR_REGISTERED_V0, and the derived design carries them.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The current wallet design names the records, entrances and requests its callers use today.
    result: VERIFIED
    evidence: The baseline design names blockchain::IN_WALLET_CREATION_V0, and the derived design carries them.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Appendonly jsonl side effect, as the platform declares it
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Provide an append-only JSONL persistence layer with ordered event history.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Clock side effect, as the platform declares it
    fqdn: capability_side_effects::CS_CLOCK_V0
    what_it_does: Answers the time now.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Mutable json side effect, as the platform declares it
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Provide a mutable key-addressable JSON state store with last-write-wins semantics.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Registry side effect, as the platform declares it
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Provide a registry capability for stable indirection by binding symbolic keys to opaque addresses and underlying storage references.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Assemble record transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Combines multiple input values into a single structured record object.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Compare equal transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    what_it_does: Compare two values for equality.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Generate id transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
    what_it_does: Generates a deterministic unique identifier based on input data using Keccak-256 hashing.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Select records transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_SELECT_RECORDS_V0
    what_it_does: Select the records of an array that satisfy declared field criteria, and answer none when none do.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate parameter rules transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Evaluate declarative parameter constraint rules against a parameter map.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate record structure transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Validate a record against a provided schema of field validation rules.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate set membership transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Validate that a value is a member of a declared set.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  gaps:
  - gap: The composition holds none of 3 artifacts the ledger's decisions need.
    severity: CRITICAL
    impact: They are authored by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  architectural_observations:
  - observation: The identity design keeps its records through one binding, and the derived design carries its name.
    evidence: blockchain::RB_IDENTITY_BINDINGS_V0 · blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - observation: 39 artifacts the composition holds mean what the ledger decides, and keep their identity.
    evidence: blockchain::AC_PARTICIPANT_V0 · blockchain::CC_CHECK_REGISTER_ACTOR_SUBMISSION_V0 · blockchain::CC_CLAIM_ACTOR_CONTACT_ADDRESS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  discovery_concerns:
  - concern: Nothing the composition holds changes meaning or is retired.
    evidence: ''
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  open_questions: []
```

Projected from what the derivation observed: the baseline design, the derived design and the composition the inspector reads. Every row cites the change-request row it models.

---

## 1. Business Entities

---

## 2. Business Processes

---

## 3. Belief Verification — THE SPINE (fill this register FIRST)

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | architectural_observations · belief_verification · business_processes · discovery_concerns · entities · entity_attributes · gaps · open_questions · pps_baseline_fqdns · process_steps |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
