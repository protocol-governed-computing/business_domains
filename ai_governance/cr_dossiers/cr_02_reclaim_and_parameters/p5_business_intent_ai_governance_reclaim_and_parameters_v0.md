# Stage 5 — Business Intent: ai_governance / reclaim and parameter result

**Stage:** 5 — Business Intent

**CR:** cr_02_reclaim_and_parameters

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
employee, and reclaiming a license that has gone unused for the business's threshold of days. The
Agent Governance subdomain governs what an AI agent may do on the business's behalf: it judges an
agent's proposed action, checks its parameters against the rules declared for the tool, and records
every action it authorizes or denies. This change decides what a reclaim does when the registry
refuses it and what the parameter check reports, and states each act it changes under a new identity.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| ai_licensing | Governs the business's AI tool licenses, and ends a reclaim the registry refuses with the license still assigned. | S4 actors AI Licensing |
| agent_governance | Checks an agent's action against the rules declared for its tool, and reports only what its checks receive. | S4 actors Agent Governance |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| End a reclaim the registry refuses | IN_SCOPE | A next version of the reclaim, whose removal step ends the contract on a refused removal. | S4 authoring_scope GAP-01 |
| Check an action's parameters | IN_SCOPE | A next version of the parameter check. | S4 authoring_scope GAP-02 |
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
| A check reports only what it receives. | A reported result nobody received is no result. | S1 business_invariants #3 |
| A published identity means what it meant when it was published. | A citation of v5 relies on what v5 said. | S1 business_invariants #4 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| End | A reclaim the registry refuses | The registry refuses the removal | IN_SCOPE | S4 capability_graph End a reclaim the registry refuses |
| Check | An action's parameters | An agent proposes an action | IN_SCOPE | S4 capability_graph Check an action's parameters |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| ai_licensing | CC_RECLAIM_UNUSED_LICENSE_V1 | CC | Reclaim license from inactive user. | S4 design_decisions #4 |
| agent_governance | CC_VALIDATE_TOOL_PARAMETERS_V1 | CC | Enforce declared parameter constraints for an authorized tool, reporting whether every rule passed. | S4 design_decisions #4 |

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
