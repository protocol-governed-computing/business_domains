# Stage 6 — Governance Intent: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_07_own_values
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: State the moment and the trail of each identity act
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: State the moment and the trail of each identity act}
  - capability: State where the contact address sits
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: State where the contact address sits}
  - capability: State a new wallet's record, prefix and moment
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: "State a new wallet's record, prefix and moment"}
  - capability: Stop the entrances sending what the acts state
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Stop the entrances sending what the acts state}
  - capability: Leave records made before this change in place
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    source_finding: {phase: p4, register: capability_graph, key: Leave records made before this change in place}
  - capability: Answer an acceptance without grounds through an entrance
    owner_subdomain: identity, once the transport standard allows it
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Answer an acceptance without grounds through an entrance}
  - capability: The four other stood-down blockchain artifacts
    owner_subdomain: identity and wallet, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: The four other stood-down blockchain artifacts}
  storage_governance:
  - storage_need: The trail of every person's moments, and the address each claimed
    purpose: Unchanged; each identity act now states the moment it appends, the trail, and where the address sits
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor trail}
  - storage_need: A durable record of every wallet, its claimed identity and its trail
    purpose: Unchanged; wallet now states every value it writes
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, key: Wallet record}
  cross_subdomain_deps:
  - dependency: Looking a person up, and reading the wallet's holder from the result
    direction: wallet -> identity
    existing_artifact: blockchain::CC_RESOLVE_ACTOR_V1
    status: SATISFIED
    source_finding: {phase: p5, register: cross_subdomain_refs, key: 'blockchain::CC_RESOLVE_ACTOR_V1'}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::WF_REGISTER_ACTOR_V1
    current_status: Present; takes the moment, the trail and the address's place from the request
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V1
    current_status: Present; takes the moment and the trail from the request
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_REJECT_ACTOR_V1
    current_status: Present; takes the moment and the trail from the request
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::WF_CREATE_WALLET_V1
    current_status: Present; takes the wallet's record, prefix and moment from the request
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    current_status: Present; sends the moment, the trail and the address's place; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    current_status: Present; sends the moment and the trail; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    current_status: Present; sends the moment and the trail; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - fqdn: blockchain::IN_WALLET_CREATION_V0
    current_status: Present; declares the prefix; published in v5
    action: REPLACE
    source_finding: {phase: p4, register: design_decisions, row: 3}
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
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    current_status: Present; records what it is handed, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    current_status: Present; claims at the place it is handed, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - fqdn: blockchain::CC_DETERMINE_WALLET_IDENTITY_V0
    current_status: Present; forms an identity from the prefix it is handed, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_DETERMINE_WALLET_IDENTITY_V0'}
  - fqdn: blockchain::CC_CREATE_WALLET_RECORD_V1
    current_status: Present; writes the record it is handed, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_CREATE_WALLET_RECORD_V1'}
  - fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V1
    current_status: Present; appends the moment it is handed, reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_APPEND_WALLET_OCCURRENCE_V1'}
  boundary_rules:
  - rule_name: AN_ACT_STATES_WHAT_THE_BUSINESS_DECIDES
    statement: Each act states, in its bindings, every value only the business may decide. No such value is bound to the request.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_WALLET_BELONGS_TO_THE_PERSON_RESOLVED
    statement: A new wallet's holder is the person the act resolved, and its identity is formed from that same person.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: AN_ENTRANCE_SENDS_WHAT_THE_CALLER_SUPPLIES
    statement: An entrance keeps its input contract and sends its act nothing the act states for itself.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: A_CHANGE_OF_MEANING_IS_A_NEW_IDENTITY
    statement: An act, entrance or entry point whose meaning changes is stated under its next version; its predecessor is retired by record, and what names it names its successor.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
    statement: Records made before this change are left as they are.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  governance_outcome:
  - capability: State the moment and the trail of each identity act
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: State the moment and the trail of each identity act}
  - capability: State where the contact address sits
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: State where the contact address sits}
  - capability: State a new wallet's record, prefix and moment
    owner_subdomain: wallet
    source_finding: {phase: p6, register: ownership, key: "State a new wallet's record, prefix and moment"}
  - capability: Stop the entrances sending what the acts state
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Stop the entrances sending what the acts state}
```

Placement of rules. Nothing moves and nothing is added: every act, entrance and entry point that
changes already belongs to identity or to wallet. What is placed here is each value the business
decides, with the act that now states it.

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
