# Stage 8 — Authoring Mandate: ai_governance / reclaim and parameter result

**Stage:** 8 — Authoring Mandate
**CR:** cr_02_reclaim_and_parameters
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Two contracts are built, each in its subdomain; the published versions they replace are
stood down, and the reclaim act and the governed action are re-pointed to them.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 | NEW | ai_licensing | — |
| 1 | 2 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | NEW | agent_governance | — |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 |
| 2 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 2 | The reclaim, answering a refused removal, and the parameter check, reporting whether every declared rule passed. |
| REPLACE | 2 | The published versions they stand in for, stood down unchanged. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 | ai_licensing |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | agent_governance |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V1 | Reclaim license from inactive user | license_id, employee_id, last_active_date, evaluation_date, threshold_days | result_status, is_inactive, days_inactive |
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | Enforce declared parameter constraints for an authorized tool | tool_name, parameters | rules, validation_result |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
