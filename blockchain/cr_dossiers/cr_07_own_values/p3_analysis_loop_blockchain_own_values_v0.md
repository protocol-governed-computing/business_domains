# Stage 3 — Analysis Loop: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'Each identity act states the moment it records and the trail it records it on, in its binding of blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0: ACTOR_REGISTERED_UNVERIFIED, ACTOR_ACCEPTED or ACTOR_REJECTED, on ACTOR_OCCURRENCES. Acceptance and rejection hand the contract the authority and the grounds from the values their entry points already declare.'
    impact: Three acts change their bindings. The contract is unchanged.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #1; S2 architectural_observations #1 and #2'
  - question_id: Q2
    finding: Registration states that the contact address sits at contact_address in the person's record, as a string, in its binding of blockchain::CC_CLAIM_CONTACT_ADDRESS_V0.
    impact: The registration act changes its bindings. The contract is unchanged.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #2'
  - question_id: Q3
    finding: The wallet act states the record it creates. The holder is the contact address of the person blockchain::CC_RESOLVE_ACTOR_V1 resolved. The balance is 0, the denomination BACHI, the classification DEFAULT and the state ACTIVE. The wallet's trail records WALLET_CREATED, with the same holder.
    impact: The wallet act changes its bindings. The contracts are unchanged.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 known_facts #6 and #7; S2 belief_verification #3; S2 architectural_observations #3'
  - question_id: Q4
    finding: The wallet act states the prefix wal in its binding of blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, and the wallet entry point stops declaring wallet_id_prefix. The entry point's other inputs are unchanged.
    impact: The wallet act and its entry point change.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #4'
  - question_id: Q5
    finding: Each identity entrance stops sending the values its act now states. Each keeps its input contract, so callers send what they send today.
    impact: Three entrances change their payload template.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 known_facts #8; S2 belief_verification #5'
  - question_id: Q6
    finding: 'Eight identities change what they mean: four acts, three entrances and the wallet entry point. Each is stated under its next version and its predecessor is retired by record. The four stood-down published acts name the retired acts in superseded_by, so each is retired by record with them, and so are blockchain::WF_RECORD_VERIFICATION_DECISION_V0, which names two of them, and blockchain::IN_ACTOR_VERIFIED_V0, which starts it.'
    impact: Fourteen identities are retired by record. A citation of v5 is answered by v5.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 known_facts #3 and #4; S2 architectural_observations #5'
  - question_id: Q7
    finding: The three identity entry points name their act's next version, in the one part that names it. The wallet act's next version starts at the entry point's next version. Nothing names an entrance, and no runtime binding names an act.
    impact: Every caller starts the same act as today, under its next version.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #7; S2 gaps #6'
  - question_id: Q8
    finding: A caller that still sends the values is admitted, and the act ignores them. Every request admitted through an entrance today is admitted after this change, and every request refused is refused.
    impact: No caller is refused for what it sent before.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #1 and #4; S2 architectural_observations #4'
  - question_id: Q9
    finding: Records made before this change stay as they were made.
    impact: No repair, no backfill.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #2; S2 discovery_concerns #1'
  - question_id: Q10
    finding: The four other stood-down blockchain artifacts name nothing this change retires, and are left as they are.
    impact: Nothing else stood down changes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 discovery_concerns #2'
  verification_results:
  - item: Each identity act takes the moment it records and the trail it records it on from the request.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1
  - item: Registration takes where the contact address sits, and what kind of value it is, from the request.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: Wallet's record is whatever the request supplies.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: The wallet entry point declares the prefix of the wallet's identity as a request value.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q4
  - item: The three identity entrances send the moment, the trail and the address's place on every request.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q5
  - item: The business's check of its entry points reports ten undeclared request values on identity and wallet acts.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: Resolved in Q1, Q2 and Q3; no act takes a value its entry point does not declare
  - item: Entrances, entry points and runtime bindings name the acts they start or bind.
    origin: {phase: p2, register: belief_verification, row: 7}
    result: CONFIRMED
    evidence: Resolved in Q6 and Q7
  - item: Each identity act records the moment and the trail the request names.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1
  - item: Registration claims the address at the place the request names.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: Wallet records whatever the request states.
    origin: {phase: p2, register: gaps, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: A caller chooses the prefix of a wallet's identity.
    origin: {phase: p2, register: gaps, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q4
  - item: The entrances send values their acts will state.
    origin: {phase: p2, register: gaps, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q5
  - item: Entry points, entrances and stood-down acts name the acts this change replaces.
    origin: {phase: p2, register: gaps, row: 6}
    result: CONFIRMED
    evidence: Resolved in Q6 and Q7
  - item: Records made before this change carry moments and values the request named.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q9
  - item: Four other blockchain artifacts stay stood down.
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q10
  dependency_discoveries:
  - dependency: The four acts
    type: Workflows
    disposition: AUTHOR_NEW
    evidence: blockchain::WF_REGISTER_ACTOR_V1, blockchain::WF_ACCEPT_ACTOR_V1, blockchain::WF_REJECT_ACTOR_V1 and blockchain::WF_CREATE_WALLET_V1 are each replaced by a next version that states its own values
  - dependency: The three entrances
    type: Transport contracts
    disposition: AUTHOR_NEW
    evidence: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 are each replaced by a next version that sends only what the caller supplies
  - dependency: The wallet entry point
    type: Intent
    disposition: AUTHOR_NEW
    evidence: blockchain::IN_WALLET_CREATION_V0 is replaced by a next version without wallet_id_prefix
  - dependency: The contracts the acts run
    type: Capability contracts
    disposition: REUSE
    evidence: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0, blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_DETERMINE_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V1 and blockchain::CC_APPEND_WALLET_OCCURRENCE_V1, unchanged
  - dependency: The identity entry points
    type: Intents
    disposition: EXISTING
    evidence: blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0 and blockchain::IN_ACTOR_REJECTION_V0, each re-pointed to its act's next version
  impact_analysis:
  - artifact: blockchain::WF_REGISTER_ACTOR_V1
    impact_scope: Retired by record and replaced by its next version — states the moment, the trail and the address's place
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: blockchain::WF_ACCEPT_ACTOR_V1
    impact_scope: Retired by record and replaced by its next version — states the moment and the trail
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: blockchain::WF_REJECT_ACTOR_V1
    impact_scope: Retired by record and replaced by its next version — states the moment and the trail
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: blockchain::WF_CREATE_WALLET_V1
    impact_scope: Retired by record and replaced by its next version — states the wallet's record, prefix and moment
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    impact_scope: Retired by record and replaced by its next version — sends only what the caller supplies
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    impact_scope: Retired by record and replaced by its next version — sends only what the caller supplies
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    impact_scope: Retired by record and replaced by its next version — sends only what the caller supplies
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::IN_WALLET_CREATION_V0
    impact_scope: Retired by record and replaced by its next version — no longer declares the prefix
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    impact_scope: Retired by record with the act it names in superseded_by
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    impact_scope: Retired by record with the act it names in superseded_by
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    impact_scope: Retired by record with the act it names in superseded_by
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_CREATE_WALLET_V0
    impact_scope: Retired by record with the act it names in superseded_by
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    impact_scope: Retired by record with the acts it names in superseded_by
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::IN_ACTOR_VERIFIED_V0
    impact_scope: Retired by record with the act it starts
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  authoring_decisions:
  - capability: State the moment and the trail of each identity act
    decision: AUTHOR_NEW
    rationale: A next version of each identity act states them in its bindings.
    alternatives_checked: 'Declaring them on the entry points was checked and rejected: it would make the moment and the trail the caller''s to choose. Amending the acts in place was rejected: identity is fixed at publication.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q1}
    - {phase: p3, register: analysis_findings, key: Q6}
  - capability: State where the contact address sits
    decision: AUTHOR_NEW
    rationale: The registration act's next version states the place and the kind.
    alternatives_checked: 'Declaring them on the entry point was checked and rejected: a caller could point the claim at another field.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: State a new wallet's record, prefix and moment
    decision: AUTHOR_NEW
    rationale: The wallet act's next version states them, and reads the holder from the person it resolved.
    alternatives_checked: 'Checking the request''s values against fixed ones was checked and rejected: a value only the business may decide is never taken from a request, so there is nothing to check.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q3}
    - {phase: p3, register: analysis_findings, key: Q4}
  - capability: Stop the entrances sending what the acts state
    decision: AUTHOR_NEW
    rationale: A next version of each identity entrance sends only what the caller supplies.
    alternatives_checked: 'Leaving the entrances as they are was checked and rejected by the business: they would send values nothing reads.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Leave records made before this change in place
    decision: REUSE
    rationale: Nothing rewrites what an act recorded.
    alternatives_checked: 'A backfill was checked and rejected: the business adds to its record and does not rewrite it.'
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
  placement_decision:
  - decision: EXTEND
    subdomain: identity
    rationale: The three identity acts and their entrances are identity's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - decision: EXTEND
    subdomain: wallet
    rationale: The wallet act and its entry point are wallet's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: Both CRITICAL gaps resolve to acts that state their own values
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All ten findings are CLOSED. The business answered the three open questions at the seed
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass followed the retired acts to the stood-down acts naming them and added four, then the stood-down act and entry point naming those, and added two; a third pass over every referrer found nothing further
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All fifteen items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED; the wallet record was established by running the act against the pinned composition
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: which values the business decides and which the caller
supplies. The business answered it at the seed: what only the business may decide, its act states.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
