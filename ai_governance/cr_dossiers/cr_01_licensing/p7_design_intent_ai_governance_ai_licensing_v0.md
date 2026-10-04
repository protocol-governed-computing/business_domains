# Stage 7 — Design Intent: ai_governance / ai_licensing

**Stage:** 7 — Design Intent
**CR:** cr_01_licensing
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Every binding names a field the capability declares, read from the pinned baseline
`25009fed290d52c7b699f7fdd85f653c594306b48568bd9d351d8e63a79ca843`.

Nothing new is authored. The three checks are redeclared whole, each with the cases that prove it;
the domain's build manifest is regenerated so that the domain compiles those cases. What each check
decides, and every act that uses them, is unchanged.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| Each check is stated whole, as it stands, with its cases | A case belongs to a transform the design names | The three checks are redeclared with the inputs, outputs, implementation and refusal they already declare | S4 design_decisions #1 |
| A no case expects a refusal; a yes case keeps its answer | The checks refuse, as the business decided | Each check has one SUCCESS case with its answer and one VIOLATION case | S4 design_decisions #2 |
| The earlier values stay, under this system's names, with one boundary case added | The author answered both | The earlier values are kept; the inactivity check gains a license unused for exactly the threshold | S4 design_decisions #3 |
| The build configuration is reached through its generator | It is derived from the design | The build manifest is named as generated, so the domain compiles the stated cases | S4 design_decisions #4 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REVIEW) | Summary | Reason | Source Finding |
|------|-----------------------------------------|---------|--------|----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | EXTEND | Evaluate whether license quota remains available under the declared cap | Stated whole with the cases that prove it. | S6 pps_artifacts_requiring_action #1 |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | EXTEND | Evaluate whether required training has been completed | Stated whole with the cases that prove it. | S6 pps_artifacts_requiring_action #2 |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | EXTEND | Evaluate license inactivity against a declared threshold | Stated whole with the cases that prove it. | S6 pps_artifacts_requiring_action #3 |
| ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | EXTEND | Declares what the ai_governance domain compiles | It does not compile stated cases and must. | S6 pps_artifacts_requiring_action #4 |
| ai_governance::CC_VALIDATE_ELIGIBILITY_V0 | REUSE |  | Runs the training and license checks for provisioning, unchanged. | S6 pps_artifacts_requiring_action #5 |
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | REUSE |  | Runs the inactivity check for reclamation, unchanged. | S6 pps_artifacts_requiring_action #6 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|---------------------------------------------------------------|------|---------|-----------------|--------|----------------|

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

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|---------------------------|-------|----------|----------------|

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | INPUT | assigned_count | integer | YES |  | Number of licenses currently assigned |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | INPUT | quota | integer | YES |  | Declared license cap |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | OUTPUT | quota_available | boolean | YES |  | True when at least one license remains under the cap |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | OUTPUT | remaining | integer | YES |  | Licenses remaining under the cap, floored at zero |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | INPUT | training_completed | boolean | YES |  | Whether the employee has completed required AI-use training |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | OUTPUT | training_eligible | boolean | YES |  | True when training is complete and the employee clears this gate |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | INPUT | last_active_date | string | YES |  | ISO-8601 date or date-time of last recorded license activity |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | INPUT | evaluation_date | string | YES |  | ISO-8601 date or date-time the evaluation is made as of — declared, never a clock read |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | INPUT | threshold_days | integer | YES |  | Inactivity threshold in days |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | OUTPUT | is_inactive | boolean | YES |  | True when days_inactive meets or exceeds threshold_days |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | OUTPUT | days_inactive | integer | YES |  | Whole days elapsed between last_active_date and evaluation_date |

---

## 9. Implementation Bindings

<!-- register:implementation_bindings optional -->
| CT Code | Module | Callable | Operation | Kind (atom, molecule) | Purity (ct_pure, ct_impure) | Refusal (raises, returns, never) | Source Finding |
|---------|--------|----------|-----------|-----------------------|-----------------------------|----------------------------------|----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | ai_governance.implementation.capability_transforms.atoms.ct_pure_check_quota_available_v0 | execute | PURE_CHECK_QUOTA_AVAILABLE | atom | ct_pure | raises | S6 pps_artifacts_requiring_action #1 |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | ai_governance.implementation.capability_transforms.atoms.ct_pure_check_training_status_v0 | execute | PURE_CHECK_TRAINING_STATUS | atom | ct_pure | raises | S6 pps_artifacts_requiring_action #2 |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | ai_governance.implementation.capability_transforms.atoms.ct_pure_evaluate_inactivity_v0 | execute | PURE_EVALUATE_INACTIVITY | atom | ct_pure | raises | S6 pps_artifacts_requiring_action #3 |

---

## 10. Vocabulary Extensions

<!-- register:vocabulary_extensions optional -->
| Vocabulary Code | Extends | Group | Casing | Value | Meaning | Source Finding |
|-----------------|---------|-------|--------|-------|---------|----------------|

---

## 11. Runtime Policies

<!-- register:runtime_policies optional -->
| RB Code | Capability | Key | Value | Source Finding |
|---------|------------|-----|-------|----------------|

---

## 12. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|

---

## 13. STRUCTURE Stores

<!-- register:structure_stores optional -->
| Store Name | Storage Type (CS_APPENDONLY_JSONL_V0, CS_MUTABLE_JSON_V0, CS_REGISTRY_V0) | Proposed Path | Used By | Source Finding |
|------------|---------------------------------------------------------------------------|---------------|---------|----------------|

---

## 14. Transport Bindings

<!-- register:transport_bindings optional -->
| Artifact | Direction (INGRESS, EGRESS) | Operation | Handler Kind (WF_INVOCATION, SNAPSHOT_READ) | Handler Target | Field | Bound To | Source Finding |
|----------|-----------------------------|-----------|---------------------------------------------|----------------|-------|----------|----------------|

---

## 15. Artifact Summary

<!-- register:artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Subdomain | Count | Artifacts |
|-------------------------------|-----------|-------|-----------|
| EXTEND | ai_licensing | 4 | ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0, ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0, ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0, ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 |

---

## 16. Generation Provenance

<!-- register:generation_provenance optional -->
| Artifact | Generator | Generator Sources | Source Finding |
|----------|-----------|-------------------|----------------|
| ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | transformation.build.render:build_manifest | S8 build_order, S8 field_declarations, transformation/design/families.py | S6 pps_artifacts_requiring_action #4 |

---

## 17. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 18. Refusal Discharge

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

---

## 19. Refusal Deferrals

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|-----------|--------------|-------------|-------|----------------|

---

## 20. Refusal — Governance-Surface Discharge

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|-----------|--------------|-------|----------------|----------------|

---

## 21. Molecule Steps

<!-- register:molecule_steps optional -->
| CT Code | Step | Kind (atom, molecule, loop) | Target | Over | Iterator | Emits | Source Finding |
|---------|------|-----------------------------|--------|------|----------|-------|----------------|

---

## 22. Molecule Step Bindings

<!-- register:molecule_step_bindings optional -->
| CT Code | Step | Role (INPUT, CARRY, UPDATE) | Field | Bound To | Source Finding |
|---------|------|-----------------------------|-------|----------|----------------|

---

## 23. Test Cases

<!-- register:test_cases optional -->
| CT Code | Case | Expected Outcome (SUCCESS, VIOLATION) | Source Finding |
|---------|------|---------------------------------------|----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | available_under_cap | SUCCESS | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | refuses_at_cap | VIOLATION | human decision |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | eligible_once_trained | SUCCESS | human decision |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | refuses_untrained | VIOLATION | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | SUCCESS | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | SUCCESS | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | refuses_recently_used | VIOLATION | human decision |

---

## 24. Test Case Values

<!-- register:test_case_values optional -->
| CT Code | Case | Role (INPUT, EXPECTED, ASSERT, RECORDED) | Field | Value | Source Finding |
|---------|------|------------------------------------------|-------|-------|----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | available_under_cap | INPUT | assigned_count | 5 | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | available_under_cap | INPUT | quota | 10 | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | available_under_cap | EXPECTED | quota_available | true | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | available_under_cap | EXPECTED | remaining | 5 | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | refuses_at_cap | INPUT | assigned_count | 10 | human decision |
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | refuses_at_cap | INPUT | quota | 10 | human decision |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | eligible_once_trained | INPUT | training_completed | true | human decision |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | eligible_once_trained | EXPECTED | training_eligible | true | human decision |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | refuses_untrained | INPUT | training_completed | false | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | INPUT | last_active_date | "2024-01-01T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | INPUT | evaluation_date | "2024-02-15T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | INPUT | threshold_days | 30 | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | EXPECTED | is_inactive | true | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_past_threshold | EXPECTED | days_inactive | 45 | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | INPUT | last_active_date | "2024-01-16T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | INPUT | evaluation_date | "2024-02-15T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | INPUT | threshold_days | 30 | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | EXPECTED | is_inactive | true | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | inactive_at_threshold | EXPECTED | days_inactive | 30 | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | refuses_recently_used | INPUT | last_active_date | "2024-02-10T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | refuses_recently_used | INPUT | evaluation_date | "2024-02-15T00:00:00Z" | human decision |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | refuses_recently_used | INPUT | threshold_days | 30 | human decision |

---

## 25. Withdrawn Facts

<!-- register:withdrawn_facts optional -->
| Artifact | Fact | Reason | Source Finding |
|----------|------|--------|----------------|

---

## gov_projection — Governed Handoff to Stage 8

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 6 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
| **Emits** → Stage 8 | design_resolution · existing_inventory · new_artifacts · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · implementation_bindings · vocabulary_extensions · runtime_policies · artifact_properties · structure_stores · artifact_summary · generation_provenance |
