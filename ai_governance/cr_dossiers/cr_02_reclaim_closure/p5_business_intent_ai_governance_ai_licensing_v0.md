# Stage 5 — Business Intent: ai_governance / ai_licensing

**Stage:** 5 — Business Intent

**CR:** cr_02_reclaim_closure

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
| ai_licensing | Governs the business's AI tool licenses, and ends a reclaim the registry refuses with the license still assigned. | S4 actors AI Licensing |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| End a reclaim the registry refuses | IN_SCOPE | The removal step ends the contract on a refused removal. | S4 authoring_scope GAP-01 |
| Tell a refused removal apart from a license still in use | DEFERRED | Both leave the license assigned. | S4 authoring_scope Tell a refused removal apart from a license still in use |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| License registry | IDENTITY_REGISTRY | Unchanged, and named because a refused removal from it now ends the reclaim. | S4 bm_entities The Assignment |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| License registry | Employee | Named by the reclaim request | One assignment per employee; unchanged by this change. | None | S4 bm_entities The Assignment |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No reclaim carries on past a removal the registry refused. | A step after a refused removal would act on an assignment still held. | S1 business_invariants #1 |
| No license is reported reclaimed that the registry did not release. | A revocation announced for a license still held is false. | S1 business_invariants #2 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| End | A reclaim the registry refuses | The registry refuses the removal | IN_SCOPE | S4 capability_graph End a reclaim the registry refuses |

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
