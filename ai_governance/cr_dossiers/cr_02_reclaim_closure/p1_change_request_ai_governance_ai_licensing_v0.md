# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / ai_licensing
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_02_reclaim_closure
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
| ai_licensing | MODIFY | A reclaim does not say what happens when the license registry refuses to remove an assignment. Nothing is added to what a reclaim does. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Reclaim | Taking back a license that has gone unused for the business's threshold of days. | CR seed §2 Business Vocabulary #1 |
| Assignment | The registry's record that a license belongs to an employee. | CR seed §2 Business Vocabulary #2 |
| Refused removal | The registry's answer to a malformed request to remove an assignment. | CR seed §2 Business Vocabulary #3 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A reclaim the registry refuses ends with the license left assigned. | CR seed §3 Requested Outcomes #1 |
| Every other reclaim is unchanged. | CR seed §3 Requested Outcomes #2 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A reclaim ends as reclaimed, still active, or in error. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A license the registry did not release stays with the employee. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A reclaim the registry refused ends as still active. | HIGH | CR seed §4 Known Facts — Business Truths #3 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The step that removes an assignment does not answer a refused removal. | An unanswered refusal is carried past. | Establish which answers of the registry the removal step answers. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The reclaim already ends as still active for a license that is not inactive. | A refused removal can end there without a new ending. | Establish where the reclaim sends its still-active answer. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |

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
| Every reclaim the registry does not refuse ends exactly as it did before this change. | Business author | CR seed §7 Constraints #1 |
| No ending is added. | Business author | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No reclaim carries on past a removal the registry refused. | CR seed §8 Business Invariants #1 |
| No license is reported reclaimed that the registry did not release. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| License | Assigned | Held by an employee. Unchanged by this change. | CR seed §9 Lifecycle States #1 |
| License | Reclaimed | Taken back after going unused. Unchanged by this change. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A license was revoked | When a reclaim removes an assignment | Unchanged; it is not announced when the registry refuses the removal. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a reclaim does when the registry refuses it | AI Licensing | CR seed §11 Authority Boundaries #1 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Telling a refused removal apart from a license still in use | The business keeps three endings; both leave the license assigned. | CR seed §12 Out of Scope #1 |
| Provisioning a license | Not this change. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| ai_licensing | MODIFIED | CR seed §13 Governance Scope #1 |
| agent_governance | ADJACENT | CR seed §13 Governance Scope #2 |

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
| A reclaim the registry refuses ends as still active, the license stays assigned, and no revocation is announced. | CR seed §15 Acceptance Criteria #1 |
| Every reclaim the registry does not refuse ends exactly as it did before this change. | CR seed §15 Acceptance Criteria #2 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| NONE IDENTIFIED |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| NONE IDENTIFIED |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Reclaiming a license | The registry refuses to remove the assignment | A license the registry did not release stays with the employee. | CR seed §18 Operation Refusals #1 |

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
