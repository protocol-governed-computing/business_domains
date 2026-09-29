# Stage 8 — Authoring Mandate: blockchain / identity

**Stage:** 8 — Authoring Mandate
**CR:** cr_05_identity
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the ten redeclared artifacts are authored
whole in their subdomain.

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
| EXTEND | 10 | Identity's three contracts, three acts, three entrances and the acceptance gate, redeclared whole so that identity holds every rule it applies and no request supplies one. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | identity |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | identity |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | identity |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | identity |
| blockchain::WF_REGISTER_ACTOR_V0 | identity |
| blockchain::WF_ACCEPT_ACTOR_V0 | identity |
| blockchain::WF_REJECT_ACTOR_V0 | identity |
| blockchain::TI_REGISTER_ACTOR_V0 | identity |
| blockchain::TI_ACCEPT_ACTOR_V0 | identity |
| blockchain::TI_REJECT_ACTOR_V0 | identity |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | Refuses a registration lacking the person's name or their address | actor_record | violations |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Refuses a decision about a person not unverified, a decision other than an acceptance or a rejection, or an authority deciding about themselves, and records the decision it checked | current_state, decision, verifying_authority, contact_address, grounds | result_status |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Refuses a rejection stating no grounds, before anything is recorded | grounds | valid |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | Admits a request to accept a person, with the grounds the authority chooses to state | blockchain::WF_ACCEPT_ACTOR_V0 | contact_address, verifying_authority, grounds |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Reused unchanged; wallet reads the same resolution, and nothing it reads changes. |
