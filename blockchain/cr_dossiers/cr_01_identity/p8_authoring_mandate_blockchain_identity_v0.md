# Stage 8 — Authoring Mandate: blockchain / identity

**Stage:** 8 — Authoring Mandate
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Artifact Authoring

Mechanically derived from the design. Every artifact the design declares appears here exactly once,
scheduled after everything it depends on. Nothing is decided at this stage; the order is read off
the design's own dependencies.

---

## 1. Build Dependency Order

<!-- register:build_order -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | blockchain::AC_PARTICIPANT_V0 | NEW | identity | — |
| 1 | 2 | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | NEW | identity | — |
| 1 | 3 | blockchain::EV_ACTOR_ACCEPTED_V0 | NEW | identity | — |
| 1 | 4 | blockchain::EV_ACTOR_REJECTED_V0 | NEW | identity | — |
| 2 | 5 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | NEW | identity | — |
| 3 | 6 | blockchain::CC_VALIDATE_REGISTRATION_V0 | NEW | identity | — |
| 3 | 7 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | NEW | identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 3 | 8 | blockchain::CC_REGISTER_ACTOR_V0 | NEW | identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 3 | 9 | blockchain::CC_RESOLVE_ACTOR_V0 | NEW | identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 3 | 10 | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | NEW | identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 3 | 11 | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | NEW | identity | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 4 | 12 | blockchain::IN_ACTOR_REGISTERED_V0 | NEW | identity | blockchain::CC_VALIDATE_REGISTRATION_V0 |
| 4 | 13 | blockchain::IN_ACTOR_VERIFIED_V0 | NEW | identity | blockchain::CC_RESOLVE_ACTOR_V0 |
| 5 | 14 | blockchain::WF_REGISTER_ACTOR_V0 | NEW | identity | blockchain::IN_ACTOR_REGISTERED_V0 |
| 5 | 15 | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | NEW | identity | blockchain::IN_ACTOR_VERIFIED_V0 |
| 6 | 16 | blockchain::RB_IDENTITY_BINDINGS_V0 | NEW | identity | blockchain::WF_REGISTER_ACTOR_V0 |

---

## 2. Critical Path

<!-- register:critical_path -->
| Position | Code |
|----------|------|
| 1 | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| 2 | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| 3 | blockchain::CC_REGISTER_ACTOR_V0 |
| 4 | blockchain::IN_ACTOR_REGISTERED_V0 |
| 5 | blockchain::WF_REGISTER_ACTOR_V0 |
| 6 | blockchain::RB_IDENTITY_BINDINGS_V0 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 16 | 1 AC, 3 EV, 1 STRUCTURE, 6 CC, 2 IN, 2 WF, 1 RB — the whole of the identity subdomain, nothing extended because nothing of this domain exists |

---

## 4. Subdomain Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::AC_PARTICIPANT_V0 | identity |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | identity |
| blockchain::EV_ACTOR_ACCEPTED_V0 | identity |
| blockchain::EV_ACTOR_REJECTED_V0 | identity |
| blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | identity |
| blockchain::CC_VALIDATE_REGISTRATION_V0 | identity |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | identity |
| blockchain::CC_REGISTER_ACTOR_V0 | identity |
| blockchain::CC_RESOLVE_ACTOR_V0 | identity |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | identity |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | identity |
| blockchain::IN_ACTOR_REGISTERED_V0 | identity |
| blockchain::IN_ACTOR_VERIFIED_V0 | identity |
| blockchain::WF_REGISTER_ACTOR_V0 | identity |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | identity |
| blockchain::RB_IDENTITY_BINDINGS_V0 | identity |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | Confirm a registration carries a name and a contact address of the form asked for, so that only details the business cannot read are refused and judgement is left to the decision | actor_record:object, registration_schema:object | violations:array |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Claim the contact address atomically so that two registrations of one person resolve to one actor rather than producing two | actor_record:object, address_path:string, address_type:string | result:string, address:string |
| blockchain::CC_REGISTER_ACTOR_V0 | Write the actor unverified once its address is claimed, so that a refused registration leaves nothing behind | actor_fields:object, contact_address:string | result_status:string |
| blockchain::CC_RESOLVE_ACTOR_V0 | Answer which actor a contact address denotes and report when none does, so a decision against an unregistered person is refused | contact_address:string | actor_record:object |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Refuse every declared refusal and move the actor to its decided state, so an actor is decided about once and never by itself | current_state:string, states_admitting_a_decision:array, decision:string, admitted_outcomes:array, verifying_authority:string, contact_address:string, decided_actor_fields:object | result_status:string |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Read the time now and append one occurrence carrying it, so the business can afterwards show who registered, who decided, what was decided and when it happened | occurrence_fields:object, stream_id:string, contact_address:string | timestamp:string, sequence_number:integer |

---

## 6. New Intents

<!-- register:new_intents optional -->
| Code | Purpose | Workflow | Inputs |
|------|---------|----------|--------|
| blockchain::IN_ACTOR_REGISTERED_V0 | Admit a request from a person to be recorded as an actor of the system | blockchain::WF_REGISTER_ACTOR_V0 | actor_record:object, registration_schema:object |
| blockchain::IN_ACTOR_VERIFIED_V0 | Admit a request from an authority to record a decision against a registered actor | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | contact_address:string, verifying_authority:string, decision:string, grounds:string |

---

## 7. Cross-Subdomain Notes

<!-- register:cross_subdomain_notes optional -->
| Code | Note |
|------|------|
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | The occurrence carries occurred_at, read from capability_side_effects::CS_CLOCK_V0 at the moment the occurrence is recorded. No caller supplies it. |
| blockchain::WF_REGISTER_ACTOR_V0 | Reached in process. No transport ingress is scheduled, so the operation is not reachable over HTTP; a follow-on change request adds the boundary without altering this workflow. |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Reached in process, on the same terms. |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 6 — Governance Intent | p6_governance_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 7 — Design Intent | p7_design_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 8 — Authoring Mandate | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Artifact Authoring

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 7 | new_artifacts · existing_inventory · rb_declarations · execution_topology · cc_composition · step_bindings · interface_fields · structure_stores · artifact_summary |
| **Emits** → Artifact Authoring | build_order · critical_path · mandate_artifact_summary · field_declarations · new_capabilities · new_intents · cross_subdomain_notes |
