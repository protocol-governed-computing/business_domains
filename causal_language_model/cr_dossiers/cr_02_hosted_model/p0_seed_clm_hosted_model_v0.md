# Change Seed — causal_language_model / model_response

**Stage:** 0 — Change Seed
**CR:** cr_02_hosted_model
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Model Response subdomain governs how a business's language model responds to a customer's
question about the customer's own accounts, under rules that apply while the model writes and with
a record of every answer and refusal. This change lets a pretrained model the business runs on its
own machine, Qwen3 8B, answer under the same rules and record-keeping as the test model. The model's
host asks the model for candidate tokens and passes them to the business; the business chooses what
may be written, records every offer and choice, and alone releases a response. The test model's
existing way of answering stays as it is.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| model_response | EXTEND_SUBDOMAIN | The subdomain exists and answers through a test model. This change adds a second way of answering, through a hosted model, beside the existing one, which stays unchanged. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| Hosted Model | A pretrained language model the business runs on its own machine, which it did not build or train. The first is Qwen3 8B, with its thinking mode turned off. |
| Host | The program that loads a hosted model, asks it what it could write next, and passes its candidates to the business. It holds no authority. |
| Token | A small piece of text a model generates, one at a time. |
| Candidate | A token the model could write next, with a score for how likely the model considers it. |
| Offer | The set of candidates the host passes to the business at one step, naming the fingerprint of the model it is claimed to come from. |
| Step | One round of an offer and the business's choice from it. |
| Hosted Request | A request, on behalf of a customer, answered by a hosted model. |
| Fingerprint | The fingerprint the host gives the stored form of a hosted model. It is the host's claim, not independent proof of the model's origin or training. |
| Reading Capacity | How many tokens the model can read in one request. |
| Maximum Response Length | The most tokens a response may have. |
| Reported Reading Size | The host's report of how many tokens the model would need to read for a request. |
| Response Rules | The rules in force for a model's time in service while it writes: prohibited words and patterns, the degree of freedom in choosing, the longest response, and whether numbers must come from what the model read. |
| Grounded Number | A number whose digits, ignoring the separators between them, are the digits of a number the model read. |
| Release | Handing a completed response to the requester from the business's own record. |
| Test Model | The scripted model that deliberately tries to break the rules. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| A hosted model answers customers only under the response rules in force for its time in service. |
| A time in service can require that every number a hosted model writes is one it read. |
| The business, not the host, decides which candidate is written at every step. |
| Only a completed response held in the business's own record is released, and only by the business. |
| Every hosted request is recorded, with the candidates offered and the choice made at every step. |
| An authorized requester can submit a request on behalf of a customer to a hosted model in service. |
| The test model's existing way of answering keeps working unchanged, and the test model can also answer through the hosted way. |
| Every business operation is traceable and auditable. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The business answers customers' questions about their own accounts using a language model that must follow rules while it writes. | HIGH |
| Every answer or refusal must be recorded. | HIGH |
| The first version used a test model that deliberately tried to break the rules. | HIGH |
| The business now wants to use Qwen3 8B, a pretrained model that runs on its own machine. | HIGH |
| The business did not build or train Qwen3 8B. | HIGH |
| A program called the host loads the model and asks it to generate a response. | HIGH |
| A pretrained model can produce an answer when it has not been given the information needed, such as a made-up account balance. | HIGH |
| The business must not release an answer simply because the model produced it. | HIGH |
| The host may request text from the model but cannot decide which text is permitted or send an answer to a customer. | HIGH |
| Every response is governed by the rules in force for the model at the time of the request. | HIGH |
| The model generates a response one token at a time. | HIGH |
| At each step the model provides a set of candidate tokens, each with a score of how likely it considers that token. | HIGH |
| The host passes the candidates to the business, which applies the response rules and chooses an allowed candidate. | HIGH |
| The host gives the business's choice back to the model, which uses it to generate the next set of candidates. | HIGH |
| The process continues until the response is complete or the business must refuse it. | HIGH |
| The business records the candidates offered at each step and the candidate it chose. | HIGH |
| The host cannot override the business's choice. | HIGH |
| The business releases only the completed response held in its own record, after the response has passed the required controls. | HIGH |
| The business cannot inspect the model's internal computations and cannot prove that the model produced the candidates the host reports. | HIGH |
| The business records which model was in service, which response rules applied, what candidates were offered at each step, which it selected, and what response, if any, it released. | HIGH |
| The business does not claim that a model's answer is true, or that the candidates came from the model as the host claims. | HIGH |
| A hosted model must be registered before it can be used. | HIGH |
| A hosted model's registration includes a description and a fingerprint supplied by the host. | HIGH |
| The fingerprint identifies the stored model as the host reports it, and is not independent proof of the model's origin or training. | HIGH |
| A hosted model's description states its reading capacity and its maximum response length, both in tokens. | HIGH |
| Each offer identifies the fingerprint of the model it is claimed to come from. | HIGH |
| An offer whose fingerprint does not match the model selected for the request is refused. | HIGH |
| Qwen3 8B, running with its thinking mode turned off, is the first hosted model, registered with the fingerprint its host supplies. | HIGH |
| The test model's response rules apply to the hosted model. | HIGH |
| Prohibited words or patterns are prevented from appearing in the response, including patterns split across several tokens. | HIGH |
| The configured degree of freedom decides the choice among permitted candidates. | HIGH |
| A hosted response's length is counted in tokens. | HIGH |
| A hosted response may be no longer than the smaller of the model's registered maximum and the longest response in the response rules. | HIGH |
| If every candidate offered at a step is forbidden, the request is refused and the record names the rule that prevented further progress. | HIGH |
| A response that reaches its maximum permitted length before it is complete is not released. | HIGH |
| A hosted request is admitted under the same conditions as a request to the test model. | HIGH |
| The host reports how many tokens the model would need to read, and the business records that report. | HIGH |
| The host learns what the model reads when the request is admitted, and reports the count with its first offer. | HIGH |
| A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written. | HIGH |
| Every request is recorded, whether answered or refused. | HIGH |
| The record of a hosted request opens when the request is admitted and closes when the response is released or refused. | HIGH |
| A response the host stops offering for stays open in the record, visibly not released. | HIGH |
| Any caller that names the request and the fingerprint of the model in service may offer candidates. | HIGH |
| The test model's existing way of answering remains unchanged. | HIGH |
| The test model must also be usable through the hosted way. | HIGH |
| Every business operation must be traceable and auditable. | HIGH |
| A time in service may require that every number in a hosted response is one the model read. | HIGH |
| When a time in service requires grounded numbers, the model may not begin a number that no number in the reading begins, nor end one that is not a number in the reading. | HIGH |
| Numbers match on their digits, so a number may be reformatted but its value not changed. | HIGH |
| Numbers written as words, and claims that are not numbers, are not judged for grounding. | HIGH |
| A grounded number is not thereby true, and the business does not claim it is. | HIGH |
| A time in service that does not ask for grounding behaves as before. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| The model_response subdomain already admits a request, forms the response rules in force, and records every request. | The hosted way reuses them; if they are not there as believed, this change must build them. | Confirm the composition holds the admission, rule-forming and recording capabilities the test model's way uses. |
| The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates. | The hosted way needs the host to offer candidates step by step; if something already does, it is reused. | Confirm nothing in the composition accepts candidates from outside and returns a choice. |
| A registered model's description can carry its reading capacity and its maximum response length. | The hosted model's limits are part of its description. | Confirm what a registration's description holds and how its reading capacity is used. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| The test model's existing way of answering must not change. | Business policy |
| The host cannot decide which text is permitted, override a choice, or send text to a customer. | Business policy |
| Only a completed response held in the business's record, which passed the controls, is released. | Business policy |
| The business must not claim a response is true, or that the candidates came from the model. | Business policy |
| Every business operation must leave a record that can be traced and audited. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| No token is written that a response rule forbids, including a pattern split across several tokens. |
| No token is written except one the business chose from what was offered. |
| No hosted response is released that is not complete. |
| No hosted response is released that is longer than its permitted length. |
| No offer is accepted for a model other than the one the request was admitted for. |
| Every hosted request is recorded from its admission, with every offer and choice. |
| Only the business releases a response. |
| Where a time in service requires grounded numbers, no number is written that is not one the model read. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Hosted Request | Writing | Admitted; the host offers and the business chooses, step by step. |
| Hosted Request | Complete | The response is complete and awaits release. |
| Hosted Request | Released | The business released the completed response. |
| Hosted Request | Refused | The request yielded no response; the record carries the reason. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| User Prompt Responded | When the business releases a completed hosted response. | A response is released, and its record shows every offer and choice it was built from. |
| User Prompt Refused | When a hosted request yields no response. | The refusal and its reason are recorded. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Hosted request record | Model Response |
| The choice of token at each step | Model Response |
| Release of a response | Model Response |
| The candidates offered | The host, as a claim the business records |
| The reported reading size | The host, as a claim the business records |
| The fingerprint of a hosted model | The host, as a claim the business records |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Proving that a candidate offer came from the model | The business cannot inspect the model; it records the host's claim. |
| Replacing a model while it is in service | A later change. |
| Reviewing a completed response through a separate review process | A later change. |
| Governing or verifying what the host does before it presents candidates | The host is outside the business's governance; only what it offers is judged. |
| Authenticating the host | Declared out of scope; the host holds no authority. |
| Changing the test model's existing way of answering | It stays as it is. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| model_response | EXTENDED |
| substitution | ADJACENT |
| disclosure | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| An authorized requester can submit a request on behalf of a customer to a hosted model in service, and the request is admitted under the same conditions as a request to the test model. |
| A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written, and the record says so. |
| At each step the business chooses a permitted candidate from the offer, and the record keeps the offer and the choice. |
| A prohibited pattern split across several tokens is not written. |
| An offer naming a fingerprint other than the model's the request was admitted for is refused. |
| When every candidate at a step is forbidden, the request is refused, and the record names the rule. |
| A response that reaches its permitted length before it is complete is not released, and the record says so. |
| A completed response is released by the business from its own record, and the released text is exactly what the business chose. |
| Where its time in service requires grounded numbers, a hosted response contains no number the model did not read, and one it read may be reformatted but not changed. |
| A response the host stops offering for stays open in the record and is never released. |
| Every hosted request, released, refused or abandoned, has a record from its admission. |
| The test model's existing way of answering behaves exactly as before. |
| The test model can answer through the hosted way, under the same rules. |
| Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way. |
| Every business operation performed can be traced and audited afterwards. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Hosted Request | The request's own identity. | Their identities match. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Hosted Request | — | Writing | An authorized requester's request is admitted. | The record opens. |
| Hosted Request | Writing | Writing | The business chooses a permitted candidate from an offer. | The offer and the choice are recorded. |
| Hosted Request | Writing | Complete | The business chooses the end of the response. | None. |
| Hosted Request | Complete | Released | The host asks for release, and the response passed the controls. | The record closes with the released response. |
| Hosted Request | Writing | Refused | Every candidate is forbidden, or the response reaches its permitted length before it is complete. | The record closes with the reason. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Offer candidates | The reported reading size exceeds the model's reading capacity. | The model cannot read it. |
| Offer candidates | The offer names a fingerprint other than the model's the request was admitted for. | No offer is accepted for another model. |
| Offer candidates | The request is not being written. | Only a request being written takes offers. |
| Offer candidates | Every candidate is forbidden. | The model cannot continue without breaking a rule. |
| Offer candidates | The response reaches its permitted length before it is complete. | An unfinished response is not released. |
| Release a response | The response is not complete. | Only a completed response is released. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Authenticating the host | A later change | Not decided within this change. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
