# Change Seed — ai_governance / reclaim and parameter result

**Stage:** 0 — Change Seed
**CR:** cr_02_reclaim_and_parameters
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
employee, and reclaiming a license that has gone unused for the business's threshold of days. The
Agent Governance subdomain governs what an AI agent may do on the business's behalf: it judges an
agent's proposed action, checks its parameters against the rules declared for the tool, and records
every action it authorizes or denies. This change decides what a reclaim does when the registry
refuses it and what the parameter check reports, and states each act it changes under a new identity.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| ai_licensing | MODIFY | A reclaim does not say what happens when the license registry refuses to remove an assignment. Nothing is added to what a reclaim does. |
| agent_governance | MODIFY | The parameter check reports a result it never receives. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Reclaim | Taking back a license that has gone unused for the business's threshold of days. |
| Assignment | The registry's record that a license belongs to an employee. |
| Refused removal | The registry's answer to a malformed request to remove an assignment. |
| Governed action | An agent's proposed action, judged and recorded by the business. |
| Parameter check | The step that checks an action's parameters against the rules declared for its tool. |
| Parameter result | What the parameter check reports: whether every declared rule passed. |
| Published | Sealed into a composition that was released and cited. |
| Successor | The new identity that states what an act does after this change. |
| Stood down | Replaced by a declared successor, kept in the record and out of reach. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A reclaim the registry refuses ends with the license left assigned. |
| The parameter check reports whether every declared rule passed. |
| Each act whose meaning this changes has a successor, and its published identity is stood down unchanged. |
| Everything in force that runs a stood-down act runs its successor. |
| Every other reclaim, and every governed action, decides as it does today. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A reclaim ends as reclaimed, still active, or in error. | HIGH |
| A license the registry did not release stays with the employee. | HIGH |
| A reclaim the registry refused ends as still active. | HIGH |
| A parameter that breaks a declared rule denies the action. | HIGH |
| The check underneath answers only whether every rule passed; a broken rule denies the action. | HIGH |
| Nothing reads the parameter result today. | HIGH |
| Identity is fixed at publication; a change of meaning is a new identity. | HIGH |
| A published identity stays in the record, stood down, when a successor replaces it. | HIGH |
| A re-point changes which act a referrer runs, and nothing else about it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The step that removes an assignment does not answer a refused removal. | An unanswered refusal is carried past. | Establish which answers of the registry the removal step answers. |
| The reclaim already ends as still active for a license that is not inactive. | A refused removal can end there without a new ending. | Establish where the reclaim sends its still-active answer. |
| The parameter check reads its result from a place the check underneath never writes. | The reported result is always empty. | Establish what the check underneath returns and what the parameter check reads. |
| Both acts this change touches were published in v5. | Each one it changes needs a successor. | Establish which touched acts the v5 composition holds. |
| One workflow runs each of the two contracts. | Everything that runs a replaced contract must run its successor. | Establish everything that names each contract, by full name and by short code. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Every reclaim the registry does not refuse ends exactly as it did before this change. | Business author |
| No ending is added. | Business author |
| The governed action decides exactly as it does today. | Business author |
| No published identity changes what it says, except to be stood down. | Business author — identity is fixed at publication. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No reclaim carries on past a removal the registry refused. |
| No license is reported reclaimed that the registry did not release. |
| A check reports only what it receives. |
| A published identity means what it meant when it was published. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| License | Assigned | Held by an employee. Unchanged by this change. |
| License | Reclaimed | Taken back after going unused. Unchanged by this change. |
| Published act | In force | Run when a request reaches it. |
| Published act | Stood down | Replaced by its successor, kept in the record as published. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A license was revoked | When a reclaim removes an assignment | Unchanged; it is not announced when the registry refuses the removal. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a reclaim does when the registry refuses it | AI Licensing |
| The rules declared for each tool | Agent Governance |
| What the check underneath answers | The platform |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Telling a refused removal apart from a license still in use | The business keeps three endings; both leave the license assigned. |
| Provisioning a license | Not this change. |
| Which rules each tool declares | Unchanged. |
| Reporting which rule failed | The check underneath denies rather than returns it. |
| The licence-cap check nothing runs | It stays as v5 published it. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| ai_licensing | MODIFIED |
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
| A reclaim the registry refuses ends as still active, the license stays assigned, and no revocation is announced. |
| Every reclaim the registry does not refuse ends exactly as it did before this change. |
| An action whose parameters satisfy every rule is authorized, and the parameter result says every rule passed. |
| An action whose parameters break a rule is denied and audited, as today. |
| Each act whose meaning this changes is stated under a new identity, and the published identity is unchanged except for its stand-down. |
| Nothing in force runs a stood-down act. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Act | Its identity | Its declaration means what the published declaration meant |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Published act | In force | Stood down | This change adds its successor | Whatever runs it is re-pointed |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Reclaiming a license | The registry refuses to remove the assignment | A license the registry did not release stays with the employee. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
