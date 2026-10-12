# Stage 5 — Business Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
    record for each person known to the system, the state that says whether the business has accepted
    them, and the record of every moment in their history. It establishes the authority to say that a
    person exists and that they are trusted — a person is an actor because identity says so, and is
    trusted because identity records an authority's decision to that effect. It manages the actor's
    lifecycle from admission through the single decision made about them, and it records every
    occurrence so that the business can afterwards show who registered, who decided, what was decided
    and on what grounds. It exists because the business must admit people before it knows anything about
    them and decide afterwards whether to trust them, and those are two acts by two parties at two
    times. It does not govern what a trusted actor may then do, which persons may be an authority, or
    anything an actor's conduct might later change.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: 'The seed states why the subdomain exists — that admission and trust are separate acts by separate parties. This states the subdomain that results: the records it holds, the authority it establishes over who exists and who is trusted, the lifecycle it manages, and the three things it does not govern. Nothing here contradicts the seed; what it adds is the standing description rather than the reason for the change.'
  scope_boundary:
  - capability: Declare the actors of this business
    status: IN_SCOPE
    notes: One actor for the ordinary participant; the authority is not one.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Declare the stores identity owns
    status: IN_SCOPE
    notes: 'Three: the actor and its state, the address registry, the trail.'
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Bind identity's workflows to the stores they use
    status: IN_SCOPE
    notes: Without it the workflows cannot reach the stores they declare.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    status: IN_SCOPE
    notes: Three distinct occurrences.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Record an acceptance and a rejection
    status: IN_SCOPE
    notes: Two records, not one carrying an outcome field.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Admit a person's registration and record them unverified
    status: IN_SCOPE
    notes: The first business operation.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Record an authority's decision against a registered actor
    status: IN_SCOPE
    notes: The second business operation, carrying every declared refusal.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Admit a request to register a person
    status: IN_SCOPE
    notes: The boundary registration is reached through.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Admit a request to record a verification decision
    status: IN_SCOPE
    notes: A distinct admission surface from registration's.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Determine the time an occurrence happened
    status: DEFERRED
    notes: Owned by the substrate. A prerequisite of this change and not a part of it — a business subdomain may not author a neutral capability.
    source_finding: {phase: p4, register: authoring_scope, key: Determine the time an occurrence happened}
  - capability: Re-application by a rejected actor
    status: DEFERRED
    notes: Deferred by the business until this change states what a rejection means.
    source_finding: {phase: p4, register: authoring_scope, key: Re-application by a rejected actor}
  - capability: Revocation of an accepted actor
    status: DEFERRED
    notes: Deferred by the business to a governed change of its own.
    source_finding: {phase: p4, register: authoring_scope, key: Revocation of an accepted actor}
  - capability: Governing which persons may be an authority
    status: DEFERRED
    notes: Identity records the name and does not resolve it.
    source_finding: {phase: p4, register: authoring_scope, key: Governing which persons may be an authority}
  - capability: Holding the material an authority examined
    status: DEFERRED
    notes: Deferred with its retention and privacy consequences.
    source_finding: {phase: p4, register: authoring_scope, key: Holding the material an authority examined}
  - capability: Correcting an actor's own details after registration
    status: DEFERRED
    notes: Deferred until a verification decision is defined.
    source_finding: {phase: p4, register: authoring_scope, key: Correcting an actor's own details after registration}
  business_objects:
  - store_name: Actor record
    record_model: MUTABLE_STATE
    business_rationale: The business needs one place that says which people it knows and whether each is trusted; the state changes once, in place, when a decision is recorded
    source_finding: {phase: p4, register: bm_entities, key: Actor}
  - store_name: Contact address registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Two registrations carrying the same address must not produce two actors, and only an atomic claim can guarantee that
    source_finding: {phase: p4, register: bm_entities, key: Contact Address}
  - store_name: Actor occurrence trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: An occurrence that has happened cannot be un-happened, so its record is never amended and never removed
    source_finding: {phase: p4, register: bm_entities, key: Occurrence}
  identity_semantics:
  - store_name: Actor record
    identity_field: Contact address
    source: Supplied by the person registering themselves
    uniqueness_rule: Two registrations carrying the same address describe the same person, and the second neither creates another actor nor is refused
    cross_subdomain_relationship: None — the actor is named by later subdomains and names none
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - store_name: Contact address registry
    identity_field: The contact address as supplied
    source: Supplied by the person registering themselves
    uniqueness_rule: The address is claimed once; a second claim on it resolves to the actor already admitted rather than refusing
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - store_name: Actor occurrence trail
    identity_field: Append position
    source: Assigned when the occurrence is appended
    uniqueness_rule: Each occurrence appends exactly one entry, and no entry is amended or removed
    cross_subdomain_relationship: Names the actor the occurrence was recorded against, and the authority when there is one
    source_finding: {phase: p4, register: bm_entities, key: Occurrence}
  invariants:
  - invariant: An actor is identified by exactly one contact address, and two actors never share one
    business_reason: The address is what makes two registrations the same person; if two actors could share one, the business could not say who it had admitted
    source_finding: {phase: p1, register: business_invariants, key: Two actors never share a contact address}
  - invariant: An actor is unverified, accepted or rejected, and never more than one at a time
    business_reason: The business would rather say it has not decided than imply a decision it has not made
    source_finding: {phase: p1, register: business_invariants, key: 'An actor is either unverified, accepted or rejected'}
  - invariant: An actor that has not been decided about is unverified
    business_reason: There is no fourth state and no absence of state; an actor with no decision is one the business has recorded and not accepted
    source_finding: {phase: p1, register: business_invariants, key: An actor that has not been decided about is unverified}
  - invariant: A decision exists only against a registration that exists
    business_reason: Without a registration it is not an incomplete decision but a meaningless one
    source_finding: {phase: p1, register: business_invariants, key: A verification decision exists only against a registration that exists}
  - invariant: An actor is decided about once, and is never accepted and rejected both
    business_reason: Trust is given or withheld once; revisiting it is a governed change the business deferred
    source_finding: {phase: p1, register: business_invariants, key: An actor is decided about once}
  - invariant: Every decision names the authority that made it
    business_reason: A decision whose author is unknown is not evidence
    source_finding: {phase: p1, register: business_invariants, key: A verification decision names the authority that made it}
  - invariant: A rejection states grounds
    business_reason: The grounds are the substance of a rejection, and a rejection without them cannot be reviewed
    source_finding: {phase: p1, register: business_invariants, key: A rejection states grounds}
  - invariant: A person never makes the decision about themselves
    business_reason: Trust the subject grants itself is not trust the business has extended
    source_finding: {phase: p1, register: business_invariants, key: A person never makes the verification decision about themselves}
  - invariant: Neither an unverified nor a rejected actor is trusted with anything
    business_reason: The whole change turns on an unverified actor being a distinct thing rather than a label on an ordinary one
    source_finding: {phase: p1, register: business_invariants, key: Neither an unverified nor a rejected actor is trusted}
  - invariant: Every recorded occurrence carries the time it occurred
    business_reason: A record whose times do not advance is regarded by the business as no record at all
    source_finding: {phase: p1, register: business_invariants, key: Every recorded occurrence carries the time it occurred}
  - invariant: No recorded occurrence is altered or removed once written
    business_reason: A correction is a further occurrence stating the correction, never an edit of what was written
    source_finding: {phase: p1, register: business_invariants, key: No recorded occurrence is altered or removed}
  actions:
  - action: Register
    object: A person, admitted as an unverified actor
    trigger: A person supplies their own identifying details
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Admit a person's registration and record them unverified}
  - action: Register
    object: A person already known, recorded as a further occurrence
    trigger: A person who has registered before supplies their details again
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Admit a person's registration and record them unverified}
  - action: Decide
    object: A registered actor, accepted or rejected
    trigger: An authority records a decision against a registered actor
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Record an authority's decision against a registered actor}
  - action: Reapply
    object: A rejected actor seeking a further decision
    trigger: A rejected person asks the business to consider them again
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Re-application by a rejected actor}
  - action: Revoke
    object: An accepted actor whose trust is withdrawn
    trigger: The business withdraws trust it has given
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Revocation of an accepted actor}
  - action: Correct
    object: An actor's own registered details
    trigger: A person's name or address changes after admission
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Correcting an actor's own details after registration}
  provisional_codes:
  - provisional_code: AC_PARTICIPANT_V0
    family: AC
    summary: The ordinary participant who registers themselves and is decided about
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  - provisional_code: STRUCTURE_IDENTITY_STORAGE_V0
    family: STRUCTURE
    summary: Declares the three stores identity owns and what each holds
    source_finding: {phase: p4, register: gap_register, key: GAP-03}
  - provisional_code: RB_IDENTITY_BINDINGS_V0
    family: RB
    summary: Binds identity's workflows to the stores they use
    source_finding: {phase: p4, register: gap_register, key: GAP-04}
  - provisional_code: EV_ACTOR_REGISTERED_UNVERIFIED_V0
    family: EV
    summary: The moment a person is admitted and trusted with nothing
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - provisional_code: EV_ACTOR_ACCEPTED_V0
    family: EV
    summary: The moment an authority records a decision to trust an actor
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - provisional_code: EV_ACTOR_REJECTED_V0
    family: EV
    summary: The moment an authority records a decision not to trust an actor, distinct in kind from an acceptance
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - provisional_code: CC_CLAIM_CONTACT_ADDRESS_V0
    family: CC
    summary: Claims a contact address so that two registrations of one person do not produce two actors
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - provisional_code: CC_RESOLVE_ACTOR_V0
    family: CC
    summary: Answers which actor a contact address denotes, and reports when none does
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - provisional_code: CC_VALIDATE_REGISTRATION_V0
    family: CC
    summary: Confirms a registration carries a name and an address, and that the address is of the form asked for
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - provisional_code: CC_REGISTER_ACTOR_V0
    family: CC
    summary: Claims the address, writes the actor unverified, and records the occurrence
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - provisional_code: CC_RECORD_VERIFICATION_DECISION_V0
    family: CC
    summary: Resolves the actor, refuses every declared refusal, moves the state and records the occurrence
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - provisional_code: CC_APPEND_ACTOR_OCCURRENCE_V0
    family: CC
    summary: Appends one occurrence to the trail, carrying the time it happened
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  - provisional_code: WF_REGISTER_ACTOR_V0
    family: WF
    summary: The governed sequence that admits a person as an unverified actor
    source_finding: {phase: p5, register: actions, key: Register}
  - provisional_code: WF_RECORD_VERIFICATION_DECISION_V0
    family: WF
    summary: The governed sequence that records an authority's decision against a registered actor
    source_finding: {phase: p5, register: actions, key: Decide}
  - provisional_code: IN_ACTOR_REGISTERED_V0
    family: IN
    summary: A request to admit a person as an actor
    source_finding: {phase: p4, register: gap_register, key: GAP-09}
  - provisional_code: IN_ACTOR_VERIFIED_V0
    family: IN
    summary: A request to record a decision, carrying the authority, the outcome and the grounds
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
  cross_subdomain_refs: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | p4_business_model_blockchain_identity_v0.md | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
| Stage 6 — Governance Intent | Pending | — |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
