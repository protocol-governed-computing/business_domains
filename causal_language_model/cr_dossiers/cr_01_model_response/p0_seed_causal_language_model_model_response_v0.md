# Change Seed — causal_language_model / model_response

**Stage:** 0 — Change Seed
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 1 — Change Request

Reorganized faithfully from `p0_business_problem_statement.md`, including the clarifications its
author answered. Human input only — nothing here was added, decided or designed by the pipeline.

---

## 0. Subdomain Purpose

<!-- register:subdomain_purpose business_language -->

The Model Response subdomain governs how a business's language model responds to a customer's
question about the customer's own accounts: under rules that apply while the model writes, not
afterwards, and with a record that shows for every model response which model wrote it, who asked,
what the model was given to read, which rules applied, and whether the response was refused and
why. It exists because staff today paste customers' questions into a model and copy its response
back, and nobody can say afterwards which model responded, what it was shown, or whether anything
stopped it from writing something it should not have written. It is the first of six functions the
causal_language_model project will govern. It carries only as much of the registry as a model
response needs, and it governs none of the remaining functions.

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale |
|-----------|----------------|-----------|
| model_response | NEW_SUBDOMAIN | causal_language_model is proposed as a new project, not part of the current software baseline, and the business requires model responses written under rules it cannot show today. It extends nothing that exists. |

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition |
|------|------------|
| causal_language_model | The project governing a business's use of language models, across six functions of which model_response is the first. |
| Business | An organization that uses a language model to respond to its customers' questions about their own accounts; a bank is one example. |
| Language Model | A model that writes a response one word at a time, each word depending on the words before it. Its exact response cannot be predicted in advance, and given the same question twice it may respond differently. |
| Model | A language model the business holds. |
| Registration | The record of a model, describing how it is built and carrying its training fingerprint. |
| Description | How a model is built, including the amount of text it can read at once. |
| Training Fingerprint | A fingerprint of a model's training, supplied by whoever provided the model. It is the provider's claim; the business records it and does not verify how the model was trained. |
| In Service | The condition of a registered model that authorized model staff have placed in service, and which may therefore respond to user prompts. |
| Time in Service | One period during which a model is in service, from being placed in service to being withdrawn, with exactly one sensitivity ceiling, system prompt and set of response rules. |
| Kind of Information | How sensitive information is: public, internal, confidential or restricted, from least to most sensitive. |
| Sensitivity Ceiling | The most sensitive kind of information a model in service may read. |
| System Prompt | The business's standing instructions to a model, set for its time in service, which the model reads with every user prompt. |
| Response Rules | The rules set for a model's time in service that apply while it writes: words and patterns it must never write, how freely it may choose its words, and the longest response it may write. |
| Forbidden Words and Patterns | Words and patterns a model must never write, such as any account number other than the customer's own. |
| Freedom of Word Choice | How freely a model may choose its words, from always choosing the most likely word to choosing more adventurously. |
| Longest Response | The longest response a model may write during its time in service. |
| User Prompt | What a requester submits on behalf of one customer: a question and any supporting material, naming the model and stating the most sensitive kind of information the question and its material contain. |
| Question | What the requester asks the model on the customer's behalf. |
| Supporting Material | Material carried with a question for the model to read, such as the customer's recent transactions. |
| Customer | The customer on whose behalf a user prompt is submitted, and whose own accounts the question is about. |
| Account | An account a customer holds with the business, identified by its account number. |
| Requester | A person who submits a user prompt on behalf of a customer. |
| Authorized Requester | A requester permitted to act for the customer a user prompt is for. |
| Authorized Model Staff | Staff of the business permitted to register models, place them in service, withdraw them, and retrieve user prompt records. |
| Model Response | What a model writes in response to a user prompt, when it finishes under the response rules. |
| Refusal | The outcome of a user prompt that yields no model response, carrying the reason. |
| User Prompt Record | The record kept of every user prompt, responded to or refused. |
| Test Model | A model the business uses until a real model is available, which deliberately tries to break the rules. |
| Business Operation | An action performed that must be traceable and auditable. |

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome |
|---------|
| Model responses are written under rules that apply while the model writes, not afterwards. |
| For any model response, the business can show a regulator which model wrote it, who asked, what the model was given to read, which rules applied while it wrote, and whether a response was refused and why. |
| A model responds to no one until authorized model staff have registered it and placed it in service. |
| Authorized model staff can register a model, place it in service with its system prompt and response rules, withdraw it from service, and retrieve the record of any user prompt. |
| Authorized requesters can submit a user prompt to a model in service on behalf of a customer. |
| The business can see the rules hold, using a test model that tries to break them, before a real model is trusted with them. |
| Every business operation is traceable and auditable. |

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) |
|------|-----------|
| The proposed name of the project is causal_language_model. | HIGH |
| The project scope covers six functions: model_response, registry, disclosure, action, substitution, reporting. | HIGH |
| The scope of this change request is limited to the model_response function, and includes only as much of the registry as a model response needs. | HIGH |
| A business wants to use a language model to respond to its customers' questions about their own accounts; a bank is one example. | HIGH |
| A language model writes a response one word at a time, and each word depends on the words before it. | HIGH |
| Nobody can predict a language model's exact response in advance; given the same question twice, it may respond differently. | HIGH |
| Today, staff paste customers' questions into a model and copy its response back. | HIGH |
| Today nobody can say afterwards which model responded, what it was shown, or whether anything stopped it from writing something it should not have written. | HIGH |
| A check made after a response is written can catch a problem only once the model has already produced it. | HIGH |
| Before a model can respond to anything, authorized model staff register it. | HIGH |
| A registration describes how the model is built, including the amount of text it can read at once, and carries a training fingerprint supplied by whoever provided the model. | HIGH |
| Two registrations with the same description and the same fingerprint are the same model, and the business holds one record for it. | HIGH |
| Registering a model that is already registered is refused, because the model already has its record. | HIGH |
| The training fingerprint is the provider's claim; the business records it and does not verify how the model was trained. | HIGH |
| A registered model does not respond to anyone until authorized model staff place it in service. | HIGH |
| When staff place a model in service, they state the most sensitive kind of information it may read, and set its system prompt and response rules. | HIGH |
| The kinds of information, from least to most sensitive, are public, internal, confidential and restricted. | HIGH |
| The system prompt is the business's standing instructions to the model, which it reads with every user prompt. | HIGH |
| The response rules are: words and patterns the model must never write, how freely it may choose its words, and the longest response it may write. | HIGH |
| A rule belongs to the response rules only if it can be applied while the model writes. | HIGH |
| A rule that can only be judged once a response is finished belongs to a later review of finished responses, which this release does not include. | HIGH |
| "Another customer's account number" depends on who the customer is; the rule is applied for each user prompt, using the account numbers of the customer the user prompt is for. | HIGH |
| The requester cannot change the response rules or the system prompt; they belong to the model's time in service. | HIGH |
| When the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one. | HIGH |
| If the model cannot finish a response without breaking a rule, it gives no response; the user prompt is refused, and the record says which rule stopped it. | HIGH |
| A response that reaches its longest permitted length before it is finished is not released; the user prompt is refused, and the record says so. | HIGH |
| A withdrawn model may be placed in service again, which begins a new time in service with its system prompt and response rules set afresh. | HIGH |
| Several models may be in service at the same time. | HIGH |
| A model already in service cannot be placed in service again; staff withdraw it first. | HIGH |
| Each time in service has exactly one system prompt and one set of response rules. | HIGH |
| An authorized requester submits a user prompt on behalf of one customer. | HIGH |
| A user prompt carries the question and any supporting material, names the model, and states the most sensitive kind of information the question and its material contain. | HIGH |
| The requester must be permitted to act for the customer the user prompt is for. | HIGH |
| Deciding which requesters may act for which customers is the business's existing business and is not decided here. | HIGH |
| Naming a customer does not by itself give the requester access to that customer's accounts. | HIGH |
| Deciding which staff are authorized model staff is the business's existing business and is not decided here. | HIGH |
| What the model reads is exactly the question, the supporting material, and the system prompt of the model's time in service; nothing else reaches the model. | HIGH |
| A user prompt is refused before the model sees it when the model is not registered, the model is not in service, the user prompt contains a more sensitive kind of information than the model may read, or what the model would read is longer than the model can read at once. | HIGH |
| Every user prompt is recorded, whether responded to or refused. | HIGH |
| A user prompt record holds who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason the user prompt was refused. | HIGH |
| The record keeps what the model read, not only a summary or fingerprint of it. | HIGH |
| The business does not claim that a model response is true. | HIGH |
| The business claims only that a model response was written by the recorded model, from the recorded material, under the recorded rules. | HIGH |
| Until a real model is available, the business uses a test model. | HIGH |
| The test model deliberately tries to break the rules: it tries to write another customer's account number. | HIGH |
| In this release the test model does not respond from material it was not given; the business can show only that nothing else reached the model, and the record shows that. | HIGH |
| Catching a response made up from nothing needs the finished response, and belongs to the later review of finished responses. | HIGH |
| The same rules govern the test model, and its responses are recorded in the same way. | HIGH |
| Every business operation must be traceable and auditable. | HIGH |
| The business starts with no models registered. | HIGH |
| The operations required are: register a model, place a registered model in service with its system prompt and response rules, withdraw a model from service, retrieve the record of any user prompt, and submit a user prompt to a model in service on behalf of a customer. | HIGH |
| Retiring models, reviewing a model response after it is written, letting a model propose actions, replacing the model in service, and regulator reporting are excluded from this release. | HIGH |
| The excluded capabilities are expected to be introduced through future governed change requests. | HIGH |
| The excluded capabilities must not be designed into the initial solution. | HIGH |

## 5. Existing-System Beliefs — Requiring Verification

*Not facts. Each is a discovery target the agent must verify against the snapshot at P2.*

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal |
|--------|----------------|-------------------|
| causal_language_model is not part of the current software baseline. | The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different. | Confirm no artifact in the pinned composition carries the causal_language_model namespace. |
| No capability in the current composition registers language models or governs how a model writes a response. | This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension. | Confirm nothing in the composition registers a model, places one in service, or applies rules while a model writes. The ai_governance domain governs AI agents and licensing, and must be checked. |

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis |
|------------|-------|

## 7. Constraints

<!-- register:constraints business_language optional -->
| Constraint | Source |
|------------|--------|
| Capabilities deferred to future change requests must not be designed into this solution. | Business policy |
| Response rules apply while the model writes, not afterwards. | Business policy |
| Only authorized model staff may register a model, place it in service, withdraw it, or retrieve user prompt records. | Business policy |
| Only an authorized requester permitted to act for the customer may submit a user prompt on that customer's behalf. | Business policy |
| The requester cannot change the response rules or the system prompt. | Business policy |
| Nothing reaches the model except the question, the supporting material and the system prompt. | Business policy |
| A user prompt refused before the model sees it never reaches the model. | Business policy |
| The record keeps exactly what the model read, not only a summary or fingerprint of it. | Business policy |
| The business must not claim that a model response is true. | Business policy |
| Every business operation must leave a record that can be traced and audited. | Business policy |

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant |
|-----------|
| Each model the business holds has exactly one record. |
| No model responds to a user prompt unless it is registered and in service. |
| A model has at most one time in service at any moment. |
| Each time in service has exactly one system prompt and one set of response rules. |
| No model reads a more sensitive kind of information than its sensitivity ceiling. |
| No model reads anything but the question, the supporting material and its system prompt. |
| No model response is released that breaks a response rule. |
| No model response is released that reached the longest response before it was finished. |
| Every user prompt is recorded, whether responded to or refused. |
| Every refusal carries its reason. |
| Every business operation is traceable and auditable. |

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning |
|--------|-------|---------|
| Model | Registered | The business holds the model's record; it responds to no one. |
| Model | In Service | Authorized model staff have placed the model in service; it may respond to user prompts under its time in service's sensitivity ceiling, system prompt and response rules. |
| User Prompt | Responded | The model finished a response under the response rules, and the model response was released to the requester. |
| User Prompt | Refused | The user prompt yielded no model response; the record carries the reason. |

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance |
|-------|----------------|--------------|
| Model Registered | When authorized model staff register a model. | The business holds a record of the model. |
| Model Placed In Service | When authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules. | The model may respond to user prompts, and a time in service begins. |
| Model Withdrawn From Service | When authorized model staff withdraw a model from service. | The model responds to no one, and its time in service ends. |
| User Prompt Responded | When a model finishes a response under the response rules. | A model response is released, and its record shows what it was written from and under which rules. |
| User Prompt Refused | When a user prompt yields no model response. | The refusal and its reason are recorded. |

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner |
|-----------------|---------------------|
| Model record | Model Response |
| Time in service | Model Response |
| User prompt record | Model Response |
| The sensitivity ceiling, system prompt and response rules for a time in service | Authorized model staff |
| The kind of information a user prompt contains | The requester who states it |
| Which requesters may act for which customers | The business's existing business |
| Which staff are authorized model staff | The business's existing business |

## 12. Out of Scope

<!-- register:out_of_scope business_language -->
| Item | Reason |
|------|--------|
| Registry beyond what a model response needs | A project function; this change request includes only as much of the registry as a model response needs. |
| Retiring models | Declared excluded from this release; expected through a future governed change request. |
| Disclosure | A project function; reviewing a model response after it is written is declared excluded from this release. |
| Action | A project function; letting a model propose actions is declared excluded from this release. |
| Substitution | A project function; replacing the model in service is declared excluded from this release. |
| Reporting | A project function; regulator reporting is declared excluded from this release. |
| Rules that can only be judged once a response is finished | They belong to a later review of finished responses. |
| Catching a response made up from nothing | It needs the finished response, and belongs to the later review of finished responses. |
| Verifying how a model was trained | The training fingerprint is the provider's claim, recorded and not verified. |
| Deciding which requesters may act for which customers | The business's existing business. |
| Deciding which staff are authorized model staff | The business's existing business. |
| Claiming that a model response is true | The business claims only what the record shows. |

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) |
|------------|--------------|
| model_response | CREATED |
| registry | ADJACENT |
| disclosure | ADJACENT |
| action | ADJACENT |
| substitution | ADJACENT |
| reporting | ADJACENT |

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) |
|----------|------------|----------|-------|

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion |
|-----------|
| Authorized model staff can register a model with its description and training fingerprint, and the business then holds exactly one record for it. |
| A registration whose description and fingerprint match a registered model is refused, and the reason states that the model is already registered. |
| Authorized model staff can place a registered model in service with a sensitivity ceiling, system prompt and response rules. |
| Placing a model in service that is already in service is refused. |
| Authorized model staff can withdraw a model from service, after which it responds to no one. |
| A withdrawn model can be placed in service again, with a system prompt and response rules set afresh. |
| Several models can be in service at the same time. |
| An authorized requester can submit a user prompt to a model in service on behalf of a customer, and receives a model response written under the response rules. |
| A user prompt naming a model that is not registered is refused before the model sees it. |
| A user prompt naming a model that is not in service is refused before the model sees it. |
| A user prompt containing a more sensitive kind of information than the model may read is refused before the model sees it. |
| A user prompt whose question, material and system prompt together are longer than the model can read at once is refused before the model sees it. |
| A requester not permitted to act for the customer cannot submit a user prompt on that customer's behalf. |
| When the test model tries to write another customer's account number, that number is not written, and the response continues with permitted words. |
| When the model cannot finish a response without breaking a rule, the user prompt is refused, and the record names the rule that stopped it. |
| A response that reaches the longest response before it is finished is not released, and the record says so. |
| The requester cannot change the response rules or the system prompt. |
| Every user prompt, responded to or refused, has a record showing who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason for refusal. |
| Authorized model staff can retrieve the record of any user prompt. |
| Staff who are not authorized model staff cannot register a model, place one in service, withdraw one, or retrieve user prompt records. |
| Every business operation performed can be traced and audited afterwards. |

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When |
|-----------------|---------------|-----------------------|
| Model | Its description and its training fingerprint together. | Their descriptions and their training fingerprints both match. |

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade |
|--------|------------|----------|--------------|---------|
| Model | — | Registered | Authorized model staff register the model. | None. |
| Model | Registered | In Service | Authorized model staff place the model in service with its sensitivity ceiling, system prompt and response rules. | A time in service begins. |
| Model | In Service | Registered | Authorized model staff withdraw the model from service. | The time in service ends. |
| User Prompt | — | Responded | The model finishes a response under the response rules. | The user prompt record is written. |
| User Prompt | — | Refused | A refusal condition holds, before or while the model writes. | The user prompt record is written with the reason. |

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason |
|-----------|--------------|-----------------|
| Register a model | Its description and fingerprint match a registered model. | The model already has its record. |
| Place a model in service | The model is not registered. | Only a registered model may be placed in service. |
| Place a model in service | The model is already in service. | Each time in service has exactly one system prompt and set of response rules; staff withdraw the model first. |
| Withdraw a model from service | The model is not in service. | Only a model in service can be withdrawn. |
| Submit a user prompt | The model is not registered. | No model responds unless it is registered. |
| Submit a user prompt | The model is not in service. | A registered model responds to no one until it is placed in service. |
| Submit a user prompt | The user prompt contains a more sensitive kind of information than the model may read. | A model reads nothing above its sensitivity ceiling. |
| Submit a user prompt | What the model would read is longer than the model can read at once. | The model cannot read it. |
| Submit a user prompt | The requester is not permitted to act for the customer. | Naming a customer does not by itself give access to that customer's accounts. |
| Submit a user prompt | The model cannot finish a response without breaking a response rule. | No response that breaks a rule is released; the record names the rule. |
| Submit a user prompt | The response reaches the longest response before it is finished. | An unfinished response is not released. |
| Register a model, place in service, withdraw, retrieve a record | The staff member is not authorized model staff. | Only authorized model staff perform these operations. |

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until |
|-----------------|-------------|-------|
| Which requesters may act for which customers | The business's existing business | Not decided within this project. |
| Which staff are authorized model staff | The business's existing business | Not decided within this project. |

---

## gov_projection — Governed Handoff to Stage 1

| Direction | Fields |
|-----------|--------|
| **Consumes** ← human | business problem statement |
| **Emits** → Stage 1 | subdomain_purpose · cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
