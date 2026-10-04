# Stage 1 — Change Request: Clarification & Fact Capture: causal_language_model / model_response
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_01_model_response
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
| model_response | NEW_SUBDOMAIN | causal_language_model is proposed as a new project, not part of the current software baseline, and the business requires model responses written under rules it cannot show today. It extends nothing that exists. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| causal_language_model | The project governing a business's use of language models, across six functions of which model_response is the first. | CR seed §2 Business Vocabulary #1 |
| Business | An organization that uses a language model to respond to its customers' questions about their own accounts; a bank is one example. | CR seed §2 Business Vocabulary #2 |
| Language Model | A model that writes a response one word at a time, each word depending on the words before it. Its exact response cannot be predicted in advance, and given the same question twice it may respond differently. | CR seed §2 Business Vocabulary #3 |
| Model | A language model the business holds. | CR seed §2 Business Vocabulary #4 |
| Registration | The record of a model, describing how it is built and carrying its training fingerprint. | CR seed §2 Business Vocabulary #5 |
| Description | How a model is built, including the amount of text it can read at once. | CR seed §2 Business Vocabulary #6 |
| Training Fingerprint | A fingerprint of a model's training, supplied by whoever provided the model. It is the provider's claim; the business records it and does not verify how the model was trained. | CR seed §2 Business Vocabulary #7 |
| In Service | The condition of a registered model that authorized model staff have placed in service, and which may therefore respond to user prompts. | CR seed §2 Business Vocabulary #8 |
| Time in Service | One period during which a model is in service, from being placed in service to being withdrawn, with exactly one sensitivity ceiling, system prompt and set of response rules. | CR seed §2 Business Vocabulary #9 |
| Kind of Information | How sensitive information is: public, internal, confidential or restricted, from least to most sensitive. | CR seed §2 Business Vocabulary #10 |
| Sensitivity Ceiling | The most sensitive kind of information a model in service may read. | CR seed §2 Business Vocabulary #11 |
| System Prompt | The business's standing instructions to a model, set for its time in service, which the model reads with every user prompt. | CR seed §2 Business Vocabulary #12 |
| Response Rules | The rules set for a model's time in service that apply while it writes: words and patterns it must never write, how freely it may choose its words, and the longest response it may write. | CR seed §2 Business Vocabulary #13 |
| Forbidden Words and Patterns | Words and patterns a model must never write, such as any account number other than the customer's own. | CR seed §2 Business Vocabulary #14 |
| Freedom of Word Choice | How freely a model may choose its words, from always choosing the most likely word to choosing more adventurously. | CR seed §2 Business Vocabulary #15 |
| Longest Response | The longest response a model may write during its time in service. | CR seed §2 Business Vocabulary #16 |
| User Prompt | What a requester submits on behalf of one customer: a question and any supporting material, naming the model, stating the most sensitive kind of information the question and its material contain, and carrying the customer's account numbers. | CR seed §2 Business Vocabulary #17 |
| Question | What the requester asks the model on the customer's behalf. | CR seed §2 Business Vocabulary #18 |
| Supporting Material | Material carried with a question for the model to read, such as the customer's recent transactions. | CR seed §2 Business Vocabulary #19 |
| Customer | The customer on whose behalf a user prompt is submitted, and whose own accounts the question is about. | CR seed §2 Business Vocabulary #20 |
| Account | An account a customer holds with the business, identified by its account number. | CR seed §2 Business Vocabulary #21 |
| Requester | A person who submits a user prompt on behalf of a customer. | CR seed §2 Business Vocabulary #22 |
| Authorized Requester | A requester permitted to act for the customer a user prompt is for. | CR seed §2 Business Vocabulary #23 |
| Authorized Model Staff | Staff of the business permitted to register models, place them in service, withdraw them, and retrieve user prompt records. | CR seed §2 Business Vocabulary #24 |
| Model Response | What a model writes in response to a user prompt, when it finishes under the response rules. | CR seed §2 Business Vocabulary #25 |
| Refusal | The outcome of a user prompt that yields no model response, carrying the reason. | CR seed §2 Business Vocabulary #26 |
| User Prompt Record | The record kept of every user prompt, responded to or refused. | CR seed §2 Business Vocabulary #27 |
| Test Model | A model the business uses until a real model is available, which deliberately tries to break the rules. | CR seed §2 Business Vocabulary #28 |
| Business Operation | An action performed that must be traceable and auditable. | CR seed §2 Business Vocabulary #29 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| Model responses are written under rules that apply while the model writes, not afterwards. | CR seed §3 Requested Outcomes #1 |
| For any model response, the business can show a regulator which model wrote it, who asked, what the model was given to read, which rules applied while it wrote, and whether a response was refused and why. | CR seed §3 Requested Outcomes #2 |
| A model responds to no one until authorized model staff have registered it and placed it in service. | CR seed §3 Requested Outcomes #3 |
| Authorized model staff can register a model, place it in service with its system prompt and response rules, withdraw it from service, and retrieve the record of any user prompt. | CR seed §3 Requested Outcomes #4 |
| Authorized requesters can submit a user prompt to a model in service on behalf of a customer. | CR seed §3 Requested Outcomes #5 |
| The business can see the rules hold, using a test model that tries to break them, before a real model is trusted with them. | CR seed §3 Requested Outcomes #6 |
| Every business operation is traceable and auditable. | CR seed §3 Requested Outcomes #7 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| The proposed name of the project is causal_language_model. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| The project scope covers six functions: model_response, registry, disclosure, action, substitution, reporting. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| The scope of this change request is limited to the model_response function, and includes only as much of the registry as a model response needs. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A business wants to use a language model to respond to its customers' questions about their own accounts; a bank is one example. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| A language model writes a response one word at a time, and each word depends on the words before it. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| Nobody can predict a language model's exact response in advance; given the same question twice, it may respond differently. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Today, staff paste customers' questions into a model and copy its response back. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| Today nobody can say afterwards which model responded, what it was shown, or whether anything stopped it from writing something it should not have written. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| A check made after a response is written can catch a problem only once the model has already produced it. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| Before a model can respond to anything, authorized model staff register it. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A registration describes how the model is built, including the amount of text it can read at once, and carries a training fingerprint supplied by whoever provided the model. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| Two registrations with the same description and the same fingerprint are the same model, and the business holds one record for it. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| Registering a model that is already registered is refused, because the model already has its record. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| The training fingerprint is the provider's claim; the business records it and does not verify how the model was trained. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| A registered model does not respond to anyone until authorized model staff place it in service. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| When staff place a model in service, they state the most sensitive kind of information it may read, and set its system prompt and response rules. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| The kinds of information, from least to most sensitive, are public, internal, confidential and restricted. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| The system prompt is the business's standing instructions to the model, which it reads with every user prompt. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| The response rules are: words and patterns the model must never write, how freely it may choose its words, and the longest response it may write. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A rule belongs to the response rules only if it can be applied while the model writes. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| A rule that can only be judged once a response is finished belongs to a later review of finished responses, which this release does not include. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| "Another customer's account number" depends on who the customer is; the rule is applied for each user prompt, using the account numbers of the customer the user prompt is for. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| The user prompt carries the account numbers of the customer it is for, taken from the business's existing records. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| The customer's account numbers are used to form the rule against another customer's account number, and reach the model only if they are also part of the supporting material. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| The requester cannot change the response rules or the system prompt; they belong to the model's time in service. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| When the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| If the model cannot finish a response without breaking a rule, it gives no response; the user prompt is refused, and the record says which rule stopped it. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| A response that reaches its longest permitted length before it is finished is not released; the user prompt is refused, and the record says so. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| A withdrawn model may be placed in service again, which begins a new time in service with its system prompt and response rules set afresh. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| Several models may be in service at the same time. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| A model already in service cannot be placed in service again; staff withdraw it first. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| Each time in service has exactly one system prompt and one set of response rules. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| An authorized requester submits a user prompt on behalf of one customer. | HIGH | CR seed §4 Known Facts — Business Truths #33 |
| A user prompt carries the question and any supporting material, names the model, and states the most sensitive kind of information the question and its material contain. | HIGH | CR seed §4 Known Facts — Business Truths #34 |
| The requester must be permitted to act for the customer the user prompt is for. | HIGH | CR seed §4 Known Facts — Business Truths #35 |
| Deciding which requesters may act for which customers is the business's existing business and is not decided here. | HIGH | CR seed §4 Known Facts — Business Truths #36 |
| Naming a customer does not by itself give the requester access to that customer's accounts. | HIGH | CR seed §4 Known Facts — Business Truths #37 |
| Deciding which staff are authorized model staff is the business's existing business and is not decided here. | HIGH | CR seed §4 Known Facts — Business Truths #38 |
| What the model reads is exactly the question, the supporting material, and the system prompt of the model's time in service; nothing else reaches the model. | HIGH | CR seed §4 Known Facts — Business Truths #39 |
| A user prompt is refused before the model sees it when the model is not registered, the model is not in service, the user prompt contains a more sensitive kind of information than the model may read, or what the model would read is longer than the model can read at once. | HIGH | CR seed §4 Known Facts — Business Truths #40 |
| Every user prompt is recorded, whether responded to or refused. | HIGH | CR seed §4 Known Facts — Business Truths #41 |
| A user prompt record holds who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason the user prompt was refused. | HIGH | CR seed §4 Known Facts — Business Truths #42 |
| The record keeps what the model read, not only a summary or fingerprint of it. | HIGH | CR seed §4 Known Facts — Business Truths #43 |
| The business does not claim that a model response is true. | HIGH | CR seed §4 Known Facts — Business Truths #44 |
| The business claims only that a model response was written by the recorded model, from the recorded material, under the recorded rules. | HIGH | CR seed §4 Known Facts — Business Truths #45 |
| Until a real model is available, the business uses a test model. | HIGH | CR seed §4 Known Facts — Business Truths #46 |
| The test model deliberately tries to break the rules: it tries to write another customer's account number. | HIGH | CR seed §4 Known Facts — Business Truths #47 |
| In this release the test model does not respond from material it was not given; the business can show only that nothing else reached the model, and the record shows that. | HIGH | CR seed §4 Known Facts — Business Truths #48 |
| Catching a response made up from nothing needs the finished response, and belongs to the later review of finished responses. | HIGH | CR seed §4 Known Facts — Business Truths #49 |
| The same rules govern the test model, and its responses are recorded in the same way. | HIGH | CR seed §4 Known Facts — Business Truths #50 |
| Every business operation must be traceable and auditable. | HIGH | CR seed §4 Known Facts — Business Truths #51 |
| The business starts with no models registered. | HIGH | CR seed §4 Known Facts — Business Truths #52 |
| The operations required are: register a model, place a registered model in service with its system prompt and response rules, withdraw a model from service, retrieve the record of any user prompt, and submit a user prompt to a model in service on behalf of a customer. | HIGH | CR seed §4 Known Facts — Business Truths #53 |
| Retiring models, reviewing a model response after it is written, letting a model propose actions, replacing the model in service, and regulator reporting are excluded from this release. | HIGH | CR seed §4 Known Facts — Business Truths #54 |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH | CR seed §4 Known Facts — Business Truths #55 |
| The excluded capabilities must not be designed into the initial solution. | HIGH | CR seed §4 Known Facts — Business Truths #56 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| causal_language_model is not part of the current software baseline. | The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different. | Confirm no artifact in the pinned composition carries the causal_language_model namespace. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| No capability in the current composition registers language models or governs how a model writes a response. | This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension. | Confirm nothing in the composition registers a model, places one in service, or applies rules while a model writes. The ai_governance domain governs AI agents and licensing, and must be checked. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |

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
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy | CR seed §7 Constraints #1 |
| Response rules apply while the model writes, not afterwards. | Business policy | CR seed §7 Constraints #2 |
| Only authorized model staff may register a model, place it in service, withdraw it, or retrieve user prompt records. | Business policy | CR seed §7 Constraints #3 |
| Only an authorized requester permitted to act for the customer may submit a user prompt on that customer's behalf. | Business policy | CR seed §7 Constraints #4 |
| The requester cannot change the response rules or the system prompt. | Business policy | CR seed §7 Constraints #5 |
| Nothing reaches the model except the question, the supporting material and the system prompt. | Business policy | CR seed §7 Constraints #6 |
| A user prompt refused before the model sees it never reaches the model. | Business policy | CR seed §7 Constraints #7 |
| The record keeps exactly what the model read, not only a summary or fingerprint of it. | Business policy | CR seed §7 Constraints #8 |
| The business must not claim that a model response is true. | Business policy | CR seed §7 Constraints #9 |
| Every business operation must leave a record that can be traced and audited. | Business policy | CR seed §7 Constraints #10 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| Each model the business holds has exactly one record. | CR seed §8 Business Invariants #1 |
| No model responds to a user prompt unless it is registered and in service. | CR seed §8 Business Invariants #2 |
| A model has at most one time in service at any moment. | CR seed §8 Business Invariants #3 |
| Each time in service has exactly one system prompt and one set of response rules. | CR seed §8 Business Invariants #4 |
| No model reads a more sensitive kind of information than its sensitivity ceiling. | CR seed §8 Business Invariants #5 |
| No model reads anything but the question, the supporting material and its system prompt. | CR seed §8 Business Invariants #6 |
| No model response is released that breaks a response rule. | CR seed §8 Business Invariants #7 |
| No model response is released that reached the longest response before it was finished. | CR seed §8 Business Invariants #8 |
| Every user prompt is recorded, whether responded to or refused. | CR seed §8 Business Invariants #9 |
| Every refusal carries its reason. | CR seed §8 Business Invariants #10 |
| Every business operation is traceable and auditable. | CR seed §8 Business Invariants #11 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Model | Registered | The business holds the model's record; it responds to no one. | CR seed §9 Lifecycle States #1 |
| Model | In Service | Authorized model staff have placed the model in service; it may respond to user prompts under its time in service's sensitivity ceiling, system prompt and response rules. | CR seed §9 Lifecycle States #2 |
| User Prompt | Responded | The model finished a response under the response rules, and the model response was released to the requester. | CR seed §9 Lifecycle States #3 |
| User Prompt | Refused | The user prompt yielded no model response; the record carries the reason. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| Model Registered | When authorized model staff register a model. | The business holds a record of the model. | CR seed §10 Business Events #1 |
| Model Placed In Service | When authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules. | The model may respond to user prompts, and a time in service begins. | CR seed §10 Business Events #2 |
| Model Withdrawn From Service | When authorized model staff withdraw a model from service. | The model responds to no one, and its time in service ends. | CR seed §10 Business Events #3 |
| User Prompt Responded | When a model finishes a response under the response rules. | A model response is released, and its record shows what it was written from and under which rules. | CR seed §10 Business Events #4 |
| User Prompt Refused | When a user prompt yields no model response. | The refusal and its reason are recorded. | CR seed §10 Business Events #5 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Model record | Model Response | CR seed §11 Authority Boundaries #1 |
| Time in service | Model Response | CR seed §11 Authority Boundaries #2 |
| User prompt record | Model Response | CR seed §11 Authority Boundaries #3 |
| The sensitivity ceiling, system prompt and response rules for a time in service | Authorized model staff | CR seed §11 Authority Boundaries #4 |
| The kind of information a user prompt contains | The requester who states it | CR seed §11 Authority Boundaries #5 |
| Which requesters may act for which customers | The business's existing business | CR seed §11 Authority Boundaries #6 |
| Which staff are authorized model staff | The business's existing business | CR seed §11 Authority Boundaries #7 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| Registry beyond what a model response needs | A project function; this change request includes only as much of the registry as a model response needs. | CR seed §12 Out of Scope #1 |
| Retiring models | Declared excluded from this release; expected through a future governed change request. | CR seed §12 Out of Scope #2 |
| Disclosure | A project function; reviewing a model response after it is written is declared excluded from this release. | CR seed §12 Out of Scope #3 |
| Action | A project function; letting a model propose actions is declared excluded from this release. | CR seed §12 Out of Scope #4 |
| Substitution | A project function; replacing the model in service is declared excluded from this release. | CR seed §12 Out of Scope #5 |
| Reporting | A project function; regulator reporting is declared excluded from this release. | CR seed §12 Out of Scope #6 |
| Rules that can only be judged once a response is finished | They belong to a later review of finished responses. | CR seed §12 Out of Scope #7 |
| Catching a response made up from nothing | It needs the finished response, and belongs to the later review of finished responses. | CR seed §12 Out of Scope #8 |
| Verifying how a model was trained | The training fingerprint is the provider's claim, recorded and not verified. | CR seed §12 Out of Scope #9 |
| Deciding which requesters may act for which customers | The business's existing business. | CR seed §12 Out of Scope #10 |
| Deciding which staff are authorized model staff | The business's existing business. | CR seed §12 Out of Scope #11 |
| Claiming that a model response is true | The business claims only what the record shows. | CR seed §12 Out of Scope #12 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| model_response | CREATED | CR seed §13 Governance Scope #1 |
| registry | ADJACENT | CR seed §13 Governance Scope #2 |
| disclosure | ADJACENT | CR seed §13 Governance Scope #3 |
| action | ADJACENT | CR seed §13 Governance Scope #4 |
| substitution | ADJACENT | CR seed §13 Governance Scope #5 |
| reporting | ADJACENT | CR seed §13 Governance Scope #6 |

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
| Authorized model staff can register a model with its description and training fingerprint, and the business then holds exactly one record for it. | CR seed §15 Acceptance Criteria #1 |
| A registration whose description and fingerprint match a registered model is refused, and the reason states that the model is already registered. | CR seed §15 Acceptance Criteria #2 |
| Authorized model staff can place a registered model in service with a sensitivity ceiling, system prompt and response rules. | CR seed §15 Acceptance Criteria #3 |
| Placing a model in service that is already in service is refused. | CR seed §15 Acceptance Criteria #4 |
| Authorized model staff can withdraw a model from service, after which it responds to no one. | CR seed §15 Acceptance Criteria #5 |
| A withdrawn model can be placed in service again, with a system prompt and response rules set afresh. | CR seed §15 Acceptance Criteria #6 |
| Several models can be in service at the same time. | CR seed §15 Acceptance Criteria #7 |
| An authorized requester can submit a user prompt to a model in service on behalf of a customer, and receives a model response written under the response rules. | CR seed §15 Acceptance Criteria #8 |
| A user prompt naming a model that is not registered is refused before the model sees it. | CR seed §15 Acceptance Criteria #9 |
| A user prompt naming a model that is not in service is refused before the model sees it. | CR seed §15 Acceptance Criteria #10 |
| A user prompt containing a more sensitive kind of information than the model may read is refused before the model sees it. | CR seed §15 Acceptance Criteria #11 |
| A user prompt whose question, material and system prompt together are longer than the model can read at once is refused before the model sees it. | CR seed §15 Acceptance Criteria #12 |
| A requester not permitted to act for the customer cannot submit a user prompt on that customer's behalf. | CR seed §15 Acceptance Criteria #13 |
| When the test model tries to write another customer's account number, that number is not written, and the response continues with permitted words. | CR seed §15 Acceptance Criteria #14 |
| When the model cannot finish a response without breaking a rule, the user prompt is refused, and the record names the rule that stopped it. | CR seed §15 Acceptance Criteria #15 |
| A response that reaches the longest response before it is finished is not released, and the record says so. | CR seed §15 Acceptance Criteria #16 |
| The requester cannot change the response rules or the system prompt. | CR seed §15 Acceptance Criteria #17 |
| Every user prompt, responded to or refused, has a record showing who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason for refusal. | CR seed §15 Acceptance Criteria #18 |
| Authorized model staff can retrieve the record of any user prompt. | CR seed §15 Acceptance Criteria #19 |
| Staff who are not authorized model staff cannot register a model, place one in service, withdraw one, or retrieve user prompt records. | CR seed §15 Acceptance Criteria #20 |
| Every business operation performed can be traced and audited afterwards. | CR seed §15 Acceptance Criteria #21 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Model | Its description and its training fingerprint together. | Their descriptions and their training fingerprints both match. | CR seed §16 Identity and Sameness #1 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Model | — | Registered | Authorized model staff register the model. | None. | CR seed §17 Lifecycle Transitions #1 |
| Model | Registered | In Service | Authorized model staff place the model in service with its sensitivity ceiling, system prompt and response rules. | A time in service begins. | CR seed §17 Lifecycle Transitions #2 |
| Model | In Service | Registered | Authorized model staff withdraw the model from service. | The time in service ends. | CR seed §17 Lifecycle Transitions #3 |
| User Prompt | — | Responded | The model finishes a response under the response rules. | The user prompt record is written. | CR seed §17 Lifecycle Transitions #4 |
| User Prompt | — | Refused | A refusal condition holds, before or while the model writes. | The user prompt record is written with the reason. | CR seed §17 Lifecycle Transitions #5 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Register a model | Its description and fingerprint match a registered model. | The model already has its record. | CR seed §18 Operation Refusals #1 |
| Place a model in service | The model is not registered. | Only a registered model may be placed in service. | CR seed §18 Operation Refusals #2 |
| Place a model in service | The model is already in service. | Each time in service has exactly one system prompt and set of response rules; staff withdraw the model first. | CR seed §18 Operation Refusals #3 |
| Withdraw a model from service | The model is not in service. | Only a model in service can be withdrawn. | CR seed §18 Operation Refusals #4 |
| Submit a user prompt | The model is not registered. | No model responds unless it is registered. | CR seed §18 Operation Refusals #5 |
| Submit a user prompt | The model is not in service. | A registered model responds to no one until it is placed in service. | CR seed §18 Operation Refusals #6 |
| Submit a user prompt | The user prompt contains a more sensitive kind of information than the model may read. | A model reads nothing above its sensitivity ceiling. | CR seed §18 Operation Refusals #7 |
| Submit a user prompt | What the model would read is longer than the model can read at once. | The model cannot read it. | CR seed §18 Operation Refusals #8 |
| Submit a user prompt | The requester is not permitted to act for the customer. | Naming a customer does not by itself give access to that customer's accounts. | CR seed §18 Operation Refusals #9 |
| Submit a user prompt | The model cannot finish a response without breaking a response rule. | No response that breaks a rule is released; the record names the rule. | CR seed §18 Operation Refusals #10 |
| Submit a user prompt | The response reaches the longest response before it is finished. | An unfinished response is not released. | CR seed §18 Operation Refusals #11 |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | Only authorized model staff perform these operations. | CR seed §18 Operation Refusals #12 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Which requesters may act for which customers | The business's existing business | Not decided within this project. | CR seed §19 Authority Deferrals #1 |
| Which staff are authorized model staff | The business's existing business | Not decided within this project. | CR seed §19 Authority Deferrals #2 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
