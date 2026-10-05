# Stage 5 — Business Intent: ai_governance / agent_governance

**Stage:** 5 — Business Intent

**CR:** cr_03_parameter_result

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Agent Governance subdomain governs what an AI agent may do on the business's behalf: it accepts an
agent's proposed action, checks that the tool is declared, that the requesting employee holds a
license tier that allows it, and that its parameters satisfy the rules declared for that tool, and
records every action it authorizes or denies. It does not govern which licenses exist, who holds
them, or what a tool does once its action is authorized.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| agent_governance | Checks an agent's action against the rules declared for its tool, and reports only what its checks receive. | S4 actors Agent Governance |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Check an action's parameters | IN_SCOPE | A new version of the parameter check. | S4 authoring_scope GAP-01 |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| A check reports only what it receives. | A reported result nobody received is no result. | S1 business_invariants #1 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Check | An action's parameters | An agent proposes an action | IN_SCOPE | S4 capability_graph Check an action's parameters |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| agent_governance | CC_VALIDATE_TOOL_PARAMETERS_V1 | CC | Enforce declared parameter constraints for an authorized tool, reporting whether every rule passed. | S4 design_decisions #2 |

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
