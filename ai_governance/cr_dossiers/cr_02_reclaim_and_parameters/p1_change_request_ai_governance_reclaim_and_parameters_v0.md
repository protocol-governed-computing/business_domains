# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / reclaim and parameter result
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_02_reclaim_and_parameters
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
| agent_governance | MODIFY | The parameter check reports a result it never receives. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Reclaim | Taking back a license that has gone unused for the business's threshold of days. | CR seed §2 Business Vocabulary #1 |
| Assignment | The registry's record that a license belongs to an employee. | CR seed §2 Business Vocabulary #2 |
| Refused removal | The registry's answer to a malformed request to remove an assignment. | CR seed §2 Business Vocabulary #3 |
| Governed action | An agent's proposed action, judged and recorded by the business. | CR seed §2 Business Vocabulary #4 |
| Parameter check | The step that checks an action's parameters against the rules declared for its tool. | CR seed §2 Business Vocabulary #5 |
| Parameter result | What the parameter check reports: whether every declared rule passed. | CR seed §2 Business Vocabulary #6 |
| Published | Sealed into a composition that was released and cited. | CR seed §2 Business Vocabulary #7 |
| Successor | The new identity that states what an act does after this change. | CR seed §2 Business Vocabulary #8 |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. | CR seed §2 Business Vocabulary #9 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A reclaim the registry refuses ends with the license left assigned. | CR seed §3 Requested Outcomes #1 |
| The parameter check reports whether every declared rule passed. | CR seed §3 Requested Outcomes #2 |
| Each act whose meaning this changes has a successor, and its published identity is stood down unchanged. | CR seed §3 Requested Outcomes #3 |
| Everything in force that runs a stood-down act runs its successor. | CR seed §3 Requested Outcomes #4 |
| Every other reclaim, and every governed action, decides as it does today. | CR seed §3 Requested Outcomes #5 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A reclaim ends as reclaimed, still active, or in error. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A license the registry did not release stays with the employee. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A reclaim the registry refused ends as still active. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A parameter that breaks a declared rule denies the action. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The check underneath answers only whether every rule passed; a broken rule denies the action. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Nothing reads the parameter result today. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Identity is fixed at publication; a change of meaning is a new identity. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A published identity stays in the record, stood down, when a successor replaces it. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A re-point changes which act a referrer runs, and nothing else about it. | HIGH | CR seed §4 Known Facts — Business Truths #9 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The step that removes an assignment does not answer a refused removal. | An unanswered refusal is carried past. | Establish which answers of the registry the removal step answers. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The reclaim already ends as still active for a license that is not inactive. | A refused removal can end there without a new ending. | Establish where the reclaim sends its still-active answer. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The parameter check reads its result from a place the check underneath never writes. | The reported result is always empty. | Establish what the check underneath returns and what the parameter check reads. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Both acts this change touches were published in v5. | Each one it changes needs a successor. | Establish which touched acts the v5 composition holds. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| One workflow runs each of the two contracts. | Everything that runs a replaced contract must run its successor. | Establish everything that names each contract, by full name and by short code. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

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
| The governed action decides exactly as it does today. | Business author | CR seed §7 Constraints #3 |
| No published identity changes what it says, except to be stood down. | Business author — identity is fixed at publication. | CR seed §7 Constraints #4 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No reclaim carries on past a removal the registry refused. | CR seed §8 Business Invariants #1 |
| No license is reported reclaimed that the registry did not release. | CR seed §8 Business Invariants #2 |
| A check reports only what it receives. | CR seed §8 Business Invariants #3 |
| A published identity means what it meant when it was published. | CR seed §8 Business Invariants #4 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| License | Assigned | Held by an employee. Unchanged by this change. | CR seed §9 Lifecycle States #1 |
| License | Reclaimed | Taken back after going unused. Unchanged by this change. | CR seed §9 Lifecycle States #2 |
| Published act | In force | Run when a request reaches it. | CR seed §9 Lifecycle States #3 |
| Published act | Stood down | Replaced by its successor, kept in the record as published. | CR seed §9 Lifecycle States #4 |

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
| The rules declared for each tool | Agent Governance | CR seed §11 Authority Boundaries #2 |
| What the check underneath answers | The platform | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Telling a refused removal apart from a license still in use | The business keeps three endings; both leave the license assigned. | CR seed §12 Out of Scope #1 |
| Provisioning a license | Not this change. | CR seed §12 Out of Scope #2 |
| Which rules each tool declares | Unchanged. | CR seed §12 Out of Scope #3 |
| Reporting which rule failed | The check underneath denies rather than returns it. | CR seed §12 Out of Scope #4 |
| The licence-cap check nothing runs | It stays as v5 published it. | CR seed §12 Out of Scope #5 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| ai_licensing | MODIFIED | CR seed §13 Governance Scope #1 |
| agent_governance | MODIFIED | CR seed §13 Governance Scope #2 |

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
| An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed. | CR seed §15 Acceptance Criteria #3 |
| An action whose parameters break a rule is denied and audited, as today. | CR seed §15 Acceptance Criteria #4 |
| Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down. | CR seed §15 Acceptance Criteria #5 |
| Nothing in force runs a stood-down act. | CR seed §15 Acceptance Criteria #6 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Act | Its identity | Its declaration means what the published declaration meant | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Published act | In force | Stood down | This change adds its successor | Whatever runs it is re-pointed | CR seed §17 Lifecycle Transitions #1 |

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
