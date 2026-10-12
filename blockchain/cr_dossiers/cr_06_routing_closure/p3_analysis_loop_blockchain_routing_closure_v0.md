# Stage 3 — Analysis Loop: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'Five steps omit BACKEND_ERROR, which their stores declare: the lookup and the read in blockchain::CC_RESOLVE_ACTOR_V0, the claim in blockchain::CC_CLAIM_WALLET_IDENTITY_V0, the write in blockchain::CC_CREATE_WALLET_RECORD_V0 and the append in blockchain::CC_APPEND_WALLET_OCCURRENCE_V0. Each step gains BACKEND_ERROR, and ends its contract with it.'
    impact: Four contracts change. No step is added, and every other answer stays.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #2 and #3'
  - question_id: Q2
    finding: Ending the contract is the only answer the business allows. Carrying on would read or write after a failed record, which the seed forbids, and nothing retries.
    impact: 'Every one of the five answers is the same: end the contract with BACKEND_ERROR.'
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 known_facts #4; S1 requested_outcomes #2'
  - question_id: Q3
    finding: Thirteen act nodes run a contract that ends, or after Q1 will end, with BACKEND_ERROR, and none routes it. Each routes it to EXIT_REJECTED, the ending every act already has.
    impact: Four acts change. No ending is added.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #1 and #4; S1 known_facts #5'
  - question_id: Q4
    finding: 'Two contracts gain BACKEND_ERROR as a way to end: blockchain::CC_RESOLVE_ACTOR_V0 and blockchain::CC_CLAIM_WALLET_IDENTITY_V0. The other two already end with it, through their clock step. Each contract''s declared outcomes gain it.'
    impact: The contracts state every outcome they can end with.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 architectural_observations #1'
  - question_id: Q5
    finding: A record made before a failure stays as it was. A registration whose trail append fails has recorded the person. The act ends as rejected, and nothing removes that record.
    impact: No repair, no backfill, no compensation step.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #2; S2 discovery_concerns #1'
  - question_id: Q6
    finding: The superseded act blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is not dispatched, so no request reaches its unrouted nodes. It is left as it is.
    impact: Nothing superseded changes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 discovery_concerns #2'
  - question_id: Q7
    finding: An act whose records are all read and written takes exactly the route it takes today. Each change adds an answer for BACKEND_ERROR and touches no other answer.
    impact: Nothing a caller sees changes unless a record fails.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #1'
  - question_id: Q8
    finding: 'Each of the eight acts changes what it means: four contracts gain answers for a failed record, and four acts gain routes for it. Each is published in v5, so each is stated under a new version, and the published one stays in the record, stood down, as v5 published it.'
    impact: A citation of v5 still names what v5 said.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #5; S2 gaps #3'
  - question_id: Q9
    finding: The three entrances and four intents that start an act are re-pointed to its new version, each in the one part that names it. The acts that run a replaced contract are replaced themselves, so their places name the new contract and keep their labels. blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is stood down and is not re-pointed.
    impact: Every caller starts the same act as today, under its new version.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #6; S2 gaps #4; S2 architectural_observations #5'
  verification_results:
  - item: Most identity and wallet acts stop without a declared ending when a record fails.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: When an acceptance's lookup of the person fails, identity carries on and records the acceptance.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q2
  - item: Three of wallet's steps carry on past a failed record in the same way.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q1; Stage 2 found five steps in all, two of them identity's
  - item: Each act already has a rejected ending.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: Five steps carry on past a failed record.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q2
  - item: Thirteen act nodes leave a failed record without a declared ending.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q3 and Q4
  - item: An act that fails after recording something leaves that record in place.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q5
  - item: A superseded act carries the same gap.
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q6
  - item: Every identity and wallet act this change touches was published in v5.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q8
  - item: Entrances and intents name the workflows they start, and workflows name the contracts they run.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: Resolved in Q9
  - item: Eight published acts would mean something v5 did not say if changed in place.
    origin: {phase: p2, register: gaps, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q8
  - item: Seven entrances and intents name the published acts.
    origin: {phase: p2, register: gaps, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q9
  dependency_discoveries:
  - dependency: Looking a person up
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: blockchain::CC_RESOLVE_ACTOR_V0 is replaced by its next version, which answers for a failed lookup and a failed read
  - dependency: Claiming a wallet's identity
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: blockchain::CC_CLAIM_WALLET_IDENTITY_V0 is replaced by its next version, which answers for a failed claim
  - dependency: Recording a wallet
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: blockchain::CC_CREATE_WALLET_RECORD_V0 is replaced by its next version, which answers for a failed write
  - dependency: Recording a moment on a wallet's trail
    type: Capability contract
    disposition: AUTHOR_NEW
    evidence: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 is replaced by its next version, which answers for a failed append
  - dependency: The four acts
    type: Workflows
    disposition: AUTHOR_NEW
    evidence: blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0 are each replaced by a next version that routes a failed record to EXIT_REJECTED
  - dependency: The stores
    type: Platform capabilities
    disposition: REUSE
    evidence: capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_MUTABLE_JSON_V0 and capability_side_effects::CS_APPENDONLY_JSONL_V0 already declare BACKEND_ERROR, unchanged
  - dependency: The contracts that already answer for a failed record
    type: Capability contracts
    disposition: REUSE
    evidence: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_REGISTER_ACTOR_V0, blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 and blockchain::CC_RECORD_VERIFICATION_DECISION_V0, unchanged
  - dependency: The entrances and intents
    type: Transport contracts and intents
    disposition: EXISTING
    evidence: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0, each re-pointed to the act's next version
  impact_analysis:
  - artifact: blockchain::CC_RESOLVE_ACTOR_V0
    impact_scope: Stood down and replaced by its next version — two steps end on a failed record
    consumer_count: '9'
    evidence: si.topology.impact impacted_count 9
  - artifact: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    impact_scope: Stood down and replaced by its next version — its step ends on a failed claim
    consumer_count: '12'
    evidence: si.topology.impact impacted_count 12
  - artifact: blockchain::CC_CREATE_WALLET_RECORD_V0
    impact_scope: Stood down and replaced by its next version — its write step ends on a failed write
    consumer_count: '14'
    evidence: si.topology.impact impacted_count 14
  - artifact: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    impact_scope: Stood down and replaced by its next version — its append step ends on a failed append
    consumer_count: '15'
    evidence: si.topology.impact impacted_count 15
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    impact_scope: Stood down and replaced by its next version — three nodes route a failed record
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    impact_scope: Stood down and replaced by its next version — three nodes route a failed record
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    impact_scope: Stood down and replaced by its next version — three nodes route a failed record
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_CREATE_WALLET_V0
    impact_scope: Stood down and replaced by its next version — four nodes route a failed record
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  authoring_decisions:
  - capability: Stop a lookup at a failed record
    decision: AUTHOR_NEW
    rationale: A next version of the lookup, whose lookup and read each end the contract when their record fails.
    alternatives_checked: 'Carrying on was checked and rejected: it is the failure this change closes. Amending the published lookup in place was rejected: it changes what a published act means.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q1}
    - {phase: p3, register: analysis_findings, key: Q8}
  - capability: Stop a wallet step at a failed record
    decision: AUTHOR_NEW
    rationale: Next versions of the three wallet contracts, whose claim, write and append each end the contract when their record fails.
    alternatives_checked: 'Retrying was checked and rejected by the business. Amending in place was rejected: it changes what a published act means.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q2}
    - {phase: p3, register: analysis_findings, key: Q8}
  - capability: End every act as rejected on a failed record
    decision: AUTHOR_NEW
    rationale: A next version of each act routes a failed record to its rejected ending, and its entrances and intents are re-pointed to it.
    alternatives_checked: 'A separate failure ending was checked and deferred by the business: it keeps two endings. Amending in place was rejected: it changes what a published act means.'
    source_finding:
    - {phase: p3, register: analysis_findings, key: Q3}
    - {phase: p3, register: analysis_findings, key: Q9}
  - capability: Leave records made before a failure in place
    decision: REUSE
    rationale: Nothing removes what an act recorded before it failed.
    alternatives_checked: 'A compensation step was checked and rejected: the business adds to its record and does not rewrite it.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  placement_decision:
  - decision: EXTEND
    subdomain: identity
    rationale: The lookup and three acts are identity's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  - decision: EXTEND
    subdomain: wallet
    rationale: Three wallet contracts and the wallet act are wallet's own.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: The one CRITICAL gap resolves to five steps that end on a failed record
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All seven findings are CLOSED. The business answered the only question, where a failed record ends, at the seed
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass followed the step changes into the acts and added the two contracts that newly end with BACKEND_ERROR; a third pass over every node of the four acts found nothing further
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All eight items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED; the failed lookup was established by running the acceptance against the pinned composition
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each failed record goes. The business answered
it at the seed: a failed record ends the act as rejected, at the step whose record failed.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
