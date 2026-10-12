# Stage 3 — Analysis Loop: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p3
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P3_V0
registers:
  analysis_findings:
  - question_id: Q1
    finding: 'An act runs once from start to end, and nothing loops across acts. A hosted response is therefore written one act per step: the host offers, the act chooses and records, and the host asks again. The business never calls the host.'
    impact: 'Three acts: begin a hosted request, offer candidates, release the response. The host drives them; it holds no authority in any of them.'
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Workflows are acyclic; causal_language_model::WF_SUBMIT_USER_PROMPT_V0 writes inside one molecule
  - question_id: Q2
    finding: 'Beginning a hosted request is admitted by the same checks as the test model''s way: the request''s identity, the requester for the customer, the model registered and in service, and the ceiling.'
    impact: Those four contracts are reused unchanged, in the same order.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
  - question_id: Q3
    finding: A hosted model's reading capacity is in tokens, counted by the host, which learns what the model reads only at admission. Admission assembles the reading exactly as for the test model, whose word count can only undercount tokens; the host reports its token count with each offer, and the business compares it with the registered capacity before choosing.
    impact: Admission reuses the test model's reading check unchanged; a new check on the offer compares the reported count with the capacity.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 counts words; the author answered that capacity is in tokens and the host reports the count
  - question_id: Q4
    finding: 'A request''s record is a trail of entries per request, and retrieval returns all of them. The record of a hosted request can therefore open at admission, take one entry per step, and close on release or refusal, with no new store. The trail itself is the state of the response: its opening entry holds the rules, the limits and the fingerprint, and its steps hold what was chosen.'
    impact: An opening entry, a step entry per offer, and the existing record as the closing entry, all in the existing trail. An abandoned request is an open trail, visible to retrieval as it stands.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 reads every entry for the request; the author answered that the record opens at admission
  - question_id: Q5
    finding: 'The rules'' choice for a token is the test model''s choice with one difference: tokens carry their own spacing and are joined as they are, so a pattern split across tokens is judged on the text as built. The end of a response is a marker the host passes as a candidate.'
    impact: A new transform chooses a permitted token by the same stopping and choosing as the word transform; the word transform is left unchanged.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 joins by a space
  - question_id: Q6
    finding: The permitted length of a hosted response is the smaller of the model's registered maximum and the longest response in the rules.
    impact: The limit is formed from both when the record opens, and a step past it is refused as unfinished.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The author answered the smaller of the two
  - question_id: Q7
    finding: An offer names a fingerprint, and the business holds the admitted model's. An offer for another model refuses the request. Any caller naming the request and the fingerprint may offer; authenticating the host is out of scope.
    impact: The fingerprint is compared at every step; there is no host authorization check.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: The author answered that the host holds no authority
  - question_id: Q8
    finding: Release reads the trail, confirms the response complete and not stopped, and closes the record with the response as the business chose it. The host never supplies the text it asks to release.
    impact: Release reuses the releasability and recording contracts.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0
  - question_id: Q9
    finding: 'A time in service''s response rules are stored as placed, and admission forms from them only the rules the test model uses. A rule that numbers come from the reading can therefore be set at placement, carried into the opening entry beside the rules in force, and applied only by the token choice. A number is judged on its digits, the separators between them ignored: it is not begun unless a number the model read begins with those digits, and not ended unless it is one.'
    impact: Grounding is carried from the stored rules into the opening entry and applied by the new choice transform; the rule-forming transform and the test model's way are unchanged, and a time in service that does not set it behaves as before.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 stores the response rules as given; causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 forms only the forbidden patterns, the freedom and the seed
  - question_id: Q10
    finding: 'A pattern judged only when it is complete lets its beginning through: a model asked for a number it read and must not write can write all but its last digit, one token at a time, and then a lookalike character in place of the last.'
    impact: The choice judges text in its compatibility form, so a lookalike is the character it looks like, and does not let the model begin a number it read that a rule forbids unless the digits could still become a permitted number it read.
    evidence_status: OBSERVED
    confidence: HIGH
    resolution_status: CLOSED
    evidence: Qwen3 8B, asked for a spouse's account number it read, wrote seven of its eight digits and then a subscript one
  verification_results:
  - item: The model_response subdomain already admits a request, forms the response rules in force, and records every request.
    origin: {phase: p2, register: belief_verification, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q2 and Q4
  - item: The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates.
    origin: {phase: p2, register: belief_verification, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q1 and Q5
  - item: A registered model's description can carry its reading capacity and its maximum response length.
    origin: {phase: p2, register: belief_verification, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q3 and Q6
  - item: Nothing lets a host offer candidates and receive the business's choice.
    origin: {phase: p2, register: gaps, row: 1}
    result: CONFIRMED
    evidence: Resolved in Q1, Q5 and Q7
  - item: Nothing records a request from its admission, with every offer and choice.
    origin: {phase: p2, register: gaps, row: 2}
    result: CONFIRMED
    evidence: Resolved in Q4
  - item: Nothing releases a response separately from writing it.
    origin: {phase: p2, register: gaps, row: 3}
    result: CONFIRMED
    evidence: Resolved in Q8
  - item: Nothing measures reading in tokens or limits a response by the model's registered maximum.
    origin: {phase: p2, register: gaps, row: 4}
    result: CONFIRMED
    evidence: Resolved in Q3 and Q6
  - item: The test model's way of answering must stay unchanged.
    origin: {phase: p2, register: discovery_concerns, row: 1}
    result: CONFIRMED
    evidence: No artifact of it is redeclared
  dependency_discoveries:
  - dependency: Admission
    type: Capability contracts
    disposition: REUSE
    evidence: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
  - dependency: Forming the rules in force
    type: Domain transform
    disposition: REUSE
    evidence: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
  - dependency: Assembling what the model reads
    type: Capability contract
    disposition: REUSE
    evidence: causal_language_model::CC_CONFIRM_READING_FITS_V0
  - dependency: Releasability and the record
    type: Capability contracts
    disposition: REUSE
    evidence: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0
  - dependency: The record trail
    type: Store
    disposition: REUSE
    evidence: The user prompt records, appended per request
  - dependency: The three hosted acts, their gates and the host
    type: Workflows, intents, actor
    disposition: AUTHOR_NEW
    evidence: Nothing takes candidates from outside
  - dependency: Opening, reading, choosing and recording a hosted response
    type: Capability contracts and transforms
    disposition: AUTHOR_NEW
    evidence: Nothing forms the hosted state or chooses a token
  impact_analysis:
  - artifact: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    impact_scope: Reused unchanged by a second act
    consumer_count: '2'
    evidence: si.topology.impact impacted_count 2
  - artifact: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    impact_scope: Reused unchanged by a second act
    consumer_count: '3'
    evidence: si.topology.impact impacted_count 3
  - artifact: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    impact_scope: Reused unchanged by a second act
    consumer_count: '4'
    evidence: si.topology.impact impacted_count 4
  - artifact: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    impact_scope: Reused unchanged by a second act
    consumer_count: '5'
    evidence: si.topology.impact impacted_count 5
  - artifact: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    impact_scope: Reused unchanged by the hosted acts
    consumer_count: '8'
    evidence: si.topology.impact impacted_count 8
  - artifact: causal_language_model::CC_RECORD_USER_PROMPT_V0
    impact_scope: Reused unchanged by the hosted acts
    consumer_count: '9'
    evidence: si.topology.impact impacted_count 9
  - artifact: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    impact_scope: Reused unchanged when a hosted record opens
    consumer_count: '8'
    evidence: si.topology.impact impacted_count 8
  - artifact: causal_language_model::CC_CONFIRM_READING_FITS_V0
    impact_scope: Reused unchanged when a hosted request is admitted
    consumer_count: '6'
    evidence: si.topology.impact impacted_count 6
  authoring_decisions:
  - capability: Begin a hosted request
    decision: AUTHOR_NEW
    rationale: An act admits the request as the test model's way does, checks the reported reading size, and opens the record.
    alternatives_checked: 'Extending the test model''s act was rejected: it must stay unchanged.'
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
  - capability: Confirm a hosted reading fits
    decision: AUTHOR_NEW
    rationale: The count the host reports with an offer is compared with the registered capacity before any token is chosen.
    alternatives_checked: 'Counting words alone was rejected by the author: capacity is in tokens. A separate reporting act was rejected by the author.'
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
  - capability: Open the record of a hosted request
    decision: AUTHOR_NEW
    rationale: The opening entry holds the rules in force, the permitted length, the fingerprint and what the model reads.
    alternatives_checked: 'A separate store for the response in progress was rejected: the trail already is its state, and a second copy could disagree with it.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Read the state of a hosted request
    decision: AUTHOR_NEW
    rationale: The trail is read and reduced to the response as built, its position, and whether it is open.
    alternatives_checked: Holding the state in a record updated in place was rejected for the same reason.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - capability: Choose a permitted token
    decision: AUTHOR_NEW
    rationale: The test model's stopping and choosing, with tokens joined as they are and the permitted length enforced.
    alternatives_checked: 'Changing the word transform was rejected: the test model''s way stays unchanged.'
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
  - capability: Offer the next candidates
    decision: AUTHOR_NEW
    rationale: An act confirms the request open and the fingerprint the admitted model's, chooses, records the step, and refuses when the rules or the length stop the response.
    alternatives_checked: 'A host choosing and reporting was rejected: the business chooses.'
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - capability: Release a hosted response
    decision: AUTHOR_NEW
    rationale: An act confirms the response complete and not stopped, and closes the record with the text the business chose.
    alternatives_checked: 'Accepting the text from the host was rejected: the host never supplies what is released.'
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
  - capability: Record a hosted request
    decision: REUSE
    rationale: The existing record closes a hosted request exactly as it records the test model's.
    alternatives_checked: Nothing further needed.
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  placement_decision:
  - decision: EXTEND
    subdomain: model_response
    rationale: The hosted way answers the same requests under the same rules into the same record. Nothing moves and no other subdomain changes.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
  saturation:
  - criterion: No unresolved CRITICAL gaps
    status: SATISFIED
    evidence: The CRITICAL gap resolves to the three hosted acts
  - criterion: No open analyst questions
    status: SATISFIED
    evidence: All eight findings are CLOSED; the author answered Gate 0
  - criterion: No dependency expansion in the last pass
    status: SATISFIED
    evidence: A second pass found the record trail as the state; a third found nothing further
  - criterion: Verification pass complete, no OVERTURNED item unresolved
    status: SATISFIED
    evidence: All eight items re-grounded and CONFIRMED
  - criterion: Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason
    status: SATISFIED
    evidence: Every finding is OBSERVED
```

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: how a host outside the business proposes, while the
business alone chooses, records and releases.

---

## 1. Analysis Findings

## 2. Verification Results

## 3. Dependency Discoveries

## 4. Impact Analysis

## 5. Authoring Decisions

## 6. Placement Decision

## 7. Saturation Assessment
