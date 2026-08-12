# Stage 6 — Governance Intent: blockchain / wallet
**Stage:** 6 — Governance Intent
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `blockchain` |
| Primary subdomain | `wallet` — NEW — declared by this CR |
| Secondary subdomain | `identity` — EXISTING — extended by this CR, and the owner of what is extended |
| Authority class | reuse existing — a person acts on their own behalf, an authority decides about them; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Wallet stands alone rather than nesting under identity because a wallet is a thing the business holds
in its own right, with its own identity, its own record and its own trail. Placing it inside identity
would make identity the owner of value as well as of who a person is, and would leave the record of
people written by a function that is not about people.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Giving an accepted person a wallet | wallet | OWNED | | S4 gap_register GAP-1 |
| Establishing the address others may pay to | wallet | OWNED | | S4 gap_register GAP-2 |
| Somewhere to hold a wallet and its trail | wallet | OWNED | | S4 gap_register GAP-3 |
| Announcing the moment a person is registered, accepted or rejected | identity | OWNED | | S4 gap_register GAP-4 |
| Refusing a rejection that states no grounds | identity | OWNED | | S4 gap_register GAP-5 |
| Holding a wallet | wallet | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph #6 |
| Recording that a wallet was created | wallet | SATISFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 | S4 capability_graph #7 |
| Determining a wallet's identity | wallet | SATISFIED | capability_transforms::CT_PURE_GENERATE_ID_V0 | S4 capability_graph #8 |
| Ensuring two wallets never share an identity | wallet | SATISFIED | capability_side_effects::CS_REGISTRY_V0 | S4 capability_graph #9 |
| Establishing that a person is held and accepted | identity | SATISFIED | blockchain::CC_RESOLVE_ACTOR_V0 | S4 capability_graph #10 |
| Supplying the time a moment occurred | wallet | SATISFIED | capability_side_effects::CS_CLOCK_V0 | S4 capability_graph #11 |
| Moving value into or out of a wallet | wallet | DEFERRED | | S4 authoring_scope deferred #1 |
| Making a wallet inactive, or closing it | wallet | DEFERRED | | S4 authoring_scope deferred #2 |
| Notifying a person that their wallet was created | wallet | DEFERRED | | S4 authoring_scope deferred #3 |
| Recovering a wallet whose holder has lost access | wallet | DEFERRED | | S4 authoring_scope deferred #5 |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| Somewhere to hold a wallet | Holds what is true of a wallet now — its holder, its balance, its address, its denomination, its classification and its state. | wallet | S5 business_objects #1 |
| Somewhere to hold a wallet's trail | Holds the moments a wallet's life passes through, added to and never rewritten. | wallet | S5 business_objects #2 |
| Somewhere to claim a wallet's identity | Holds the identities already claimed, so that a second wallet for one person is refused by the claim failing. | wallet | S5 business_objects #3 |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Establishing that a person is one the business holds, and carrying the state that says whether they were accepted | wallet → identity | blockchain::CC_RESOLVE_ACTOR_V0 | SATISFIED | S5 cross_subdomain_refs #1 |
| The moment a person is accepted being announced, so that giving them a wallet has something to follow | wallet → identity | blockchain::EV_ACTOR_ACCEPTED_V0 | GAP | S4 dependency_graph #1 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Records a decision, announces nothing, and does not require grounds on a rejection. | EXTEND | S4 gap_register GAP-4 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Records the decision. Does not read the grounds stated. | EXTEND | S4 gap_register GAP-5 |
| blockchain::WF_REGISTER_ACTOR_V0 | Admits a person unverified, and announces nothing. | EXTEND | S4 gap_register GAP-4 |
| blockchain::EV_ACTOR_ACCEPTED_V0 | Declared. Referred to by nothing. | REUSE | S4 dependency_graph #1 |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | Declared. Referred to by nothing. | REUSE | S4 gap_register GAP-4 |
| blockchain::EV_ACTOR_REJECTED_V0 | Declared. Referred to by nothing. | REUSE | S4 gap_register GAP-4 |
| blockchain::CC_RESOLVE_ACTOR_V0 | Resolves a person and carries their state. | REUSE | S5 cross_subdomain_refs #1 |
| blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0 | Declares what the domain compiles. It does not know of a second subdomain. | REVIEW | S4 gap_register GAP-3 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| WALLET_WRITES_ONLY_ITS_OWN | Wallet writes the three places it owns and no other. It never writes a person, a person's trail, or anything identity owns. | S4 constraint_register #7 |
| IDENTITY_WRITES_ONLY_ITS_OWN | Identity writes people and their trail. It never writes a wallet, and it does not create one. | S4 constraint_register #7 |
| ANNOUNCEMENT_OWNED_BY_ITS_SUBJECT | The moments a person is registered, accepted or rejected are identity's, because they are moments in a person's life. Wallet consumes the acceptance moment and declares none of the three. A consumer never owns the announcement it waits on. | S4 gap_register GAP-4 |
| WALLET_READS_A_PERSON_NEVER_WRITES_ONE | Wallet establishes that a person is held and accepted by reading what identity already offers. It does not restate a person's state, and it does not correct one. | S5 cross_subdomain_refs #1 |
| ACCEPTANCE_STANDS_ALONE | A wallet that cannot be created does not un-accept the person. The two are separate acts and fail separately. | S4 design_decisions #7 |
| NO_NEW_WAY_TO_TOUCH_THE_WORLD | This change adds no way for the platform to touch the world. Everything it does to anything is one of the ways that already exist. | S4 design_decisions #2 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Giving an accepted person a wallet | wallet | S4 gap_register GAP-1 |
| Establishing the address others may pay to | wallet | S4 gap_register GAP-2 |
| Somewhere to hold a wallet and its trail | wallet | S4 gap_register GAP-3 |
| Announcing the moment a person is registered, accepted or rejected | identity | S4 gap_register GAP-4 |
| Refusing a rejection that states no grounds | identity | S4 gap_register GAP-5 |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, objects, identity semantics, invariants, actions, provisional codes | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
