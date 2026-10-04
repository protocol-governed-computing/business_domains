# Change Seed — ai_governance / ai_licensing

**Stage:** 0 — Change Seed
**CR:** cr_02_reclaim_closure
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarification its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
employee while licenses remain under the business's cap and once the employee has completed the
required training, and reclaiming a license that has gone unused for the business's threshold of
days. Each of its checks refuses when its answer is no. It does not govern what an agent may do,
which employees exist, or which tools the business licenses.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| ai_licensing | MODIFY | A reclaim does not say what happens when the license registry refuses to remove an assignment. Nothing is added to what a reclaim does. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Reclaim | Taking back a license that has gone unused for the business's threshold of days. |
| Assignment | The registry's record that a license belongs to an employee. |
| Refused removal | The registry's answer to a malformed request to remove an assignment. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A reclaim the registry refuses ends with the license left assigned. |
| Every other reclaim is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A reclaim ends as reclaimed, still active, or in error. | HIGH |
| A license the registry did not release stays with the employee. | HIGH |
| A reclaim the registry refused ends as still active. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The step that removes an assignment does not answer a refused removal. | An unanswered refusal is carried past. | Establish which answers of the registry the removal step answers. |
| The reclaim already ends as still active for a license that is not inactive. | A refused removal can end there without a new ending. | Establish where the reclaim sends its still-active answer. |

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

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No reclaim carries on past a removal the registry refused. |
| No license is reported reclaimed that the registry did not release. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| License | Assigned | Held by an employee. Unchanged by this change. |
| License | Reclaimed | Taken back after going unused. Unchanged by this change. |

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

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Telling a refused removal apart from a license still in use | The business keeps three endings; both leave the license assigned. |
| Provisioning a license | Not this change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| ai_licensing | MODIFIED |
| agent_governance | ADJACENT |

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

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| NONE IDENTIFIED | | | | |

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
