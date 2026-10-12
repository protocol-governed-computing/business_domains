# Stage 3 — Analysis Loop: blockchain / wallet

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: The business's currency is not named anywhere in the composition. The business denominates every wallet in one currency and the name is a business fact, not a discoverable one. It is carried as a business truth and stated once where a wallet is recorded.
    impact: Every wallet carries it. Nothing else depends on the name.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Searching the composition's vocabulary for the term returns no match.
  - question_id: Q2
    finding: 'Establishing an address from key material the business is given is pure computation: the same material always yields the same address, and nothing outside the calculation is read or changed. It is therefore a way of working something out, not a way of touching the world, and the platform''s set of ways to touch the world does not need to grow.'
    impact: Decides whether this change is a domain change or a governance change. It is a domain change.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The business supplies the key material rather than the system generating it, so the calculation has no source of variation. The platform's closed set covers holding, trailing, claiming an identity, timing and deriving an identity; producing an address is none of those and needs none of them.
  - question_id: Q3
    finding: A moment that nothing refers to cannot be announced from anywhere. Making the three declared moments real is a change to how a decision and a registration are recorded, not a new thing to declare.
    impact: Wallet follows acceptance and cannot be built on a moment that never occurs.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: All three declared moments report a reference count of zero.
  - question_id: Q4
    finding: Grounds are required where a rejection is admitted and read by nothing thereafter. Refusing a groundless rejection is a change to what the recording of a decision checks, not to what the boundary admits.
    impact: The identity a wallet depends on keeps its own stated rule.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The contract that records a decision does not mention grounds.
  - question_id: Q5
    finding: Nothing in the composition holds a wallet, and nothing declares where one would be held. Both are authored new; neither displaces anything.
    impact: The substance of this change.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: No vocabulary match for the term anywhere in the composition.
  - question_id: Q6
    finding: A wallet is held as a changing record, and its creation is recorded on a trail that is added to and never rewritten. Both already exist in the platform's closed set and are used unchanged.
    impact: No new way of touching the world is needed.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Two of the six things the platform can do cover exactly this, and identity already uses both.
  verification_results:
  - item: 'Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them.'
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Twenty-three artifacts for the domain, all owned by identity; the two operations and their boundary contracts are present.
  - item: A person keeps the details they registered with when a decision is recorded about them.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Re-exercised against the pinned composition; an accepted person still carries their registered name and preferences.
  - item: Identity declares that it announces an acceptance, and does not actually announce it.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Reference count of zero on each, re-read from the pinned snapshot.
  - item: A rejection stating no grounds is currently accepted and recorded rather than refused.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Re-exercised; the rejection succeeds and the person is rejected with nothing recorded as to why.
  - item: No wallet exists anywhere in the business today.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Vocabulary search returns no match.
  - item: A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: Still absent. What the business holds to remains a business truth, not a finding.
  - item: Everything a wallet needs in order to be held, identified, timed and trailed already exists.
    origin: {phase: p2, register: architectural_observations, row: 4}
    result: CONFIRMED
    evidence: Re-read; the five capabilities are present and unchanged.
  - item: The act that creates a wallet reads records identity owns and declares nothing about them.
    origin: {phase: p2, register: belief_verification, row: 7}
    result: CONFIRMED
    evidence: The reused contract reads `CONTACT_ADDRESS_REGISTRY` and `ACTORS`; the act names only its own binding.
  - item: The business permits an act to declare the bindings it consults, and refuses a write through one.
    origin: {phase: p2, register: belief_verification, row: 8}
    result: CONFIRMED
    evidence: The constitution states the model, the invariant holds it, and the composition seals both bindings with each record marked.
  - item: A person nobody accepted is given a wallet today.
    origin: {phase: p2, register: belief_verification, row: 9}
    result: CONFIRMED
    evidence: Dispatching the act for an undecided person returns SUCCESS and records a wallet.
  dependency_discoveries:
  - dependency: Holding a changing record
    type: capability
    disposition: REUSE
    evidence: '`capability_side_effects::CS_MUTABLE_JSON_V0` — already used by identity to hold people.'
  - dependency: Holding a trail that is added to and never rewritten
    type: capability
    disposition: REUSE
    evidence: '`capability_side_effects::CS_APPENDONLY_JSONL_V0` — already used by identity for occurrences.'
  - dependency: Claiming an identity so two things cannot share one
    type: capability
    disposition: REUSE
    evidence: '`capability_side_effects::CS_REGISTRY_V0`.'
  - dependency: Supplying the time a moment occurred
    type: capability
    disposition: REUSE
    evidence: '`capability_side_effects::CS_CLOCK_V0`.'
  - dependency: Deriving an identity from what it is given
    type: capability
    disposition: REUSE
    evidence: '`capability_transforms::CT_PURE_GENERATE_ID_V0` — the same means identity uses.'
  - dependency: Establishing an address from supplied key material
    type: capability
    disposition: AUTHOR_NEW
    evidence: Pure computation; nothing in the composition does it. Owned by the domain, not the platform.
  - dependency: Establishing whether a person is one the business holds, and has accepted
    type: capability
    disposition: REUSE
    evidence: '`blockchain::CC_RESOLVE_ACTOR_V0` resolves a person; the acceptance state is on the record it returns.'
  - dependency: Recording that a moment occurred
    type: capability
    disposition: REUSE
    evidence: '`blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0` — nine consumers already depend on it, so it is a settled means.'
  - dependency: Announcing the three declared moments
    type: capability
    disposition: EXISTING
    evidence: The moments are declared and referenced by nothing; announcing them changes where they are referred to, not what they are.
  - dependency: Refusing a rejection that states no grounds
    type: capability
    disposition: EXISTING
    evidence: Changes what the recording of a decision checks.
  - dependency: Somewhere to hold a wallet
    type: storage
    disposition: AUTHOR_NEW
    evidence: Nothing declares it.
  - dependency: Somewhere to hold a wallet's trail
    type: storage
    disposition: AUTHOR_NEW
    evidence: Nothing declares it.
  - dependency: The records identity owns
    type: data
    disposition: EXISTING
    evidence: '`blockchain::RB_IDENTITY_BINDINGS_V0` covers all three, and is the binding the act declares it consults.'
  - dependency: Refusing a value outside the set the business admits
    type: capability
    disposition: REUSE
    evidence: '`capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0` raises, so a step that names it fails when the person was not accepted.'
  impact_analysis:
  - artifact: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    impact_scope: Nothing consumes it. Changing what it checks and what it announces reaches no other artifact.
    consumer_count: '0'
    evidence: '`si.topology.impact` reports `impacted_count 0`.'
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    impact_scope: Three consumers. The blast radius of adding a grounds check is confined to them.
    consumer_count: '3'
    evidence: '`si.topology.impact` reports `impacted_count 3`.'
  - artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    impact_scope: Nine consumers. Reused unchanged by this CR; nothing about it is altered, which is why the count is recorded rather than acted on.
    consumer_count: '9'
    evidence: '`si.topology.impact` reports `impacted_count 9`.'
  - artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    impact_scope: Nothing refers to it. Referring to it for the first time breaks nothing.
    consumer_count: '0'
    evidence: Reference count of zero.
  - artifact: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    impact_scope: Nothing refers to it.
    consumer_count: '0'
    evidence: Reference count of zero.
  - artifact: blockchain::EV_ACTOR_REJECTED_V0
    impact_scope: Nothing refers to it.
    consumer_count: '0'
    evidence: Reference count of zero.
  authoring_decisions:
  - capability: Giving an accepted person a wallet
    decision: AUTHOR_NEW
    rationale: Nothing in the composition does any part of it.
    alternatives_checked: Nothing to reuse; the vocabulary search returned no match.
    source_finding: {phase: p2, register: gaps, row: 1}
  - capability: Holding a wallet
    decision: REUSE
    rationale: A wallet is a record that changes. The platform already holds records that change, and identity uses the same means for people.
    alternatives_checked: 'Holding it as a trail was rejected: a balance is current state, not a history. `capability_side_effects::CS_MUTABLE_JSON_V0`'
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 8}
  - capability: Recording that a wallet was created
    decision: REUSE
    rationale: The moment goes on a trail added to and never rewritten, exactly as identity's moments do.
    alternatives_checked: '`capability_side_effects::CS_APPENDONLY_JSONL_V0`'
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 9}
  - capability: Determining a wallet's identity
    decision: REUSE
    rationale: The business already derives an identity from what it is given, and one person holds one wallet, so the person is what it is derived from.
    alternatives_checked: '`capability_transforms::CT_PURE_GENERATE_ID_V0`; deriving from person and classification was rejected because one person holds one wallet.'
    source_finding: {phase: p1, register: known_facts, row: 17}
  - capability: Ensuring two wallets never share an identity
    decision: REUSE
    rationale: Claiming a key is exactly this, and refusing the claim is how a second wallet is refused.
    alternatives_checked: '`capability_side_effects::CS_REGISTRY_V0`'
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - capability: Establishing the address others may pay to
    decision: AUTHOR_NEW
    rationale: 'Pure computation over key material the business supplies: the same material always yields the same address, nothing outside is read, nothing is changed. It is therefore a way of working something out, which the domain may author, and not a way of touching the world, which is closed.'
    alternatives_checked: 'Adding it to the platform''s closed set was examined and rejected — it is not neutral, and it is not needed, because the calculation is pure. Generating the key material rather than being given it was rejected at the seed: it would make the same request produce a different wallet each time.'
    source_finding: {phase: p1, register: known_facts, row: 18}
  - capability: Establishing that a person is held and accepted
    decision: REUSE
    rationale: Identity already resolves a person and the acceptance state travels on the record returned.
    alternatives_checked: '`blockchain::CC_RESOLVE_ACTOR_V0`'
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - capability: Announcing the moment a person is registered, accepted or rejected
    decision: EXTEND
    rationale: The moments are declared already. What is missing is anywhere referring to them, which is a change to how the two identity operations record what they did.
    alternatives_checked: 'Declaring new moments was rejected: three already exist and a second set would split one meaning in two.'
    source_finding: {phase: p2, register: gaps, row: 2}
  - capability: Refusing a rejection that states no grounds
    decision: EXTEND
    rationale: The rule is the business's own and already stated. What changes is that the recording of a decision now checks it.
    alternatives_checked: 'Requiring it only where the request is admitted was rejected: that is already so, and it is why the gap went unnoticed.'
    source_finding: {phase: p2, register: gaps, row: 3}
  - capability: Supplying the time a moment occurred
    decision: REUSE
    rationale: The platform supplies the time and identity already uses it.
    alternatives_checked: '`capability_side_effects::CS_CLOCK_V0`'
    source_finding: {phase: p1, register: known_facts, row: 19}
  - capability: Declaring that the wallet act reads the records identity owns
    decision: EXTEND
    rationale: The act exists and reads them already; what it lacks is the statement.
    alternatives_checked: 'Keeping a copy of who exists inside the wallet''s records was rejected by the business: a second copy of one truth can disagree with the thing it describes.'
    source_finding: {phase: p2, register: gaps, row: 7}
  - capability: Refusing a wallet to a person the business has not accepted
    decision: AUTHOR_NEW
    rationale: Nothing turns the state the act reads into a decision, so the refusal the business declared has no branch to route to.
    alternatives_checked: 'Reading the state inside an existing step was rejected: a step that succeeds whatever it finds leaves the refusal unreachable, and the transform that refuses must be able to raise.'
    source_finding: {phase: p2, register: gaps, row: 8}
  placement_decision:
  - decision: NEW_SUBDOMAIN
    subdomain: wallet
    rationale: A wallet is a thing the business holds in its own right, with its own identity, its own record and its own trail. It is owned by wallet and written only by wallet. Placing it inside identity would make identity the owner of value as well as of who a person is, and would leave the store of people written by a function that is not about people.
    source_finding: {phase: p1, register: authority_boundaries, row: 1}
  - decision: EXTEND
    subdomain: identity
    rationale: The announcements and the grounds check are identity's own, on identity's own artifacts, written by identity. Wallet does not write them and does not own them; it depends on the first of them.
    source_finding: {phase: p1, register: authority_boundaries, row: 4}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'All five critical gaps from Stage 2 are resolved: two by authoring new, two by extending identity, one by reusing what exists.'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: Both questions carried from Stage 2 are closed — the currency is a business truth, and the address is pure computation the domain may author.
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: The twelve dependencies were established in one pass and re-verification surfaced none beyond them.
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: Seven items re-grounded against the pinned snapshot; all seven CONFIRMED, none overturned.
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason
    status: SATISFIED
    evidence: All six findings are OBSERVED. None rests on inference.
```

Every gap Stage 2 recorded is resolved here, or carried with a stated reason. Every finding was
re-grounded against the pinned snapshot rather than inherited from Stage 2.

---

## 1. Analysis Findings

---

## 2. Mandatory Verification Pass

---

## 3. Dependency Discoveries

---

## 4. Impact Analysis

---

## 5. Authoring Decisions

---

## 6. Subdomain Placement Decision

---

## 7. Saturation Assessment
