# Change Seed — blockchain / identity

**Stage:** 0 — Change Seed
**CR:** cr_05_identity
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
record for each person known to the system, the state that says whether the business has accepted
them, and the record of every moment in their history. A person supplies their own details and is
admitted unverified; separately, an authority records a decision accepting or rejecting them. The
details a person was admitted with are theirs and stay theirs: a decision records whether the
business trusts someone, and it is not an occasion to alter who they said they were. Identity also
decides what of itself is offered to callers outside it. It does not govern what a trusted actor may
then do, which persons may be an authority, or who a caller is.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| identity | MODIFY | Identity is built and reachable. It applies its rules as each request states them rather than holding them itself, and it registers a person whose registration it has found incomplete. Nothing is added to what identity does; its own rules are made to hold however it is reached. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Registration | What a person supplies to become known to the business: their name and the address they are reached at. |
| Decision | What an authority records about a person: an acceptance or a rejection. There is no third. |
| Authority | The person who records a decision about someone else. |
| Grounds | The reason an authority states when rejecting a person. |
| Public entrance | The way a caller outside the business reaches identity. |
| Business rule | Something the business decided about identity: what a registration must contain, who may be decided about, which decisions may be recorded. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Identity holds what a registration must contain, and refuses a registration that does not meet it. |
| Identity holds which people an authority may decide about, and refuses a decision about anyone else, whatever the request says. |
| Identity holds which decisions may be recorded, and refuses any other, whatever the request says. |
| Everything a caller sees through the public entrance is unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| A registration names the person and the address they are reached at. Both are required. | HIGH |
| A person is decided about once. Only an unverified person may be accepted or rejected. | HIGH |
| A decision is an acceptance or a rejection. There is no third. | HIGH |
| A rejection states its grounds. An acceptance may. | HIGH |
| An authority does not decide about themselves. | HIGH |
| A business rule the caller supplies is a business rule the caller can widen. | HIGH |
| The wallet function met this and closed it for itself. | HIGH |
| A registration missing its name or address is refused. | HIGH |
| What a request says about the business's rules is ignored, not refused; it is not part of the request. | HIGH |
| A decision refused because the person was already decided about changes no record. | HIGH |
| The business adds to its record and does not rewrite it. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The public entrance supplies the business's rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded. | If the entrance supplies them, a caller through it is held to them, and what changes is invisible there. | Confirm what the public entrance supplies to identity on each request. |
| Identity takes each of those rules from the request rather than holding them itself. | This is the hole: anything reaching identity another way states its own rules and is judged by them. | Establish where identity reads each rule from. |
| A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded. | The consequence the business wants closed. | Establish what identity does with a decision request stating a wider rule than the business's. |
| Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway. | The second consequence the business wants closed. | Establish what identity does with what its registration check finds. |
| Through the public entrance an incomplete registration is refused before identity checks it. | Explains why nothing has shown the second fault from outside. | Confirm what the public entrance refuses before identity is reached. |
| The wallet function holds its own rule about who may have a wallet, rather than taking it from the request. | The business has already closed this hole once, and the change follows that precedent. | Confirm where wallet's rule is held. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| NONE IDENTIFIED | |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers. | Business author |
| Records made under a request's own rules stay as they were made. | Business author — the record is added to, never rewritten. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No person is registered without a name and an address they are reached at. |
| No person is decided about more than once. |
| No decision other than an acceptance or a rejection is recorded. |
| No rejection is recorded without its grounds. |
| No authority decides about themselves. |
| A business rule of identity's is held by identity, and no request changes it. |
| A refusal changes no record. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Person | Unverified | Registered, and not yet decided about. The only state a decision may be recorded from. |
| Person | Accepted | An authority recorded an acceptance. |
| Person | Rejected | An authority recorded a rejection, with its grounds. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| A person was registered | When a person supplies a complete registration | Unchanged by this change. |
| A person was accepted | When an authority records an acceptance about an unverified person | Unchanged by this change. |
| A person was rejected | When an authority records a rejection, with grounds, about an unverified person | Unchanged by this change. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| What a registration must contain | Identity |
| Which people may be decided about | Identity |
| Which decisions may be recorded | Identity |
| Person, and whether the business accepts them | Identity |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Who may be an authority, or whether the one named is entitled to decide | Not this change. |
| What a registration may contain beyond its two required parts | Not this change. |
| The wallet function | It already holds its own rules. |
| People already registered or decided about | The business adds to its record and does not rewrite it. |
| The other five functions | Not this change. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| Identity | MODIFIED |
| Wallet | ADJACENT |
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
| A registration missing its name or its address is refused, however identity is reached, and no person is registered by it. |
| A decision about a person already accepted or rejected is refused, whatever the request says about who may be decided about, and no record changes. |
| A decision other than an acceptance or a rejection is refused, whatever the request says about which decisions are allowed. |
| A request stating rules of its own is judged by the business's rules, and is not refused for stating them. |
| Every request admitted through the public entrance before this change is admitted after it, with the same answer; every request refused there is refused, with the same answer. |
| Records made before this change are unchanged by it. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| NONE IDENTIFIED | | |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Person | Does not exist | Unverified | A complete registration | Unchanged by this change. |
| Person | Unverified | Accepted | An authority recording an acceptance | Unchanged by this change. |
| Person | Unverified | Rejected | An authority recording a rejection with grounds | Unchanged by this change. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Registering a person | The registration lacks the person's name or their address | The business said both are required. |
| Recording a decision | The person is not unverified | A person is decided about once. |
| Recording a decision | The decision is neither an acceptance nor a rejection | There is no third decision. |
| Recording a rejection | No grounds are stated | The business decided a rejection must say why. |
| Recording a decision | The authority is the person decided about | An authority does not decide about themselves. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| NONE IDENTIFIED | | |
