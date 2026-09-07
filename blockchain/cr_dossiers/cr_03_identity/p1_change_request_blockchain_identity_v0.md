# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_03_identity
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-------------------------------------------------------------------|---------|--------------|
| MODIFY | The identity function exists and works. Recording a decision destroys details it was never entitled to touch, against a rule the business set when the function was established. This changes how a decision is written so that it adds to what the business holds rather than replacing it. Nothing is added to what identity offers and nothing is withdrawn. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Admitted Details | What a person supplied when they registered — their name, their contact address and their preferences — which are theirs and stay theirs. | CR seed §2 Business Vocabulary #1 |
| Decision | An authority's act of accepting or rejecting a registered person. | CR seed §2 Business Vocabulary #2 |
| Decided Details | The three things a decision is entitled to change: the person's state, the authority who decided, and the grounds stated. | CR seed §2 Business Vocabulary #3 |
| The Record | What the business holds about a person: their admitted details together with their decided details. | CR seed §2 Business Vocabulary #4 |
| The Trail | The occurrences recorded against a person, added to and never rewritten. | CR seed §2 Business Vocabulary #5 |
| Thinned Record | A record from which a decision has already removed a person's admitted details, before this change. | CR seed §2 Business Vocabulary #6 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Recording a decision leaves untouched everything the business knows about a person, except the three things a decision is entitled to change. | CR seed §3 Requested Outcomes #1 |
| A person accepted or rejected still carries the name they registered with. | CR seed §3 Requested Outcomes #2 |
| A person accepted or rejected still carries the preferences they were admitted with. | CR seed §3 Requested Outcomes #3 |
| A caller can tell no difference: what they send and what they are told back are unchanged. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The business decided at the outset that a person keeps the details they were admitted with. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Nothing an authority does should change who a person said they were. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| Recording a decision erases what the business already knows about the person. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| After a decision the business holds only the person's address, their state, and the authority who decided. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The person's own name is gone after a decision, and so are their preferences. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Nobody asked for that; the business stated the opposite rule. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| The business has been breaking that rule since the function was built. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| This is a defect and not a new requirement. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The business is deciding nothing here it has not already decided. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A decision is entitled to change three things: the person's state, the authority who decided, and the grounds stated. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A decision must leave alone everything else the business holds, starting with the name and the preferences. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| A decision records a decision; changing a person's details is a different act. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| A decision never has a reason to change a person's own details. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| The defect was noticed when a person registered from the web page was accepted and the record afterwards carried no name. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| People already decided about have already lost their details and stay as they are. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| The business does not rewrite what it has recorded. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| The business would rather carry a thin old record than start editing history. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The record is added to and never rewritten, and that rule holds even when what was written is thin. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| What a caller sends and what they are told back are unchanged. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A person using the web page cannot tell that anything is different, and neither can anyone recording a decision another way. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| This change is invisible from outside, and it should be. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| A rejection must state grounds and an acceptance need not, exactly as before. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| The trail is unaffected: the same moments are recorded, saying the same things. | HIGH | CR seed §4 Known Facts — Business Truths #23 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The business author believes recording a decision replaces the person's record rather than adding to it. | The whole change rests on it. If the record is merely written incompletely rather than replaced, the cause and the correction are both different. | Establish how a decision writes a person's record, and whether what it writes replaces the record held or updates part of it. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are. | If it cannot, keeping a person's details through a decision needs something the platform does not offer, and this change must ask for it rather than assume it. | Establish whether the composition offers an operation that updates named fields of a held record without replacing the whole of it. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them. | If the details are assembled from several places, leaving one alone may not be sufficient. | Establish where a person's name and preferences are held, and whether anything else writes to the same place. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The business author believes nothing else in the composition depends on the shape a decision currently leaves behind. | A thinned record is the shape everything downstream has seen since the function was built; something may have been written against it. | Establish whether any artifact reads a person's record and expects only the fields a decision currently leaves. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The business author believes what a caller sends and is told is declared apart from how a decision is performed. | The business promises this change is invisible from outside. If the two are bound together, that promise cannot be kept. | Establish whether what a caller may send and what they are told are declared separately from the steps that record a decision. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| The people already decided about are few enough that leaving their thinned records alone costs the business little. | The business author accepts thinned records rather than rewriting them, which holds only while the loss is small. | CR seed §6 Assumptions #1 |
| A person's admitted details are worth keeping — something will eventually read them. | The business author treats their loss as a defect rather than a shape to accept, which presumes a reader. | CR seed §6 Assumptions #2 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| A decision may change only the person's state, the authority who decided, and the grounds stated. | The business author's statement of what a decision is entitled to change. | CR seed §7 Constraints #1 |
| A decision may change none of a person's own details. | The business author's statement that a decision records a decision. | CR seed §7 Constraints #2 |
| What a caller sends and is told back is unchanged. | The business author's statement that this change is invisible from outside. | CR seed §7 Constraints #3 |
| Records already written are never rewritten, including thin ones. | The business author's statement that the business does not rewrite what it has recorded. | CR seed §7 Constraints #4 |
| Grounds are required to reject and optional to accept. | Carried unchanged from the change that established the decision. | CR seed §7 Constraints #5 |
| What is recorded in the trail is unchanged. | The business author's statement that the same moments are recorded, saying the same things. | CR seed §7 Constraints #6 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| A person's admitted details survive every decision recorded about them. | CR seed §8 Business Invariants #1 |
| A decision changes the person's state, the authority named and the grounds, and nothing else about them. | CR seed §8 Business Invariants #2 |
| No decision alters a detail the person supplied themselves. | CR seed §8 Business Invariants #3 |
| A record already written is never rewritten, however thin it is. | CR seed §8 Business Invariants #4 |
| What a caller sends and what they are told back is unchanged by how a decision is written. | CR seed §8 Business Invariants #5 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| NONE IDENTIFIED |  | This change introduces no state. A person is unverified, accepted or rejected exactly as before. | CR seed §9 Lifecycle States #1 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments the business records are unchanged in when they occur and in what they mean. | CR seed §10 Business Events #1 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| A person's admitted details | The person themselves, and no decision recorded about them. | CR seed §11 Authority Boundaries #1 |
| A person's decided details | An authority within the business, through the identity function. | CR seed §11 Authority Boundaries #2 |
| How a decision is written | The identity function of the blockchain project. | CR seed §11 Authority Boundaries #3 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| How a decision is performed, beyond not destroying what it should not touch | Named by the business author as outside this change. | CR seed §12 Out of Scope #1 |
| Anything about grounds | A rejection must state them and an acceptance need not, exactly as before. | CR seed §12 Out of Scope #2 |
| Which persons may be an authority, or whether the one named is entitled to decide | Unchanged and still deferred. | CR seed §12 Out of Scope #3 |
| Rewriting records already thinned by a decision made before this change | The record is added to and never rewritten. | CR seed §12 Out of Scope #4 |
| Correcting a person's own details | A separate change and still deferred. | CR seed §12 Out of Scope #5 |
| The other six blockchain functions | Named, planned, and outside this change. | CR seed §12 Out of Scope #6 |

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
| A person accepted after registering still carries the name they registered with. | CR seed §15 Acceptance Criteria #1 |
| A person accepted after registering still carries the preferences they were admitted with. | CR seed §15 Acceptance Criteria #2 |
| A person rejected after registering still carries their name and their preferences. | CR seed §15 Acceptance Criteria #3 |
| A decision changes the person's state, the authority named and the grounds, and nothing else about them. | CR seed §15 Acceptance Criteria #4 |
| A caller sending exactly what they send today is told exactly what they are told today. | CR seed §15 Acceptance Criteria #5 |
| The trail after a decision holds the same moment, saying the same thing, as it did before this change. | CR seed §15 Acceptance Criteria #6 |
| A record thinned by a decision made before this change is left as it is. | CR seed §15 Acceptance Criteria #7 |
| A rejection stating no grounds is refused where it was refused before, and no differently. | CR seed §15 Acceptance Criteria #8 |
| A person is decided about once, and a second decision is refused as before. | CR seed §15 Acceptance Criteria #9 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| The Record | The contact address the person registered with. | Their addresses match — one person has one record, holding their admitted details and their decided details together. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Person | Unverified | Accepted | An authority accepts them. | None. The person's admitted details are carried across the transition rather than dropped, which is the correction this change makes. | CR seed §17 Lifecycle Transitions #1 |
| Person | Unverified | Rejected | An authority rejects them, stating grounds. | None, and the same correction applies. | CR seed §17 Lifecycle Transitions #2 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Record a decision | Never on any new ground; every refusal is the one it was before. | This change alters what a decision writes, not what it admits. | CR seed §18 Operation Refusals #1 |
| Record a decision | Never on the ground that it would change a person's own details, because it may not change them at all. | A decision records a decision. | CR seed §18 Operation Refusals #2 |
| Rewrite a record already thinned | Always. | The record is added to and never rewritten. | CR seed §18 Operation Refusals #3 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Correcting a person's own details | A follow-on governed change for correction | The business chooses to take it up. | CR seed §19 Authority Deferrals #1 |
| Which persons may be an authority | A follow-on governed change for authority over verifiers | The business chooses to take it up. | CR seed §19 Authority Deferrals #2 |
| Restoring details lost from records already thinned | Nowhere; the business declines it | The business does not rewrite what it has recorded. | CR seed §19 Authority Deferrals #3 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
