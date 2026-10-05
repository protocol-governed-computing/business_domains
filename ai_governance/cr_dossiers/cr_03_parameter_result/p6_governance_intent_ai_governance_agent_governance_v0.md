# Stage 6 — Governance Intent: ai_governance / agent_governance

**Stage:** 6 — Governance Intent

**CR:** cr_03_parameter_result

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. The parameter check is Agent Governance's; the checks it runs are the platform's,
unchanged.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Check an action's parameters | agent_governance | OWNED | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | S5 scope_boundary Check an action's parameters |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| NONE IDENTIFIED |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Checking against rules | agent_governance -> capability_transforms | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| Looking up a tool's rules | agent_governance -> capability_transforms | capability_transforms::CT_PURE_LOOKUP_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_LOOKUP_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | Present; reports a result it never receives | REPLACE | S4 design_decisions #2 |
| ai_governance::WF_GOVERN_AGENT_ACTION_V0 | Present; runs the parameter check being replaced | REVIEW | S4 design_decisions #3 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| capability_transforms::CT_PURE_LOOKUP_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_LOOKUP_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| REPORT_ONLY_WHAT_IS_RECEIVED | A check's declared result is read from what the check underneath returns. | S4 design_decisions #1 |
| RE_POINT_THE_RUNNER | The governed action runs the new version; nothing else about it changes. | S4 design_decisions #3 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Check an action's parameters | agent_governance | S6 ownership Check an action's parameters |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
