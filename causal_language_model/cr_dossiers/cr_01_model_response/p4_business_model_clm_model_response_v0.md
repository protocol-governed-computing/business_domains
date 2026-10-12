# Stage 4 — Business Model: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p4
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Authorized model staff
    role: Registers models, places them in service with their sensitivity ceiling, system prompt and response rules, withdraws them, and retrieves user prompt records
    authority_class: Operator
    source_finding: {phase: p1, register: authority_boundaries, key: 'The sensitivity ceiling, system prompt and response rules for a time in service'}
  - actor: Authorized requester
    role: Submits a user prompt on behalf of one customer, and states the kind of information it contains
    authority_class: Operator
    source_finding: {phase: p1, register: authority_boundaries, key: The kind of information a user prompt contains}
  - actor: Customer
    role: The person on whose behalf a user prompt is submitted, and whose own accounts the question is about
    authority_class: Beneficiary
    source_finding: {phase: p1, register: business_vocabulary, key: Customer}
  - actor: Model provider
    role: Supplies a model and asserts its training fingerprint, which the business records and does not verify
    authority_class: Claimant
    source_finding: {phase: p1, register: known_facts, key: the training fingerprint is the provider's claim}
  - actor: The business's existing arrangements
    role: Decide which requesters may act for which customers, and which staff are model staff; not part of this change
    authority_class: Deferred authority
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  bm_entities:
  - entity: Model
    description: A language model the business holds, identified by its description and training fingerprint together
    store_model: One durable record per model, addressed by its description and fingerprint together, never duplicated, carrying its own state
    source_finding: {phase: p2, register: entities, key: Model}
  - entity: Time in Service
    description: One period during which a model is in service, with exactly one sensitivity ceiling, system prompt and set of response rules
    store_model: One durable record per period, naming the one model it belongs to, open until the model is withdrawn; at most one open per model
    source_finding: {phase: p2, register: entities, key: Time in Service}
  - entity: User Prompt Record
    description: The record kept of every user prompt, responded to or refused
    store_model: An append-only trail, one entry per user prompt, never rewritten
    source_finding: {phase: p2, register: entities, key: User Prompt Record}
  resources:
  - resource: Model records
    description: The business's single record of every model it holds
    source_finding: {phase: p2, register: entities, key: Model}
  - resource: Times in service
    description: The record of every period a model was in service, with the rules it was under
    source_finding: {phase: p2, register: entities, key: Time in Service}
  - resource: User prompt records
    description: The complete record of every user prompt, what the model read, the rules in force and the outcome
    source_finding: {phase: p2, register: entities, key: User Prompt Record}
  - resource: Operation trail
    description: The subdomain's own durable record of every operation performed
    source_finding: {phase: p3, register: authoring_decisions, key: Record each performed operation in the subdomain's own trail}
  events:
  - event: Model registered
    trigger: Authorized model staff register a model
    lifecycle_meaning: The business holds a record of the model
    source_finding: {phase: p1, register: business_events, key: Model Registered}
  - event: Model placed in service
    trigger: Authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules
    lifecycle_meaning: A time in service begins, and the model may respond
    source_finding: {phase: p1, register: business_events, key: Model Placed In Service}
  - event: Model withdrawn from service
    trigger: Authorized model staff withdraw a model from service
    lifecycle_meaning: The time in service ends, and the model responds to no one
    source_finding: {phase: p1, register: business_events, key: Model Withdrawn From Service}
  - event: User prompt responded
    trigger: A model finishes a response under the response rules
    lifecycle_meaning: A model response is released and recorded with what it was written from and under which rules
    source_finding: {phase: p1, register: business_events, key: User Prompt Responded}
  - event: User prompt refused
    trigger: A user prompt yields no model response
    lifecycle_meaning: The refusal and its reason are recorded
    source_finding: {phase: p1, register: business_events, key: User Prompt Refused}
  relationships:
  - subject: Model
    verb: is identified by
    object: Description and training fingerprint
    capability_need: Refuse a registration whose description and fingerprint match a registered model
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - subject: Time in service
    verb: belongs to
    object: Model
    capability_need: Open at most one time in service per model, and close it on withdrawal
    source_finding: {phase: p1, register: business_invariants, key: a model has at most one time in service at any moment}
  - subject: User prompt
    verb: is submitted to
    object: Model in service
    capability_need: Refuse a user prompt before the model sees it when the model is not registered or not in service
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - subject: Response rules
    verb: act on
    object: Each word the model is about to write
    capability_need: Stop a forbidden word while the model writes, and choose a permitted one
    source_finding: {phase: p1, register: known_facts, key: 'when the model is about to write a word a rule forbids, the rule stops that word'}
  - subject: Authorized requester
    verb: acts for
    object: Customer
    capability_need: Confirm the requester may act for the customer before the user prompt proceeds
    source_finding: {phase: p1, register: operation_refusals, row: 9}
  - subject: User prompt
    verb: is recorded in
    object: User prompt record
    capability_need: Record every user prompt, responded to or refused, with what the model read
    source_finding: {phase: p1, register: business_invariants, key: every user prompt is recorded}
  capability_graph:
  - capability: Hold a model record durably and change its state in place
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a model record durably and change its state in place}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Hold a time in service durably and close it on withdrawal
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a time in service durably and close it on withdrawal}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Enforce that one record exists per model
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one record exists per model}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Form the key that identifies a model
    source_finding: {phase: p3, register: authoring_decisions, key: Form the key that identifies a model}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Nothing in the composition satisfies it.
  - capability: Keep every user prompt record, answered or refused
    source_finding: {phase: p3, register: authoring_decisions, key: 'Keep every user prompt record, answered or refused'}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Assemble and validate the subdomain's records
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble and validate the subdomain's records}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Confirm the parameters supplied to an operation satisfy their declared rules
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the parameters supplied to an operation satisfy their declared rules}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Declare the kinds of information in their order
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the kinds of information in their order}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: Nothing in the composition satisfies it.
  - capability: Confirm a stated kind of information is one of the declared kinds
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a stated kind of information is one of the declared kinds}
    status: SATISFIED
    gap_register_entry: ''
    notes: Reused as-is from the composition; read, never modified.
  - capability: Refuse a kind of information more sensitive than the ceiling
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a kind of information more sensitive than the ceiling}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: Nothing in the composition satisfies it.
  - capability: Assemble what the model reads, and refuse it when it is longer than the model can read at once
    source_finding: {phase: p3, register: authoring_decisions, key: 'Assemble what the model reads, and refuse it when it is longer than the model can read at once'}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Nothing in the composition satisfies it.
  - capability: Form the response rules in force for one user prompt
    source_finding: {phase: p3, register: authoring_decisions, key: Form the response rules in force for one user prompt}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: Nothing in the composition satisfies it.
  - capability: Offer the model's next words, with a result not determined by its inputs
    source_finding: {phase: p3, register: authoring_decisions, key: 'Offer the model''s next words, with a result not determined by its inputs'}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: Nothing in the composition satisfies it.
  - capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    source_finding: {phase: p3, register: authoring_decisions, key: 'Choose one permitted word under the response rules, the freedom of word choice and a stated seed'}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: Nothing in the composition satisfies it.
  - capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    source_finding: {phase: p3, register: authoring_decisions, key: 'Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached'}
    status: CRITICAL
    gap_register_entry: GAP-08
    notes: Nothing in the composition satisfies it.
  - capability: Run a composed body once per pass of a transform's loop
    source_finding: {phase: p3, register: authoring_decisions, key: Run a composed body once per pass of a transform's loop}
    status: SATISFIED
    gap_register_entry: GAP-09
    notes: 'Owned by platform: capability_transforms::CONSTITUTION_MOLECULES_V0, declared and run.'
  - capability: A test model that tries to write another customer's account number
    source_finding: {phase: p3, register: authoring_decisions, key: A test model that tries to write another customer's account number}
    status: CRITICAL
    gap_register_entry: GAP-10
    notes: Nothing in the composition satisfies it.
  - capability: Model staff and requester actors whose authorization an operation binds
    source_finding: {phase: p3, register: authoring_decisions, key: Model staff and requester actors whose authorization an operation binds}
    status: CRITICAL
    gap_register_entry: GAP-11
    notes: Nothing in the composition satisfies it.
  - capability: Confirm the staff member is model staff, and the requester may act for the customer
    source_finding: {phase: p3, register: authoring_decisions, key: 'Confirm the staff member is model staff, and the requester may act for the customer'}
    status: CRITICAL
    gap_register_entry: GAP-12
    notes: Nothing in the composition satisfies it.
  - capability: Register a model
    source_finding: {phase: p3, register: authoring_decisions, key: Register a model}
    status: CRITICAL
    gap_register_entry: GAP-13
    notes: Nothing in the composition satisfies it.
  - capability: Place a model in service, and withdraw it
    source_finding: {phase: p3, register: authoring_decisions, key: 'Place a model in service, and withdraw it'}
    status: CRITICAL
    gap_register_entry: GAP-14
    notes: Nothing in the composition satisfies it.
  - capability: Submit a user prompt and release or refuse the model response
    source_finding: {phase: p3, register: authoring_decisions, key: Submit a user prompt and release or refuse the model response}
    status: CRITICAL
    gap_register_entry: GAP-15
    notes: Nothing in the composition satisfies it.
  - capability: Retrieve a user prompt record
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve a user prompt record}
    status: CRITICAL
    gap_register_entry: GAP-16
    notes: Nothing in the composition satisfies it.
  - capability: Record each performed operation in the subdomain's own trail
    source_finding: {phase: p3, register: authoring_decisions, key: Record each performed operation in the subdomain's own trail}
    status: CRITICAL
    gap_register_entry: GAP-17
    notes: Nothing in the composition satisfies it.
  - capability: Declare the subdomain's stores and bind its operations to them
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the subdomain's stores and bind its operations to them}
    status: CRITICAL
    gap_register_entry: GAP-18
    notes: Nothing in the composition satisfies it.
  - capability: A governed entry point for each operation
    source_finding: {phase: p3, register: authoring_decisions, key: A governed entry point for each operation}
    status: CRITICAL
    gap_register_entry: GAP-19
    notes: Nothing in the composition satisfies it.
  - capability: A business moment for each of the five events
    source_finding: {phase: p3, register: authoring_decisions, key: A business moment for each of the five events}
    status: CRITICAL
    gap_register_entry: GAP-20
    notes: Nothing in the composition satisfies it.
  dependency_graph:
  - from: model_response
    to: capability_side_effects::CS_MUTABLE_JSON_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Durable record storage}
  - from: model_response
    to: capability_side_effects::CS_REGISTRY_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Uniqueness}
  - from: model_response
    to: capability_side_effects::CS_APPENDONLY_JSONL_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Append-only trail}
  - from: model_response
    to: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Record assembly}
  - from: model_response
    to: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Record shape validation}
  - from: model_response
    to: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Parameter validation}
  - from: model_response
    to: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    dependency_type: capability call
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Value-set membership}
  - from: model_response
    to: capability_transforms::CONSTITUTION_MOLECULES_V0
    dependency_type: molecule execution
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Molecule execution}
  - from: model_response
    to: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
    dependency_type: non-deterministic step
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Non-deterministic step}
  - from: model_response
    to: The business's existing arrangements
    dependency_type: data read
    pps_status: GAP
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  constraint_register:
  - number: '1'
    constraint: Each model the business holds has exactly one record.
    source_finding: {phase: p1, register: business_invariants, row: 1}
    source: invariant
  - number: '2'
    constraint: No model responds to a user prompt unless it is registered and in service.
    source_finding: {phase: p1, register: business_invariants, row: 2}
    source: invariant
  - number: '3'
    constraint: A model has at most one time in service at any moment.
    source_finding: {phase: p1, register: business_invariants, row: 3}
    source: invariant
  - number: '4'
    constraint: Each time in service has exactly one system prompt and one set of response rules.
    source_finding: {phase: p1, register: business_invariants, row: 4}
    source: invariant
  - number: '5'
    constraint: No model reads a more sensitive kind of information than its sensitivity ceiling.
    source_finding: {phase: p1, register: business_invariants, row: 5}
    source: invariant
  - number: '6'
    constraint: No model reads anything but the question, the supporting material and its system prompt.
    source_finding: {phase: p1, register: business_invariants, row: 6}
    source: invariant
  - number: '7'
    constraint: No model response is released that breaks a response rule.
    source_finding: {phase: p1, register: business_invariants, row: 7}
    source: invariant
  - number: '8'
    constraint: No model response is released that reached the longest response before it was finished.
    source_finding: {phase: p1, register: business_invariants, row: 8}
    source: invariant
  - number: '9'
    constraint: Every user prompt is recorded, whether responded to or refused.
    source_finding: {phase: p1, register: business_invariants, row: 9}
    source: invariant
  - number: '10'
    constraint: Every refusal carries its reason.
    source_finding: {phase: p1, register: business_invariants, row: 10}
    source: invariant
  - number: '11'
    constraint: Every business operation is traceable and auditable.
    source_finding: {phase: p1, register: business_invariants, row: 11}
    source: invariant
  - number: '12'
    constraint: Capabilities deferred to future change requests must not be designed into this solution.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: governance rule
  - number: '13'
    constraint: Response rules apply while the model writes, not afterwards.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: business policy
  - number: '14'
    constraint: The requester cannot change the response rules or the system prompt.
    source_finding: {phase: p1, register: constraints, row: 5}
    source: business policy
  - number: '15'
    constraint: A user prompt refused before the model sees it never reaches the model.
    source_finding: {phase: p1, register: constraints, row: 7}
    source: business policy
  - number: '16'
    constraint: The record keeps exactly what the model read, not only a summary or fingerprint of it.
    source_finding: {phase: p1, register: constraints, row: 8}
    source: business policy
  - number: '17'
    constraint: The business must not claim that a model response is true.
    source_finding: {phase: p1, register: constraints, row: 9}
    source: business policy
  - number: '18'
    constraint: Each pass of writing runs two declared steps, the model's offer and the rules' choice, so each word's rule decision is visible.
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    source: governance rule
  - number: '19'
    constraint: Only the model's step is declared as giving results not determined by its inputs.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    source: governance rule
  - number: '20'
    constraint: The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    source: governance rule
  - number: '21'
    constraint: The rules' step draws from a stated seed, recorded with the rules in force, and never draws one itself.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
    source: governance rule
  - number: '22'
    constraint: The subdomain appends only to stores it owns.
    source_finding: {phase: p3, register: authoring_decisions, key: Record each performed operation in the subdomain's own trail}
    source: governance rule
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Form the key that identifies a model}
    capability: Form the key that identifies a model
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the kinds of information in their order}
    capability: Declare the kinds of information in their order
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Refuse a kind of information more sensitive than the ceiling}
    capability: Refuse a kind of information more sensitive than the ceiling
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: 'Assemble what the model reads, and refuse it when it is longer than the model can read at once'}
    capability: Assemble what the model reads, and refuse it when it is longer than the model can read at once
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Form the response rules in force for one user prompt}
    capability: Form the response rules in force for one user prompt
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: 'Offer the model''s next words, with a result not determined by its inputs'}
    capability: Offer the model's next words, with a result not determined by its inputs
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: 'Choose one permitted word under the response rules, the freedom of word choice and a stated seed'}
    capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-08
    source_finding: {phase: p3, register: authoring_decisions, key: 'Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached'}
    capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-09
    source_finding: {phase: p3, register: authoring_decisions, key: Run a composed body once per pass of a transform's loop}
    capability: Run a composed body once per pass of a transform's loop
    owner_subdomain: platform
    resolution: REUSE
  - gap_code: GAP-10
    source_finding: {phase: p3, register: authoring_decisions, key: A test model that tries to write another customer's account number}
    capability: A test model that tries to write another customer's account number
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-11
    source_finding: {phase: p3, register: authoring_decisions, key: Model staff and requester actors whose authorization an operation binds}
    capability: Model staff and requester actors whose authorization an operation binds
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-12
    source_finding: {phase: p3, register: authoring_decisions, key: 'Confirm the staff member is model staff, and the requester may act for the customer'}
    capability: Confirm the staff member is model staff, and the requester may act for the customer
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-13
    source_finding: {phase: p3, register: authoring_decisions, key: Register a model}
    capability: Register a model
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-14
    source_finding: {phase: p3, register: authoring_decisions, key: 'Place a model in service, and withdraw it'}
    capability: Place a model in service, and withdraw it
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-15
    source_finding: {phase: p3, register: authoring_decisions, key: Submit a user prompt and release or refuse the model response}
    capability: Submit a user prompt and release or refuse the model response
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-16
    source_finding: {phase: p3, register: authoring_decisions, key: Retrieve a user prompt record}
    capability: Retrieve a user prompt record
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-17
    source_finding: {phase: p3, register: authoring_decisions, key: Record each performed operation in the subdomain's own trail}
    capability: Record each performed operation in the subdomain's own trail
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-18
    source_finding: {phase: p3, register: authoring_decisions, key: Declare the subdomain's stores and bind its operations to them}
    capability: Declare the subdomain's stores and bind its operations to them
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-19
    source_finding: {phase: p3, register: authoring_decisions, key: A governed entry point for each operation}
    capability: A governed entry point for each operation
    owner_subdomain: model_response
    resolution: NEW
  - gap_code: GAP-20
    source_finding: {phase: p3, register: authoring_decisions, key: A business moment for each of the five events}
    capability: A business moment for each of the five events
    owner_subdomain: model_response
    resolution: NEW
  design_decisions:
  - number: '1'
    decision: model_response is a new subdomain, a peer of the five other project functions, rather than an extension of anything existing.
    source_finding: {phase: p3, register: placement_decision}
    rationale: Nothing in the composition carries the project's namespace, registers a model or governs how one writes.
    constraints_imposed: The subdomain owns its records exclusively; the five other functions are adjacent and untouched.
  - number: '2'
    decision: 'A response is written word by word, each pass running two declared steps: the model offers its next words, and the response rules choose one. The writing transform is a molecule whose loop runs those two steps each pass.'
    source_finding: {phase: p3, register: analysis_findings, row: 1}
    rationale: The rules must act while the model writes, visibly to governance; the platform declares and runs the construct. Decided by the business owner.
    constraints_imposed: No platform extension; no schema, constitution or invariant changes.
  - number: '3'
    decision: Only the model's step is declared as giving results not determined by its inputs; its result is offered to the response rules' step and never decided on.
    source_finding: {phase: p3, register: analysis_findings, row: 2}
    rationale: A reader of the composition must see exactly where determinism ends, and the platform governs that step.
    constraints_imposed: The rules' step and every other transform stay declared deterministic; the writing transform emits the chosen response, never the model's offer.
  - number: '4'
    decision: The model's offered words are recorded in the trace, and a user prompt's trace is reproduced from its record rather than compared across fresh runs.
    source_finding: {phase: p3, register: analysis_findings, row: 3}
    rationale: The platform records every result of a step not determined by its inputs; a replay substitutes the record. Decided by the business owner at rebaseline.
    constraints_imposed: A model response may appear wherever the design places it; it is also kept whole in the user prompt record.
  - number: '5'
    decision: The rules' step draws from a stated seed recorded with the rules in force.
    source_finding: {phase: p3, register: analysis_findings, row: 10}
    rationale: Given the model's offered words, the rules and the seed, anyone reading the record can re-derive each chosen word.
    constraints_imposed: The seed is an input of the rules' step, never drawn inside it.
  - number: '6'
    decision: The test model is a permanent realization of the model's step; a real model later joins it as a second realization.
    source_finding: {phase: p3, register: analysis_findings, row: 11}
    rationale: The rules must be shown to hold against a model that tries to break them, before and after a real model exists.
    constraints_imposed: The model's step is declared by the domain; its realization is supplied outside the domain's own pure transforms.
  - number: '7'
    decision: The user prompt carries the customer's account numbers; the subdomain reads no customer records of its own.
    source_finding: {phase: p3, register: analysis_findings, row: 4}
    rationale: The rule against another customer's account number is formed per user prompt. Decided by the business owner.
    constraints_imposed: The account numbers reach the model only if they are also part of the supporting material.
  - number: '8'
    decision: Uniqueness on a model is enforced by reusing the registry with a key formed from the description and fingerprint.
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one record exists per model}
    rationale: Register-if-absent gives an atomic guarantee, and forming the key is this subdomain's rule.
    constraints_imposed: No side effect is modified.
  - number: '9'
    decision: A model's state and a time in service's openness are data on their records.
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a model record durably and change its state in place}
    rationale: A model moves into and out of service repeatedly.
    constraints_imposed: The record store must support update in place.
  - number: '10'
    decision: The sensitivity check confirms membership first, then compares by the declared order.
    source_finding: {phase: p3, register: analysis_findings, row: 5}
    rationale: Membership is mechanism; the comparison is this subdomain's rule.
    constraints_imposed: The kinds are declared once, in order, least sensitive first.
  - number: '11'
    decision: Retrieving a user prompt record is recorded in the operation trail but raises no business event.
    source_finding: {phase: p1, register: business_events, key: Model Registered}
    rationale: Every operation must be traceable, while nothing reacts to a read.
    constraints_imposed: Five business moments are authored, not six.
  - number: '12'
    decision: Authorization is read on every operation and granted nowhere in this change.
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
    rationale: Which requesters may act for which customers, and which staff are model staff, is decided by the business's existing arrangements.
    constraints_imposed: The subdomain authors authorization reads and no authorization grant.
  authoring_scope:
  - capability: Form the key that identifies a model
    gap_register_ref: GAP-01
  - capability: Declare the kinds of information in their order
    gap_register_ref: GAP-02
  - capability: Refuse a kind of information more sensitive than the ceiling
    gap_register_ref: GAP-03
  - capability: Assemble what the model reads, and refuse it when it is longer than the model can read at once
    gap_register_ref: GAP-04
  - capability: Form the response rules in force for one user prompt
    gap_register_ref: GAP-05
  - capability: Offer the model's next words, with a result not determined by its inputs
    gap_register_ref: GAP-06
  - capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    gap_register_ref: GAP-07
  - capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    gap_register_ref: GAP-08
  - capability: Run a composed body once per pass of a transform's loop
    gap_register_ref: GAP-09
  - capability: A test model that tries to write another customer's account number
    gap_register_ref: GAP-10
  - capability: Model staff and requester actors whose authorization an operation binds
    gap_register_ref: GAP-11
  - capability: Confirm the staff member is model staff, and the requester may act for the customer
    gap_register_ref: GAP-12
  - capability: Register a model
    gap_register_ref: GAP-13
  - capability: Place a model in service, and withdraw it
    gap_register_ref: GAP-14
  - capability: Submit a user prompt and release or refuse the model response
    gap_register_ref: GAP-15
  - capability: Retrieve a user prompt record
    gap_register_ref: GAP-16
  - capability: Record each performed operation in the subdomain's own trail
    gap_register_ref: GAP-17
  - capability: Declare the subdomain's stores and bind its operations to them
    gap_register_ref: GAP-18
  - capability: A governed entry point for each operation
    gap_register_ref: GAP-19
  - capability: A business moment for each of the five events
    gap_register_ref: GAP-20
```

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

---

## 2. Capability Graph (capability_graph)

---

## 3. Dependency Graph (dependency_graph)

The dependencies on the platform are satisfied: it declares and runs molecules and steps whose result
is not determined by their inputs. The dependency on the business's existing arrangements is owned by the business, not by this change: the subdomain reads
whether a requester may act for a customer and whether staff are model staff, and decides neither.

---

## 4. Constraint Register (constraint_register)

---

## 5. Gap Register (gap_register)

---

## 6. Design Decisions (design_decisions)

---

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Registry beyond what a model response needs | A project function; this change request includes only as much of the registry as a model response needs |
| Retiring models | Declared excluded from this release |
| Disclosure | A project function; reviewing a model response after it is written is declared excluded from this release |
| Action | A project function; letting a model propose actions is declared excluded from this release |
| Substitution | A project function; replacing the model in service is declared excluded from this release |
| Reporting | A project function; regulator reporting is declared excluded from this release |
| Catching a response made up from nothing | It needs the finished response, and belongs to the later review of finished responses |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 3 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · resources · events · relationships · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
