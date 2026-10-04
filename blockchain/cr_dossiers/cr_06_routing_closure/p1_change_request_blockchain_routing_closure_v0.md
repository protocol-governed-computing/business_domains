# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity and wallet
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_06_routing_closure
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
| identity | MODIFY | Identity's acts do not say what happens when a record fails, and one carries on past a failed lookup. Nothing is added to what identity does. | CR seed §1 CR Type #1 |
| wallet | MODIFY | Wallet's act does not say what happens when a record fails, and three of its steps carry on past a failure. Nothing is added to what wallet does. | CR seed §1 CR Type #2 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Record | Something the business keeps: a person's record, a claimed address, a trail of moments, or a wallet. | CR seed §2 Business Vocabulary #1 |
| Failed record | A record that could not be read or written, because the store was unreachable or answered with an error. | CR seed §2 Business Vocabulary #2 |
| Act | One thing a caller asks identity or wallet to do: register, accept, reject, or create a wallet. | CR seed §2 Business Vocabulary #3 |
| Rejected | The ending of an act that did not succeed. | CR seed §2 Business Vocabulary #4 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Every identity and wallet act ends as rejected when a record it needs fails. | CR seed §3 Requested Outcomes #1 |
| An act stops at the step whose record failed, and nothing after it runs. | CR seed §3 Requested Outcomes #2 |
| Everything else identity and wallet do is unchanged. | CR seed §3 Requested Outcomes #3 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| An act either succeeds or is rejected. There is no third ending. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| A rejection changes no record. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The business adds to its record and does not rewrite it. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A failed record ends the act. Nothing retries. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A failed record ends as rejected, not as a separate failure. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Every identity and wallet act reads or writes a record the business keeps. | HIGH | CR seed §4 Known Facts — Business Truths #6 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| Most identity and wallet acts stop without a declared ending when a record fails. | The caller cannot tell an intended refusal from an unplanned failure. | Establish, for each act, what happens when each record it touches fails. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| When an acceptance's lookup of the person fails, identity carries on and records the acceptance. | This is the failure the business wants closed first. | Establish what identity does when the lookup fails during an acceptance. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| Three of wallet's steps carry on past a failed record in the same way. | The same gap, in the same form, in the other subdomain. | Establish which wallet steps carry on past a failed record. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| Each act already has a rejected ending. | The change can end a failed record there without adding an ending. | Confirm every identity and wallet act has a rejected ending. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |

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
| Nothing changes for an act whose records are all read and written. | Business author | CR seed §7 Constraints #1 |
| Records made before a failure stay as they were made. | Business author — the record is added to, never rewritten. | CR seed §7 Constraints #2 |
| No ending is added. | Business author — a failure ends as rejected. | CR seed §7 Constraints #3 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No act carries on past a record it could not read or write. | CR seed §8 Business Invariants #1 |
| Every act ends as succeeded or rejected. | CR seed §8 Business Invariants #2 |
| A refusal changes no record. | CR seed §8 Business Invariants #3 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Person | Unverified | Registered, and not yet decided about. Unchanged by this change. | CR seed §9 Lifecycle States #1 |
| Person | Accepted | An authority recorded an acceptance. Unchanged by this change. | CR seed §9 Lifecycle States #2 |
| Person | Rejected | An authority recorded a rejection, with its grounds. Unchanged by this change. | CR seed §9 Lifecycle States #3 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| A person was registered | When a person supplies a complete registration and every record is written | Unchanged; it is not announced when a record fails. | CR seed §10 Business Events #1 |
| A person was accepted | When an authority records an acceptance and every record is written | Unchanged; it is not announced when a record fails. | CR seed §10 Business Events #2 |
| A person was rejected | When an authority records a rejection and every record is written | Unchanged; it is not announced when a record fails. | CR seed §10 Business Events #3 |
| A wallet was created | When an accepted person is given a wallet and every record is written | Unchanged; it is not announced when a record fails. | CR seed §10 Business Events #4 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| What an identity act does when a record fails | Identity | CR seed §11 Authority Boundaries #1 |
| What a wallet act does when a record fails | Wallet | CR seed §11 Authority Boundaries #2 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Telling a refusal apart from a failure | A later decision; the business keeps two endings. | CR seed §12 Out of Scope #1 |
| Trying a failed record again | The business decided a failed record ends the act. | CR seed §12 Out of Scope #2 |
| Records made before a failure | The business adds to its record and does not rewrite it. | CR seed §12 Out of Scope #3 |
| The other five functions | Not this change. | CR seed §12 Out of Scope #4 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| Identity | MODIFIED | CR seed §13 Governance Scope #1 |
| Wallet | MODIFIED | CR seed §13 Governance Scope #2 |
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
| An acceptance whose lookup of the person fails is rejected, and no acceptance is recorded. | CR seed §15 Acceptance Criteria #1 |
| Every identity and wallet act ends as rejected when a record it needs fails. | CR seed §15 Acceptance Criteria #2 |
| An act stops at the step whose record failed, and nothing after it runs. | CR seed §15 Acceptance Criteria #3 |
| Every act whose records are all read and written ends exactly as it did before this change. | CR seed §15 Acceptance Criteria #4 |
| Records made before a failure are unchanged by it. | CR seed §15 Acceptance Criteria #5 |

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
| NONE IDENTIFIED |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Registering a person | A record the registration needs fails | A failed record ends the act. | CR seed §18 Operation Refusals #1 |
| Accepting a person | A record the acceptance needs fails | A failed record ends the act. | CR seed §18 Operation Refusals #2 |
| Rejecting a person | A record the rejection needs fails | A failed record ends the act. | CR seed §18 Operation Refusals #3 |
| Creating a wallet | A record the wallet needs fails | A failed record ends the act. | CR seed §18 Operation Refusals #4 |

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
