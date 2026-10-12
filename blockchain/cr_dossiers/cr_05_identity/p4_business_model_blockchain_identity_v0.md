# Stage 4 — Business Model: blockchain / identity

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person registering
    role: Supplies a registration and is held unverified.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: known_facts, row: 1}
  - actor: The authority
    role: Records a decision about an unverified person, never about themselves.
    authority_class: External business authority
    source_finding: {phase: p1, register: known_facts, row: 5}
  - actor: Identity
    role: Holds the record, and now holds every rule it applies to it.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Record
    description: 'What the business holds about a person: their registration, their state and the decision made about them.'
    store_model: One keyed store, one record per contact address, unchanged.
    source_finding: {phase: p2, register: entities, row: 1}
  - entity: The Registration
    description: The name and the address a person is reached at, both required.
    store_model: Held in the record when the person is registered unverified.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - entity: The Decision
    description: An acceptance or a rejection, the authority, and the grounds.
    store_model: Written into the record's decided parts, built from the decision identity checked.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - entity: The Business's Rules
    description: What a registration must contain, which states admit a decision, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states grounds.
    store_model: Held by the identity steps that apply them. Held by nothing today.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: The moments identity records are unchanged in when they occur and in what they mean.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: Identity
    verb: refuses
    object: a registration missing what it must contain
    capability_need: Check a registration and refuse an incomplete one
    source_finding: {phase: p3, register: authoring_decisions, key: Check a registration and refuse an incomplete one}
  - subject: Identity
    verb: records
    object: a person as unverified when they register
    capability_need: Register a person unverified
    source_finding: {phase: p3, register: authoring_decisions, key: Register a person unverified}
  - subject: An authority
    verb: records
    object: an acceptance or a rejection about an unverified person
    capability_need: Record a decision only about an unverified person, and only an acceptance or a rejection
    source_finding: {phase: p3, register: authoring_decisions, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
  - subject: Identity
    verb: refuses
    object: an authority deciding about themselves
    capability_need: Refuse an authority deciding about themselves
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse an authority deciding about themselves}
  - subject: Identity
    verb: refuses
    object: a rejection stating no grounds
    capability_need: Refuse a rejection stating no grounds
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a rejection stating no grounds}
  capability_graph:
  - capability: Check a registration and refuse an incomplete one
    source_finding: {phase: p3, register: authoring_decisions, key: Check a registration and refuse an incomplete one}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: The check finds what is missing today and refuses nothing. It holds what a registration must contain and refuses on what it finds.
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    source_finding: {phase: p3, register: authoring_decisions, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: The deciding step holds both sets and builds the record from the decision it checked.
  - capability: Refuse an authority deciding about themselves
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse an authority deciding about themselves}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: A comparison of the authority with the person, and a fixed rule on its result.
  - capability: Refuse a rejection stating no grounds
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a rejection stating no grounds}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: The grounds step holds its own rules.
  - capability: Fix the decision each act records
    source_finding: {phase: p3, register: authoring_decisions, key: Fix the decision each act records}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: The acceptance act records an acceptance, the rejection act a rejection.
  - capability: Register a person unverified
    source_finding: {phase: p3, register: authoring_decisions, key: Register a person unverified}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: The registration act writes the state unverified as its own.
  - capability: Reach identity from outside
    source_finding: {phase: p3, register: authoring_decisions, key: Reach identity from outside}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: The entrances stop supplying what identity now holds; a caller sends and is told what they are today.
  - capability: Admit an acceptance with its grounds
    source_finding: {phase: p3, register: authoring_decisions, key: Admit an acceptance with its grounds}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: The acceptance gate declares the optional grounds the act reads.
  - capability: Admit a registration without the schema identity holds
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a registration without the schema identity holds}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: The registration gate stops requiring what the entrance no longer supplies.
  - capability: Record the moment of each act
    source_finding: {phase: p3, register: authoring_decisions, key: Record the moment of each act}
    status: SATISFIED
    gap_register_entry: ''
    notes: Unchanged; the moment stays the request's to name, outside this change.
  dependency_graph:
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking a record's structure}
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Refusing on a list of rules}
  - from: identity
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Refusing a value outside a set}
  - from: identity
    to: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Comparing two values}
  - from: identity
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: platform transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Assembling a record from fields}
  - from: identity
    to: blockchain::CC_RESOLVE_ACTOR_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'Resolving the person, claiming the address, writing the record, appending the moment'}
  - from: identity
    to: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'Resolving the person, claiming the address, writing the record, appending the moment'}
  - from: identity
    to: blockchain::CC_REGISTER_ACTOR_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'Resolving the person, claiming the address, writing the record, appending the moment'}
  - from: identity
    to: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: 'Resolving the person, claiming the address, writing the record, appending the moment'}
  - from: identity
    to: blockchain::CC_VALIDATE_REGISTRATION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Checking a registration}
  - from: identity
    to: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Recording a decision}
  - from: identity
    to: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Requiring rejection grounds}
  constraint_register:
  - number: '1'
    constraint: 'Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers.'
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: Records made under a request's own rules stay as they were made.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: What a request says about the business's rules is ignored, not refused.
    source_finding: {phase: p1, register: known_facts, row: 9}
    source: The business author
  - number: '4'
    constraint: A refusal changes no record.
    source_finding: {phase: p1, register: known_facts, row: 10}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Check a registration and refuse an incomplete one}
    capability: Check a registration and refuse an incomplete one
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
    capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse an authority deciding about themselves}
    capability: Refuse an authority deciding about themselves
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a rejection stating no grounds}
    capability: Refuse a rejection stating no grounds
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Fix the decision each act records}
    capability: Fix the decision each act records
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Register a person unverified}
    capability: Register a person unverified
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Reach identity from outside}
    capability: Reach identity from outside
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: Admit an acceptance with its grounds}
    capability: Admit an acceptance with its grounds
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-09
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    capability: Record the moment of each act as the act's own
    owner_subdomain: identity, in a later change
    resolution: DEFERRED
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: Admit a registration without the schema identity holds}
    capability: Admit a registration without the schema identity holds
    owner_subdomain: identity
    resolution: EXTEND
  design_decisions:
  - number: '1'
    decision: Each rule is held by the step that applies it, as a fixed value.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: A rule written where it is applied holds for every act that composes the step, and no act or request can widen it.
    constraints_imposed: Nothing may hand identity a rule identity holds.
  - number: '2'
    decision: The registration check is followed by a rule refusing when it found anything.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The platform check stays a reporter, as ruled; the business's contract decides.
    constraints_imposed: The check's report is consumed, never left unread.
  - number: '3'
    decision: The self-decision rule is a comparison followed by a fixed rule on its result.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: The rule checker compares a field only against a fixed value, and the platform already offers the comparison.
    constraints_imposed: No platform transform is changed or added.
  - number: '4'
    decision: The decided record is built from the decision the step checked, and each act fixes its decision.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: The state recorded must be the decision admitted, and a rejection must pass the rejection act's grounds rule.
    constraints_imposed: No part of the decided record may come from the request except the authority and the grounds.
  - number: '5'
    decision: Registration writes the state unverified as its own.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: The business's lifecycle has one way in, and it leads to unverified.
    constraints_imposed: No request can register a person in any other state.
  - number: '6'
    decision: The entrances stop supplying what identity holds, and change nothing a caller sends or is told.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
    rationale: Constants nothing reads would read as the rule.
    constraints_imposed: Every request the entrance admits today reaches the same outcome afterwards.
  - number: '7'
    decision: Records made before this change are left as they are.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
    rationale: The record is added to and never rewritten.
    constraints_imposed: No migration, backfill or repair step may be authored.
  authoring_scope:
  - capability: Check a registration and refuse an incomplete one
    gap_register_ref: GAP-01
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    gap_register_ref: GAP-02
  - capability: Refuse an authority deciding about themselves
    gap_register_ref: GAP-03
  - capability: Refuse a rejection stating no grounds
    gap_register_ref: GAP-04
  - capability: Fix the decision each act records
    gap_register_ref: GAP-05
  - capability: Register a person unverified
    gap_register_ref: GAP-06
  - capability: Reach identity from outside
    gap_register_ref: GAP-07
  - capability: Admit an acceptance with its grounds
    gap_register_ref: GAP-08
  - capability: Admit a registration without the schema identity holds
    gap_register_ref: GAP-10
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one identity already has: each step keeps doing what it does, and holds the rule
it applies instead of being handed it.

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
| Record the moment of each act as the act's own | GAP-09. The moment and its stream come from the request; no rule of the business names them, and this change does not ask. |
| Records made under a request's own rules | Declined by the business: the record is added to and never rewritten. |

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
