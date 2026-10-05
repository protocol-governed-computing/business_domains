# Stage 1 — Change Request: Clarification & Fact Capture: ai_governance / agent_governance
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_03_parameter_result
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
| agent_governance | MODIFY | The parameter check reports a result it never receives. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Governed action | An agent's proposed action, judged and recorded by the business. | CR seed §2 Business Vocabulary #1 |
| Parameter check | The step that checks an action's parameters against the rules declared for its tool. | CR seed §2 Business Vocabulary #2 |
| Parameter result | What the parameter check reports: whether every declared rule passed. | CR seed §2 Business Vocabulary #3 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| The parameter check reports whether every declared rule passed. | CR seed §3 Requested Outcomes #1 |
| The new parameter check stands in for the old one, which stays in the record and out of reach. | CR seed §3 Requested Outcomes #2 |
| The governed action runs the new parameter check, with its steps, routes and audits unchanged. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A parameter that breaks a declared rule denies the action. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A change of what a check reports is a new version of it. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The check underneath answers only whether every rule passed; a broken rule denies the action. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| Nothing reads the parameter result today. | HIGH | CR seed §4 Known Facts — Business Truths #4 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The parameter check reads its result from a place the check underneath never writes. | The reported result is always empty. | Establish what the check underneath returns and what the parameter check reads. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Only the governed action runs the parameter check. | Everything that runs it must follow the new version. | Establish every artifact that names the parameter check. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |

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
| The governed action decides exactly as it does today. | Business author | CR seed §7 Constraints #1 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A check reports only what it receives. | CR seed §8 Business Invariants #1 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Parameter check | In force | Run by the governed action. | CR seed §9 Lifecycle States #1 |
| Parameter check | Replaced | Stood down by its new version, kept in the record and out of reach. | CR seed §9 Lifecycle States #2 |

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
| The rules declared for each tool | Agent Governance | CR seed §11 Authority Boundaries #1 |
| What the check underneath answers | The platform | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Which rules each tool declares | Unchanged. | CR seed §12 Out of Scope #1 |
| Reporting which rule failed | The check underneath denies rather than returns it. | CR seed §12 Out of Scope #2 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| agent_governance | MODIFIED | CR seed §13 Governance Scope #1 |

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
| An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed. | CR seed §15 Acceptance Criteria #1 |
| An action whose parameters break a rule is denied and audited, as today. | CR seed §15 Acceptance Criteria #2 |
| The old parameter check is stood down, and nothing in force reaches it. | CR seed §15 Acceptance Criteria #3 |

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
| Parameter check | In force | Replaced | This change adds its new version | The governed action runs the new version | CR seed §17 Lifecycle Transitions #1 |

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
