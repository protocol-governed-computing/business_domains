# Stage 6 — Governance Intent: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p6
  domain: causal_language_model
  subdomain: model_response
  cr: cr_01_model_response
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Register a model
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-13}
  - capability: Place a model in service, and withdraw it
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-14}
  - capability: Submit a user prompt and release or refuse the model response
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-15}
  - capability: Retrieve a user prompt record
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-16}
  - capability: Form the key that identifies a model
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Declare the kinds of information in their order
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Refuse a kind of information more sensitive than the ceiling
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Assemble what the model reads, and refuse it when it is longer than the model can read at once
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Form the response rules in force for one user prompt
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Offer the model's next words, with a result not determined by its inputs
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-08}
  - capability: A test model that tries to write another customer's account number
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-10}
  - capability: Model staff and requester actors whose authorization an operation binds
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-11}
  - capability: Confirm the staff member is model staff, and the requester may act for the customer
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-12}
  - capability: Record each performed operation in the subdomain's own trail
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-17}
  - capability: Declare the subdomain's stores and bind its operations to them
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-18}
  - capability: A governed entry point for each operation
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-19}
  - capability: A business moment for each of the five events
    owner_subdomain: model_response
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p4, register: authoring_scope, key: GAP-20}
  - capability: Run a composed body once per pass of a transform's loop
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CONSTITUTION_MOLECULES_V0
    source_finding: {phase: p4, register: authoring_scope, key: GAP-09}
  - capability: Hold a durable record that can be read, listed and updated in place
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_MUTABLE_JSON_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Hold a model record durably and change its state in place}
  - capability: Claim a value once so a second claim on it fails
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_REGISTRY_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Enforce that one record exists per model}
  - capability: Append an entry to a trail that cannot be amended
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_side_effects::CS_APPENDONLY_JSONL_V0
    source_finding: {phase: p3, register: authoring_decisions, key: 'Keep every user prompt record, answered or refused'}
  - capability: Assemble a durable record from supplied values
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble and validate the subdomain's records}
  - capability: Confirm a record carries the fields its contract declares
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Assemble and validate the subdomain's records}
  - capability: Confirm supplied parameters satisfy declared rules
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm the parameters supplied to an operation satisfy their declared rules}
  - capability: Confirm a value belongs to a declared set
    owner_subdomain: platform
    disposition: SATISFIED
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a stated kind of information is one of the declared kinds}
  - capability: Deciding which requesters may act for which customers
    owner_subdomain: The business's existing arrangements
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  - capability: Deciding which staff are model staff
    owner_subdomain: The business's existing arrangements
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p1, register: authority_deferrals, row: 2}
  storage_governance:
  - storage_need: A durable record of every model the business holds
    purpose: One record per model, carrying its registered-or-in-service state
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: Model record}
  - storage_need: A claim on each model's identity, held once
    purpose: Duplicate registration must be refused at the moment of registration
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: Model identity register}
  - storage_need: A durable record of every time in service
    purpose: Each period with its ceiling, system prompt and response rules, open until withdrawal
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: Time in service record}
  - storage_need: A claim on each time in service's identity, held once
    purpose: A second placement under the same identity must be refused, never overwrite the first
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: Time in service identity register}
  - storage_need: A claim on each user prompt's identity, held once
    purpose: One user prompt identity must resolve to exactly one user prompt record
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: User prompt identity register}
  - storage_need: A record of every user prompt that cannot be amended
    purpose: What the model read, the rules in force and the outcome, kept whole as evidence
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: User prompt record}
  - storage_need: A trail of performed operations that cannot be amended
    purpose: Every operation must be traceable afterwards
    subdomain: model_response
    source_finding: {phase: p5, register: business_objects, key: Operation trail}
  cross_subdomain_deps:
  - dependency: Read whether a requester may act for a customer, and whether staff are model staff
    direction: model_response -> business_arrangements
    existing_artifact: ''
    status: GAP
    source_finding: {phase: p1, register: authority_deferrals, row: 1}
  pps_artifacts_requiring_action:
  - fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    current_status: Declared and in use by ai_governance, blockchain, book_library_mgmt and workload
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_MUTABLE_JSON_V0'}
  - fqdn: capability_side_effects::CS_REGISTRY_V0
    current_status: Declared and in use by ai_governance, blockchain and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_REGISTRY_V0'}
  - fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    current_status: Declared and in use by ai_governance, blockchain and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_side_effects::CS_APPENDONLY_JSONL_V0'}
  - fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    current_status: Declared and in use by blockchain and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    current_status: Declared and in use by blockchain and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    current_status: Declared and in use by ai_governance, blockchain and book_library_mgmt
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    current_status: Declared and in use by ai_governance and blockchain
    action: REUSE
    source_finding: {phase: p3, register: impact_analysis, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - fqdn: capability_transforms::CONSTITUTION_MOLECULES_V0
    current_status: Governs how a molecule runs; no transform in the composition is a molecule yet
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 8}
  - fqdn: capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0
    current_status: Governs a step whose result is not determined by its inputs; none is declared yet
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, row: 9}
  boundary_rules:
  - rule_name: MODEL_RESPONSE_OWNS_ITS_STORES
    statement: Every store model_response reads or writes is declared by model_response, and no operation writes into a store another subdomain owns.
    source_finding: {phase: p4, register: constraint_register, row: 22}
  - rule_name: AUTHORIZATION_IS_READ_NEVER_GRANTED
    statement: Model response confirms model staff and a requester's authority to act for the customer on every operation, and grants authorization nowhere.
    source_finding: {phase: p4, register: design_decisions, row: 12}
  - rule_name: RULES_ACT_WHILE_WRITING
    statement: Each pass of writing runs two declared steps, the model's offer and the rules' choice, so each word's rule decision is a step governance can see.
    source_finding: {phase: p4, register: constraint_register, row: 18}
  - rule_name: DETERMINISM_ENDS_AT_THE_MODEL
    statement: Only the model's step is declared as giving results not determined by its inputs; every other step is declared deterministic.
    source_finding: {phase: p4, register: constraint_register, row: 19}
  - rule_name: RESPONSE_REPRODUCED_FROM_RECORD
    statement: The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly.
    source_finding: {phase: p4, register: constraint_register, row: 20}
  - rule_name: SEED_IS_A_RECORDED_INPUT
    statement: The rules' step draws from a stated seed recorded with the rules in force, and never draws one itself.
    source_finding: {phase: p4, register: constraint_register, row: 21}
  - rule_name: REFUSED_BEFORE_THE_MODEL_SEES_IT
    statement: A user prompt refused on registration, service, sensitivity or length never reaches the model's step.
    source_finding: {phase: p4, register: constraint_register, row: 15}
  - rule_name: NOTHING_ELSE_REACHES_THE_MODEL
    statement: The model's step reads the question, the supporting material and the system prompt, and nothing else.
    source_finding: {phase: p4, register: constraint_register, row: 6}
  - rule_name: EVERY_USER_PROMPT_IS_RECORDED
    statement: Every user prompt, responded to or refused, appends one entry to the user prompt record, and no entry is amended.
    source_finding: {phase: p4, register: constraint_register, row: 9}
  - rule_name: ONE_OPEN_TIME_IN_SERVICE
    statement: A model has at most one open time in service, and placement is refused while one is open.
    source_finding: {phase: p4, register: constraint_register, row: 3}
  - rule_name: READS_RAISE_NO_EVENT
    statement: Retrieving a user prompt record is recorded in the operation trail and recognises no business moment.
    source_finding: {phase: p4, register: design_decisions, row: 11}
  governance_outcome:
  - capability: Register a model
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: Register a model}
  - capability: Place a model in service, and withdraw it
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: 'Place a model in service, and withdraw it'}
  - capability: Submit a user prompt and release or refuse the model response
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: Submit a user prompt and release or refuse the model response}
  - capability: Retrieve a user prompt record
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: Retrieve a user prompt record}
  - capability: Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: 'Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached'}
  - capability: Offer the model's next words, with a result not determined by its inputs
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: 'Offer the model''s next words, with a result not determined by its inputs'}
  - capability: Choose one permitted word under the response rules, the freedom of word choice and a stated seed
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: 'Choose one permitted word under the response rules, the freedom of word choice and a stated seed'}
  - capability: Confirm the staff member is model staff, and the requester may act for the customer
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: 'Confirm the staff member is model staff, and the requester may act for the customer'}
  - capability: Record each performed operation in the subdomain's own trail
    owner_subdomain: model_response
    source_finding: {phase: p6, register: ownership, key: Record each performed operation in the subdomain's own trail}
  - capability: Run a composed body once per pass of a transform's loop
    owner_subdomain: platform
    source_finding: {phase: p6, register: ownership, key: Run a composed body once per pass of a transform's loop}
```

---

## Domain Placement

| Field | Value |
| --- | --- |
| Domain | `causal_language_model` |
| Primary subdomain | `model_response` — NEW — declared by this CR |
| Authority class | two new actor types: authorized model staff, and the authorized requester acting for a customer |
| Governing constitutions | `governance::CONSTITUTION_GOVERNANCE_V0`, `workflow::CONSTITUTION_WORKFLOW_V0`, `capability_transforms::CONSTITUTION_CAPABILITY_TRANSFORMS_V0`, `structure::CONSTITUTION_STRUCTURE_V0` |

Model response stands alone rather than nesting under an existing subdomain because nothing in the
composition registers a model or governs how one writes: there is no boundary to extend, and the five
other project functions do not exist yet. Two new actor types are required because no actor in the
composition names model staff or a requester acting for a customer.

The platform carries no extension for this change. It declares and runs molecules, whose loop runs a
composed body once per pass, and it governs the model's step as one whose result is not determined by
its inputs: recorded when produced, replayed from the record, and offered to a deterministic step.
This change reuses both.

---

## 1. Subdomain Boundary — Ownership

Nineteen capabilities are owned by model_response and authored by this change, and one is owned by
the platform and carried by it. Seven are satisfied by mechanisms the platform already declares,
reused as-is. Two are deferred to the business's existing arrangements.

---

## 2. Storage Governance Requirements

Every store named here is owned by model_response and written only by its own operations.

---

## 3. Cross-Subdomain Dependency Declaration

Model response reads authorization and never grants it, so deciding who is authorized is a gap owned
by the business rather than work this change performs. No operation writes into a store another
subdomain owns, and no capability contract from another subdomain is called.

---

## 4. PPS Artifacts Requiring Action

Every artifact is read, never modified, so no consumer of any of them is affected by this change.

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
