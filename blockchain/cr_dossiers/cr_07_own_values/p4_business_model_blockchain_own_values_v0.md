# Stage 4 — Business Model: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person
    role: Registers, and is given a wallet once accepted. Unchanged by this change.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: business_vocabulary, row: 7}
  - actor: The authority
    role: Accepts or rejects a person. Unchanged by this change.
    authority_class: External business authority
    source_finding: {phase: p1, register: business_vocabulary, row: 7}
  - actor: Identity
    role: States the moment each of its acts records, the trail it goes on, and where a contact address sits.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  - actor: Wallet
    role: States the record of every wallet it creates, its identity's prefix and its moment.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Trail
    description: The moments in a person's or a wallet's history.
    store_model: Append-only, unchanged.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Claimed Address
    description: The contact address a person holds.
    store_model: One registry, unchanged.
    source_finding: {phase: p2, register: entities, row: 2}
  - entity: The Wallet
    description: An accepted person's wallet, its claimed identity and its record.
    store_model: One keyed store and one registry, unchanged.
    source_finding: {phase: p2, register: entities, row: 3}
  - entity: The Request
    description: What a caller sends to start an act.
    store_model: Not stored; handed to the act.
    source_finding: {phase: p2, register: entities, row: 4}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: The moments identity and wallet announce are unchanged; each is now the act's own.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: Identity
    verb: states
    object: the moment and the trail of each of its acts
    capability_need: State the moment and the trail of each identity act
    source_finding: {phase: p3, register: authoring_decisions, key: State the moment and the trail of each identity act}
  - subject: Identity
    verb: states
    object: where a contact address sits
    capability_need: State where the contact address sits
    source_finding: {phase: p3, register: authoring_decisions, key: State where the contact address sits}
  - subject: Wallet
    verb: states
    object: a new wallet's record, prefix and moment
    capability_need: State a new wallet's record, prefix and moment
    source_finding: {phase: p3, register: authoring_decisions, key: "State a new wallet's record, prefix and moment"}
  - subject: Identity
    verb: stops
    object: its entrances sending what its acts state
    capability_need: Stop the entrances sending what the acts state
    source_finding: {phase: p3, register: authoring_decisions, key: Stop the entrances sending what the acts state}
  capability_graph:
  - capability: State the moment and the trail of each identity act
    source_finding: {phase: p3, register: authoring_decisions, key: State the moment and the trail of each identity act}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Registration, acceptance and rejection each state their moment, on ACTOR_OCCURRENCES.
  - capability: State where the contact address sits
    source_finding: {phase: p3, register: authoring_decisions, key: State where the contact address sits}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: Registration states contact_address, as a string.
  - capability: State a new wallet's record, prefix and moment
    source_finding: {phase: p3, register: authoring_decisions, key: "State a new wallet's record, prefix and moment"}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: The holder is the person resolved; the rest are fixed values, and the entry point stops declaring the prefix.
  - capability: Stop the entrances sending what the acts state
    source_finding: {phase: p3, register: authoring_decisions, key: Stop the entrances sending what the acts state}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Each identity entrance sends only what the caller supplies.
  - capability: Leave records made before this change in place
    source_finding: {phase: p3, register: authoring_decisions, key: Leave records made before this change in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Unchanged; nothing rewrites what an act recorded.
  dependency_graph:
  - from: identity
    to: blockchain::WF_REGISTER_ACTOR_V1
    dependency_type: act replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The four acts}
  - from: identity
    to: blockchain::WF_ACCEPT_ACTOR_V1
    dependency_type: act replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The four acts}
  - from: identity
    to: blockchain::WF_REJECT_ACTOR_V1
    dependency_type: act replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The four acts}
  - from: wallet
    to: blockchain::WF_CREATE_WALLET_V1
    dependency_type: act replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The four acts}
  - from: identity
    to: blockchain::TI_REGISTER_ACTOR_V0
    dependency_type: entrance replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - from: identity
    to: blockchain::TI_ACCEPT_ACTOR_V0
    dependency_type: entrance replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - from: identity
    to: blockchain::TI_REJECT_ACTOR_V0
    dependency_type: entrance replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - from: wallet
    to: blockchain::IN_WALLET_CREATION_V0
    dependency_type: entry point replaced by its next version
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The wallet entry point}
  - from: identity
    to: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts the acts run}
  - from: identity
    to: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts the acts run}
  - from: wallet
    to: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts the acts run}
  - from: wallet
    to: blockchain::CC_CREATE_WALLET_RECORD_V1
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts the acts run}
  - from: wallet
    to: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The contracts the acts run}
  - from: identity
    to: blockchain::IN_ACTOR_REGISTERED_V0
    dependency_type: entry point re-pointed
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The identity entry points}
  - from: identity
    to: blockchain::IN_ACTOR_ACCEPTANCE_V0
    dependency_type: entry point re-pointed
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The identity entry points}
  - from: identity
    to: blockchain::IN_ACTOR_REJECTION_V0
    dependency_type: entry point re-pointed
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The identity entry points}
  constraint_register:
  - number: '1'
    constraint: Nothing changes for a request that supplies the values the acts now state.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: Records made before this change stay as they were made.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: No ending is added.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: Callers through an entrance send the same inputs as before.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  - number: '5'
    constraint: A change of meaning is a new identity, and its predecessor is retired by record.
    source_finding: {phase: p1, register: known_facts, row: 4}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: State the moment and the trail of each identity act}
    capability: State the moment and the trail of each identity act
    owner_subdomain: identity
    resolution: AUTHOR_NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: State where the contact address sits}
    capability: State where the contact address sits
    owner_subdomain: identity
    resolution: AUTHOR_NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: "State a new wallet's record, prefix and moment"}
    capability: State a new wallet's record, prefix and moment
    owner_subdomain: wallet
    resolution: AUTHOR_NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Stop the entrances sending what the acts state}
    capability: Stop the entrances sending what the acts state
    owner_subdomain: identity
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: Each act states, in its bindings, every value only the business may decide.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: A value the act states cannot be named by a caller.
    constraints_imposed: No act binds a moment, a trail, a place, a wallet value or a prefix to the request.
  - number: '2'
    decision: The wallet's holder is read from the person the act resolved.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: A wallet's holder is the person identity accepted.
    constraints_imposed: The holder and the wallet's identity come from the same resolved person.
  - number: '3'
    decision: The wallet entry point stops declaring the prefix.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: The prefix is the business's, not the caller's.
    constraints_imposed: The entry point's other inputs are unchanged.
  - number: '4'
    decision: Each identity entrance keeps its input contract and stops sending what its act states.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: Callers send the same inputs as before.
    constraints_imposed: No entrance gains or loses an input.
  - number: '5'
    decision: Each act, entrance and entry point whose meaning changes is stated under its next version, and its predecessor is retired by record, with the stood-down acts that name it.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: Identity is fixed at publication, and one version of each artifact is live.
    constraints_imposed: Nothing in force names a retired identity.
  - number: '6'
    decision: The identity entry points are re-pointed to their act's next version.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
    rationale: Every caller starts the same act as today.
    constraints_imposed: Only the part naming the act changes.
  - number: '7'
    decision: Records made before this change are left as they are.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    rationale: The record is added to and never rewritten.
    constraints_imposed: No backfill or repair step may be authored.
  authoring_scope:
  - capability: State the moment and the trail of each identity act
    gap_register_ref: GAP-01
  - capability: State where the contact address sits
    gap_register_ref: GAP-02
  - capability: State a new wallet's record, prefix and moment
    gap_register_ref: GAP-03
  - capability: Stop the entrances sending what the acts state
    gap_register_ref: GAP-04
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one identity or wallet already has: each contract keeps doing what it does, and
the act decides what it is handed.

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
| Answer an acceptance without grounds through an entrance | Waits on the transport standard letting an entrance's answer leave a field out. |
| The four other stood-down blockchain artifacts | Untouched by this change; nothing it retires is named by them. |

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
