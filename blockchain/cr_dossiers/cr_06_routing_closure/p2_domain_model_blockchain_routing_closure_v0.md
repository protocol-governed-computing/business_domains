# Stage 2 — Domain Model Verification: blockchain / identity and wallet

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain:
  - identity
  - wallet
  cr: cr_06_routing_closure
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Person's Record
    description: 'What the business holds about a person: their registration, their state and the decision made about them.'
    store_model: One keyed store, one record per contact address, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: The Claimed Address
    description: The contact address a person holds, which no one else may hold.
    store_model: One registry, one entry per address, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: The Trail
    description: The moments in a person's or a wallet's history.
    store_model: Append-only, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: The Wallet
    description: The wallet an accepted person is given, and its claimed identity.
    store_model: One keyed store and one registry, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: A Failed Record
    description: A record that could not be read or written.
    store_model: Not stored; it is an answer a store gives.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  entity_attributes:
  - entity: A Failed Record
    attribute: The store's answer
    meaning: 'BACKEND_ERROR: the store was unreachable or answered with an error. Every store identity and wallet use declares it.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: The Person's Record
    attribute: State
    meaning: Unverified, accepted or rejected. Unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  business_processes:
  - process: Register a person
    initiator: The person
    outcome: A complete registration is recorded unverified; anything else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Accept a person
    initiator: An authority
    outcome: An unverified person is recorded accepted; anything else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Reject a person
    initiator: An authority
    outcome: An unverified person is recorded rejected, with grounds; anything else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Create a wallet
    initiator: An accepted person
    outcome: A wallet is recorded for an accepted person; anything else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  process_steps:
  - process: Register a person
    step: '1'
    action: Check the registration.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 5}
  - process: Register a person
    step: '2'
    action: Claim the contact address.
    record_produced: The claimed address.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - process: Register a person
    step: '3'
    action: Record the person unverified.
    record_produced: The person's record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 3}
  - process: Register a person
    step: '4'
    action: Record that they registered.
    record_produced: A moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 4}
  - process: Accept or reject a person
    step: '1'
    action: Look the person up by their address, and read their record.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Accept or reject a person
    step: '2'
    action: Record the decision.
    record_produced: The person's record, in its decided parts.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 6}
  - process: Accept or reject a person
    step: '3'
    action: Record that it occurred.
    record_produced: A moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 4}
  - process: Create a wallet
    step: '1'
    action: Look the person up, and require them accepted.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 1}
  - process: Create a wallet
    step: '2'
    action: Claim the wallet's identity.
    record_produced: The claimed wallet identity.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 7}
  - process: Create a wallet
    step: '3'
    action: Record the wallet.
    record_produced: The wallet.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 8}
  - process: Create a wallet
    step: '4'
    action: Record that it was created.
    record_produced: A moment on the wallet's trail.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 9}
  belief_verification:
  - belief: Most identity and wallet acts stop without a declared ending when a record fails.
    result: VERIFIED
    evidence: 'Every store identity and wallet use declares BACKEND_ERROR for each operation they call. Thirteen act nodes run a contract that can end with BACKEND_ERROR, and none of the four acts routes it: blockchain::WF_REGISTER_ACTOR_V0 at three nodes, blockchain::WF_ACCEPT_ACTOR_V0 at three, blockchain::WF_REJECT_ACTOR_V0 at three, and blockchain::WF_CREATE_WALLET_V0 at four. The runtime refuses an unrouted outcome when one arises, so the act stops, but nothing the business declared says how it ended.'
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: When an acceptance's lookup of the person fails, identity carries on and records the acceptance.
    result: VERIFIED
    evidence: blockchain::CC_RESOLVE_ACTOR_V0's lookup step answers for SUCCESS, NOT_FOUND and VIOLATION, and its store, capability_side_effects::CS_REGISTRY_V0, also declares BACKEND_ERROR for RESOLVE. Run against the pinned composition with the address registry corrupted, the lookup answered BACKEND_ERROR; the runtime carried on to read the person's record, the contract reported SUCCESS, and the acceptance was recorded. The trace recorded neither the lookup's answer nor the decision to carry on.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: Three of wallet's steps carry on past a failed record in the same way.
    result: VERIFIED
    evidence: blockchain::CC_CLAIM_WALLET_IDENTITY_V0's claim step, blockchain::CC_CREATE_WALLET_RECORD_V0's write step and blockchain::CC_APPEND_WALLET_OCCURRENCE_V0's append step each omit BACKEND_ERROR, which their stores declare. Identity's reading step in blockchain::CC_RESOLVE_ACTOR_V0 omits it too. Five steps in four contracts.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: Each act already has a rejected ending.
    result: VERIFIED
    evidence: All four acts declare EXIT_REJECTED, and route every refusal they answer for there.
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: Every identity and wallet act this change touches was published in v5.
    result: VERIFIED
    evidence: The four contracts whose steps change (blockchain::CC_RESOLVE_ACTOR_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0) and the four acts whose routing changes (blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::WF_CREATE_WALLET_V0) are each in the sealed v5 composition. The four contracts that already end with BACKEND_ERROR keep what they declare.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: Entrances and intents name the workflows they start, and workflows name the contracts they run.
    result: VERIFIED
    evidence: The four contracts are run by blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0, all replaced here, and by blockchain::WF_RECORD_VERIFICATION_DECISION_V0, stood down before v5. The acts are named by blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 in handler.workflow, and by blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0 in workflow, by short code. Outside the composition, the identity and wallet execution validations and the RUNBOOK run the acts by full name.
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  pps_baseline_fqdns:
  - capability: Looking a person up
    fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    what_it_does: Resolves a contact address to the person's record, and reads it.
    fit: PARTIAL
    cannot_do: Neither step answers for a failed record, so a failed lookup is carried past.
  - capability: Claiming a contact address
    fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    what_it_does: Claims the address a registration names.
    fit: PARTIAL
    cannot_do: It ends with BACKEND_ERROR on a failed claim, and no act routes it.
  - capability: Recording a person
    fqdn: blockchain::CC_REGISTER_ACTOR_V0
    what_it_does: Writes the person's record.
    fit: PARTIAL
    cannot_do: It ends with BACKEND_ERROR on a failed write, and no act routes it.
  - capability: Recording a moment on a person's trail
    fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    what_it_does: Appends a moment to the person's trail.
    fit: PARTIAL
    cannot_do: It ends with BACKEND_ERROR on a failed append, and no act routes it.
  - capability: Checking a registration
    fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    what_it_does: Refuses an incomplete registration.
    fit: EXACT
    cannot_do: Nothing for this purpose; it touches no record.
  - capability: Recording a decision
    fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    what_it_does: Records the decision it checked.
    fit: PARTIAL
    cannot_do: It ends with BACKEND_ERROR on a failed write, and no act routes it.
  - capability: Claiming a wallet's identity
    fqdn: blockchain::CC_CLAIM_WALLET_IDENTITY_V0
    what_it_does: Claims the identity a wallet is given.
    fit: PARTIAL
    cannot_do: Its step does not answer for a failed claim, so the act carries past it.
  - capability: Recording a wallet
    fqdn: blockchain::CC_CREATE_WALLET_RECORD_V0
    what_it_does: Writes the wallet's record.
    fit: PARTIAL
    cannot_do: Its write step does not answer for a failed write.
  - capability: Recording a moment on a wallet's trail
    fqdn: blockchain::CC_APPEND_WALLET_OCCURRENCE_V0
    what_it_does: Appends a moment to the wallet's trail.
    fit: PARTIAL
    cannot_do: Its append step does not answer for a failed append.
  - capability: Registration act
    fqdn: blockchain::WF_REGISTER_ACTOR_V0
    what_it_does: Checks, claims, records and announces a registration.
    fit: PARTIAL
    cannot_do: Three nodes leave a failed record unrouted.
  - capability: Acceptance act
    fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    what_it_does: Looks the person up, records the acceptance and announces it.
    fit: PARTIAL
    cannot_do: Three nodes leave a failed record unrouted.
  - capability: Rejection act
    fqdn: blockchain::WF_REJECT_ACTOR_V0
    what_it_does: Requires grounds, looks the person up, records the rejection and announces it.
    fit: PARTIAL
    cannot_do: Three nodes leave a failed record unrouted.
  - capability: Wallet act
    fqdn: blockchain::WF_CREATE_WALLET_V0
    what_it_does: Looks the person up, claims and records a wallet, and announces it.
    fit: PARTIAL
    cannot_do: Four nodes leave a failed record unrouted.
  - capability: Registration entrance
    fqdn: blockchain::TI_REGISTER_ACTOR_V0
    what_it_does: Admits a caller's registration and starts the act it names.
    fit: PARTIAL
    cannot_do: Names the published registration act.
  - capability: Acceptance entrance
    fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    what_it_does: Admits a caller's acceptance and starts the act it names.
    fit: PARTIAL
    cannot_do: Names the published acceptance act.
  - capability: Rejection entrance
    fqdn: blockchain::TI_REJECT_ACTOR_V0
    what_it_does: Admits a caller's rejection and starts the act it names.
    fit: PARTIAL
    cannot_do: Names the published rejection act.
  - capability: Registration intent
    fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    what_it_does: Starts the registration act.
    fit: PARTIAL
    cannot_do: Names the published registration act.
  - capability: Acceptance intent
    fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    what_it_does: Starts the acceptance act.
    fit: PARTIAL
    cannot_do: Names the published acceptance act.
  - capability: Rejection intent
    fqdn: blockchain::IN_ACTOR_REJECTION_V0
    what_it_does: Starts the rejection act.
    fit: PARTIAL
    cannot_do: Names the published rejection act.
  - capability: Wallet intent
    fqdn: blockchain::IN_WALLET_CREATION_V0
    what_it_does: Starts the wallet act.
    fit: PARTIAL
    cannot_do: Names the published wallet act.
  gaps:
  - gap: Five steps carry on past a failed record.
    severity: CRITICAL
    impact: A person was accepted whose lookup had failed. The same can happen in wallet when a claim, a write or an append fails.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Thirteen act nodes leave a failed record without a declared ending.
    severity: MAJOR
    impact: The act stops, and nothing the business declared says how it ended. The caller cannot tell a refusal from a failure nobody planned for.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Eight published acts would mean something v5 did not say if changed in place.
    severity: CRITICAL
    impact: A citation of v5 would name acts that answer a failed record v5 left unanswered.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - gap: Seven entrances and intents name the published acts.
    severity: MAJOR
    impact: Once the acts are stood down, they would still be started.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  architectural_observations:
  - observation: The two gaps feed each other. When a step answers for a failed record, the contract can then end with it, and every act running that contract must route it.
    evidence: Closing the five step gaps adds BACKEND_ERROR to two contracts that do not end with it today, and the act nodes running them gain a failed record to route.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - observation: The stores already say they can fail. Nothing new is needed to name the failure.
    evidence: Every store's operations declare BACKEND_ERROR among their outcomes.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: entity_attributes, row: 1}
  - observation: Each act already has the ending a failed record should reach.
    evidence: All four acts declare EXIT_REJECTED.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - observation: The open standard now requires both closures.
    evidence: '`v1` Changes 3 and 4 of the Open PGC Standard require a composed step to answer for every outcome its store declares (CP-13), and construction to refuse an outcome no route answers (GC-15). This change makes identity and wallet meet both.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: A workflow's place keeps its label when the contract it runs is replaced.
    evidence: The compiler maps each place's label to the contract it runs, so a binding that reads a place keeps working when only the contract's identity changes.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  - observation: A stood-down act may name a stood-down act.
    evidence: blockchain::WF_RECORD_VERIFICATION_DECISION_V0 runs the published lookup and is out of reach; it is not re-pointed.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  discovery_concerns:
  - concern: An act that fails after recording something leaves that record in place.
    evidence: A registration whose trail append fails has already recorded the person. The business decided a refusal changes no record, and that records made before a failure stay as they were.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: constraints, row: 2}
  - concern: A superseded act carries the same gap.
    evidence: blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is superseded and no longer dispatched, so nothing reaches its two unrouted nodes.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is what each identity and wallet act does when a record it touches fails. Each
contract's steps were read for the outcomes their stores declare and the outcomes each step answers
for. Each act's routing was read for the outcomes its contracts can end with. The acceptance's
failed lookup was run directly against the pinned composition, with the address registry made
unreadable, on a scratch data root.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
