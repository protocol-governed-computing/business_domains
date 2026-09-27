# Stage 4 — Business Model: causal_language_model / model_response

**Stage:** 4 — Business Model
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

This document consolidates Stages 1 to 3. It re-litigates nothing and introduces no design: every
row carries the prior-stage finding it came from, and every capability Stage 3 committed appears in
the capability graph exactly as Stage 3 stated it.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| Authorized model staff | Registers models, places them in service with their sensitivity ceiling, system prompt and response rules, withdraws them, and retrieves user prompt records | Operator | S1 authority_boundaries The sensitivity ceiling, system prompt and response rules for a time in service |
| Authorized requester | Submits a user prompt on behalf of one customer, and states the kind of information it contains | Operator | S1 authority_boundaries The kind of information a user prompt contains |
| Customer | The person on whose behalf a user prompt is submitted, and whose own accounts the question is about | Beneficiary | S1 business_vocabulary — Customer |
| Model provider | Supplies a model and asserts its training fingerprint, which the business records and does not verify | Claimant | S1 known_facts — the training fingerprint is the provider's claim |
| The business's existing arrangements | Decide which requesters may act for which customers, and which staff are model staff; not part of this change | Deferred authority | S1 authority_deferrals #1 |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Model | A language model the business holds, identified by its description and training fingerprint together | One durable record per model, addressed by its description and fingerprint together, never duplicated, carrying its own state | S2 entities Model |
| Time in Service | One period during which a model is in service, with exactly one sensitivity ceiling, system prompt and set of response rules | One durable record per period, naming the one model it belongs to, open until the model is withdrawn; at most one open per model | S2 entities Time in Service |
| User Prompt Record | The record kept of every user prompt, responded to or refused | An append-only trail, one entry per user prompt, never rewritten | S2 entities User Prompt Record |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| Model records | The business's single record of every model it holds | S2 entities Model |
| Times in service | The record of every period a model was in service, with the rules it was under | S2 entities Time in Service |
| User prompt records | The complete record of every user prompt, what the model read, the rules in force and the outcome | S2 entities User Prompt Record |
| Operation trail | The subdomain's own durable record of every operation performed | S3 authoring_decisions Record each performed operation in the subdomain's own trail |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| Model registered | Authorized model staff register a model | The business holds a record of the model | S1 business_events Model Registered |
| Model placed in service | Authorized model staff place a registered model in service with its sensitivity ceiling, system prompt and response rules | A time in service begins, and the model may respond | S1 business_events Model Placed In Service |
| Model withdrawn from service | Authorized model staff withdraw a model from service | The time in service ends, and the model responds to no one | S1 business_events Model Withdrawn From Service |
| User prompt responded | A model finishes a response under the response rules | A model response is released and recorded with what it was written from and under which rules | S1 business_events User Prompt Responded |
| User prompt refused | A user prompt yields no model response | The refusal and its reason are recorded | S1 business_events User Prompt Refused |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Model | is identified by | Description and training fingerprint | Refuse a registration whose description and fingerprint match a registered model | S1 identity_and_sameness #1 |
| Time in service | belongs to | Model | Open at most one time in service per model, and close it on withdrawal | S1 business_invariants — a model has at most one time in service at any moment |
| User prompt | is submitted to | Model in service | Refuse a user prompt before the model sees it when the model is not registered or not in service | S1 operation_refusals #5 |
| Response rules | act on | Each word the model is about to write | Stop a forbidden word while the model writes, and choose a permitted one | S1 known_facts — when the model is about to write a word a rule forbids, the rule stops that word |
| Authorized requester | acts for | Customer | Confirm the requester may act for the customer before the user prompt proceeds | S1 operation_refusals #9 |
| User prompt | is recorded in | User prompt record | Record every user prompt, responded to or refused, with what the model read | S1 business_invariants — every user prompt is recorded |

---

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Hold a model record durably and change its state in place | S3 authoring_decisions Hold a model record durably and change its state in place | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Hold a time in service durably and close it on withdrawal | S3 authoring_decisions Hold a time in service durably and close it on withdrawal | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Enforce that one record exists per model | S3 authoring_decisions Enforce that one record exists per model | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Form the key that identifies a model | S3 authoring_decisions Form the key that identifies a model | CRITICAL | GAP-01 | Nothing in the composition satisfies it. |
| Keep every user prompt record, answered or refused | S3 authoring_decisions Keep every user prompt record, answered or refused | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Assemble and validate the subdomain's records | S3 authoring_decisions Assemble and validate the subdomain's records | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Confirm the parameters supplied to an operation satisfy their declared rules | S3 authoring_decisions Confirm the parameters supplied to an operation satisfy their declared rules | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Declare the kinds of information in their order | S3 authoring_decisions Declare the kinds of information in their order | CRITICAL | GAP-02 | Nothing in the composition satisfies it. |
| Confirm a stated kind of information is one of the declared kinds | S3 authoring_decisions Confirm a stated kind of information is one of the declared kinds | SATISFIED |  | Reused as-is from the composition; read, never modified. |
| Refuse a kind of information more sensitive than the ceiling | S3 authoring_decisions Refuse a kind of information more sensitive than the ceiling | CRITICAL | GAP-03 | Nothing in the composition satisfies it. |
| Assemble what the model reads, and refuse it when it is longer than the model can read at once | S3 authoring_decisions Assemble what the model reads, and refuse it when it is longer than the model can read at once | CRITICAL | GAP-04 | Nothing in the composition satisfies it. |
| Form the response rules in force for one user prompt | S3 authoring_decisions Form the response rules in force for one user prompt | CRITICAL | GAP-05 | Nothing in the composition satisfies it. |
| Offer the model's next words, with a result not determined by its inputs | S3 authoring_decisions Offer the model's next words, with a result not determined by its inputs | CRITICAL | GAP-06 | Nothing in the composition satisfies it. |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | S3 authoring_decisions Choose one permitted word under the response rules, the freedom of word choice and a stated seed | CRITICAL | GAP-07 | Nothing in the composition satisfies it. |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | S3 authoring_decisions Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | CRITICAL | GAP-08 | Nothing in the composition satisfies it. |
| Run a composed body once per pass of a transform's loop | S3 authoring_decisions Run a composed body once per pass of a transform's loop | SATISFIED | GAP-09 | Owned by platform: capability_transforms::CONSTITUTION_MOLECULES_V0, declared and run. |
| A test model that tries to write another customer's account number | S3 authoring_decisions A test model that tries to write another customer's account number | CRITICAL | GAP-10 | Nothing in the composition satisfies it. |
| Model staff and requester actors whose authorization an operation binds | S3 authoring_decisions Model staff and requester actors whose authorization an operation binds | CRITICAL | GAP-11 | Nothing in the composition satisfies it. |
| Confirm the staff member is model staff, and the requester may act for the customer | S3 authoring_decisions Confirm the staff member is model staff, and the requester may act for the customer | CRITICAL | GAP-12 | Nothing in the composition satisfies it. |
| Register a model | S3 authoring_decisions Register a model | CRITICAL | GAP-13 | Nothing in the composition satisfies it. |
| Place a model in service, and withdraw it | S3 authoring_decisions Place a model in service, and withdraw it | CRITICAL | GAP-14 | Nothing in the composition satisfies it. |
| Submit a user prompt and release or refuse the model response | S3 authoring_decisions Submit a user prompt and release or refuse the model response | CRITICAL | GAP-15 | Nothing in the composition satisfies it. |
| Retrieve a user prompt record | S3 authoring_decisions Retrieve a user prompt record | CRITICAL | GAP-16 | Nothing in the composition satisfies it. |
| Record each performed operation in the subdomain's own trail | S3 authoring_decisions Record each performed operation in the subdomain's own trail | CRITICAL | GAP-17 | Nothing in the composition satisfies it. |
| Declare the subdomain's stores and bind its operations to them | S3 authoring_decisions Declare the subdomain's stores and bind its operations to them | CRITICAL | GAP-18 | Nothing in the composition satisfies it. |
| A governed entry point for each operation | S3 authoring_decisions A governed entry point for each operation | CRITICAL | GAP-19 | Nothing in the composition satisfies it. |
| A business moment for each of the five events | S3 authoring_decisions A business moment for each of the five events | CRITICAL | GAP-20 | Nothing in the composition satisfies it. |

---

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| model_response | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 dependency_discoveries Durable record storage |
| model_response | capability_side_effects::CS_REGISTRY_V0 | capability call | SATISFIED | S3 dependency_discoveries Uniqueness |
| model_response | capability_side_effects::CS_APPENDONLY_JSONL_V0 | capability call | SATISFIED | S3 dependency_discoveries Append-only trail |
| model_response | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | capability call | SATISFIED | S3 dependency_discoveries Record assembly |
| model_response | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | capability call | SATISFIED | S3 dependency_discoveries Record shape validation |
| model_response | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | capability call | SATISFIED | S3 dependency_discoveries Parameter validation |
| model_response | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | capability call | SATISFIED | S3 dependency_discoveries Value-set membership |
| model_response | capability_transforms::CONSTITUTION_MOLECULES_V0 | molecule execution | SATISFIED | S3 dependency_discoveries Molecule execution |
| model_response | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | non-deterministic step | SATISFIED | S3 dependency_discoveries Non-deterministic step |
| model_response | The business's existing arrangements | data read | GAP | S1 authority_deferrals #1 |

The dependencies on the platform are satisfied: it declares and runs molecules and steps whose result
is not determined by their inputs. The dependency on the business's existing arrangements is owned by the business, not by this change: the subdomain reads
whether a requester may act for a customer and whether staff are model staff, and decides neither.

---

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Each model the business holds has exactly one record. | S1 business_invariants #1 | invariant |
| 2 | No model responds to a user prompt unless it is registered and in service. | S1 business_invariants #2 | invariant |
| 3 | A model has at most one time in service at any moment. | S1 business_invariants #3 | invariant |
| 4 | Each time in service has exactly one system prompt and one set of response rules. | S1 business_invariants #4 | invariant |
| 5 | No model reads a more sensitive kind of information than its sensitivity ceiling. | S1 business_invariants #5 | invariant |
| 6 | No model reads anything but the question, the supporting material and its system prompt. | S1 business_invariants #6 | invariant |
| 7 | No model response is released that breaks a response rule. | S1 business_invariants #7 | invariant |
| 8 | No model response is released that reached the longest response before it was finished. | S1 business_invariants #8 | invariant |
| 9 | Every user prompt is recorded, whether responded to or refused. | S1 business_invariants #9 | invariant |
| 10 | Every refusal carries its reason. | S1 business_invariants #10 | invariant |
| 11 | Every business operation is traceable and auditable. | S1 business_invariants #11 | invariant |
| 12 | Capabilities deferred to future change requests must not be designed into this solution. | S1 constraints #1 | governance rule |
| 13 | Response rules apply while the model writes, not afterwards. | S1 constraints #2 | business policy |
| 14 | The requester cannot change the response rules or the system prompt. | S1 constraints #5 | business policy |
| 15 | A user prompt refused before the model sees it never reaches the model. | S1 constraints #7 | business policy |
| 16 | The record keeps exactly what the model read, not only a summary or fingerprint of it. | S1 constraints #8 | business policy |
| 17 | The business must not claim that a model response is true. | S1 constraints #9 | business policy |
| 18 | Each pass of writing runs two declared steps, the model's offer and the rules' choice, so each word's rule decision is visible. | S3 analysis_findings #1 | governance rule |
| 19 | Only the model's step is declared as giving results not determined by its inputs. | S3 analysis_findings #2 | governance rule |
| 20 | The model's offered words are recorded, and a replay of a user prompt from its record reproduces its trace exactly. | S3 analysis_findings #3 | governance rule |
| 21 | The rules' step draws from a stated seed, recorded with the rules in force, and never draws one itself. | S3 analysis_findings #10 | governance rule |
| 22 | The subdomain appends only to stores it owns. | S3 authoring_decisions Record each performed operation in the subdomain's own trail | governance rule |

---

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Form the key that identifies a model | Form the key that identifies a model | model_response | NEW |
| GAP-02 | S3 authoring_decisions Declare the kinds of information in their order | Declare the kinds of information in their order | model_response | NEW |
| GAP-03 | S3 authoring_decisions Refuse a kind of information more sensitive than the ceiling | Refuse a kind of information more sensitive than the ceiling | model_response | NEW |
| GAP-04 | S3 authoring_decisions Assemble what the model reads, and refuse it when it is longer than the model can read at once | Assemble what the model reads, and refuse it when it is longer than the model can read at once | model_response | NEW |
| GAP-05 | S3 authoring_decisions Form the response rules in force for one user prompt | Form the response rules in force for one user prompt | model_response | NEW |
| GAP-06 | S3 authoring_decisions Offer the model's next words, with a result not determined by its inputs | Offer the model's next words, with a result not determined by its inputs | model_response | NEW |
| GAP-07 | S3 authoring_decisions Choose one permitted word under the response rules, the freedom of word choice and a stated seed | Choose one permitted word under the response rules, the freedom of word choice and a stated seed | model_response | NEW |
| GAP-08 | S3 authoring_decisions Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | model_response | NEW |
| GAP-09 | S3 authoring_decisions Run a composed body once per pass of a transform's loop | Run a composed body once per pass of a transform's loop | platform | REUSE |
| GAP-10 | S3 authoring_decisions A test model that tries to write another customer's account number | A test model that tries to write another customer's account number | model_response | NEW |
| GAP-11 | S3 authoring_decisions Model staff and requester actors whose authorization an operation binds | Model staff and requester actors whose authorization an operation binds | model_response | NEW |
| GAP-12 | S3 authoring_decisions Confirm the staff member is model staff, and the requester may act for the customer | Confirm the staff member is model staff, and the requester may act for the customer | model_response | NEW |
| GAP-13 | S3 authoring_decisions Register a model | Register a model | model_response | NEW |
| GAP-14 | S3 authoring_decisions Place a model in service, and withdraw it | Place a model in service, and withdraw it | model_response | NEW |
| GAP-15 | S3 authoring_decisions Submit a user prompt and release or refuse the model response | Submit a user prompt and release or refuse the model response | model_response | NEW |
| GAP-16 | S3 authoring_decisions Retrieve a user prompt record | Retrieve a user prompt record | model_response | NEW |
| GAP-17 | S3 authoring_decisions Record each performed operation in the subdomain's own trail | Record each performed operation in the subdomain's own trail | model_response | NEW |
| GAP-18 | S3 authoring_decisions Declare the subdomain's stores and bind its operations to them | Declare the subdomain's stores and bind its operations to them | model_response | NEW |
| GAP-19 | S3 authoring_decisions A governed entry point for each operation | A governed entry point for each operation | model_response | NEW |
| GAP-20 | S3 authoring_decisions A business moment for each of the five events | A business moment for each of the five events | model_response | NEW |

---

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | model_response is a new subdomain, a peer of the five other project functions, rather than an extension of anything existing. | S3 placement_decision | Nothing in the composition carries the project's namespace, registers a model or governs how one writes. | The subdomain owns its records exclusively; the five other functions are adjacent and untouched. |
| 2 | A response is written word by word, each pass running two declared steps: the model offers its next words, and the response rules choose one. The writing transform is a molecule whose loop runs those two steps each pass. | S3 analysis_findings #1 | The rules must act while the model writes, visibly to governance; the platform declares and runs the construct. Decided by the business owner. | No platform extension; no schema, constitution or invariant changes. |
| 3 | Only the model's step is declared as giving results not determined by its inputs; its result is offered to the response rules' step and never decided on. | S3 analysis_findings #2 | A reader of the composition must see exactly where determinism ends, and the platform governs that step. | The rules' step and every other transform stay declared deterministic; the writing transform emits the chosen response, never the model's offer. |
| 4 | The model's offered words are recorded in the trace, and a user prompt's trace is reproduced from its record rather than compared across fresh runs. | S3 analysis_findings #3 | The platform records every result of a step not determined by its inputs; a replay substitutes the record. Decided by the business owner at rebaseline. | A model response may appear wherever the design places it; it is also kept whole in the user prompt record. |
| 5 | The rules' step draws from a stated seed recorded with the rules in force. | S3 analysis_findings #10 | Given the model's offered words, the rules and the seed, anyone reading the record can re-derive each chosen word. | The seed is an input of the rules' step, never drawn inside it. |
| 6 | The test model is a permanent realization of the model's step; a real model later joins it as a second realization. | S3 analysis_findings #11 | The rules must be shown to hold against a model that tries to break them, before and after a real model exists. | The model's step is declared by the domain; its realization is supplied outside the domain's own pure transforms. |
| 7 | The user prompt carries the customer's account numbers; the subdomain reads no customer records of its own. | S3 analysis_findings #4 | The rule against another customer's account number is formed per user prompt. Decided by the business owner. | The account numbers reach the model only if they are also part of the supporting material. |
| 8 | Uniqueness on a model is enforced by reusing the registry with a key formed from the description and fingerprint. | S3 authoring_decisions Enforce that one record exists per model | Register-if-absent gives an atomic guarantee, and forming the key is this subdomain's rule. | No side effect is modified. |
| 9 | A model's state and a time in service's openness are data on their records. | S3 authoring_decisions Hold a model record durably and change its state in place | A model moves into and out of service repeatedly. | The record store must support update in place. |
| 10 | The sensitivity check confirms membership first, then compares by the declared order. | S3 analysis_findings #5 | Membership is mechanism; the comparison is this subdomain's rule. | The kinds are declared once, in order, least sensitive first. |
| 11 | Retrieving a user prompt record is recorded in the operation trail but raises no business event. | S1 business_events Model Registered | Every operation must be traceable, while nothing reacts to a read. | Five business moments are authored, not six. |
| 12 | Authorization is read on every operation and granted nowhere in this change. | S1 authority_deferrals #1 | Which requesters may act for which customers, and which staff are model staff, is decided by the business's existing arrangements. | The subdomain authors authorization reads and no authorization grant. |

---

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Form the key that identifies a model | GAP-01 |
| Declare the kinds of information in their order | GAP-02 |
| Refuse a kind of information more sensitive than the ceiling | GAP-03 |
| Assemble what the model reads, and refuse it when it is longer than the model can read at once | GAP-04 |
| Form the response rules in force for one user prompt | GAP-05 |
| Offer the model's next words, with a result not determined by its inputs | GAP-06 |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | GAP-07 |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | GAP-08 |
| Run a composed body once per pass of a transform's loop | GAP-09 |
| A test model that tries to write another customer's account number | GAP-10 |
| Model staff and requester actors whose authorization an operation binds | GAP-11 |
| Confirm the staff member is model staff, and the requester may act for the customer | GAP-12 |
| Register a model | GAP-13 |
| Place a model in service, and withdraw it | GAP-14 |
| Submit a user prompt and release or refuse the model response | GAP-15 |
| Retrieve a user prompt record | GAP-16 |
| Record each performed operation in the subdomain's own trail | GAP-17 |
| Declare the subdomain's stores and bind its operations to them | GAP-18 |
| A governed entry point for each operation | GAP-19 |
| A business moment for each of the five events | GAP-20 |

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
