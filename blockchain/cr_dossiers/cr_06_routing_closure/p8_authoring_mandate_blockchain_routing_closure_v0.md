# Stage 8 — Authoring Mandate: blockchain / identity and wallet

**Stage:** 8 — Authoring Mandate
**CR:** cr_06_routing_closure
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. The four contracts come first; three acts run the next version of a replaced contract and
wait for it. The published versions are stood down as their next versions are built, and the
entrances and intents are re-pointed with them.

---

## 1. Build Order

<!-- register:build_order optional -->
| Wave | Step | Code | Action (REPLACE, EXTEND, NEW) | Subdomain | Depends On |
|------|------|------|-------------------------------|-----------|------------|
| 1 | 1 | blockchain::CC_RESOLVE_ACTOR_V1 | NEW | identity | — |
| 1 | 2 | blockchain::CC_CLAIM_WALLET_IDENTITY_V1 | NEW | wallet | — |
| 1 | 3 | blockchain::CC_CREATE_WALLET_RECORD_V1 | NEW | wallet | — |
| 1 | 4 | blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 | NEW | wallet | — |
| 1 | 5 | blockchain::WF_REGISTER_ACTOR_V1 | NEW | identity | — |
| 2 | 6 | blockchain::WF_ACCEPT_ACTOR_V1 | NEW | identity | blockchain::CC_RESOLVE_ACTOR_V1 |
| 2 | 7 | blockchain::WF_REJECT_ACTOR_V1 | NEW | identity | blockchain::CC_RESOLVE_ACTOR_V1 |
| 2 | 8 | blockchain::WF_CREATE_WALLET_V1 | NEW | wallet | blockchain::CC_RESOLVE_ACTOR_V1, blockchain::CC_CLAIM_WALLET_IDENTITY_V1, blockchain::CC_CREATE_WALLET_RECORD_V1, blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 |

---

## 2. Critical Path

<!-- register:critical_path optional -->
| Position | Code |
|----------|------|
| 1 | blockchain::CC_RESOLVE_ACTOR_V1 |
| 2 | blockchain::WF_CREATE_WALLET_V1 |

---

## 3. Artifact Summary

<!-- register:mandate_artifact_summary -->
| Action (REPLACE, EXTEND, NEW) | Count | Description |
|-------------------------------|-------|-------------|
| NEW | 8 | The next versions of four contracts that end on a failed record, and of four acts that route a failed record to their rejected ending. |
| REPLACE | 8 | The published versions they stand in for, stood down unchanged. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::CC_RESOLVE_ACTOR_V1 | identity |
| blockchain::WF_REGISTER_ACTOR_V1 | identity |
| blockchain::WF_ACCEPT_ACTOR_V1 | identity |
| blockchain::WF_REJECT_ACTOR_V1 | identity |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V1 | wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V1 | wallet |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 | wallet |
| blockchain::WF_CREATE_WALLET_V1 | wallet |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| blockchain::CC_RESOLVE_ACTOR_V1 | Answers which actor a contact address denotes, and reports when none does | contact_address | value |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V1 | Claims the identity, and refuses when the person already holds a wallet | wallet_id | result_status |
| blockchain::CC_CREATE_WALLET_RECORD_V1 | Records the wallet with a balance of zero, its denomination and its classification | wallet_id, wallet_fields | result_status |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V1 | Records the moment on the wallet's trail | stream_id, occurrence_fields | result_status |

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
| blockchain::CC_RESOLVE_ACTOR_V1 | Identity's lookup, whose next version wallet runs too; both acts gain the same answer for a failed record. |
