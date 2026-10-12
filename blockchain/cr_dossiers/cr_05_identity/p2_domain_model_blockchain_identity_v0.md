# Stage 2 — Domain Model Verification: blockchain / identity

## Machine

```yaml
document:
  phase: p2
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: The Record
    description: 'What the business holds about a person: what they registered with, their state, and the decision made about them.'
    store_model: One keyed store, one record per contact address, unchanged by this change.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - entity: The Registration
    description: 'What a person supplies to become known: their name and the address they are reached at.'
    store_model: Held in the person's record when they are registered.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - entity: The Decision
    description: 'What an authority records about an unverified person: acceptance or rejection, the authority, and the grounds.'
    store_model: Written into the person's record; the rest of the record is left as it was.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 3}
  - entity: The Business's Rules
    description: What a registration must contain, which people may be decided about, which decisions may be recorded, that a rejection states grounds, and that an authority does not decide about themselves.
    store_model: Held nowhere in identity today. Each travels with the request that is judged by it.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  entity_attributes:
  - entity: The Registration
    attribute: Name
    meaning: What the person is called. Required.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - entity: The Registration
    attribute: Contact Address
    meaning: The address the person is reached at. Required.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 1}
  - entity: The Decision
    attribute: State
    meaning: Unverified, accepted or rejected.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_states, row: 1}
  - entity: The Decision
    attribute: Verifying Authority
    meaning: The authority the decision names.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 5}
  - entity: The Decision
    attribute: Grounds
    meaning: The reason stated. Required on a rejection.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 4}
  business_processes:
  - process: Register a person
    initiator: The person
    outcome: A complete registration is recorded unverified; an incomplete one is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Accept a person
    initiator: An authority within the business
    outcome: An unverified person is recorded accepted; anyone else is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Reject a person
    initiator: An authority within the business
    outcome: An unverified person is recorded rejected, with grounds; anyone else, or a rejection without grounds, is refused.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  process_steps:
  - process: Register a person
    step: '1'
    action: Check the registration against what it must contain.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - process: Register a person
    step: '2'
    action: Claim the contact address, refusing one already held.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 2}
  - process: Register a person
    step: '3'
    action: Record the person unverified, and record that they registered.
    record_produced: The person's record, and a moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 1}
  - process: Accept or reject a person
    step: '1'
    action: Resolve the person the address names, refusing if none is found.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 4}
  - process: Accept or reject a person
    step: '2'
    action: Refuse unless the person's state admits a decision, the decision is one the business allows, and the authority is not the person.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - process: Accept or reject a person
    step: '3'
    action: Record the decision, and record that it occurred.
    record_produced: The person's record, changed in its decided parts only, and a moment on the trail.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 2}
  belief_verification:
  - belief: 'The public entrance supplies the business''s rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded.'
    result: VERIFIED
    evidence: blockchain::TI_REGISTER_ACTOR_V0 maps each request onto a payload carrying `registration_schema` — name and contact address, both required. blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 carry `states_admitting_a_decision` as UNVERIFIED and `admitted_outcomes` as ACCEPTED and REJECTED. All are constants of the boundary declaration, not values the caller sends. The two decision boundaries also carry `self_check_rules`, and the rejection boundary `grounds_rules`, in the same way.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: Identity takes each of those rules from the request rather than holding them itself.
    result: VERIFIED
    evidence: blockchain::WF_REGISTER_ACTOR_V0 binds `registration_schema` from the payload into blockchain::CC_VALIDATE_REGISTRATION_V0. blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 bind `states_admitting_a_decision`, `admitted_outcomes` and `self_check_rules` from the payload into blockchain::CC_RECORD_VERIFICATION_DECISION_V0, and the rejection workflow binds `grounds_rules` from the payload into blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0. None of these is declared by the intents that admit the requests — blockchain::IN_ACTOR_ACCEPTANCE_V0 and blockchain::IN_ACTOR_REJECTION_V0 declare only the contact address, the authority and the grounds — so the gate neither requires nor restricts them.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: 'A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded.'
    result: VERIFIED
    evidence: 'Run directly against the pinned composition: a person accepted under the business''s rules and accepted again under the same rules is refused, and accepted again with `states_admitting_a_decision` widened to include ACCEPTED succeeds. A decision of SUSPENDED is refused under the business''s outcomes and recorded when the request widens `admitted_outcomes` to include it; the person''s state is SUSPENDED afterwards, a state the business does not have. A request that sends no `self_check_rules` records an authority accepting themselves.'
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  - belief: Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway.
    result: VERIFIED
    evidence: 'blockchain::CC_VALIDATE_REGISTRATION_V0 has one step, which runs capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and publishes the violations it finds. That transform reports and never refuses, and nothing in the contract or the workflow reads the violations, so the step always succeeds. Run directly: a registration with no name, checked against a schema requiring one, is registered, and the person is held unverified with no name.'
    source_finding: {phase: p1, register: system_beliefs, row: 4}
  - belief: Through the public entrance an incomplete registration is refused before identity checks it.
    result: VERIFIED
    evidence: blockchain::TI_REGISTER_ACTOR_V0 declares `name` and `contact_address` as required inputs, and the transport resolver refuses a request missing a required input with INPUT_MISSING before any workflow is dispatched. The fault in identity's registration check cannot be reached from outside.
    source_finding: {phase: p1, register: system_beliefs, row: 5}
  - belief: The wallet function holds its own rule about who may have a wallet, rather than taking it from the request.
    result: VERIFIED
    evidence: blockchain::WF_CREATE_WALLET_V0 hands blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 `states_admitting_a_wallet` as the literal set ACCEPTED, written in the workflow, and the holder's state from the resolved record. Nothing in the request can widen it.
    source_finding: {phase: p1, register: system_beliefs, row: 6}
  pps_baseline_fqdns:
  - capability: Checking a registration
    fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    what_it_does: Checks a registration against a schema and publishes the violations.
    fit: PARTIAL
    cannot_do: It refuses nothing, and it takes the schema from the request.
  - capability: Claiming a contact address
    fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    what_it_does: Claims the address a registration names, reporting one already held.
    fit: EXACT
    cannot_do: Nothing for this purpose; unchanged by this change.
  - capability: Recording a decision
    fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    what_it_does: Refuses a state that admits no decision, an outcome not admitted and an authority deciding about themselves, then records the decided parts of the record.
    fit: PARTIAL
    cannot_do: Every refusal it makes is against a set or a rule handed to it; it holds none of them.
  - capability: Requiring grounds for a rejection
    fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    what_it_does: Refuses a rejection whose grounds fail the rules handed to it.
    fit: PARTIAL
    cannot_do: It holds no rule of its own; the rules come from the request.
  - capability: Resolving a person
    fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    what_it_does: Resolves a contact address to the person's record.
    fit: EXACT
    cannot_do: Nothing for this purpose.
  - capability: Registration act
    fqdn: blockchain::WF_REGISTER_ACTOR_V0
    what_it_does: Checks, claims, records and announces a registration.
    fit: PARTIAL
    cannot_do: It binds the registration schema from the request, and continues past a check that found violations.
  - capability: Acceptance act
    fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    what_it_does: Resolves the person, records the acceptance and announces it.
    fit: PARTIAL
    cannot_do: It binds the admitted states, the admitted outcomes and the self-decision rule from the request.
  - capability: Rejection act
    fqdn: blockchain::WF_REJECT_ACTOR_V0
    what_it_does: Requires grounds, resolves the person, records the rejection and announces it.
    fit: PARTIAL
    cannot_do: It binds the grounds rules, the admitted states, the admitted outcomes and the self-decision rule from the request.
  - capability: Public registration entrance
    fqdn: blockchain::TI_REGISTER_ACTOR_V0
    what_it_does: Admits a registration request and supplies the schema and the rest of the act's constants.
    fit: EXACT
    cannot_do: Nothing for this purpose. It stops supplying rules identity will hold itself.
  - capability: Public acceptance entrance
    fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    what_it_does: Admits an acceptance request and supplies the admitted states, outcomes and self-decision rule.
    fit: EXACT
    cannot_do: Nothing for this purpose. It stops supplying rules identity will hold itself.
  - capability: Public rejection entrance
    fqdn: blockchain::TI_REJECT_ACTOR_V0
    what_it_does: Admits a rejection request and supplies the admitted states, outcomes, self-decision rule and grounds rules.
    fit: EXACT
    cannot_do: Nothing for this purpose. It stops supplying rules identity will hold itself.
  - capability: Membership check
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Refuses a value that is not in a given set.
    fit: EXACT
    cannot_do: Nothing; the set it is given is what this change fixes.
  - capability: Rule check
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Refuses parameters that fail a given list of rules.
    fit: EXACT
    cannot_do: Nothing; it can refuse on a check's violations, as another domain already does.
  - capability: Structure check
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Reports every way a record fails a schema.
    fit: PARTIAL
    cannot_do: It reports and never refuses. Refusing on what it reports is the calling contract's business (ruled for v5).
  - capability: Holding a rule in the act
    fqdn: blockchain::WF_CREATE_WALLET_V0
    what_it_does: Hands its refusal the admitted states as a literal written in the workflow.
    fit: EXACT
    cannot_do: Nothing; it is the precedent this change follows.
  gaps:
  - gap: Identity holds none of its own rules; each comes with the request it judges.
    severity: CRITICAL
    impact: Anything reaching identity other than through the public entrance can record a second decision, a decision the business never allowed, or an authority deciding about themselves.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: A registration identity finds incomplete is registered anyway.
    severity: MAJOR
    impact: A person can be held with no name. Unreachable through the public entrance, reachable any other way.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 4}
  - gap: Nothing records which of identity's rules are the business's own.
    severity: MINOR
    impact: The rules are stated in the business's documents and in the public entrance's constants, and nowhere identity itself reads.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  architectural_observations:
  - observation: The public entrance holds the rules correctly, so nothing seen from outside is wrong, and nothing seen from outside can show the fault.
    evidence: Every constant the entrances supply is the business's rule, and the entrance refuses an incomplete registration before identity is reached. The fault is in what identity accepts from anything else.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 5}
  - observation: Wallet closed the same hole by writing the rule into the act.
    evidence: The wallet act's refusal is handed a literal set; the request carries no rule at all.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 6}
  - observation: A check that reports is made to refuse by a rule that follows it.
    evidence: Another domain's registration check follows the structure check with a rule step requiring the violations to be empty, and refuses otherwise. The same composition applies here without any new capability.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 13}
  - observation: The admission gates are silent on the rules, so moving them into the acts changes no gate.
    evidence: Neither decision intent declares a rule field; the rules pass through the gate undeclared. Holding them in the acts removes fields nothing admits against.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  discovery_concerns:
  - concern: Two more of identity's rules travel with the request than the change request names.
    evidence: The rule that an authority does not decide about themselves, and the rule that a rejection states its grounds, are each handed to identity by the request, and the first was shown widened by a request that sends none. The change request names what a registration must contain, who may be decided about and which decisions may be recorded; its invariants state that every business rule of identity's is held by identity, which covers these two as well. Put to the business author, who answered that identity holds all five.
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - concern: The two rule sets a decision is checked against are also used to compose the record it writes and the moment it records.
    evidence: The decided record and the occurrence are assembled from request fields as well, and the recorded state is taken from them rather than from the decision. Whether the record could disagree with the decision is not what this change asks, and it is not examined here.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. The function
exists, runs and is reached from outside. What is verified here is where each of identity's rules is
read from, and what identity does with what its registration check finds. Each belief about behaviour
was established by running identity's acts directly against the pinned composition, on a scratch
data root, bypassing the public entrance.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
