# Stage 7 — Design Intent: ai_governance / ai_licensing

**Stage:** 7 — Design Intent
**CR:** cr_02_reclaim_closure
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`6783308c59ca6d3f96c88c8101f78397b7411c69d4f76995f0baa5fe6bafbbfb`.

Nothing new is authored. The reclaim contract is redeclared whole: its removal step gains an answer
for a refused removal and ends the contract with it. Every other step, route, binding and field is
restated exactly as it stands.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The removal step ends the contract on a refused removal | No reclaim carries on past a removal the registry refused | The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 routes VIOLATION to exit | S4 design_decisions #1 |
| A refused removal ends as still active | A license the registry did not release stays with the employee | ai_governance::WF_AUTO_RECLAIM_V0 already routes the contract's VIOLATION to EXIT_ACTIVE, and is reused unchanged | S4 design_decisions #2 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | EXTEND | Reclaim license from inactive user | Its removal step carries on past a refusal its registry declares. | S6 pps_artifacts_requiring_action #1 |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | REUSE |  | Named by the amended contract, unchanged. | S6 pps_artifacts_requiring_action #2 |
| ai_governance::WF_AUTO_RECLAIM_V0 | REUSE |  | Runs the amended contract, and already routes its refusal to still active. | S6 pps_artifacts_requiring_action #3 |
| capability_side_effects::CS_REGISTRY_V0 | REUSE |  | Named by the amended contract, unchanged. | S6 cross_subdomain_deps #1 |
| ai_governance::RB_LICENSE_BINDINGS_V0 | REUSE |  | Binds the license registry, unchanged. | S6 cross_subdomain_deps #1 |
| ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V0 | REUSE |  | Places the license registry, unchanged. | S6 cross_subdomain_deps #1 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|

---

## 4. Runtime Binding (RB) Declarations

<!-- register:rb_declarations -->
| RB Code | Binds WF | CS Bindings | Storage Structure | Source Finding |
|---------|----------|-------------|-------------------|----------------|
| NONE IDENTIFIED |

---

## 5. Execution Topology

<!-- register:execution_topology optional_columns=runs -->
| Workflow | Node | Runs | Node Type (IN, CC, EXIT, EXIT_SUCCESS) | Routing | Source Finding |
|----------|------|------|----------------------------------------|---------|----------------|
| NONE IDENTIFIED |

---

## 6. Capability Composition

<!-- register:cc_composition optional -->
| CC Code | Step | Step Name | Capability | Kind (CT, CS) | Operation | Store | Consumes | Produces | Routing | Interpreted By | Semantic Status | Interface |
|---------|------|-----------|------------|---------------|-----------|-------|----------|----------|---------|----------------|-----------------|-----------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | 1 | evaluate_inactivity | ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | CT | EVALUATE_INACTIVITY | — | last_active_date, evaluation_date, threshold_days | is_inactive, days_inactive | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: last_active_date=last_active_date, evaluation_date=evaluation_date, threshold_days=threshold_days; out: is_inactive=is_inactive, days_inactive=days_inactive |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | 2 | deregister_license | capability_side_effects::CS_REGISTRY_V0 | CS | DEREGISTER | LICENSE_REGISTRY | key_or_address | result_status | SUCCESS -> exit; NOT_FOUND -> exit; BACKEND_ERROR -> exit; VIOLATION -> exit | — | SUCCESS | in: key_or_address=employee_id; out: result_status=result_status |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | evaluate_inactivity | INPUT | last_active_date | inputs.last_active_date | S7 cc_composition evaluate_inactivity |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | evaluate_inactivity | INPUT | evaluation_date | inputs.evaluation_date | S7 cc_composition evaluate_inactivity |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | evaluate_inactivity | INPUT | threshold_days | inputs.threshold_days | S7 cc_composition evaluate_inactivity |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | evaluate_inactivity | OUTPUT | is_inactive | capability_result.is_inactive | S7 cc_composition evaluate_inactivity |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | evaluate_inactivity | OUTPUT | days_inactive | capability_result.days_inactive | S7 cc_composition evaluate_inactivity |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | deregister_license | INPUT | key_or_address | inputs.employee_id | S7 cc_composition deregister_license |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | deregister_license | OUTPUT | result_status | result_status | S7 cc_composition deregister_license |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | INPUT | license_id | string | YES |  | License to evaluate |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | INPUT | employee_id | string | YES |  | Employee holding the license |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | INPUT | last_active_date | string (date-time) | YES |  | Last usage date |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | INPUT | evaluation_date | string (date-time) | YES |  | The date the reclaim is evaluated as of |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | INPUT | threshold_days | integer | YES | 30 | Inactivity threshold in days |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | OUTPUT | result_status | string | NO |  | Operation result |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | OUTPUT | is_inactive | boolean | NO |  | Whether the user is inactive |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | OUTPUT | days_inactive | integer | NO |  | Number of days inactive |

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | description | Evaluates inactivity and reclaims license if threshold exceeded | S6 pps_artifacts_requiring_action #1 |

---

## 10. Structure Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|------|------|------|----------------|

---

## 11. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | ai_licensing | 1 | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No act, transform, vocabulary, policy, entrance or generator is touched.

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|---|---|---|---|---|---|---|

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---|---|---|---|---|

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|---|---|---|---|

---

## 14. Refusal Discharge

The refusal the business named is carried by the reclaim act, which this change does not touch: it
already routes the contract's VIOLATION to EXIT_ACTIVE. The act states admission rules and a renamed
node that no register carries, so it cannot be restated here, and the discharge names it instead.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|
| Reclaiming a license | The registry refuses to remove the assignment | ai_governance::WF_AUTO_RECLAIM_V0, reused unchanged: its node for ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 routes VIOLATION to EXIT_ACTIVE | The act is next restated | S0 operation_refusals #1 |

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn: the amended contract keeps every fact it has and gains one answer.

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---|---|---|---|---|---|---|---|

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---|---|---|---|---|---|

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---|---|---|---|

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---|---|---|---|---|---|

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|---|---|---|---|

