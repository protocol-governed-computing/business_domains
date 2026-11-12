# Stage 5 — Business Intent — blockchain / identity, wallet

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_11_repeat_announces
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: The blockchain domain governs identity and wallets. Identity says who an actor is and whether the business trusts them. Wallet says where a person the business has accepted holds value.
  purpose_provenance:
  - source: Change seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: null
  subdomain_purposes:
  - subdomain: identity
    purpose: Identity says who an actor is and whether the business trusts them. A person registers and is admitted unverified, and an authority accepts or rejects them once.
    source_finding: {phase: p0, register: cr_type, row: 1}
  - subdomain: wallet
    purpose: Wallet says where a person the business has accepted holds value. An accepted person is given exactly one wallet, formed from the public key they supply. Wallet reads identity's records and never writes them.
    source_finding: {phase: p0, register: cr_type, row: 2}
  scope_boundary:
  - capability: Register actor
    status: IN_SCOPE
    notes: Records a new actor
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - capability: Accept actor
    status: IN_SCOPE
    notes: Moves an actor from unverified to accepted
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - capability: Reject actor
    status: IN_SCOPE
    notes: Moves an actor from unverified to rejected
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - capability: List actors
    status: IN_SCOPE
    notes: Returns the actors that match
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - capability: Create wallet
    status: IN_SCOPE
    notes: Records a new wallet
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - capability: Authenticating callers
    status: DEFERRED
    notes: No caller needs an account or a login.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - capability: Wallets of any classification but default
    status: DEFERRED
    notes: The business names four classifications, and only default wallets are created.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - capability: Moving value between wallets
    status: DEFERRED
    notes: A wallet holds a balance; no act the business asks for moves it.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  business_objects:
  - store_name: Actor record
    record_model: MUTABLE_STATE
    business_rationale: The business must know who registered, by their contact address, and whether it trusts them, keeping what they registered with.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - store_name: Wallet record
    record_model: MUTABLE_STATE
    business_rationale: The business must know where a person it has accepted holds value, one wallet to each such person.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - store_name: Wallet identity registry
    record_model: IDENTITY_REGISTRY
    business_rationale: Telling one wallet from another needs a claim on its identity at the moment it is recorded.
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  - store_name: Audit trail of identity
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - store_name: Audit trail of wallet
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  identity_semantics:
  - store_name: Actor record
    identity_field: Contact address
    source: Supplied with the request
    uniqueness_rule: Two actors are the same when they carry the same contact address.
    cross_subdomain_relationship: None
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  - store_name: Wallet record
    identity_field: Holder
    source: Formed by the business
    uniqueness_rule: Two wallets are the same when they carry the same holder.
    cross_subdomain_relationship: Names exactly one actor
    source_finding: {phase: p0, register: identity_and_sameness, row: 2}
  invariants:
  - invariant: Recording an actor again with the same contact address records the repeat, and the actor already recorded is unchanged by it.
    business_reason: The business keeps one record of each actor, and a repeat does not undo what was decided.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No two wallets share their holder.
    business_reason: Two wallets that are the same would describe one wallet twice.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: Each wallet is held by one actor who is accepted.
    business_reason: A wallet no actor holds belongs to nobody the business knows.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Every identity operation records contact address, verifying authority and grounds on the identity trail, and no entry is changed or removed.
    business_reason: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: Every wallet operation records holder on the wallet trail, and no entry is changed or removed.
    business_reason: Every operation must be traceable afterwards, and a trail that could be amended would not be evidence.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  actions:
  - action: Register actor
    object: actor
    trigger: Requested by the participant
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - action: Accept actor
    object: actor
    trigger: Requested by the participant
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - action: Reject actor
    object: actor
    trigger: Requested by the participant
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - action: List actors
    object: actor
    trigger: Requested by the participant
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - action: Create wallet
    object: wallet
    trigger: Requested by the participant
    status: IN_SCOPE
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  provisional_codes:
  - subdomain: identity
    provisional_code: WF_REGISTER_ACTOR_V0
    family: WF
    summary: Records a new actor
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - subdomain: identity
    provisional_code: WF_ACCEPT_ACTOR_V0
    family: WF
    summary: Moves an actor from unverified to accepted
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - subdomain: identity
    provisional_code: WF_REJECT_ACTOR_V0
    family: WF
    summary: Moves an actor from unverified to rejected
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - subdomain: identity
    provisional_code: WF_LIST_ACTORS_V0
    family: WF
    summary: Returns the actors that match
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - subdomain: wallet
    provisional_code: WF_CREATE_WALLET_V0
    family: WF
    summary: Records a new wallet
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  cross_subdomain_refs: []
```

Projected from the change seed, which is projected from the decision ledger. Every row cites the seed row it restates.

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Change seed | actions · business_objects · cross_subdomain_refs · identity_semantics · invariants · provisional_codes · purpose_provenance · scope_boundary · subdomain_purpose · subdomain_purposes |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
