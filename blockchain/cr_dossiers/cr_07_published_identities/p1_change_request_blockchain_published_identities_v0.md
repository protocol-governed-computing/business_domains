# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / published identities
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_07_published_identities
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| identity | MODIFY | Four of identity's published acts do what v5 did not say, under the identities v5 published. | CR seed §1 CR Type #1 |
| wallet | MODIFY | Four of wallet's published acts do what v5 did not say, under the identities v5 published. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Published | Sealed into a composition that was released and cited. | CR seed §2 Business Vocabulary #1 |
| Published identity | An identity a released composition holds; what it means is fixed. | CR seed §2 Business Vocabulary #2 |
| Successor | The new identity that states what an act does today. | CR seed §2 Business Vocabulary #3 |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. | CR seed §2 Business Vocabulary #4 |
| Failed record | A record an act needs that cannot be read or written. | CR seed §2 Business Vocabulary #5 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Each of the eight acts has a successor that does what it does today. | CR seed §3 Requested Outcomes #1 |
| Each published identity says again what v5 published, and is stood down. | CR seed §3 Requested Outcomes #2 |
| Everything in force that names one of the eight names its successor. | CR seed §3 Requested Outcomes #3 |
| Every identity and wallet act answers every request exactly as it does today. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| Identity is fixed at publication; an unpublished identity may change before release. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A change of meaning is a new identity, and the old one stays in the record and out of reach. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A failed record ends the act, as cr_06 decided. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| No request gets a different answer, and no stored record is touched. | HIGH | CR seed §4 Known Facts — Business Truths #4 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Exactly eight published acts of this domain changed meaning since v5, all by cr_06. | The change must be the whole of it. | Establish every published identity of the domain whose meaning changed since v5. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Each of the eight differs from v5 only in how a failed record is reported and routed. | The successors must carry that and nothing else. | Establish every difference between each act and what v5 published. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The four workflows run the four contracts, and are named by the entrances and intents that start them. | Each must name a successor. | Establish everything that names any of the eight, by full name and by short code. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The domain's design of record states each of the eight fully. | The successors can be built from it. | Establish which delivered design determines each of the eight. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| NONE IDENTIFIED |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Every identity and wallet act answers every request as it does today. | Business author | CR seed §7 Constraints #1 |
| No published identity changes what it says, except to be stood down. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A published identity means what it meant when it was published. | CR seed §8 Business Invariants #1 |
| A failed record ends the act. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Published act | In force | Run when a request reaches it. | CR seed §9 Lifecycle States #1 |
| Published act | Stood down | Replaced by its successor, kept in the record as published. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What an identity act does | Identity | CR seed §11 Authority Boundaries #1 |
| What a wallet act does | Wallet | CR seed §11 Authority Boundaries #2 |
| What is published, and when | The business author | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What any act does | Settled by cr_06; only its identity changes. | CR seed §12 Out of Scope #1 |
| Acts published in v5 that did not change | They keep their identities. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| identity | MODIFIED | CR seed §13 Governance Scope #1 |
| wallet | MODIFIED | CR seed §13 Governance Scope #2 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| Each successor does what its predecessor does today, and nothing else. | CR seed §15 Acceptance Criteria #1 |
| Each published identity's text is what v5 published, with only its stand-down added. | CR seed §15 Acceptance Criteria #2 |
| Nothing in force names a stood-down act. | CR seed §15 Acceptance Criteria #3 |
| Every identity and wallet request is answered as it is today. | CR seed §15 Acceptance Criteria #4 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Published act | Its identity | Its text is what the release sealed | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Published act | In force | Stood down | This change adds its successor | Whatever names it is re-pointed | CR seed §17 Lifecycle Transitions #1 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| NONE IDENTIFIED |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| NONE IDENTIFIED |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
