# Change Seed — ai_governance / agent_governance

**Stage:** 0 — Change Seed
**CR:** cr_03_parameter_result
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Agent Governance subdomain governs what an AI agent may do on the business's behalf: it accepts an
agent's proposed action, checks that the tool is declared, that the requesting employee holds a
license tier that allows it, and that its parameters satisfy the rules declared for that tool, and
records every action it authorizes or denies. It does not govern which licenses exist, who holds
them, or what a tool does once its action is authorized.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| agent_governance | MODIFY | The parameter check reports a result it never receives. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Governed action | An agent's proposed action, judged and recorded by the business. |
| Parameter check | The step that checks an action's parameters against the rules declared for its tool. |
| Parameter result | What the parameter check reports: whether every declared rule passed. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| The parameter check reports whether every declared rule passed. |
| The new parameter check stands in for the old one, which stays in the record and out of reach. |
| The governed action runs the new parameter check, with its steps, routes and audits unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A parameter that breaks a declared rule denies the action. | HIGH |
| A change of what a check reports is a new version of it. | HIGH |
| The check underneath answers only whether every rule passed; a broken rule denies the action. | HIGH |
| Nothing reads the parameter result today. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The parameter check reads its result from a place the check underneath never writes. | The reported result is always empty. | Establish what the check underneath returns and what the parameter check reads. |
| Only the governed action runs the parameter check. | Everything that runs it must follow the new version. | Establish every artifact that names the parameter check. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The governed action decides exactly as it does today. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A check reports only what it receives. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Parameter check | In force | Run by the governed action. |
| Parameter check | Replaced | Stood down by its new version, kept in the record and out of reach. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The rules declared for each tool | Agent Governance |
| What the check underneath answers | The platform |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Which rules each tool declares | Unchanged. |
| Reporting which rule failed | The check underneath denies rather than returns it. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| agent_governance | MODIFIED |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed. |
| An action whose parameters break a rule is denied and audited, as today. |
| The old parameter check is stood down, and nothing in force reaches it. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Parameter check | In force | Replaced | This change adds its new version | The governed action runs the new version |

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
