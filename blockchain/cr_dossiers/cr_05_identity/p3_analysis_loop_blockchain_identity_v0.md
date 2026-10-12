# Stage 3 — Analysis Loop: blockchain / identity

## Machine

```yaml
document:
  phase: p3
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'Every rule identity applies is handed to it by the request, and the public entrance is the only thing supplying the business''s values. There are five: what a registration must contain, which states admit a decision, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states its grounds.'
    impact: Moving each into identity closes the gap whichever way identity is reached, and removes those values from the entrances, which no longer need to supply them.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #1 and #2; the author answered that identity holds all five (S2 discovery_concerns #1)'
  - question_id: Q2
    finding: The registration check reports and nothing acts on the report. The structure check publishes its violations; the contract's single step succeeds whatever it found. A rule step requiring the violations to be empty, following the check, turns the report into a refusal, and a composition in another domain already does exactly this.
    impact: The registration contract gains one step. The platform check stays a reporter, as ruled for v5.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 has one step; causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 follows the same check with capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 requiring `violations` to equal an empty list
  - question_id: Q3
    finding: 'Four of the five rules are fixed values and can be written where they are used: the registration schema, the admitted states, the admitted outcomes and the grounds rules. Written in the contracts that apply them, they hold for every act composing those contracts, and no act or request can widen them. Wallet wrote its rule in the act rather than the contract; here the deciding contract is shared by the acceptance and rejection acts, and the rules are the same for both, so the contract is the one place that holds them for both.'
    impact: Three contracts change what they take and what they hold. The acts stop binding the rules from the request.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::CC_RECORD_VERIFICATION_DECISION_V0 is composed by blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 with the same sets; blockchain::WF_CREATE_WALLET_V0 hands its contract a literal set
  - question_id: Q4
    finding: The fifth rule — an authority does not decide about themselves — compares two values of the request, and the rule checker compares a field only against a fixed value. Comparing the authority with the person, then requiring that they are not equal, holds the rule with nothing taken from the request, using two platform transforms the composition already publishes.
    impact: The deciding contract replaces its request-supplied self-check with a comparison and a fixed rule on its result.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 supports not_null, eq, neq, in and numeric comparisons against a rule's value, and no comparison between fields; capability_transforms::CT_PURE_COMPARE_EQUAL_V0 returns whether two values are equal
  - question_id: Q5
    finding: 'The state a decision records is taken from the request, not from the decision the contract checked. Run directly against the pinned composition, a request whose decision is ACCEPTED, and so admitted, records the state SUSPENDED. And the decision itself is the request''s: the acceptance act records whatever decision it is handed, so a rejection can be recorded through it without the grounds the rejection act requires. Holding which decisions may be recorded therefore needs the record to be built from the checked decision, and each act to fix the decision it records.'
    impact: The deciding contract builds the decided record from its own inputs — the decision, the authority and the grounds — and each act hands it its own decision as a fixed value.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::CC_RECORD_VERIFICATION_DECISION_V0 assembles the record from `decided_actor_fields`, a request field whose `state` is independent of `decision`; run directly, ACCEPTED was checked and SUSPENDED recorded
  - question_id: Q6
    finding: Registration records whatever state the request hands it. Run directly against the pinned composition, a registration carrying the state ACCEPTED is registered accepted, with no decision and no authority, and the wallet function would then give that person a wallet. The business's lifecycle has one way in, a complete registration, and it leads to unverified.
    impact: The registration act writes the state unverified as its own fixed value, whatever the request carries.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::WF_REGISTER_ACTOR_V0 writes `actor_record` from the payload, whose `state` blockchain::TI_REGISTER_ACTOR_V0 sets to UNVERIFIED as a constant; run directly with ACCEPTED, the person was held accepted
  - question_id: Q7
    finding: Nothing a caller sees through the public entrance changes. Every value the entrances supply today is the business's rule and becomes identity's own, so every request admitted there reaches the same outcome, and what the caller is told is projected from result surfaces that do not change. The entrances only stop supplying what identity now holds.
    impact: The entrances are amended to drop their rule constants. No input a caller sends, and no answer a caller receives, changes.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S2 belief_verification #1 and #5; the TE declarations are untouched'
  - question_id: Q8
    finding: The acceptance and rejection gates declare none of the rule fields. The registration gate requires the schema, so once the entrance stops supplying it, every registration through the entrance would be refused at admission. The acceptance gate does not declare the grounds an acceptance may carry, although the entrance accepts them and the act will read them.
    impact: The registration intent stops requiring the schema identity now holds. The acceptance intent declares grounds as optional, so the gate states what the act reads.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::IN_ACTOR_REGISTERED_V0 requires actor_record and registration_schema; blockchain::IN_ACTOR_ACCEPTANCE_V0 declares contact_address and verifying_authority; blockchain::TI_ACCEPT_ACTOR_V0 accepts grounds as optional
  - question_id: Q9
    finding: The moment each act records, and the stream it records to, also come from the request. A direct caller can record a moment that names a different occurrence from the one that happened. The trail is outside what this change asks, and no rule of the business's names it.
    impact: Recorded and carried; not changed here.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_REGISTER_ACTOR_V0 bind occurrence_fields and stream_id from the payload
  - question_id: Q10
    finding: Records made under a request's own rules stay as they were made. The business adds to its record and does not rewrite it, so a person registered or decided about under a widened rule keeps that record.
    impact: No repair, no backfill.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: 'S1 constraints #2; S1 out_of_scope #4'
  verification_results:
  - item: 'The public entrance supplies the business''s rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded.'
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q7
  - item: Identity takes each of those rules from the request rather than holding them itself.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q1, Q3 and Q4
  - item: 'A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded.'
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q3 and Q5; Q5 adds that the recorded state need not be the checked decision
  - item: Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway.
    origin: {phase: p2, register: belief_verification, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: Through the public entrance an incomplete registration is refused before identity checks it.
    origin: {phase: p2, register: belief_verification, row: 5}
    result: CONFIRMED
    evidence: Resolved in Q7
  - item: The wallet function holds its own rule about who may have a wallet, rather than taking it from the request.
    origin: {phase: p2, register: belief_verification, row: 6}
    result: CONFIRMED
    evidence: Resolved in Q3
  - item: Identity holds none of its own rules; each comes with the request it judges.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 through Q6
  - item: A registration identity finds incomplete is registered anyway.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q2
  - item: Two more of identity's rules travel with the request than the change request names.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q4, per the author's answer
  - item: The two rule sets a decision is checked against are also used to compose the record it writes and the moment it records.
    origin: {phase: p2, register: discovery_concerns, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q5 for the record, and carried in Q9 for the moment
  dependency_discoveries:
  - dependency: Checking a record's structure
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, unchanged
  - dependency: Refusing on a list of rules
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged
  - dependency: Refusing a value outside a set
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, unchanged
  - dependency: Comparing two values
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_COMPARE_EQUAL_V0, unchanged
  - dependency: Assembling a record from fields
    type: Platform transform
    disposition: REUSE
    evidence: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, unchanged
  - dependency: Checking a registration
    type: Capability contract
    disposition: EXTEND
    evidence: blockchain::CC_VALIDATE_REGISTRATION_V0 holds its schema and refuses on violations
  - dependency: Recording a decision
    type: Capability contract
    disposition: EXTEND
    evidence: blockchain::CC_RECORD_VERIFICATION_DECISION_V0 holds its sets and self-decision rule, and builds its record from the decision
  - dependency: Requiring rejection grounds
    type: Capability contract
    disposition: EXTEND
    evidence: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 holds its rules
  - dependency: The three acts
    type: Workflows
    disposition: EXTEND
    evidence: blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 stop binding rules from the request, and fix the state or decision each records
  - dependency: The three entrances
    type: Transport ingress
    disposition: EXTEND
    evidence: blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 stop supplying what identity holds
  - dependency: The acceptance gate
    type: Intent
    disposition: EXTEND
    evidence: blockchain::IN_ACTOR_ACCEPTANCE_V0 declares optional grounds
  - dependency: The registration gate
    type: Intent
    disposition: EXTEND
    evidence: blockchain::IN_ACTOR_REGISTERED_V0 stops requiring the schema
  - dependency: Resolving the person, claiming the address, writing the record, appending the moment
    type: Capability contracts
    disposition: REUSE
    evidence: blockchain::CC_RESOLVE_ACTOR_V0, blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_REGISTER_ACTOR_V0 and blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0, unchanged
  - dependency: The moment each act records
    type: Workflow bindings
    disposition: INVESTIGATE
    evidence: Carried in Q9; outside this change
  impact_analysis:
  - artifact: blockchain::CC_VALIDATE_REGISTRATION_V0
    impact_scope: Amended — holds its schema, gains a refusal step
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    impact_scope: Amended — holds its sets and self-decision rule, builds its record from the decision
    consumer_count: '10'
    evidence: si.topology.impact impacted_count 10
  - artifact: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    impact_scope: Amended — holds its rules
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: blockchain::WF_REGISTER_ACTOR_V0
    impact_scope: Amended — stops binding the schema, writes the state unverified
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_ACCEPT_ACTOR_V0
    impact_scope: Amended — stops binding the rules, fixes its decision
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::WF_REJECT_ACTOR_V0
    impact_scope: Amended — stops binding the rules, fixes its decision
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_REGISTER_ACTOR_V0
    impact_scope: Amended — drops the schema and the state it supplied
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_ACCEPT_ACTOR_V0
    impact_scope: Amended — drops the rules and the decided record it supplied
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::TI_REJECT_ACTOR_V0
    impact_scope: Amended — drops the rules and the decided record it supplied
    consumer_count: '0'
    evidence: si.topology.impact impacted_count 0
  - artifact: blockchain::IN_ACTOR_ACCEPTANCE_V0
    impact_scope: Amended — declares optional grounds
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  - artifact: blockchain::IN_ACTOR_REGISTERED_V0
    impact_scope: Amended — stops requiring the schema
    consumer_count: '1'
    evidence: si.topology.impact impacted_count 1
  authoring_decisions:
  - capability: Check a registration and refuse an incomplete one
    decision: EXTEND
    rationale: The check already finds what is missing. It holds what a registration must contain, and a rule following it refuses when anything is found, as another part of the business already does.
    alternatives_checked: 'Making the platform check refuse was checked and rejected by ruling: a check that decides can no longer be used only to report. Refusing at the entrance alone was checked and rejected: that is today''s arrangement, and it holds nothing against any other way in.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    decision: EXTEND
    rationale: The deciding step holds which states admit a decision and which decisions may be recorded, and builds the record from the decision it checked.
    alternatives_checked: 'Holding the sets in each act, as wallet did, was checked and rejected: both acts share one deciding step with the same sets, and holding them there covers every act that composes it. Checking the request''s record against the decision was checked and rejected: it keeps the record the request''s to state.'
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - capability: Refuse an authority deciding about themselves
    decision: EXTEND
    rationale: The deciding step compares the authority with the person and refuses when they are the same, taking nothing from the request but the two values.
    alternatives_checked: 'A new rule operation comparing two fields was checked and rejected: the comparison the platform already offers, followed by a fixed rule, says the same thing without changing the platform.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Refuse a rejection stating no grounds
    decision: EXTEND
    rationale: 'The grounds step holds its own rules: grounds are present and not empty.'
    alternatives_checked: Nothing else was needed; the step existed and took its rules from the request.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - capability: Fix the decision each act records
    decision: EXTEND
    rationale: The acceptance act records an acceptance and the rejection act a rejection, each as its own fixed value.
    alternatives_checked: 'Leaving the decision to the request was checked and rejected: a rejection could then be recorded through the acceptance act without grounds.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Register a person unverified
    decision: EXTEND
    rationale: The registration act records the state unverified as its own fixed value.
    alternatives_checked: 'Checking the requested state was checked and rejected: there is only one state a registration may lead to, so there is nothing to check, only something to write.'
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
  - capability: Reach identity from outside
    decision: EXTEND
    rationale: The entrances stop supplying what identity now holds. A caller sends and is told exactly what they are today.
    alternatives_checked: 'Leaving the constants in place was checked and rejected: they would be values nothing reads, and a reader would take them for the rule.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Admit an acceptance with its grounds
    decision: EXTEND
    rationale: The acceptance gate declares the optional grounds the entrance already accepts and the act now reads.
    alternatives_checked: Nothing else was needed.
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
  - capability: Admit a registration without the schema identity holds
    decision: EXTEND
    rationale: The registration gate stops requiring the schema, which identity now holds and the entrance no longer supplies.
    alternatives_checked: 'Leaving the gate as it is was checked and rejected: every registration through the entrance would be refused at admission.'
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
  - capability: Record the moment of each act
    decision: REUSE
    rationale: Unchanged. The moment and its stream remain the request's to name; recorded as a finding and outside this change.
    alternatives_checked: 'Holding the moment in each act was checked and deferred: no rule of the business names it, and the change request does not ask.'
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
  placement_decision:
  - decision: EXTEND
    subdomain: identity
    rationale: Every rule held here is identity's own, and every step that changes belongs to identity. Nothing moves and no other subdomain changes.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: 'The one CRITICAL gap resolves to committed decisions: each of the five rules is held by the step that applies it, and the record and the decision each act writes are its own'
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All ten findings are CLOSED. The one question Stage 2 raised was answered by the business author
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass, running the acts directly, added the recorded state and the registered state; a third pass over what each act writes found only the recorded moment, carried as outside this change
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All ten items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED; four were established by running the acts against the pinned composition
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each of identity's rules is held, and what
identity does with what it finds. Two further places where the request decides what identity
records were found by running the acts directly, and are resolved here under the change request's
own invariant that a business rule of identity's is held by identity.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
