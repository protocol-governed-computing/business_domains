# Stage 2 — Domain Model Verification: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p2
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Model
    description: A registered model, with its description, fingerprint, state and open time in service.
    store_model: One record per model, updated in place.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 22}
  - entity: Time in Service
    description: A period a model is in service, with its ceiling, system prompt and response rules.
    store_model: One record per time in service.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 10}
  - entity: User Prompt Record
    description: The record kept of every request, answered or refused, including what the model read and the rules in force.
    store_model: Entries appended to a trail per request, never rewritten.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 40}
  - entity: Hosted Request
    description: A request answered by a hosted model, step by step.
    store_model: None yet.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 41}
  - entity: Offer
    description: The candidates the host passes at one step, naming the model's fingerprint.
    store_model: None yet.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 26}
  entity_attributes:
  - entity: Model
    attribute: Description
    meaning: How the model is built. It is held as the registration states it; its reading capacity is read at admission.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Model
    attribute: Fingerprint
    meaning: The fingerprint the registration carries, recorded and not verified.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - entity: Time in Service
    attribute: Response rules
    meaning: Prohibited words and patterns, the degree of freedom, and the longest response.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: User Prompt Record
    attribute: Outcome
    meaning: Whether the request was answered or refused, with the reason.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - entity: Offer
    attribute: Candidates
    meaning: The tokens the model could write next, each with its score.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, row: 12}
  business_processes:
  - process: Submit a user prompt to the test model
    initiator: Authorized requester
    outcome: The request is admitted or refused; the test model writes under the rules within one act; the response is released or refused, and recorded.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - process: Answer through a hosted model
    initiator: Authorized requester, then the host
    outcome: 'Not yet possible: nothing takes candidates from outside.'
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  process_steps:
  - process: Submit a user prompt to the test model
    step: '1'
    action: Claim the request's identity and confirm the requester acts for the customer.
    record_produced: None, or a refusal record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - process: Submit a user prompt to the test model
    step: '2'
    action: Confirm the model is registered and in service, and the kind of information within its ceiling.
    record_produced: None, or a refusal record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - process: Submit a user prompt to the test model
    step: '3'
    action: Assemble what the model reads and confirm it fits.
    record_produced: None, or a refusal record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - process: Submit a user prompt to the test model
    step: '4'
    action: Form the rules in force and write the response word by word under them.
    record_produced: None.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - process: Submit a user prompt to the test model
    step: '5'
    action: Release the response or refuse it.
    record_produced: The user prompt record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  belief_verification:
  - belief: The model_response subdomain already admits a request, forms the response rules in force, and records every request.
    result: VERIFIED
    evidence: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0 and causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 admit a request; causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 forms the rules in force; causal_language_model::CC_RECORD_USER_PROMPT_V0 appends the record to a trail per request, and causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 returns every entry in it.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates.
    result: VERIFIED
    evidence: causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 runs the writing molecule causal_language_model::CT_WRITE_RESPONSE_V0 inside causal_language_model::WF_SUBMIT_USER_PROMPT_V0; the offer is the test model's own step, causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0. No intent takes candidates.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - belief: A registered model's description can carry its reading capacity and its maximum response length.
    result: VERIFIED
    evidence: causal_language_model::CC_REGISTER_MODEL_V0 takes the description as a whole object and records it as stated; admission reads `description.reading_capacity`. Nothing reads a maximum response length from it today.
    source_finding: {phase: p1, register: system_beliefs, row: 3}
  pps_baseline_fqdns:
  - capability: Claim a request's identity
    fqdn: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    what_it_does: Refuses a request already made.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Confirm the requester acts for the customer
    fqdn: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    what_it_does: Refuses a requester not permitted for the customer.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Admit a request to a model
    fqdn: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    what_it_does: Refuses a model not registered or not in service, and returns the model record.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Confirm the ceiling
    fqdn: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    what_it_does: Refuses a request above the model's ceiling, and returns the time in service.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Assemble what the model reads
    fqdn: causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0
    what_it_does: Returns exactly what the model reads, counting it in words.
    fit: PARTIAL
    cannot_do: It counts words; a hosted model's capacity is in tokens, counted by the host.
  - capability: Form the rules in force
    fqdn: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    what_it_does: Forms the forbidden patterns, the account rule, the freedom and the seed, and the positions up to the longest response.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Choose a permitted word
    fqdn: causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0
    what_it_does: Stops forbidden words and chooses a permitted one, joining words by a space.
    fit: PARTIAL
    cannot_do: Tokens carry their own spacing and are joined as they are.
  - capability: Confirm a response releasable
    fqdn: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    what_it_does: Refuses a response a rule stopped, or one not finished.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Record a request
    fqdn: causal_language_model::CC_RECORD_USER_PROMPT_V0
    what_it_does: Appends the user prompt record.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Retrieve a request's record
    fqdn: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0
    what_it_does: Returns every entry recorded for a request.
    fit: EXACT
    cannot_do: Nothing.
  - capability: Submit to the test model
    fqdn: causal_language_model::WF_SUBMIT_USER_PROMPT_V0
    what_it_does: Answers a request through the test model in one act.
    fit: EXACT
    cannot_do: Unchanged by this change.
  gaps:
  - gap: Nothing lets a host offer candidates and receive the business's choice.
    severity: CRITICAL
    impact: A hosted model cannot answer under the rules at all.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Nothing records a request from its admission, with every offer and choice.
    severity: MAJOR
    impact: An abandoned hosted request would leave no record.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - gap: Nothing releases a response separately from writing it.
    severity: MAJOR
    impact: The host would have to be trusted to finish the response.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Nothing measures reading in tokens or limits a response by the model's registered maximum.
    severity: MINOR
    impact: A hosted model's limits would not be enforced.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 3}
  - gap: Nothing requires the numbers in a response to be ones the model read.
    severity: MAJOR
    impact: A hosted model could write a balance or an account number it made up.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  architectural_observations:
  - observation: A request's record is a trail of entries, and retrieval returns all of them.
    evidence: causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 reads every entry for the request. A record that opens at admission and closes later fits it without change.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 10}
  - observation: An act runs once, start to end; nothing loops across acts.
    evidence: Workflows are acyclic; the test model's loop is inside one molecule. A hosted response is therefore one act per step, driven by the host.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 11}
  discovery_concerns:
  - concern: The test model's way of answering must stay unchanged.
    evidence: causal_language_model::WF_SUBMIT_USER_PROMPT_V0 and its contracts are reused or left alone, never redeclared.
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: pps_baseline_fqdns, row: 11}
  open_questions: null
```

Every belief the change request declared is resolved against the pinned composition. What is
verified here is what the test model's way of answering already provides — admission, the rules in
force, the record — and what nothing yet provides: a way for anyone outside to offer candidates and
receive the business's choice.

---

## 1. Business Entities

## 2. Business Processes

## 3. Belief Verification — THE SPINE

## 4. PPS Baseline — What Already Exists

## 5. Gap Analysis — What Is Missing

## 6. Architectural Observations

## 7. Discovery Concerns

## 8. Open Questions
