# Stage 5 — Business Intent: blockchain / identity

**Stage:** 5 — Business Intent

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Identity subdomain governs who an actor is and whether the business trusts them. It holds one
record for each person known to the system, the state that says whether the business has accepted
them, and the record of every moment in their history. A person supplies their own details and is
admitted unverified; separately, an authority records a decision accepting or rejecting them. The
details a person was admitted with are theirs and stay theirs: a decision records whether the
business trusts someone, and it may change only three things about them — their state, the authority
that decided, and the grounds stated. Identity also decides what of itself is offered to callers
outside it. It does not govern what a trusted actor may then do, which persons may be an authority,
or who a caller is.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | The seed states that a person's admitted details survive the decision made about them. This states the same rule as a bound rather than a promise: three things a decision may change, and everything else it may not. Nothing here contradicts the seed or either earlier change; what it adds is the enumeration, which is what makes the rule something a mechanism can hold rather than something a document asserts. |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Record a decision against a registered person | IN_SCOPE | One step of the contract changes; its refusals, inputs and result statuses do not. | S4 authoring_scope GAP-01 |
| State which of a person's details a decision may change | IN_SCOPE | The three the business names become the fields the change sets. | S4 authoring_scope GAP-02 |
| Assemble the record a decision writes | DEFERRED | Retained unchanged, and left without a consumer by this change. | S4 authoring_scope Assemble the record a decision writes |
| Say which artifacts consume a store | DEFERRED | Owned by the components that build the composition's indexes, not by a business domain. | S4 authoring_scope Say which artifacts consume a store |
| Restoring details lost from records already thinned | DEFERRED | Declined by the business; the record is added to and never rewritten. | S4 authoring_scope Restoring details lost from records already thinned |
| Correcting a person's own details | DEFERRED | Deferred by the business and unchanged. | S4 authoring_scope Correcting a person's own details |
| Enforcing that a rejection states grounds inside the business | DEFERRED | Unchanged by this change and enforced at the boundary only. | S4 authoring_scope Enforcing that a rejection states grounds inside the business |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Actor record | MUTABLE_STATE | Unchanged by this change and named because what changes is how it is written. It holds one record per person, whose state changes when a decision is recorded and whose admitted details must survive that change. | S4 bm_entities The Record |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Actor record | Contact address | Supplied by the person registering themselves | Two actors never share a contact address, unchanged and established by the change that created the function. This change addresses the record by that key and depends on no property beyond the key identifying one record. | None — the actor is named by later subdomains and names none | S4 design_decisions #3 |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| A person's admitted details survive every decision recorded about them. | The business decided at the outset that a person keeps what they were admitted with. Nothing an authority does should change who a person said they were. | S1 business_invariants #1 |
| A decision changes the person's state, the authority named and the grounds, and nothing else about them. | Naming what a decision may change is what makes everything else safe from it. Stated as a bound rather than an intention, it is something a mechanism can hold. | S1 business_invariants #2 |
| No decision alters a detail the person supplied themselves. | A decision records a decision. Changing a person's details is a different act, and one the business has deferred. | S1 business_invariants #3 |
| A record already written is never rewritten, however thin it is. | The business would rather carry a thin old record than start editing history. | S1 business_invariants #4 |
| What a caller sends and what they are told back is unchanged by how a decision is written. | The business is correcting how it does something, not what it offers, and a caller should not be able to tell. | S1 business_invariants #5 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Decide | A registered person, accepted or rejected, keeping everything they were admitted with | An authority records a decision against a registered person | IN_SCOPE | S4 capability_graph Record a decision against a registered person |
| Bound | What a decision may change about a person, to the state, the authority and the grounds | The business states which details a decision is entitled to touch | IN_SCOPE | S4 capability_graph State which of a person's details a decision may change |
| Correct | A person's own registered details | A person's name or address changes after admission | DEFERRED | S4 authoring_scope Correcting a person's own details |
| Restore | Details lost from a record thinned before this change | The business chooses to repair what it has already recorded | DEFERRED | S4 authoring_scope Restoring details lost from records already thinned |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|------------------|-------------------------|---------|----------------|

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| NONE IDENTIFIED | | | |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
