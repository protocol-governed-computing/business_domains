# Stage 1 — Change Request: Clarification & Fact Capture: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p1
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P1_V0
registers:
  cr_type:
  - subdomain: model_response
    classification: NEW_SUBDOMAIN
    rationale: causal_language_model is proposed as a new project, not part of the current software baseline, and the business requires model responses written under rules it cannot show today. It extends nothing that exists.
    source_finding: {phase: p0, register: cr_type, row: 1}
  business_vocabulary:
  - term: causal_language_model
    definition: The project governing a business's use of language models, across six functions of which model_response is the first.
    source_finding: {phase: p0, register: business_vocabulary, row: 1}
  - term: Business
    definition: An organization that uses a language model to respond to its customers' questions about their own accounts; a bank is one example.
    source_finding: {phase: p0, register: business_vocabulary, row: 2}
  - term: Language Model
    definition: A model that writes a response one word at a time, each word depending on the words before it. Its exact response cannot be predicted in advance, and given the same question twice it may respond differently.
    source_finding: {phase: p0, register: business_vocabulary, row: 3}
  - term: Model
    definition: A language model the business holds.
    source_finding: {phase: p0, register: business_vocabulary, row: 4}
  - term: Registration
    definition: The record of a model, describing how it is built and carrying its training fingerprint.
    source_finding: {phase: p0, register: business_vocabulary, row: 5}
  - term: Description
    definition: How a model is built, including the amount of text it can read at once.
    source_finding: {phase: p0, register: business_vocabulary, row: 6}
  - term: Training Fingerprint
    definition: A fingerprint of a model's training, supplied by whoever provided the model. It is the provider's claim; the business records it and does not verify how the model was trained.
    source_finding: {phase: p0, register: business_vocabulary, row: 7}
  - term: In Service
    definition: The condition of a registered model that authorized model staff have placed in service, and which may therefore respond to user prompts.
    source_finding: {phase: p0, register: business_vocabulary, row: 8}
  - term: Time in Service
    definition: One period during which a model is in service, from being placed in service to being withdrawn, with exactly one sensitivity ceiling, system prompt and set of response rules.
    source_finding: {phase: p0, register: business_vocabulary, row: 9}
  - term: Kind of Information
    definition: 'How sensitive information is: public, internal, confidential or restricted, from least to most sensitive.'
    source_finding: {phase: p0, register: business_vocabulary, row: 10}
  - term: Sensitivity Ceiling
    definition: The most sensitive kind of information a model in service may read.
    source_finding: {phase: p0, register: business_vocabulary, row: 11}
  - term: System Prompt
    definition: The business's standing instructions to a model, set for its time in service, which the model reads with every user prompt.
    source_finding: {phase: p0, register: business_vocabulary, row: 12}
  - term: Response Rules
    definition: 'The rules set for a model''s time in service that apply while it writes: words and patterns it must never write, how freely it may choose its words, and the longest response it may write.'
    source_finding: {phase: p0, register: business_vocabulary, row: 13}
  - term: Forbidden Words and Patterns
    definition: Words and patterns a model must never write, such as any account number other than the customer's own.
    source_finding: {phase: p0, register: business_vocabulary, row: 14}
  - term: Freedom of Word Choice
    definition: How freely a model may choose its words, from always choosing the most likely word to choosing more adventurously.
    source_finding: {phase: p0, register: business_vocabulary, row: 15}
  - term: Longest Response
    definition: The longest response a model may write during its time in service.
    source_finding: {phase: p0, register: business_vocabulary, row: 16}
  - term: User Prompt
    definition: 'What a requester submits on behalf of one customer: a question and any supporting material, naming the model, stating the most sensitive kind of information the question and its material contain, and carrying the customer''s account numbers.'
    source_finding: {phase: p0, register: business_vocabulary, row: 17}
  - term: Question
    definition: What the requester asks the model on the customer's behalf.
    source_finding: {phase: p0, register: business_vocabulary, row: 18}
  - term: Supporting Material
    definition: Material carried with a question for the model to read, such as the customer's recent transactions.
    source_finding: {phase: p0, register: business_vocabulary, row: 19}
  - term: Customer
    definition: The customer on whose behalf a user prompt is submitted, and whose own accounts the question is about.
    source_finding: {phase: p0, register: business_vocabulary, row: 20}
  - term: Account
    definition: An account a customer holds with the business, identified by its account number.
    source_finding: {phase: p0, register: business_vocabulary, row: 21}
  - term: Requester
    definition: A person who submits a user prompt on behalf of a customer.
    source_finding: {phase: p0, register: business_vocabulary, row: 22}
  - term: Authorized Requester
    definition: A requester permitted to act for the customer a user prompt is for.
    source_finding: {phase: p0, register: business_vocabulary, row: 23}
  - term: Authorized Model Staff
    definition: Staff of the business permitted to register models, place them in service, withdraw them, and retrieve user prompt records.
    source_finding: {phase: p0, register: business_vocabulary, row: 24}
  - term: Model Response
    definition: What a model writes in response to a user prompt, when it finishes under the response rules.
    source_finding: {phase: p0, register: business_vocabulary, row: 25}
  - term: Refusal
    definition: The outcome of a user prompt that yields no model response, carrying the reason.
    source_finding: {phase: p0, register: business_vocabulary, row: 26}
  - term: User Prompt Record
    definition: The record kept of every user prompt, responded to or refused.
    source_finding: {phase: p0, register: business_vocabulary, row: 27}
  - term: Test Model
    definition: A model the business uses until a real model is available, which deliberately tries to break the rules.
    source_finding: {phase: p0, register: business_vocabulary, row: 28}
  - term: Business Operation
    definition: An action performed that must be traceable and auditable.
    source_finding: {phase: p0, register: business_vocabulary, row: 29}
  requested_outcomes:
  - outcome: Model responses are written under rules that apply while the model writes, not afterwards.
    source_finding: {phase: p0, register: requested_outcomes, row: 1}
  - outcome: For any model response, the business can show a regulator which model wrote it, who asked, what the model was given to read, which rules applied while it wrote, and whether a response was refused and why.
    source_finding: {phase: p0, register: requested_outcomes, row: 2}
  - outcome: A model responds to no one until authorized model staff have registered it and placed it in service.
    source_finding: {phase: p0, register: requested_outcomes, row: 3}
  - outcome: Authorized model staff can register a model, place it in service with its system prompt and response rules, withdraw it from service, and retrieve the record of any user prompt.
    source_finding: {phase: p0, register: requested_outcomes, row: 4}
  - outcome: Authorized requesters can submit a user prompt to a model in service on behalf of a customer.
    source_finding: {phase: p0, register: requested_outcomes, row: 5}
  - outcome: The business can see the rules hold, using a test model that tries to break them, before a real model is trusted with them.
    source_finding: {phase: p0, register: requested_outcomes, row: 6}
  - outcome: Every business operation is traceable and auditable.
    source_finding: {phase: p0, register: requested_outcomes, row: 7}
  known_facts:
  - fact: The proposed name of the project is causal_language_model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 1}
  - fact: 'The project scope covers six functions: model_response, registry, disclosure, action, substitution, reporting.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 2}
  - fact: The scope of this change request is limited to the model_response function, and includes only as much of the registry as a model response needs.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 3}
  - fact: A business wants to use a language model to respond to its customers' questions about their own accounts; a bank is one example.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 4}
  - fact: A language model writes a response one word at a time, and each word depends on the words before it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 5}
  - fact: Nobody can predict a language model's exact response in advance; given the same question twice, it may respond differently.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 6}
  - fact: Today, staff paste customers' questions into a model and copy its response back.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 7}
  - fact: Today nobody can say afterwards which model responded, what it was shown, or whether anything stopped it from writing something it should not have written.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 8}
  - fact: A check made after a response is written can catch a problem only once the model has already produced it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 9}
  - fact: Before a model can respond to anything, authorized model staff register it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 10}
  - fact: A registration describes how the model is built, including the amount of text it can read at once, and carries a training fingerprint supplied by whoever provided the model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 11}
  - fact: Two registrations with the same description and the same fingerprint are the same model, and the business holds one record for it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 12}
  - fact: Registering a model that is already registered is refused, because the model already has its record.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 13}
  - fact: The training fingerprint is the provider's claim; the business records it and does not verify how the model was trained.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 14}
  - fact: A registered model does not respond to anyone until authorized model staff place it in service.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 15}
  - fact: When staff place a model in service, they state the most sensitive kind of information it may read, and set its system prompt and response rules.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 16}
  - fact: The kinds of information, from least to most sensitive, are public, internal, confidential and restricted.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 17}
  - fact: The system prompt is the business's standing instructions to the model, which it reads with every user prompt.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 18}
  - fact: 'The response rules are: words and patterns the model must never write, how freely it may choose its words, and the longest response it may write.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 19}
  - fact: A rule belongs to the response rules only if it can be applied while the model writes.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 20}
  - fact: A rule that can only be judged once a response is finished belongs to a later review of finished responses, which this release does not include.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 21}
  - fact: '"Another customer''s account number" depends on who the customer is; the rule is applied for each user prompt, using the account numbers of the customer the user prompt is for.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 22}
  - fact: The user prompt carries the account numbers of the customer it is for, taken from the business's existing records.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 23}
  - fact: The customer's account numbers are used to form the rule against another customer's account number, and reach the model only if they are also part of the supporting material.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 24}
  - fact: The requester cannot change the response rules or the system prompt; they belong to the model's time in service.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 25}
  - fact: When the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 26}
  - fact: If the model cannot finish a response without breaking a rule, it gives no response; the user prompt is refused, and the record says which rule stopped it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 27}
  - fact: A response that reaches its longest permitted length before it is finished is not released; the user prompt is refused, and the record says so.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 28}
  - fact: A withdrawn model may be placed in service again, which begins a new time in service with its system prompt and response rules set afresh.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 29}
  - fact: Several models may be in service at the same time.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 30}
  - fact: A model already in service cannot be placed in service again; staff withdraw it first.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 31}
  - fact: Each time in service has exactly one system prompt and one set of response rules.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 32}
  - fact: An authorized requester submits a user prompt on behalf of one customer.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 33}
  - fact: A user prompt carries the question and any supporting material, names the model, and states the most sensitive kind of information the question and its material contain.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 34}
  - fact: The requester must be permitted to act for the customer the user prompt is for.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 35}
  - fact: Deciding which requesters may act for which customers is the business's existing business and is not decided here.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 36}
  - fact: Naming a customer does not by itself give the requester access to that customer's accounts.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 37}
  - fact: Deciding which staff are authorized model staff is the business's existing business and is not decided here.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 38}
  - fact: What the model reads is exactly the question, the supporting material, and the system prompt of the model's time in service; nothing else reaches the model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 39}
  - fact: A user prompt is refused before the model sees it when the model is not registered, the model is not in service, the user prompt contains a more sensitive kind of information than the model may read, or what the model would read is longer than the model can read at once.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 40}
  - fact: Every user prompt is recorded, whether responded to or refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 41}
  - fact: A user prompt record holds who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason the user prompt was refused.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 42}
  - fact: The record keeps what the model read, not only a summary or fingerprint of it.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 43}
  - fact: The business does not claim that a model response is true.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 44}
  - fact: The business claims only that a model response was written by the recorded model, from the recorded material, under the recorded rules.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 45}
  - fact: Until a real model is available, the business uses a test model.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 46}
  - fact: 'The test model deliberately tries to break the rules: it tries to write another customer''s account number.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 47}
  - fact: In this release the test model does not respond from material it was not given; the business can show only that nothing else reached the model, and the record shows that.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 48}
  - fact: Catching a response made up from nothing needs the finished response, and belongs to the later review of finished responses.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 49}
  - fact: The same rules govern the test model, and its responses are recorded in the same way.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 50}
  - fact: Every business operation must be traceable and auditable.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 51}
  - fact: The business starts with no models registered.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 52}
  - fact: 'The operations required are: register a model, place a registered model in service with its system prompt and response rules, withdraw a model from service, retrieve the record of any user prompt, and submit a user prompt to a model in service on behalf of a customer.'
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 53}
  - fact: Retiring models, reviewing a model response after it is written, letting a model propose actions, replacing the model in service, and regulator reporting are excluded from this release.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 54}
  - fact: The excluded capabilities are expected to be introduced through future governed change requests.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 55}
  - fact: The excluded capabilities must not be designed into the initial solution.
    certainty: HIGH
    source_finding: {phase: p0, register: known_facts, row: 56}
  system_beliefs:
  - belief: causal_language_model is not part of the current software baseline.
    why_it_matters: The change is classified NEW_SUBDOMAIN on that basis; if the project already exists, this is an extension and its scope is different.
    verification_goal: Confirm no artifact in the pinned composition carries the causal_language_model namespace.
    source_finding: {phase: p0, register: system_beliefs, row: 1}
  - belief: No capability in the current composition registers language models or governs how a model writes a response.
    why_it_matters: This change exists to fill that gap; if such a capability exists, the change becomes a reuse or an extension.
    verification_goal: Confirm nothing in the composition registers a model, places one in service, or applies rules while a model writes. The ai_governance domain governs AI agents and licensing, and must be checked.
    source_finding: {phase: p0, register: system_beliefs, row: 2}
  assumptions: null
  constraints:
  - constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 1}
  - constraint: Response rules apply while the model writes, not afterwards.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 2}
  - constraint: Only authorized model staff may register a model, place it in service, withdraw it, or retrieve user prompt records.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 3}
  - constraint: Only an authorized requester permitted to act for the customer may submit a user prompt on that customer's behalf.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 4}
  - constraint: The requester cannot change the response rules or the system prompt.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 5}
  - constraint: Nothing reaches the model except the question, the supporting material and the system prompt.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 6}
  - constraint: A user prompt refused before the model sees it never reaches the model.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 7}
  - constraint: The record keeps exactly what the model read, not only a summary or fingerprint of it.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 8}
  - constraint: The business must not claim that a model response is true.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 9}
  - constraint: Every business operation must leave a record that can be traced and audited.
    source: Business policy
    source_finding: {phase: p0, register: constraints, row: 10}
  business_invariants:
  - invariant: Each model the business holds has exactly one record.
    source_finding: {phase: p0, register: business_invariants, row: 1}
  - invariant: No model responds to a user prompt unless it is registered and in service.
    source_finding: {phase: p0, register: business_invariants, row: 2}
  - invariant: A model has at most one time in service at any moment.
    source_finding: {phase: p0, register: business_invariants, row: 3}
  - invariant: Each time in service has exactly one system prompt and one set of response rules.
    source_finding: {phase: p0, register: business_invariants, row: 4}
  - invariant: No model reads a more sensitive kind of information than its sensitivity ceiling.
    source_finding: {phase: p0, register: business_invariants, row: 5}
  - invariant: No model reads anything but the question, the supporting material and its system prompt.
    source_finding: {phase: p0, register: business_invariants, row: 6}
  - invariant: No model response is released that breaks a response rule.
    source_finding: {phase: p0, register: business_invariants, row: 7}
  - invariant: No model response is released that reached the longest response before it was finished.
    source_finding: {phase: p0, register: business_invariants, row: 8}
  - invariant: Every user prompt is recorded, whether responded to or refused.
    source_finding: {phase: p0, register: business_invariants, row: 9}
  - invariant: Every refusal carries its reason.
    source_finding: {phase: p0, register: business_invariants, row: 10}
  - invariant: Every business operation is traceable and auditable.
    source_finding: {phase: p0, register: business_invariants, row: 11}
  lifecycle_states:
  - object: Model
    state: Registered
    meaning: The business holds the model's record; it responds to no one.
    source_finding: {phase: p0, register: lifecycle_states, row: 1}
  - object: Model
    state: In Service
    meaning: Authorized model staff have placed the model in service; it may respond to user prompts under its time in service's sensitivity ceiling, system prompt and response rules.
    source_finding: {phase: p0, register: lifecycle_states, row: 2}
  - object: User Prompt
    state: Responded
    meaning: The model finished a response under the response rules, and the model response was released to the requester.
    source_finding: {phase: p0, register: lifecycle_states, row: 3}
  - object: User Prompt
    state: Refused
    meaning: The user prompt yielded no model response; the record carries the reason.
    source_finding: {phase: p0, register: lifecycle_states, row: 4}
  business_events:
  - event: Model Registered
    when_it_occurs: When authorized model staff register a model.
    significance: The business holds a record of the model.
    source_finding: {phase: p0, register: business_events, row: 1}
  - event: Model Placed In Service
    when_it_occurs: When authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules.
    significance: The model may respond to user prompts, and a time in service begins.
    source_finding: {phase: p0, register: business_events, row: 2}
  - event: Model Withdrawn From Service
    when_it_occurs: When authorized model staff withdraw a model from service.
    significance: The model responds to no one, and its time in service ends.
    source_finding: {phase: p0, register: business_events, row: 3}
  - event: User Prompt Responded
    when_it_occurs: When a model finishes a response under the response rules.
    significance: A model response is released, and its record shows what it was written from and under which rules.
    source_finding: {phase: p0, register: business_events, row: 4}
  - event: User Prompt Refused
    when_it_occurs: When a user prompt yields no model response.
    significance: The refusal and its reason are recorded.
    source_finding: {phase: p0, register: business_events, row: 5}
  authority_boundaries:
  - business_object: Model record
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 1}
  - business_object: Time in service
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 2}
  - business_object: User prompt record
    authoritative_owner: Model Response
    source_finding: {phase: p0, register: authority_boundaries, row: 3}
  - business_object: The sensitivity ceiling, system prompt and response rules for a time in service
    authoritative_owner: Authorized model staff
    source_finding: {phase: p0, register: authority_boundaries, row: 4}
  - business_object: The kind of information a user prompt contains
    authoritative_owner: The requester who states it
    source_finding: {phase: p0, register: authority_boundaries, row: 5}
  - business_object: Which requesters may act for which customers
    authoritative_owner: The business's existing business
    source_finding: {phase: p0, register: authority_boundaries, row: 6}
  - business_object: Which staff are authorized model staff
    authoritative_owner: The business's existing business
    source_finding: {phase: p0, register: authority_boundaries, row: 7}
  out_of_scope:
  - item: Registry beyond what a model response needs
    reason: A project function; this change request includes only as much of the registry as a model response needs.
    source_finding: {phase: p0, register: out_of_scope, row: 1}
  - item: Retiring models
    reason: Declared excluded from this release; expected through a future governed change request.
    source_finding: {phase: p0, register: out_of_scope, row: 2}
  - item: Disclosure
    reason: A project function; reviewing a model response after it is written is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 3}
  - item: Action
    reason: A project function; letting a model propose actions is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 4}
  - item: Substitution
    reason: A project function; replacing the model in service is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 5}
  - item: Reporting
    reason: A project function; regulator reporting is declared excluded from this release.
    source_finding: {phase: p0, register: out_of_scope, row: 6}
  - item: Rules that can only be judged once a response is finished
    reason: They belong to a later review of finished responses.
    source_finding: {phase: p0, register: out_of_scope, row: 7}
  - item: Catching a response made up from nothing
    reason: It needs the finished response, and belongs to the later review of finished responses.
    source_finding: {phase: p0, register: out_of_scope, row: 8}
  - item: Verifying how a model was trained
    reason: The training fingerprint is the provider's claim, recorded and not verified.
    source_finding: {phase: p0, register: out_of_scope, row: 9}
  - item: Deciding which requesters may act for which customers
    reason: The business's existing business.
    source_finding: {phase: p0, register: out_of_scope, row: 10}
  - item: Deciding which staff are authorized model staff
    reason: The business's existing business.
    source_finding: {phase: p0, register: out_of_scope, row: 11}
  - item: Claiming that a model response is true
    reason: The business claims only what the record shows.
    source_finding: {phase: p0, register: out_of_scope, row: 12}
  governance_scope:
  - scope_item: model_response
    relationship: CREATED
    source_finding: {phase: p0, register: governance_scope, row: 1}
  - scope_item: registry
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 2}
  - scope_item: disclosure
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 3}
  - scope_item: action
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 4}
  - scope_item: substitution
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 5}
  - scope_item: reporting
    relationship: ADJACENT
    source_finding: {phase: p0, register: governance_scope, row: 6}
  clarification_requests: null
  acceptance_criteria:
  - criterion: Authorized model staff can register a model with its description and training fingerprint, and the business then holds exactly one record for it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 1}
  - criterion: A registration whose description and fingerprint match a registered model is refused, and the reason states that the model is already registered.
    source_finding: {phase: p0, register: acceptance_criteria, row: 2}
  - criterion: Authorized model staff can place a registered model in service with a sensitivity ceiling, system prompt and response rules.
    source_finding: {phase: p0, register: acceptance_criteria, row: 3}
  - criterion: Placing a model in service that is already in service is refused.
    source_finding: {phase: p0, register: acceptance_criteria, row: 4}
  - criterion: Authorized model staff can withdraw a model from service, after which it responds to no one.
    source_finding: {phase: p0, register: acceptance_criteria, row: 5}
  - criterion: A withdrawn model can be placed in service again, with a system prompt and response rules set afresh.
    source_finding: {phase: p0, register: acceptance_criteria, row: 6}
  - criterion: Several models can be in service at the same time.
    source_finding: {phase: p0, register: acceptance_criteria, row: 7}
  - criterion: An authorized requester can submit a user prompt to a model in service on behalf of a customer, and receives a model response written under the response rules.
    source_finding: {phase: p0, register: acceptance_criteria, row: 8}
  - criterion: A user prompt naming a model that is not registered is refused before the model sees it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 9}
  - criterion: A user prompt naming a model that is not in service is refused before the model sees it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 10}
  - criterion: A user prompt containing a more sensitive kind of information than the model may read is refused before the model sees it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 11}
  - criterion: A user prompt whose question, material and system prompt together are longer than the model can read at once is refused before the model sees it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 12}
  - criterion: A requester not permitted to act for the customer cannot submit a user prompt on that customer's behalf.
    source_finding: {phase: p0, register: acceptance_criteria, row: 13}
  - criterion: When the test model tries to write another customer's account number, that number is not written, and the response continues with permitted words.
    source_finding: {phase: p0, register: acceptance_criteria, row: 14}
  - criterion: When the model cannot finish a response without breaking a rule, the user prompt is refused, and the record names the rule that stopped it.
    source_finding: {phase: p0, register: acceptance_criteria, row: 15}
  - criterion: A response that reaches the longest response before it is finished is not released, and the record says so.
    source_finding: {phase: p0, register: acceptance_criteria, row: 16}
  - criterion: The requester cannot change the response rules or the system prompt.
    source_finding: {phase: p0, register: acceptance_criteria, row: 17}
  - criterion: Every user prompt, responded to or refused, has a record showing who asked and for which customer, which model and its time in service, exactly what the model read, the kind of information it contained, the response rules in force, and the model response or the reason for refusal.
    source_finding: {phase: p0, register: acceptance_criteria, row: 18}
  - criterion: Authorized model staff can retrieve the record of any user prompt.
    source_finding: {phase: p0, register: acceptance_criteria, row: 19}
  - criterion: Staff who are not authorized model staff cannot register a model, place one in service, withdraw one, or retrieve user prompt records.
    source_finding: {phase: p0, register: acceptance_criteria, row: 20}
  - criterion: Every business operation performed can be traced and audited afterwards.
    source_finding: {phase: p0, register: acceptance_criteria, row: 21}
  identity_and_sameness:
  - business_object: Model
    identified_by: Its description and its training fingerprint together.
    two_are_the_same_when: Their descriptions and their training fingerprints both match.
    source_finding: {phase: p0, register: identity_and_sameness, row: 1}
  lifecycle_transitions:
  - object: Model
    from_state: null
    to_state: Registered
    triggered_by: Authorized model staff register the model.
    cascade: None.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 1}
  - object: Model
    from_state: Registered
    to_state: In Service
    triggered_by: Authorized model staff place the model in service with its sensitivity ceiling, system prompt and response rules.
    cascade: A time in service begins.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 2}
  - object: Model
    from_state: In Service
    to_state: Registered
    triggered_by: Authorized model staff withdraw the model from service.
    cascade: The time in service ends.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 3}
  - object: User Prompt
    from_state: null
    to_state: Responded
    triggered_by: The model finishes a response under the response rules.
    cascade: The user prompt record is written.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 4}
  - object: User Prompt
    from_state: null
    to_state: Refused
    triggered_by: A refusal condition holds, before or while the model writes.
    cascade: The user prompt record is written with the reason.
    source_finding: {phase: p0, register: lifecycle_transitions, row: 5}
  operation_refusals:
  - operation: Register a model
    refused_when: Its description and fingerprint match a registered model.
    business_reason: The model already has its record.
    source_finding: {phase: p0, register: operation_refusals, row: 1}
  - operation: Place a model in service
    refused_when: The model is not registered.
    business_reason: Only a registered model may be placed in service.
    source_finding: {phase: p0, register: operation_refusals, row: 2}
  - operation: Place a model in service
    refused_when: The model is already in service.
    business_reason: Each time in service has exactly one system prompt and set of response rules; staff withdraw the model first.
    source_finding: {phase: p0, register: operation_refusals, row: 3}
  - operation: Withdraw a model from service
    refused_when: The model is not in service.
    business_reason: Only a model in service can be withdrawn.
    source_finding: {phase: p0, register: operation_refusals, row: 4}
  - operation: Submit a user prompt
    refused_when: The model is not registered.
    business_reason: No model responds unless it is registered.
    source_finding: {phase: p0, register: operation_refusals, row: 5}
  - operation: Submit a user prompt
    refused_when: The model is not in service.
    business_reason: A registered model responds to no one until it is placed in service.
    source_finding: {phase: p0, register: operation_refusals, row: 6}
  - operation: Submit a user prompt
    refused_when: The user prompt contains a more sensitive kind of information than the model may read.
    business_reason: A model reads nothing above its sensitivity ceiling.
    source_finding: {phase: p0, register: operation_refusals, row: 7}
  - operation: Submit a user prompt
    refused_when: What the model would read is longer than the model can read at once.
    business_reason: The model cannot read it.
    source_finding: {phase: p0, register: operation_refusals, row: 8}
  - operation: Submit a user prompt
    refused_when: The requester is not permitted to act for the customer.
    business_reason: Naming a customer does not by itself give access to that customer's accounts.
    source_finding: {phase: p0, register: operation_refusals, row: 9}
  - operation: Submit a user prompt
    refused_when: The model cannot finish a response without breaking a response rule.
    business_reason: No response that breaks a rule is released; the record names the rule.
    source_finding: {phase: p0, register: operation_refusals, row: 10}
  - operation: Submit a user prompt
    refused_when: The response reaches the longest response before it is finished.
    business_reason: An unfinished response is not released.
    source_finding: {phase: p0, register: operation_refusals, row: 11}
  - operation: Register a model, place in service, withdraw, retrieve a record
    refused_when: The staff member is not authorized model staff.
    business_reason: Only authorized model staff perform these operations.
    source_finding: {phase: p0, register: operation_refusals, row: 12}
  authority_deferrals:
  - business_object: Which requesters may act for which customers
    deferred_to: The business's existing business
    until: Not decided within this project.
    source_finding: {phase: p0, register: authority_deferrals, row: 1}
  - business_object: Which staff are authorized model staff
    deferred_to: The business's existing business
    until: Not decided within this project.
    source_finding: {phase: p0, register: authority_deferrals, row: 2}
```

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

---

## 2. Business Vocabulary

---

## 3. Requested Outcomes

---

## 4. Known Facts — Business Truths

---

## 5. Existing-System Beliefs — Requiring Verification

---

## 6. Assumptions

---

## 7. Constraints

---

## 8. Business Invariants

---

## 9. Lifecycle States

---

## 10. Business Events

---

## 11. Authority Boundaries

---

## 12. Out of Scope

---

## 13. Governance Scope

---

## 14. Clarification Requests

---

## 15. Acceptance Criteria

---

## 16. Identity and Sameness

---

## 17. Lifecycle Transitions

---

## 18. Operation Refusals

---

## 19. Authority Deferrals

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
