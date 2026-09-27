# Stage 2 — Domain Model Verification: causal_language_model / model_response

**Stage:** 2 — Domain Model Verification
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every claim about what exists is grounded in the pinned baseline
`f6cfaac48c1fba78ab92d38a65828b91a105ae56f0be78040cfc6b71701b13e6` — 425 artifacts across
ai_governance, blockchain, book_library_mgmt, inspection, platform, transformation, workload — read
through the inspection interface. The semantic model is inherited from Stage 1 and confirmed here,
never re-derived.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Model | A language model the business holds, identified by its description and training fingerprint together. | One durable record per model, addressed by its description and fingerprint together, never duplicated. | INFERRED | S1 identity_and_sameness #1 |
| Time in Service | One period during which a model is in service, carrying exactly one sensitivity ceiling, system prompt and set of response rules. | One durable record per period, naming the single model it belongs to, open while the model is in service and closed when it is withdrawn. At most one is open per model. | INFERRED | S1 business_invariants — a model has at most one time in service at any moment |
| User Prompt Record | The record kept of every user prompt, responded to or refused. | An append-only trail: one entry per user prompt, never rewritten. | INFERRED | S1 business_invariants — every user prompt is recorded, whether responded to or refused |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Model | Description | How the model is built; part of what identifies it. | INFERRED | S1 identity_and_sameness #1 |
| Model | Readable Length | The amount of text the model can read at once, stated in its description. | INFERRED | S1 known_facts — a registration describes how the model is built, including the amount of text it can read at once |
| Model | Training Fingerprint | The provider's claim about the model's training; part of what identifies it, recorded and not verified. | INFERRED | S1 business_vocabulary — Training Fingerprint |
| Model | State | Whether the model is registered or in service. | INFERRED | S1 lifecycle_states Model |
| Time in Service | Model | The single model this period belongs to. | INFERRED | S1 business_vocabulary — Time in Service |
| Time in Service | Sensitivity Ceiling | The most sensitive kind of information the model may read during this period. | INFERRED | S1 business_vocabulary — Sensitivity Ceiling |
| Time in Service | System Prompt | The business's standing instructions to the model during this period. | INFERRED | S1 business_vocabulary — System Prompt |
| Time in Service | Forbidden Words and Patterns | Words and patterns the model must never write during this period. | INFERRED | S1 business_vocabulary — Forbidden Words and Patterns |
| Time in Service | Freedom of Word Choice | How freely the model may choose its words during this period. | INFERRED | S1 business_vocabulary — Freedom of Word Choice |
| Time in Service | Longest Response | The longest response the model may write during this period. | INFERRED | S1 business_vocabulary — Longest Response |
| Time in Service | Open | Whether the period is current, which it is from placement until withdrawal. | INFERRED | S1 lifecycle_transitions #3 |
| User Prompt Record | Requester and Customer | Who asked, and for which customer. | INFERRED | S1 known_facts — a user prompt record holds who asked and for which customer |
| User Prompt Record | Model and Time in Service | Which model responded or was asked, and the period it was in service. | INFERRED | S1 known_facts — a user prompt record holds which model and its time in service |
| User Prompt Record | What the Model Read | Exactly the question, the supporting material and the system prompt, kept whole rather than as a summary or fingerprint. | INFERRED | S1 constraints — the record keeps exactly what the model read |
| User Prompt Record | Kind of Information | The kind of information the requester stated the user prompt contains. | INFERRED | S1 authority_boundaries — the kind of information a user prompt contains |
| User Prompt Record | Response Rules in Force | The response rules of the time in service the user prompt was submitted under. | INFERRED | S1 known_facts — a user prompt record holds the response rules in force |
| User Prompt Record | Outcome | The model response, or the reason the user prompt was refused, naming the rule where a rule stopped it. | INFERRED | S1 business_invariants — every refusal carries its reason |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a model | Authorized model staff | The business holds exactly one record for the model, or the registration is refused because the model is already registered. | INFERRED | S1 business_events Model Registered |
| Place a model in service | Authorized model staff | A time in service begins with its sensitivity ceiling, system prompt and response rules, or placement is refused. | INFERRED | S1 business_events Model Placed In Service |
| Withdraw a model from service | Authorized model staff | The model's time in service ends and it responds to no one. | INFERRED | S1 business_events Model Withdrawn From Service |
| Submit a user prompt | Authorized requester | A model response written under the response rules is released, or the user prompt is refused with its reason; either way it is recorded. | INFERRED | S1 business_events User Prompt Responded |
| Retrieve a user prompt record | Authorized model staff | The record of the user prompt asked for. | INFERRED | S1 known_facts — the operations required |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a model | 1 | Confirm the staff member is authorized model staff | An authorization decision | INFERRED | S1 operation_refusals #12 |
| Register a model | 2 | Confirm no registered model carries this description and fingerprint | A sameness decision | INFERRED | S1 operation_refusals #1 |
| Register a model | 3 | Record the model's description and fingerprint as its record, registered | The model record | INFERRED | S1 business_invariants — each model has exactly one record |
| Register a model | 4 | Record that the model was registered | A durable, auditable record of the operation | INFERRED | S1 business_invariants — every business operation is traceable and auditable |
| Place a model in service | 1 | Confirm the staff member is authorized model staff | An authorization decision | INFERRED | S1 operation_refusals #12 |
| Place a model in service | 2 | Confirm the model is registered | An existence decision | INFERRED | S1 operation_refusals #2 |
| Place a model in service | 3 | Confirm the model is not already in service | A state decision | INFERRED | S1 operation_refusals #3 |
| Place a model in service | 4 | Record a new time in service with its sensitivity ceiling, system prompt and response rules, and mark the model in service | The time in service record and the updated model record | INFERRED | S1 lifecycle_transitions #2 |
| Place a model in service | 5 | Record that the model was placed in service | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Withdraw a model from service | 1 | Confirm the staff member is authorized model staff | An authorization decision | INFERRED | S1 operation_refusals #12 |
| Withdraw a model from service | 2 | Confirm the model is in service | A state decision | INFERRED | S1 operation_refusals #4 |
| Withdraw a model from service | 3 | Close the time in service and mark the model registered | The closed time in service and the updated model record | INFERRED | S1 lifecycle_transitions #3 |
| Withdraw a model from service | 4 | Record that the model was withdrawn | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |
| Submit a user prompt | 1 | Confirm the requester is permitted to act for the customer | An authorization decision | INFERRED | S1 operation_refusals #9 |
| Submit a user prompt | 2 | Confirm the model is registered | An existence decision | INFERRED | S1 operation_refusals #5 |
| Submit a user prompt | 3 | Confirm the model is in service, and read its open time in service | A state decision | INFERRED | S1 operation_refusals #6 |
| Submit a user prompt | 4 | Confirm the stated kind of information is no more sensitive than the sensitivity ceiling | A sensitivity decision | INFERRED | S1 operation_refusals #7 |
| Submit a user prompt | 5 | Assemble what the model reads: the question, the supporting material and the system prompt, and nothing else | What the model reads | INFERRED | S1 constraints — nothing reaches the model except the question, the supporting material and the system prompt |
| Submit a user prompt | 6 | Confirm what the model reads is no longer than the model can read at once | A length decision | INFERRED | S1 operation_refusals #8 |
| Submit a user prompt | 7 | Form the forbidden words and patterns for this user prompt, using the account numbers of the customer it is for | The rules in force for this user prompt | INFERRED | S1 known_facts — "another customer's account number" depends on who the customer is |
| Submit a user prompt | 8 | Write the response one word at a time: the model offers its next words, the response rules stop any forbidden word, and one permitted word is chosen under the freedom of word choice | The response so far, and the words the rules stopped | INFERRED | S1 known_facts — when the model is about to write a word a rule forbids, the rule stops that word and the model continues with a permitted one |
| Submit a user prompt | 9 | Stop writing when the response is finished, when no permitted word remains, or when the longest response is reached | A completion decision | INFERRED | S1 operation_refusals #10 |
| Submit a user prompt | 10 | Release the response if it finished; otherwise refuse, naming the rule that stopped it or the length reached | The model response or the refusal | INFERRED | S1 operation_refusals #11 |
| Submit a user prompt | 11 | Record the user prompt with its requester, customer, model, time in service, what the model read, kind of information, rules in force and outcome | The user prompt record | INFERRED | S1 business_invariants — every user prompt is recorded, whether responded to or refused |
| Retrieve a user prompt record | 1 | Confirm the staff member is authorized model staff | An authorization decision | INFERRED | S1 operation_refusals #12 |
| Retrieve a user prompt record | 2 | Read the user prompt record asked for | The user prompt record | INFERRED | S1 known_facts — the operations required |
| Retrieve a user prompt record | 3 | Record that the record was retrieved | A durable, auditable record of the operation | INFERRED | S1 business_invariants — traceable and auditable |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| causal_language_model is not part of the current software baseline. | NOT_FOUND | The composition declares seven domains — ai_governance, blockchain, book_library_mgmt, inspection, platform, transformation, workload — and its artifact index carries no identity in the causal_language_model namespace. | S1 system_beliefs #1 |
| No capability in the current composition registers language models or governs how a model writes a response. | NOT_FOUND | Semantic vocabulary search returns no identity for prompt, token, sensitivity, confidential, customer, account or instruction. The identities matching model are transformation::IN_BUSINESS_MODEL_SUBMITTED_V0, transformation::IN_DOMAIN_MODEL_SUBMITTED_V0 and their two admissibility workflows, which judge design documents. ai_governance::WF_GOVERN_AGENT_ACTION_V0 mediates actions an agent proposes, against license-tier authority, after the proposal is made; it registers no model and governs no writing. | S1 system_beliefs #2 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Uniqueness registry | capability_side_effects::CS_REGISTRY_V0 | Registers a key, resolves it, reports whether it exists, counts and deregisters. | PARTIAL | It enforces uniqueness on one key; a model is identified by its description and fingerprint together, and the composite is not a key it forms. |
| Identity key formation | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | Forms a single key from the attributes that identify a book. | PARTIAL | It forms a book's key; the model's key must be formed from its own attributes. |
| Durable record store | capability_side_effects::CS_MUTABLE_JSON_V0 | Writes, reads, lists, updates in place and deletes durable records. | EXACT | It holds whatever it is given; it enforces no identity, no state and no authorization. |
| Append-only trail | capability_side_effects::CS_APPENDONLY_JSONL_V0 | Appends an entry and returns the whole trail. | EXACT | It appends what it is handed; it does not decide which operations must be recorded. |
| Record shape validation | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Confirms a record carries the fields its contract declares. | EXACT | It does not know which fields a model or a user prompt requires. |
| Record assembly | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Assembles a durable record from supplied values. | EXACT | It applies no identity rule and decides no sameness. |
| Set membership | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Confirms a value belongs to a declared set. | PARTIAL | It confirms membership, not order; comparing a kind of information with a ceiling needs the order of the kinds. |
| Parameter rule validation | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Confirms supplied parameters satisfy declared rules. | PARTIAL | It judges supplied values once; it does not act while a response is written. |
| Controlled value set | blockchain::VOCAB_WALLET_CLASSIFICATION_V0 | Declares a closed list of values a subdomain uses. | EXACT | It declares a wallet's classifications, not kinds of information. |
| Authorization check | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | Confirms a staff member may perform a subdomain's operations. | PARTIAL | It confirms catalog staff; model staff and requesters acting for a customer are not its concern. |
| Operation trail | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | Composes the recording of a performed operation into the subdomain's own trail. | PARTIAL | It appends to the catalog's store; a subdomain owns its stores exclusively. |
| Business actor | book_library_mgmt::AC_LIBRARY_STAFF_V0 | Declares a business actor whose identity an operation binds. | PARTIAL | It names library staff; neither model staff nor requesters exist. |
| Subdomain storage declaration | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 | Declares the stores a business subdomain owns and the paths they occupy. | EXACT | It declares another subdomain's stores. |
| Runtime binding declaration | book_library_mgmt::RB_CATALOG_BINDINGS_V0 | Binds a subdomain's workflows to the stores and policies they use. | EXACT | It binds another subdomain's surface. |
| Repeated computation | workload::CT_PURE_COLLATZ_STEP_V0 | Computes a whole repeated sequence for each input within one transform. | PARTIAL | The repetition happens inside one transform, so no step within it is visible to governance; a response written word by word under rules needs each word's rule decision to be visible. |
| Agent action mediation | ai_governance::WF_GOVERN_AGENT_ACTION_V0 | Mediates an action an agent proposes, against the authority its license grants. | MISMATCH | It judges a finished proposal; it does not act while a response is written. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing in the composition holds a model record, a time in service or a user prompt record. | CRITICAL | Every requested outcome depends on these records; the store mechanisms exist, the subdomain's own stores do not. | OBSERVED | S2 belief_verification #2 |
| No capability registers a model, places one in service, withdraws one, accepts a user prompt, or retrieves a user prompt record. | CRITICAL | The five business processes have no counterpart in the composition and must all be authored. | OBSERVED | S2 belief_verification #2 |
| Nothing writes a response word by word with the response rules acting on each word as a step governance can see. | CRITICAL | The central requested outcome is that rules apply while the model writes. The only repeated computation composed today keeps its repetition inside one transform, where no rule decision is visible. | OBSERVED | S1 requested_outcomes #1 |
| No actor exists for model staff or for requesters, and none asserts authority to act for a customer. | CRITICAL | Every operation is refused unless its initiator is authorized, and there is nothing to bind that decision to. | OBSERVED | S1 operation_refusals #12 |
| No business moment exists for a model being registered, placed in service or withdrawn, or for a user prompt being responded to or refused. | CRITICAL | Five business events are declared and none is recognised anywhere in the composition. | OBSERVED | S1 business_events Model Registered |
| Uniqueness on a model's description and fingerprint together has no counterpart in the composition. | MAJOR | Duplicate registration must be refused, and the registry available enforces uniqueness on a single key. | OBSERVED | S1 identity_and_sameness #1 |
| No kinds of information, and no ordering between them, are declared anywhere. | MAJOR | A user prompt is refused when its kind is more sensitive than the ceiling, which needs the kinds and their order. | OBSERVED | S1 known_facts — the kinds of information, from least to most sensitive |
| No test model exists. | MAJOR | The business sees the rules hold only through a model that tries to break them. | OBSERVED | S1 requested_outcomes #6 |
| Deciding which requesters may act for which customers, and which staff are model staff, is deferred to the business's existing arrangements, which the composition does not hold. | MINOR | Noted, not modelled: the subdomain reads authorization and never grants it. | OBSERVED | S1 authority_deferrals #1 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A business subdomain in this composition declares its own stores and binds its own operations to them, so a new subdomain has a worked precedent for owning its records. | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 · book_library_mgmt::RB_CATALOG_BINDINGS_V0 | OBSERVED | S2 belief_verification #1 |
| Registering something once, identified by several attributes together, has a worked precedent: a key formed from the attributes and a uniqueness registry keyed on it. | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 · capability_side_effects::CS_REGISTRY_V0 | OBSERVED | S1 identity_and_sameness #1 |
| Operations in this composition are declared as step sequences that may not return to an earlier step. | workflow::CONSTITUTION_WORKFLOW_V0 · workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0 | OBSERVED | S1 known_facts — a language model writes a response one word at a time |
| Transforms are placed by what they declare: a deterministic atom, a molecule, or an atom whose result is not determined by its inputs, each governed by its own constitution. Every result of such an atom is recorded when produced, a replay substitutes the record and never runs the atom, and its result is offered to a deterministic step rather than decided on. No transform in the composition is yet declared so. | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 · capability_transforms::INVARIANT_CT_GOVERNED_BY_KIND_V0 · capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0 | OBSERVED | S1 known_facts — nobody can predict a language model's exact response in advance |
| A transform may be a molecule: declared steps, including a loop that runs a composed body once per member of a collection and carries its values between passes. The runtime runs it, and records each step it runs. No composition yet carries a molecule. | capability_transforms::CONSTITUTION_MOLECULES_V0 · capability_transforms::INVARIANT_MOLECULE_RUNNABLE_V0 | OBSERVED | S1 known_facts — a language model writes a response one word at a time |
| The execution trace declares which of its content is determinative and which is merely observational. A step's detail is determinative, and for an atom whose result is not determined by its inputs that detail carries the result's values. | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 | OBSERVED | S1 known_facts — given the same question twice, it may respond differently |
| Recording a performed operation into the subdomain's own trail is already composed as a governed step, within another subdomain. | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 | OBSERVED | S1 business_invariants — every business operation is traceable and auditable |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Writing word by word repeats, while operations may not return to an earlier step. The repetition must therefore live below the operation. The platform declares and runs the form it takes — a molecule's loop — and the only composed precedent keeps the repetition inside one atom, where no rule decision is visible. | workflow::CONSTITUTION_WORKFLOW_V0 · capability_transforms::CONSTITUTION_MOLECULES_V0 | MAJOR | OBSERVED | S1 requested_outcomes #1 |
| The model is the first capability whose result is not determined by its inputs. The platform declares where such a capability belongs, and requires that its result be offered to a deterministic step and never decided on; no composition yet carries one. | capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 · capability_transforms::INVARIANT_NONDETERMINISM_NOT_ROUTED_V0 | MAJOR | OBSERVED | S1 known_facts — nobody can predict a language model's exact response in advance |
| A model's offered words differ between runs of the same user prompt, and the trace records them as determinative, so two fresh runs of the same user prompt yield different traces. A replay from the record reproduces one exactly. | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 · capability_transforms::CONSTITUTION_NONDETERMINISTIC_ATOMS_V0 | MAJOR | OBSERVED | S1 known_facts — given the same question twice, it may respond differently |
| The rule against another customer's account number needs the account numbers of the customer the user prompt is for, and the statement does not say where the subdomain reads them from. | — | MAJOR | INFERRED | S1 known_facts — "another customer's account number" depends on who the customer is |
| Comparing a kind of information with a ceiling needs the kinds' order, and the available value-set check confirms membership only. | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | MINOR | OBSERVED | S1 known_facts — the kinds of information, from least to most sensitive |
| A user prompt record keeps whole what the model read, so its entries are as large as the material submitted. | capability_side_effects::CS_APPENDONLY_JSONL_V0 | MINOR | INFERRED | S1 constraints — the record keeps exactly what the model read |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Where does the subdomain read the customer's account numbers from, to form the rule against another customer's account number? | BUSINESS | The rule cannot be formed for a user prompt without them. | S2 discovery_concerns #4 |
| How can each word's rule decision be a step governance can see, when the repetition must live below the operation? | ARCHITECTURE | It decides whether the rules visibly act while the model writes, which is the central requested outcome. | S2 discovery_concerns #1 |
| How is a capability declared whose result is not determined by its inputs? | ARCHITECTURE | The model is such a capability, and no composition yet carries one. | S2 discovery_concerns #2 |

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
