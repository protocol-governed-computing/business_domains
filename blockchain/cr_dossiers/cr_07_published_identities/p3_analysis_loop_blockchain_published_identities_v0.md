# Stage 3 — Analysis Loop: blockchain / published identities

**Stage:** 3 — Analysis Loop

**CR:** cr_07_published_identities

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

The two gaps and one concern carried from Stage 2 are driven to committed decisions against the
pinned composition and v5.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Each of the eight gains a successor, its code ending _V1, determined by cr_06's design with the eight codes renamed: the same steps, routes, bindings and announcements. The successor workflows run the successor contracts. | Each act does what it does today under an identity that says so. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 architectural_observations #3 |
| Q2 | Each published identity is returned to its v5 text and stood down by its successor. The v5 workflows keep naming the v5 contracts; both are out of reach. | v5 means what it published. | OBSERVED | HIGH | CLOSED | S2 gaps #1; S2 architectural_observations #2 |
| Q3 | The three entrances and four intents that start the workflows are re-pointed to the successors. The identity, wallet and routing-closure validations and the runtime's determinism test run the successors. | Nothing in force starts a stood-down act. | OBSERVED | HIGH | CLOSED | S2 gaps #2; S2 belief_verification #3 |
| Q4 | Construction acceptance compares an identity v5 published with what v5 published, and an identity v5 did not publish with the latest design that determines it. A published identity cannot follow a later design; that is the rule this change serves. | The harness checks that published identities are unchanged, and stops reporting book_library's sealed version field as a difference. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns #1 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| Exactly eight published acts of this domain changed meaning since v5, all by cr_06. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q2 |
| Each of the eight differs from v5 only in how a failed record is reported and routed. | S2 belief_verification #2 | CONFIRMED | Resolved in Q1 |
| The four workflows run the four contracts, and are named by the entrances and intents that start them. | S2 belief_verification #3 | CONFIRMED | Resolved in Q3 |
| The domain's design of record states each of the eight fully. | S2 belief_verification #4 | CONFIRMED | Resolved in Q1 |
| Construction acceptance compares each identity with the latest design that determines it. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q4 |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| The four contracts | Capability contract | AUTHOR_NEW | Each replaced by its _V1 successor |
| The four workflows | Workflow | AUTHOR_NEW | Each replaced by its _V1 successor |
| The entrances and intents | Transport ingress, intent | EXISTING | Re-pointed to the successor workflows |
| The rest of the domain | Contracts, events, bindings, structures | REUSE | Named by the successors, unchanged |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Stood down; run by four workflows, three replaced here and one stood down before v5 | 4 | si.artifact.refs |
| blockchain::WF_REGISTER_ACTOR_V0 | Stood down; started by one entrance and one intent | 2 | the domain's declarations, by full name and short code |
| blockchain::WF_ACCEPT_ACTOR_V0 | Stood down; started by one entrance and one intent | 2 | the same |
| blockchain::WF_REJECT_ACTOR_V0 | Stood down; started by one entrance and one intent | 2 | the same |
| blockchain::WF_CREATE_WALLET_V0 | Stood down; started by one intent | 1 | the same |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| State the identity acts | AUTHOR_NEW | Successors of the resolving contract and three identity workflows, as they stand. | Keeping the change under the published identities was rejected: identity is fixed at publication. | S3 analysis_findings Q1 |
| State the wallet acts | AUTHOR_NEW | Successors of three wallet contracts and the wallet workflow, as they stand. | The same. | S3 analysis_findings Q1 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | identity | The identity acts are identity's. | S3 analysis_findings Q1 |
| EXTEND | wallet | The wallet acts are wallet's. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The CRITICAL gap resolves in Q1 and Q2 |
| No open analyst questions | SATISFIED | All four findings are CLOSED |
| No dependency expansion in the last pass | SATISFIED | A search by full name and short code found nothing more |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Every item CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
