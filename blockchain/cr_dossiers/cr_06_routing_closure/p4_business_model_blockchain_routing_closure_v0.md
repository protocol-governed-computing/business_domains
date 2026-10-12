# Stage 4 — Business Model: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person
    role: Registers, and is given a wallet once accepted. Unchanged by this change.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - actor: The authority
    role: Accepts or rejects a person. Unchanged by this change.
    authority_class: External business authority
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - actor: Identity
    role: Ends each of its acts as rejected when a record fails.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  - actor: Wallet
    role: Ends its act as rejected when a record fails.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Person's Record
    description: A person's registration, state and decision.
    store_model: One keyed store, one record per contact address, unchanged.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Claimed Address
    description: The contact address a person holds.
    store_model: One registry, unchanged.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: The Trail
    description: The moments in a person's or a wallet's history.
    store_model: Append-only, unchanged.
    source_finding: {phase: p2, register: entities, row: 3}
  - entity: The Wallet
    description: An accepted person's wallet and its claimed identity.
    store_model: One keyed store and one registry, unchanged.
    source_finding: {phase: p2, register: entities, row: 4}
  - entity: A Failed Record
    description: A record that could not be read or written.
    store_model: Not stored; an answer a store gives.
    source_finding: {phase: p2, register: entities, row: 5}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: The moments identity and wallet announce are unchanged, and none is announced when a record fails.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: Identity
    verb: stops
    object: a lookup whose record failed
    capability_need: Stop a lookup at a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a lookup at a failed record}
  - subject: Wallet
    verb: stops
    object: a step whose record failed
    capability_need: Stop a wallet step at a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a wallet step at a failed record}
  - subject: Identity and wallet
    verb: end
    object: an act whose record failed, as rejected
    capability_need: End every act as rejected on a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: End every act as rejected on a failed record}
  capability_graph:
  - capability: Stop a lookup at a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a lookup at a failed record}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The lookup and the read each end the contract on a failed record.
  - capability: Stop a wallet step at a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a wallet step at a failed record}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: The claim, the write and the append each end their contract on a failed record.
  - capability: End every act as rejected on a failed record
    source_finding: {phase: p3, register: authoring_decisions, key: End every act as rejected on a failed record}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Thirteen act nodes route a failed record to the rejected ending.
  - capability: Leave records made before a failure in place
    source_finding: {phase: p3, register: authoring_decisions, key: Leave records made before a failure in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Unchanged; nothing removes what an act recorded before it failed.
  dependency_graph:
  - from: identity
    to: blockchain::CC_RESOLVE_ACTOR_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Looking a person up}
  - from: wallet
    to: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Claiming a wallet's identity}
  - from: wallet
    to: blockchain::CC_CREATE_WALLET_RECORD_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a wallet}
  - from: wallet
    to: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    dependency_type: contract replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a moment on a wallet's trail}
  - from: identity
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: platform store
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The stores}
  - from: identity
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: platform store
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The stores}
  - from: wallet
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: platform store
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The stores}
  - from: identity
    to: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts that already answer for a failed record}
  - from: identity
    to: blockchain::CC_REGISTER_ACTOR_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts that already answer for a failed record}
  - from: identity
    to: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts that already answer for a failed record}
  - from: identity
    to: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts that already answer for a failed record}
  constraint_register:
  - number: '1'
    constraint: Nothing changes for an act whose records are all read and written.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: Records made before a failure stay as they were made.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: No ending is added.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: A failed record ends the act. Nothing retries.
    source_finding: {phase: p1, register: known_facts, row: 4}
    source: The business author
  - number: '5'
    constraint: No published identity changes what it says, except to be stood down.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a lookup at a failed record}
    capability: Stop a lookup at a failed record
    owner_subdomain: identity
    resolution: AUTHOR_NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Stop a wallet step at a failed record}
    capability: Stop a wallet step at a failed record
    owner_subdomain: wallet
    resolution: AUTHOR_NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: End every act as rejected on a failed record}
    capability: End every act as rejected on a failed record
    owner_subdomain: identity, wallet
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: Each step whose store can fail ends its contract on a failed record.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: A step that carries on past a failed record decides something the business never said.
    constraints_imposed: Every step answers for every outcome its store declares.
  - number: '2'
    decision: Each act routes a failed record to its rejected ending.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: The business keeps two endings, and a failed record is not a success.
    constraints_imposed: Every outcome an act's contract can end with has a route.
  - number: '3'
    decision: A contract that can now end with a failed record says so.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: A contract states every outcome it can end with.
    constraints_imposed: No contract ends with an outcome it does not declare.
  - number: '4'
    decision: Records made before a failure are left as they are.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: The record is added to and never rewritten.
    constraints_imposed: No compensation, repair or backfill step may be authored.
  - number: '5'
    decision: Each of the eight acts is stated under a next version, and its published version is stood down unchanged.
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
    rationale: A change of meaning is a new identity, and identity is fixed at publication.
    constraints_imposed: The published declaration gains only its stand-down.
  - number: '6'
    decision: The entrances and intents that start an act are re-pointed to its next version.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    rationale: Every caller starts the same act as today.
    constraints_imposed: Only the part naming the act changes.
  authoring_scope:
  - capability: Stop a lookup at a failed record
    gap_register_ref: GAP-01
  - capability: Stop a wallet step at a failed record
    gap_register_ref: GAP-02
  - capability: End every act as rejected on a failed record
    gap_register_ref: GAP-03
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one identity or wallet already has: each step keeps doing what it does, and
answers for the failed record its store can report.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

## 2. Capability Graph (capability_graph)

## 3. Dependency Graph (dependency_graph)

## 4. Constraint Register (constraint_register)

## 5. Gap Register (gap_register)

## 6. Design Decisions (design_decisions)

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Tell a refusal apart from a failure | Declined for now by the business: it keeps two endings. |
| The superseded act's unrouted nodes | Not dispatched; nothing reaches them. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
