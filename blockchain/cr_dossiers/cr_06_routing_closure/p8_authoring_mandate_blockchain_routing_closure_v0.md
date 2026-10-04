# Stage 8 — Authoring Mandate: blockchain / identity and wallet

**Stage:** 8 — Authoring Mandate
**CR:** cr_06_routing_closure
**Status:** DRAFT
**Feeds:** Construction

IN WHAT ORDER. Mechanically derived from the design; it reconciles with Stage 7 exactly and adds
nothing. Nothing is created, so nothing is scheduled: the eight redeclared artifacts are authored
whole in their subdomains.

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
| EXTEND | 8 | Four contracts that now end on a failed record, and four acts that route a failed record to their rejected ending, redeclared whole. |

---

## 4. Field Declarations

<!-- register:field_declarations -->
| Code | Subdomain Field |
|------|-----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | identity |
| blockchain::WF_REGISTER_ACTOR_V0 | identity |
| blockchain::WF_ACCEPT_ACTOR_V0 | identity |
| blockchain::WF_REJECT_ACTOR_V0 | identity |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | wallet |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | wallet |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | wallet |
| blockchain::WF_CREATE_WALLET_V0 | wallet |

---

## 5. New Capabilities

<!-- register:new_capabilities optional -->
| Code | Purpose | Inputs | Outputs |
|------|---------|--------|---------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Answers which actor a contact address denotes, and reports when none does | contact_address | value |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Claims the identity, and refuses when the person already holds a wallet | wallet_id | result_status |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | Records the wallet with a balance of zero, its denomination and its classification | wallet_id, wallet_fields | result_status |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Records the moment on the wallet's trail | stream_id, occurrence_fields | result_status |

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
| blockchain::CC_RESOLVE_ACTOR_V0 | Identity's lookup, which wallet also runs; both gain the same answer for a failed record. |
