# Change Seed — blockchain / identity

**Stage:** 0 — Change Seed
**CR:** cr_03_identity
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

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | The earlier changes stated that a person is admitted on their own claim and decided about separately, and that identity owns what it offers to the outside. This adds the sentence that was always implied and never stated plainly in the purpose itself: a person's admitted details survive the decision made about them. Nothing here contradicts either earlier change; the seed's own §3 already recorded that an actor keeps the details it was admitted with. |

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| identity | MODIFY | The identity function exists and works. Recording a decision destroys details it was never entitled to touch, against a rule the business set when the function was established. This changes how a decision is written so that it adds to what the business holds rather than replacing it. Nothing is added to what identity offers and nothing is withdrawn. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Admitted Details | What a person supplied when they registered — their name, their contact address and their preferences — which are theirs and stay theirs. |
| Decision | An authority's act of accepting or rejecting a registered person. |
| Decided Details | The three things a decision is entitled to change: the person's state, the authority who decided, and the grounds stated. |
| The Record | What the business holds about a person: their admitted details together with their decided details. |
| The Trail | The occurrences recorded against a person, added to and never rewritten. |
| Thinned Record | A record from which a decision has already removed a person's admitted details, before this change. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Recording a decision leaves untouched everything the business knows about a person, except the three things a decision is entitled to change. |
| A person accepted or rejected still carries the name they registered with. |
| A person accepted or rejected still carries the preferences they were admitted with. |
| A caller can tell no difference: what they send and what they are told back are unchanged. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The business decided at the outset that a person keeps the details they were admitted with. | HIGH |
| Nothing an authority does should change who a person said they were. | HIGH |
| Recording a decision erases what the business already knows about the person. | HIGH |
| After a decision the business holds only the person's address, their state, and the authority who decided. | HIGH |
| The person's own name is gone after a decision, and so are their preferences. | HIGH |
| Nobody asked for that; the business stated the opposite rule. | HIGH |
| The business has been breaking that rule since the function was built. | HIGH |
| This is a defect and not a new requirement. | HIGH |
| The business is deciding nothing here it has not already decided. | HIGH |
| A decision is entitled to change three things: the person's state, the authority who decided, and the grounds stated. | HIGH |
| A decision must leave alone everything else the business holds, starting with the name and the preferences. | HIGH |
| A decision records a decision; changing a person's details is a different act. | HIGH |
| A decision never has a reason to change a person's own details. | HIGH |
| The defect was noticed when a person registered from the web page was accepted and the record afterwards carried no name. | HIGH |
| People already decided about have already lost their details and stay as they are. | HIGH |
| The business does not rewrite what it has recorded. | HIGH |
| The business would rather carry a thin old record than start editing history. | HIGH |
| The record is added to and never rewritten, and that rule holds even when what was written is thin. | HIGH |
| What a caller sends and what they are told back are unchanged. | HIGH |
| A person using the web page cannot tell that anything is different, and neither can anyone recording a decision another way. | HIGH |
| This change is invisible from outside, and it should be. | HIGH |
| A rejection must state grounds and an acceptance need not, exactly as before. | HIGH |
| The trail is unaffected: the same moments are recorded, saying the same things. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The business author believes recording a decision replaces the person's record rather than adding to it. | The whole change rests on it. If the record is merely written incompletely rather than replaced, the cause and the correction are both different. | Establish how a decision writes a person's record, and whether what it writes replaces the record held or updates part of it. |
| The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are. | If it cannot, keeping a person's details through a decision needs something the platform does not offer, and this change must ask for it rather than assume it. | Establish whether the composition offers an operation that updates named fields of a held record without replacing the whole of it. |
| The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them. | If the details are assembled from several places, leaving one alone may not be sufficient. | Establish where a person's name and preferences are held, and whether anything else writes to the same place. |
| The business author believes nothing else in the composition depends on the shape a decision currently leaves behind. | A thinned record is the shape everything downstream has seen since the function was built; something may have been written against it. | Establish whether any artifact reads a person's record and expects only the fields a decision currently leaves. |
| The business author believes what a caller sends and is told is declared apart from how a decision is performed. | The business promises this change is invisible from outside. If the two are bound together, that promise cannot be kept. | Establish whether what a caller may send and what they are told are declared separately from the steps that record a decision. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|
| The people already decided about are few enough that leaving their thinned records alone costs the business little. | The business author accepts thinned records rather than rewriting them, which holds only while the loss is small. |
| A person's admitted details are worth keeping — something will eventually read them. | The business author treats their loss as a defect rather than a shape to accept, which presumes a reader. |

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| A decision may change only the person's state, the authority who decided, and the grounds stated. | The business author's statement of what a decision is entitled to change. |
| A decision may change none of a person's own details. | The business author's statement that a decision records a decision. |
| What a caller sends and is told back is unchanged. | The business author's statement that this change is invisible from outside. |
| Records already written are never rewritten, including thin ones. | The business author's statement that the business does not rewrite what it has recorded. |
| Grounds are required to reject and optional to accept. | Carried unchanged from the change that established the decision. |
| What is recorded in the trail is unchanged. | The business author's statement that the same moments are recorded, saying the same things. |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| A person's admitted details survive every decision recorded about them. |
| A decision changes the person's state, the authority named and the grounds, and nothing else about them. |
| No decision alters a detail the person supplied themselves. |
| A record already written is never rewritten, however thin it is. |
| What a caller sends and what they are told back is unchanged by how a decision is written. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| NONE IDENTIFIED | | This change introduces no state. A person is unverified, accepted or rejected exactly as before. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments the business records are unchanged in when they occur and in what they mean. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| A person's admitted details | The person themselves, and no decision recorded about them. |
| A person's decided details | An authority within the business, through the identity function. |
| How a decision is written | The identity function of the blockchain project. |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| How a decision is performed, beyond not destroying what it should not touch | Named by the business author as outside this change. |
| Anything about grounds | A rejection must state them and an acceptance need not, exactly as before. |
| Which persons may be an authority, or whether the one named is entitled to decide | Unchanged and still deferred. |
| Rewriting records already thinned by a decision made before this change | The record is added to and never rewritten. |
| Correcting a person's own details | A separate change and still deferred. |
| The other six blockchain functions | Named, planned, and outside this change. |

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
| A person accepted after registering still carries the name they registered with. |
| A person accepted after registering still carries the preferences they were admitted with. |
| A person rejected after registering still carries their name and their preferences. |
| A decision changes the person's state, the authority named and the grounds, and nothing else about them. |
| A caller sending exactly what they send today is told exactly what they are told today. |
| The trail after a decision holds the same moment, saying the same thing, as it did before this change. |
| A record thinned by a decision made before this change is left as it is. |
| A rejection stating no grounds is refused where it was refused before, and no differently. |
| A person is decided about once, and a second decision is refused as before. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| The Record | The contact address the person registered with. | Their addresses match — one person has one record, holding their admitted details and their decided details together. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Person | Unverified | Accepted | An authority accepts them. | None. The person's admitted details are carried across the transition rather than dropped, which is the correction this change makes. |
| Person | Unverified | Rejected | An authority rejects them, stating grounds. | None, and the same correction applies. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Record a decision | Never on any new ground; every refusal is the one it was before. | This change alters what a decision writes, not what it admits. |
| Record a decision | Never on the ground that it would change a person's own details, because it may not change them at all. | A decision records a decision. |
| Rewrite a record already thinned | Always. | The record is added to and never rewritten. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Correcting a person's own details | A follow-on governed change for correction | The business chooses to take it up. |
| Which persons may be an authority | A follow-on governed change for authority over verifiers | The business chooses to take it up. |
| Restoring details lost from records already thinned | Nowhere; the business declines it | The business does not rewrite what it has recorded. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
