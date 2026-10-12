# Stage 1 — Change Request: Clarification & Fact Capture: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p1
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: model_response
    classification: EXTEND_SUBDOMAIN
    rationale: The subdomain exists and answers through a test model. This change adds a second way of answering, through a hosted model, beside the existing one, which stays unchanged.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: Hosted Model
    definition: A pretrained language model the business runs on its own machine, which it did not build or train. The first is Qwen3 8B, with its thinking mode turned off.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Host
    definition: The program that loads a hosted model, asks it what it could write next, and passes its candidates to the business. It holds no authority.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Token
    definition: A small piece of text a model generates, one at a time.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Candidate
    definition: A token the model could write next, with a score for how likely the model considers it.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Offer
    definition: The set of candidates the host passes to the business at one step, naming the fingerprint of the model it is claimed to come from.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Step
    definition: One round of an offer and the business's choice from it.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Hosted Request
    definition: A request, on behalf of a customer, answered by a hosted model.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: Fingerprint
    definition: The fingerprint the host gives the stored form of a hosted model. It is the host's claim, not independent proof of the model's origin or training.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Reading Capacity
    definition: How many tokens the model can read in one request.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Maximum Response Length
    definition: The most tokens a response may have.
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Reported Reading Size
    definition: The host's report of how many tokens the model would need to read for a request.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: Response Rules
    definition: 'The rules in force for a model''s time in service while it writes: prohibited words and patterns, the degree of freedom in choosing, the longest response, and whether numbers must come from what the model read.'
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  - term: Grounded Number
    definition: A number whose digits, ignoring the separators between them, are the digits of a number the model read.
    source_finding: {phase: p0, register: business_vocabulary, row: 13}
  - term: Release
    definition: Handing a completed response to the requester from the business's own record.
    source_finding: {phase: p0, register: business_vocabulary, row: 14}
  - term: Test Model
    definition: The scripted model that deliberately tries to break the rules.
    source_finding: {phase: p0, register: business_vocabulary, row: 15}
  requested_outcomes:
  - outcome: A hosted model answers customers only under the response rules in force for its time in service.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: A time in service can require that every number a hosted model writes is one it read.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: The business, not the host, decides which candidate is written at every step.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Only a completed response held in the business's own record is released, and only by the business.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Every hosted request is recorded, with the candidates offered and the choice made at every step.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: An authorized requester can submit a request on behalf of a customer to a hosted model in service.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: The test model's existing way of answering keeps working unchanged, and the test model can also answer through the hosted way.
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  - outcome: Every business operation is traceable and auditable.
    source_finding: {phase: p0, register: requested_outcomes, row: 8}
  known_facts:
  - fact: The business answers customers' questions about their own accounts using a language model that must follow rules while it writes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: Every answer or refusal must be recorded.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The first version used a test model that deliberately tried to break the rules.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: The business now wants to use Qwen3 8B, a pretrained model that runs on its own machine.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: The business did not build or train Qwen3 8B.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: A program called the host loads the model and asks it to generate a response.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: A pretrained model can produce an answer when it has not been given the information needed, such as a made-up account balance.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: The business must not release an answer simply because the model produced it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: The host may request text from the model but cannot decide which text is permitted or send an answer to a customer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: Every response is governed by the rules in force for the model at the time of the request.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: The model generates a response one token at a time.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: At each step the model provides a set of candidate tokens, each with a score of how likely it considers that token.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: The host passes the candidates to the business, which applies the response rules and chooses an allowed candidate.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: The host gives the business's choice back to the model, which uses it to generate the next set of candidates.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: The process continues until the response is complete or the business must refuse it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: The business records the candidates offered at each step and the candidate it chose.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: The host cannot override the business's choice.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: The business releases only the completed response held in its own record, after the response has passed the required controls.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: The business cannot inspect the model's internal computations and cannot prove that the model produced the candidates the host reports.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: The business records which model was in service, which response rules applied, what candidates were offered at each step, which it selected, and what response, if any, it released.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: The business does not claim that a model's answer is true, or that the candidates came from the model as the host claims.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: A hosted model must be registered before it can be used.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: A hosted model's registration includes a description and a fingerprint supplied by the host.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: The fingerprint identifies the stored model as the host reports it, and is not independent proof of the model's origin or training.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: A hosted model's description states its reading capacity and its maximum response length, both in tokens.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: Each offer identifies the fingerprint of the model it is claimed to come from.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: An offer whose fingerprint does not match the model selected for the request is refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: Qwen3 8B, running with its thinking mode turned off, is the first hosted model, registered with the fingerprint its host supplies.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  - fact: The test model's response rules apply to the hosted model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 29}
  - fact: Prohibited words or patterns are prevented from appearing in the response, including patterns split across several tokens.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 30}
  - fact: The configured degree of freedom decides the choice among permitted candidates.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 31}
  - fact: A hosted response's length is counted in tokens.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 32}
  - fact: A hosted response may be no longer than the smaller of the model's registered maximum and the longest response in the response rules.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 33}
  - fact: If every candidate offered at a step is forbidden, the request is refused and the record names the rule that prevented further progress.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 34}
  - fact: A response that reaches its maximum permitted length before it is complete is not released.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 35}
  - fact: A hosted request is admitted under the same conditions as a request to the test model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 36}
  - fact: The host reports how many tokens the model would need to read, and the business records that report.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 37}
  - fact: The host learns what the model reads when the request is admitted, and reports the count with its first offer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 38}
  - fact: A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 39}
  - fact: Every request is recorded, whether answered or refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 40}
  - fact: The record of a hosted request opens when the request is admitted and closes when the response is released or refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 41}
  - fact: A response the host stops offering for stays open in the record, visibly not released.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 42}
  - fact: Any caller that names the request and the fingerprint of the model in service may offer candidates.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 43}
  - fact: The test model's existing way of answering remains unchanged.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 44}
  - fact: The test model must also be usable through the hosted way.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 45}
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 46}
  - fact: A time in service may require that every number in a hosted response is one the model read.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 47}
  - fact: When a time in service requires grounded numbers, the model may not begin a number that no number in the reading begins, nor end one that is not a number in the reading.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 48}
  - fact: Numbers match on their digits, so a number may be reformatted but its value not changed.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 49}
  - fact: Numbers written as words, and claims that are not numbers, are not judged for grounding.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 50}
  - fact: A grounded number is not thereby true, and the business does not claim it is.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 51}
  - fact: A time in service that does not ask for grounding behaves as before.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 52}
  system_beliefs:
  - belief: The model_response subdomain already admits a request, forms the response rules in force, and records every request.
    why_it_matters: The hosted way reuses them; if they are not there as believed, this change must build them.
    verification_goal: Confirm the composition holds the admission, rule-forming and recording capabilities the test model's way uses.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates.
    why_it_matters: The hosted way needs the host to offer candidates step by step; if something already does, it is reused.
    verification_goal: Confirm nothing in the composition accepts candidates from outside and returns a choice.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  - belief: A registered model's description can carry its reading capacity and its maximum response length.
    why_it_matters: The hosted model's limits are part of its description.
    verification_goal: Confirm what a registration's description holds and how its reading capacity is used.
    source_finding: {phase: p0, register: system_beliefs, row: 3}
  assumptions: null
  constraints:
  - constraint: The test model's existing way of answering must not change.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: The host cannot decide which text is permitted, override a choice, or send text to a customer.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Only a completed response held in the business's record, which passed the controls, is released.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: The business must not claim a response is true, or that the candidates came from the model.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 5}
  business_invariants:
  - invariant: No token is written that a response rule forbids, including a pattern split across several tokens.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No token is written except one the business chose from what was offered.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: No hosted response is released that is not complete.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: No hosted response is released that is longer than its permitted length.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: No offer is accepted for a model other than the one the request was admitted for.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: Every hosted request is recorded from its admission, with every offer and choice.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: Only the business releases a response.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: Where a time in service requires grounded numbers, no number is written that is not one the model read.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  lifecycle_states:
  - object: Hosted Request
    state: Writing
    meaning: Admitted; the host offers and the business chooses, step by step.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Hosted Request
    state: Complete
    meaning: The response is complete and awaits release.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: Hosted Request
    state: Released
    meaning: The business released the completed response.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: Hosted Request
    state: Refused
    meaning: The request yielded no response; the record carries the reason.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: User Prompt Responded
    when_it_occurs: When the business releases a completed hosted response.
    significance: A response is released, and its record shows every offer and choice it was built from.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: User Prompt Refused
    when_it_occurs: When a hosted request yields no response.
    significance: The refusal and its reason are recorded.
    source_finding: {phase: p0, register: business_events, row: 2}
  authority_boundaries:
  - business_object: Hosted request record
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: The choice of token at each step
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: Release of a response
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: The candidates offered
    authoritative_owner: The host, as a claim the business records
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  - business_object: The reported reading size
    authoritative_owner: The host, as a claim the business records
    source_finding: {phase: p0, register: authority_boundaries, row: 5}
  - business_object: The fingerprint of a hosted model
    authoritative_owner: The host, as a claim the business records
    source_finding: {phase: p0, register: authority_boundaries, row: 6}
  out_of_scope:
  - item: Proving that a candidate offer came from the model
    reason: The business cannot inspect the model; it records the host's claim.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Replacing a model while it is in service
    reason: A later change.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Reviewing a completed response through a separate review process
    reason: A later change.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Governing or verifying what the host does before it presents candidates
    reason: The host is outside the business's governance; only what it offers is judged.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Authenticating the host
    reason: Declared out of scope; the host holds no authority.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Changing the test model's existing way of answering
    reason: It stays as it is.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  governance_scope:
  - scope_item: model_response
    relationship: EXTENDED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: substitution
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: disclosure
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  clarification_requests: null
  acceptance_criteria:
  - criterion: An authorized requester can submit a request on behalf of a customer to a hosted model in service, and the request is admitted under the same conditions as a request to the test model.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written, and the record says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: At each step the business chooses a permitted candidate from the offer, and the record keeps the offer and the choice.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: A prohibited pattern split across several tokens is not written.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: An offer naming a fingerprint other than the model's the request was admitted for is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: When every candidate at a step is forbidden, the request is refused, and the record names the rule.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: A response that reaches its permitted length before it is complete is not released, and the record says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: A completed response is released by the business from its own record, and the released text is exactly what the business chose.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: Where its time in service requires grounded numbers, a hosted response contains no number the model did not read, and one it read may be reformatted but not changed.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: A response the host stops offering for stays open in the record and is never released.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: Every hosted request, released, refused or abandoned, has a record from its admission.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: The test model's existing way of answering behaves exactly as before.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: The test model can answer through the hosted way, under the same rules.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  - criterion: Every business operation performed can be traced and audited afterwards.
    source_finding: {phase: p0, register: acceptance_criteria, row: 15}
  identity_and_sameness:
  - business_object: Hosted Request
    identified_by: The request's own identity.
    two_are_the_same_when: Their identities match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Hosted Request
    from_state: null
    to_state: Writing
    triggered_by: An authorized requester's request is admitted.
    cascade: The record opens.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Hosted Request
    from_state: Writing
    to_state: Writing
    triggered_by: The business chooses a permitted candidate from an offer.
    cascade: The offer and the choice are recorded.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Hosted Request
    from_state: Writing
    to_state: Complete
    triggered_by: The business chooses the end of the response.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: Hosted Request
    from_state: Complete
    to_state: Released
    triggered_by: The host asks for release, and the response passed the controls.
    cascade: The record closes with the released response.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  - object: Hosted Request
    from_state: Writing
    to_state: Refused
    triggered_by: Every candidate is forbidden, or the response reaches its permitted length before it is complete.
    cascade: The record closes with the reason.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 5}
  operation_refusals:
  - operation: Offer candidates
    refused_when: The reported reading size exceeds the model's reading capacity.
    business_reason: The model cannot read it.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Offer candidates
    refused_when: The offer names a fingerprint other than the model's the request was admitted for.
    business_reason: No offer is accepted for another model.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Offer candidates
    refused_when: The request is not being written.
    business_reason: Only a request being written takes offers.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Offer candidates
    refused_when: Every candidate is forbidden.
    business_reason: The model cannot continue without breaking a rule.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Offer candidates
    refused_when: The response reaches its permitted length before it is complete.
    business_reason: An unfinished response is not released.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Release a response
    refused_when: The response is not complete.
    business_reason: Only a completed response is released.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  authority_deferrals:
  - business_object: Authenticating the host
    deferred_to: A later change
    until: Not decided within this change.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
