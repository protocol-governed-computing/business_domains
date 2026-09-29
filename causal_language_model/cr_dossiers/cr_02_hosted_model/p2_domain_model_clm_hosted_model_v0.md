# Stage 2 — Domain Model Verification: causal_language_model / model_response

**Stage:** 2 — Domain Model Verification
**CR:** cr_02_hosted_model
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. What is
verified here is what the test model's way of answering already provides — admission, the rules in
force, the record — and what nothing yet provides: a way for anyone outside to offer candidates and
receive the business's choice.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Model | A registered model, with its description, fingerprint, state and open time in service. | One record per model, updated in place. | OBSERVED | S1 known_facts #22 |
| Time in Service | A period a model is in service, with its ceiling, system prompt and response rules. | One record per time in service. | OBSERVED | S1 known_facts #10 |
| User Prompt Record | The record kept of every request, answered or refused, including what the model read and the rules in force. | Entries appended to a trail per request, never rewritten. | OBSERVED | S1 known_facts #40 |
| Hosted Request | A request answered by a hosted model, step by step. | None yet. | OBSERVED | S1 known_facts #41 |
| Offer | The candidates the host passes at one step, naming the model's fingerprint. | None yet. | OBSERVED | S1 known_facts #26 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Model | Description | How the model is built. It is held as the registration states it; its reading capacity is read at admission. | OBSERVED | S2 belief_verification #3 |
| Model | Fingerprint | The fingerprint the registration carries, recorded and not verified. | OBSERVED | S2 belief_verification #3 |
| Time in Service | Response rules | Prohibited words and patterns, the degree of freedom, and the longest response. | OBSERVED | S2 belief_verification #1 |
| User Prompt Record | Outcome | Whether the request was answered or refused, with the reason. | OBSERVED | S2 belief_verification #1 |
| Offer | Candidates | The tokens the model could write next, each with its score. | OBSERVED | S1 known_facts #12 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Submit a user prompt to the test model | Authorized requester | The request is admitted or refused; the test model writes under the rules within one act; the response is released or refused, and recorded. | OBSERVED | S2 belief_verification #2 |
| Answer through a hosted model | Authorized requester, then the host | Not yet possible: nothing takes candidates from outside. | OBSERVED | S2 belief_verification #2 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Submit a user prompt to the test model | 1 | Claim the request's identity and confirm the requester acts for the customer. | None, or a refusal record. | OBSERVED | S2 belief_verification #1 |
| Submit a user prompt to the test model | 2 | Confirm the model is registered and in service, and the kind of information within its ceiling. | None, or a refusal record. | OBSERVED | S2 belief_verification #1 |
| Submit a user prompt to the test model | 3 | Assemble what the model reads and confirm it fits. | None, or a refusal record. | OBSERVED | S2 belief_verification #1 |
| Submit a user prompt to the test model | 4 | Form the rules in force and write the response word by word under them. | None. | OBSERVED | S2 belief_verification #2 |
| Submit a user prompt to the test model | 5 | Release the response or refuse it. | The user prompt record. | OBSERVED | S2 belief_verification #1 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The model_response subdomain already admits a request, forms the response rules in force, and records every request. | VERIFIED | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0 and causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 admit a request; causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 forms the rules in force; causal_language_model::CC_RECORD_USER_PROMPT_V0 appends the record to a trail per request, and causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 returns every entry in it. | S1 system_beliefs #1 |
| The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates. | VERIFIED | causal_language_model::CC_WRITE_MODEL_RESPONSE_V0 runs the writing molecule causal_language_model::CT_WRITE_RESPONSE_V0 inside causal_language_model::WF_SUBMIT_USER_PROMPT_V0; the offer is the test model's own step, causal_language_model::CT_IMPURE_OFFER_NEXT_WORDS_V0. No intent takes candidates. | S1 system_beliefs #2 |
| A registered model's description can carry its reading capacity and its maximum response length. | VERIFIED | causal_language_model::CC_REGISTER_MODEL_V0 takes the description as a whole object and records it as stated; admission reads `description.reading_capacity`. Nothing reads a maximum response length from it today. | S1 system_beliefs #3 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Claim a request's identity | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | Refuses a request already made. | EXACT | Nothing. |
| Confirm the requester acts for the customer | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | Refuses a requester not permitted for the customer. | EXACT | Nothing. |
| Admit a request to a model | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | Refuses a model not registered or not in service, and returns the model record. | EXACT | Nothing. |
| Confirm the ceiling | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | Refuses a request above the model's ceiling, and returns the time in service. | EXACT | Nothing. |
| Assemble what the model reads | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 | Returns exactly what the model reads, counting it in words. | PARTIAL | It counts words; a hosted model's capacity is in tokens, counted by the host. |
| Form the rules in force | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | Forms the forbidden patterns, the account rule, the freedom and the seed, and the positions up to the longest response. | EXACT | Nothing. |
| Choose a permitted word | causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 | Stops forbidden words and chooses a permitted one, joining words by a space. | PARTIAL | Tokens carry their own spacing and are joined as they are. |
| Confirm a response releasable | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | Refuses a response a rule stopped, or one not finished. | EXACT | Nothing. |
| Record a request | causal_language_model::CC_RECORD_USER_PROMPT_V0 | Appends the user prompt record. | EXACT | Nothing. |
| Retrieve a request's record | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 | Returns every entry recorded for a request. | EXACT | Nothing. |
| Submit to the test model | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 | Answers a request through the test model in one act. | EXACT | Unchanged by this change. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing lets a host offer candidates and receive the business's choice. | CRITICAL | A hosted model cannot answer under the rules at all. | OBSERVED | S2 belief_verification #2 |
| Nothing records a request from its admission, with every offer and choice. | MAJOR | An abandoned hosted request would leave no record. | OBSERVED | S2 belief_verification #1 |
| Nothing releases a response separately from writing it. | MAJOR | The host would have to be trusted to finish the response. | OBSERVED | S2 belief_verification #2 |
| Nothing measures reading in tokens or limits a response by the model's registered maximum. | MINOR | A hosted model's limits would not be enforced. | OBSERVED | S2 belief_verification #3 |
| Nothing requires the numbers in a response to be ones the model read. | MAJOR | A hosted model could write a balance or an account number it made up. | OBSERVED | S2 belief_verification #1 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A request's record is a trail of entries, and retrieval returns all of them. | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 reads every entry for the request. A record that opens at admission and closes later fits it without change. | OBSERVED | S2 pps_baseline_fqdns #10 |
| An act runs once, start to end; nothing loops across acts. | Workflows are acyclic; the test model's loop is inside one molecule. A hosted response is therefore one act per step, driven by the host. | OBSERVED | S2 pps_baseline_fqdns #11 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The test model's way of answering must stay unchanged. | causal_language_model::WF_SUBMIT_USER_PROMPT_V0 and its contracts are reused or left alone, never redeclared. | MINOR | OBSERVED | S2 pps_baseline_fqdns #11 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
