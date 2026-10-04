# Stage 5 — Business Intent: causal_language_model / model_response

**Stage:** 5 — Business Intent
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 6 — Governance Intent

---

## 1. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

Model response governs how a business's language model responds to a customer's question about the
customer's own accounts. It establishes the authority to say which model may respond, under which
rules, to whom: a model responds because staff registered it and placed it in service, and a word is
written because the rules in force permitted it. It manages a model from registration into service
and out again, applies the response rules to every word while the model writes rather than to the
finished response, and records every user prompt, whether responded to or refused, with exactly what
the model read and the rules it was under. It declares the single place where its results stop being
determined by their inputs: the model's own offer of next words. It exists because staff today paste
customers' questions into a model and copy its response back, and nobody can say afterwards which
model responded, what it was shown, or whether anything stopped it from writing what it should not.
It does not decide who may act for which customer, which staff are model staff, whether a response is
true, or what happens to a response after it is written.

<!-- register:purpose_provenance business_language=refinement -->
| Source | Disposition (INHERITED, REFINED) | Refinement |
|--------|----------------------------------|------------|
| CR seed §0 Subdomain Purpose | REFINED | States the authority the subdomain establishes — a model responds because staff placed it in service, and a word is written because the rules permitted it — the lifecycle it manages, the single declared place where determinism ends, and what it does not decide. |

<!-- register:subdomain_purposes business_language=purpose -->
| Subdomain | Purpose | Source Finding |
|-----------|---------|----------------|
| model_response | Governs which model may respond to a customer's question, under which rules, applying those rules to every word while the model writes, and records every user prompt with exactly what the model read and the outcome. | S4 design_decisions #1 |

---

## 2. Scope Boundary

<!-- register:scope_boundary business_language=capability,notes -->
| Capability | Status (IN_SCOPE, DEFERRED) | Notes | Source Finding |
|------------|-----------------------------|-------|----------------|
| Register a model | IN_SCOPE | Refused if the model is already registered | S4 authoring_scope GAP-13 |
| Place a model in service, and withdraw it | IN_SCOPE | Placement refused if the model is not registered or already in service; withdrawal refused if it is not in service | S4 authoring_scope GAP-14 |
| Submit a user prompt and release or refuse the model response | IN_SCOPE | Refused before the model sees it on four conditions, and while it writes on two | S4 authoring_scope GAP-15 |
| Retrieve a user prompt record | IN_SCOPE | Recorded in the operation trail; raises no business event | S4 authoring_scope GAP-16 |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | IN_SCOPE | Each pass runs two declared steps, the model's offer and the rules' choice | S4 authoring_scope GAP-08 |
| Offer the model's next words, with a result not determined by its inputs | IN_SCOPE | The single step declared as not deterministic | S4 authoring_scope GAP-06 |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | IN_SCOPE | Deterministic given the offered words, the rules and the seed | S4 authoring_scope GAP-07 |
| Run a composed body once per pass of a transform's loop | IN_SCOPE | Owned by the platform, which declares and runs it; reused | S4 authoring_scope GAP-09 |
| A test model that tries to write another customer's account number | IN_SCOPE | A permanent realization of the model's step | S4 authoring_scope GAP-10 |
| Retiring models | DEFERRED | Declared excluded from this release | S4 authoring_scope Retiring models |
| Reviewing a model response after it is written | DEFERRED | The disclosure function | S4 authoring_scope Disclosure |
| Letting a model propose actions | DEFERRED | The action function | S4 authoring_scope Action |
| Replacing the model in service | DEFERRED | The substitution function | S4 authoring_scope Substitution |
| Regulator reporting | DEFERRED | The reporting function | S4 authoring_scope Reporting |
| Catching a response made up from nothing | DEFERRED | Needs the finished response | S4 authoring_scope Catching a response made up from nothing |

---

## 3. Business Objects

<!-- register:business_objects optional business_language=store_name,business_rationale -->
| Store Name | Record Model (MUTABLE_STATE, APPEND_ONLY_JOURNAL, IDENTITY_REGISTRY, HYBRID) | Business Rationale | Source Finding |
|------------|------------------------------------------------------------------------------|--------------------|----------------|
| Model record | MUTABLE_STATE | The business holds one record per model, and a model moves into and out of service on the same record | S4 bm_entities Model |
| Model identity register | IDENTITY_REGISTRY | A second registration of the same model must be refused atomically | S4 design_decisions #8 |
| Time in service record | MUTABLE_STATE | A time in service is opened at placement and closed at withdrawal, on the same record | S4 bm_entities Time in Service |
| Time in service identity register | IDENTITY_REGISTRY | A time in service must never be opened twice under one identity, or a later placement would overwrite an earlier one | S4 bm_entities Time in Service |
| User prompt identity register | IDENTITY_REGISTRY | One user prompt identity must resolve to exactly one user prompt record | S4 bm_entities User Prompt Record |
| User prompt record | APPEND_ONLY_JOURNAL | Every user prompt is recorded with exactly what the model read and its outcome, and a record that could be amended would not be evidence | S4 bm_entities User Prompt Record |
| Operation trail | APPEND_ONLY_JOURNAL | Every operation must be traceable afterwards | S4 resources Operation trail |

---

## 4. Identity Semantics

<!-- register:identity_semantics business_language=identity_field,source,uniqueness_rule,cross_subdomain_relationship -->
| Store Name | Identity Field | Source | Uniqueness Rule | Cross-Subdomain Relationship | Source Finding |
|------------|----------------|--------|-----------------|------------------------------|----------------|
| Model record | Description and training fingerprint together | Supplied by model staff at registration; the fingerprint is the provider's claim | Two registrations whose descriptions and fingerprints both match describe the same model, and the second is refused | None | S1 identity_and_sameness #1 |
| Model identity register | The key formed from the description and fingerprint | Formed at registration | One entry per model; a second claim of the same key is refused | None | S4 design_decisions #8 |
| Time in service record | The model and the moment it was placed in service | Assigned at placement | At most one open time in service per model | Names exactly one model record | S1 business_invariants #3 |
| Time in service identity register | The time in service's identity | Claimed at placement, before the time in service is opened | One entry per time in service; a second claim of the same identity is refused | Names exactly one time in service record | S1 business_invariants #3 |
| User prompt identity register | The user prompt's identity | Named by the requester and claimed before anything else is done with the user prompt | One entry per user prompt; a second submission under the same identity is refused | Names exactly one user prompt record | S4 bm_entities User Prompt Record |
| User prompt record | The user prompt's identity | Claimed at submission | Each claimed user prompt appends at most one entry, and no entry is amended or removed | Names one model and one time in service | S4 bm_entities User Prompt Record |
| Operation trail | Append position | Assigned when the entry is appended | Each performed operation appends exactly one entry, and no entry is amended or removed | Names the staff member or requester who performed the operation | S4 resources Operation trail |

---

## 5. Business Invariants

<!-- register:invariants business_language=invariant,business_reason -->
| Invariant | Business Reason | Source Finding |
|-----------|-----------------|----------------|
| Each model the business holds has exactly one record | The business needs one place that says which models it holds | S4 constraint_register #1 |
| No model responds to a user prompt unless it is registered and in service | Registration records a model; only placement authorizes it to respond | S4 constraint_register #2 |
| A model has at most one time in service at any moment | A response must be attributable to exactly one set of rules | S4 constraint_register #3 |
| Each time in service has exactly one system prompt and one set of response rules | The rules a response was written under must be unambiguous | S4 constraint_register #4 |
| No model reads a more sensitive kind of information than its sensitivity ceiling | The ceiling is what staff authorized the model to read | S4 constraint_register #5 |
| No model reads anything but the question, the supporting material and its system prompt | The record must be able to say exactly what the model read | S4 constraint_register #6 |
| No model response is released that breaks a response rule | The rules apply while the model writes, so nothing forbidden is written | S4 constraint_register #7 |
| No model response is released that reached the longest response before it was finished | An unfinished response is not a response | S4 constraint_register #8 |
| Every user prompt is recorded, whether responded to or refused | A regulator asks about refusals as well as responses | S4 constraint_register #9 |
| Every refusal carries its reason | A refusal without a reason cannot be examined | S4 constraint_register #10 |
| Every business operation is traceable and auditable | The business must be able to show what was done and by whom | S4 constraint_register #11 |
| Each word's rule decision is a step governance can see | The rules must visibly act while the model writes | S4 constraint_register #18 |
| Only the model's step gives results not determined by its inputs | A reader must see exactly where determinism ends | S4 constraint_register #19 |
| The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly | A user prompt's trace must be reproducible from what was recorded | S4 constraint_register #20 |
| Every word chosen more adventurously than the most likely one is drawn from a recorded seed | Anyone reading the record can re-derive each chosen word | S4 constraint_register #21 |

---

## 6. Business Actions

<!-- register:actions business_language=object,trigger -->
| Action | Object | Trigger | Status (IN_SCOPE, DEFERRED) | Source Finding |
|--------|--------|---------|-----------------------------|----------------|
| Register | Model | Model staff record a model the business holds | IN_SCOPE | S4 capability_graph Register a model |
| Place in service | Model | Model staff authorize a registered model to respond, under a sensitivity ceiling, system prompt and response rules | IN_SCOPE | S4 capability_graph Place a model in service, and withdraw it |
| Withdraw from service | Model | Model staff stop a model responding | IN_SCOPE | S4 capability_graph Place a model in service, and withdraw it |
| Submit | User prompt | A requester asks a question on behalf of a customer | IN_SCOPE | S4 capability_graph Submit a user prompt and release or refuse the model response |
| Retrieve | User prompt record | Model staff examine what happened to a user prompt | IN_SCOPE | S4 capability_graph Retrieve a user prompt record |
| Retire | Model | Model staff judge a model no longer to be held | DEFERRED | S4 authoring_scope Retiring models |
| Review | Model response | A finished response is examined before release | DEFERRED | S4 authoring_scope Disclosure |
| Replace | Model in service | Staff substitute another model | DEFERRED | S4 authoring_scope Substitution |

---

## 7. Provisional Artifact Codes

<!-- register:provisional_codes business_language=summary -->
| Subdomain | Provisional Code | Family (AC, IN, WF, CC, CT, EV, RB, VOCAB, STRUCTURE, TI, TE) | Summary | Source Finding |
|-----------|------------------|-------------------------|---------|----------------|
| model_response | AC_MODEL_STAFF_V0 | AC | The authorized model staff member who registers, places, withdraws and retrieves | S4 actors Authorized model staff |
| model_response | AC_REQUESTER_V0 | AC | The authorized requester who submits a user prompt on behalf of a customer | S4 actors Authorized requester |
| model_response | IN_REGISTER_MODEL_V0 | IN | A request to register a model with its description and fingerprint | S5 actions Register |
| model_response | IN_PLACE_MODEL_IN_SERVICE_V0 | IN | A request to place a registered model in service with its ceiling, system prompt and response rules | S5 actions Place in service |
| model_response | IN_WITHDRAW_MODEL_FROM_SERVICE_V0 | IN | A request to withdraw a model from service | S5 actions Withdraw from service |
| model_response | IN_SUBMIT_USER_PROMPT_V0 | IN | A user prompt submitted on behalf of a customer | S5 actions Submit |
| model_response | IN_RETRIEVE_USER_PROMPT_RECORD_V0 | IN | A request to retrieve the record of a user prompt | S5 actions Retrieve |
| model_response | WF_REGISTER_MODEL_V0 | WF | Registering a model, refusing a second registration of the same model | S4 capability_graph Register a model |
| model_response | WF_PLACE_MODEL_IN_SERVICE_V0 | WF | Opening a time in service for a registered model not already in service | S4 capability_graph Place a model in service, and withdraw it |
| model_response | WF_WITHDRAW_MODEL_FROM_SERVICE_V0 | WF | Closing a model's time in service | S4 capability_graph Place a model in service, and withdraw it |
| model_response | WF_SUBMIT_USER_PROMPT_V0 | WF | Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it | S4 capability_graph Submit a user prompt and release or refuse the model response |
| model_response | WF_RETRIEVE_USER_PROMPT_RECORD_V0 | WF | Reading a user prompt record and recording that it was read | S4 capability_graph Retrieve a user prompt record |
| model_response | CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0 | CC | Confirm the staff member is model staff | S4 gap_register GAP-12 |
| model_response | CC_CLAIM_USER_PROMPT_IDENTITY_V0 | CC | Claim a user prompt's identity so a second submission under it is refused | S4 gap_register GAP-15 |
| model_response | CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0 | CC | Confirm the requester may act for the customer the user prompt is for | S4 gap_register GAP-12 |
| model_response | CC_CLAIM_MODEL_IDENTITY_V0 | CC | Claim a model's identity so a second registration of the same model is refused | S4 gap_register GAP-13 |
| model_response | CC_REGISTER_MODEL_V0 | CC | Record a model's description and fingerprint as its record, registered | S4 gap_register GAP-13 |
| model_response | CC_PLACE_MODEL_IN_SERVICE_V0 | CC | Open a time in service with its ceiling, system prompt and response rules, and mark the model in service | S4 gap_register GAP-14 |
| model_response | CC_WITHDRAW_MODEL_FROM_SERVICE_V0 | CC | Close the time in service and mark the model registered | S4 gap_register GAP-14 |
| model_response | CC_ADMIT_USER_PROMPT_V0 | CC | Refuse a user prompt before the model sees it when its model is not registered or not in service | S4 gap_register GAP-15 |
| model_response | CC_CONFIRM_WITHIN_CEILING_V0 | CC | Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling | S4 gap_register GAP-15 |
| model_response | CC_CONFIRM_READING_FITS_V0 | CC | Assemble exactly what the model reads and refuse it before the model sees it when it is too long | S4 gap_register GAP-15 |
| model_response | CC_WRITE_MODEL_RESPONSE_V0 | CC | Write the response word by word under the rules in force | S4 gap_register GAP-15 |
| model_response | CC_CONFIRM_RESPONSE_RELEASABLE_V0 | CC | Release a written response only when it finished and no rule stopped it, refusing it with the rule or length that stopped it | S4 gap_register GAP-15 |
| model_response | CC_RECORD_USER_PROMPT_V0 | CC | Append the user prompt record with what the model read, the rules in force and the outcome | S4 gap_register GAP-15 |
| model_response | CC_RETRIEVE_USER_PROMPT_RECORD_V0 | CC | Read the record of a user prompt | S4 gap_register GAP-16 |
| model_response | CC_APPEND_MODEL_OPERATION_V0 | CC | Append a durable account of a performed operation to the subdomain's own trail | S4 gap_register GAP-17 |
| model_response | CT_PURE_FORM_MODEL_IDENTITY_KEY_V0 | CT | Forms the single key claimed for a model from its description and fingerprint | S4 gap_register GAP-01 |
| model_response | CT_PURE_COMPARE_SENSITIVITY_V0 | CT | Decides whether a kind of information is no more sensitive than a ceiling, by the declared order | S4 gap_register GAP-03 |
| model_response | CT_PURE_ASSEMBLE_MODEL_READING_V0 | CT | Assembles exactly what the model reads and decides whether it fits what the model can read at once | S4 gap_register GAP-04 |
| model_response | CT_PURE_FORM_RESPONSE_RULES_V0 | CT | Forms the response rules in force for one user prompt from the time in service and the customer's account numbers | S4 gap_register GAP-05 |
| model_response | CT_IMPURE_OFFER_NEXT_WORDS_V0 | CT | The model's step: offers its next words given the response so far; the one step whose result is not determined by its inputs | S4 gap_register GAP-06 |
| model_response | CT_PURE_CHOOSE_PERMITTED_WORD_V0 | CT | Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed | S4 gap_register GAP-07 |
| model_response | CT_WRITE_NEXT_WORD_V0 | CT | One pass of writing, composed of the model's offer and the rules' choice | S4 gap_register GAP-08 |
| model_response | CT_WRITE_RESPONSE_V0 | CT | Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped | S4 gap_register GAP-08 |
| model_response | EV_MODEL_REGISTERED_V0 | EV | The moment the business records a model | S4 gap_register GAP-20 |
| model_response | EV_MODEL_SERVICE_STARTED_V0 | EV | The moment a model is placed in service and a time in service begins | S4 gap_register GAP-20 |
| model_response | EV_MODEL_SERVICE_ENDED_V0 | EV | The moment a model is withdrawn from service and its time in service ends | S4 gap_register GAP-20 |
| model_response | EV_USER_PROMPT_RESPONDED_V0 | EV | The moment a model response is released | S4 gap_register GAP-20 |
| model_response | EV_USER_PROMPT_REFUSED_V0 | EV | The moment a user prompt yields no response | S4 gap_register GAP-20 |
| model_response | VOCAB_KIND_OF_INFORMATION_V0 | VOCAB | The kinds of information, least sensitive first: public, internal, confidential, restricted | S4 gap_register GAP-02 |
| model_response | RB_MODEL_RESPONSE_BINDINGS_V0 | RB | Binds the subdomain's operations to the stores and mechanisms they use | S4 gap_register GAP-18 |
| model_response | STRUCTURE_MODEL_RESPONSE_STORAGE_V0 | STRUCTURE | Declares the stores the subdomain owns and the paths they occupy | S4 gap_register GAP-18 |

---

## 8. Cross-Subdomain References

<!-- register:cross_subdomain_refs optional business_language=role -->
| CC Code | Defined In | Role | Source Finding |
|---------|------------|------|----------------|

No capability contract from another subdomain is referenced. The subdomain reuses declared
mechanisms — durable records, uniqueness, append-only trails and four pure transforms — and composes
them itself. The test model is a realization, not a capability contract, and is carried to Stage 7.

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 0, Stage 4 | subdomain_purpose · actors · bm_entities · resources · events · capability_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
