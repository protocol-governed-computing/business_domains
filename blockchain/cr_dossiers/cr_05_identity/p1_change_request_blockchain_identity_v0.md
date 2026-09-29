# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_05_identity
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
| identity | MODIFY | Identity is built and reachable. It applies its rules as each request states them rather than holding them itself, and it registers a person whose registration it has found incomplete. Nothing is added to what identity does; its own rules are made to hold however it is reached. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Registration | What a person supplies to become known to the business: their name and the address they are reached at. | CR seed §2 Business Vocabulary #1 |
| Decision | What an authority records about a person: an acceptance or a rejection. There is no third. | CR seed §2 Business Vocabulary #2 |
| Authority | The person who records a decision about someone else. | CR seed §2 Business Vocabulary #3 |
| Grounds | The reason an authority states when rejecting a person. | CR seed §2 Business Vocabulary #4 |
| Public entrance | The way a caller outside the business reaches identity. | CR seed §2 Business Vocabulary #5 |
| Business rule | Something the business decided about identity: what a registration must contain, who may be decided about, which decisions may be recorded. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Identity holds what a registration must contain, and refuses a registration that does not meet it. | CR seed §3 Requested Outcomes #1 |
| Identity holds which people an authority may decide about, and refuses a decision about anyone else, whatever the request says. | CR seed §3 Requested Outcomes #2 |
| Identity holds which decisions may be recorded, and refuses any other, whatever the request says. | CR seed §3 Requested Outcomes #3 |
| Everything a caller sees through the public entrance is unchanged. | CR seed §3 Requested Outcomes #4 |
| Identity holds that an authority does not decide about themselves, and refuses such a decision, whatever the request says. | CR seed §3 Requested Outcomes #5 |
| Identity holds that a rejection states its grounds, and refuses one that does not, whatever the request says. | CR seed §3 Requested Outcomes #6 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| A registration names the person and the address they are reached at. Both are required. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A person is decided about once. Only an unverified person may be accepted or rejected. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| A decision is an acceptance or a rejection. There is no third. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A rejection states its grounds. An acceptance may. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| An authority does not decide about themselves. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A business rule the caller supplies is a business rule the caller can widen. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The wallet function met this and closed it for itself. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| A registration missing its name or address is refused. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| What a request says about the business's rules is ignored, not refused; it is not part of the request. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A decision refused because the person was already decided about changes no record. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| The business adds to its record and does not rewrite it. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Every business rule of identity's is held by identity: what a registration must contain, who may be decided about, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states its grounds. | HIGH | CR seed §4 Known Facts — Business Truths #12 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The public entrance supplies the business's rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded. | If the entrance supplies them, a caller through it is held to them, and what changes is invisible there. | Confirm what the public entrance supplies to identity on each request. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| Identity takes each of those rules from the request rather than holding them itself. | This is the hole: anything reaching identity another way states its own rules and is judged by them. | Establish where identity reads each rule from. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded. | The consequence the business wants closed. | Establish what identity does with a decision request stating a wider rule than the business's. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway. | The second consequence the business wants closed. | Establish what identity does with what its registration check finds. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| Through the public entrance an incomplete registration is refused before identity checks it. | Explains why nothing has shown the second fault from outside. | Confirm what the public entrance refuses before identity is reached. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |
| The wallet function holds its own rule about who may have a wallet, rather than taking it from the request. | The business has already closed this hole once, and the change follows that precedent. | Confirm where wallet's rule is held. | CR seed §5 Existing-System Beliefs — Requiring Verification #6 |

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
| Nothing a caller sees through the public entrance changes: the same requests are admitted and refused, with the same answers. | Business author | CR seed §7 Constraints #1 |
| Records made under a request's own rules stay as they were made. | Business author — the record is added to, never rewritten. | CR seed §7 Constraints #2 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No person is registered without a name and an address they are reached at. | CR seed §8 Business Invariants #1 |
| No person is decided about more than once. | CR seed §8 Business Invariants #2 |
| No decision other than an acceptance or a rejection is recorded. | CR seed §8 Business Invariants #3 |
| No rejection is recorded without its grounds. | CR seed §8 Business Invariants #4 |
| No authority decides about themselves. | CR seed §8 Business Invariants #5 |
| A business rule of identity's is held by identity, and no request changes it. | CR seed §8 Business Invariants #6 |
| A refusal changes no record. | CR seed §8 Business Invariants #7 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Person | Unverified | Registered, and not yet decided about. The only state a decision may be recorded from. | CR seed §9 Lifecycle States #1 |
| Person | Accepted | An authority recorded an acceptance. | CR seed §9 Lifecycle States #2 |
| Person | Rejected | An authority recorded a rejection, with its grounds. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A person was registered | When a person supplies a complete registration | Unchanged by this change. | CR seed §10 Business Events #1 |
| A person was accepted | When an authority records an acceptance about an unverified person | Unchanged by this change. | CR seed §10 Business Events #2 |
| A person was rejected | When an authority records a rejection, with grounds, about an unverified person | Unchanged by this change. | CR seed §10 Business Events #3 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What a registration must contain | Identity | CR seed §11 Authority Boundaries #1 |
| Which people may be decided about | Identity | CR seed §11 Authority Boundaries #2 |
| Which decisions may be recorded | Identity | CR seed §11 Authority Boundaries #3 |
| Person, and whether the business accepts them | Identity | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Who may be an authority, or whether the one named is entitled to decide | Not this change. | CR seed §12 Out of Scope #1 |
| What a registration may contain beyond its two required parts | Not this change. | CR seed §12 Out of Scope #2 |
| The wallet function | It already holds its own rules. | CR seed §12 Out of Scope #3 |
| People already registered or decided about | The business adds to its record and does not rewrite it. | CR seed §12 Out of Scope #4 |
| The other five functions | Not this change. | CR seed §12 Out of Scope #5 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| Identity | MODIFIED | CR seed §13 Governance Scope #1 |
| Wallet | ADJACENT | CR seed §13 Governance Scope #2 |
| Transaction | ADJACENT | CR seed §13 Governance Scope #3 |
| Mempool | ADJACENT | CR seed §13 Governance Scope #4 |
| Block | ADJACENT | CR seed §13 Governance Scope #5 |
| Chain | ADJACENT | CR seed §13 Governance Scope #6 |
| Consensus | ADJACENT | CR seed §13 Governance Scope #7 |

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
| A registration missing its name or its address is refused, however identity is reached, and no person is registered by it. | CR seed §15 Acceptance Criteria #1 |
| A decision about a person already accepted or rejected is refused, whatever the request says about who may be decided about, and no record changes. | CR seed §15 Acceptance Criteria #2 |
| A decision other than an acceptance or a rejection is refused, whatever the request says about which decisions are allowed. | CR seed §15 Acceptance Criteria #3 |
| An authority deciding about themselves is refused, whatever the request says. | CR seed §15 Acceptance Criteria #4 |
| A rejection stating no grounds is refused, whatever the request says. | CR seed §15 Acceptance Criteria #5 |
| A request stating rules of its own is judged by the business's rules, and is not refused for stating them. | CR seed §15 Acceptance Criteria #6 |
| Every request admitted through the public entrance before this change is admitted after it, with the same answer; every request refused there is refused, with the same answer. | CR seed §15 Acceptance Criteria #7 |
| Records made before this change are unchanged by it. | CR seed §15 Acceptance Criteria #8 |

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
| Person | Does not exist | Unverified | A complete registration | Unchanged by this change. | CR seed §17 Lifecycle Transitions #1 |
| Person | Unverified | Accepted | An authority recording an acceptance | Unchanged by this change. | CR seed §17 Lifecycle Transitions #2 |
| Person | Unverified | Rejected | An authority recording a rejection with grounds | Unchanged by this change. | CR seed §17 Lifecycle Transitions #3 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Registering a person | The registration lacks the person's name or their address | The business said both are required. | CR seed §18 Operation Refusals #1 |
| Recording a decision | The person is not unverified | A person is decided about once. | CR seed §18 Operation Refusals #2 |
| Recording a decision | The decision is neither an acceptance nor a rejection | There is no third decision. | CR seed §18 Operation Refusals #3 |
| Recording a rejection | No grounds are stated | The business decided a rejection must say why. | CR seed §18 Operation Refusals #4 |
| Recording a decision | The authority is the person decided about | An authority does not decide about themselves. | CR seed §18 Operation Refusals #5 |

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
