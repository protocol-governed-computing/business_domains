# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / ai_licensing
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_01_licensing
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
| ai_licensing | MODIFY | The three checks are built and run. Nothing proves them; cases are stated beside each so that every build proves it. What each check decides does not change. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Check | One of the three decisions: whether a license is available, whether an employee is eligible, whether a license is inactive. | CR seed §2 Business Vocabulary #1 |
| Case | What a check is given, and what it must answer or that it must refuse. | CR seed §2 Business Vocabulary #2 |
| Cap | The number of licenses the business allows to be assigned. | CR seed §2 Business Vocabulary #3 |
| Threshold | The number of days a license may go unused before it is reclaimed. | CR seed §2 Business Vocabulary #4 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Beside each of the three checks are the cases that prove it: a case it admits, with what it answers, and a case it refuses. | CR seed §3 Requested Outcomes #1 |
| The cases are the ones the business already had, restated to expect a refusal where the answer is no, and to use this system's names. | CR seed §3 Requested Outcomes #2 |
| What each check decides, and every act that uses them, is unchanged. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A check whose answer is no refuses. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A license is available while fewer are assigned than the cap. At the cap, none is. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| An employee is eligible once their required training is complete. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A license is inactive once it has gone unused for the threshold of days or more. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The earlier cases expect a no answer where this system refuses. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| The earlier cases' no case becomes a refusal case, and the yes case keeps its answer. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The earlier cases keep their values under this system's names. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A license unused for exactly the threshold is inactive, and is proven as a case. | HIGH | CR seed §4 Known Facts — Business Truths #8 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| None of the three checks is proven. | A check nothing proves can change what it decides without anyone seeing. | Establish whether each check carries cases that every build runs. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Each check refuses when its answer is no. | The cases must expect what the check does. | Establish what each check does with a no answer. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system. | A case naming what a check does not take or give proves nothing. | Establish the names each check takes and gives. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |

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
| What each check decides, and every act that uses them, is unchanged. | Business author | CR seed §7 Constraints #1 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No check answers no; a no is a refusal. | CR seed §8 Business Invariants #1 |
| Every check is proven on every build by the cases stated beside it. | CR seed §8 Business Invariants #2 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Check | Proven | Its cases are stated beside it and hold on every build. | CR seed §9 Lifecycle States #1 |
| Check | Unproven | Nothing states what it must answer. This change ends that state for all three. | CR seed §9 Lifecycle States #2 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED |  | This change announces nothing new. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| The three checks and their cases | AI Licensing | CR seed §11 Authority Boundaries #1 |
| The cap, the training required and the threshold | The acts that use the checks | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| The cap, the training required and the threshold | Each is stated by the act that uses the check, and none changes. | CR seed §12 Out of Scope #1 |
| The agent_governance subdomain | Not this change. | CR seed §12 Out of Scope #2 |

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
| Each of the three checks is proven on every build. | CR seed §15 Acceptance Criteria #1 |
| A license check with fewer assigned than the cap answers that one is available, with how many remain; at the cap it refuses. | CR seed §15 Acceptance Criteria #2 |
| A training check for an employee with training complete answers that they are eligible; without it, it refuses. | CR seed §15 Acceptance Criteria #3 |
| An inactivity check for a license unused for the threshold or more answers that it is inactive, with how many days; for one used more recently, it refuses. | CR seed §15 Acceptance Criteria #4 |
| Every act that uses the checks behaves as it did before this change. | CR seed §15 Acceptance Criteria #5 |

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
| Check | Unproven | Proven | Its cases being stated beside it | None. | CR seed §17 Lifecycle Transitions #1 |

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
