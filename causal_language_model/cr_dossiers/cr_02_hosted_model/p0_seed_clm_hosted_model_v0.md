# Change Seed — causal_language_model / model_response

## Machine

```yaml
document:
  phase: p0
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Model Response subdomain governs how a business's language model responds to a customer's
    question about the customer's own accounts, under rules that apply while the model writes and with
    a record of every answer and refusal. This change lets a pretrained model the business runs on its
    own machine, Qwen3 8B, answer under the same rules and record-keeping as the test model. The model's
    host asks the model for candidate tokens and passes them to the business; the business chooses what
    may be written, records every offer and choice, and alone releases a response. The test model's
    existing way of answering stays as it is.
  cr_type:
  - subdomain: model_response
    classification: EXTEND_SUBDOMAIN
    rationale: The subdomain exists and answers through a test model. This change adds a second way of answering, through a hosted model, beside the existing one, which stays unchanged.
  business_vocabulary:
  - term: Hosted Model
    definition: A pretrained language model the business runs on its own machine, which it did not build or train. The first is Qwen3 8B, with its thinking mode turned off.
  - term: Host
    definition: The program that loads a hosted model, asks it what it could write next, and passes its candidates to the business. It holds no authority.
  - term: Token
    definition: A small piece of text a model generates, one at a time.
  - term: Candidate
    definition: A token the model could write next, with a score for how likely the model considers it.
  - term: Offer
    definition: The set of candidates the host passes to the business at one step, naming the fingerprint of the model it is claimed to come from.
  - term: Step
    definition: One round of an offer and the business's choice from it.
  - term: Hosted Request
    definition: A request, on behalf of a customer, answered by a hosted model.
  - term: Fingerprint
    definition: The fingerprint the host gives the stored form of a hosted model. It is the host's claim, not independent proof of the model's origin or training.
  - term: Reading Capacity
    definition: How many tokens the model can read in one request.
  - term: Maximum Response Length
    definition: The most tokens a response may have.
  - term: Reported Reading Size
    definition: The host's report of how many tokens the model would need to read for a request.
  - term: Response Rules
    definition: 'The rules in force for a model''s time in service while it writes: prohibited words and patterns, the degree of freedom in choosing, the longest response, and whether numbers must come from what the model read.'
  - term: Grounded Number
    definition: A number whose digits, ignoring the separators between them, are the digits of a number the model read.
  - term: Release
    definition: Handing a completed response to the requester from the business's own record.
  - term: Test Model
    definition: The scripted model that deliberately tries to break the rules.
  requested_outcomes:
  - outcome: A hosted model answers customers only under the response rules in force for its time in service.
  - outcome: A time in service can require that every number a hosted model writes is one it read.
  - outcome: The business, not the host, decides which candidate is written at every step.
  - outcome: Only a completed response held in the business's own record is released, and only by the business.
  - outcome: Every hosted request is recorded, with the candidates offered and the choice made at every step.
  - outcome: An authorized requester can submit a request on behalf of a customer to a hosted model in service.
  - outcome: The test model's existing way of answering keeps working unchanged, and the test model can also answer through the hosted way.
  - outcome: Every business operation is traceable and auditable.
  known_facts:
  - fact: The business answers customers' questions about their own accounts using a language model that must follow rules while it writes.
    certainty: HIGH
  - fact: Every answer or refusal must be recorded.
    certainty: HIGH
  - fact: The first version used a test model that deliberately tried to break the rules.
    certainty: HIGH
  - fact: The business now wants to use Qwen3 8B, a pretrained model that runs on its own machine.
    certainty: HIGH
  - fact: The business did not build or train Qwen3 8B.
    certainty: HIGH
  - fact: A program called the host loads the model and asks it to generate a response.
    certainty: HIGH
  - fact: A pretrained model can produce an answer when it has not been given the information needed, such as a made-up account balance.
    certainty: HIGH
  - fact: The business must not release an answer simply because the model produced it.
    certainty: HIGH
  - fact: The host may request text from the model but cannot decide which text is permitted or send an answer to a customer.
    certainty: HIGH
  - fact: Every response is governed by the rules in force for the model at the time of the request.
    certainty: HIGH
  - fact: The model generates a response one token at a time.
    certainty: HIGH
  - fact: At each step the model provides a set of candidate tokens, each with a score of how likely it considers that token.
    certainty: HIGH
  - fact: The host passes the candidates to the business, which applies the response rules and chooses an allowed candidate.
    certainty: HIGH
  - fact: The host gives the business's choice back to the model, which uses it to generate the next set of candidates.
    certainty: HIGH
  - fact: The process continues until the response is complete or the business must refuse it.
    certainty: HIGH
  - fact: The business records the candidates offered at each step and the candidate it chose.
    certainty: HIGH
  - fact: The host cannot override the business's choice.
    certainty: HIGH
  - fact: The business releases only the completed response held in its own record, after the response has passed the required controls.
    certainty: HIGH
  - fact: The business cannot inspect the model's internal computations and cannot prove that the model produced the candidates the host reports.
    certainty: HIGH
  - fact: The business records which model was in service, which response rules applied, what candidates were offered at each step, which it selected, and what response, if any, it released.
    certainty: HIGH
  - fact: The business does not claim that a model's answer is true, or that the candidates came from the model as the host claims.
    certainty: HIGH
  - fact: A hosted model must be registered before it can be used.
    certainty: HIGH
  - fact: A hosted model's registration includes a description and a fingerprint supplied by the host.
    certainty: HIGH
  - fact: The fingerprint identifies the stored model as the host reports it, and is not independent proof of the model's origin or training.
    certainty: HIGH
  - fact: A hosted model's description states its reading capacity and its maximum response length, both in tokens.
    certainty: HIGH
  - fact: Each offer identifies the fingerprint of the model it is claimed to come from.
    certainty: HIGH
  - fact: An offer whose fingerprint does not match the model selected for the request is refused.
    certainty: HIGH
  - fact: Qwen3 8B, running with its thinking mode turned off, is the first hosted model, registered with the fingerprint its host supplies.
    certainty: HIGH
  - fact: The test model's response rules apply to the hosted model.
    certainty: HIGH
  - fact: Prohibited words or patterns are prevented from appearing in the response, including patterns split across several tokens.
    certainty: HIGH
  - fact: The configured degree of freedom decides the choice among permitted candidates.
    certainty: HIGH
  - fact: A hosted response's length is counted in tokens.
    certainty: HIGH
  - fact: A hosted response may be no longer than the smaller of the model's registered maximum and the longest response in the response rules.
    certainty: HIGH
  - fact: If every candidate offered at a step is forbidden, the request is refused and the record names the rule that prevented further progress.
    certainty: HIGH
  - fact: A response that reaches its maximum permitted length before it is complete is not released.
    certainty: HIGH
  - fact: A hosted request is admitted under the same conditions as a request to the test model.
    certainty: HIGH
  - fact: The host reports how many tokens the model would need to read, and the business records that report.
    certainty: HIGH
  - fact: The host learns what the model reads when the request is admitted, and reports the count with its first offer.
    certainty: HIGH
  - fact: A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written.
    certainty: HIGH
  - fact: Every request is recorded, whether answered or refused.
    certainty: HIGH
  - fact: The record of a hosted request opens when the request is admitted and closes when the response is released or refused.
    certainty: HIGH
  - fact: A response the host stops offering for stays open in the record, visibly not released.
    certainty: HIGH
  - fact: Any caller that names the request and the fingerprint of the model in service may offer candidates.
    certainty: HIGH
  - fact: The test model's existing way of answering remains unchanged.
    certainty: HIGH
  - fact: The test model must also be usable through the hosted way.
    certainty: HIGH
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
  - fact: A time in service may require that every number in a hosted response is one the model read.
    certainty: HIGH
  - fact: When a time in service requires grounded numbers, the model may not begin a number that no number in the reading begins, nor end one that is not a number in the reading.
    certainty: HIGH
  - fact: Numbers match on their digits, so a number may be reformatted but its value not changed.
    certainty: HIGH
  - fact: Numbers written as words, and claims that are not numbers, are not judged for grounding.
    certainty: HIGH
  - fact: A grounded number is not thereby true, and the business does not claim it is.
    certainty: HIGH
  - fact: A time in service that does not ask for grounding behaves as before.
    certainty: HIGH
  system_beliefs:
  - belief: The model_response subdomain already admits a request, forms the response rules in force, and records every request.
    why_it_matters: The hosted way reuses them; if they are not there as believed, this change must build them.
    verification_goal: Confirm the composition holds the admission, rule-forming and recording capabilities the test model's way uses.
  - belief: The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates.
    why_it_matters: The hosted way needs the host to offer candidates step by step; if something already does, it is reused.
    verification_goal: Confirm nothing in the composition accepts candidates from outside and returns a choice.
  - belief: A registered model's description can carry its reading capacity and its maximum response length.
    why_it_matters: The hosted model's limits are part of its description.
    verification_goal: Confirm what a registration's description holds and how its reading capacity is used.
  assumptions: null
  constraints:
  - constraint: The test model's existing way of answering must not change.
    source: Business policy
  - constraint: The host cannot decide which text is permitted, override a choice, or send text to a customer.
    source: Business policy
  - constraint: Only a completed response held in the business's record, which passed the controls, is released.
    source: Business policy
  - constraint: The business must not claim a response is true, or that the candidates came from the model.
    source: Business policy
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
  business_invariants:
  - invariant: No token is written that a response rule forbids, including a pattern split across several tokens.
  - invariant: No token is written except one the business chose from what was offered.
  - invariant: No hosted response is released that is not complete.
  - invariant: No hosted response is released that is longer than its permitted length.
  - invariant: No offer is accepted for a model other than the one the request was admitted for.
  - invariant: Every hosted request is recorded from its admission, with every offer and choice.
  - invariant: Only the business releases a response.
  - invariant: Where a time in service requires grounded numbers, no number is written that is not one the model read.
  lifecycle_states:
  - object: Hosted Request
    state: Writing
    meaning: Admitted; the host offers and the business chooses, step by step.
  - object: Hosted Request
    state: Complete
    meaning: The response is complete and awaits release.
  - object: Hosted Request
    state: Released
    meaning: The business released the completed response.
  - object: Hosted Request
    state: Refused
    meaning: The request yielded no response; the record carries the reason.
  business_events:
  - event: User Prompt Responded
    when_it_occurs: When the business releases a completed hosted response.
    significance: A response is released, and its record shows every offer and choice it was built from.
  - event: User Prompt Refused
    when_it_occurs: When a hosted request yields no response.
    significance: The refusal and its reason are recorded.
  authority_boundaries:
  - business_object: Hosted request record
    authoritative_owner: Model Response
  - business_object: The choice of token at each step
    authoritative_owner: Model Response
  - business_object: Release of a response
    authoritative_owner: Model Response
  - business_object: The candidates offered
    authoritative_owner: The host, as a claim the business records
  - business_object: The reported reading size
    authoritative_owner: The host, as a claim the business records
  - business_object: The fingerprint of a hosted model
    authoritative_owner: The host, as a claim the business records
  out_of_scope:
  - item: Proving that a candidate offer came from the model
    reason: The business cannot inspect the model; it records the host's claim.
  - item: Replacing a model while it is in service
    reason: A later change.
  - item: Reviewing a completed response through a separate review process
    reason: A later change.
  - item: Governing or verifying what the host does before it presents candidates
    reason: The host is outside the business's governance; only what it offers is judged.
  - item: Authenticating the host
    reason: Declared out of scope; the host holds no authority.
  - item: Changing the test model's existing way of answering
    reason: It stays as it is.
  governance_scope:
  - scope_item: model_response
    relationship: EXTENDED
  - scope_item: substitution
    relationship: ADJACENT
  - scope_item: disclosure
    relationship: ADJACENT
  clarification_requests: null
  acceptance_criteria:
  - criterion: An authorized requester can submit a request on behalf of a customer to a hosted model in service, and the request is admitted under the same conditions as a request to the test model.
  - criterion: A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written, and the record says so.
  - criterion: At each step the business chooses a permitted candidate from the offer, and the record keeps the offer and the choice.
  - criterion: A prohibited pattern split across several tokens is not written.
  - criterion: An offer naming a fingerprint other than the model's the request was admitted for is refused.
  - criterion: When every candidate at a step is forbidden, the request is refused, and the record names the rule.
  - criterion: A response that reaches its permitted length before it is complete is not released, and the record says so.
  - criterion: A completed response is released by the business from its own record, and the released text is exactly what the business chose.
  - criterion: Where its time in service requires grounded numbers, a hosted response contains no number the model did not read, and one it read may be reformatted but not changed.
  - criterion: A response the host stops offering for stays open in the record and is never released.
  - criterion: Every hosted request, released, refused or abandoned, has a record from its admission.
  - criterion: The test model's existing way of answering behaves exactly as before.
  - criterion: The test model can answer through the hosted way, under the same rules.
  - criterion: Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way.
  - criterion: Every business operation performed can be traced and audited afterwards.
  identity_and_sameness:
  - business_object: Hosted Request
    identified_by: The request's own identity.
    two_are_the_same_when: Their identities match.
  lifecycle_transitions:
  - object: Hosted Request
    from_state: null
    to_state: Writing
    triggered_by: An authorized requester's request is admitted.
    cascade: The record opens.
  - object: Hosted Request
    from_state: Writing
    to_state: Writing
    triggered_by: The business chooses a permitted candidate from an offer.
    cascade: The offer and the choice are recorded.
  - object: Hosted Request
    from_state: Writing
    to_state: Complete
    triggered_by: The business chooses the end of the response.
    cascade: None.
  - object: Hosted Request
    from_state: Complete
    to_state: Released
    triggered_by: The host asks for release, and the response passed the controls.
    cascade: The record closes with the released response.
  - object: Hosted Request
    from_state: Writing
    to_state: Refused
    triggered_by: Every candidate is forbidden, or the response reaches its permitted length before it is complete.
    cascade: The record closes with the reason.
  operation_refusals:
  - operation: Offer candidates
    refused_when: The reported reading size exceeds the model's reading capacity.
    business_reason: The model cannot read it.
  - operation: Offer candidates
    refused_when: The offer names a fingerprint other than the model's the request was admitted for.
    business_reason: No offer is accepted for another model.
  - operation: Offer candidates
    refused_when: The request is not being written.
    business_reason: Only a request being written takes offers.
  - operation: Offer candidates
    refused_when: Every candidate is forbidden.
    business_reason: The model cannot continue without breaking a rule.
  - operation: Offer candidates
    refused_when: The response reaches its permitted length before it is complete.
    business_reason: An unfinished response is not released.
  - operation: Release a response
    refused_when: The response is not complete.
    business_reason: Only a completed response is released.
  authority_deferrals:
  - business_object: Authenticating the host
    deferred_to: A later change
    until: Not decided within this change.
```

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

## 1. CR Type

## 2. Business Vocabulary

## 3. Requested Outcomes

## 4. Known Facts — Business Truths

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

## 6. Assumptions

## 7. Constraints

## 8. Business Invariants

## 9. Lifecycle States

## 10. Business Events

## 11. Authority Boundaries

## 12. Out of Scope

## 13. Governance Scope

## 14. Clarification Requests

## 15. Acceptance Criteria

## 16. Identity and Sameness

## 17. Lifecycle Transitions

## 18. Operation Refusals

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
