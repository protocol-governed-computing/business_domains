# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain: identity
  cr: cr_03_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - classification: MODIFY
    rationale: The identity function exists and works. Recording a decision destroys details it was never entitled to touch, against a rule the business set when the function was established. This changes how a decision is written so that it adds to what the business holds rather than replacing it. Nothing is added to what identity offers and nothing is withdrawn.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Admitted Details
    definition: What a person supplied when they registered — their name, their contact address and their preferences — which are theirs and stay theirs.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Decision
    definition: An authority's act of accepting or rejecting a registered person.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Decided Details
    definition: 'The three things a decision is entitled to change: the person''s state, the authority who decided, and the grounds stated.'
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: The Record
    definition: 'What the business holds about a person: their admitted details together with their decided details.'
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: The Trail
    definition: The occurrences recorded against a person, added to and never rewritten.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Thinned Record
    definition: A record from which a decision has already removed a person's admitted details, before this change.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  requested_outcomes:
  - outcome: Recording a decision leaves untouched everything the business knows about a person, except the three things a decision is entitled to change.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: A person accepted or rejected still carries the name they registered with.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: A person accepted or rejected still carries the preferences they were admitted with.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: 'A caller can tell no difference: what they send and what they are told back are unchanged.'
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  known_facts:
  - fact: The business decided at the outset that a person keeps the details they were admitted with.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Nothing an authority does should change who a person said they were.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: Recording a decision erases what the business already knows about the person.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: After a decision the business holds only the person's address, their state, and the authority who decided.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The person's own name is gone after a decision, and so are their preferences.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Nobody asked for that; the business stated the opposite rule.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: The business has been breaking that rule since the function was built.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: This is a defect and not a new requirement.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The business is deciding nothing here it has not already decided.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: 'A decision is entitled to change three things: the person''s state, the authority who decided, and the grounds stated.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: A decision must leave alone everything else the business holds, starting with the name and the preferences.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: A decision records a decision; changing a person's details is a different act.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: A decision never has a reason to change a person's own details.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: The defect was noticed when a person registered from the web page was accepted and the record afterwards carried no name.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: People already decided about have already lost their details and stay as they are.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: The business does not rewrite what it has recorded.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: The business would rather carry a thin old record than start editing history.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: The record is added to and never rewritten, and that rule holds even when what was written is thin.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: What a caller sends and what they are told back are unchanged.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: A person using the web page cannot tell that anything is different, and neither can anyone recording a decision another way.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: This change is invisible from outside, and it should be.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: A rejection must state grounds and an acceptance need not, exactly as before.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: 'The trail is unaffected: the same moments are recorded, saying the same things.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  system_beliefs:
  - belief: The business author believes recording a decision replaces the person's record rather than adding to it.
    why_it_matters: The whole change rests on it. If the record is merely written incompletely rather than replaced, the cause and the correction are both different.
    verification_goal: Establish how a decision writes a person's record, and whether what it writes replaces the record held or updates part of it.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are.
    why_it_matters: If it cannot, keeping a person's details through a decision needs something the platform does not offer, and this change must ask for it rather than assume it.
    verification_goal: Establish whether the composition offers an operation that updates named fields of a held record without replacing the whole of it.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them.
    why_it_matters: If the details are assembled from several places, leaving one alone may not be sufficient.
    verification_goal: Establish where a person's name and preferences are held, and whether anything else writes to the same place.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  - belief: The business author believes nothing else in the composition depends on the shape a decision currently leaves behind.
    why_it_matters: A thinned record is the shape everything downstream has seen since the function was built; something may have been written against it.
    verification_goal: Establish whether any artifact reads a person's record and expects only the fields a decision currently leaves.
    source_finding: {phase: p0, register: system_beliefs, row: 4}
  - belief: The business author believes what a caller sends and is told is declared apart from how a decision is performed.
    why_it_matters: The business promises this change is invisible from outside. If the two are bound together, that promise cannot be kept.
    verification_goal: Establish whether what a caller may send and what they are told are declared separately from the steps that record a decision.
    source_finding: {phase: p0, register: system_beliefs, row: 5}
  assumptions:
  - assumption: The people already decided about are few enough that leaving their thinned records alone costs the business little.
    basis: The business author accepts thinned records rather than rewriting them, which holds only while the loss is small.
    source_finding: {phase: p0, register: assumptions, row: 1}
  - assumption: A person's admitted details are worth keeping — something will eventually read them.
    basis: The business author treats their loss as a defect rather than a shape to accept, which presumes a reader.
    source_finding: {phase: p0, register: assumptions, row: 2}
  constraints:
  - constraint: A decision may change only the person's state, the authority who decided, and the grounds stated.
    source: The business author's statement of what a decision is entitled to change.
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: A decision may change none of a person's own details.
    source: The business author's statement that a decision records a decision.
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: What a caller sends and is told back is unchanged.
    source: The business author's statement that this change is invisible from outside.
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: Records already written are never rewritten, including thin ones.
    source: The business author's statement that the business does not rewrite what it has recorded.
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: Grounds are required to reject and optional to accept.
    source: Carried unchanged from the change that established the decision.
    source_finding: {phase: p0, register: constraints, row: 5}
  - constraint: What is recorded in the trail is unchanged.
    source: The business author's statement that the same moments are recorded, saying the same things.
    source_finding: {phase: p0, register: constraints, row: 6}
  business_invariants:
  - invariant: A person's admitted details survive every decision recorded about them.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: A decision changes the person's state, the authority named and the grounds, and nothing else about them.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No decision alters a detail the person supplied themselves.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: A record already written is never rewritten, however thin it is.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: What a caller sends and what they are told back is unchanged by how a decision is written.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: NONE IDENTIFIED
    state: ''
    meaning: This change introduces no state. A person is unverified, accepted or rejected exactly as before.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  business_events:
  - event: NONE IDENTIFIED
    when_it_occurs: This change recognises no new moment.
    significance: The moments the business records are unchanged in when they occur and in what they mean.
    source_finding: {phase: p0, register: business_events, row: 1}
  authority_boundaries:
  - business_object: A person's admitted details
    authoritative_owner: The person themselves, and no decision recorded about them.
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: A person's decided details
    authoritative_owner: An authority within the business, through the identity function.
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: How a decision is written
    authoritative_owner: The identity function of the blockchain project.
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  out_of_scope:
  - item: How a decision is performed, beyond not destroying what it should not touch
    reason: Named by the business author as outside this change.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Anything about grounds
    reason: A rejection must state them and an acceptance need not, exactly as before.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Which persons may be an authority, or whether the one named is entitled to decide
    reason: Unchanged and still deferred.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Rewriting records already thinned by a decision made before this change
    reason: The record is added to and never rewritten.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Correcting a person's own details
    reason: A separate change and still deferred.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: The other six blockchain functions
    reason: Named, planned, and outside this change.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  governance_scope:
  - scope_item: Identity
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: Wallet
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: Transaction
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  - scope_item: Mempool
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 4}
  - scope_item: Block
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 5}
  - scope_item: Chain
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 6}
  - scope_item: Consensus
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 7}
  clarification_requests: []
  acceptance_criteria:
  - criterion: A person accepted after registering still carries the name they registered with.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A person accepted after registering still carries the preferences they were admitted with.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: A person rejected after registering still carries their name and their preferences.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A decision changes the person's state, the authority named and the grounds, and nothing else about them.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: A caller sending exactly what they send today is told exactly what they are told today.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: The trail after a decision holds the same moment, saying the same thing, as it did before this change.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: A record thinned by a decision made before this change is left as it is.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: A rejection stating no grounds is refused where it was refused before, and no differently.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: A person is decided about once, and a second decision is refused as before.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  identity_and_sameness:
  - business_object: The Record
    identified_by: The contact address the person registered with.
    two_are_the_same_when: Their addresses match — one person has one record, holding their admitted details and their decided details together.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Person
    from_state: Unverified
    to_state: Accepted
    triggered_by: An authority accepts them.
    cascade: None. The person's admitted details are carried across the transition rather than dropped, which is the correction this change makes.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Person
    from_state: Unverified
    to_state: Rejected
    triggered_by: An authority rejects them, stating grounds.
    cascade: None, and the same correction applies.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  operation_refusals:
  - operation: Record a decision
    refused_when: Never on any new ground; every refusal is the one it was before.
    business_reason: This change alters what a decision writes, not what it admits.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Record a decision
    refused_when: Never on the ground that it would change a person's own details, because it may not change them at all.
    business_reason: A decision records a decision.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Rewrite a record already thinned
    refused_when: Always.
    business_reason: The record is added to and never rewritten.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  authority_deferrals:
  - business_object: Correcting a person's own details
    deferred_to: A follow-on governed change for correction
    until: The business chooses to take it up.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
  - business_object: Which persons may be an authority
    deferred_to: A follow-on governed change for authority over verifiers
    until: The business chooses to take it up.
    source_finding: {phase: p0, register: authority_deferrals, row: 2}
  - business_object: Restoring details lost from records already thinned
    deferred_to: Nowhere; the business declines it
    until: The business does not rewrite what it has recorded.
    source_finding: {phase: p0, register: authority_deferrals, row: 3}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
