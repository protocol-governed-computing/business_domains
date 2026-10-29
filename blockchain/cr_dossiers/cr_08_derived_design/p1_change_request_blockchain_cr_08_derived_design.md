# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p1
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_08_derived_design
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity says who an actor is and whether the business trusts them. A person registers and is admitted unverified, and an authority accepts or rejects them once.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet says where a person the business has accepted holds value. An accepted person is given exactly one wallet, formed from the public key they supply. Wallet reads identity's records and never writes them.
    source_finding: {phase: p0, register: cr_type, row: 2}
  business_vocabulary:
  - term: Actor
    definition: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Wallet
    definition: The business must know where a person it has accepted holds value, one wallet to each such person.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  requested_outcomes:
  - outcome: 'Register actor: records a new actor.'
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: 'Accept actor: moves an actor from unverified to accepted.'
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: 'Reject actor: moves an actor from unverified to rejected.'
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: 'Create wallet: records a new wallet.'
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  known_facts:
  - fact: An actor is identified by its contact address.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: A wallet is identified by its holder.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  system_beliefs:
  - belief: The current identity design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the identity baseline design and find there each name the derived design carries.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The current wallet design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the wallet baseline design and find there each name the derived design carries.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: Recording an actor again with the same contact address records the repeat, and the actor already recorded is unchanged by it.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two wallets share their holder.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Each wallet is held by one actor who is accepted.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every identity operation records contact address, verifying authority and grounds on the identity trail, and no entry is changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every wallet operation records holder on the wallet trail, and no entry is changed or removed.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  lifecycle_states:
  - object: actor
    state: unverified
    meaning: An actor is unverified after register actor.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: actor
    state: accepted
    meaning: An actor is accepted after accept actor.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: actor
    state: rejected
    meaning: An actor is rejected after reject actor.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: wallet
    state: active
    meaning: A wallet is active after create wallet.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: Actor registered unverified
    when_it_occurs: When register actor completes
    significance: Others learn that register actor completed without reading the identity records.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Actor accepted
    when_it_occurs: When accept actor completes
    significance: Others learn that accept actor completed without reading the identity records.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Actor rejected
    when_it_occurs: When reject actor completes
    significance: Others learn that reject actor completed without reading the identity records.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: Wallet created
    when_it_occurs: When create wallet completes
    significance: Others learn that create wallet completed without reading the wallet records.
    source_finding: {phase: p0, register: business_events, row: 4}
  authority_boundaries:
  - business_object: actor
    authoritative_owner: identity
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: wallet
    authoritative_owner: wallet
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  out_of_scope:
  - item: Authenticating callers
    reason: No caller needs an account or a login.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Wallets of any classification but default
    reason: The business names four classifications, and only default wallets are created.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Moving value between wallets
    reason: A wallet holds a balance; no act the business asks for moves it.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  governance_scope:
  - scope_item: identity
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: wallet
    relationship: MODIFIED
    source_finding: {phase: p0, register: governance_scope, row: 2}
  clarification_requests: []
  acceptance_criteria:
  - criterion: Accept actor is refused when the actor is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: Accept actor is refused when the actor is not unverified.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Reject actor is refused when the actor is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Reject actor is refused when the actor is not unverified.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Create wallet is refused when a wallet that is the same is already recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: Create wallet is refused when the actor who would hold it is not recorded.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Create wallet is refused when the actor who would hold it is not accepted.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  identity_and_sameness:
  - business_object: actor
    identified_by: contact address
    two_are_the_same_when: they carry the same contact address
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - business_object: wallet
    identified_by: holder
    two_are_the_same_when: they carry the same holder
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  lifecycle_transitions:
  - object: actor
    from_state: unverified
    to_state: accepted
    triggered_by: accept actor
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: actor
    from_state: unverified
    to_state: rejected
    triggered_by: reject actor
    cascade: None
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  operation_refusals:
  - operation: accept actor
    refused_when: the actor is not recorded
    business_reason: There is no actor to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: accept actor
    refused_when: the actor is not unverified
    business_reason: Only an unverified actor becomes accepted.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: reject actor
    refused_when: the actor is not recorded
    business_reason: There is no actor to act on.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: reject actor
    refused_when: the actor is not unverified
    business_reason: Only an unverified actor becomes rejected.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: create wallet
    refused_when: a wallet that is the same is already recorded
    business_reason: Two wallets that are the same would describe one wallet twice.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: create wallet
    refused_when: the actor who would hold it is not recorded
    business_reason: A wallet no actor holds belongs to nobody the business knows.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: create wallet
    refused_when: the actor who would hold it is not accepted
    business_reason: Only accepted actors hold wallets.
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  authority_deferrals: []
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
