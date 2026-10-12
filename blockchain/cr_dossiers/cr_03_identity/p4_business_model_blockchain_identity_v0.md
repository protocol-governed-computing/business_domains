# Stage 4 — Business Model: blockchain / identity

## Machine

```yaml
document:
  phase: p4
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: The person registering
    role: Supplies the details that are theirs and stay theirs. Takes no part in this change and is the party it exists for.
    authority_class: Ordinary participant
    source_finding: {phase: p1, register: known_facts, row: 2}
  - actor: The authority
    role: Records a decision, which may change three things about a person and nothing else.
    authority_class: External business authority
    source_finding: {phase: p1, register: known_facts, row: 10}
  - actor: Identity
    role: Holds the record and owns how a decision is written into it.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: The Record
    description: 'What the business holds about a person: their admitted details together with their decided details.'
    store_model: One keyed store, one record per contact address, declared once and read by one artifact.
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Admitted Details
    description: The name, contact address and preferences a person supplied at registration.
    store_model: Held in the record, written when the person is admitted, and — today — removed when a decision is recorded.
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: Decided Details
    description: 'The state, the deciding authority and the grounds: the three things a decision may change.'
    store_model: Held in the same record, written by the deciding act.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - entity: Thinned Record
    description: A record a decision has already stripped of its admitted details.
    store_model: The same store, left as it is.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
  resources: []
  events:
  - event: NONE IDENTIFIED
    trigger: This change recognises no new moment.
    lifecycle_meaning: The moments the business records are unchanged in when they occur and in what they mean; the trail is unchanged by constraint.
    source_finding: {phase: p1, register: business_events, row: 1}
  relationships:
  - subject: A decision
    verb: changes
    object: the person's state, the deciding authority and the grounds
    capability_need: State which of a person's details a decision may change
    source_finding: {phase: p3, register: authoring_decisions, key: State which of a person's details a decision may change}
  - subject: A decision
    verb: leaves
    object: everything else the business holds about the person
    capability_need: Change part of a held record without replacing it
    source_finding: {phase: p3, register: authoring_decisions, key: Change part of a held record without replacing it}
  - subject: An authority
    verb: records
    object: a decision against a registered person
    capability_need: Record a decision against a registered person
    source_finding: {phase: p3, register: authoring_decisions, key: Record a decision against a registered person}
  - subject: A person
    verb: keeps
    object: the details they were admitted with
    capability_need: Change part of a held record without replacing it
    source_finding: {phase: p3, register: authoring_decisions, key: Change part of a held record without replacing it}
  capability_graph:
  - capability: Record a decision against a registered person
    source_finding: {phase: p3, register: authoring_decisions, key: Record a decision against a registered person}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Right in every respect but one. Its refusals, inputs and result statuses are unchanged; the step that writes is replaced.
  - capability: Change part of a held record without replacing it
    source_finding: {phase: p3, register: authoring_decisions, key: Change part of a held record without replacing it}
    status: SATISFIED
    gap_register_entry: ''
    notes: The capability publishes a keyed update, and the domain already binds that capability because its keyed write is what the step uses today.
  - capability: State which of a person's details a decision may change
    source_finding: {phase: p3, register: authoring_decisions, key: State which of a person's details a decision may change}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: Realised as the set of fields the update sets. What is not in the set is what a decision may not touch.
  - capability: Assemble the record a decision writes
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble the record a decision writes}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Retained unchanged, and left without a consumer by GAP-01. Recorded rather than resolved.
  - capability: Resolve the actor before a decision is recorded
    source_finding: {phase: p3, register: authoring_decisions, key: Resolve the actor before a decision is recorded}
    status: SATISFIED
    gap_register_entry: ''
    notes: Unchanged, and the reason the two operations never disagree in practice.
  - capability: Reach the decision from outside
    source_finding: {phase: p3, register: authoring_decisions, key: Reach the decision from outside}
    status: SATISFIED
    gap_register_entry: ''
    notes: The four boundary declarations name the workflow, not the contract, and are untouched.
  - capability: Restore details already lost
    source_finding: {phase: p3, register: authoring_decisions, key: Restore details already lost}
    status: SATISFIED
    gap_register_entry: ''
    notes: Nothing is authored. The business declines to rewrite records already written.
  dependency_graph:
  - from: identity
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Partial update of a held record at a key}
  - from: identity
    to: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    dependency_type: store declaration
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The store the decision writes}
  - from: identity
    to: blockchain::RB_IDENTITY_BINDINGS_V0
    dependency_type: runtime binding
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The binding that reaches the store}
  - from: identity
    to: blockchain::CC_RESOLVE_ACTOR_V0
    dependency_type: capability contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Resolving the actor before deciding}
  - from: identity
    to: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    dependency_type: composing workflow
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: The workflows that compose the deciding contract}
  - from: identity
    to: blockchain::TI_ACCEPT_ACTOR_V0
    dependency_type: boundary declaration
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: What a caller may send and is told}
  - from: identity
    to: blockchain::TI_REJECT_ACTOR_V0
    dependency_type: boundary declaration
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: What a caller may send and is told}
  - from: identity
    to: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    dependency_type: amended contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  constraint_register:
  - number: '1'
    constraint: A decision may change only the person's state, the authority who decided, and the grounds stated.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: A decision may change none of a person's own details.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: What a caller sends and is told back is unchanged.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: Records already written are never rewritten, including thin ones.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  - number: '5'
    constraint: Grounds are required to reject and optional to accept.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: Carried from the change that established the decision
  - number: '6'
    constraint: What is recorded in the trail is unchanged.
    source_finding: {phase: p1, register: constraints, row: 6}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Record a decision against a registered person}
    capability: Record a decision against a registered person
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: State which of a person's details a decision may change}
    capability: State which of a person's details a decision may change
    owner_subdomain: identity
    resolution: EXTEND
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble the record a decision writes}
    capability: Assemble the record a decision writes
    owner_subdomain: identity, in a later change
    resolution: DEFERRED
  - gap_code: GAP-04
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
    capability: Say which artifacts consume a store
    owner_subdomain: the components that build and publish the composition's indexes, not identity
    resolution: DEFERRED
  design_decisions:
  - number: '1'
    decision: The deciding contract's write becomes a partial update, and nothing else about the contract changes.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: Four of its five steps are correct. The defect is that one step writes a whole record where it must change part of one.
    constraints_imposed: No refusal, input or result status of the contract may change, or the correction stops being a correction.
  - number: '2'
    decision: The fields the update sets are the three a decision is entitled to change.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: Stating the rule as the set of updated fields puts it where a mechanism reads it. Stated only as an invariant it has been true and unenforced since the function was built.
    constraints_imposed: Adding a field to that set is a business change, not a technical one.
  - number: '3'
    decision: The record is addressed by the key that identifies it, and the correction depends on no rule of this domain.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: The store now offers a keyed update as well as a keyed write, so changing part of a record needs neither a replacement nor a filter. A correction that leaned on identity's uniqueness rule would have carried that rule wherever it was copied.
    constraints_imposed: 'The correction is portable: any domain changing part of a record it did not create uses the same operation, with no invariant to re-establish.'
  - number: '4'
    decision: A decision that reaches an actor the store does not hold now refuses instead of creating one.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: The two operations disagree about an absent subject, and the disagreement is in the safe direction.
    constraints_imposed: Nothing may rely on a decision creating the person it decides about.
  - number: '5'
    decision: The assembling step is retained though its output loses its consumer.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: The business asked for the smallest correction that ends the data loss, and removing a step changes the contract's shape more than the defect requires.
    constraints_imposed: A step whose output nothing reads is recorded as GAP-03 and not left unremarked.
  - number: '6'
    decision: Records already thinned are left as they are.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    rationale: The record is added to and never rewritten, and that holds even when what was written is thin.
    constraints_imposed: No migration, backfill or repair step may be authored.
  authoring_scope:
  - capability: Record a decision against a registered person
    gap_register_ref: GAP-01
  - capability: State which of a person's details a decision may change
    gap_register_ref: GAP-02
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. One capability is extended and
every other is satisfied by an artifact already in the composition, which is what a defect
correction looks like when the design was right and the artifact was not.

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
| Assemble the record a decision writes | GAP-03. Its output loses its only consumer with this change. Removing it alters the contract's shape more than ending the data loss requires, and the business asked for the smallest correction. |
| Say which artifacts consume a store | GAP-04 is owned by the components that build and publish the composition's indexes. A business domain does not author them, and this change needed the answer and obtained it by reading the contracts instead. |
| Restoring details lost from records already thinned | Declined by the business: the record is added to and never rewritten. |
| Correcting a person's own details | Deferred by the business and unchanged. |
| Enforcing that a rejection states grounds inside the business | Unchanged by this change and enforced at the boundary only. |

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
