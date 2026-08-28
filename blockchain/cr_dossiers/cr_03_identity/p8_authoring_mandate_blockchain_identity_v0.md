# Stage 8 — Authoring Mandate: blockchain / identity

**Stage:** 8 — Authoring Mandate

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Artifact Authoring

Mechanically derived from the design. Every artifact the design declares appears here exactly once,
scheduled after everything it depends on. Nothing is decided at this stage; the order is read off the
design's own dependencies.

**Nothing is scheduled.** This change authors no artifact, and an amended artifact is never a build
step — a mandate may not schedule authoring an identity the composition already holds. The one
artifact this change touches is realized because the design amends it, which construction reads from
the design rather than from this mandate. A build order with no rows is the correct shape for a
correction, and it is stated here rather than left to be inferred from an absence.

---

## 1. Build Dependency Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|

---

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| EXTEND | 1 | One capability contract, rendered whole under its own code. Four of its five steps are unchanged; the fifth calls a keyed update in place of a keyed write, taking the record the fourth step assembles as the fields to set. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | identity |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|

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
| capability_side_effects::CS_MUTABLE_JSON_V0 | The keyed update this correction calls was added to the capability before this change was designed, on the neutral surface and not by this domain. A business domain may not author a capability, and the operation it needed did not exist: the store offered a keyed write and a filtered update, and nothing that changed part of one record addressed by its key. Identity depends on it exactly as the change that established this function depended on a clock. |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Composes the amended contract and is not amended. Its routing reads the contract's result statuses, which the correction preserves, so re-rendering the contract changes nothing the workflow observes. |
| blockchain::CC_RESOLVE_ACTOR_V0 | Reached unchanged, and the only reader of the store. From this change forward it will read records still carrying the name and preferences a decision had been stripping. It reads the record whole and asserts nothing about its shape, so more fields reach it and nothing about it needs to change. |
| blockchain::TI_ACCEPT_ACTOR_V0 | Unchanged, with blockchain::TI_REJECT_ACTOR_V0 and both egress declarations. They name a workflow rather than a contract, which is why a correction inside a contract is invisible to every caller. |

---

## Gate 2 — Dossier Lock

**Gate 2 closes here.** The dossier is locked before artifact authoring begins.

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | design_resolution · existing_inventory · new_artifacts · cc_composition · step_bindings · interface_fields · artifact_properties · artifact_summary |
| **Emits** → Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
