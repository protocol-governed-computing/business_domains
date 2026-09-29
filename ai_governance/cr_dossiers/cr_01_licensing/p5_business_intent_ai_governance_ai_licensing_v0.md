# Stage 5 — Business Intent: ai_governance / ai_licensing

**Stage:** 5 — Business Intent

**CR:** cr_01_licensing

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
employee while licenses remain under the business's cap and once the employee has completed the
required training, and reclaiming a license that has gone unused for the business's threshold of
days. Each of its checks refuses when its answer is no. It does not govern what an agent may do,
which employees exist, or which tools the business licenses.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| ai_licensing | Governs the business's AI tool licenses, and now proves each check it decides them by. | S4 bm_entities The Case |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Prove the license check | IN_SCOPE | Stated with its cases; decides nothing new. | S4 authoring_scope GAP-01 |
| Prove the training check | IN_SCOPE | Stated with its cases; decides nothing new. | S4 authoring_scope GAP-02 |
| Prove the inactivity check | IN_SCOPE | Stated with its cases; decides nothing new. | S4 authoring_scope GAP-03 |
| Compile the cases stated beside each check | IN_SCOPE | Reached through its generator. | S4 authoring_scope GAP-04 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED | | | |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED | | | | | |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No check answers no; a no is a refusal. | A check that answered no would let its act continue. | S1 business_invariants #1 |
| Every check is proven on every build by the cases stated beside it. | A check nothing proves can change unseen. | S1 business_invariants #2 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Prove | Each check, by its cases | Every build | IN_SCOPE | S4 capability_graph Prove the license check |

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
