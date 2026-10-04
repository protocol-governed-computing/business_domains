# Stage 8 — Authoring Mandate: ai_governance / ai_licensing

**Stage:** 8 — Authoring Mandate
**CR:** cr_01_licensing
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the three checks are redeclared whole with their
cases, and the build manifest is regenerated.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| EXTEND | 4 | The licensing domain's three checks, redeclared whole with the cases that prove them, and the build manifest regenerated so the domain compiles those cases. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | ai_licensing |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | ai_licensing |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | ai_licensing |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0 | Evaluate whether license quota remains available under the declared cap | assigned_count, quota | quota_available, remaining |
| ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0 | Evaluate whether required training has been completed | training_completed | training_eligible |
| ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0 | Evaluate license inactivity against a declared threshold | last_active_date, evaluation_date, threshold_days | is_inactive, days_inactive |

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
| ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0 | Generated, not authored. It describes the whole domain, so it still names agent_governance, which this change does not touch. |
