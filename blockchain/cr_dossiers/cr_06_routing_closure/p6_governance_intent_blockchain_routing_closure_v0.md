# Stage 6 — Governance Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Stop a lookup at a failed record
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Stop a lookup at a failed record}
  - capability: Stop a wallet step at a failed record
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Stop a wallet step at a failed record}
  - capability: End every act as rejected on a failed record
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: End every act as rejected on a failed record}
  - capability: Leave records made before a failure in place
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    source_finding: {phase: p4, register: capability_graph, key: Leave records made before a failure in place}
  - capability: Tell a refusal apart from a failure
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Tell a refusal apart from a failure}
  - capability: The superseded act's unrouted nodes
    owner_subdomain: nowhere; the act is not dispatched
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: The superseded act's unrouted nodes}
  storage_governance:
  - storage_need: A durable record of every person the business knows, and the address each claimed
    purpose: Unchanged; a failed read, lookup or claim of it now ends the act
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor record}
  - storage_need: A durable record of every wallet, its claimed identity and its trail
    purpose: Unchanged; a failed claim, write or append now ends the act
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, key: Wallet record}
  cross_subdomain_deps:
  - dependency: Looking a person up
    direction: wallet -> identity
    existing_artifact: blockchain::CC_RESOLVE_ACTOR_V0
    status: SATISFIED
    source_finding: {phase: p5, register: cross_subdomain_refs, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - dependency: Keeping a person's record
    direction: identity -> platform
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - dependency: Claiming an address or a wallet identity
    direction: identity -> platform
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - dependency: Appending to a trail
    direction: wallet -> platform
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    current_status: Present; neither step answers for a failed record; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    current_status: Present; its step does not answer for a failed claim; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
    current_status: Present; its write step does not answer for a failed write; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    current_status: Present; its append step does not answer for a failed append; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    current_status: Present; three nodes leave a failed record unrouted; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    current_status: Present; three nodes leave a failed record unrouted; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_REJECT_ACTOR_V0
    current_status: Present; three nodes leave a failed record unrouted; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_CREATE_WALLET_V0
    current_status: Present; four nodes leave a failed record unrouted; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    current_status: Present; already answers for a failed claim, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    current_status: Present; already answers for a failed write, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_REGISTER_ACTOR_V0'}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    current_status: Present; already answers for a failed append, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    current_status: Present; already answers for a failed write, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    current_status: Present; names the registration act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    current_status: Present; names the acceptance act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    current_status: Present; names the rejection act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    current_status: Present; names the registration act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    current_status: Present; names the acceptance act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::IN_ACTOR_REJECTION_V0
    current_status: Present; names the rejection act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    current_status: Present; names the wallet act being replaced
    action: REVIEW
    source_finding: {phase: p4, register: design_decisions, row: 6}
  boundary_rules:
  - rule_name: A_STEP_ANSWERS_FOR_ITS_STORE
    statement: Each step answers for every outcome its store declares. A failed record ends the contract.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: AN_ACT_ROUTES_EVERY_ENDING
    statement: Each act routes every outcome its contracts can end with. A failed record reaches the rejected ending.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: A_CONTRACT_DECLARES_HOW_IT_ENDS
    statement: A contract declares every outcome it can end with.
    source_finding: {phase: p4, register: design_decisions, row: 3}
  - rule_name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
    statement: Records made before a failure are left as they are.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: A_PUBLISHED_ACT_IS_REPLACED_NOT_AMENDED
    statement: An act whose meaning changes is stated under its next version; the published version is stood down unchanged, and what names it names its successor.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  governance_outcome:
  - capability: Stop a lookup at a failed record
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Stop a lookup at a failed record}
  - capability: Stop a wallet step at a failed record
    owner_subdomain: wallet
    source_finding: {phase: p6, register: ownership, key: Stop a wallet step at a failed record}
  - capability: End every act as rejected on a failed record
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: End every act as rejected on a failed record}
```

Placement of rules. Nothing moves and nothing is added: every step and act that changes already
belongs to identity or to wallet. What is placed here is each answer to a failed record, with the
step or act that gives it.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
