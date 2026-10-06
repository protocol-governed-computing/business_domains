# Change Seed — blockchain / published identities

**Stage:** 0 — Change Seed
**CR:** cr_07_published_identities
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
subdomain governs the wallet an accepted person is given. Both keep records the business relies on:
the person's record, the address they claimed, the trail of moments in their history, and their
wallet. This change decides under which identities their acts are stated, and changes nothing they do.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| identity | MODIFY | Four of identity's published acts do what v5 did not say, under the identities v5 published. |
| wallet | MODIFY | Four of wallet's published acts do what v5 did not say, under the identities v5 published. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Published | Sealed into a composition that was released and cited. |
| Published identity | An identity a released composition holds; what it means is fixed. |
| Successor | The new identity that states what an act does today. |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. |
| Failed record | A record an act needs that cannot be read or written. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Each of the eight acts has a successor that does what it does today. |
| Each published identity says again what v5 published, and is stood down. |
| Everything in force that names one of the eight names its successor. |
| Every identity and wallet act answers every request exactly as it does today. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| Identity is fixed at publication; an unpublished identity may change before release. | HIGH |
| A change of meaning is a new identity, and the old one stays in the record and out of reach. | HIGH |
| A failed record ends the act, as cr_06 decided. | HIGH |
| No request gets a different answer, and no stored record is touched. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Exactly eight published acts of this domain changed meaning since v5, all by cr_06. | The change must be the whole of it. | Establish every published identity of the domain whose meaning changed since v5. |
| Each of the eight differs from v5 only in how a failed record is reported and routed. | The successors must carry that and nothing else. | Establish every difference between each act and what v5 published. |
| The four workflows run the four contracts, and are named by the entrances and intents that start them. | Each must name a successor. | Establish everything that names any of the eight, by full name and by short code. |
| The domain's design of record states each of the eight fully. | The successors can be built from it. | Establish which delivered design determines each of the eight. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every identity and wallet act answers every request as it does today. | Business author |
| No published identity changes what it says, except to be stood down. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A published identity means what it meant when it was published. |
| A failed record ends the act. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Published act | In force | Run when a request reaches it. |
| Published act | Stood down | Replaced by its successor, kept in the record as published. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What an identity act does | Identity |
| What a wallet act does | Wallet |
| What is published, and when | The business author |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| What any act does | Settled by cr_06; only its identity changes. |
| Acts published in v5 that did not change | They keep their identities. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| identity | MODIFIED |
| wallet | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Each successor does what its predecessor does today, and nothing else. |
| Each published identity's text is what v5 published, with only its stand-down added. |
| Nothing in force names a stood-down act. |
| Every identity and wallet request is answered as it is today. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Published act | Its identity | Its text is what the release sealed |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Published act | In force | Stood down | This change adds its successor | Whatever names it is re-pointed |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| NONE IDENTIFIED | | |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
