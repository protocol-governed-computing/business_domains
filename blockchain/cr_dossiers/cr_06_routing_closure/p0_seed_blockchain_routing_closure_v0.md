# Change Seed — blockchain / identity and wallet

**Stage:** 0 — Change Seed
**CR:** cr_06_routing_closure
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
wallet. This change decides what every identity and wallet act does when one of those records cannot
be read or written.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| identity | MODIFY | Identity's acts do not say what happens when a record fails, and one carries on past a failed lookup. Nothing is added to what identity does. |
| wallet | MODIFY | Wallet's act does not say what happens when a record fails, and three of its steps carry on past a failure. Nothing is added to what wallet does. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Record | Something the business keeps: a person's record, a claimed address, a trail of moments, or a wallet. |
| Failed record | A record that could not be read or written, because the store was unreachable or answered with an error. |
| Act | One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet. |
| Rejected | The ending of an act that did not succeed. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Every identity and wallet act ends as rejected when a record it needs fails. |
| An act stops at the step whose record failed, and nothing after it runs. |
| Everything else identity and wallet do is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| An act either succeeds or is rejected. There is no third ending. | HIGH |
| A rejection changes no record. | HIGH |
| The business adds to its record and does not rewrite it. | HIGH |
| A failed record ends the act. Nothing retries. | HIGH |
| A failed record ends as rejected, not as a separate failure. | HIGH |
| Every identity and wallet act reads or writes a record the business keeps. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| Most identity and wallet acts stop without a declared ending when a record fails. | The caller cannot tell an intended refusal from an unplanned failure. | Establish, for each act, what happens when each record it touches fails. |
| When an acceptance's lookup of the person fails, identity carries on and records the acceptance. | This is the failure the business wants closed first. | Establish what identity does when the lookup fails during an acceptance. |
| Three of wallet's steps carry on past a failed record in the same way. | The same gap, in the same form, in the other subdomain. | Establish which wallet steps carry on past a failed record. |
| Each act already has a rejected ending. | The change can end a failed record there without adding an ending. | Confirm every identity and wallet act has a rejected ending. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Nothing changes for an act whose records are all read and written. | Business author |
| Records made before a failure stay as they were made. | Business author — the record is added to, never rewritten. |
| No ending is added. | Business author — a failure ends as rejected. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No act carries on past a record it could not read or write. |
| Every act ends as succeeded or rejected. |
| A refusal changes no record. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Person | Unverified | Registered, and not yet decided about. Unchanged by this change. |
| Person | Accepted | An authority recorded an acceptance. Unchanged by this change. |
| Person | Rejected | An authority recorded a rejection, with its grounds. Unchanged by this change. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A person was registered | When a person supplies a complete registration and every record is written | Unchanged; it is not announced when a record fails. |
| A person was accepted | When an authority records an acceptance and every record is written | Unchanged; it is not announced when a record fails. |
| A person was rejected | When an authority records a rejection and every record is written | Unchanged; it is not announced when a record fails. |
| A wallet was created | When an accepted person is given a wallet and every record is written | Unchanged; it is not announced when a record fails. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What an identity act does when a record fails | Identity |
| What a wallet act does when a record fails | Wallet |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Telling a refusal apart from a failure | A later decision; the business keeps two endings. |
| Trying a failed record again | The business decided a failed record ends the act. |
| Records made before a failure | The business adds to its record and does not rewrite it. |
| The other five functions | Not this change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| Identity | MODIFIED |
| Wallet | MODIFIED |
| Transaction | ADJACENT |
| Mempool | ADJACENT |
| Block | ADJACENT |
| Chain | ADJACENT |
| Consensus | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|
| NONE IDENTIFIED |

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| An acceptance whose lookup of the person fails is rejected, and no acceptance is recorded. |
| Every identity and wallet act ends as rejected when a record it needs fails. |
| An act stops at the step whose record failed, and nothing after it runs. |
| Every act whose records are all read and written ends exactly as it did before this change. |
| Records made before a failure are unchanged by it. |

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
| Registering a person | A record the registration needs fails | A failed record ends the act. |
| Accepting a person | A record the acceptance needs fails | A failed record ends the act. |
| Rejecting a person | A record the rejection needs fails | A failed record ends the act. |
| Creating a wallet | A record the wallet needs fails | A failed record ends the act. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
