# Change Seed — ai_governance / ai_licensing

**Stage:** 0 — Change Seed
**CR:** cr_01_licensing
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
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
| ai_licensing | MODIFY | The three checks are built and run. Nothing proves them; cases are stated beside each so that every build proves it. What each check decides does not change. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Check | One of the three decisions: whether a license is available, whether an employee is eligible, whether a license is inactive. |
| Case | What a check is given, and what it must answer or that it must refuse. |
| Cap | The number of licenses the business allows to be assigned. |
| Threshold | The number of days a license may go unused before it is reclaimed. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Beside each of the three checks are the cases that prove it: a case it admits, with what it answers, and a case it refuses. |
| The cases are the ones the business already had, restated to expect a refusal where the answer is no, and to use this system's names. |
| What each check decides, and every act that uses them, is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A check whose answer is no refuses. | HIGH |
| A license is available while fewer are assigned than the cap. At the cap, none is. | HIGH |
| An employee is eligible once their required training is complete. | HIGH |
| A license is inactive once it has gone unused for the threshold of days or more. | HIGH |
| The earlier cases expect a no answer where this system refuses. | HIGH |
| The earlier cases' no case becomes a refusal case, and the yes case keeps its answer. | HIGH |
| The earlier cases keep their values under this system's names. | HIGH |
| A license unused for exactly the threshold is inactive, and is proven as a case. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| None of the three checks is proven. | A check nothing proves can change what it decides without anyone seeing. | Establish whether each check carries cases that every build runs. |
| Each check refuses when its answer is no. | The cases must expect what the check does. | Establish what each check does with a no answer. |
| The earlier cases name the inactivity check's evaluation date and the training check's answer differently from this system. | A case naming what a check does not take or give proves nothing. | Establish the names each check takes and gives. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| What each check decides, and every act that uses them, is unchanged. | Business author |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No check answers no; a no is a refusal. |
| Every check is proven on every build by the cases stated beside it. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Check | Proven | Its cases are stated beside it and hold on every build. |
| Check | Unproven | Nothing states what it must answer. This change ends that state for all three. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | | This change announces nothing new. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| The three checks and their cases | AI Licensing |
| The cap, the training required and the threshold | The acts that use the checks |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| The cap, the training required and the threshold | Each is stated by the act that uses the check, and none changes. |
| The agent_governance subdomain | Not this change. |

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
| Each of the three checks is proven on every build. |
| A license check with fewer assigned than the cap answers that one is available, with how many remain; at the cap it refuses. |
| A training check for an employee with training complete answers that they are eligible; without it, it refuses. |
| An inactivity check for a license unused for the threshold or more answers that it is inactive, with how many days; for one used more recently, it refuses. |
| Every act that uses the checks behaves as it did before this change. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Check | Unproven | Proven | Its cases being stated beside it | None. |

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
