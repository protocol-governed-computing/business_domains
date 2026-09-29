# Stage 1 — Change Request: Clarification & Fact Capture: causal_language_model / model_response
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_02_hosted_model
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|---------|-------------------------------------------------------------------|---------|--------------|
| model_response | EXTEND_SUBDOMAIN | The subdomain exists and answers through a test model. This change adds a second way of answering, through a hosted model, beside the existing one, which stays unchanged. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| Hosted Model | A pretrained language model the business runs on its own machine, which it did not build or train. The first is Qwen3 8B, with its thinking mode turned off. | CR seed §2 Business Vocabulary #1 |
| Host | The program that loads a hosted model, asks it what it could write next, and passes its candidates to the business. It holds no authority. | CR seed §2 Business Vocabulary #2 |
| Token | A small piece of text a model generates, one at a time. | CR seed §2 Business Vocabulary #3 |
| Candidate | A token the model could write next, with a score for how likely the model considers it. | CR seed §2 Business Vocabulary #4 |
| Offer | The set of candidates the host passes to the business at one step, naming the fingerprint of the model it is claimed to come from. | CR seed §2 Business Vocabulary #5 |
| Step | One round of an offer and the business's choice from it. | CR seed §2 Business Vocabulary #6 |
| Hosted Request | A request, on behalf of a customer, answered by a hosted model. | CR seed §2 Business Vocabulary #7 |
| Fingerprint | The fingerprint the host gives the stored form of a hosted model. It is the host's claim, not independent proof of the model's origin or training. | CR seed §2 Business Vocabulary #8 |
| Reading Capacity | How many tokens the model can read in one request. | CR seed §2 Business Vocabulary #9 |
| Maximum Response Length | The most tokens a response may have. | CR seed §2 Business Vocabulary #10 |
| Reported Reading Size | The host's report of how many tokens the model would need to read for a request. | CR seed §2 Business Vocabulary #11 |
| Response Rules | The rules in force for a model's time in service while it writes: prohibited words and patterns, the degree of freedom in choosing, the longest response, and whether numbers must come from what the model read. | CR seed §2 Business Vocabulary #12 |
| Grounded Number | A number whose digits, ignoring the separators between them, are the digits of a number the model read. | CR seed §2 Business Vocabulary #13 |
| Release | Handing a completed response to the requester from the business's own record. | CR seed §2 Business Vocabulary #14 |
| Test Model | The scripted model that deliberately tries to break the rules. | CR seed §2 Business Vocabulary #15 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A hosted model answers customers only under the response rules in force for its time in service. | CR seed §3 Requested Outcomes #1 |
| A time in service can require that every number a hosted model writes is one it read. | CR seed §3 Requested Outcomes #2 |
| The business, not the host, decides which candidate is written at every step. | CR seed §3 Requested Outcomes #3 |
| Only a completed response held in the business's own record is released, and only by the business. | CR seed §3 Requested Outcomes #4 |
| Every hosted request is recorded, with the candidates offered and the choice made at every step. | CR seed §3 Requested Outcomes #5 |
| An authorized requester can submit a request on behalf of a customer to a hosted model in service. | CR seed §3 Requested Outcomes #6 |
| The test model's existing way of answering keeps working unchanged, and the test model can also answer through the hosted way. | CR seed §3 Requested Outcomes #7 |
| Every business operation is traceable and auditable. | CR seed §3 Requested Outcomes #8 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The business answers customers' questions about their own accounts using a language model that must follow rules while it writes. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| Every answer or refusal must be recorded. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The first version used a test model that deliberately tried to break the rules. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| The business now wants to use Qwen3 8B, a pretrained model that runs on its own machine. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| The business did not build or train Qwen3 8B. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A program called the host loads the model and asks it to generate a response. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| A pretrained model can produce an answer when it has not been given the information needed, such as a made-up account balance. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| The business must not release an answer simply because the model produced it. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| The host may request text from the model but cannot decide which text is permitted or send an answer to a customer. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| Every response is governed by the rules in force for the model at the time of the request. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| The model generates a response one token at a time. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| At each step the model provides a set of candidate tokens, each with a score of how likely it considers that token. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| The host passes the candidates to the business, which applies the response rules and chooses an allowed candidate. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| The host gives the business's choice back to the model, which uses it to generate the next set of candidates. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| The process continues until the response is complete or the business must refuse it. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| The business records the candidates offered at each step and the candidate it chose. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| The host cannot override the business's choice. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The business releases only the completed response held in its own record, after the response has passed the required controls. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| The business cannot inspect the model's internal computations and cannot prove that the model produced the candidates the host reports. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| The business records which model was in service, which response rules applied, what candidates were offered at each step, which it selected, and what response, if any, it released. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| The business does not claim that a model's answer is true, or that the candidates came from the model as the host claims. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| A hosted model must be registered before it can be used. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| A hosted model's registration includes a description and a fingerprint supplied by the host. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| The fingerprint identifies the stored model as the host reports it, and is not independent proof of the model's origin or training. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| A hosted model's description states its reading capacity and its maximum response length, both in tokens. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| Each offer identifies the fingerprint of the model it is claimed to come from. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| An offer whose fingerprint does not match the model selected for the request is refused. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| Qwen3 8B, running with its thinking mode turned off, is the first hosted model, registered with the fingerprint its host supplies. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| The test model's response rules apply to the hosted model. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| Prohibited words or patterns are prevented from appearing in the response, including patterns split across several tokens. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| The configured degree of freedom decides the choice among permitted candidates. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| A hosted response's length is counted in tokens. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| A hosted response may be no longer than the smaller of the model's registered maximum and the longest response in the response rules. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| If every candidate offered at a step is forbidden, the request is refused and the record names the rule that prevented further progress. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| A response that reaches its maximum permitted length before it is complete is not released. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| A hosted request is admitted under the same conditions as a request to the test model. | HIGH | CR seed §4 Known Facts — Business Truths #36 |
| The host reports how many tokens the model would need to read, and the business records that report. | HIGH | CR seed §4 Known Facts — Business Truths #37 |
| The host learns what the model reads when the request is admitted, and reports the count with its first offer. | HIGH | CR seed §4 Known Facts — Business Truths #38 |
| A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written. | HIGH | CR seed §4 Known Facts — Business Truths #39 |
| Every request is recorded, whether answered or refused. | HIGH | CR seed §4 Known Facts — Business Truths #40 |
| The record of a hosted request opens when the request is admitted and closes when the response is released or refused. | HIGH | CR seed §4 Known Facts — Business Truths #41 |
| A response the host stops offering for stays open in the record, visibly not released. | HIGH | CR seed §4 Known Facts — Business Truths #42 |
| Any caller that names the request and the fingerprint of the model in service may offer candidates. | HIGH | CR seed §4 Known Facts — Business Truths #43 |
| The test model's existing way of answering remains unchanged. | HIGH | CR seed §4 Known Facts — Business Truths #44 |
| The test model must also be usable through the hosted way. | HIGH | CR seed §4 Known Facts — Business Truths #45 |
| Every business operation must be traceable and auditable. | HIGH | CR seed §4 Known Facts — Business Truths #46 |
| A time in service may require that every number in a hosted response is one the model read. | HIGH | CR seed §4 Known Facts — Business Truths #47 |
| When a time in service requires grounded numbers, the model may not begin a number that no number in the reading begins, nor end one that is not a number in the reading. | HIGH | CR seed §4 Known Facts — Business Truths #48 |
| Numbers match on their digits, so a number may be reformatted but its value not changed. | HIGH | CR seed §4 Known Facts — Business Truths #49 |
| Numbers written as words, and claims that are not numbers, are not judged for grounding. | HIGH | CR seed §4 Known Facts — Business Truths #50 |
| A grounded number is not thereby true, and the business does not claim it is. | HIGH | CR seed §4 Known Facts — Business Truths #51 |
| A time in service that does not ask for grounding behaves as before. | HIGH | CR seed §4 Known Facts — Business Truths #52 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The model_response subdomain already admits a request, forms the response rules in force, and records every request. | The hosted way reuses them; if they are not there as believed, this change must build them. | Confirm the composition holds the admission, rule-forming and recording capabilities the test model's way uses. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates. | The hosted way needs the host to offer candidates step by step; if something already does, it is reused. | Confirm nothing in the composition accepts candidates from outside and returns a choice. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| A registered model's description can carry its reading capacity and its maximum response length. | The hosted model's limits are part of its description. | Confirm what a registration's description holds and how its reading capacity is used. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| The test model's existing way of answering must not change. | Business policy | CR seed §7 Constraints #1 |
| The host cannot decide which text is permitted, override a choice, or send text to a customer. | Business policy | CR seed §7 Constraints #2 |
| Only a completed response held in the business's record, which passed the controls, is released. | Business policy | CR seed §7 Constraints #3 |
| The business must not claim a response is true, or that the candidates came from the model. | Business policy | CR seed §7 Constraints #4 |
| Every business operation must leave a record that can be traced and audited. | Business policy | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| No token is written that a response rule forbids, including a pattern split across several tokens. | CR seed §8 Business Invariants #1 |
| No token is written except one the business chose from what was offered. | CR seed §8 Business Invariants #2 |
| No hosted response is released that is not complete. | CR seed §8 Business Invariants #3 |
| No hosted response is released that is longer than its permitted length. | CR seed §8 Business Invariants #4 |
| No offer is accepted for a model other than the one the request was admitted for. | CR seed §8 Business Invariants #5 |
| Every hosted request is recorded from its admission, with every offer and choice. | CR seed §8 Business Invariants #6 |
| Only the business releases a response. | CR seed §8 Business Invariants #7 |
| Where a time in service requires grounded numbers, no number is written that is not one the model read. | CR seed §8 Business Invariants #8 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Hosted Request | Writing | Admitted; the host offers and the business chooses, step by step. | CR seed §9 Lifecycle States #1 |
| Hosted Request | Complete | The response is complete and awaits release. | CR seed §9 Lifecycle States #2 |
| Hosted Request | Released | The business released the completed response. | CR seed §9 Lifecycle States #3 |
| Hosted Request | Refused | The request yielded no response; the record carries the reason. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| User Prompt Responded | When the business releases a completed hosted response. | A response is released, and its record shows every offer and choice it was built from. | CR seed §10 Business Events #1 |
| User Prompt Refused | When a hosted request yields no response. | The refusal and its reason are recorded. | CR seed §10 Business Events #2 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Hosted request record | Model Response | CR seed §11 Authority Boundaries #1 |
| The choice of token at each step | Model Response | CR seed §11 Authority Boundaries #2 |
| Release of a response | Model Response | CR seed §11 Authority Boundaries #3 |
| The candidates offered | The host, as a claim the business records | CR seed §11 Authority Boundaries #4 |
| The reported reading size | The host, as a claim the business records | CR seed §11 Authority Boundaries #5 |
| The fingerprint of a hosted model | The host, as a claim the business records | CR seed §11 Authority Boundaries #6 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Proving that a candidate offer came from the model | The business cannot inspect the model; it records the host's claim. | CR seed §12 Out of Scope #1 |
| Replacing a model while it is in service | A later change. | CR seed §12 Out of Scope #2 |
| Reviewing a completed response through a separate review process | A later change. | CR seed §12 Out of Scope #3 |
| Governing or verifying what the host does before it presents candidates | The host is outside the business's governance; only what it offers is judged. | CR seed §12 Out of Scope #4 |
| Authenticating the host | Declared out of scope; the host holds no authority. | CR seed §12 Out of Scope #5 |
| Changing the test model's existing way of answering | It stays as it is. | CR seed §12 Out of Scope #6 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| model_response | EXTENDED | CR seed §13 Governance Scope #1 |
| substitution | ADJACENT | CR seed §13 Governance Scope #2 |
| disclosure | ADJACENT | CR seed §13 Governance Scope #3 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| An authorized requester can submit a request on behalf of a customer to a hosted model in service, and the request is admitted under the same conditions as a request to the test model. | CR seed §15 Acceptance Criteria #1 |
| A hosted request whose reported reading size exceeds the model's reading capacity is refused before any token is chosen or written, and the record says so. | CR seed §15 Acceptance Criteria #2 |
| At each step the business chooses a permitted candidate from the offer, and the record keeps the offer and the choice. | CR seed §15 Acceptance Criteria #3 |
| A prohibited pattern split across several tokens is not written. | CR seed §15 Acceptance Criteria #4 |
| An offer naming a fingerprint other than the model's the request was admitted for is refused. | CR seed §15 Acceptance Criteria #5 |
| When every candidate at a step is forbidden, the request is refused, and the record names the rule. | CR seed §15 Acceptance Criteria #6 |
| A response that reaches its permitted length before it is complete is not released, and the record says so. | CR seed §15 Acceptance Criteria #7 |
| A completed response is released by the business from its own record, and the released text is exactly what the business chose. | CR seed §15 Acceptance Criteria #8 |
| Where its time in service requires grounded numbers, a hosted response contains no number the model did not read, and one it read may be reformatted but not changed. | CR seed §15 Acceptance Criteria #9 |
| A response the host stops offering for stays open in the record and is never released. | CR seed §15 Acceptance Criteria #10 |
| Every hosted request, released, refused or abandoned, has a record from its admission. | CR seed §15 Acceptance Criteria #11 |
| The test model's existing way of answering behaves exactly as before. | CR seed §15 Acceptance Criteria #12 |
| The test model can answer through the hosted way, under the same rules. | CR seed §15 Acceptance Criteria #13 |
| Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way. | CR seed §15 Acceptance Criteria #14 |
| Every business operation performed can be traced and audited afterwards. | CR seed §15 Acceptance Criteria #15 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Hosted Request | The request's own identity. | Their identities match. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Hosted Request | — | Writing | An authorized requester's request is admitted. | The record opens. | CR seed §17 Lifecycle Transitions #1 |
| Hosted Request | Writing | Writing | The business chooses a permitted candidate from an offer. | The offer and the choice are recorded. | CR seed §17 Lifecycle Transitions #2 |
| Hosted Request | Writing | Complete | The business chooses the end of the response. | None. | CR seed §17 Lifecycle Transitions #3 |
| Hosted Request | Complete | Released | The host asks for release, and the response passed the controls. | The record closes with the released response. | CR seed §17 Lifecycle Transitions #4 |
| Hosted Request | Writing | Refused | Every candidate is forbidden, or the response reaches its permitted length before it is complete. | The record closes with the reason. | CR seed §17 Lifecycle Transitions #5 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Offer candidates | The reported reading size exceeds the model's reading capacity. | The model cannot read it. | CR seed §18 Operation Refusals #1 |
| Offer candidates | The offer names a fingerprint other than the model's the request was admitted for. | No offer is accepted for another model. | CR seed §18 Operation Refusals #2 |
| Offer candidates | The request is not being written. | Only a request being written takes offers. | CR seed §18 Operation Refusals #3 |
| Offer candidates | Every candidate is forbidden. | The model cannot continue without breaking a rule. | CR seed §18 Operation Refusals #4 |
| Offer candidates | The response reaches its permitted length before it is complete. | An unfinished response is not released. | CR seed §18 Operation Refusals #5 |
| Release a response | The response is not complete. | Only a completed response is released. | CR seed §18 Operation Refusals #6 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Authenticating the host | A later change | Not decided within this change. | CR seed §19 Authority Deferrals #1 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
