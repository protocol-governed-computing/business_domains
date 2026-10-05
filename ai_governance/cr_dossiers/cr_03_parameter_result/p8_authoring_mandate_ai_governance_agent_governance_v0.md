# Stage 8 — Authoring Mandate: ai_governance / agent_governance

**Stage:** 8 — Authoring Mandate
**CR:** cr_03_parameter_result
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. One contract is built in its subdomain; the one it replaces is stood down, and the governed
action re-pointed to the new one.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | NEW | agent_governance | — |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 1 | The parameter check, reporting whether every declared rule passed. |
| REPLACE | 1 | The parameter check it stands in for. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V1 | agent_governance |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
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
