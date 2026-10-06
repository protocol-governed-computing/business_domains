# Stage 6 — Governance Intent: ai_governance / reclaim and parameter result

**Stage:** 6 — Governance Intent

**CR:** cr_02_reclaim_and_parameters

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Nothing moves and nothing is added: the reclaim belongs to AI Licensing.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| End a reclaim the registry refuses | ai_licensing | OWNED | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | S5 scope_boundary End a reclaim the registry refuses |
| Tell a refused removal apart from a license still in use | ai_licensing, in a later change | DEFERRED |  | S5 scope_boundary Tell a refused removal apart from a license still in use |
| Check an action's parameters | agent_governance | OWNED | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | S5 scope_boundary Check an action's parameters |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of which employee holds which license | Unchanged; a refused removal from it now ends the reclaim | ai_licensing | S5 business_objects License registry |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Keeping the license registry | ai_licensing -> platform | capability_side_effects::CS_REGISTRY_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_REGISTRY_V0 |
| Checking against rules | agent_governance -> capability_transforms | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| Looking up a tool's rules | agent_governance -> capability_transforms | capability_transforms::CT_PURE_LOOKUP_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_LOOKUP_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Present; its removal step does not answer a refused removal; published in v5 | REPLACE | S4 design_decisions #4 |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | Present and reused unchanged | REUSE | S4 dependency_graph ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 |
| ai_governance::WF_AUTO_RECLAIM_V0 | Present; already routes VIOLATION to still active; runs the reclaim being replaced | REVIEW | S4 design_decisions #5 |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | Present; reports a result it never receives; published in v5 | REPLACE | S4 design_decisions #4 |
| ai_governance::WF_GOVERN_AGENT_ACTION_V0 | Present; runs the parameter check being replaced | REVIEW | S4 design_decisions #5 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| capability_transforms::CT_PURE_LOOKUP_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_LOOKUP_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_STEP_ANSWERS_FOR_ITS_STORE | The removal step answers every outcome the registry declares, and ends the contract on each. | S4 design_decisions #1 |
| A_LICENSE_NOT_RELEASED_IS_STILL_ACTIVE | A reclaim the registry refused ends as still active. | S4 design_decisions #2 |
| REPORT_ONLY_WHAT_IS_RECEIVED | A check's declared result is read from what the check underneath returns. | S4 design_decisions #3 |
| RE_POINT_THE_RUNNER | The reclaim act and the governed action run the next versions; nothing else about them changes. | S4 design_decisions #5 |
| A_PUBLISHED_ACT_IS_REPLACED_NOT_AMENDED | An act whose meaning changes is stated under its next version; the published version is stood down unchanged. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| End a reclaim the registry refuses | ai_licensing | S6 ownership End a reclaim the registry refuses |
| Check an action's parameters | agent_governance | S6 ownership Check an action's parameters |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
