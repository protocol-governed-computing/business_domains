# Stage 5 — Business Intent: blockchain / wallet

## Machine

```yaml
document:
  phase: p5
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Wallet subdomain governs where a person the business has accepted holds value. It holds one
    record for each wallet, the balance that wallet carries, the address others may pay to, and the
    state that says whether the wallet is in use. A wallet belongs to exactly one accepted person and
    follows from their acceptance rather than from a separate request. Wallet is the unit the rest of
    the project operates on: a transaction moves value between wallets, a block records transactions,
    and consensus finalises blocks. It does not govern whether a person is accepted, who may decide
    that, or how value moves once a wallet holds it.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: The seed's paragraph, word for word. This phase adds nothing to it.
  subdomain_purposes:
  - subdomain: wallet
    purpose: Governs where a person the business has accepted holds value — one record per wallet, its balance, the address others may pay to, and the state that says whether it is in use.
    source_finding: {phase: p1, register: cr_type, row: 1}
  - subdomain: identity
    purpose: 'Governs who a person is and whether the business trusts them: the record of each person, the state that says whether they were accepted, and the trail of moments in their history. This change adds nothing to that. It makes identity announce the three moments it already declares, so that acceptance can be acted on, and enforces the rule identity already stated that a rejection must say why.'
    source_finding: {phase: p1, register: cr_type, row: 2}
  scope_boundary:
  - capability: Giving an accepted person a wallet
    status: IN_SCOPE
    notes: The whole of the change.
    source_finding: {phase: p4, register: authoring_scope, row: 1}
  - capability: Establishing the address others may pay to
    status: IN_SCOPE
    notes: Worked out from key material the business is supplied.
    source_finding: {phase: p4, register: authoring_scope, row: 2}
  - capability: Somewhere to hold a wallet and its trail
    status: IN_SCOPE
    notes: Owned by wallet, written only by wallet.
    source_finding: {phase: p4, register: authoring_scope, row: 3}
  - capability: Announcing the moment a person is registered, accepted or rejected
    status: IN_SCOPE
    notes: Owned by identity. Wallet consumes the acceptance moment and declares none of them.
    source_finding: {phase: p4, register: authoring_scope, row: 4}
  - capability: Refusing a rejection that states no grounds
    status: IN_SCOPE
    notes: Owned by identity.
    source_finding: {phase: p4, register: authoring_scope, row: 5}
  - capability: Moving value into or out of a wallet
    status: DEFERRED
    notes: Transaction does not exist.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Making a wallet inactive, or closing it
    status: DEFERRED
    notes: The lifecycle is declared; only creation is built.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: Notifying a person that their wallet was created
    status: DEFERRED
    notes: The business dropped it.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  - capability: Giving a wallet to people already accepted
    status: DEFERRED
    notes: The business does not go back for them.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #4'}
  - capability: Recovering a wallet whose holder has lost access
    status: DEFERRED
    notes: The business has not decided what recovery means.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #5'}
  - capability: A second wallet for one person
    status: DEFERRED
    notes: Not until a second classification is actually needed.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #6'}
  - capability: Transaction ordering
    status: DEFERRED
    notes: No consumer until transaction exists.
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #7'}
  - capability: Declaring that the wallet act reads the records identity owns
    status: IN_SCOPE
    notes: One statement, and the act stops without it.
    source_finding: {phase: p4, register: authoring_scope, row: 9}
  - capability: Refusing a wallet to a person the business has not accepted
    status: IN_SCOPE
    notes: The business declared this refusal and nothing carries it out.
    source_finding: {phase: p4, register: authoring_scope, row: 10}
  business_objects:
  - store_name: Wallets
    record_model: MUTABLE_STATE
    business_rationale: A wallet carries a balance and a state that will change over its life. What the business needs is what is true now, not how it got there.
    source_finding: {phase: p4, register: bm_entities, row: 1}
  - store_name: Wallet occurrences
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: The moments a wallet's life passes through are added to and never rewritten, so the business can show what happened and when.
    source_finding: {phase: p4, register: bm_entities, row: 3}
  - store_name: Wallet identities
    record_model: IDENTITY_REGISTRY
    business_rationale: Claiming a wallet's identity is how the business refuses a second wallet for a person and guarantees no two wallets share one.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  identity_semantics:
  - store_name: Wallets
    identity_field: The wallet's own identity
    source: Worked out from the person who holds it.
    uniqueness_rule: One person holds one wallet, so one person yields one wallet identity. A second attempt resolves to the identity already claimed and creates nothing.
    cross_subdomain_relationship: The holder is a person Identity holds and has accepted. Wallet reads that person; it never writes them.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - store_name: Wallet occurrences
    identity_field: The wallet the moment concerns, together with the moment itself
    source: The wallet whose life the moment belongs to.
    uniqueness_rule: A moment is never rewritten, so two entries are never the same entry; the trail only grows.
    cross_subdomain_relationship: Each moment names the wallet, and through it the person.
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - store_name: Wallet identities
    identity_field: The wallet's own identity
    source: The same identity the wallet record carries.
    uniqueness_rule: The claim succeeds once. A second claim on the same identity fails, and that failure is how a second wallet is refused.
    cross_subdomain_relationship: None.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  invariants:
  - invariant: A wallet has exactly one holder.
    business_reason: Value is held by a person, and the business must always be able to say which one.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: A wallet's balance is never negative, and is zero when created.
    business_reason: A wallet cannot hold less than nothing, and a new wallet has been given nothing.
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: No two wallets share an identity.
    business_reason: Two wallets under one identity make it impossible to say whose value is whose.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - invariant: No wallet exists for a person the business does not hold, or has not accepted.
    business_reason: A wallet follows acceptance. Value held by a person the business never accepted is value it cannot account for.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - invariant: The same request produces the same wallet.
    business_reason: The business must be able to reproduce and check what it did. Key material is supplied to it, never generated by it.
    source_finding: {phase: p4, register: constraint_register, row: 5}
  - invariant: A recorded moment is never changed or removed.
    business_reason: The trail is the business's record of what happened; a rewritten record proves nothing.
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - invariant: A wallet is written only by wallet, and a person only by identity.
    business_reason: Ownership of a record is what makes it answerable to one function rather than several.
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - invariant: Every wallet carries the default classification and the business's single currency.
    business_reason: The business creates one kind of wallet at present, and denominates every one of them the same way.
    source_finding: {phase: p4, register: constraint_register, row: 10}
  - invariant: The act that creates a wallet declares every binding it consults.
    business_reason: A reach nobody declared is one no reviewer saw, and it stays invisible until the act runs and asks for a record it never said it would read.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: Identity is the only writer of what identity owns.
    business_reason: A second writer means two parts of the business decide what is true about a person while neither is answerable for it.
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: No wallet exists for a person the business has not accepted.
    business_reason: A wallet follows acceptance and nothing else. Value held by a person the business never decided about is value it cannot account for, and the decision to give it was made by nobody.
    source_finding: {phase: p4, register: constraint_register, row: 4}
  actions:
  - action: Create a wallet
    object: Wallet
    trigger: A person being accepted.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - action: Record a decision about a person
    object: Holder
    trigger: An authority recording acceptance or rejection.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 5}
  - action: Register a person
    object: Holder
    trigger: A person supplying their details.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 4}
  - action: Move value into or out of a wallet
    object: Wallet
    trigger: Deferred.
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - action: Make a wallet inactive, or close it
    object: Wallet
    trigger: Deferred.
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - action: Declare the bindings the act consults
    object: Reach
    trigger: The design of the act that creates a wallet.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 9}
  - action: Refuse a wallet to a person the business has not accepted
    object: Wallet
    trigger: A wallet being created for a person whose state is not acceptance.
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, row: 10}
  provisional_codes:
  - subdomain: wallet
    provisional_code: IN_WALLET_CREATION_V0
    family: IN
    summary: Admits a request to give an accepted person a wallet, and refuses one that names nobody.
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - subdomain: wallet
    provisional_code: WF_CREATE_WALLET_V0
    family: WF
    summary: The order in which giving an accepted person a wallet is carried out.
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - subdomain: wallet
    provisional_code: CC_REQUIRE_ACCEPTED_HOLDER_V0
    family: CC
    summary: Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded.
    source_finding: {phase: p4, register: capability_graph, row: 1}
  - subdomain: wallet
    provisional_code: CC_DETERMINE_WALLET_IDENTITY_V0
    family: CC
    summary: Works out the wallet's identity from the person who holds it.
    source_finding: {phase: p4, register: capability_graph, row: 8}
  - subdomain: wallet
    provisional_code: CC_CLAIM_WALLET_IDENTITY_V0
    family: CC
    summary: Claims that identity, and refuses when the person already holds a wallet.
    source_finding: {phase: p4, register: capability_graph, row: 9}
  - subdomain: wallet
    provisional_code: CC_ESTABLISH_WALLET_ADDRESS_V0
    family: CC
    summary: Establishes the address others may pay to, from key material supplied.
    source_finding: {phase: p4, register: capability_graph, row: 2}
  - subdomain: wallet
    provisional_code: CC_CREATE_WALLET_RECORD_V0
    family: CC
    summary: Records the wallet with a balance of zero, its denomination and its classification.
    source_finding: {phase: p4, register: capability_graph, row: 6}
  - subdomain: wallet
    provisional_code: CC_APPEND_WALLET_OCCURRENCE_V0
    family: CC
    summary: Records that the wallet was created, for whom, and when.
    source_finding: {phase: p4, register: capability_graph, row: 7}
  - subdomain: wallet
    provisional_code: CT_PURE_DERIVE_WALLET_ADDRESS_V0
    family: CT
    summary: Works out an address from supplied key material. The same material always yields the same address.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - subdomain: wallet
    provisional_code: EV_WALLET_CREATED_V0
    family: EV
    summary: The moment a person came to hold value.
    source_finding: {phase: p4, register: events, row: 1}
  - subdomain: wallet
    provisional_code: RB_WALLET_BINDINGS_V0
    family: RB
    summary: Reaches the places a wallet, its trail and its claimed identities are held.
    source_finding: {phase: p4, register: gap_register, key: GAP-3}
  - subdomain: wallet
    provisional_code: STRUCTURE_WALLET_STORAGE_V0
    family: STRUCTURE
    summary: Declares where a wallet, its trail and its claimed identities are held.
    source_finding: {phase: p4, register: gap_register, key: GAP-3}
  - subdomain: wallet
    provisional_code: VOCAB_WALLET_CLASSIFICATION_V0
    family: VOCAB
    summary: The set of classifications a wallet may carry, of which only the default is used at present.
    source_finding: {phase: p4, register: constraint_register, row: 10}
  - subdomain: identity
    provisional_code: IN_ACTOR_ACCEPTANCE_V0
    family: IN
    summary: Admits a request to accept a person, and refuses one that names nobody.
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
  - subdomain: identity
    provisional_code: IN_ACTOR_REJECTION_V0
    family: IN
    summary: Admits a request to reject a person, and refuses one that states no grounds.
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
  - subdomain: identity
    provisional_code: WF_ACCEPT_ACTOR_V0
    family: WF
    summary: The order in which an acceptance is recorded and announced.
    source_finding: {phase: p3, register: authoring_decisions, row: 8}
  - subdomain: identity
    provisional_code: WF_REJECT_ACTOR_V0
    family: WF
    summary: The order in which a rejection is recorded and announced, with its grounds required throughout.
    source_finding: {phase: p3, register: authoring_decisions, row: 8}
  - subdomain: identity
    provisional_code: CC_REQUIRE_REJECTION_GROUNDS_V0
    family: CC
    summary: Refuses a rejection that states no grounds, before anything is recorded.
    source_finding: {phase: p3, register: authoring_decisions, row: 9}
  cross_subdomain_refs:
  - cc_code: blockchain::CC_RESOLVE_ACTOR_V0
    defined_in: identity
    role: Establishes that the person is one the business holds, and carries the state that says whether they were accepted. Read only; wallet writes nothing of identity's.
    source_finding: {phase: p4, register: dependency_graph, row: 2}
```

WHAT must be true. Provisional names are admissible here; no bindings, no paths, no addresses.

---

## 1. Subdomain Purpose

---

### Purpose of every subdomain this change touches

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

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
