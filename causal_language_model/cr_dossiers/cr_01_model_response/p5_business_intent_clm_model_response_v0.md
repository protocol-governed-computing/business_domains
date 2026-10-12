# Stage 5 — Business Intent: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p5
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

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
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: REFINED
    refinement: States the authority the subdomain establishes — a model responds because staff placed it in service, and a word is written because the rules permitted it — the lifecycle it manages, the single declared place where determinism ends, and what it does not decide.
  subdomain_purposes:
  - subdomain: model_response
    purpose: Governs which model may respond to a customer's question, under which rules, applying those rules to every word while the model writes, and records every user prompt with exactly what the model read and the outcome.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  scope_boundary:
  - capability: Register a model
    status: IN_SCOPE
    notes: Refused if the model is already registered
    source_finding: {phase: p4, register: authoring_scope, key: GAP-13}
  - capability: Place a model in service, and withdraw it
    status: IN_SCOPE
    notes: Placement refused if the model is not registered or already in service; withdrawal refused if it is not in service
    source_finding: {phase: p4, register: authoring_scope, key: GAP-14}
  - capability: Submit a user prompt and release or refuse the model response
    status: IN_SCOPE
    notes: Refused before the model sees it on four conditions, and while it writes on two
    source_finding: {phase: p4, register: authoring_scope, key: GAP-15}
  - capability: Retrieve a user prompt record
    status: IN_SCOPE
    notes: Recorded in the operation trail; raises no business event
    source_finding: {phase: p4, register: authoring_scope, key: GAP-16}
  - capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    status: IN_SCOPE
    notes: Each pass runs two declared steps, the model's offer and the rules' choice
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: Offer the model's next words, with a result not determined by its inputs
    status: IN_SCOPE
    notes: The single step declared as not deterministic
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    status: IN_SCOPE
    notes: Deterministic given the offered words, the rules and the seed
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Run a composed body once per pass of a transform's loop
    status: IN_SCOPE
    notes: Owned by the platform, which declares and runs it; reused
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: A test model that tries to write another customer's account number
    status: IN_SCOPE
    notes: A permanent realization of the model's step
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Retiring models
    status: DEFERRED
    notes: Declared excluded from this release
    source_finding: {phase: p4, register: authoring_scope, key: Retiring models}
  - capability: Reviewing a model response after it is written
    status: DEFERRED
    notes: The disclosure function
    source_finding: {phase: p4, register: authoring_scope, key: Disclosure}
  - capability: Letting a model propose actions
    status: DEFERRED
    notes: The action function
    source_finding: {phase: p4, register: authoring_scope, key: Action}
  - capability: Replacing the model in service
    status: DEFERRED
    notes: The substitution function
    source_finding: {phase: p4, register: authoring_scope, key: Substitution}
  - capability: Regulator reporting
    status: DEFERRED
    notes: The reporting function
    source_finding: {phase: p4, register: authoring_scope, key: Reporting}
  - capability: Catching a response made up from nothing
    status: DEFERRED
    notes: Needs the finished response
    source_finding: {phase: p4, register: authoring_scope, key: Catching a response made up from nothing}
  business_objects:
  - store_name: Model record
    record_model: MUTABLE_STATE
    business_rationale: The business holds one record per model, and a model moves into and out of service on the same record
    source_finding: {phase: p4, register: bm_entities, key: Model}
  - store_name: Model identity register
    record_model: IDENTITY_REGISTRY
    business_rationale: A second registration of the same model must be refused atomically
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - store_name: Time in service record
    record_model: MUTABLE_STATE
    business_rationale: A time in service is opened at placement and closed at withdrawal, on the same record
    source_finding: {phase: p4, register: bm_entities, key: Time in Service}
  - store_name: Time in service identity register
    record_model: IDENTITY_REGISTRY
    business_rationale: A time in service must never be opened twice under one identity, or a later placement would overwrite an earlier one
    source_finding: {phase: p4, register: bm_entities, key: Time in Service}
  - store_name: User prompt identity register
    record_model: IDENTITY_REGISTRY
    business_rationale: One user prompt identity must resolve to exactly one user prompt record
    source_finding: {phase: p4, register: bm_entities, key: User Prompt Record}
  - store_name: User prompt record
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every user prompt is recorded with exactly what the model read and its outcome, and a record that could be amended would not be evidence
    source_finding: {phase: p4, register: bm_entities, key: User Prompt Record}
  - store_name: Operation trail
    record_model: APPEND_ONLY_JOURNAL
    business_rationale: Every operation must be traceable afterwards
    source_finding: {phase: p4, register: resources, key: Operation trail}
  identity_semantics:
  - store_name: Model record
    identity_field: Description and training fingerprint together
    source: Supplied by model staff at registration; the fingerprint is the provider's claim
    uniqueness_rule: Two registrations whose descriptions and fingerprints both match describe the same model, and the second is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - store_name: Model identity register
    identity_field: The key formed from the description and fingerprint
    source: Formed at registration
    uniqueness_rule: One entry per model; a second claim of the same key is refused
    cross_subdomain_relationship: None
    source_finding: {phase: p4, register: design_decisions, row: 8}
  - store_name: Time in service record
    identity_field: The model and the moment it was placed in service
    source: Assigned at placement
    uniqueness_rule: At most one open time in service per model
    cross_subdomain_relationship: Names exactly one model record
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - store_name: Time in service identity register
    identity_field: The time in service's identity
    source: Claimed at placement, before the time in service is opened
    uniqueness_rule: One entry per time in service; a second claim of the same identity is refused
    cross_subdomain_relationship: Names exactly one time in service record
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - store_name: User prompt identity register
    identity_field: The user prompt's identity
    source: Named by the requester and claimed before anything else is done with the user prompt
    uniqueness_rule: One entry per user prompt; a second submission under the same identity is refused
    cross_subdomain_relationship: Names exactly one user prompt record
    source_finding: {phase: p4, register: bm_entities, key: User Prompt Record}
  - store_name: User prompt record
    identity_field: The user prompt's identity
    source: Claimed at submission
    uniqueness_rule: Each claimed user prompt appends at most one entry, and no entry is amended or removed
    cross_subdomain_relationship: Names one model and one time in service
    source_finding: {phase: p4, register: bm_entities, key: User Prompt Record}
  - store_name: Operation trail
    identity_field: Append position
    source: Assigned when the entry is appended
    uniqueness_rule: Each performed operation appends exactly one entry, and no entry is amended or removed
    cross_subdomain_relationship: Names the staff member or requester who performed the operation
    source_finding: {phase: p4, register: resources, key: Operation trail}
  invariants:
  - invariant: Each model the business holds has exactly one record
    business_reason: The business needs one place that says which models it holds
    source_finding: {phase: p4, register: constraint_register, row: 1}
  - invariant: No model responds to a user prompt unless it is registered and in service
    business_reason: Registration records a model; only placement authorizes it to respond
    source_finding: {phase: p4, register: constraint_register, row: 2}
  - invariant: A model has at most one time in service at any moment
    business_reason: A response must be attributable to exactly one set of rules
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - invariant: Each time in service has exactly one system prompt and one set of response rules
    business_reason: The rules a response was written under must be unambiguous
    source_finding: {phase: p4, register: constraint_register, row: 4}
  - invariant: No model reads a more sensitive kind of information than its sensitivity ceiling
    business_reason: The ceiling is what staff authorized the model to read
    source_finding: {phase: p4, register: constraint_register, row: 5}
  - invariant: No model reads anything but the question, the supporting material and its system prompt
    business_reason: The record must be able to say exactly what the model read
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - invariant: No model response is released that breaks a response rule
    business_reason: The rules apply while the model writes, so nothing forbidden is written
    source_finding: {phase: p4, register: constraint_register, row: 7}
  - invariant: No model response is released that reached the longest response before it was finished
    business_reason: An unfinished response is not a response
    source_finding: {phase: p4, register: constraint_register, row: 8}
  - invariant: Every user prompt is recorded, whether responded to or refused
    business_reason: A regulator asks about refusals as well as responses
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - invariant: Every refusal carries its reason
    business_reason: A refusal without a reason cannot be examined
    source_finding: {phase: p4, register: constraint_register, row: 10}
  - invariant: Every business operation is traceable and auditable
    business_reason: The business must be able to show what was done and by whom
    source_finding: {phase: p4, register: constraint_register, row: 11}
  - invariant: Each word's rule decision is a step governance can see
    business_reason: The rules must visibly act while the model writes
    source_finding: {phase: p4, register: constraint_register, row: 18}
  - invariant: Only the model's step gives results not determined by its inputs
    business_reason: A reader must see exactly where determinism ends
    source_finding: {phase: p4, register: constraint_register, row: 19}
  - invariant: The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly
    business_reason: A user prompt's trace must be reproducible from what was recorded
    source_finding: {phase: p4, register: constraint_register, row: 20}
  - invariant: Every word chosen more adventurously than the most likely one is drawn from a recorded seed
    business_reason: Anyone reading the record can re-derive each chosen word
    source_finding: {phase: p4, register: constraint_register, row: 21}
  actions:
  - action: Register
    object: Model
    trigger: Model staff record a model the business holds
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Register a model}
  - action: Place in service
    object: Model
    trigger: Model staff authorize a registered model to respond, under a sensitivity ceiling, system prompt and response rules
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Place a model in service, and withdraw it'}
  - action: Withdraw from service
    object: Model
    trigger: Model staff stop a model responding
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: 'Place a model in service, and withdraw it'}
  - action: Submit
    object: User prompt
    trigger: A requester asks a question on behalf of a customer
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Submit a user prompt and release or refuse the model response}
  - action: Retrieve
    object: User prompt record
    trigger: Model staff examine what happened to a user prompt
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Retrieve a user prompt record}
  - action: Retire
    object: Model
    trigger: Model staff judge a model no longer to be held
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Retiring models}
  - action: Review
    object: Model response
    trigger: A finished response is examined before release
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Disclosure}
  - action: Replace
    object: Model in service
    trigger: Staff substitute another model
    status: DEFERRED
    source_finding: {phase: p4, register: authoring_scope, key: Substitution}
  provisional_codes:
  - subdomain: model_response
    provisional_code: AC_MODEL_STAFF_V0
    family: AC
    summary: The authorized model staff member who registers, places, withdraws and retrieves
    source_finding: {phase: p4, register: actors, key: Authorized model staff}
  - subdomain: model_response
    provisional_code: AC_REQUESTER_V0
    family: AC
    summary: The authorized requester who submits a user prompt on behalf of a customer
    source_finding: {phase: p4, register: actors, key: Authorized requester}
  - subdomain: model_response
    provisional_code: IN_REGISTER_MODEL_V0
    family: IN
    summary: A request to register a model with its description and fingerprint
    source_finding: {phase: p5, register: actions, key: Register}
  - subdomain: model_response
    provisional_code: IN_PLACE_MODEL_IN_SERVICE_V0
    family: IN
    summary: A request to place a registered model in service with its ceiling, system prompt and response rules
    source_finding: {phase: p5, register: actions, key: Place in service}
  - subdomain: model_response
    provisional_code: IN_WITHDRAW_MODEL_FROM_SERVICE_V0
    family: IN
    summary: A request to withdraw a model from service
    source_finding: {phase: p5, register: actions, key: Withdraw from service}
  - subdomain: model_response
    provisional_code: IN_SUBMIT_USER_PROMPT_V0
    family: IN
    summary: A user prompt submitted on behalf of a customer
    source_finding: {phase: p5, register: actions, key: Submit}
  - subdomain: model_response
    provisional_code: IN_RETRIEVE_USER_PROMPT_RECORD_V0
    family: IN
    summary: A request to retrieve the record of a user prompt
    source_finding: {phase: p5, register: actions, key: Retrieve}
  - subdomain: model_response
    provisional_code: WF_REGISTER_MODEL_V0
    family: WF
    summary: Registering a model, refusing a second registration of the same model
    source_finding: {phase: p4, register: capability_graph, key: Register a model}
  - subdomain: model_response
    provisional_code: WF_PLACE_MODEL_IN_SERVICE_V0
    family: WF
    summary: Opening a time in service for a registered model not already in service
    source_finding: {phase: p4, register: capability_graph, key: 'Place a model in service, and withdraw it'}
  - subdomain: model_response
    provisional_code: WF_WITHDRAW_MODEL_FROM_SERVICE_V0
    family: WF
    summary: Closing a model's time in service
    source_finding: {phase: p4, register: capability_graph, key: 'Place a model in service, and withdraw it'}
  - subdomain: model_response
    provisional_code: WF_SUBMIT_USER_PROMPT_V0
    family: WF
    summary: Admitting a user prompt, writing the response under the rules, releasing or refusing it, and recording it
    source_finding: {phase: p4, register: capability_graph, key: Submit a user prompt and release or refuse the model response}
  - subdomain: model_response
    provisional_code: WF_RETRIEVE_USER_PROMPT_RECORD_V0
    family: WF
    summary: Reading a user prompt record and recording that it was read
    source_finding: {phase: p4, register: capability_graph, key: Retrieve a user prompt record}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_MODEL_STAFF_AUTHORIZED_V0
    family: CC
    summary: Confirm the staff member is model staff
    source_finding: {phase: p4, register: gap_register, key: GAP-12}
  - subdomain: model_response
    provisional_code: CC_CLAIM_USER_PROMPT_IDENTITY_V0
    family: CC
    summary: Claim a user prompt's identity so a second submission under it is refused
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    family: CC
    summary: Confirm the requester may act for the customer the user prompt is for
    source_finding: {phase: p4, register: gap_register, key: GAP-12}
  - subdomain: model_response
    provisional_code: CC_CLAIM_MODEL_IDENTITY_V0
    family: CC
    summary: Claim a model's identity so a second registration of the same model is refused
    source_finding: {phase: p4, register: gap_register, key: GAP-13}
  - subdomain: model_response
    provisional_code: CC_REGISTER_MODEL_V0
    family: CC
    summary: Record a model's description and fingerprint as its record, registered
    source_finding: {phase: p4, register: gap_register, key: GAP-13}
  - subdomain: model_response
    provisional_code: CC_PLACE_MODEL_IN_SERVICE_V0
    family: CC
    summary: Open a time in service with its ceiling, system prompt and response rules, and mark the model in service
    source_finding: {phase: p4, register: gap_register, key: GAP-14}
  - subdomain: model_response
    provisional_code: CC_WITHDRAW_MODEL_FROM_SERVICE_V0
    family: CC
    summary: Close the time in service and mark the model registered
    source_finding: {phase: p4, register: gap_register, key: GAP-14}
  - subdomain: model_response
    provisional_code: CC_ADMIT_USER_PROMPT_V0
    family: CC
    summary: Refuse a user prompt before the model sees it when its model is not registered or not in service
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_WITHIN_CEILING_V0
    family: CC
    summary: Refuse a user prompt before the model sees it when it states a kind more sensitive than the ceiling
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_READING_FITS_V0
    family: CC
    summary: Assemble exactly what the model reads and refuse it before the model sees it when it is too long
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_WRITE_MODEL_RESPONSE_V0
    family: CC
    summary: Write the response word by word under the rules in force
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_RESPONSE_RELEASABLE_V0
    family: CC
    summary: Release a written response only when it finished and no rule stopped it, refusing it with the rule or length that stopped it
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_RECORD_USER_PROMPT_V0
    family: CC
    summary: Append the user prompt record with what the model read, the rules in force and the outcome
    source_finding: {phase: p4, register: gap_register, key: GAP-15}
  - subdomain: model_response
    provisional_code: CC_RETRIEVE_USER_PROMPT_RECORD_V0
    family: CC
    summary: Read the record of a user prompt
    source_finding: {phase: p4, register: gap_register, key: GAP-16}
  - subdomain: model_response
    provisional_code: CC_APPEND_MODEL_OPERATION_V0
    family: CC
    summary: Append a durable account of a performed operation to the subdomain's own trail
    source_finding: {phase: p4, register: gap_register, key: GAP-17}
  - subdomain: model_response
    provisional_code: CT_PURE_FORM_MODEL_IDENTITY_KEY_V0
    family: CT
    summary: Forms the single key claimed for a model from its description and fingerprint
    source_finding: {phase: p4, register: gap_register, key: GAP-01}
  - subdomain: model_response
    provisional_code: CT_PURE_COMPARE_SENSITIVITY_V0
    family: CT
    summary: Decides whether a kind of information is no more sensitive than a ceiling, by the declared order
    source_finding: {phase: p4, register: gap_register, key: GAP-03}
  - subdomain: model_response
    provisional_code: CT_PURE_ASSEMBLE_MODEL_READING_V0
    family: CT
    summary: Assembles exactly what the model reads and decides whether it fits what the model can read at once
    source_finding: {phase: p4, register: gap_register, key: GAP-04}
  - subdomain: model_response
    provisional_code: CT_PURE_FORM_RESPONSE_RULES_V0
    family: CT
    summary: Forms the response rules in force for one user prompt from the time in service and the customer's account numbers
    source_finding: {phase: p4, register: gap_register, key: GAP-05}
  - subdomain: model_response
    provisional_code: CT_IMPURE_OFFER_NEXT_WORDS_V0
    family: CT
    summary: 'The model''s step: offers its next words given the response so far; the one step whose result is not determined by its inputs'
    source_finding: {phase: p4, register: gap_register, key: GAP-06}
  - subdomain: model_response
    provisional_code: CT_PURE_CHOOSE_PERMITTED_WORD_V0
    family: CT
    summary: Stops forbidden words among those offered and chooses one permitted word under the freedom of word choice and a stated seed
    source_finding: {phase: p4, register: gap_register, key: GAP-07}
  - subdomain: model_response
    provisional_code: CT_WRITE_NEXT_WORD_V0
    family: CT
    summary: One pass of writing, composed of the model's offer and the rules' choice
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - subdomain: model_response
    provisional_code: CT_WRITE_RESPONSE_V0
    family: CT
    summary: Writes a response by repeating one pass per word, up to the longest response, carrying the response so far and the words stopped
    source_finding: {phase: p4, register: gap_register, key: GAP-08}
  - subdomain: model_response
    provisional_code: EV_MODEL_REGISTERED_V0
    family: EV
    summary: The moment the business records a model
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - subdomain: model_response
    provisional_code: EV_MODEL_SERVICE_STARTED_V0
    family: EV
    summary: The moment a model is placed in service and a time in service begins
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - subdomain: model_response
    provisional_code: EV_MODEL_SERVICE_ENDED_V0
    family: EV
    summary: The moment a model is withdrawn from service and its time in service ends
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - subdomain: model_response
    provisional_code: EV_USER_PROMPT_RESPONDED_V0
    family: EV
    summary: The moment a model response is released
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - subdomain: model_response
    provisional_code: EV_USER_PROMPT_REFUSED_V0
    family: EV
    summary: The moment a user prompt yields no response
    source_finding: {phase: p4, register: gap_register, key: GAP-20}
  - subdomain: model_response
    provisional_code: VOCAB_KIND_OF_INFORMATION_V0
    family: VOCAB
    summary: 'The kinds of information, least sensitive first: public, internal, confidential, restricted'
    source_finding: {phase: p4, register: gap_register, key: GAP-02}
  - subdomain: model_response
    provisional_code: RB_MODEL_RESPONSE_BINDINGS_V0
    family: RB
    summary: Binds the subdomain's operations to the stores and mechanisms they use
    source_finding: {phase: p4, register: gap_register, key: GAP-18}
  - subdomain: model_response
    provisional_code: STRUCTURE_MODEL_RESPONSE_STORAGE_V0
    family: STRUCTURE
    summary: Declares the stores the subdomain owns and the paths they occupy
    source_finding: {phase: p4, register: gap_register, key: GAP-18}
  cross_subdomain_refs: null
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Business Invariants

---

## 6. Business Actions

---

## 7. Provisional Artifact Codes

---

## 8. Cross-Subdomain References

No capability contract from another subdomain is referenced. The subdomain reuses declared
mechanisms — durable records, uniqueness, append-only trails and four pure transforms — and composes
them itself. The test model is a realization, not a capability contract, and is carried to Stage 7.

---

## gov_projection — Governed Handoff to Stage 6

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 0, Stage 4 | subdomain_purpose · actors · bm_entities · resources · events · capability_graph · constraint_register · gap_register · design_decisions · authoring_scope |
| **Emits** → Stage 6 | subdomain_purpose · purpose_provenance · subdomain_purposes · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
