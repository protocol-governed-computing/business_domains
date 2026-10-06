# Stage 3 — Analysis Loop: blockchain / identity and wallet

**Stage:** 3 — Analysis Loop

**CR:** cr_06_routing_closure

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each failed record goes. The business answered
it at the seed: a failed record ends the act as rejected, at the step whose record failed.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Five steps omit BACKEND_ERROR, which their stores declare: the lookup and the read in blockchain::CC_RESOLVE_ACTOR_V0, the claim in blockchain::CC_CLAIM_WALLET_IDENTITY_V0, the write in blockchain::CC_CREATE_WALLET_RECORD_V0 and the append in blockchain::CC_APPEND_WALLET_OCCURRENCE_V0. Each step gains BACKEND_ERROR, and ends its contract with it. | Four contracts change. No step is added, and every other answer stays. | OBSERVED | HIGH | CLOSED | S2 belief_verification #2 and #3 |
| Q2 | Ending the contract is the only answer the business allows. Carrying on would read or write after a failed record, which the seed forbids, and nothing retries. | Every one of the five answers is the same: end the contract with BACKEND_ERROR. | OBSERVED | HIGH | CLOSED | S1 known_facts #4; S1 requested_outcomes #2 |
| Q3 | Thirteen act nodes run a contract that ends, or after Q1 will end, with BACKEND_ERROR, and none routes it. Each routes it to EXIT_REJECTED, the ending every act already has. | Four acts change. No ending is added. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 and #4; S1 known_facts #5 |
| Q4 | Two contracts gain BACKEND_ERROR as a way to end: blockchain::CC_RESOLVE_ACTOR_V0 and blockchain::CC_CLAIM_WALLET_IDENTITY_V0. The other two already end with it, through their clock step. Each contract's declared outcomes gain it. | The contracts state every outcome they can end with. | OBSERVED | HIGH | CLOSED | S2 architectural_observations #1 |
| Q5 | A record made before a failure stays as it was. A registration whose trail append fails has recorded the person. The act ends as rejected, and nothing removes that record. | No repair, no backfill, no compensation step. | OBSERVED | HIGH | CLOSED | S1 constraints #2; S2 discovery_concerns #1 |
| Q6 | The superseded act blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is not dispatched, so no request reaches its unrouted nodes. It is left as it is. | Nothing superseded changes. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #2 |
| Q7 | An act whose records are all read and written takes exactly the route it takes today. Each change adds an answer for BACKEND_ERROR and touches no other answer. | Nothing a caller sees changes unless a record fails. | OBSERVED | HIGH | CLOSED | S1 constraints #1 |
| Q8 | Each of the eight acts changes what it means: four contracts gain answers for a failed record, and four acts gain routes for it. Each is published in v5, so each is stated under a new version, and the published one stays in the record, stood down, as v5 published it. | A citation of v5 still names what v5 said. | OBSERVED | HIGH | CLOSED | S2 belief_verification #5; S2 gaps #3 |
| Q9 | The three entrances and four intents that start an act are re-pointed to its new version, each in the one part that names it. The acts that run a replaced contract are replaced themselves, so their places name the new contract and keep their labels. blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is stood down and is not re-pointed. | Every caller starts the same act as today, under its new version. | OBSERVED | HIGH | CLOSED | S2 belief_verification #6; S2 gaps #4; S2 architectural_observations #5 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Most identity and wallet acts stop without a declared ending when a record fails. | S2 belief_verification #1 | CONFIRMED | Resolved in Q3 |
| When an acceptance's lookup of the person fails, identity carries on and records the acceptance. | S2 belief_verification #2 | CONFIRMED | Resolved in Q1 and Q2 |
| Three of wallet's steps carry on past a failed record in the same way. | S2 belief_verification #3 | CONFIRMED | Resolved in Q1; Stage 2 found five steps in all, two of them identity's |
| Each act already has a rejected ending. | S2 belief_verification #4 | CONFIRMED | Resolved in Q3 |
| Five steps carry on past a failed record. | S2 gaps #1 | CONFIRMED | Resolved in Q1 and Q2 |
| Thirteen act nodes leave a failed record without a declared ending. | S2 gaps #2 | CONFIRMED | Resolved in Q3 and Q4 |
| An act that fails after recording something leaves that record in place. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q5 |
| A superseded act carries the same gap. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q6 |
| Every identity and wallet act this change touches was published in v5. | S2 belief_verification #5 | CONFIRMED | Resolved in Q8 |
| Entrances and intents name the workflows they start, and workflows name the contracts they run. | S2 belief_verification #6 | CONFIRMED | Resolved in Q9 |
| Eight published acts would mean something v5 did not say if changed in place. | S2 gaps #3 | CONFIRMED | Resolved in Q8 |
| Seven entrances and intents name the published acts. | S2 gaps #4 | CONFIRMED | Resolved in Q9 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Looking a person up | Capability contract | AUTHOR_NEW | blockchain::CC_RESOLVE_ACTOR_V0 is replaced by its next version, which answers for a failed lookup and a failed read |
| Claiming a wallet's identity | Capability contract | AUTHOR_NEW | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 is replaced by its next version, which answers for a failed claim |
| Recording a wallet | Capability contract | AUTHOR_NEW | blockchain::CC_CREATE_WALLET_RECORD_V0 is replaced by its next version, which answers for a failed write |
| Recording a moment on a wallet's trail | Capability contract | AUTHOR_NEW | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 is replaced by its next version, which answers for a failed append |
| The four acts | Workflows | AUTHOR_NEW | blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0 are each replaced by a next version that routes a failed record to EXIT_REJECTED |
| The stores | Platform capabilities | REUSE | capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_MUTABLE_JSON_V0 and capability_side_effects::CS_APPENDONLY_JSONL_V0 already declare BACKEND_ERROR, unchanged |
| The contracts that already answer for a failed record | Capability contracts | REUSE | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_REGISTER_ACTOR_V0, blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 and blockchain::CC_RECORD_VERIFICATION_DECISION_V0, unchanged |
| The entrances and intents | Transport contracts and intents | EXISTING | blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0, blockchain::TI_REJECT_ACTOR_V0, blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0, each re-pointed to the act's next version |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Stood down and replaced by its next version — two steps end on a failed record | 9 | si.topology.impact impacted_count 9 |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Stood down and replaced by its next version — its step ends on a failed claim | 12 | si.topology.impact impacted_count 12 |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | Stood down and replaced by its next version — its write step ends on a failed write | 14 | si.topology.impact impacted_count 14 |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Stood down and replaced by its next version — its append step ends on a failed append | 15 | si.topology.impact impacted_count 15 |
| blockchain::WF_REGISTER_ACTOR_V0 | Stood down and replaced by its next version — three nodes route a failed record | 0 | si.topology.impact impacted_count 0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | Stood down and replaced by its next version — three nodes route a failed record | 0 | si.topology.impact impacted_count 0 |
| blockchain::WF_REJECT_ACTOR_V0 | Stood down and replaced by its next version — three nodes route a failed record | 0 | si.topology.impact impacted_count 0 |
| blockchain::WF_CREATE_WALLET_V0 | Stood down and replaced by its next version — four nodes route a failed record | 0 | si.topology.impact impacted_count 0 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Stop a lookup at a failed record | AUTHOR_NEW | A next version of the lookup, whose lookup and read each end the contract when their record fails. | Carrying on was checked and rejected: it is the failure this change closes. Amending the published lookup in place was rejected: it changes what a published act means. | S3 analysis_findings Q1; S3 analysis_findings Q8 |
| Stop a wallet step at a failed record | AUTHOR_NEW | Next versions of the three wallet contracts, whose claim, write and append each end the contract when their record fails. | Retrying was checked and rejected by the business. Amending in place was rejected: it changes what a published act means. | S3 analysis_findings Q2; S3 analysis_findings Q8 |
| End every act as rejected on a failed record | AUTHOR_NEW | A next version of each act routes a failed record to its rejected ending, and its entrances and intents are re-pointed to it. | A separate failure ending was checked and deferred by the business: it keeps two endings. Amending in place was rejected: it changes what a published act means. | S3 analysis_findings Q3; S3 analysis_findings Q9 |
| Leave records made before a failure in place | REUSE | Nothing removes what an act recorded before it failed. | A compensation step was checked and rejected: the business adds to its record and does not rewrite it. | S3 analysis_findings Q5 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | identity | The lookup and three acts are identity's own. | S3 analysis_findings Q1 |
| EXTEND | wallet | Three wallet contracts and the wallet act are wallet's own. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap resolves to five steps that end on a failed record |
| No open analyst questions | SATISFIED | All seven findings are CLOSED. The business answered the only question, where a failed record ends, at the seed |
| No dependency expansion in the last pass | SATISFIED | A second pass followed the step changes into the acts and added the two contracts that newly end with BACKEND_ERROR; a third pass over every node of the four acts found nothing further |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All eight items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED; the failed lookup was established by running the acceptance against the pinned composition |
