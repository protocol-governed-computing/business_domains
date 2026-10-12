# Stage 2 — Domain Model Verification: blockchain / identity

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Record
    description: 'What the business holds about a person: their admitted details together with their decided details.'
    store_model: One keyed store, holding one record per contact address, declared once by the subdomain's storage declaration and by nothing else.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Admitted Details
    description: The name, the contact address and the preferences a person supplied when they registered.
    store_model: Held in the same record. Written when the person is admitted and, today, removed when a decision is recorded.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: Decided Details
    description: 'The three things a decision is entitled to change: the person''s state, the authority who decided, and the grounds stated.'
    store_model: Held in the same record, written by the deciding act.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 10}
  - entity: The Trail
    description: The occurrences recorded against a person, added to and never rewritten.
    store_model: A separate append-only stream, untouched by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 6}
  - entity: Thinned Record
    description: A record from which a decision has already removed a person's admitted details.
    store_model: The same store. Left as it is; the business declines to rewrite it.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 15}
  entity_attributes:
  - entity: Admitted Details
    attribute: Name
    meaning: What the person is called, supplied by them at registration.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: Admitted Details
    attribute: Contact Address
    meaning: The address the person registered with, which identifies them and keys their record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Admitted Details
    attribute: Preferred Currency
    meaning: A convenience recorded at registration, having a default.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: Admitted Details
    attribute: Preferred Language
    meaning: A convenience recorded at registration, having a default.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: Decided Details
    attribute: State
    meaning: Whether the person is unverified, accepted or rejected.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - entity: Decided Details
    attribute: Verifying Authority
    meaning: The authority the decision names.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 10}
  - entity: Decided Details
    attribute: Grounds
    meaning: The reason stated for the decision.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 10}
  business_processes:
  - process: Record a decision about a person
    initiator: An authority within the business
    outcome: The person's state, the deciding authority and the grounds are recorded, and everything else the business holds about them is left as it was.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  process_steps:
  - process: Record a decision about a person
    step: '1'
    action: Resolve the person the address names, and refuse if none is found.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - process: Record a decision about a person
    step: '2'
    action: Refuse every refusal the business declared — a state that admits no decision, an outcome that is not admitted, an authority deciding about itself.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Record a decision about a person
    step: '3'
    action: Change the person's state, the authority named and the grounds, leaving every other detail as it is.
    record_produced: The person's record, still carrying what they were admitted with.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - process: Record a decision about a person
    step: '4'
    action: Record that the decision occurred.
    record_produced: An occurrence, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 6}
  belief_verification:
  - belief: The business author believes recording a decision replaces the person's record rather than adding to it.
    result: VERIFIED
    evidence: 'The fifth and last step of blockchain::CC_RECORD_VERIFICATION_DECISION_V0 writes to the ACTORS store with the operation WRITE, keyed on the contact address, and the value it writes is the record assembled by its own fourth step from the decided fields it was given. WRITE sets the whole value at the key, so whatever the assembled record does not carry ceases to be held. The assembled record carries the contact address, the state, the authority and the grounds, and nothing the person supplied. The belief holds exactly: the record is replaced, not added to.'
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are.
    result: VERIFIED
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE alongside WRITE, READ, EXISTS, LIST, SELECT, DELETE, DELETE_MANY and UPDATE_WHERE. UPDATE takes a key and a set of updates, and sets only the named fields on the record held at that key, leaving its other fields as they were. It reports SUCCESS when the key was held and VIOLATION when it was not, so it changes a record and never creates one. The capability this change needs exists, addresses one record by the key that identifies it, and is published on the surface identity already uses.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them.
    result: VERIFIED
    evidence: 'The composition declares exactly one store for this business''s actors, blockchain::ACTORS, at one path, declared once by blockchain::STRUCTURE_IDENTITY_STORAGE_V0 and by no other artifact. Of the domain''s six capability contracts, three name that store: one writes the actor when it is admitted, one writes it when a decision is recorded, and one reads it. No other artifact of any domain declares or writes it. Not overwriting is therefore sufficient.'
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: The business author believes nothing else in the composition depends on the shape a decision currently leaves behind.
    result: VERIFIED
    evidence: blockchain::CC_RESOLVE_ACTOR_V0 is the only reader of the store. It reads the record whole and publishes it as one object, and the deciding workflow consumes a single field of it — the state — to decide whether a decision is admitted. Nothing reads a name or a preference, and nothing enumerates the record's fields or asserts their number. Restoring what a decision currently removes adds fields to a value one consumer reads one field of, which no artifact can observe.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: The business author believes what a caller sends and is told is declared apart from how a decision is performed.
    result: VERIFIED
    evidence: What a caller may send is declared by blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0, and what they are told by blockchain::TE_ACCEPT_ACTOR_V0 and blockchain::TE_REJECT_ACTOR_V0. Each names the workflow it dispatches to and maps the caller's values onto that workflow's payload; none of the four names a capability contract or a step. A change inside a contract the workflow composes is invisible to all four, and the answer a caller is told is projected from the workflow's result surface, which this change does not alter.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  pps_baseline_fqdns:
  - capability: Recording a decision
    fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    what_it_does: Refuses every declared refusal in three steps, assembles the decided record in a fourth, and writes it in a fifth.
    fit: PARTIAL
    cannot_do: Its first four steps are correct and untouched by this change. Its fifth writes a whole record where it should change part of one, which is the defect.
  - capability: Whole-value write
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0 WRITE
    what_it_does: Sets the value held at a key, whatever was there before.
    fit: MISMATCH
    cannot_do: It cannot preserve what the value it is given does not carry. It is the right operation for admitting a person, whose record does not yet exist, and the wrong one for deciding about them.
  - capability: Partial update at a key
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0 UPDATE
    what_it_does: Sets named fields on the record held at one key, leaving its other fields as they are, and reports whether that key was held.
    fit: EXACT
    cannot_do: 'It changes a record and never creates one: a key nothing holds is reported as a violation. It addresses exactly the record the key identifies, so nothing about it depends on a rule of the domain that calls it.'
  - capability: Reading an actor
    fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    what_it_does: Resolves a contact address to an actor and reads the record whole.
    fit: EXACT
    cannot_do: Nothing for this purpose. It is the only reader, and it reads the whole record without asserting its shape.
  - capability: The actor store
    fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    what_it_does: Declares the store holding this business's actors, at one path.
    fit: EXACT
    cannot_do: Nothing for this purpose; the store is unchanged by this change.
  - capability: Admitting a person
    fqdn: blockchain::CC_REGISTER_ACTOR_V0
    what_it_does: Writes the actor when they are admitted, carrying the details they supplied.
    fit: EXACT
    cannot_do: Nothing for this purpose. It writes a record that does not yet exist, which is what a whole-value write is for.
  gaps:
  - gap: Recording a decision writes a whole record where it should change part of one.
    severity: CRITICAL
    impact: Every person accepted or rejected loses the name and the preferences they registered with. The business stated the opposite rule when the function was established and has been breaking it since.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Nothing in the composition states which of a person's details a decision may change.
    severity: MAJOR
    impact: The rule is stated in the business's own documents and realised in no artifact, which is why the defect was invisible to every check the composition runs.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - gap: Nothing restores the details already lost from records decided about before this change.
    severity: MINOR
    impact: Deliberately so — the business declines to rewrite what it has recorded, and would rather carry a thin old record than edit history.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: out_of_scope, row: 4}
  architectural_observations:
  - observation: The two writes to one store want different operations, because they answer different questions.
    evidence: blockchain::CC_REGISTER_ACTOR_V0 writes a record that does not yet exist, for which a whole-value write is correct. blockchain::CC_RECORD_VERIFICATION_DECISION_V0 writes a record that does, for which it is not. Both use the same operation today, and only one of them should.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - observation: The store's operations divide by how a record is addressed and by how much of it is changed, and one of the four was missing.
    evidence: A whole-value write addresses one record by its key; a filtered update addresses a set by matching values. Nothing addressed one record by its key and changed part of it, which is exactly what recording a decision needs. The capability now publishes it, so the correction rests on the operation it needs rather than on a rule of the domain that calls it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 3}
  - observation: The two operations disagree about a subject that is absent, and the disagreement is in the safe direction.
    evidence: A whole-value write to a key nothing holds creates it and reports success. A partial update whose filter matches nothing changes nothing and reports a violation. A decision reaches its write only after the actor has been resolved, so neither case should arise; if it did, the current operation would invent an actor and the proposed one would refuse.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 3}
  - observation: Every operation on the actor store already serialises concurrent callers within one process.
    evidence: The store's implementation takes a per-file lock around load, modify and save for each of its operations, so a partial update is not a weaker guarantee than the whole-value write it replaces. The lock is held per process, so it orders callers inside one server and not between a server and a separate run.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 3}
  - observation: The correction is invisible to every layer above the contract.
    evidence: The workflow composing the contract routes on its result status, which is unchanged; the boundary declarations name the workflow, not the contract; and the answer a caller is told is projected from the workflow's result surface. Nothing between the caller and the changed step observes the change.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  discovery_concerns:
  - concern: The composition cannot answer which artifacts consume a store, for fourteen of the fifteen stores it holds.
    evidence: The inspection operation that exists for this question reports no consumer for every store but one. The exception is a store whose runtime binding names a concrete path in its policy; every other binding names a storage declaration instead, and the index that answers the question joins a binding to a store by path alone. The domains that bind by declaration are every one the pipeline authored, plus the reference workload. This change needed exactly that answer — whether anything depends on the shape a decision leaves — and had to establish it by reading the contracts instead.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - concern: A rule the business states in its own documents is realised in no artifact and therefore checked by nothing.
    evidence: The business declared at the outset that a person keeps the details they were admitted with. No invariant, no contract step and no phase rule expresses it, so every document has passed and every build has succeeded while the function did the opposite. This is the second such rule found in this subdomain, after the requirement that a rejection states grounds.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: gaps, row: 2}
  - concern: The occurrence a decision records carries less than the business describes.
    evidence: An occurrence holds the contact address, the grounds, the time, what happened and the authority. A registration that differs from an earlier one is described by the business as recording the differing details, and the occurrence carries no name to record them in. This change does not touch the trail and does not correct it.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 6}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. This change
request is against a defect rather than an absence: the function exists, runs and is reached from
outside, and what is verified here is how one of its steps writes, what the platform offers instead,
and whether anything depends on what that step currently leaves behind.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
