# Stage 3 — Analysis Loop: blockchain / identity

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain: identity
  cr: cr_01_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'Nothing in the composition supplies the time at which something occurs. No capability operation returns one, and no transform derives one. The one worked precedent for an audit trail declares a time in the event''s schema and never fills it: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 appends a record and returns only a record id and a sequence number, so whatever time an event carries was assembled by its caller.'
    impact: The business requires the time to be determined at the moment the occurrence happens, which no caller-supplied value satisfies. The capability that determines it does not exist and must be authored.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 publishes APPEND and GET_ALL, whose outputs are result_status, record_id and sequence_number; book_library_mgmt::EV_BOOK_REGISTERED_V0 declares a required timestamp its appending contract never supplies
  - question_id: Q2
    finding: Determining the current time is a side effect and not a transform. A transform in this composition is pure by declaration — deterministic, no I/O — and a clock is neither, so no capability transform can supply the time however it is written.
    impact: The time capability is a capability side effect, which places it in the neutral substrate rather than in this business domain.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0 governs the transform surface; every transform in capability_transforms:: is declared pure, and none returns a value it did not derive from its inputs'
  - question_id: Q3
    finding: The business requirement decomposes into two guarantees the seed states as one. Ordering is guaranteed by the append itself — the stream returns a sequence number the store generates and no caller can influence. Wall-clock time is not guaranteed by anything. A record whose times did not advance would still be correctly ordered, but would not be the record the business asked for.
    impact: Ordering needs no new capability. Time does. The two are recorded separately so that a defect in one is not read as evidence about the other.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 APPEND returns sequence_number among its outputs; its input surface is record, stream_id and actor_id, none of which is a position
  - question_id: Q4
    finding: An actor's state is held as a value and not derived from the occurrences recorded against it. Deriving it would require reading the whole stream on every operation, and the refusal that an actor is decided about once needs the current state at the moment of deciding, not a reconstruction of it.
    impact: The actor's current state is held in a keyed store; the occurrences remain the evidence and are never the source of truth for state.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 offers only APPEND and GET_ALL, so a state read from it is a whole-stream read; capability_side_effects::CS_MUTABLE_JSON_V0 offers READ and SELECT against a key
  - question_id: Q5
    finding: The contact address is the identifier and no second identifier is generated against it. The business states two registrations carrying the same address are the same person, which makes the address the key; a generated identifier would be a second identity requiring the address to be resolved to it before anything could be done, and nothing in the change asks for one.
    impact: Identifier generation is not used. The address is claimed in a registry the way the catalog claims a book's identity key.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_GENERATE_ID_V0 is impacted by 9 artifacts and generates an identity unrelated to any business value; book_library_mgmt::CC_CLAIM_BOOK_IDENTITY_V0 is the worked precedent for claiming a business key instead
  - question_id: Q6
    finding: 'Uniqueness of the contact address is claimed through the registry, which reports rather than accepts an already-held key. That is exactly the repeated-registration behaviour the business asked for: the second registration neither creates a second actor nor fails.'
    impact: Repeated registration needs no bespoke capability and no read-then-write, which would not be atomic. The registry's own report of an existing key is the business outcome.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER, RESOLVE, EXISTS, COUNT and DEREGISTER and is impacted by 47 artifacts
  - question_id: Q7
    finding: 'Refusing a decision against an actor already decided about is expressible without a new capability: the actor''s state is resolved before the decision is recorded, and the transition is admitted only from the unverified state. The comparison is a pure transform against a declared set.'
    impact: The refusal is a declared step in the contract, not an invented runtime check.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 reads a value against a declared admitted set; capability_side_effects::CS_MUTABLE_JSON_V0 READ resolves the current state
  - question_id: Q8
    finding: Refusing a decision whose author is the actor decided about rests on comparing two names, not on resolving an authority. The business states an authority is identified outside this function and never resolved here, so the refusal is a comparison of the authority named on the decision against the actor it names.
    impact: The refusal is expressible today and needs no authority store, which the business deferred.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_COMPARE_EQUAL_V0 compares two supplied values; authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 governs execution authority, which is a different question and does not serve this refusal
  - question_id: Q9
    finding: An acceptance and a rejection are recorded as different occurrences rather than as one occurrence carrying an outcome field. The business requires that it can ask who has been rejected and receive an answer, and that a rejected actor can never be read as accepted; two distinct occurrences make both properties structural rather than a matter of reading a field correctly.
    impact: 'Two events are authored, not one. This is the defect the reverse-engineered module carried: it recorded a verification event whatever the decision was.'
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: book_library_mgmt declares a distinct event per outcome — book_library_mgmt::EV_BOOK_REGISTERED_V0 and book_library_mgmt::EV_BOOK_RETIRED_V0 — rather than one event carrying a state field
  - question_id: Q10
    finding: 'The actors of this business must be declared by this domain. Every domain in the composition declares its own and none is shared: the platform governs the form of an actor declaration and declares no actor.'
    impact: One actor is authored for the ordinary participant. The authority is not an actor of this function, so none is authored for it.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: actor::CONSTITUTION_ACTOR_IDENTITY_V0 governs actor declarations and declares no actor; ai_governance, book_library_mgmt, transformation and workload each declare their own
  verification_results:
  - item: The business author believes nothing in the blockchain domain exists yet, so identity is established rather than extended.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: 'Re-read against the pinned composition: the artifact catalog reports no artifact in the blockchain namespace, and the six domains it declares are unchanged'
  - item: The business author believes the platform already offers a way to record occurrences that is added to and never rewritten.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0 publishes APPEND and GET_ALL only; it is impacted by 58 artifacts, so the trail rests on the most heavily depended-upon side effect in the composition
  - item: The business author believes the platform already offers a way to hold a registry of business objects that can be looked up by their identifier.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: capability_side_effects::CS_REGISTRY_V0 publishes REGISTER alongside RESOLVE and EXISTS; impacted by 47 artifacts
  - item: The business author believes the platform already offers a way to generate an identifier for a newly admitted business object.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: capability_transforms::CT_PURE_GENERATE_ID_V0 is present and impacted by 9 artifacts. Confirmed to exist and, per Q5, not used by this change
  - item: The business author believes the platform already distinguishes a kind of actor empowered to act on the business's behalf from an ordinary participant.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: actor::CONSTITUTION_ACTOR_IDENTITY_V0 and authority::CONSTITUTION_AUTHORITY_GOVERNANCE_V0 are present with their separation invariants. Confirmed as a platform rule about execution, which Q8 establishes is not the separation this change needs
  - item: No capability supplies the time an occurrence happened.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: 'Re-read across all five declared capabilities: no operation returns a time, and no transform derives one'
  - item: A trail placed on the mutable store rather than the append-only one could be rewritten.
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE_WHERE, DELETE and DELETE_MANY; the choice of capability is what enforces the business requirement
  - item: Repeated registration is expressible without a bespoke capability.
    origin: {phase: p2, register: architectural_observations, row: 3}
    result: CONFIRMED
    evidence: 'Promoted from INFERRED: capability_side_effects::CS_REGISTRY_V0 declares REGISTER against a key and reports its outcome, which is the whole of what the business asked for'
  - item: An actor's current state and its trail are different storage problems.
    origin: {phase: p2, register: architectural_observations, row: 2}
    result: CONFIRMED
    evidence: 'Q4 resolves the choice: the state is keyed and read directly, the trail is appended and never read for state'
  dependency_discoveries:
  - dependency: capability_side_effects::CS_APPENDONLY_JSONL_V0
    type: side effect
    disposition: REUSE
    evidence: Holds the trail of occurrences; offers no update or delete, which is what makes the record unrewritable
  - dependency: capability_side_effects::CS_REGISTRY_V0
    type: side effect
    disposition: REUSE
    evidence: Claims the contact address and resolves it; reports an already-held key, which is the repeated-registration outcome
  - dependency: capability_side_effects::CS_MUTABLE_JSON_V0
    type: side effect
    disposition: REUSE
    evidence: Holds an actor's current state, read at the moment of deciding
  - dependency: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    type: transform
    disposition: REUSE
    evidence: Reads a registration for absent fields and for the form they must take, which is the whole of the unreadable-detail refusal
  - dependency: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    type: transform
    disposition: REUSE
    evidence: Reads a decision outcome against the two admitted values, and a current state against the states a decision is admitted from
  - dependency: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    type: transform
    disposition: REUSE
    evidence: Compares the authority named on a decision against the actor it decides about
  - dependency: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    type: transform
    disposition: REUSE
    evidence: Assembles the record each occurrence appends
  - dependency: capability_transforms::CT_PURE_EXTRACT_V0
    type: transform
    disposition: REUSE
    evidence: Extracts named values from a supplied registration or decision
  - dependency: A capability side effect supplying the current time
    type: side effect
    disposition: AUTHOR_NEW
    evidence: Nothing in the composition supplies one, and Q2 establishes it cannot be a transform. It is neutral mechanism rather than business behaviour, so it belongs to the substrate and not to this domain — a platform dependency this change requires and does not itself author
  - dependency: actor::CONSTITUTION_ACTOR_IDENTITY_V0
    type: governance
    disposition: EXISTING
    evidence: Governs the actor this domain declares
  - dependency: transport::CONSTITUTION_TRANSPORT_INGRESS_V0
    type: governance
    disposition: EXISTING
    evidence: Governs the boundary each operation is reached through
  impact_analysis:
  - artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    impact_scope: Reused unchanged; nothing about it is altered by this change
    consumer_count: '58'
    evidence: si.topology.impact impacted_count 58
  - artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    impact_scope: Reused unchanged
    consumer_count: '51'
    evidence: si.topology.impact impacted_count 51
  - artifact: capability_side_effects::CS_REGISTRY_V0
    impact_scope: Reused unchanged
    consumer_count: '47'
    evidence: si.topology.impact impacted_count 47
  - artifact: capability_transforms::CT_PURE_GENERATE_ID_V0
    impact_scope: Not used by this change
    consumer_count: '9'
    evidence: si.topology.impact impacted_count 9; Q5 resolves the address as the identifier
  - artifact: The blockchain namespace
    impact_scope: Created by this change; no existing artifact refers to it
    consumer_count: '0'
    evidence: The artifact catalog reports no artifact in the blockchain namespace
  authoring_decisions:
  - capability: Hold the trail of occurrences
    decision: REUSE
    rationale: The append-only capability offers no update and no delete, so the requirement that the record is never rewritten is a property of the mechanism rather than a discipline over it.
    alternatives_checked: 'The mutable store was checked and rejected: it permits update and delete, so a trail placed on it could be rewritten.'
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - capability: Hold an actor's current state
    decision: REUSE
    rationale: The state is read at the moment of deciding, which a keyed read answers and a whole-stream read does not.
    alternatives_checked: Deriving the state from the trail was checked and rejected in Q4.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Claim and resolve the contact address
    decision: REUSE
    rationale: The registry claims a business key and reports an already-held one, which is both the uniqueness rule and the repeated-registration outcome.
    alternatives_checked: Generating a separate identifier was checked and rejected in Q5.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - capability: Determine the time an occurrence happened
    decision: AUTHOR_NEW
    rationale: Nothing in the composition supplies a time, and a clock cannot be a transform. This change depends on a neutral capability the substrate does not yet offer.
    alternatives_checked: Every declared capability was checked; the catalog precedent was checked and shown to leave the time to its caller, which the business does not permit.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - capability: Read a registration for absent or malformed details
    decision: REUSE
    rationale: The business drew the refusal boundary at absence and form, which is exactly what record structure validation reads.
    alternatives_checked: Nothing else was needed; a judgement-based test would be the verification decision made early.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Record an acceptance and a rejection
    decision: AUTHOR_NEW
    rationale: Two distinct occurrences, so that a rejected actor can never be read as accepted and the business can ask who has been rejected.
    alternatives_checked: One occurrence carrying an outcome field was checked and rejected in Q9.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
  - capability: Declare the actors of this business
    decision: AUTHOR_NEW
    rationale: Every domain declares its own actors and none is shared. One is authored for the ordinary participant; the authority is not an actor of this function.
    alternatives_checked: Reusing another domain's actor was checked and rejected — no actor is declared outside a domain.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
  - capability: Admit a person's registration and record them unverified
    decision: AUTHOR_NEW
    rationale: The first of the two business operations. Nothing in the composition performs it, and it is the operation every other function's actor comes from.
    alternatives_checked: No existing workflow was found to extend; the composition holds no artifact of this domain.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - capability: Record an authority's decision against a registered actor
    decision: AUTHOR_NEW
    rationale: The second business operation, separate from the first because the business made it a separate act by a different party at a different time.
    alternatives_checked: 'Combining it with registration was checked and rejected: the business states that treating them as one is what this change exists to prevent.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Admit a request to register a person
    decision: AUTHOR_NEW
    rationale: The boundary each operation is reached through admits the request and states what it requires before any work begins.
    alternatives_checked: The composition's eighteen transport ingress contracts were checked; all belong to inspection and none admits a business registration.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Admit a request to record a verification decision
    decision: AUTHOR_NEW
    rationale: The decision is reached from outside and its admission surface is distinct from registration's, because what it requires is different.
    alternatives_checked: 'Sharing one admission surface with registration was checked and rejected: the two carry different required values.'
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
  - capability: Recognise the moments an actor is registered, accepted and rejected
    decision: AUTHOR_NEW
    rationale: Three moments the business named, each recorded as its own occurrence so that a rejected actor can never be read as accepted.
    alternatives_checked: One event carrying an outcome field was checked and rejected in Q9.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
  - capability: Declare the stores identity owns
    decision: AUTHOR_NEW
    rationale: The actor state, the address registry and the trail each need a declared store; nothing declares them because the domain does not exist.
    alternatives_checked: Reusing another domain's store declaration was checked and rejected — a store declaration is owned by the subdomain that holds it.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Bind identity's workflows to the stores they use
    decision: AUTHOR_NEW
    rationale: Without a binding the workflows cannot reach the stores they declare.
    alternatives_checked: Nothing exists to extend; book_library_mgmt::RB_CATALOG_BINDINGS_V0 binds the catalog's workflows and not this domain's.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  placement_decision:
  - decision: NEW_SUBDOMAIN
    subdomain: identity
    rationale: The composition holds no artifact of the blockchain domain, so there is nothing to extend. Identity is the first of the project's seven functions and owns the actor every later function names.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'The seven CRITICAL gaps carried from Stage 2 each resolve to a committed decision: the actor store and its state to REUSE of capability_side_effects::CS_MUTABLE_JSON_V0, the trail to REUSE of capability_side_effects::CS_APPENDONLY_JSONL_V0, address uniqueness to REUSE of capability_side_effects::CS_REGISTRY_V0, the actors and the decision record to AUTHOR_NEW, and the time to an AUTHOR_NEW substrate capability recorded as a dependency this change does not itself author'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: The three Stage 2 open questions are answered as Q1, Q4 and Q5, and all ten findings in this stage are CLOSED. The four business questions Stage 2 carried were returned to the business author and answered in the problem statement before this stage ran
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The eleven dependencies were established in one pass against the five declared capabilities and the catalog precedent; re-reading them surfaced no further dependency
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All nine items re-grounded and CONFIRMED, including the two Stage 2 discovery concerns and the belief about identifier generation, which is confirmed to exist and confirmed not to be used
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: 'Both Stage 2 INFERRED rows are promoted: repeated registration is confirmed OBSERVED against capability_side_effects::CS_REGISTRY_V0, and the conditional-transition concern is resolved OBSERVED by Q7. Every finding in this stage is OBSERVED'
```

Every decision here is taken against a composition that holds nothing of this domain, so the reuse
question is asked of the substrate alone and of one worked precedent — the catalog subdomain, which
solved the same storage problems first. Impact counts are read from the composition, never
estimated.

---

## 1. Analysis Findings

## 2. Mandatory Verification Pass

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Subdomain Placement Decision

## 7. Saturation Assessment

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · assumptions · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · constraints |
| **Consumes** ← Stage 2 | belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
