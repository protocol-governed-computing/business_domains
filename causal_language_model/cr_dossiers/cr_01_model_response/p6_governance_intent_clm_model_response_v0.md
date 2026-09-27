# Stage 6 — Governance Intent: causal_language_model / model_response

**Stage:** 6 — Governance Intent
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

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

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Register a model | model_response | OWNED |  | S4 authoring_scope GAP-13 |
| Place a model in service, and withdraw it | model_response | OWNED |  | S4 authoring_scope GAP-14 |
| Submit a user prompt and release or refuse the model response | model_response | OWNED |  | S4 authoring_scope GAP-15 |
| Retrieve a user prompt record | model_response | OWNED |  | S4 authoring_scope GAP-16 |
| Form the key that identifies a model | model_response | OWNED |  | S4 authoring_scope GAP-01 |
| Declare the kinds of information in their order | model_response | OWNED |  | S4 authoring_scope GAP-02 |
| Refuse a kind of information more sensitive than the ceiling | model_response | OWNED |  | S4 authoring_scope GAP-03 |
| Assemble what the model reads, and refuse it when it is longer than the model can read at once | model_response | OWNED |  | S4 authoring_scope GAP-04 |
| Form the response rules in force for one user prompt | model_response | OWNED |  | S4 authoring_scope GAP-05 |
| Offer the model's next words, with a result not determined by its inputs | model_response | OWNED |  | S4 authoring_scope GAP-06 |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | model_response | OWNED |  | S4 authoring_scope GAP-07 |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | model_response | OWNED |  | S4 authoring_scope GAP-08 |
| A test model that tries to write another customer's account number | model_response | OWNED |  | S4 authoring_scope GAP-10 |
| Model staff and requester actors whose authorization an operation binds | model_response | OWNED |  | S4 authoring_scope GAP-11 |
| Confirm the staff member is model staff, and the requester may act for the customer | model_response | OWNED |  | S4 authoring_scope GAP-12 |
| Record each performed operation in the subdomain's own trail | model_response | OWNED |  | S4 authoring_scope GAP-17 |
| Declare the subdomain's stores and bind its operations to them | model_response | OWNED |  | S4 authoring_scope GAP-18 |
| A governed entry point for each operation | model_response | OWNED |  | S4 authoring_scope GAP-19 |
| A business moment for each of the five events | model_response | OWNED |  | S4 authoring_scope GAP-20 |
| Run a composed body once per pass of a transform's loop | platform | SATISFIED | capability_transforms::CONSTITUTION_MOLECULES_V0 | S4 authoring_scope GAP-09 |
| Hold a durable record that can be read, listed and updated in place | platform | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S3 authoring_decisions Hold a model record durably and change its state in place |
| Claim a value once so a second claim on it fails | platform | SATISFIED | capability_side_effects::CS_REGISTRY_V0 | S3 authoring_decisions Enforce that one record exists per model |
| Append an entry to a trail that cannot be amended | platform | SATISFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 | S3 authoring_decisions Keep every user prompt record, answered or refused |
| Assemble a durable record from supplied values | platform | SATISFIED | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | S3 authoring_decisions Assemble and validate the subdomain's records |
| Confirm a record carries the fields its contract declares | platform | SATISFIED | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | S3 authoring_decisions Assemble and validate the subdomain's records |
| Confirm supplied parameters satisfy declared rules | platform | SATISFIED | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | S3 authoring_decisions Confirm the parameters supplied to an operation satisfy their declared rules |
| Confirm a value belongs to a declared set | platform | SATISFIED | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | S3 authoring_decisions Confirm a stated kind of information is one of the declared kinds |
| Deciding which requesters may act for which customers | The business's existing arrangements | DEFERRED |  | S1 authority_deferrals #1 |
| Deciding which staff are model staff | The business's existing arrangements | DEFERRED |  | S1 authority_deferrals #2 |

Nineteen capabilities are owned by model_response and authored by this change, and one is owned by
the platform and carried by it. Seven are satisfied by mechanisms the platform already declares,
reused as-is. Two are deferred to the business's existing arrangements.

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every model the business holds | One record per model, carrying its registered-or-in-service state | model_response | S5 business_objects Model record |
| A claim on each model's identity, held once | Duplicate registration must be refused at the moment of registration | model_response | S5 business_objects Model identity register |
| A durable record of every time in service | Each period with its ceiling, system prompt and response rules, open until withdrawal | model_response | S5 business_objects Time in service record |
| A record of every user prompt that cannot be amended | What the model read, the rules in force and the outcome, kept whole as evidence | model_response | S5 business_objects User prompt record |
| A trail of performed operations that cannot be amended | Every operation must be traceable afterwards | model_response | S5 business_objects Operation trail |

Every store named here is owned by model_response and written only by its own operations.

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Read whether a requester may act for a customer, and whether staff are model staff | model_response -> business_arrangements |  | GAP | S1 authority_deferrals #1 |

Model response reads authorization and never grants it, so deciding who is authorized is a gap owned
by the business rather than work this change performs. No operation writes into a store another
subdomain owns, and no capability contract from another subdomain is called.

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|------------------------------------------|----------------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Declared and in use by ai_governance, blockchain, book_library_mgmt and workload | REUSE | S3 impact_analysis capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | Declared and in use by ai_governance, blockchain and book_library_mgmt | REUSE | S3 impact_analysis capability_side_effects::CS_REGISTRY_V0 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | Declared and in use by ai_governance, blockchain and book_library_mgmt | REUSE | S3 impact_analysis capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Declared and in use by blockchain and book_library_mgmt | REUSE | S3 impact_analysis capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Declared and in use by blockchain and book_library_mgmt | REUSE | S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Declared and in use by ai_governance, blockchain and book_library_mgmt | REUSE | S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Declared and in use by ai_governance and blockchain | REUSE | S3 impact_analysis capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| capability_transforms::CONSTITUTION_MOLECULES_V0 | Governs how a molecule runs; no transform in the composition is a molecule yet | REUSE | S4 dependency_graph #8 |
| capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | Governs a step whose result is not determined by its inputs; none is declared yet | REUSE | S4 dependency_graph #9 |

Every artifact is read, never modified, so no consumer of any of them is affected by this change.

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| MODEL_RESPONSE_OWNS_ITS_STORES | Every store model_response reads or writes is declared by model_response, and no operation writes into a store another subdomain owns. | S4 constraint_register #22 |
| AUTHORIZATION_IS_READ_NEVER_GRANTED | Model response confirms model staff and a requester's authority to act for the customer on every operation, and grants authorization nowhere. | S4 design_decisions #12 |
| RULES_ACT_WHILE_WRITING | Each pass of writing runs two declared steps, the model's offer and the rules' choice, so each word's rule decision is a step governance can see. | S4 constraint_register #18 |
| DETERMINISM_ENDS_AT_THE_MODEL | Only the model's step is declared as giving results not determined by its inputs; every other step is declared deterministic. | S4 constraint_register #19 |
| RESPONSE_REPRODUCED_FROM_RECORD | The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly. | S4 constraint_register #20 |
| SEED_IS_A_RECORDED_INPUT | The rules' step draws from a stated seed recorded with the rules in force, and never draws one itself. | S4 constraint_register #21 |
| REFUSED_BEFORE_THE_MODEL_SEES_IT | A user prompt refused on registration, service, sensitivity or length never reaches the model's step. | S4 constraint_register #15 |
| NOTHING_ELSE_REACHES_THE_MODEL | The model's step reads the question, the supporting material and the system prompt, and nothing else. | S4 constraint_register #6 |
| EVERY_USER_PROMPT_IS_RECORDED | Every user prompt, responded to or refused, appends one entry to the user prompt record, and no entry is amended. | S4 constraint_register #9 |
| ONE_OPEN_TIME_IN_SERVICE | A model has at most one open time in service, and placement is refused while one is open. | S4 constraint_register #3 |
| READS_RAISE_NO_EVENT | Retrieving a user prompt record is recorded in the operation trail and recognises no business moment. | S4 design_decisions #11 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Register a model | model_response | S6 ownership Register a model |
| Place a model in service, and withdraw it | model_response | S6 ownership Place a model in service, and withdraw it |
| Submit a user prompt and release or refuse the model response | model_response | S6 ownership Submit a user prompt and release or refuse the model response |
| Retrieve a user prompt record | model_response | S6 ownership Retrieve a user prompt record |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | model_response | S6 ownership Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached |
| Offer the model's next words, with a result not determined by its inputs | model_response | S6 ownership Offer the model's next words, with a result not determined by its inputs |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | model_response | S6 ownership Choose one permitted word under the response rules, the freedom of word choice and a stated seed |
| Confirm the staff member is model staff, and the requester may act for the customer | model_response | S6 ownership Confirm the staff member is model staff, and the requester may act for the customer |
| Record each performed operation in the subdomain's own trail | model_response | S6 ownership Record each performed operation in the subdomain's own trail |
| Run a composed body once per pass of a transform's loop | platform | S6 ownership Run a composed body once per pass of a transform's loop |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
