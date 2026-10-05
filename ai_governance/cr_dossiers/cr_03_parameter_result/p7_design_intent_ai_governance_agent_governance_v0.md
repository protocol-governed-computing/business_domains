# Stage 7 — Design Intent: ai_governance / agent_governance

**Stage:** 7 — Design Intent
**CR:** cr_03_parameter_result
**Status:** DRAFT
**Feeds:** Stage 8 — Authoring Mandate

Read against the pinned baseline
`6ddb2b55337926a3c43ab30821b1f6b6570723b633495b900c069951cb6bb5c4`.

The parameter check is replaced by a version that reports what it receives: whether every declared
rule passed, read from the check underneath. Its steps, rules and routes are those of the version it
replaces. The governed action is re-pointed to run it, and nothing else about the action changes.

---

## 1. Design Decisions Resolution

<!-- register:design_resolution optional -->
| Decision | Business Fact | Resolution | Source Finding |
|----------|---------------|------------|----------------|
| The check reports what it receives | A check reports only what it receives | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 maps `validation_result` from the check's `valid`, a boolean | S4 design_decisions #1 |
| A new version | A change of what a check reports is a new version | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 supersedes ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0, with the same two steps, rules and routes | S4 design_decisions #2 |
| The governed action runs the new version | It decides exactly as today | ai_governance::WF_GOVERN_AGENT_ACTION_V0 is re-pointed: the place that runs the check runs ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1; its label and routes are unchanged | S4 design_decisions #3 |

---

## 2. Artifact Inventory — Existing Artifacts

<!-- register:existing_inventory -->
| FQDN | Action (REPLACE, REUSE, EXTEND, REPOINT, REVIEW) | Summary | Reason | Source Finding |
|------|------------------------------------------|---------|--------|----------------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | REPLACE |  | Reports a result it never receives. Stood down by its next version. | S6 pps_artifacts_requiring_action #1 |
| ai_governance::WF_GOVERN_AGENT_ACTION_V0 | REPOINT |  | Runs the parameter check being replaced; re-pointed to its next version. | S6 pps_artifacts_requiring_action #2 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | REUSE |  | Checks the parameters against the rules, unchanged. | S6 pps_artifacts_requiring_action #3 |
| capability_transforms::CT_PURE_LOOKUP_V0 | REUSE |  | Looks up the tool's rules, unchanged. | S6 pps_artifacts_requiring_action #4 |

---

## 3. Artifact Family Mapping — New Artifacts

<!-- register:new_artifacts optional business_language=capability -->
| Capability | Family (AC, IN, WF, RB, CC, CT, EV, VOCAB, STRUCTURE, TI, TE) | Code | Summary | Owner Subdomain | Status | Source Finding |
|------------|------------------------------------------------|------|---------|-----------------|--------|----------------|
| Check an action's parameters | CC | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | Enforce declared parameter constraints for an authorized tool | agent_governance | NEW | S6 governance_outcome #1 |

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
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | 1 | lookup_parameter_rules | capability_transforms::CT_PURE_LOOKUP_V0 | CT | LOOKUP | — | key, map | result | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: key=tool_name, map=rules declared per tool; out: result=rules |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | 2 | validate_parameters | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | CT | VALIDATE_PARAMETER_RULES | — | parameters, rules | valid | SUCCESS -> continue; VIOLATION -> exit | — | SUCCESS | in: parameters=parameters, rules=rules; out: valid=validation_result |

---

## 7. Step Bindings

<!-- register:step_bindings optional -->
| Owner | Step | Direction (INPUT, OUTPUT) | Field | Bound To | Source Finding |
|-------|------|--------------------------|-------|----------|----------------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | lookup_parameter_rules | INPUT | key | inputs.tool_name | S7 cc_composition lookup_parameter_rules |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | lookup_parameter_rules | INPUT | map | {"READ_RECORD": [{"field": "record_type", "op": "in", "allowed": ["license_pool", "user_profile"]}, {"field": "id", "op": "not_null"}], "PROVISION_STANDARD_LICENSE": [{"field": "tier", "op": "eq", "value": "standard"}, {"field": "quantity", "op": "lte", "value": 100}], "PROVISION_PREMIUM_LICENSE": [{"field": "tier", "op": "eq", "value": "premium"}, {"field": "quantity", "op": "lte", "value": 50}]} | S7 cc_composition lookup_parameter_rules |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | lookup_parameter_rules | OUTPUT | rules | capability_result.result | S7 cc_composition lookup_parameter_rules |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | validate_parameters | INPUT | parameters | inputs.parameters | S7 cc_composition validate_parameters |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | validate_parameters | INPUT | rules | results.lookup_parameter_rules.rules | S7 cc_composition validate_parameters |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | validate_parameters | OUTPUT | validation_result | capability_result.valid | S7 cc_composition validate_parameters |

---

## 8. Interface Fields

<!-- register:interface_fields optional -->
| Artifact | Direction (INPUT, OUTPUT, ATTRIBUTE) | Field | Type | Required (YES, NO) | Default | Meaning |
|----------|--------------------------------------|-------|------|--------------------|---------|---------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | INPUT | tool_name | string | YES |  | Tool the agent proposes to use |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | INPUT | parameters | object | YES |  | Parameters of the proposed action |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | OUTPUT | rules | array | NO |  | The rules declared for the tool |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | OUTPUT | validation_result | boolean | NO |  | Whether every declared rule passed |

---

## 9. Artifact Properties

<!-- register:artifact_properties optional -->
| Artifact | Property | Value | Source Finding |
|----------|----------|-------|----------------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | supersedes | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | S4 design_decisions #2 |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | description | Evaluates declarative parameter constraints — policy in governance, evaluation in generic CT | S6 pps_artifacts_requiring_action #1 |

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
| NEW | agent_governance | 1 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 |
| REPLACE | agent_governance | 1 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 |

---

## 12. Declared Reach

<!-- register:declared_reach optional -->
| Act | Consults | Source Finding |
|-----|----------|----------------|

---

## 13. Unchanged Registers

No transform, vocabulary, policy, entrance or generator is touched. The governed action is re-pointed, not restated.

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

The business declared no refusal.

<!-- register:refusal_discharge optional -->
| Operation | Refused When | Act | Step | Outcome | Source Finding |
|-----------|--------------|-----|------|---------|----------------|

<!-- register:refusal_deferrals optional -->
| Operation | Refused When | Deferred To | Until | Source Finding |
|---|---|---|---|---|

<!-- register:refusal_governance_discharge optional -->
| Operation | Refused When | Phase | Governing Rule | Source Finding |
|---|---|---|---|---|

---

## 15. Molecules, Tests and Withdrawals

No molecule or test is touched, and nothing is withdrawn.

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

