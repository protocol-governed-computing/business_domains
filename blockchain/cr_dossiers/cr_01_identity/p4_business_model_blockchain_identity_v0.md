# Stage 4 — Business Model: blockchain / identity

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person registering
    role: Supplies their own identifying details and is admitted unverified.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: authority_boundaries, key: The details an actor registers with}
  - actor: The authority
    role: Records a decision accepting or rejecting a registered actor. Identified outside this function and never resolved by it.
    authority_class: External business authority
    source_finding: {phase: p1, register: authority_boundaries, key: Verification Decision}
  - actor: Identity
    role: Holds the actor, its state and the record of occurrences against it.
    authority_class: Owning subdomain
    source_finding: {phase: p1, register: authority_boundaries, key: Actor}
  bm_entities:
  - entity: Actor
    description: A person known to the system, whether or not the business has accepted them.
    store_model: A keyed store holding the actor and its current state, read at the moment of deciding.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - entity: Contact Address
    description: The address a person registers with; what identifies them as an actor.
    store_model: A registry claiming the address, which reports rather than accepts an address already held.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - entity: Verification Decision
    description: The outcome an authority states against a registered actor, with who stated it, when, and on what grounds.
    store_model: Held as the actor's state, and recorded as an occurrence that is never rewritten.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - entity: Occurrence
    description: A recorded moment in an actor's history, written when it happens and never rewritten.
    store_model: An append-only trail offering no update and no delete.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  resources: []
  events:
  - event: Actor Registered Unverified
    trigger: A person supplies their identifying details and is admitted.
    lifecycle_meaning: The business knows of the person and trusts them with nothing. It is the occurrence a decision is made against.
    source_finding: {phase: p1, register: business_events, key: Actor Registered Unverified}
  - event: Actor Registered Again
    trigger: A person already known registers a second time.
    lifecycle_meaning: The actor is unchanged; that the person registered twice is kept.
    source_finding: {phase: p1, register: business_events, key: Actor Registered Again}
  - event: Actor Accepted
    trigger: An authority records a decision to trust a registered actor.
    lifecycle_meaning: The actor becomes trusted, and the other functions may name them.
    source_finding: {phase: p1, register: business_events, key: Actor Accepted}
  - event: Actor Rejected
    trigger: An authority records a decision not to trust a registered actor.
    lifecycle_meaning: The actor remains trusted with nothing, and can afterwards be listed among those rejected.
    source_finding: {phase: p1, register: business_events, key: Actor Rejected}
  relationships:
  - subject: A person
    verb: registers
    object: themselves as an actor
    capability_need: Admit a person's registration and record them unverified
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a person's registration and record them unverified}
  - subject: An actor
    verb: is identified by
    object: a contact address
    capability_need: Claim and resolve the contact address
    source_finding: {phase: p3, register: authoring_decisions, key: Claim and resolve the contact address}
  - subject: An authority
    verb: decides about
    object: a registered actor
    capability_need: Record an authority's decision against a registered actor
    source_finding: {phase: p3, register: authoring_decisions, key: Record an authority's decision against a registered actor}
  - subject: An occurrence
    verb: is recorded against
    object: an actor
    capability_need: Hold the trail of occurrences
    source_finding: {phase: p3, register: authoring_decisions, key: Hold the trail of occurrences}
  - subject: An occurrence
    verb: carries
    object: the time it happened
    capability_need: Determine the time an occurrence happened
    source_finding: {phase: p3, register: authoring_decisions, key: Determine the time an occurrence happened}
  capability_graph:
  - capability: Hold the trail of occurrences
    source_finding: {phase: p3, register: authoring_decisions, key: Hold the trail of occurrences}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; the capability offers no update and no delete, which is what enforces the requirement.
  - capability: Hold an actor's current state
    source_finding: {phase: p3, register: authoring_decisions, key: Hold an actor's current state}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; read at the moment of deciding rather than derived from the trail.
  - capability: Claim and resolve the contact address
    source_finding: {phase: p3, register: authoring_decisions, key: Claim and resolve the contact address}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; an already-held address is reported, which is the repeated-registration outcome.
  - capability: Read a registration for absent or malformed details
    source_finding: {phase: p3, register: authoring_decisions, key: Read a registration for absent or malformed details}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is; the business drew the refusal boundary at absence and form, which is what it reads.
  - capability: Determine the time an occurrence happened
    source_finding: {phase: p3, register: authoring_decisions, key: Determine the time an occurrence happened}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Owned by the substrate, not by this subdomain. Nothing in the composition supplies a time and a clock cannot be a transform.
  - capability: Declare the actors of this business
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the actors of this business}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: One actor for the ordinary participant. The authority is not an actor of this function.
  - capability: Declare the stores identity owns
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores identity owns}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: 'Three stores: the actor and its state, the address registry, the trail.'
  - capability: Bind identity's workflows to the stores they use
    source_finding: {phase: p3, register: authoring_decisions, key: Bind identity's workflows to the stores they use}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Without it the workflows cannot reach the stores they declare.
  - capability: Recognise the moments an actor is registered, accepted and rejected
    source_finding: {phase: p3, register: authoring_decisions, key: 'Recognise the moments an actor is registered, accepted and rejected'}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: Three distinct occurrences, so a rejected actor can never be read as accepted.
  - capability: Record an acceptance and a rejection
    source_finding: {phase: p3, register: authoring_decisions, key: Record an acceptance and a rejection}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: Two records, not one carrying an outcome field.
  - capability: Admit a person's registration and record them unverified
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a person's registration and record them unverified}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: The first business operation; composes the reused claim, state and trail capabilities.
  - capability: Record an authority's decision against a registered actor
    source_finding: {phase: p3, register: authoring_decisions, key: Record an authority's decision against a registered actor}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: The second business operation, and the one carrying every refusal the business declared.
  - capability: Admit a request to register a person
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to register a person}
    status: CRITICAL
    gap_register_entry: GAP-09
    notes: The boundary registration is reached through, stating what it requires before any work begins.
  - capability: Admit a request to record a verification decision
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to record a verification decision}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: A distinct admission surface, because what a decision requires differs from what a registration requires.
  dependency_graph:
  - from: identity
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - from: identity
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - from: identity
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - from: identity
    to: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_transforms::CT_PURE_COMPARE_EQUAL_V0'}
  - from: identity
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - from: identity
    to: capability_transforms::CT_PURE_EXTRACT_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'capability_transforms::CT_PURE_EXTRACT_V0'}
  - from: identity
    to: actor::CONSTITUTION_ACTOR_IDENTITY_V0
    dependency_type: governance
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'actor::CONSTITUTION_ACTOR_IDENTITY_V0'}
  - from: identity
    to: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    dependency_type: governance
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'transport::CONSTITUTION_TRANSPORT_INGRESS_V0'}
  - from: identity
    to: the substrate capability supplying the current time
    dependency_type: capability call
    pps_status: GAP
    source_finding: {phase: p3, register: dependency_discoveries, key: A capability side effect supplying the current time}
  constraint_register:
  - number: '1'
    constraint: Registration and the verification decision are separate acts, by different parties at different times.
    source_finding: {phase: p1, register: constraints, key: Registration and the verification decision are separate acts}
    source: domain knowledge
  - number: '2'
    constraint: An unverified or rejected actor may hold no wallet and submit no transaction.
    source_finding: {phase: p1, register: constraints, key: An unverified or rejected actor may hold no wallet}
    source: domain knowledge
  - number: '3'
    constraint: A recorded occurrence may never be altered or removed.
    source_finding: {phase: p1, register: constraints, key: A recorded occurrence may never be altered or removed}
    source: invariant
  - number: '4'
    constraint: The time of an occurrence is determined at the moment it occurs.
    source_finding: {phase: p1, register: constraints, key: The time of an occurrence is determined at the moment it occurs}
    source: invariant
  - number: '5'
    constraint: Identity governs who an actor is and whether they are trusted, and nothing about what a trusted actor may do.
    source_finding: {phase: p1, register: constraints, key: Identity governs who an actor is and whether they are trusted}
    source: governance rule
  - number: '6'
    constraint: Two actors never share a contact address, and an actor is identified by exactly one.
    source_finding: {phase: p1, register: business_invariants, key: Two actors never share a contact address}
    source: invariant
  - number: '7'
    constraint: An actor is decided about once, and is never accepted and rejected both.
    source_finding: {phase: p1, register: business_invariants, key: An actor is decided about once}
    source: invariant
  - number: '8'
    constraint: A person never makes the verification decision about themselves.
    source_finding: {phase: p1, register: business_invariants, key: A person never makes the verification decision about themselves}
    source: invariant
  - number: '9'
    constraint: A rejection states grounds, and every decision names the authority that made it.
    source_finding: {phase: p1, register: business_invariants, key: A rejection states grounds}
    source: invariant
  - number: '10'
    constraint: An authority is identified outside this function and is never resolved by it.
    source_finding: {phase: p1, register: known_facts, key: An authority is identified outside the identity function}
    source: governance rule
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Determine the time an occurrence happened}
    capability: Determine the time an occurrence happened
    owner_subdomain: substrate — the neutral capability surface, not identity
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the actors of this business}
    capability: Declare the actors of this business
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the stores identity owns}
    capability: Declare the stores identity owns
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Bind identity's workflows to the stores they use}
    capability: Bind identity's workflows to the stores they use
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: 'Recognise the moments an actor is registered, accepted and rejected'}
    capability: Recognise the moments an actor is registered, accepted and rejected
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Record an acceptance and a rejection}
    capability: Record an acceptance and a rejection
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a person's registration and record them unverified}
    capability: Admit a person's registration and record them unverified
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Record an authority's decision against a registered actor}
    capability: Record an authority's decision against a registered actor
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-09
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to register a person}
    capability: Admit a request to register a person
    owner_subdomain: identity
    resolution: NEW
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a request to record a verification decision}
    capability: Admit a request to record a verification decision
    owner_subdomain: identity
    resolution: NEW
  design_decisions:
  - number: '1'
    decision: The trail rests on the append-only capability and never on the mutable one.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: The append-only capability offers no update and no delete, so unrewritability is a property of the mechanism rather than a discipline over it.
    constraints_imposed: No operation may read the trail to decide anything; state is read from the state store.
  - number: '2'
    decision: An actor's state is held as a value, not derived from the occurrences.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: The refusal that an actor is decided about once needs the state at the moment of deciding, not a reconstruction of it.
    constraints_imposed: The trail is evidence and is never the source of truth for state.
  - number: '3'
    decision: The contact address is the identifier; no second identifier is generated.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: Two registrations carrying the same address are the same person, which makes the address the key.
    constraints_imposed: Identifier generation is not used, and nothing resolves an actor by anything but its address.
  - number: '4'
    decision: Acceptance and rejection are recorded as two occurrences, not one carrying an outcome.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    rationale: The business must be able to list who was rejected and must never read a rejected actor as accepted; two records make both structural.
    constraints_imposed: No operation may write a single decision record and distinguish the outcome by a field.
  - number: '5'
    decision: The time capability is a gap owned by the substrate, not authored here.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: Determining the current time is a side effect and cannot be a transform; it is neutral mechanism and does not belong to a business domain.
    constraints_imposed: This change cannot complete until the substrate offers it; no identity artifact may invent a time.
  - number: '6'
    decision: The authority is recorded and never resolved.
    source_finding: {phase: p1, register: known_facts, key: An authority is identified outside the identity function}
    rationale: The business states an authority is part of the business rather than a participant admitted through this door.
    constraints_imposed: No store holds authorities, and the self-verification refusal compares two names rather than resolving one.
  authoring_scope:
  - capability: Declare the actors of this business
    gap_register_ref: GAP-02
  - capability: Declare the stores identity owns
    gap_register_ref: GAP-03
  - capability: Bind identity's workflows to the stores they use
    gap_register_ref: GAP-04
  - capability: Recognise the moments an actor is registered, accepted and rejected
    gap_register_ref: GAP-05
  - capability: Record an acceptance and a rejection
    gap_register_ref: GAP-06
  - capability: Admit a person's registration and record them unverified
    gap_register_ref: GAP-07
  - capability: Record an authority's decision against a registered actor
    gap_register_ref: GAP-08
  - capability: Admit a request to register a person
    gap_register_ref: GAP-09
  - capability: Admit a request to record a verification decision
    gap_register_ref: GAP-10
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists, what is authored is a declared gap. Nothing is
re-litigated and nothing new is decided. One gap is owned outside this subdomain, which the register
records rather than hides.

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
| Determine the time an occurrence happened | GAP-01 is owned by the substrate. It is a prerequisite of this change and not a part of it: a business domain may not author a neutral capability, and this change cannot be built until the substrate offers one. |
| Re-application by a rejected actor | Deferred by the business until this change states what a rejection means. |
| Revocation of an accepted actor | Deferred by the business to a governed change of its own. |
| Governing which persons may be an authority | Deferred by the business; identity records the name and does not resolve it. |
| Holding the material an authority examined | Deferred by the business with its retention and privacy consequences. |
| Correcting an actor's own details after registration | Deferred by the business until a verification decision is defined. |

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
