# Stage 6 — Governance Intent: blockchain / identity and wallet

**Stage:** 6 — Governance Intent

**CR:** cr_06_routing_closure

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Nothing moves and nothing is added: every step and act that changes already
belongs to identity or to wallet. What is placed here is each answer to a failed record, with the
step or act that gives it.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Stop a lookup at a failed record | identity | OWNED |  | S5 scope_boundary Stop a lookup at a failed record |
| Stop a wallet step at a failed record | wallet | OWNED |  | S5 scope_boundary Stop a wallet step at a failed record |
| End every act as rejected on a failed record | identity | OWNED |  | S5 scope_boundary End every act as rejected on a failed record |
| Leave records made before a failure in place | identity | SATISFIED | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | S4 capability_graph Leave records made before a failure in place |
| Tell a refusal apart from a failure | identity, in a later change | DEFERRED |  | S5 scope_boundary Tell a refusal apart from a failure |
| The superseded act's unrouted nodes | nowhere; the act is not dispatched | DEFERRED |  | S5 scope_boundary The superseded act's unrouted nodes |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every person the business knows, and the address each claimed | Unchanged; a failed read, lookup or claim of it now ends the act | identity | S5 business_objects Actor record |
| A durable record of every wallet, its claimed identity and its trail | Unchanged; a failed claim, write or append now ends the act | wallet | S5 business_objects Wallet record |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Looking a person up | wallet -> identity | blockchain::CC_RESOLVE_ACTOR_V0 | SATISFIED | S5 cross_subdomain_refs blockchain::CC_RESOLVE_ACTOR_V0 |
| Keeping a person's record | identity -> platform | capability_side_effects::CS_MUTABLE_JSON_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_MUTABLE_JSON_V0 |
| Claiming an address or a wallet identity | identity -> platform | capability_side_effects::CS_REGISTRY_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_REGISTRY_V0 |
| Appending to a trail | wallet -> platform | capability_side_effects::CS_APPENDONLY_JSONL_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_APPENDONLY_JSONL_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| blockchain::CC_RESOLVE_ACTOR_V0 | Present; neither step answers for a failed record | EXTEND | S4 dependency_graph blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Present; its step does not answer for a failed claim | EXTEND | S4 dependency_graph blockchain::CC_CLAIM_WALLET_IDENTITY_V0 |
| blockchain::CC_CREATE_WALLET_RECORD_V0 | Present; its write step does not answer for a failed write | EXTEND | S4 dependency_graph blockchain::CC_CREATE_WALLET_RECORD_V0 |
| blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Present; its append step does not answer for a failed append | EXTEND | S4 dependency_graph blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | Present; three nodes leave a failed record unrouted | EXTEND | S4 design_decisions #2 |
| blockchain::WF_ACCEPT_ACTOR_V0 | Present; three nodes leave a failed record unrouted | EXTEND | S4 design_decisions #2 |
| blockchain::WF_REJECT_ACTOR_V0 | Present; three nodes leave a failed record unrouted | EXTEND | S4 design_decisions #2 |
| blockchain::WF_CREATE_WALLET_V0 | Present; four nodes leave a failed record unrouted | EXTEND | S4 design_decisions #2 |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Present; already answers for a failed claim, reused unchanged | REUSE | S4 dependency_graph blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::CC_REGISTER_ACTOR_V0 | Present; already answers for a failed write, reused unchanged | REUSE | S4 dependency_graph blockchain::CC_REGISTER_ACTOR_V0 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Present; already answers for a failed append, reused unchanged | REUSE | S4 dependency_graph blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Present; already answers for a failed write, reused unchanged | REUSE | S4 dependency_graph blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_STEP_ANSWERS_FOR_ITS_STORE | Each step answers for every outcome its store declares. A failed record ends the contract. | S4 design_decisions #1 |
| AN_ACT_ROUTES_EVERY_ENDING | Each act routes every outcome its contracts can end with. A failed record reaches the rejected ending. | S4 design_decisions #2 |
| A_CONTRACT_DECLARES_HOW_IT_ENDS | A contract declares every outcome it can end with. | S4 design_decisions #3 |
| THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN | Records made before a failure are left as they are. | S4 design_decisions #4 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Stop a lookup at a failed record | identity | S6 ownership Stop a lookup at a failed record |
| Stop a wallet step at a failed record | wallet | S6 ownership Stop a wallet step at a failed record |
| End every act as rejected on a failed record | identity | S6 ownership End every act as rejected on a failed record |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
