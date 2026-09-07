# Stage 5 — Business Intent: blockchain / wallet
**Stage:** 5 — Business Intent
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

WHAT must be true. Provisional names are admissible here; no bindings, no paths, no addresses.

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Wallet subdomain governs where a person the business has accepted holds value. It holds one
record for each wallet, the balance that wallet carries, the address others may pay to, and the
state that says whether the wallet is in use. A wallet belongs to exactly one accepted person and
follows from their acceptance rather than from a separate request. Wallet is the unit the rest of
the project operates on: a transaction moves value between wallets, a block records transactions,
and consensus finalises blocks. It does not govern whether a person is accepted, who may decide
that, or how value moves once a wallet holds it.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | The seed's paragraph, word for word. This phase adds nothing to it. |

---


### Purpose of every subdomain this change touches

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| wallet | Governs where a person the business has accepted holds value — one record per wallet, its balance, the address others may pay to, and the state that says whether it is in use. | S1 cr_type #1 |
| identity | Governs who a person is and whether the business trusts them: the record of each person, the state that says whether they were accepted, and the trail of moments in their history. This change adds nothing to that. It makes identity announce the three moments it already declares, so that acceptance can be acted on, and enforces the rule identity already stated that a rejection must say why. | S1 cr_type #2 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Giving an accepted person a wallet | IN_SCOPE | The whole of the change. | S4 authoring_scope #1 |
| Establishing the address others may pay to | IN_SCOPE | Worked out from key material the business is supplied. | S4 authoring_scope #2 |
| Somewhere to hold a wallet and its trail | IN_SCOPE | Owned by wallet, written only by wallet. | S4 authoring_scope #3 |
| Announcing the moment a person is registered, accepted or rejected | IN_SCOPE | Owned by identity. Wallet consumes the acceptance moment and declares none of them. | S4 authoring_scope #4 |
| Refusing a rejection that states no grounds | IN_SCOPE | Owned by identity. | S4 authoring_scope #5 |
| Moving value into or out of a wallet | DEFERRED | Transaction does not exist. | S4 authoring_scope deferred #1 |
| Making a wallet inactive, or closing it | DEFERRED | The lifecycle is declared; only creation is built. | S4 authoring_scope deferred #2 |
| Notifying a person that their wallet was created | DEFERRED | The business dropped it. | S4 authoring_scope deferred #3 |
| Giving a wallet to people already accepted | DEFERRED | The business does not go back for them. | S4 authoring_scope deferred #4 |
| Recovering a wallet whose holder has lost access | DEFERRED | The business has not decided what recovery means. | S4 authoring_scope deferred #5 |
| A second wallet for one person | DEFERRED | Not until a second classification is actually needed. | S4 authoring_scope deferred #6 |
| Transaction ordering | DEFERRED | No consumer until transaction exists. | S4 authoring_scope deferred #7 |
| Declaring that the wallet act reads the records identity owns | IN_SCOPE | One statement, and the act stops without it. | S4 authoring_scope #9 |
| Refusing a wallet to a person the business has not accepted | IN_SCOPE | The business declared this refusal and nothing carries it out. | S4 authoring_scope #10 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Wallets | MUTABLE_STATE | A wallet carries a balance and a state that will change over its life. What the business needs is what is true now, not how it got there. | S4 bm_entities #1 |
| Wallet occurrences | APPEND_ONLY_JOURNAL | The moments a wallet's life passes through are added to and never rewritten, so the business can show what happened and when. | S4 bm_entities #3 |
| Wallet identities | IDENTITY_REGISTRY | Claiming a wallet's identity is how the business refuses a second wallet for a person and guarantees no two wallets share one. | S4 constraint_register #3 |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Wallets | The wallet's own identity | Worked out from the person who holds it. | One person holds one wallet, so one person yields one wallet identity. A second attempt resolves to the identity already claimed and creates nothing. | The holder is a person Identity holds and has accepted. Wallet reads that person; it never writes them. | S4 design_decisions #4 |
| Wallet occurrences | The wallet the moment concerns, together with the moment itself | The wallet whose life the moment belongs to. | A moment is never rewritten, so two entries are never the same entry; the trail only grows. | Each moment names the wallet, and through it the person. | S4 constraint_register #6 |
| Wallet identities | The wallet's own identity | The same identity the wallet record carries. | The claim succeeds once. A second claim on the same identity fails, and that failure is how a second wallet is refused. | None. | S4 constraint_register #3 |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| A wallet has exactly one holder. | Value is held by a person, and the business must always be able to say which one. | S4 constraint_register #1 |
| A wallet's balance is never negative, and is zero when created. | A wallet cannot hold less than nothing, and a new wallet has been given nothing. | S4 constraint_register #2 |
| No two wallets share an identity. | Two wallets under one identity make it impossible to say whose value is whose. | S4 constraint_register #3 |
| No wallet exists for a person the business does not hold, or has not accepted. | A wallet follows acceptance. Value held by a person the business never accepted is value it cannot account for. | S4 constraint_register #4 |
| The same request produces the same wallet. | The business must be able to reproduce and check what it did. Key material is supplied to it, never generated by it. | S4 constraint_register #5 |
| A recorded moment is never changed or removed. | The trail is the business's record of what happened; a rewritten record proves nothing. | S4 constraint_register #6 |
| A wallet is written only by wallet, and a person only by identity. | Ownership of a record is what makes it answerable to one function rather than several. | S4 constraint_register #7 |
| Every wallet carries the default classification and the business's single currency. | The business creates one kind of wallet at present, and denominates every one of them the same way. | S4 constraint_register #10 |
| The act that creates a wallet declares every binding it consults. | A reach nobody declared is one no reviewer saw, and it stays invisible until the act runs and asks for a record it never said it would read. | S4 constraint_register #1 |
| Identity is the only writer of what identity owns. | A second writer means two parts of the business decide what is true about a person while neither is answerable for it. | S4 constraint_register #1 |
| No wallet exists for a person the business has not accepted. | A wallet follows acceptance and nothing else. Value held by a person the business never decided about is value it cannot account for, and the decision to give it was made by nobody. | S4 constraint_register #4 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Create a wallet | Wallet | A person being accepted. | IN_SCOPE | S4 capability_graph #1 |
| Record a decision about a person | Holder | An authority recording acceptance or rejection. | IN_SCOPE | S4 capability_graph #5 |
| Register a person | Holder | A person supplying their details. | IN_SCOPE | S4 capability_graph #4 |
| Move value into or out of a wallet | Wallet | Deferred. | DEFERRED | S4 authoring_scope deferred #1 |
| Make a wallet inactive, or close it | Wallet | Deferred. | DEFERRED | S4 authoring_scope deferred #2 |
| Declare the bindings the act consults | Reach | The design of the act that creates a wallet. | IN_SCOPE | S4 capability_graph #9 |
| Refuse a wallet to a person the business has not accepted | Wallet | A wallet being created for a person whose state is not acceptance. | IN_SCOPE | S4 capability_graph #10 |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes optional business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| wallet | IN_WALLET_CREATION_V0 | IN | Admits a request to give an accepted person a wallet, and refuses one that names nobody. | S4 capability_graph #1 |
| wallet | WF_CREATE_WALLET_V0 | WF | The order in which giving an accepted person a wallet is carried out. | S4 capability_graph #1 |
| wallet | CC_REQUIRE_ACCEPTED_HOLDER_V0 | CC | Refuses a wallet for a person the business has not accepted, before anything is claimed or recorded. | S4 capability_graph #1 |
| wallet | CC_DETERMINE_WALLET_IDENTITY_V0 | CC | Works out the wallet's identity from the person who holds it. | S4 capability_graph #8 |
| wallet | CC_CLAIM_WALLET_IDENTITY_V0 | CC | Claims that identity, and refuses when the person already holds a wallet. | S4 capability_graph #9 |
| wallet | CC_ESTABLISH_WALLET_ADDRESS_V0 | CC | Establishes the address others may pay to, from key material supplied. | S4 capability_graph #2 |
| wallet | CC_CREATE_WALLET_RECORD_V0 | CC | Records the wallet with a balance of zero, its denomination and its classification. | S4 capability_graph #6 |
| wallet | CC_APPEND_WALLET_OCCURRENCE_V0 | CC | Records that the wallet was created, for whom, and when. | S4 capability_graph #7 |
| wallet | CT_PURE_DERIVE_WALLET_ADDRESS_V0 | CT | Works out an address from supplied key material. The same material always yields the same address. | S4 design_decisions #2 |
| wallet | EV_WALLET_CREATED_V0 | EV | The moment a person came to hold value. | S4 events #1 |
| wallet | RB_WALLET_BINDINGS_V0 | RB | Reaches the places a wallet, its trail and its claimed identities are held. | S4 gap_register GAP-3 |
| wallet | STRUCTURE_WALLET_STORAGE_V0 | STRUCTURE | Declares where a wallet, its trail and its claimed identities are held. | S4 gap_register GAP-3 |
| wallet | VOCAB_WALLET_CLASSIFICATION_V0 | VOCAB | The set of classifications a wallet may carry, of which only the default is used at present. | S4 constraint_register #10 |
| identity | IN_ACTOR_ACCEPTANCE_V0 | IN | Admits a request to accept a person, and refuses one that names nobody. | S3 authoring_decisions #9 |
| identity | IN_ACTOR_REJECTION_V0 | IN | Admits a request to reject a person, and refuses one that states no grounds. | S3 authoring_decisions #9 |
| identity | WF_ACCEPT_ACTOR_V0 | WF | The order in which an acceptance is recorded and announced. | S3 authoring_decisions #8 |
| identity | WF_REJECT_ACTOR_V0 | WF | The order in which a rejection is recorded and announced, with its grounds required throughout. | S3 authoring_decisions #8 |
| identity | CC_REQUIRE_REJECTION_GROUNDS_V0 | CC | Refuses a rejection that states no grounds, before anything is recorded. | S3 authoring_decisions #9 |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | identity | Establishes that the person is one the business holds, and carries the state that says whether they were accepted. Read only; wallet writes nothing of identity's. | S4 dependency_graph #2 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | Capability graph, gaps, design decisions, authoring scope | COMPLETE |
| Stage 5 — Business Intent | This document | COMPLETE |
