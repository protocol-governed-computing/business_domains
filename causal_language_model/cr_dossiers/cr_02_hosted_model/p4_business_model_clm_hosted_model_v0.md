# Stage 4 — Business Model: causal_language_model / model_response

**Stage:** 4 — Business Model

**CR:** cr_02_hosted_model

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized Requester | Submits a request on behalf of a customer to a hosted model in service. | Business role | S2 business_processes #2 |
| Host | Offers the candidates a hosted model could write next, and asks for release. Holds no authority. | External party | S3 analysis_findings Q7 |
| Model Response | Admits, chooses, records and releases. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Hosted Request | A request answered step by step by a hosted model. | Its record trail: an opening entry, a step entry per offer, and a closing entry. | S3 analysis_findings Q4 |
| Offer | The candidates passed at one step, naming the model's fingerprint. | Kept in the step entry with the choice made from it. | S3 analysis_findings Q7 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| The user prompt records | The trail every request is recorded in, per request. | S3 dependency_discoveries The record trail |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| User Prompt Responded | The business releases a completed hosted response. | The hosted request is released. | S1 business_events #1 |
| User Prompt Refused | A hosted request yields no response. | The hosted request is refused. | S1 business_events #2 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Authorized Requester | begins | a hosted request | Begin a hosted request | S3 authoring_decisions Begin a hosted request |
| Host | offers | the next candidates | Offer the next candidates | S3 authoring_decisions Offer the next candidates |
| Host | asks to release | a completed response | Release a hosted response | S3 authoring_decisions Release a hosted response |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Begin a hosted request | S3 authoring_decisions Begin a hosted request | CRITICAL | GAP-01 | Admits as the test model's way does. |
| Confirm a hosted reading fits | S3 authoring_decisions Confirm a hosted reading fits | CRITICAL | GAP-02 | The reported size against the capacity. |
| Open the record of a hosted request | S3 authoring_decisions Open the record of a hosted request | CRITICAL | GAP-03 | The trail is the state. |
| Read the state of a hosted request | S3 authoring_decisions Read the state of a hosted request | CRITICAL | GAP-04 | Reduced from the trail. |
| Choose a permitted token | S3 authoring_decisions Choose a permitted token | CRITICAL | GAP-05 | The test model's rules, on tokens. |
| Offer the next candidates | S3 authoring_decisions Offer the next candidates | CRITICAL | GAP-06 | One act per step. |
| Release a hosted response | S3 authoring_decisions Release a hosted response | CRITICAL | GAP-07 | Only the business releases. |
| Record a hosted request | S3 authoring_decisions Record a hosted request | SATISFIED | — | The existing record closes it. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| model_response | causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0 | reused contract | SATISFIED | S3 dependency_discoveries Admission |
| model_response | causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | reused contract | SATISFIED | S3 dependency_discoveries Admission |
| model_response | causal_language_model::CC_ADMIT_USER_PROMPT_V0 | reused contract | SATISFIED | S3 dependency_discoveries Admission |
| model_response | causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0 | reused contract | SATISFIED | S3 dependency_discoveries Admission |
| model_response | causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0 | reused transform | SATISFIED | S3 dependency_discoveries Forming the rules in force |
| model_response | causal_language_model::CC_CONFIRM_READING_FITS_V0 | reused contract | SATISFIED | S3 dependency_discoveries Assembling what the model reads |
| model_response | causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0 | reused contract | SATISFIED | S3 dependency_discoveries Releasability and the record |
| model_response | causal_language_model::CC_RECORD_USER_PROMPT_V0 | reused contract | SATISFIED | S3 dependency_discoveries Releasability and the record |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | The test model's existing way of answering must not change. | S1 constraints #1 | The business author |
| 2 | The host cannot decide which text is permitted, override a choice, or send text to a customer. | S1 constraints #2 | The business author |
| 3 | Only a completed response held in the business's record, which passed the controls, is released. | S1 constraints #3 | The business author |
| 4 | The business must not claim a response is true, or that the candidates came from the model. | S1 constraints #4 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Begin a hosted request | Begin a hosted request | model_response | AUTHOR_NEW |
| GAP-02 | S3 authoring_decisions Confirm a hosted reading fits | Confirm a hosted reading fits | model_response | AUTHOR_NEW |
| GAP-03 | S3 authoring_decisions Open the record of a hosted request | Open the record of a hosted request | model_response | AUTHOR_NEW |
| GAP-04 | S3 authoring_decisions Read the state of a hosted request | Read the state of a hosted request | model_response | AUTHOR_NEW |
| GAP-05 | S3 authoring_decisions Choose a permitted token | Choose a permitted token | model_response | AUTHOR_NEW |
| GAP-06 | S3 authoring_decisions Offer the next candidates | Offer the next candidates | model_response | AUTHOR_NEW |
| GAP-07 | S3 authoring_decisions Release a hosted response | Release a hosted response | model_response | AUTHOR_NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | A hosted response is written one act per step, driven by the host; the business never calls the host. | S3 analysis_findings Q1 | Acts are acyclic, and the host holds no authority. | The host offers and asks; it never chooses or releases. |
| 2 | A hosted request is admitted by the test model's four admission contracts, unchanged. | S3 analysis_findings Q2 | The same conditions admit both ways. | No admission contract is redeclared. |
| 3 | Admission assembles the reading as for the test model; the host reports its token count with each offer, compared with the capacity before choosing. | S3 analysis_findings Q3 | Capacity is in tokens, counted by the host once it has the reading. | The count is the host's claim, recorded with the step. |
| 4 | The record trail is the hosted request's state: an opening entry, a step entry per offer, a closing entry. | S3 analysis_findings Q4 | One truth; an abandoned request stays visibly open. | No store holds a second copy of the state. |
| 5 | A token is chosen by the test model's rules, joined as it is. | S3 analysis_findings Q5 | A pattern split across tokens is judged on the text as built. | The word transform is unchanged. |
| 6 | The permitted length is the smaller of the registered maximum and the rules' longest response. | S3 analysis_findings Q6 | The author answered. | A step past it refuses the request as unfinished. |
| 7 | An offer for another model's fingerprint refuses the request; the host is not authenticated. | S3 analysis_findings Q7 | The author answered. | The fingerprint is compared at every step. |
| 8 | Release closes the record with the text the business chose. | S3 analysis_findings Q8 | The host never supplies what is released. | Release refuses a response not complete, or stopped. |
| 9 | Grounding is a response rule of the time in service, carried into the opening entry and applied by the token choice. | S3 analysis_findings Q9 | The author set it per time in service; the stored rules already carry it. | Unset, it is off; no existing artifact changes. |
| 10 | The choice judges the compatibility form of the text, and does not begin a forbidden number the model read. | S3 analysis_findings Q10 | A rule judged only on completion lets a beginning through. | A number the model did not read is judged when it is complete, unless grounding refuses it first. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Begin a hosted request | GAP-01 |
| Confirm a hosted reading fits | GAP-02 |
| Open the record of a hosted request | GAP-03 |
| Read the state of a hosted request | GAP-04 |
| Choose a permitted token | GAP-05 |
| Offer the next candidates | GAP-06 |
| Release a hosted response | GAP-07 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Authenticate the host | Out of scope by the author's answer. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
