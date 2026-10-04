# Stage 5 — Business Intent: causal_language_model / model_response

**Stage:** 5 — Business Intent

**CR:** cr_02_hosted_model

**Status:** DRAFT

**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Model Response subdomain governs how a business's language model responds to a customer's
question about the customer's own accounts, under rules that apply while the model writes and with
a record of every answer and refusal. This change lets a pretrained model the business runs on its
own machine, Qwen3 8B, answer under the same rules and record-keeping as the test model. The model's
host asks the model for candidate tokens and passes them to the business; the business chooses what
may be written, records every offer and choice, and alone releases a response. The test model's
existing way of answering stays as it is.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | INHERITED | |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| model_response | Governs model responses under rules applied while the model writes, now through a hosted model as well as the test model. | S4 bm_entities Hosted Request |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Begin a hosted request | IN_SCOPE | Admitted as the test model's way admits. | S4 authoring_scope GAP-01 |
| Confirm a hosted reading fits | IN_SCOPE | The reported size against the capacity. | S4 authoring_scope GAP-02 |
| Open the record of a hosted request | IN_SCOPE | The opening entry of the trail. | S4 authoring_scope GAP-03 |
| Read the state of a hosted request | IN_SCOPE | Reduced from the trail. | S4 authoring_scope GAP-04 |
| Choose a permitted token | IN_SCOPE | The test model's rules, on tokens. | S4 authoring_scope GAP-05 |
| Offer the next candidates | IN_SCOPE | One act per step. | S4 authoring_scope GAP-06 |
| Release a hosted response | IN_SCOPE | Only the business releases. | S4 authoring_scope GAP-07 |
| Authenticate the host | DEFERRED | Out of scope by the author's answer. | S4 authoring_scope Authenticate the host |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| NONE IDENTIFIED | | | |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| NONE IDENTIFIED | | | | | |

---

## 5. Invariants

<!-- register:invariants business_language -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| No token is written that a response rule forbids, including a pattern split across several tokens. | The rules apply while the model writes. | S1 business_invariants #1 |
| No token is written except one the business chose from what was offered. | The host cannot override the choice. | S1 business_invariants #2 |
| No hosted response is released that is not complete. | An unfinished response is not released. | S1 business_invariants #3 |
| No hosted response is released that is longer than its permitted length. | The limits are in force. | S1 business_invariants #4 |
| No offer is accepted for a model other than the one the request was admitted for. | The record attributes every offer to the admitted model. | S1 business_invariants #5 |
| Every hosted request is recorded from its admission, with every offer and choice. | Every request is recorded, answered, refused or abandoned. | S1 business_invariants #6 |
| Only the business releases a response. | The host cannot send text to a customer. | S1 business_invariants #7 |

---

## 6. Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Begin | A hosted request | An authorized requester submits a request to a hosted model | IN_SCOPE | S4 capability_graph Begin a hosted request |
| Offer | The next candidates | The host passes what the model could write next | IN_SCOPE | S4 capability_graph Offer the next candidates |
| Release | A completed hosted response | The host asks for release | IN_SCOPE | S4 capability_graph Release a hosted response |

---

## 7. Provisional Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| model_response | AC_MODEL_HOST_V0 | AC | The host of a model in service, which proposes and holds no authority | S4 actors Host |
| model_response | IN_BEGIN_HOSTED_RESPONSE_V0 | IN | A request to a hosted model on behalf of a customer | S4 capability_graph Begin a hosted request |
| model_response | WF_BEGIN_HOSTED_RESPONSE_V0 | WF | Admitting a hosted request and opening its record, or refusing it | S4 capability_graph Begin a hosted request |
| model_response | IN_OFFER_NEXT_TOKENS_V0 | IN | The candidates a hosted model could write next, naming its fingerprint | S4 capability_graph Offer the next candidates |
| model_response | WF_OFFER_NEXT_TOKENS_V0 | WF | Choosing a permitted token from an offer and recording the step, or refusing the request | S4 capability_graph Offer the next candidates |
| model_response | IN_RELEASE_HOSTED_RESPONSE_V0 | IN | A request to release a completed hosted response | S4 capability_graph Release a hosted response |
| model_response | WF_RELEASE_HOSTED_RESPONSE_V0 | WF | Releasing a completed hosted response from the record | S4 capability_graph Release a hosted response |
| model_response | CC_CONFIRM_HOSTED_READING_FITS_V0 | CC | Refuse an offer whose reported reading size exceeds the model's capacity | S4 capability_graph Confirm a hosted reading fits |
| model_response | CC_OPEN_HOSTED_RECORD_V0 | CC | Form the rules in force and open the record of a hosted request | S4 capability_graph Open the record of a hosted request |
| model_response | CC_READ_HOSTED_STATE_V0 | CC | Read a hosted request's trail and reduce it to the response as built | S4 capability_graph Read the state of a hosted request |
| model_response | CC_CONFIRM_OFFER_FOR_MODEL_V0 | CC | Refuse an offer naming another model's fingerprint | S4 capability_graph Offer the next candidates |
| model_response | CC_CHOOSE_PERMITTED_TOKEN_V0 | CC | Choose a permitted token from an offer under the rules in force | S4 capability_graph Choose a permitted token |
| model_response | CC_RECORD_HOSTED_STEP_V0 | CC | Record an offer and the choice made from it in the request's trail | S4 capability_graph Choose a permitted token |
| model_response | CT_PURE_READ_HOSTED_STATE_V0 | CT | Reduce a hosted request's trail to its state | S4 capability_graph Read the state of a hosted request |
| model_response | CT_PURE_CHOOSE_PERMITTED_TOKEN_V0 | CT | Stop forbidden tokens and choose a permitted one | S4 capability_graph Choose a permitted token |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|-----------|------|----------------|
| NONE IDENTIFIED | | | |
