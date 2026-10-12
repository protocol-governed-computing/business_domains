# Stage 2 — Domain Model Verification: blockchain / identity

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Actor
    description: A person known to the system, whether or not the business has accepted them.
    store_model: None — the composition holds no store for an actor of this business. A registry capability and an append-only capability both exist and neither is declared over any actor store.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: Verification Decision
    description: The outcome an authority states against a registered actor, together with who stated it, when, and on what grounds.
    store_model: None — nothing in the composition records a decision of one actor about another.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: Occurrence
    description: A recorded moment in an actor's history, written when it happens and never rewritten.
    store_model: None for this business. An append-only capability exists that could hold one; no stream is declared over it for identity.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - entity: Authority
    description: A party within the business empowered to decide about an actor, identified outside the identity function.
    store_model: None, and none required — the business states an authority is not held or resolved here, so what is modelled is the recording of its name, not the party.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 17}
  - entity: Contact Address
    description: The address a person registers with, which is what identifies them as an actor.
    store_model: None — no uniqueness registry is declared over any address of this business.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Preference
    description: A convenience recorded at registration — preferred currency or preferred language — bearing on neither identity nor the verification decision.
    store_model: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  entity_attributes:
  - entity: Actor
    attribute: Name
    meaning: What the person is called, supplied by them at registration.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - entity: Actor
    attribute: Contact Address
    meaning: The address the person registers with; what identifies them as an actor.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Actor
    attribute: State
    meaning: Whether the actor is unverified, accepted or rejected.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  - entity: Actor
    attribute: Preferred Currency
    meaning: The currency the person prefers to be quoted in. Has a default.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 24}
  - entity: Actor
    attribute: Preferred Language
    meaning: The language the person prefers to be addressed in. Has a default.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 24}
  - entity: Verification Decision
    attribute: Outcome
    meaning: Acceptance or rejection; there is no third.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 13}
  - entity: Verification Decision
    attribute: Deciding Authority
    meaning: The authority that stated the outcome, recorded on every decision.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 20}
  - entity: Verification Decision
    attribute: Grounds
    meaning: The reason stated for the outcome; required for a rejection.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 19}
  - entity: Occurrence
    attribute: Time
    meaning: The moment the occurrence happened, determined as it occurs.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 21}
  - entity: Occurrence
    attribute: Actor
    meaning: The actor the occurrence was recorded against.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  business_processes:
  - process: Register a person
    initiator: The person themselves
    outcome: The person is an actor of the system and is unverified, or is refused for details the business cannot read.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Record a verification decision
    initiator: An authority within the business
    outcome: The registered actor is accepted or rejected, and the decision is held as evidence naming its author, its time and its grounds.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  process_steps:
  - process: Register a person
    step: '1'
    action: Read the details supplied and refuse if a name or a contact address is absent.
    record_produced: None — a refusal produces no actor.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Register a person
    step: '2'
    action: Determine whether the contact address already identifies an actor.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - process: Register a person
    step: '3'
    action: Admit the person as an actor if the address is new, leaving the existing actor unchanged if it is not.
    record_produced: The actor, unverified.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 8}
  - process: Register a person
    step: '4'
    action: Record that the registration occurred, whether or not it created the actor.
    record_produced: An occurrence carrying the time it happened.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 9}
  - process: Record a verification decision
    step: '1'
    action: Resolve the actor the decision names and refuse if no such registration exists.
    record_produced: None — a refusal produces no decision.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Record a verification decision
    step: '2'
    action: Refuse if the actor has already been decided about, if the deciding authority is the actor itself, if the outcome is neither acceptance nor rejection, if no authority is named, or if a rejection states no grounds.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Record a verification decision
    step: '3'
    action: Move the actor from unverified to accepted or to rejected.
    record_produced: The actor in its decided state.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - process: Record a verification decision
    step: '4'
    action: Record that the decision occurred, distinctly for an acceptance and for a rejection.
    record_produced: An occurrence carrying the authority, the outcome, the grounds and the time.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 16}
  belief_verification:
  - belief: The business author believes nothing in the blockchain domain exists yet, so identity is established rather than extended.
    result: VERIFIED
    evidence: 'The pinned composition declares six business and platform namespaces — ai_governance, book_library_mgmt, inspection, platform, transformation, workload — across 345 artifacts, and inspection of the artifact catalog for the blockchain namespace returns no artifact in that namespace. The belief holds: nothing of this domain exists, and the change establishes rather than extends.'
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The business author believes the platform already offers a way to record occurrences that is added to and never rewritten.
    result: VERIFIED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 is declared in the composition as a storage capability offering exactly two operations, APPEND and GET_ALL. It admits a record, a stream and the actor appending, and returns the position at which the record was written. It offers no update and no delete, which is what makes the requirement that the record is added to and never rewritten a property of the mechanism rather than a discipline over it.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The business author believes the platform already offers a way to hold a registry of business objects that can be looked up by their identifier.
    result: VERIFIED
    evidence: capability_side_effects::CS_REGISTRY_V0 is declared in the composition offering REGISTER, RESOLVE, EXISTS, COUNT and DEREGISTER. Registering a key already held is reported rather than silently accepted, which is what a repeated registration of one contact address requires, and RESOLVE reports the absence of a key, which is what refusing a decision against an actor that never registered requires.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: The business author believes the platform already offers a way to generate an identifier for a newly admitted business object.
    result: VERIFIED
    evidence: capability_transforms::CT_PURE_GENERATE_ID_V0 is declared in the composition as a neutral capability transform, alongside capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, which read a supplied record for absent fields and a supplied value against an admitted set.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The business author believes the platform already distinguishes a kind of actor empowered to act on the business's behalf from an ordinary participant.
    result: VERIFIED
    evidence: actor::CONSTITUTION_ACTOR_IDENTITY_V0 governs how an actor is declared and authority::CONSTITUTION_AUTHORITY_GOVERNANCE_V0 governs authority over execution. actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0 and authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 hold the two apart as a platform rule, and every domain in the composition declares its own actors against them — ai_governance::AC_SYSTEM_V0 beside ai_governance::AC_EMPLOYEE_V0, and book_library_mgmt::AC_LIBRARY_STAFF_V0. The distinction is available; no actor of this business exists to carry it.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  pps_baseline_fqdns:
  - capability: Append-only recording
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Appends a record to a named stream and reads the stream whole. Offers no update and no delete.
    fit: EXACT
    cannot_do: It records occurrences; it holds no current state, so the state of an actor cannot be read from it without reading every occurrence against them.
  - capability: Identifier registry
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Registers a key against a value, resolves a key, reports whether one exists, counts and deregisters.
    fit: EXACT
    cannot_do: It holds identity, not history. It cannot say that a key was registered twice, only that it is held.
  - capability: Mutable record storage
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Writes, reads, updates, selects and deletes keyed records.
    fit: PARTIAL
    cannot_do: It permits update and delete, which the record of occurrences must not; it is fit for an actor's current state and unfit for the trail.
  - capability: Identifier generation
    fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
    what_it_does: Generates an identifier for a newly admitted object.
    fit: EXACT
    cannot_do: It generates an identifier; it neither derives one from a contact address nor decides whether an address is already held.
  - capability: Record structure validation
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Reads a supplied record for fields the declaration requires and for the form they must take.
    fit: EXACT
    cannot_do: It reads a record for absence and for form, which is exactly the boundary the business drew; it judges nothing about belief, which the business placed with the verification decision.
  - capability: Set membership validation
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Reads a supplied value against a declared admitted set.
    fit: EXACT
    cannot_do: Nothing for this purpose; the outcome of a decision is one of two admitted values.
  - capability: Record assembly
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Assembles a record from supplied fields.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Value extraction
    fqdn: capability_transforms::CT_PURE_EXTRACT_V0
    what_it_does: Extracts a named value from a supplied structure.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Actor identity governance
    fqdn: actor::CONSTITUTION_ACTOR_IDENTITY_V0
    what_it_does: Governs how an actor is declared and what an actor declaration must carry.
    fit: EXACT
    cannot_do: It governs the form of an actor declaration; it declares no actor of this business.
  - capability: Authority governance
    fqdn: authority::CONSTITUTION_AUTHORITY_GOVERNANCE_V0
    what_it_does: Governs authority over execution and holds actor and authority apart.
    fit: EXACT
    cannot_do: It governs who may execute; it does not govern one actor deciding about another, which is what a verification decision is.
  gaps:
  - gap: No store holds an actor of this business.
    severity: CRITICAL
    impact: A person cannot be admitted, and nothing can be looked up afterwards.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: No store holds the occurrences recorded against an actor.
    severity: CRITICAL
    impact: The business could not show who registered, who decided, what was decided or when, which is a requested outcome in its own right.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Nothing claims a contact address so that two actors cannot share one.
    severity: CRITICAL
    impact: Two registrations of one person would create two actors, and the identity rule the business stated would not hold.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Nothing declares the actors of this business.
    severity: CRITICAL
    impact: A person registering and an authority deciding are different kinds of party, and without the ordinary participant declared neither operation has an actor to admit.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Nothing holds an actor's state, so unverified, accepted and rejected are not represented.
    severity: CRITICAL
    impact: The whole change turns on an unverified actor being a distinct thing; without a state it is a label on nothing.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Nothing records a verification decision, its author or its grounds.
    severity: CRITICAL
    impact: Neither requested outcome concerning the decision can be met.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: No capability determines the time at which an occurrence happens.
    severity: CRITICAL
    impact: Every occurrence must carry the time it actually happened, and the business regards a record whose times do not advance as no record at all. Nothing observed in the composition supplies a time.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: architectural_observations, row: 3}
  - gap: No capability distinguishes a rejection from an acceptance in what it records.
    severity: MAJOR
    impact: The business must be able to ask who has been rejected and receive an answer, and must never be able to read a rejected actor as accepted.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: No capability refuses an operation on the ground that a decision has already been made.
    severity: MAJOR
    impact: An actor is decided about once, and nothing observed enforces it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Re-application after rejection, revocation, authority over verifiers, identity evidence and correction of an actor's details are absent from the composition.
    severity: MINOR
    impact: Each is deferred by the change request to a governed change of its own and is not modelled here.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: out_of_scope, row: 4}
  architectural_observations:
  - observation: The requirement that the record is never rewritten is satisfiable by choosing the capability rather than by disciplining its use.
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 offers APPEND and GET_ALL and nothing else, while capability_side_effects::CS_MUTABLE_JSON_V0 offers update and delete. A trail placed on the first cannot be rewritten; one placed on the second could be.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - observation: An actor's current state and the trail of occurrences against it are different storage problems and the composition offers a different capability for each.
    evidence: The registry resolves a key to a value and holds no history; the append-only stream holds history and answers no question about current state without being read whole.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - observation: Repeated registration is expressible without a bespoke capability, because registering a key already held is reported rather than accepted silently.
    evidence: capability_side_effects::CS_REGISTRY_V0 declares REGISTER among its operations and reports the outcome of one, so an existing key is a reportable outcome and not a failure.
    evidence_status: INFERRED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - observation: Every domain in the composition declares its own actors rather than drawing them from a shared set.
    evidence: ai_governance declares five actors including ai_governance::AC_SYSTEM_V0, book_library_mgmt declares book_library_mgmt::AC_LIBRARY_STAFF_V0, and no actor is declared outside a domain.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - observation: Nothing observed in the capability surface supplies the current time.
    evidence: The five capabilities declared are capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_SNAPSHOT_QUERY_V0 and capability_side_effects::CS_TEXT_ARTIFACT_V0, and none declares an operation returning a time.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: gaps, row: 7}
  - observation: The composition already carries governed transport boundary artifacts, so a business function reached from outside is an established shape rather than a new one.
    evidence: The pinned composition carries eighteen transport ingress and eighteen transport egress artifacts, all in the inspection namespace.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  discovery_concerns:
  - concern: The business requires every occurrence to carry the time it actually happened, and no capability observed in the composition supplies a time.
    evidence: No operation of the five declared capabilities returns a time, and no capability transform observed derives one.
    severity: CRITICAL
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: gaps, row: 7}
  - concern: An occurrence recorded against an actor is required to be unalterable, and the append-only capability enforces that only for what is placed on it.
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 is equally available and permits update and delete. Nothing observed prevents a trail being placed on it.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: architectural_observations, row: 1}
  - concern: The business requires that a person may never verify themselves while also stating that an authority is never resolved here, so the refusal must rest on a name the function does not hold.
    evidence: authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 and authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0 govern who may execute a workflow, which is not the same question as whether the subject of a decision is its author. Comparing an unresolved authority name against the actor decided about is the only observed means of expressing it.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 17}
  - concern: The business requires an actor to be decided about once, and neither observed storage capability expresses a transition permitted only from one state.
    evidence: The registry resolves and registers; the append-only stream appends. Neither declares a conditional transition.
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p2, register: gaps, row: 9}
  - concern: The change request states that an unverified or rejected actor may hold no wallet and submit no transaction, and neither function exists to be constrained.
    evidence: No artifact of the blockchain namespace is held by the composition.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  open_questions:
  - question: Where does the time of an occurrence come from, given that no observed capability supplies one?
    category: Capability
    why_it_matters: The business regards a record whose times do not advance as no record at all, and nothing observed can satisfy it.
    source_finding: {phase: p2, register: discovery_concerns, row: 1}
  - question: Is an actor's state held as a value that is read and replaced, or derived by reading the occurrences recorded against them?
    category: Modelling
    why_it_matters: The two available storage capabilities answer different questions, and the choice decides how "decided about once" is enforced.
    source_finding: {phase: p2, register: architectural_observations, row: 2}
  - question: Is the contact address itself the actor's identifier, or is a generated identifier held against it?
    category: Modelling
    why_it_matters: Identifier generation exists and so does a registry; whether both are needed depends on whether the business address is the key.
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 4}
```

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This is the first change request against a domain the
composition does not hold: what already exists here is platform capability and nothing of the
business, so the baseline is a register of mechanism rather than of prior behaviour.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
