# Stage 6 — Governance Intent: blockchain / wallet

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Giving an accepted person a wallet
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Establishing the address others may pay to
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - capability: Somewhere to hold a wallet and its trail
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-3}
  - capability: Announcing the moment a person is registered, accepted or rejected
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - capability: Refusing a rejection that states no grounds
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-5}
  - capability: Holding a wallet
    owner_subdomain: wallet
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p4, register: capability_graph, row: 6}
  - capability: Recording that a wallet was created
    owner_subdomain: wallet
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    source_finding: {phase: p4, register: capability_graph, row: 7}
  - capability: Determining a wallet's identity
    owner_subdomain: wallet
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_GENERATE_ID_V0
    source_finding: {phase: p4, register: capability_graph, row: 8}
  - capability: Ensuring two wallets never share an identity
    owner_subdomain: wallet
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    source_finding: {phase: p4, register: capability_graph, row: 9}
  - capability: Establishing that a person is held and accepted
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_RESOLVE_ACTOR_V0
    source_finding: {phase: p4, register: capability_graph, row: 10}
  - capability: Supplying the time a moment occurred
    owner_subdomain: wallet
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_CLOCK_V0
    source_finding: {phase: p4, register: capability_graph, row: 11}
  - capability: Moving value into or out of a wallet
    owner_subdomain: wallet
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #1'}
  - capability: Making a wallet inactive, or closing it
    owner_subdomain: wallet
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #2'}
  - capability: Notifying a person that their wallet was created
    owner_subdomain: wallet
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #3'}
  - capability: Recovering a wallet whose holder has lost access
    owner_subdomain: wallet
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: 'deferred #5'}
  - capability: Declaring that the wallet act reads the records identity owns
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: blockchain::WF_CREATE_WALLET_V0
    source_finding: {phase: p4, register: gap_register, key: GAP-9}
  - capability: Refusing a wallet to a person the business has not accepted
    owner_subdomain: wallet
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
  storage_governance:
  - storage_need: Somewhere to hold a wallet
    purpose: Holds what is true of a wallet now — its holder, its balance, its address, its denomination, its classification and its state.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 1}
  - storage_need: Somewhere to hold a wallet's trail
    purpose: Holds the moments a wallet's life passes through, added to and never rewritten.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 2}
  - storage_need: Somewhere to claim a wallet's identity
    purpose: Holds the identities already claimed, so that a second wallet for one person is refused by the claim failing.
    subdomain: wallet
    source_finding: {phase: p5, register: business_objects, row: 3}
  cross_subdomain_deps:
  - dependency: Establishing that a person is one the business holds, and carrying the state that says whether they were accepted
    direction: wallet → identity
    existing_artifact: blockchain::CC_RESOLVE_ACTOR_V0
    status: SATISFIED
    source_finding: {phase: p5, register: cross_subdomain_refs, row: 1}
  - dependency: The moment a person is accepted being announced, so that giving them a wallet has something to follow
    direction: wallet → identity
    existing_artifact: blockchain::EV_ACTOR_ACCEPTED_V0
    status: GAP
    source_finding: {phase: p4, register: dependency_graph, row: 1}
  - dependency: The records identity's contract reads, consulted and never written
    direction: wallet -> identity
    existing_artifact: blockchain::RB_IDENTITY_BINDINGS_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, row: 9}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    current_status: Records a decision, announces nothing, and does not require grounds on a rejection.
    action: REPLACE
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    current_status: Records the decision. Does not read the grounds stated.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-5}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    current_status: Admits a person unverified, and announces nothing.
    action: EXTEND
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    current_status: Declared. Referred to by nothing.
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 1}
  - fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    current_status: Declared. Referred to by nothing.
    action: REUSE
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - fqdn: blockchain::EV_ACTOR_REJECTED_V0
    current_status: Declared. Referred to by nothing.
    action: REUSE
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    current_status: Resolves a person and carries their state.
    action: REUSE
    source_finding: {phase: p5, register: cross_subdomain_refs, row: 1}
  - fqdn: blockchain::STRUCTURE_BUILD_BLOCKCHAIN_CONFIG_V0
    current_status: Declares what the domain compiles. It does not know of a second subdomain.
    action: REVIEW
    source_finding: {phase: p4, register: gap_register, key: GAP-3}
  boundary_rules:
  - rule_name: WALLET_WRITES_ONLY_ITS_OWN
    statement: Wallet writes the three places it owns and no other. It never writes a person, a person's trail, or anything identity owns.
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - rule_name: IDENTITY_WRITES_ONLY_ITS_OWN
    statement: Identity writes people and their trail. It never writes a wallet, and it does not create one.
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - rule_name: ANNOUNCEMENT_OWNED_BY_ITS_SUBJECT
    statement: The moments a person is registered, accepted or rejected are identity's, because they are moments in a person's life. Wallet consumes the acceptance moment and declares none of the three. A consumer never owns the announcement it waits on.
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - rule_name: WALLET_READS_A_PERSON_NEVER_WRITES_ONE
    statement: Wallet establishes that a person is held and accepted by reading what identity already offers. It does not restate a person's state, and it does not correct one.
    source_finding: {phase: p5, register: cross_subdomain_refs, row: 1}
  - rule_name: ACCEPTANCE_STANDS_ALONE
    statement: A wallet that cannot be created does not un-accept the person. The two are separate acts and fail separately.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  - rule_name: NO_NEW_WAY_TO_TOUCH_THE_WORLD
    statement: This change adds no way for the platform to touch the world. Everything it does to anything is one of the ways that already exist.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: A_REACH_IS_DECLARED_WHERE_IT_IS_REVIEWED
    statement: The act declares every binding it consults, in its own artifact. A reach added to a built artifact by hand works, passes every check, and is a reach no reviewer saw.
    source_finding: {phase: p4, register: design_decisions, row: 9}
  - rule_name: A_WALLET_FOLLOWS_ACCEPTANCE_AND_NOTHING_ELSE
    statement: No wallet exists for a person the business has not accepted. The refusal is a step that raises, placed before anything is claimed or recorded.
    source_finding: {phase: p4, register: design_decisions, row: 10}
  governance_outcome:
  - capability: Giving an accepted person a wallet
    owner_subdomain: wallet
    source_finding: {phase: p4, register: gap_register, key: GAP-1}
  - capability: Establishing the address others may pay to
    owner_subdomain: wallet
    source_finding: {phase: p4, register: gap_register, key: GAP-2}
  - capability: Somewhere to hold a wallet and its trail
    owner_subdomain: wallet
    source_finding: {phase: p4, register: gap_register, key: GAP-3}
  - capability: Announcing the moment a person is registered, accepted or rejected
    owner_subdomain: identity
    source_finding: {phase: p4, register: gap_register, key: GAP-4}
  - capability: Refusing a rejection that states no grounds
    owner_subdomain: identity
    source_finding: {phase: p4, register: gap_register, key: GAP-5}
  - capability: Declaring that the wallet act reads the records identity owns
    owner_subdomain: wallet
    source_finding: {phase: p4, register: gap_register, key: GAP-9}
  - capability: Refusing a wallet to a person the business has not accepted
    owner_subdomain: wallet
    source_finding: {phase: p4, register: gap_register, key: GAP-10}
```

WHERE things belong and who owns them. No new artifact codes; no cross-subdomain writes.

---

## Domain Placement (reference)

| Field | Value |
| --- | --- |
| Domain | `blockchain` |
| Primary subdomain | `wallet` — NEW — declared by this CR |
| Secondary subdomain | `identity` — EXISTING — extended by this CR, and the owner of what is extended |
| Authority class | reuse existing — a person acts on their own behalf, an authority decides about them; no new actor type |
| Governing constitutions | `fb.constitution::CONSTITUTION_GOVERNANCE_V0`, `fb.topology::CONSTITUTION_WORKFLOW_V0`, `fb.constitution::CONSTITUTION_STRUCTURE_V0` |

Wallet stands alone rather than nesting under identity because a wallet is a thing the business holds
in its own right, with its own identity, its own record and its own trail. Placing it inside identity
would make identity the owner of value as well as of who a person is, and would leave the record of
people written by a function that is not about people.

---

## 1. Subdomain Boundary — Ownership

---

## 2. Storage Governance Requirements

---

## 3. Cross-Subdomain Dependency Declaration

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 5 — Business Intent | Purpose, objects, identity semantics, invariants, actions, provisional codes | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |
