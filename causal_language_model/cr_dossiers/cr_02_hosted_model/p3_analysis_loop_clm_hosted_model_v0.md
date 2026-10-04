# Stage 3 — Analysis Loop: causal_language_model / model_response

**Stage:** 3 — Analysis Loop

**CR:** cr_02_hosted_model

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: how a host outside the business proposes, while the
business alone chooses, records and releases.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | An act runs once from start to end, and nothing loops across acts. A hosted response is therefore written one act per step: the host offers, the act chooses and records, and the host asks again. The business never calls the host. | Three acts: begin a hosted request, offer candidates, release the response. The host drives them; it holds no authority in any of them. | OBSERVED | HIGH | CLOSED | Workflows are acyclic; causal_language_model::WF_SUBMIT_USER_PROMPT_V0 writes inside one molecule |
| Q2 | Beginning a hosted request is admitted by the same checks as the test model's way: the request's identity, the requester for the customer, the model registered and in service, and the ceiling. | Those four contracts are reused unchanged, in the same order. | OBSERVED | HIGH | CLOSED | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 |
| Q3 | A hosted model's reading capacity is in tokens, counted by the host, which learns what the model reads only at admission. Admission assembles the reading exactly as for the test model, whose word count can only undercount tokens; the host reports its token count with each offer, and the business compares it with the registered capacity before choosing. | Admission reuses the test model's reading check unchanged; a new check on the offer compares the reported count with the capacity. | OBSERVED | HIGH | CLOSED | causal_language_model::CT_PURE_ASSEMBLE_MODEL_READING_V0 counts words; the author answered that capacity is in tokens and the host reports the count |
| Q4 | A request's record is a trail of entries per request, and retrieval returns all of them. The record of a hosted request can therefore open at admission, take one entry per step, and close on release or refusal, with no new store. The trail itself is the state of the response: its opening entry holds the rules, the limits and the fingerprint, and its steps hold what was chosen. | An opening entry, a step entry per offer, and the existing record as the closing entry, all in the existing trail. An abandoned request is an open trail, visible to retrieval as it stands. | OBSERVED | HIGH | CLOSED | causal_language_model::CC_RETRIEVE_USER_PROMPT_RECORD_V0 reads every entry for the request; the author answered that the record opens at admission |
| Q5 | The rules' choice for a token is the test model's choice with one difference: tokens carry their own spacing and are joined as they are, so a pattern split across tokens is judged on the text as built. The end of a response is a marker the host passes as a candidate. | A new transform chooses a permitted token by the same stopping and choosing as the word transform; the word transform is left unchanged. | OBSERVED | HIGH | CLOSED | causal_language_model::CT_PURE_CHOOSE_PERMITTED_WORD_V0 joins by a space |
| Q6 | The permitted length of a hosted response is the smaller of the model's registered maximum and the longest response in the rules. | The limit is formed from both when the record opens, and a step past it is refused as unfinished. | OBSERVED | HIGH | CLOSED | The author answered the smaller of the two |
| Q7 | An offer names a fingerprint, and the business holds the admitted model's. An offer for another model refuses the request. Any caller naming the request and the fingerprint may offer; authenticating the host is out of scope. | The fingerprint is compared at every step; there is no host authorization check. | OBSERVED | HIGH | CLOSED | The author answered that the host holds no authority |
| Q8 | Release reads the trail, confirms the response complete and not stopped, and closes the record with the response as the business chose it. The host never supplies the text it asks to release. | Release reuses the releasability and recording contracts. | OBSERVED | HIGH | CLOSED | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0 |
| Q9 | A time in service's response rules are stored as placed, and admission forms from them only the rules the test model uses. A rule that numbers come from the reading can therefore be set at placement, carried into the opening entry beside the rules in force, and applied only by the token choice. A number is judged on its digits, the separators between them ignored: it is not begun unless a number the model read begins with those digits, and not ended unless it is one. | Grounding is carried from the stored rules into the opening entry and applied by the new choice transform; the rule-forming transform and the test model's way are unchanged, and a time in service that does not set it behaves as before. | OBSERVED | HIGH | CLOSED | causal_language_model::CC_PLACE_MODEL_IN_SERVICE_V0 stores the response rules as given; causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 forms only the forbidden patterns, the freedom and the seed |
| Q10 | A pattern judged only when it is complete lets its beginning through: a model asked for a number it read and must not write can write all but its last digit, one token at a time, and then a lookalike character in place of the last. | The choice judges text in its compatibility form, so a lookalike is the character it looks like, and does not let the model begin a number it read that a rule forbids unless the digits could still become a permitted number it read. | OBSERVED | HIGH | CLOSED | Qwen3 8B, asked for a spouse's account number it read, wrote seven of its eight digits and then a subscript one |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The model_response subdomain already admits a request, forms the response rules in force, and records every request. | S2 belief_verification #1 | CONFIRMED | Resolved in Q2 and Q4 |
| The test model's way of answering chooses each word inside a single act, with no way for anyone outside to offer candidates. | S2 belief_verification #2 | CONFIRMED | Resolved in Q1 and Q5 |
| A registered model's description can carry its reading capacity and its maximum response length. | S2 belief_verification #3 | CONFIRMED | Resolved in Q3 and Q6 |
| Nothing lets a host offer candidates and receive the business's choice. | S2 gaps #1 | CONFIRMED | Resolved in Q1, Q5 and Q7 |
| Nothing records a request from its admission, with every offer and choice. | S2 gaps #2 | CONFIRMED | Resolved in Q4 |
| Nothing releases a response separately from writing it. | S2 gaps #3 | CONFIRMED | Resolved in Q8 |
| Nothing measures reading in tokens or limits a response by the model's registered maximum. | S2 gaps #4 | CONFIRMED | Resolved in Q3 and Q6 |
| The test model's way of answering must stay unchanged. | S2 discovery_concerns #1 | CONFIRMED | No artifact of it is redeclared |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Admission | Capability contracts | REUSE | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0, causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0, causal_language_model::CC_ADMIT_USER_PROMPT_V0, causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 |
| Forming the rules in force | Domain transform | REUSE | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 |
| Assembling what the model reads | Capability contract | REUSE | causal_language_model::CC_CONFIRM_READING_FITS_V0 |
| Releasability and the record | Capability contracts | REUSE | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0, causal_language_model::CC_RECORD_USER_PROMPT_V0 |
| The record trail | Store | REUSE | The user prompt records, appended per request |
| The three hosted acts, their gates and the host | Workflows, intents, actor | AUTHOR_NEW | Nothing takes candidates from outside |
| Opening, reading, choosing and recording a hosted response | Capability contracts and transforms | AUTHOR_NEW | Nothing forms the hosted state or chooses a token |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | Reused unchanged by a second act | 2 | si.topology.impact impacted_count 2 |
| causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | Reused unchanged by a second act | 3 | si.topology.impact impacted_count 3 |
| causal_language_model::CC_ADMIT_USER_PROMPT_V0 | Reused unchanged by a second act | 4 | si.topology.impact impacted_count 4 |
| causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | Reused unchanged by a second act | 5 | si.topology.impact impacted_count 5 |
| causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | Reused unchanged by the hosted acts | 8 | si.topology.impact impacted_count 8 |
| causal_language_model::CC_RECORD_USER_PROMPT_V0 | Reused unchanged by the hosted acts | 9 | si.topology.impact impacted_count 9 |
| causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | Reused unchanged when a hosted record opens | 8 | si.topology.impact impacted_count 8 |
| causal_language_model::CC_CONFIRM_READING_FITS_V0 | Reused unchanged when a hosted request is admitted | 6 | si.topology.impact impacted_count 6 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Begin a hosted request | AUTHOR_NEW | An act admits the request as the test model's way does, checks the reported reading size, and opens the record. | Extending the test model's act was rejected: it must stay unchanged. | S3 analysis_findings Q2 |
| Confirm a hosted reading fits | AUTHOR_NEW | The count the host reports with an offer is compared with the registered capacity before any token is chosen. | Counting words alone was rejected by the author: capacity is in tokens. A separate reporting act was rejected by the author. | S3 analysis_findings Q3 |
| Open the record of a hosted request | AUTHOR_NEW | The opening entry holds the rules in force, the permitted length, the fingerprint and what the model reads. | A separate store for the response in progress was rejected: the trail already is its state, and a second copy could disagree with it. | S3 analysis_findings Q4 |
| Read the state of a hosted request | AUTHOR_NEW | The trail is read and reduced to the response as built, its position, and whether it is open. | Holding the state in a record updated in place was rejected for the same reason. | S3 analysis_findings Q4 |
| Choose a permitted token | AUTHOR_NEW | The test model's stopping and choosing, with tokens joined as they are and the permitted length enforced. | Changing the word transform was rejected: the test model's way stays unchanged. | S3 analysis_findings Q5 |
| Offer the next candidates | AUTHOR_NEW | An act confirms the request open and the fingerprint the admitted model's, chooses, records the step, and refuses when the rules or the length stop the response. | A host choosing and reporting was rejected: the business chooses. | S3 analysis_findings Q7 |
| Release a hosted response | AUTHOR_NEW | An act confirms the response complete and not stopped, and closes the record with the text the business chose. | Accepting the text from the host was rejected: the host never supplies what is released. | S3 analysis_findings Q8 |
| Record a hosted request | REUSE | The existing record closes a hosted request exactly as it records the test model's. | Nothing further needed. | S3 analysis_findings Q4 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | model_response | The hosted way answers the same requests under the same rules into the same record. Nothing moves and no other subdomain changes. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The CRITICAL gap resolves to the three hosted acts |
| No open analyst questions | SATISFIED | All eight findings are CLOSED; the author answered Gate 0 |
| No dependency expansion in the last pass | SATISFIED | A second pass found the record trail as the state; a third found nothing further |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All eight items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED |
