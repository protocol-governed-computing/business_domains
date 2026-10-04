# Stage 5 — Business Intent: blockchain / identity and wallet

**Stage:** 5 — Business Intent

**CR:** cr_06_routing_closure

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. The Wallet
subdomain governs the wallet an accepted person is given. Both keep records the business relies on:
the person's record, the address they claimed, the trail of moments in their history, and their
wallet. This change decides what every identity and wallet act does when one of those records cannot
be read or written.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| identity | Governs who an actor is and whether the business trusts them, and ends each of its acts as rejected when a record fails. | S4 actors Identity |
| wallet | Governs the wallet an accepted person is given, and ends its act as rejected when a record fails. | S4 actors Wallet |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Stop a lookup at a failed record | IN_SCOPE | The lookup and the read each end the contract on a failed record. | S4 authoring_scope GAP-01 |
| Stop a wallet step at a failed record | IN_SCOPE | The claim, the write and the append each end their contract on a failed record. | S4 authoring_scope GAP-02 |
| End every act as rejected on a failed record | IN_SCOPE | Each act routes a failed record to its rejected ending. | S4 authoring_scope GAP-03 |
| Tell a refusal apart from a failure | DEFERRED | The business keeps two endings. | S4 authoring_scope Tell a refusal apart from a failure |
| The superseded act's unrouted nodes | DEFERRED | Not dispatched; nothing reaches them. | S4 authoring_scope The superseded act's unrouted nodes |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Actor record | MUTABLE_STATE | Unchanged, and named because a failed read or write of it now ends the act. | S4 bm_entities The Person's Record |
| Contact address registry | IDENTITY_REGISTRY | Unchanged, and named because a failed lookup or claim in it now ends the act. | S4 bm_entities The Claimed Address |
| Wallet record | MUTABLE_STATE | Unchanged, and named because a failed write of it now ends the act. | S4 bm_entities The Wallet |
| Wallet trail | APPEND_ONLY_JOURNAL | Unchanged, and named because a failed append to it now ends the act. | S4 bm_entities The Trail |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Actor record | Contact address | Supplied by the person registering themselves | Two actors never share a contact address; unchanged by this change. | Named by wallet, which looks the person up | S4 bm_entities The Person's Record |
| Wallet record | Wallet identity | Determined when the wallet is created | Two wallets never share an identity; unchanged by this change. | Names the accepted person it belongs to | S4 bm_entities The Wallet |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No act carries on past a record it could not read or write. | A step after a failed record would act on something the business does not hold. | S1 business_invariants #1 |
| Every act ends as succeeded or rejected. | The business keeps two endings. | S1 business_invariants #2 |
| A refusal changes no record. | A refused request leaves the business as it found it, and records made before a failure stay. | S1 business_invariants #3 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Reject | An act whose record failed | A store reports a failed record | IN_SCOPE | S4 capability_graph End every act as rejected on a failed record |
| Stop | A lookup whose record failed | The address registry or the actor record fails | IN_SCOPE | S4 capability_graph Stop a lookup at a failed record |
| Stop | A wallet step whose record failed | The wallet registry, record or trail fails | IN_SCOPE | S4 capability_graph Stop a wallet step at a failed record |
| Distinguish | A failure from a refusal | An act ends on a failed record | DEFERRED | S4 authoring_scope Tell a refusal apart from a failure |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | identity | Wallet looks the person up through identity's lookup; it gains the same answer for a failed record. | S4 dependency_graph blockchain::CC_RESOLVE_ACTOR_V0 |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
