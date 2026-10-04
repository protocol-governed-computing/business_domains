# Stage 8 — Authoring Mandate: ai_governance / ai_licensing

**Stage:** 8 — Authoring Mandate
**CR:** cr_02_reclaim_closure
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the one redeclared contract is authored whole
in its subdomain.

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
| EXTEND | 1 | The reclaim contract, whose removal step now ends it on a refused removal, redeclared whole. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | ai_licensing |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Reclaim license from inactive user | license_id, employee_id, last_active_date, evaluation_date, threshold_days | result_status, is_inactive, days_inactive |

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
