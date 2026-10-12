# Stage 2 — Domain Model Verification: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p2
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Model
    description: A language model the business holds, identified by its description and training fingerprint together.
    store_model: One durable record per model, addressed by its description and fingerprint together, never duplicated.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Time in Service
    description: One period during which a model is in service, carrying exactly one sensitivity ceiling, system prompt and set of response rules.
    store_model: One durable record per period, naming the single model it belongs to, open while the model is in service and closed when it is withdrawn. At most one is open per model.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: a model has at most one time in service at any moment}
  - entity: User Prompt Record
    description: The record kept of every user prompt, responded to or refused.
    store_model: 'An append-only trail: one entry per user prompt, never rewritten.'
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: 'every user prompt is recorded, whether responded to or refused'}
  entity_attributes:
  - entity: Model
    attribute: Description
    meaning: How the model is built; part of what identifies it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: Model
    attribute: Readable Length
    meaning: The amount of text the model can read at once, stated in its description.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: 'a registration describes how the model is built, including the amount of text it can read at once'}
  - entity: Model
    attribute: Training Fingerprint
    meaning: The provider's claim about the model's training; part of what identifies it, recorded and not verified.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Training Fingerprint}
  - entity: Model
    attribute: State
    meaning: Whether the model is registered or in service.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_states, key: Model}
  - entity: Time in Service
    attribute: Model
    meaning: The single model this period belongs to.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Time in Service}
  - entity: Time in Service
    attribute: Sensitivity Ceiling
    meaning: The most sensitive kind of information the model may read during this period.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Sensitivity Ceiling}
  - entity: Time in Service
    attribute: System Prompt
    meaning: The business's standing instructions to the model during this period.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: System Prompt}
  - entity: Time in Service
    attribute: Forbidden Words and Patterns
    meaning: Words and patterns the model must never write during this period.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Forbidden Words and Patterns}
  - entity: Time in Service
    attribute: Freedom of Word Choice
    meaning: How freely the model may choose its words during this period.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Freedom of Word Choice}
  - entity: Time in Service
    attribute: Longest Response
    meaning: The longest response the model may write during this period.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, key: Longest Response}
  - entity: Time in Service
    attribute: Open
    meaning: Whether the period is current, which it is from placement until withdrawal.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - entity: User Prompt Record
    attribute: Requester and Customer
    meaning: Who asked, and for which customer.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a user prompt record holds who asked and for which customer}
  - entity: User Prompt Record
    attribute: Model and Time in Service
    meaning: Which model responded or was asked, and the period it was in service.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a user prompt record holds which model and its time in service}
  - entity: User Prompt Record
    attribute: What the Model Read
    meaning: Exactly the question, the supporting material and the system prompt, kept whole rather than as a summary or fingerprint.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: constraints, key: the record keeps exactly what the model read}
  - entity: User Prompt Record
    attribute: Kind of Information
    meaning: The kind of information the requester stated the user prompt contains.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: authority_boundaries, key: the kind of information a user prompt contains}
  - entity: User Prompt Record
    attribute: Response Rules in Force
    meaning: The response rules of the time in service the user prompt was submitted under.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: a user prompt record holds the response rules in force}
  - entity: User Prompt Record
    attribute: Outcome
    meaning: The model response, or the reason the user prompt was refused, naming the rule where a rule stopped it.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: every refusal carries its reason}
  business_processes:
  - process: Register a model
    initiator: Authorized model staff
    outcome: The business holds exactly one record for the model, or the registration is refused because the model is already registered.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Model Registered}
  - process: Place a model in service
    initiator: Authorized model staff
    outcome: A time in service begins with its sensitivity ceiling, system prompt and response rules, or placement is refused.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Model Placed In Service}
  - process: Withdraw a model from service
    initiator: Authorized model staff
    outcome: The model's time in service ends and it responds to no one.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: Model Withdrawn From Service}
  - process: Submit a user prompt
    initiator: Authorized requester
    outcome: A model response written under the response rules is released, or the user prompt is refused with its reason; either way it is recorded.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_events, key: User Prompt Responded}
  - process: Retrieve a user prompt record
    initiator: Authorized model staff
    outcome: The record of the user prompt asked for.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: the operations required}
  process_steps:
  - process: Register a model
    step: '1'
    action: Confirm the staff member is authorized model staff
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Register a model
    step: '2'
    action: Confirm no registered model carries this description and fingerprint
    record_produced: A sameness decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Register a model
    step: '3'
    action: Record the model's description and fingerprint as its record, registered
    record_produced: The model record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: each model has exactly one record}
  - process: Register a model
    step: '4'
    action: Record that the model was registered
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: every business operation is traceable and auditable}
  - process: Place a model in service
    step: '1'
    action: Confirm the staff member is authorized model staff
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Place a model in service
    step: '2'
    action: Confirm the model is registered
    record_produced: An existence decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Place a model in service
    step: '3'
    action: Confirm the model is not already in service
    record_produced: A state decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Place a model in service
    step: '4'
    action: Record a new time in service with its sensitivity ceiling, system prompt and response rules, and mark the model in service
    record_produced: The time in service record and the updated model record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 2}
  - process: Place a model in service
    step: '5'
    action: Record that the model was placed in service
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Withdraw a model from service
    step: '1'
    action: Confirm the staff member is authorized model staff
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Withdraw a model from service
    step: '2'
    action: Confirm the model is in service
    record_produced: A state decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Withdraw a model from service
    step: '3'
    action: Close the time in service and mark the model registered
    record_produced: The closed time in service and the updated model record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: lifecycle_transitions, row: 3}
  - process: Withdraw a model from service
    step: '4'
    action: Record that the model was withdrawn
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  - process: Submit a user prompt
    step: '1'
    action: Confirm the requester is permitted to act for the customer
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 9}
  - process: Submit a user prompt
    step: '2'
    action: Confirm the model is registered
    record_produced: An existence decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Submit a user prompt
    step: '3'
    action: Confirm the model is in service, and read its open time in service
    record_produced: A state decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 6}
  - process: Submit a user prompt
    step: '4'
    action: Confirm the stated kind of information is no more sensitive than the sensitivity ceiling
    record_produced: A sensitivity decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Submit a user prompt
    step: '5'
    action: 'Assemble what the model reads: the question, the supporting material and the system prompt, and nothing else'
    record_produced: What the model reads
    evidence_status: INFERRED
    source_finding: {phase: p1, register: constraints, key: 'nothing reaches the model except the question, the supporting material and the system prompt'}
  - process: Submit a user prompt
    step: '6'
    action: Confirm what the model reads is no longer than the model can read at once
    record_produced: A length decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 8}
  - process: Submit a user prompt
    step: '7'
    action: Form the forbidden words and patterns for this user prompt, using the account numbers of the customer it is for
    record_produced: The rules in force for this user prompt
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: '"another customer''s account number" depends on who the customer is'}
  - process: Submit a user prompt
    step: '8'
    action: 'Write the response one word at a time: the model offers its next words, the response rules stop any forbidden word, and one permitted word is chosen under the freedom of word choice'
    record_produced: The response so far, and the words the rules stopped
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: 'when the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one'}
  - process: Submit a user prompt
    step: '9'
    action: Stop writing when the response is finished, when no permitted word remains, or when the longest response is reached
    record_produced: A completion decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 10}
  - process: Submit a user prompt
    step: '10'
    action: Release the response if it finished; otherwise refuse, naming the rule that stopped it or the length reached
    record_produced: The model response or the refusal
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 11}
  - process: Submit a user prompt
    step: '11'
    action: Record the user prompt with its requester, customer, model, time in service, what the model read, kind of information, rules in force and outcome
    record_produced: The user prompt record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: 'every user prompt is recorded, whether responded to or refused'}
  - process: Retrieve a user prompt record
    step: '1'
    action: Confirm the staff member is authorized model staff
    record_produced: An authorization decision
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Retrieve a user prompt record
    step: '2'
    action: Read the user prompt record asked for
    record_produced: The user prompt record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: the operations required}
  - process: Retrieve a user prompt record
    step: '3'
    action: Record that the record was retrieved
    record_produced: A durable, auditable record of the operation
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_invariants, key: traceable and auditable}
  belief_verification:
  - belief: causal_language_model is not part of the current software baseline.
    result: NOT_FOUND
    evidence: The composition declares seven domains — ai_governance, blockchain, book_library_mgmt, inspection, platform, transformation, workload — and its artifact index carries no identity in the causal_language_model namespace.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: No capability in the current composition registers language models or governs how a model writes a response.
    result: NOT_FOUND
    evidence: Semantic vocabulary search returns no identity for prompt, token, sensitivity, confidential, customer, account or instruction. The identities matching model are transformation::IN_BUSINESS_MODEL_SUBMITTED_V0, transformation::IN_DOMAIN_MODEL_SUBMITTED_V0 and their two admissibility workflows, which judge design documents. ai_governance::WF_GOVERN_AGENT_ACTION_V0 mediates actions an agent proposes, against license-tier authority, after the proposal is made; it registers no model and governs no writing.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Uniqueness registry
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Registers a key, resolves it, reports whether it exists, counts and deregisters.
    fit: PARTIAL
    cannot_do: It enforces uniqueness on one key; a model is identified by its description and fingerprint together, and the composite is not a key it forms.
  - capability: Identity key formation
    fqdn: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0
    what_it_does: Forms a single key from the attributes that identify a book.
    fit: PARTIAL
    cannot_do: It forms a book's key; the model's key must be formed from its own attributes.
  - capability: Durable record store
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Writes, reads, lists, updates in place and deletes durable records.
    fit: EXACT
    cannot_do: It holds whatever it is given; it enforces no identity, no state and no authorization.
  - capability: Append-only trail
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Appends an entry and returns the whole trail.
    fit: EXACT
    cannot_do: It appends what it is handed; it does not decide which operations must be recorded.
  - capability: Record shape validation
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Confirms a record carries the fields its contract declares.
    fit: EXACT
    cannot_do: It does not know which fields a model or a user prompt requires.
  - capability: Record assembly
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Assembles a durable record from supplied values.
    fit: EXACT
    cannot_do: It applies no identity rule and decides no sameness.
  - capability: Set membership
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Confirms a value belongs to a declared set.
    fit: PARTIAL
    cannot_do: It confirms membership, not order; comparing a kind of information with a ceiling needs the order of the kinds.
  - capability: Parameter rule validation
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Confirms supplied parameters satisfy declared rules.
    fit: PARTIAL
    cannot_do: It judges supplied values once; it does not act while a response is written.
  - capability: Controlled value set
    fqdn: blockchain::VOCAB_WALLET_CLASSIFICATION_V0
    what_it_does: Declares a closed list of values a subdomain uses.
    fit: EXACT
    cannot_do: It declares a wallet's classifications, not kinds of information.
  - capability: Authorization check
    fqdn: book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0
    what_it_does: Confirms a staff member may perform a subdomain's operations.
    fit: PARTIAL
    cannot_do: It confirms catalog staff; model staff and requesters acting for a customer are not its concern.
  - capability: Operation trail
    fqdn: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    what_it_does: Composes the recording of a performed operation into the subdomain's own trail.
    fit: PARTIAL
    cannot_do: It appends to the catalog's store; a subdomain owns its stores exclusively.
  - capability: Business actor
    fqdn: book_library_mgmt::AC_LIBRARY_STAFF_V0
    what_it_does: Declares a business actor whose identity an operation binds.
    fit: PARTIAL
    cannot_do: It names library staff; neither model staff nor requesters exist.
  - capability: Subdomain storage declaration
    fqdn: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0
    what_it_does: Declares the stores a business subdomain owns and the paths they occupy.
    fit: EXACT
    cannot_do: It declares another subdomain's stores.
  - capability: Runtime binding declaration
    fqdn: book_library_mgmt::RB_CATALOG_BINDINGS_V0
    what_it_does: Binds a subdomain's workflows to the stores and policies they use.
    fit: EXACT
    cannot_do: It binds another subdomain's surface.
  - capability: Repeated computation
    fqdn: workload::CT_PURE_COLLATZ_STEP_V0
    what_it_does: Computes a whole repeated sequence for each input within one transform.
    fit: PARTIAL
    cannot_do: The repetition happens inside one transform, so no step within it is visible to governance; a response written word by word under rules needs each word's rule decision to be visible.
  - capability: Agent action mediation
    fqdn: ai_governance::WF_GOVERN_AGENT_ACTION_V0
    what_it_does: Mediates an action an agent proposes, against the authority its license grants.
    fit: MISMATCH
    cannot_do: It judges a finished proposal; it does not act while a response is written.
  gaps:
  - gap: Nothing in the composition holds a model record, a time in service or a user prompt record.
    severity: CRITICAL
    impact: Every requested outcome depends on these records; the store mechanisms exist, the subdomain's own stores do not.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: No capability registers a model, places one in service, withdraws one, accepts a user prompt, or retrieves a user prompt record.
    severity: CRITICAL
    impact: The five business processes have no counterpart in the composition and must all be authored.
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 2}
  - gap: Nothing writes a response word by word with the response rules acting on each word as a step governance can see.
    severity: CRITICAL
    impact: The central requested outcome is that rules apply while the model writes. The only repeated computation composed today keeps its repetition inside one transform, where no rule decision is visible.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - gap: No actor exists for model staff or for requesters, and none asserts authority to act for a customer.
    severity: CRITICAL
    impact: Every operation is refused unless its initiator is authorized, and there is nothing to bind that decision to.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - gap: No business moment exists for a model being registered, placed in service or withdrawn, or for a user prompt being responded to or refused.
    severity: CRITICAL
    impact: Five business events are declared and none is recognised anywhere in the composition.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_events, key: Model Registered}
  - gap: Uniqueness on a model's description and fingerprint together has no counterpart in the composition.
    severity: MAJOR
    impact: Duplicate registration must be refused, and the registry available enforces uniqueness on a single key.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - gap: No kinds of information, and no ordering between them, are declared anywhere.
    severity: MAJOR
    impact: A user prompt is refused when its kind is more sensitive than the ceiling, which needs the kinds and their order.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: 'the kinds of information, from least to most sensitive'}
  - gap: No test model exists.
    severity: MAJOR
    impact: The business sees the rules hold only through a model that tries to break them.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - gap: Deciding which requesters may act for which customers, and which staff are model staff, is deferred to the business's existing arrangements, which the composition does not hold.
    severity: MINOR
    impact: 'Noted, not modelled: the subdomain reads authorization and never grants it.'
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  architectural_observations:
  - observation: A business subdomain in this composition declares its own stores and binds its own operations to them, so a new subdomain has a worked precedent for owning its records.
    evidence: book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 · book_library_mgmt::RB_CATALOG_BINDINGS_V0
    evidence_status: OBSERVED
    source_finding: {phase: p2, register: belief_verification, row: 1}
  - observation: 'Registering something once, identified by several attributes together, has a worked precedent: a key formed from the attributes and a uniqueness registry keyed on it.'
    evidence: book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · capability_side_effects::CS_REGISTRY_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - observation: Operations in this composition are declared as step sequences that may not return to an earlier step.
    evidence: workflow::CONSTITUTION_WORKFLOW_V0 · workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: a language model writes a response one word at a time}
  - observation: 'Transforms are placed by what they declare: a deterministic atom, a molecule, or an atom whose result is not determined by its inputs, each governed by its own constitution. Every result of such an atom is recorded when produced, a replay substitutes the record and never runs the atom, and its result is offered to a deterministic step rather than decided on. No transform in the composition is yet declared so.'
    evidence: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 · capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0 · capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: nobody can predict a language model's exact response in advance}
  - observation: 'A transform may be a molecule: declared steps, including a loop that runs a composed body once per member of a collection and carries its values between passes. The runtime runs it, and records each step it runs. No composition yet carries a molecule.'
    evidence: capability_transforms::CONSTITUTION_MOLECULES_V0 · capability_transforms::INVARIANT_MOLECULE_RUNNABLE_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: a language model writes a response one word at a time}
  - observation: The execution trace declares which of its content is determinative and which is merely observational. A step's detail is determinative, and for an atom whose result is not determined by its inputs that detail carries the result's values.
    evidence: vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: 'given the same question twice, it may respond differently'}
  - observation: Recording a performed operation into the subdomain's own trail is already composed as a governed step, within another subdomain.
    evidence: book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: business_invariants, key: every business operation is traceable and auditable}
  discovery_concerns:
  - concern: Writing word by word repeats, while operations may not return to an earlier step. The repetition must therefore live below the operation. The platform declares and runs the form it takes — a molecule's loop — and the only composed precedent keeps the repetition inside one atom, where no rule decision is visible.
    evidence: workflow::CONSTITUTION_WORKFLOW_V0 · capability_transforms::CONSTITUTION_MOLECULES_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - concern: The model is the first capability whose result is not determined by its inputs. The platform declares where such a capability belongs, and requires that its result be offered to a deterministic step and never decided on; no composition yet carries one.
    evidence: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 · capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: nobody can predict a language model's exact response in advance}
  - concern: A model's offered words differ between runs of the same user prompt, and the trace records them as determinative, so two fresh runs of the same user prompt yield different traces. A replay from the record reproduces one exactly.
    evidence: vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 · capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: 'given the same question twice, it may respond differently'}
  - concern: The rule against another customer's account number needs the account numbers of the customer the user prompt is for, and the statement does not say where the subdomain reads them from.
    evidence: null
    severity: MAJOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: known_facts, key: '"another customer''s account number" depends on who the customer is'}
  - concern: Comparing a kind of information with a ceiling needs the kinds' order, and the available value-set check confirms membership only.
    evidence: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    severity: MINOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: known_facts, key: 'the kinds of information, from least to most sensitive'}
  - concern: A user prompt record keeps whole what the model read, so its entries are as large as the material submitted.
    evidence: capability_side_effects::CS_APPENDONLY_JSONL_V0
    severity: MINOR
    evidence_status: INFERRED
    source_finding: {phase: p1, register: constraints, key: the record keeps exactly what the model read}
  open_questions:
  - question: Where does the subdomain read the customer's account numbers from, to form the rule against another customer's account number?
    category: BUSINESS
    why_it_matters: The rule cannot be formed for a user prompt without them.
    source_finding: {phase: p2, register: discovery_concerns, row: 4}
  - question: How can each word's rule decision be a step governance can see, when the repetition must live below the operation?
    category: ARCHITECTURE
    why_it_matters: It decides whether the rules visibly act while the model writes, which is the central requested outcome.
    source_finding: {phase: p2, register: discovery_concerns, row: 1}
  - question: How is a capability declared whose result is not determined by its inputs?
    category: ARCHITECTURE
    why_it_matters: The model is such a capability, and no composition yet carries one.
    source_finding: {phase: p2, register: discovery_concerns, row: 2}
```

Every claim about what exists is grounded in the pinned baseline
`3918d97c73a7431ecc9ef512938b34afa9028cd6e382626398750dca12defb1f` — 425 artifacts across
ai_governance, blockchain, book_library_mgmt, inspection, platform, transformation, workload — read
through the inspection interface. The semantic model is inherited from Stage 1 and confirmed here,
never re-derived.

---

## 1. Business Entities

### Entity Attributes

---

## 2. Business Processes

### Process Steps

---

## 3. Belief Verification — THE SPINE

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
