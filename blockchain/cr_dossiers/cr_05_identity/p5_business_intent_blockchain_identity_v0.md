# Stage 5 — Business Intent: blockchain / identity

**Stage:** 5 — Business Intent

**CR:** cr_05_identity

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
business trusts someone, and it is not an occasion to alter who they said they were. Identity also
decides what of itself is offered to callers outside it. It does not govern what a trusted actor may
then do, which persons may be an authority, or who a caller is.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| identity | Governs who an actor is and whether the business trusts them, and now holds every rule it applies to that question. | S4 bm_entities The Business's Rules |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Check a registration and refuse an incomplete one | IN_SCOPE | The check holds what a registration must contain and refuses on what it finds. | S4 authoring_scope GAP-01 |
| Record a decision only about an unverified person, and only an acceptance or a rejection | IN_SCOPE | The deciding step holds both sets and builds the record from the decision it checked. | S4 authoring_scope GAP-02 |
| Refuse an authority deciding about themselves | IN_SCOPE | A comparison and a fixed rule on its result. | S4 authoring_scope GAP-03 |
| Refuse a rejection stating no grounds | IN_SCOPE | The grounds step holds its own rules. | S4 authoring_scope GAP-04 |
| Fix the decision each act records | IN_SCOPE | Each act records its own decision. | S4 authoring_scope GAP-05 |
| Register a person unverified | IN_SCOPE | The registration act writes the state unverified as its own. | S4 authoring_scope GAP-06 |
| Reach identity from outside | IN_SCOPE | The entrances stop supplying what identity holds; nothing a caller sends or is told changes. | S4 authoring_scope GAP-07 |
| Admit an acceptance with its grounds | IN_SCOPE | The acceptance gate declares the optional grounds the act reads. | S4 authoring_scope GAP-08 |
| Admit a registration without the schema identity holds | IN_SCOPE | The registration gate stops requiring what identity now holds. | S4 authoring_scope GAP-10 |
| Record the moment of each act as the act's own | DEFERRED | The moment and its stream stay the request's to name. | S4 authoring_scope Record the moment of each act as the act's own |
| Records made under a request's own rules | DEFERRED | Declined by the business; the record is added to and never rewritten. | S4 authoring_scope Records made under a request's own rules |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Actor record | MUTABLE_STATE | Unchanged by this change, and named because what changes is what may be written into it: a registration only as unverified, a decision only as the one checked. | S4 bm_entities The Record |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Actor record | Contact address | Supplied by the person registering themselves | Two actors never share a contact address; unchanged by this change. | None — the actor is named by later subdomains and names none | S4 bm_entities The Record |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No person is registered without a name and an address they are reached at. | The business said both are required. | S1 business_invariants #1 |
| No person is decided about more than once. | Only an unverified person may be accepted or rejected. | S1 business_invariants #2 |
| No decision other than an acceptance or a rejection is recorded. | There is no third decision. | S1 business_invariants #3 |
| No rejection is recorded without its grounds. | The business decided a rejection must say why. | S1 business_invariants #4 |
| No authority decides about themselves. | A decision about oneself is not a decision by the business. | S1 business_invariants #5 |
| A business rule of identity's is held by identity, and no request changes it. | A business rule the caller supplies is a business rule the caller can widen. | S1 business_invariants #6 |
| A refusal changes no record. | A refused request leaves the business as it found it. | S1 business_invariants #7 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Register | A person, held unverified, whose registration is complete | A person supplies a registration | IN_SCOPE | S4 capability_graph Register a person unverified |
| Refuse | A registration missing its name or address | A person supplies an incomplete registration | IN_SCOPE | S4 capability_graph Check a registration and refuse an incomplete one |
| Accept | An unverified person, decided about by someone other than themselves | An authority records an acceptance | IN_SCOPE | S4 capability_graph Record a decision only about an unverified person, and only an acceptance or a rejection |
| Reject | An unverified person, with grounds, decided about by someone other than themselves | An authority records a rejection | IN_SCOPE | S4 capability_graph Refuse a rejection stating no grounds |
| Name the moment | The moment each act records | An act completes | DEFERRED | S4 authoring_scope Record the moment of each act as the act's own |

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
| NONE IDENTIFIED | | | |

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 4 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
