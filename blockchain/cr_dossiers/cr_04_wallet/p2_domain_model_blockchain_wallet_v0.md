# Stage 2 — Domain Model Discovery: blockchain / wallet

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain: wallet
  cr: cr_04_wallet
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Wallet
    description: Where an accepted person holds value.
    store_model: None. No store holds a wallet anywhere in the composition.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: Holder
    description: The accepted person a wallet belongs to. Already held by the business as a person.
    store_model: A record of people, keyed by the address they registered with.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: Balance
    description: What a wallet carries.
    store_model: None.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Address
    description: What others may pay to.
    store_model: None.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_vocabulary, row: 6}
  - entity: Occurrence
    description: A moment the business recorded, added to and never rewritten.
    store_model: A trail of occurrences against a person.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: business_vocabulary, row: 9}
  entity_attributes:
  - entity: Wallet
    attribute: Its own identity
    meaning: Distinguishes one wallet from another.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Wallet
    attribute: Holder
    meaning: The one person it belongs to.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - entity: Wallet
    attribute: Balance
    meaning: What it carries. Zero when created, never negative.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 14}
  - entity: Wallet
    attribute: Denomination
    meaning: The currency the balance is expressed in.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 16}
  - entity: Wallet
    attribute: Classification
    meaning: What kind of wallet it is. Default for every wallet this change creates.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 15}
  - entity: Wallet
    attribute: Address
    meaning: What others may pay to.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 7}
  - entity: Wallet
    attribute: State
    meaning: Active when created; may become inactive; may be closed.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  - entity: Holder
    attribute: Registered details
    meaning: What the person supplied and keeps.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - entity: Holder
    attribute: State
    meaning: Whether the business has accepted, rejected, or not yet decided about them.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - entity: Occurrence
    attribute: What occurred, and when
    meaning: The moment and its time.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: known_facts, row: 19}
  business_processes:
  - process: Giving an accepted person a wallet
    initiator: The acceptance of a person
    outcome: The person holds a wallet, and the moment is on the trail.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Registering a person
    initiator: The person
    outcome: The person is held, unverified.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - process: Recording a decision about a person
    initiator: An authority
    outcome: The person is accepted or rejected, keeping the details they registered with.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  process_steps:
  - process: Giving an accepted person a wallet
    step: '1'
    action: Establish that the person is one the business holds and has accepted.
    record_produced: None.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Giving an accepted person a wallet
    step: '2'
    action: Determine the wallet's identity, and stop if the person already holds one.
    record_produced: None.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Giving an accepted person a wallet
    step: '3'
    action: Establish the address others may pay to, from key material supplied to the business.
    record_produced: None.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 18}
  - process: Giving an accepted person a wallet
    step: '4'
    action: Record the wallet, with a balance of zero, its denomination and its classification.
    record_produced: The wallet.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 14}
  - process: Giving an accepted person a wallet
    step: '5'
    action: Record that the wallet was created, for whom, and when.
    record_produced: An occurrence on the trail.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Recording a decision about a person
    step: '1'
    action: Establish the person exists and has not already been decided about.
    record_produced: None.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - process: Recording a decision about a person
    step: '2'
    action: Record the decision, the authority, and the grounds where stated.
    record_produced: The person's state, and an occurrence.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  belief_verification:
  - belief: 'Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them.'
    result: VERIFIED
    evidence: Twenty-three artifacts are held for this domain, all owned by identity, including `blockchain::WF_REGISTER_ACTOR_V0` and `blockchain::WF_RECORD_VERIFICATION_DECISION_V0`, reachable through `blockchain::TI_REGISTER_ACTOR_V0`, `blockchain::TI_ACCEPT_ACTOR_V0` and `blockchain::TI_REJECT_ACTOR_V0`.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: A person keeps the details they registered with when a decision is recorded about them.
    result: VERIFIED
    evidence: Exercising the function against the pinned composition shows an accepted person still carrying the name and preferences they registered with, alongside the deciding authority and the time.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: Identity declares that it announces an acceptance, and does not actually announce it.
    result: VERIFIED
    evidence: 'Three moments are declared — `blockchain::EV_ACTOR_ACCEPTED_V0`, `blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0`, `blockchain::EV_ACTOR_REJECTED_V0`. Each reports a reference count of zero: nothing in the composition refers to any of them, so no announcement can be made from anywhere.'
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: A rejection stating no grounds is currently accepted and recorded rather than refused.
    result: VERIFIED
    evidence: Grounds are declared as required where a rejection is admitted at the boundary, and no step of the contract that records a decision reads them. Exercising the function, a rejection stating no grounds succeeds and the person is rejected.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: No wallet exists anywhere in the business today.
    result: NOT_FOUND
    evidence: Searching the composition's whole vocabulary for the term returns no match. No entity, store, process or moment concerning a wallet is held anywhere.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail.
    result: INSUFFICIENT_EVIDENCE
    evidence: Nothing of that design is present in this composition, so the snapshot cannot confirm or refute it. What the business still holds to was established by the business itself and is recorded as truth in the change request rather than as a finding here.
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  - belief: The act that creates a wallet reads records identity owns and declares nothing about them.
    result: VERIFIED
    evidence: '`blockchain::WF_CREATE_WALLET_V0` reaches `blockchain::CC_RESOLVE_ACTOR_V0`, whose two steps read `CONTACT_ADDRESS_REGISTRY` and then `ACTORS`. Both are declared by `blockchain::STRUCTURE_IDENTITY_STORAGE_V0` and reached only by `blockchain::RB_IDENTITY_BINDINGS_V0`, which the act names nowhere.'
    source_finding: {phase: p1, register: system_beliefs, row: 7}
  - belief: The business permits an act to declare the bindings it consults, and refuses a write through one.
    result: VERIFIED
    evidence: '`runtime_binding::CONSTITUTION_RUNTIME_BINDING_V0` §2a states the resolution model and `runtime_binding::INVARIANT_RB_STORAGE_SUBDOMAIN_OWNED_V0` holds a binding to describing only its own subdomain''s records. The composition seals an act''s storage from the binding it owns and those it consults, marking every record owned or consulted, and refuses a write against a consulted one.'
    source_finding: {phase: p1, register: system_beliefs, row: 8}
  - belief: A person nobody accepted is given a wallet today.
    result: VERIFIED
    evidence: Registering a person and never deciding about them, then dispatching the act, returns SUCCESS and records a wallet against them. The act takes the address off the record it read and never reads the state beside it.
    source_finding: {phase: p1, register: system_beliefs, row: 9}
  pps_baseline_fqdns:
  - capability: Records a decision about a person
    fqdn: blockchain::WF_RECORD_VERIFICATION_DECISION_V0
    what_it_does: Accepts or rejects a person, keeping their registered details.
    fit: PARTIAL
    cannot_do: Announces nothing, so nothing can follow acceptance. Does not require grounds on a rejection.
  - capability: Registers a person
    fqdn: blockchain::WF_REGISTER_ACTOR_V0
    what_it_does: Admits a person unverified on their own claim.
    fit: EXACT
    cannot_do: Nothing about a wallet.
  - capability: Holds people
    fqdn: blockchain::STRUCTURE_IDENTITY_STORAGE_V0
    what_it_does: Declares where people and their occurrences are held.
    fit: PARTIAL
    cannot_do: Declares nowhere to hold a wallet.
  - capability: Declares the acceptance moment
    fqdn: blockchain::EV_ACTOR_ACCEPTED_V0
    what_it_does: Names the moment a person is accepted.
    fit: PARTIAL
    cannot_do: Is referenced by nothing and is therefore never announced.
  - capability: Declares the registration moment
    fqdn: blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0
    what_it_does: Names the moment a person is admitted unverified.
    fit: PARTIAL
    cannot_do: Is referenced by nothing.
  - capability: Declares the rejection moment
    fqdn: blockchain::EV_ACTOR_REJECTED_V0
    what_it_does: Names the moment a person is rejected.
    fit: PARTIAL
    cannot_do: Is referenced by nothing.
  - capability: Admits a rejection
    fqdn: blockchain::TI_REJECT_ACTOR_V0
    what_it_does: Admits a rejection at the boundary, declaring grounds as required.
    fit: PARTIAL
    cannot_do: Requiring grounds at the boundary is not the same as refusing a rejection that states none; no step reads them.
  - capability: Holds a changing record
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Holds records that change.
    fit: EXACT
    cannot_do: Nothing specific to a wallet.
  - capability: Holds a trail
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Holds a trail added to and never rewritten.
    fit: EXACT
    cannot_do: Nothing specific to a wallet.
  - capability: Claims an identity
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Claims a key so two things cannot share one identity.
    fit: EXACT
    cannot_do: Nothing specific to a wallet.
  - capability: Supplies the time
    fqdn: capability_side_effects::CS_CLOCK_V0
    what_it_does: Supplies the current time.
    fit: EXACT
    cannot_do: Nothing specific to a wallet.
  - capability: Determines an identity
    fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
    what_it_does: Derives an identity from what it is given.
    fit: EXACT
    cannot_do: Nothing specific to a wallet.
  gaps:
  - gap: Nothing holds a wallet.
    severity: CRITICAL
    impact: The whole of this change. There is nowhere to record that a person holds value.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - gap: No moment is ever announced, so nothing can follow an acceptance.
    severity: CRITICAL
    impact: A wallet follows acceptance. If acceptance is never announced, wallet creation has nothing to follow.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - gap: A rejection stating no grounds is not refused.
    severity: CRITICAL
    impact: The business's own rule is unenforced, and refusals are on record with no reason attached.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - gap: There is no way to establish an address others may pay to.
    severity: CRITICAL
    impact: A wallet must have one.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: known_facts, row: 7}
  - gap: Nothing declares where a wallet would be held.
    severity: CRITICAL
    impact: A record with nowhere to live cannot be written.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - gap: The business's own currency is not named anywhere in the composition.
    severity: OPEN QUESTION
    impact: Every wallet is denominated in it.
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: assumptions, row: 3}
  - gap: The act reads records it declares no reach to.
    severity: CRITICAL
    impact: The act asks for a record it never said it would read, which is invisible until it runs.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 7}
  - gap: A person the business has not accepted is given a wallet.
    severity: CRITICAL
    impact: The business's own rule, stated plainly and enforced nowhere.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 9}
  architectural_observations:
  - observation: Every artifact this domain holds belongs to identity. Wallet would be the domain's second function.
    evidence: Twenty-three artifacts, all recorded against the identity subdomain.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - observation: A declared moment that nothing refers to is indistinguishable, from the outside, from a moment the business never declared.
    evidence: All three declared moments report a reference count of zero.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - observation: A requirement stated where a request is admitted is not the same as a rule the business enforces. Grounds are declared required at the boundary and read by nothing thereafter.
    evidence: The contract that records a decision does not mention grounds.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - observation: Everything a wallet needs in order to be held, identified, timed and trailed already exists in the platform's closed set. Nothing new of that kind is required.
    evidence: Five capabilities cover holding, trailing, claiming an identity, timing and deriving an identity.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - observation: The business already holds people and their trail in named places. A wallet is a third thing to hold, not a change to either.
    evidence: Two stores are declared for this domain.
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  discovery_concerns:
  - concern: The business believed it announced three moments and announces none. Nothing reported a fault, because nothing checks.
    evidence: Reference count of zero on all three declared moments.
    severity: CRITICAL
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - concern: The way a wallet's address is established is the one thing this change needs that the platform has no means for.
    evidence: Nothing in the closed set of things the platform can do produces an address.
    severity: MAJOR
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - concern: Wallet creation following acceptance means a second function depends on a moment identity has never actually announced. If that dependency is built before the announcement is real, wallet cannot run at all.
    evidence: Reference count of zero on the acceptance moment.
    severity: MAJOR
    evidence_status: VERIFIED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - concern: The business's own currency has no name anywhere in the composition, and every wallet is denominated in it.
    evidence: No vocabulary match.
    severity: MINOR
    evidence_status: NOT_FOUND
    source_finding: {phase: p1, register: assumptions, row: 3}
  open_questions:
  - question: What is the business's currency called?
    category: business
    why_it_matters: Every wallet is denominated in it, and the composition does not name it.
    source_finding: {phase: p1, register: assumptions, row: 3}
  - question: Is establishing an address from supplied key material something the business does itself, or something the platform must be given the means to do?
    category: governance
    why_it_matters: The platform's set of things it can do is closed, and nothing in it produces an address.
    source_finding: {phase: p1, register: known_facts, row: 18}
```

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface. What was searched is recorded, not only what was found.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3
