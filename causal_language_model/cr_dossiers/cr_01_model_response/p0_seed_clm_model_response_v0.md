# Change Seed — causal_language_model / model_response

## Machine

```yaml
document:
  phase: p0
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P0_V0
registers:
  subdomain_purpose: |2

    The Model Response subdomain governs how a business's language model responds to a customer's
    question about the customer's own accounts: under rules that apply while the model writes, not
    afterwards, and with a record that shows for every model response which model wrote it, who asked,
    what the model was given to read, which rules applied, and whether the response was refused and
    why. It exists because staff today paste customers' questions into a model and copy its response
    back, and nobody can say afterwards which model responded, what it was shown, or whether anything
    stopped it from writing something it should not have written. It is the first of six functions the
    causal_language_model project will govern. It carries only as much of the registry as a model
    response needs, and it governs none of the remaining functions.
  cr_type:
  - subdomain: model_response
    classification: NEW_SUBDOMAIN
    rationale: causal_language_model is proposed as a new project, not part of the current software baseline, and the business requires model responses written under rules it cannot show today. It extends nothing that exists.
  business_vocabulary:
  - term: causal_language_model
    definition: The project governing a business's use of language models, across six functions of which model_response is the first.
  - term: Business
    definition: An organization that uses a language model to respond to its customers' questions about their own accounts; a bank is one example.
  - term: Language Model
    definition: A model that writes a response one word at a time, each word depending on the words before it. Its exact response cannot be predicted in advance, and given the same question twice it may respond differently.
  - term: Model
    definition: A language model the business holds.
  - term: Registration
    definition: The record of a model, describing how it is built and carrying its training fingerprint.
  - term: Description
    definition: How a model is built, including the amount of text it can read at once.
  - term: Training Fingerprint
    definition: A fingerprint of a model's training, supplied by whoever provided the model. It is the provider's claim; the business records it and does not verify how the model was trained.
  - term: In Service
    definition: The condition of a registered model that authorized model staff have placed in service, and which may therefore respond to user prompts.
  - term: Time in Service
    definition: One period during which a model is in service, from being placed in service to being withdrawn, with exactly one sensitivity ceiling, system prompt and set of response rules.
  - term: Kind of Information
    definition: 'How sensitive information is: public, internal, confidential or restricted, from least to most sensitive.'
  - term: Sensitivity Ceiling
    definition: The most sensitive kind of information a model in service may read.
  - term: System Prompt
    definition: The business's standing instructions to a model, set for its time in service, which the model reads with every user prompt.
  - term: Response Rules
    definition: 'The rules set for a model''s time in service that apply while it writes: words and patterns it must never write, how freely it may choose its words, and the longest response it may write.'
  - term: Forbidden Words and Patterns
    definition: Words and patterns a model must never write, such as any account number other than the customer's own.
  - term: Freedom of Word Choice
    definition: How freely a model may choose its words, from always choosing the most likely word to choosing more adventurously.
  - term: Longest Response
    definition: The longest response a model may write during its time in service.
  - term: User Prompt
    definition: 'What a requester submits on behalf of one customer: a question and any supporting material, naming the model, stating the most sensitive kind of information the question and its material contain, and carrying the customer''s account numbers.'
  - term: Question
    definition: What the requester asks the model on the customer's behalf.
  - term: Supporting Material
    definition: Material carried with a question for the model to read, such as the customer's recent transactions.
  - term: Customer
    definition: The customer on whose behalf a user prompt is submitted, and whose own accounts the question is about.
  - term: Account
    definition: An account a customer holds with the business, identified by its account number.
  - term: Requester
    definition: A person who submits a user prompt on behalf of a customer.
  - term: Authorized Requester
    definition: A requester permitted to act for the customer a user prompt is for.
  - term: Authorized Model Staff
    definition: Staff of the business permitted to register models, place them in service, withdraw them, and retrieve user prompt records.
  - term: Model Response
    definition: What a model writes in response to a user prompt, when it finishes under the response rules.
  - term: Refusal
    definition: The outcome of a user prompt that yields no model response, carrying the reason.
  - term: User Prompt Record
    definition: The record kept of every user prompt, responded to or refused.
  - term: Test Model
    definition: A model the business uses until a real model is available, which deliberately tries to break the rules.
  - term: Business Operation
    definition: An action performed that must be traceable and auditable.
  requested_outcomes:
  - outcome: Model responses are written under rules that apply while the model writes, not afterwards.
  - outcome: For any model response, the business can show a regulator which model wrote it, who asked, what the model was given to read, which rules applied while it wrote, and whether a response was refused and why.
  - outcome: A model responds to no one until authorized model staff have registered it and placed it in service.
  - outcome: Authorized model staff can register a model, place it in service with its system prompt and response rules, withdraw it from service, and retrieve the record of any user prompt.
  - outcome: Authorized requesters can submit a user prompt to a model in service on behalf of a customer.
  - outcome: The business can see the rules hold, using a test model that tries to break them, before a real model is trusted with them.
  - outcome: Every business operation is traceable and auditable.
  known_facts:
  - fact: The proposed name of the project is causal_language_model.
    certainty: HIGH
  - fact: 'The project scope covers six functions: model_response, registry, disclosure, action, substitution, reporting.'
    certainty: HIGH
  - fact: The scope of this change request is limited to the model_response function, and includes only as much of the registry as a model response needs.
    certainty: HIGH
  - fact: A business wants to use a language model to respond to its customers' questions about their own accounts; a bank is one example.
    certainty: HIGH
  - fact: A language model writes a response one word at a time, and each word depends on the words before it.
    certainty: HIGH
  - fact: Nobody can predict a language model's exact response in advance; given the same question twice, it may respond differently.
    certainty: HIGH
  - fact: Today, staff paste customers' questions into a model and copy its response back.
    certainty: HIGH
  - fact: Today nobody can say afterwards which model responded, what it was shown, or whether anything stopped it from writing something it should not have written.
    certainty: HIGH
  - fact: A check made after a response is written can catch a problem only once the model has already produced it.
    certainty: HIGH
  - fact: Before a model can respond to anything, authorized model staff register it.
    certainty: HIGH
  - fact: A registration describes how the model is built, including the amount of text it can read at once, and carries a training fingerprint supplied by whoever provided the model.
    certainty: HIGH
  - fact: Two registrations with the same description and the same fingerprint are the same model, and the business holds one record for it.
    certainty: HIGH
  - fact: Registering a model that is already registered is refused, because the model already has its record.
    certainty: HIGH
  - fact: The training fingerprint is the provider's claim; the business records it and does not verify how the model was trained.
    certainty: HIGH
  - fact: A registered model does not respond to anyone until authorized model staff place it in service.
    certainty: HIGH
  - fact: When staff place a model in service, they state the most sensitive kind of information it may read, and set its system prompt and response rules.
    certainty: HIGH
  - fact: The kinds of information, from least to most sensitive, are public, internal, confidential and restricted.
    certainty: HIGH
  - fact: The system prompt is the business's standing instructions to the model, which it reads with every user prompt.
    certainty: HIGH
  - fact: 'The response rules are: words and patterns the model must never write, how freely it may choose its words, and the longest response it may write.'
    certainty: HIGH
  - fact: A rule belongs to the response rules only if it can be applied while the model writes.
    certainty: HIGH
  - fact: A rule that can only be judged once a response is finished belongs to a later review of finished responses, which this release does not include.
    certainty: HIGH
  - fact: '"Another customer''s account number" depends on who the customer is; the rule is applied for each user prompt, using the account numbers of the customer the user prompt is for.'
    certainty: HIGH
  - fact: The user prompt carries the account numbers of the customer it is for, taken from the business's existing records.
    certainty: HIGH
  - fact: The customer's account numbers are used to form the rule against another customer's account number, and reach the model only if they are also part of the supporting material.
    certainty: HIGH
  - fact: The requester cannot change the response rules or the system prompt; they belong to the model's time in service.
    certainty: HIGH
  - fact: When the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one.
    certainty: HIGH
  - fact: If the model cannot finish a response without breaking a rule, it gives no response; the user prompt is refused, and the record says which rule stopped it.
    certainty: HIGH
  - fact: A response that reaches its longest permitted length before it is finished is not released; the user prompt is refused, and the record says so.
    certainty: HIGH
  - fact: A withdrawn model may be placed in service again, which begins a new time in service with its system prompt and response rules set afresh.
    certainty: HIGH
  - fact: Several models may be in service at the same time.
    certainty: HIGH
  - fact: A model already in service cannot be placed in service again; staff withdraw it first.
    certainty: HIGH
  - fact: Each time in service has exactly one system prompt and one set of response rules.
    certainty: HIGH
  - fact: An authorized requester submits a user prompt on behalf of one customer.
    certainty: HIGH
  - fact: A user prompt carries the question and any supporting material, names the model, and states the most sensitive kind of information the question and its material contain.
    certainty: HIGH
  - fact: The requester must be permitted to act for the customer the user prompt is for.
    certainty: HIGH
  - fact: Deciding which requesters may act for which customers is the business's existing business and is not decided here.
    certainty: HIGH
  - fact: Naming a customer does not by itself give the requester access to that customer's accounts.
    certainty: HIGH
  - fact: Deciding which staff are authorized model staff is the business's existing business and is not decided here.
    certainty: HIGH
  - fact: What the model reads is exactly the question, the supporting material, and the system prompt of the model's time in service; nothing else reaches the model.
    certainty: HIGH
  - fact: A user prompt is refused before the model sees it when the model is not registered, the model is not in service, the user prompt contains a more sensitive kind of information than the model may read, or what the model would read is longer than the model can read at once.
    certainty: HIGH
  - fact: Every user prompt is recorded, whether responded to or refused.
    certainty: HIGH
  - fact: A user prompt record holds who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason the user prompt was refused.
    certainty: HIGH
  - fact: The record keeps what the model read, not only a summary or fingerprint of it.
    certainty: HIGH
  - fact: The business does not claim that a model response is true.
    certainty: HIGH
  - fact: The business claims only that a model response was written by the recorded model, from the recorded material, under the recorded rules.
    certainty: HIGH
  - fact: Until a real model is available, the business uses a test model.
    certainty: HIGH
  - fact: 'The test model deliberately tries to break the rules: it tries to write another customer''s account number.'
    certainty: HIGH
  - fact: In this release the test model does not respond from material it was not given; the business can show only that nothing else reached the model, and the record shows that.
    certainty: HIGH
  - fact: Catching a response made up from nothing needs the finished response, and belongs to the later review of finished responses.
    certainty: HIGH
  - fact: The same rules govern the test model, and its responses are recorded in the same way.
    certainty: HIGH
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
  - fact: The business starts with no models registered.
    certainty: HIGH
  - fact: 'The operations required are: register a model, place a registered model in service with its system prompt and response rules, withdraw a model from service, retrieve the record of any user prompt, and submit a user prompt to a model in service on behalf of a customer.'
    certainty: HIGH
  - fact: Retiring models, reviewing a model response after it is written, letting a model propose actions, replacing the model in service, and regulator reporting are excluded from this release.
    certainty: HIGH
  - fact: The excluded capabilities are expected to be introduced through future governed change requests.
    certainty: HIGH
  - fact: The excluded capabilities must not be designed into the initial solution.
    certainty: HIGH
  system_beliefs:
  - belief: causal_language_model is not part of the current software baseline.
    why_it_matters: The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different.
    verification_goal: Confirm no artifact in the pinned composition carries the causal_language_model namespace.
  - belief: No capability in the current composition registers language models or governs how a model writes a response.
    why_it_matters: This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension.
    verification_goal: Confirm nothing in the composition registers a model, places one in service, or applies rules while a model writes. The ai_governance domain governs AI agents and licensing, and must be checked.
  assumptions: null
  constraints:
  - constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source: Business policy
  - constraint: Response rules apply while the model writes, not afterwards.
    source: Business policy
  - constraint: Only authorized model staff may register a model, place it in service, withdraw it, or retrieve user prompt records.
    source: Business policy
  - constraint: Only an authorized requester permitted to act for the customer may submit a user prompt on that customer's behalf.
    source: Business policy
  - constraint: The requester cannot change the response rules or the system prompt.
    source: Business policy
  - constraint: Nothing reaches the model except the question, the supporting material and the system prompt.
    source: Business policy
  - constraint: A user prompt refused before the model sees it never reaches the model.
    source: Business policy
  - constraint: The record keeps exactly what the model read, not only a summary or fingerprint of it.
    source: Business policy
  - constraint: The business must not claim that a model response is true.
    source: Business policy
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
  business_invariants:
  - invariant: Each model the business holds has exactly one record.
  - invariant: No model responds to a user prompt unless it is registered and in service.
  - invariant: A model has at most one time in service at any moment.
  - invariant: Each time in service has exactly one system prompt and one set of response rules.
  - invariant: No model reads a more sensitive kind of information than its sensitivity ceiling.
  - invariant: No model reads anything but the question, the supporting material and its system prompt.
  - invariant: No model response is released that breaks a response rule.
  - invariant: No model response is released that reached the longest response before it was finished.
  - invariant: Every user prompt is recorded, whether responded to or refused.
  - invariant: Every refusal carries its reason.
  - invariant: Every business operation is traceable and auditable.
  lifecycle_states:
  - object: Model
    state: Registered
    meaning: The business holds the model's record; it responds to no one.
  - object: Model
    state: In Service
    meaning: Authorized model staff have placed the model in service; it may respond to user prompts under its time in service's sensitivity ceiling, system prompt and response rules.
  - object: User Prompt
    state: Responded
    meaning: The model finished a response under the response rules, and the model response was released to the requester.
  - object: User Prompt
    state: Refused
    meaning: The user prompt yielded no model response; the record carries the reason.
  business_events:
  - event: Model Registered
    when_it_occurs: When authorized model staff register a model.
    significance: The business holds a record of the model.
  - event: Model Placed In Service
    when_it_occurs: When authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules.
    significance: The model may respond to user prompts, and a time in service begins.
  - event: Model Withdrawn From Service
    when_it_occurs: When authorized model staff withdraw a model from service.
    significance: The model responds to no one, and its time in service ends.
  - event: User Prompt Responded
    when_it_occurs: When a model finishes a response under the response rules.
    significance: A model response is released, and its record shows what it was written from and under which rules.
  - event: User Prompt Refused
    when_it_occurs: When a user prompt yields no model response.
    significance: The refusal and its reason are recorded.
  authority_boundaries:
  - business_object: Model record
    authoritative_owner: Model Response
  - business_object: Time in service
    authoritative_owner: Model Response
  - business_object: User prompt record
    authoritative_owner: Model Response
  - business_object: The sensitivity ceiling, system prompt and response rules for a time in service
    authoritative_owner: Authorized model staff
  - business_object: The kind of information a user prompt contains
    authoritative_owner: The requester who states it
  - business_object: Which requesters may act for which customers
    authoritative_owner: The business's existing business
  - business_object: Which staff are authorized model staff
    authoritative_owner: The business's existing business
  out_of_scope:
  - item: Registry beyond what a model response needs
    reason: A project function; this change request includes only as much of the registry as a model response needs.
  - item: Retiring models
    reason: Declared excluded from this release; expected through a future governed change request.
  - item: Disclosure
    reason: A project function; reviewing a model response after it is written is declared excluded from this release.
  - item: Action
    reason: A project function; letting a model propose actions is declared excluded from this release.
  - item: Substitution
    reason: A project function; replacing the model in service is declared excluded from this release.
  - item: Reporting
    reason: A project function; regulator reporting is declared excluded from this release.
  - item: Rules that can only be judged once a response is finished
    reason: They belong to a later review of finished responses.
  - item: Catching a response made up from nothing
    reason: It needs the finished response, and belongs to the later review of finished responses.
  - item: Verifying how a model was trained
    reason: The training fingerprint is the provider's claim, recorded and not verified.
  - item: Deciding which requesters may act for which customers
    reason: The business's existing business.
  - item: Deciding which staff are authorized model staff
    reason: The business's existing business.
  - item: Claiming that a model response is true
    reason: The business claims only what the record shows.
  governance_scope:
  - scope_item: model_response
    relationship: CREATED
  - scope_item: registry
    relationship: ADJACENT
  - scope_item: disclosure
    relationship: ADJACENT
  - scope_item: action
    relationship: ADJACENT
  - scope_item: substitution
    relationship: ADJACENT
  - scope_item: reporting
    relationship: ADJACENT
  clarification_requests: null
  acceptance_criteria:
  - criterion: Authorized model staff can register a model with its description and training fingerprint, and the business then holds exactly one record for it.
  - criterion: A registration whose description and fingerprint match a registered model is refused, and the reason states that the model is already registered.
  - criterion: Authorized model staff can place a registered model in service with a sensitivity ceiling, system prompt and response rules.
  - criterion: Placing a model in service that is already in service is refused.
  - criterion: Authorized model staff can withdraw a model from service, after which it responds to no one.
  - criterion: A withdrawn model can be placed in service again, with a system prompt and response rules set afresh.
  - criterion: Several models can be in service at the same time.
  - criterion: An authorized requester can submit a user prompt to a model in service on behalf of a customer, and receives a model response written under the response rules.
  - criterion: A user prompt naming a model that is not registered is refused before the model sees it.
  - criterion: A user prompt naming a model that is not in service is refused before the model sees it.
  - criterion: A user prompt containing a more sensitive kind of information than the model may read is refused before the model sees it.
  - criterion: A user prompt whose question, material and system prompt together are longer than the model can read at once is refused before the model sees it.
  - criterion: A requester not permitted to act for the customer cannot submit a user prompt on that customer's behalf.
  - criterion: When the test model tries to write another customer's account number, that number is not written, and the response continues with permitted words.
  - criterion: When the model cannot finish a response without breaking a rule, the user prompt is refused, and the record names the rule that stopped it.
  - criterion: A response that reaches the longest response before it is finished is not released, and the record says so.
  - criterion: The requester cannot change the response rules or the system prompt.
  - criterion: Every user prompt, responded to or refused, has a record showing who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason for refusal.
  - criterion: Authorized model staff can retrieve the record of any user prompt.
  - criterion: Staff who are not authorized model staff cannot register a model, place one in service, withdraw one, or retrieve user prompt records.
  - criterion: Every business operation performed can be traced and audited afterwards.
  identity_and_sameness:
  - business_object: Model
    identified_by: Its description and its training fingerprint together.
    two_are_the_same_when: Their descriptions and their training fingerprints both match.
  lifecycle_transitions:
  - object: Model
    from_state: null
    to_state: Registered
    triggered_by: Authorized model staff register the model.
    cascade: None.
  - object: Model
    from_state: Registered
    to_state: In Service
    triggered_by: Authorized model staff place the model in service with its sensitivity ceiling, system prompt and response rules.
    cascade: A time in service begins.
  - object: Model
    from_state: In Service
    to_state: Registered
    triggered_by: Authorized model staff withdraw the model from service.
    cascade: The time in service ends.
  - object: User Prompt
    from_state: null
    to_state: Responded
    triggered_by: The model finishes a response under the response rules.
    cascade: The user prompt record is written.
  - object: User Prompt
    from_state: null
    to_state: Refused
    triggered_by: A refusal condition holds, before or while the model writes.
    cascade: The user prompt record is written with the reason.
  operation_refusals:
  - operation: Register a model
    refused_when: Its description and fingerprint match a registered model.
    business_reason: The model already has its record.
  - operation: Place a model in service
    refused_when: The model is not registered.
    business_reason: Only a registered model may be placed in service.
  - operation: Place a model in service
    refused_when: The model is already in service.
    business_reason: Each time in service has exactly one system prompt and set of response rules; staff withdraw the model first.
  - operation: Withdraw a model from service
    refused_when: The model is not in service.
    business_reason: Only a model in service can be withdrawn.
  - operation: Submit a user prompt
    refused_when: The model is not registered.
    business_reason: No model responds unless it is registered.
  - operation: Submit a user prompt
    refused_when: The model is not in service.
    business_reason: A registered model responds to no one until it is placed in service.
  - operation: Submit a user prompt
    refused_when: The user prompt contains a more sensitive kind of information than the model may read.
    business_reason: A model reads nothing above its sensitivity ceiling.
  - operation: Submit a user prompt
    refused_when: What the model would read is longer than the model can read at once.
    business_reason: The model cannot read it.
  - operation: Submit a user prompt
    refused_when: The requester is not permitted to act for the customer.
    business_reason: Naming a customer does not by itself give access to that customer's accounts.
  - operation: Submit a user prompt
    refused_when: The model cannot finish a response without breaking a response rule.
    business_reason: No response that breaks a rule is released; the record names the rule.
  - operation: Submit a user prompt
    refused_when: The response reaches the longest response before it is finished.
    business_reason: An unfinished response is not released.
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    business_reason: Only authorized model staff perform these operations.
  authority_deferrals:
  - business_object: Which requesters may act for which customers
    deferred_to: The business's existing business
    until: Not decided within this project.
  - business_object: Which staff are authorized model staff
    deferred_to: The business's existing business
    until: Not decided within this project.
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
