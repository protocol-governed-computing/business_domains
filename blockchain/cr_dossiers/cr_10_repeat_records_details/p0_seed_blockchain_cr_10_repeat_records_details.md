# Change Seed — blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p0
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_10_repeat_records_details
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: The blockchain domain governs identity and wallets. Identity says who an actor is and whether the business trusts them. Wallet says where a person the business has accepted holds value.
  cr_type:
  - subdomain: identity
    classification: MODIFY
    rationale: Identity says who an actor is and whether the business trusts them. A person registers and is admitted unverified, and an authority accepts or rejects them once.
  - subdomain: wallet
    classification: MODIFY
    rationale: Wallet says where a person the business has accepted holds value. An accepted person is given exactly one wallet, formed from the public key they supply. Wallet reads identity's records and never writes them.
  business_vocabulary:
  - term: Actor
    definition: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
  - term: Wallet
    definition: The business must know where a person it has accepted holds value, one wallet to each such person.
  requested_outcomes:
  - outcome: 'Register actor: records a new actor.'
  - outcome: 'Accept actor: moves an actor from unverified to accepted.'
  - outcome: 'Reject actor: moves an actor from unverified to rejected.'
  - outcome: 'List actors: returns the actors that match.'
  - outcome: 'Create wallet: records a new wallet.'
  known_facts:
  - fact: An actor is identified by its contact address.
    certainty: HIGH
  - fact: A wallet is identified by its holder.
    certainty: HIGH
  system_beliefs:
  - belief: The current identity design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the identity baseline design and find there each name the derived design carries.
  - belief: The current wallet design names the records, entrances and requests its callers use today.
    why_it_matters: The derived design keeps those names, so a caller meets no change the ledger did not decide.
    verification_goal: Read the wallet baseline design and find there each name the derived design carries.
  assumptions: []
  constraints: []
  business_invariants:
  - invariant: Recording an actor again with the same contact address records the repeat, and the actor already recorded is unchanged by it.
  - invariant: No two wallets share their holder.
  - invariant: Each wallet is held by one actor who is accepted.
  - invariant: Every identity operation records contact address, verifying authority and grounds on the identity trail, and no entry is changed or removed.
  - invariant: Every wallet operation records holder on the wallet trail, and no entry is changed or removed.
  lifecycle_states:
  - object: actor
    state: unverified
    meaning: An actor is unverified after register actor.
  - object: actor
    state: accepted
    meaning: An actor is accepted after accept actor.
  - object: actor
    state: rejected
    meaning: An actor is rejected after reject actor.
  - object: wallet
    state: active
    meaning: A wallet is active after create wallet.
  business_events:
  - event: Actor registered unverified
    when_it_occurs: When register actor completes
    significance: Others learn that register actor completed without reading the identity records.
  - event: Actor accepted
    when_it_occurs: When accept actor completes
    significance: Others learn that accept actor completed without reading the identity records.
  - event: Actor rejected
    when_it_occurs: When reject actor completes
    significance: Others learn that reject actor completed without reading the identity records.
  - event: Wallet created
    when_it_occurs: When create wallet completes
    significance: Others learn that create wallet completed without reading the wallet records.
  authority_boundaries:
  - business_object: actor
    authoritative_owner: identity
  - business_object: wallet
    authoritative_owner: wallet
  out_of_scope:
  - item: Authenticating callers
    reason: No caller needs an account or a login.
  - item: Wallets of any classification but default
    reason: The business names four classifications, and only default wallets are created.
  - item: Moving value between wallets
    reason: A wallet holds a balance; no act the business asks for moves it.
  governance_scope:
  - scope_item: identity
    relationship: MODIFIED
  - scope_item: wallet
    relationship: MODIFIED
  clarification_requests: []
  acceptance_criteria:
  - criterion: Accept actor is refused when the actor is not recorded.
  - criterion: Accept actor is refused when the actor is not unverified.
  - criterion: Reject actor is refused when the actor is not recorded.
  - criterion: Reject actor is refused when the actor is not unverified.
  - criterion: Create wallet is refused when a wallet that is the same is already recorded.
  - criterion: Create wallet is refused when the actor who would hold it is not recorded.
  - criterion: Create wallet is refused when the actor who would hold it is not accepted.
  identity_and_sameness:
  - business_object: actor
    identified_by: contact address
    two_are_the_same_when: they carry the same contact address
  - business_object: wallet
    identified_by: holder
    two_are_the_same_when: they carry the same holder
  lifecycle_transitions:
  - object: actor
    from_state: unverified
    to_state: accepted
    triggered_by: accept actor
    cascade: None
  - object: actor
    from_state: unverified
    to_state: rejected
    triggered_by: reject actor
    cascade: None
  operation_refusals:
  - operation: accept actor
    refused_when: the actor is not recorded
    business_reason: There is no actor to act on.
  - operation: accept actor
    refused_when: the actor is not unverified
    business_reason: Only an unverified actor becomes accepted.
  - operation: reject actor
    refused_when: the actor is not recorded
    business_reason: There is no actor to act on.
  - operation: reject actor
    refused_when: the actor is not unverified
    business_reason: Only an unverified actor becomes rejected.
  - operation: create wallet
    refused_when: a wallet that is the same is already recorded
    business_reason: Two wallets that are the same would describe one wallet twice.
  - operation: create wallet
    refused_when: the actor who would hold it is not recorded
    business_reason: A wallet no actor holds belongs to nobody the business knows.
  - operation: create wallet
    refused_when: the actor who would hold it is not accepted
    business_reason: Only accepted actors hold wallets.
  authority_deferrals: []
```

Projected from the decision ledger. Business prose (the purpose, each vocabulary definition, what is out of scope) is the ledger's own, word for word; every other row is said from the ledger's structure and claims nothing it does not state.

---

## 0. Subdomain Purpose

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

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← the decision ledger | the owner's answers |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
