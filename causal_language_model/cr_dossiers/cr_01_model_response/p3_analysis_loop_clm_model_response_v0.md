# Stage 3 — Analysis Loop: causal_language_model / model_response

**Stage:** 3 — Analysis Loop
**CR:** cr_01_model_response
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every decision below is grounded in the pinned baseline
`1b0cfbd3d094b7e93a965135c32b9f94ba8c3c43c0a1e8e8aacac8ebbdc9d010`, re-read at this stage rather
than inherited from Stage 2. Two questions could not be settled by evidence and were decided by the
business owner: where the customer's account numbers come from, and how each word's rule decision is
made visible to governance.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| S2 discovery_concerns #1 | Operations may not return to an earlier step, so writing word by word must repeat below the operation. The platform already declares the construct: a transform whose loop step runs a composed body once per pass, carrying the response so far between passes. The compiler already emits a loop whose body is a composed transform. The runtime cannot yet run it: each pass is dispatched as a single step, and a composed body carries no single implementation to dispatch. The business owner decided to extend the runtime within this change so that a loop's body may be a composed transform. Each pass then runs two declared steps: the model offers its next words, and the response rules choose one. | Each word's rule decision becomes a step governance can see. One runtime extension is carried by this change; no schema, constitution or invariant changes. | OBSERVED | HIGH | CLOSED | si.artifact.list --kind CT reports 28 transforms, all atoms, so no composed transform runs in the composition today. Running the compiler's loop shape through the runtime's transform executor raises CTExecutionError "CT-IR step missing handler_ref". Decided by the business owner at this stage. |
| S2 discovery_concerns #2 | A transform declares its purity class: none, emits a value, or has effects. The model's step is declared as a transform whose result is not determined by its inputs. Nothing in the compiler or the runtime reads the purity class, and the purity assertion checks only that business outcomes are returned rather than raised. The declaration is therefore lawful, inspectable and inert, and it names exactly where determinism ends: at the model's step, and nowhere else. | The response rules' step stays deterministic and is declared so; a reader of the composition sees which single step is not. | OBSERVED | HIGH | CLOSED | capability_transforms::CT_EXEC_EMIT_V0 is declared ct_exec and every other transform ct_pure. capability_transforms::INVARIANT_ATOM_OUTPUT_PURITY_V0 is enforced by an assertion over raised exceptions only. No compiler or runtime source reads ct_purity. |
| S2 discovery_concerns #3 | The execution trace records, for a transform's step, only the names of its results, never their values. It records the inputs of a governed operation and the payload of a business moment. A model response kept out of operation inputs and moment payloads therefore never enters trace content that is compared between runs. It is kept whole in the subdomain's own user prompt record. | Two faithful runs of the same user prompt yield comparable traces. Stage 7 carries the constraint that no business moment's payload and no operation's input carries a model response. | OBSERVED | HIGH | CLOSED | The runtime's evidence emitter records result keys at step completion, inputs at operation start, and the payload at a business moment. vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 declares detail determinative. |
| S2 discovery_concerns #4 | The user prompt carries the account numbers of the customer it is for, taken from the business's existing records. They form the rule against another customer's account number for that user prompt, and reach the model only if they are also part of the supporting material. | The rule is formed per user prompt from what the user prompt carries; the subdomain reads no customer records of its own. | OBSERVED | HIGH | CLOSED | Answered by the business owner and folded into the problem statement's clarifications; S1 known_facts carries it. |
| S2 discovery_concerns #5 | The kinds of information are declared as an ordered list, least sensitive first. Comparing a kind with a ceiling is a small pure comparison over that order, which the membership check does not perform. Membership is still checked first. | One pure comparison is authored; the membership check is reused beneath it. | OBSERVED | HIGH | CLOSED | Declared value sets carry their entries as an ordered list, as blockchain::VOCAB_WALLET_CLASSIFICATION_V0 does. capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 confirms membership only. |
| S2 discovery_concerns #6 | A user prompt record keeps whole what the model read, so its entries are as large as what was submitted. The append-only trail appends whatever it is handed. | Accepted: no limit on record size was stated. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_APPENDONLY_JSONL_V0 publishes APPEND and GET_ALL with no size constraint. |
| S2 open_questions #1 | Answered as S3 analysis_findings #4. | — | OBSERVED | HIGH | CLOSED | See S3 analysis_findings #4. |
| S2 open_questions #2 | Answered as S3 analysis_findings #1. | — | OBSERVED | HIGH | CLOSED | See S3 analysis_findings #1. |
| S2 open_questions #3 | Answered as S3 analysis_findings #2. | — | OBSERVED | HIGH | CLOSED | See S3 analysis_findings #2. |
| S2 process_steps Submit a user prompt #8 | Choosing a word more adventurously than the most likely one is a random draw. The response rules' step is deterministic only when the draw is made from a stated seed. The seed is therefore part of what the rules act under, and is kept in the user prompt record with the rules in force. | Given the model's offered words, the rules and the seed, the chosen word can be re-derived by anyone reading the record. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7 as a design obligation: the seed is a recorded input of the rules' step, never drawn inside it. |
| S2 gaps #8 | The test model is the realization of the model's step until a real model is available. It is a permanent conformance realization, not scaffolding, and it deliberately offers another customer's account number among its next words. A real model later joins it as a second realization of the same declared step. | The rules are shown to hold against a model that tries to break them, and changing the model later changes only which realization the step names. | INFERRED | HIGH | CLOSED | Carried forward to Stage 7: the step's declaration is the domain's; its realization is supplied outside the domain's own pure transforms. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| causal_language_model is not part of the current software baseline. | S2 belief_verification #1 | CONFIRMED | Re-read at this stage: si.artifact.list for domain causal_language_model returns nothing, and si.snapshot.summary reports seven domains over 407 artifacts. |
| No capability in the current composition registers language models or governs how a model writes a response. | S2 belief_verification #2 | CONFIRMED | Re-read at this stage: si.vocab.search returns no identity for prompt, token, sensitivity, confidential, customer, account or instruction; the model matches are four design-document admissibility identities in the transformation domain. |
| A business subdomain declares its own stores and binds its own operations to them. | S2 architectural_observations #1 | CONFIRMED | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 declares that subdomain's stores; book_library_mgmt::RB_CATALOG_BINDINGS_V0 binds its surface. |
| Registering something identified by several attributes together has a worked precedent. | S2 architectural_observations #2 | CONFIRMED | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 forms one key; capability_side_effects::CS_REGISTRY_V0 publishes register-if-absent on it. |
| Operations are step sequences that may not return to an earlier step. | S2 architectural_observations #3 | CONFIRMED | workflow::CONSTITUTION_WORKFLOW_V0 and workflow::INVARIANT_WF_EXECUTION_PATH_VALID_V0 are carried by the artifact index. |
| No transform is declared to give different results from the same inputs. | S2 architectural_observations #4 | CONFIRMED | si.artifact.list --kind CT reports 28 transforms: capability_transforms::CT_EXEC_EMIT_V0 declared ct_exec, every other ct_pure. |
| The trace declares which of its content is determinative. | S2 architectural_observations #5 | CONFIRMED | vocabulary::VOCAB_EVIDENCE_CONTENT_CLASSIFICATION_V0 declares determinative and observational fields. |
| Recording a performed operation into a subdomain's own trail is composed as a governed step. | S2 architectural_observations #6 | CONFIRMED | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 is carried by the artifact index. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, EXTEND, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | Durable record storage | REUSE | Publishes WRITE, READ, LIST, UPDATE; a model's state and a time in service's open flag change in place. |
| capability_side_effects::CS_REGISTRY_V0 | Uniqueness | REUSE | Publishes register-if-absent, keyed on one value formed from the model's description and fingerprint. |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | Append-only trail | REUSE | Publishes APPEND and GET_ALL; holds the user prompt record and the operation trail. |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Record assembly | REUSE | Assembles a durable record from supplied values. |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Record shape validation | REUSE | Confirms a record carries its declared fields. |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Parameter validation | REUSE | Confirms supplied parameters satisfy declared rules. |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Value-set membership | REUSE | Confirms a stated kind of information is one of the declared kinds. |
| The runtime's execution of a transform's loop | Platform execution | EXTEND | The loop's body may be a composed transform, run as its own sequence of steps each pass; the construct is declared and the compiler emits it. |
| The subdomain's stores: models, times in service, user prompt records, operation trail | Store declaration | AUTHOR_NEW | No store in the composition holds any of them. |
| Model staff and requester actors, and their authorization checks | Business actor | AUTHOR_NEW | No actor in the composition names either. |
| The model's step, the response rules' step, and the composed writing transform | Transform | AUTHOR_NEW | No transform in the composition offers or chooses words. |
| Five operations, their entry points and five business moments | Governed operation surface | AUTHOR_NEW | Semantic vocabulary search returns no identity for any of them. |
| The test model | Conformance realization | AUTHOR_NEW | No realization of a model exists. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| capability_side_effects::CS_MUTABLE_JSON_V0 | ai_governance, blockchain, book_library_mgmt, workload | 76 | si.topology.impact impacted_count 76 |
| capability_side_effects::CS_REGISTRY_V0 | ai_governance, blockchain, book_library_mgmt | 68 | si.topology.impact impacted_count 68 |
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | ai_governance, blockchain, book_library_mgmt | 85 | si.topology.impact impacted_count 85 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | blockchain, book_library_mgmt | 56 | si.topology.impact impacted_count 56 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | blockchain, book_library_mgmt | 33 | si.topology.impact impacted_count 33 |
| capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | ai_governance, blockchain, book_library_mgmt | 44 | si.topology.impact impacted_count 44 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | ai_governance, blockchain | 18 | si.topology.impact impacted_count 18 |
| book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 | book_library_mgmt | 29 | si.topology.impact impacted_count 29 — examined as the worked form and not reused |
| book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 | book_library_mgmt | 22 | si.topology.impact impacted_count 22 — examined as the worked form and not reused |
| workload::CT_PURE_COLLATZ_STEP_V0 | workload | 3 | si.topology.impact impacted_count 3 — examined and not reused |

Every reused artifact is read, never modified, so this change adds consumers and disturbs none of the
counts above. The runtime extension adds a way to run a composed loop body; no transform in the
composition has one, so nothing that runs today runs differently.

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Hold a model record durably and change its state in place | REUSE | A model moves between registered and in service, so its state is data on the record. | capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is. | S2 entities #1 |
| Hold a time in service durably and close it on withdrawal | REUSE | A time in service is opened at placement and closed at withdrawal, on the same record. | capability_side_effects::CS_MUTABLE_JSON_V0 satisfies it as-is. | S2 entities #2 |
| Enforce that one record exists per model | REUSE | Register-if-absent gives an atomic uniqueness guarantee on a key formed from the description and fingerprint. | capability_side_effects::CS_REGISTRY_V0 reused with a formed key, as the catalog does for a book. | S2 gaps #6 |
| Form the key that identifies a model | AUTHOR_NEW | Which attributes identify a model is this subdomain's rule. | book_library_mgmt::CT_PURE_FORM_BOOK_IDENTITY_KEY_V0 was examined as the worked form and rejected as a book's rule. | S2 gaps #6 |
| Keep every user prompt record, answered or refused | REUSE | An append-only trail keeps each entry whole and never rewrites it. | capability_side_effects::CS_APPENDONLY_JSONL_V0 satisfies it as-is. | S3 analysis_findings #6 |
| Assemble and validate the subdomain's records | REUSE | Assembly and shape validation carry no subdomain meaning. | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 and capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 satisfy it as-is. | S2 pps_baseline_fqdns Record assembly |
| Confirm the parameters supplied to an operation satisfy their declared rules | REUSE | Parameter validation is mechanism; the rules are declared by the subdomain's own operations. | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 satisfies it as-is. | S2 pps_baseline_fqdns Parameter rule validation |
| Declare the kinds of information in their order | AUTHOR_NEW | Four kinds, least sensitive first, used by placement and by every user prompt. | blockchain::VOCAB_WALLET_CLASSIFICATION_V0 was examined as the worked form and rejected as a wallet's classifications. | S2 gaps #7 |
| Confirm a stated kind of information is one of the declared kinds | REUSE | Membership is mechanism. | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 satisfies it as-is. | S3 analysis_findings #5 |
| Refuse a kind of information more sensitive than the ceiling | AUTHOR_NEW | The comparison needs the kinds' order, which membership does not use. | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 was examined and rejected as confirming membership only. | S3 analysis_findings #5 |
| Assemble what the model reads, and refuse it when it is longer than the model can read at once | AUTHOR_NEW | What the model reads is exactly the question, the supporting material and the system prompt, and nothing else. | No transform in the composition assembles a model's reading. | S2 process_steps Submit a user prompt #5 |
| Form the response rules in force for one user prompt | AUTHOR_NEW | The rule against another customer's account number is formed from the account numbers the user prompt carries. | No transform in the composition forms rules per request. | S3 analysis_findings #4 |
| Offer the model's next words, with a result not determined by its inputs | AUTHOR_NEW | This is the model's step, declared as the one step where determinism ends. | No transform in the composition is declared with effects of this class. | S3 analysis_findings #2 |
| Choose one permitted word under the response rules, the freedom of word choice and a stated seed | AUTHOR_NEW | The rules stop forbidden words while the model writes; given the offered words, the rules and the seed, the choice is deterministic. | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 was examined and rejected: it judges supplied values once, not each word as it is written. | S3 analysis_findings #10 |
| Write a response word by word, each pass offering and then choosing, until it finishes, no permitted word remains, or the longest response is reached | AUTHOR_NEW | The repetition lives below the operation, with each pass's two steps declared. | No transform eligible for reuse repeats a step; the one repeated computation in the composition is internal to the workload domain, not offerable here, and keeps its repetition inside one transform where no decision is visible. | S3 analysis_findings #1 |
| Run a composed body once per pass of a transform's loop | EXTEND | The construct is declared and the compiler emits it; the runtime is extended to run it. No transform in the composition has a composed body, so nothing that runs today changes. | A separate governance dossier was considered and not required: no schema, constitution or invariant changes. Putting both steps in one transform was rejected: it hides the rules from governance. | S3 analysis_findings #1 |
| A test model that tries to write another customer's account number | AUTHOR_NEW | The business sees the rules hold before a real model is trusted with them. | No realization of a model exists. | S3 analysis_findings #11 |
| Model staff and requester actors whose authorization an operation binds | AUTHOR_NEW | Every operation is refused unless its initiator is authorized, and nothing existing names either. | book_library_mgmt::AC_LIBRARY_STAFF_V0 was examined as the worked form and rejected as library staff. | S2 gaps #4 |
| Confirm the staff member is model staff, and the requester may act for the customer | AUTHOR_NEW | The subdomain reads authorization and never grants it. | book_library_mgmt::CC_CONFIRM_STAFF_AUTHORIZED_V0 was examined as the worked form and rejected as catalog staff. | S2 gaps #4 |
| Register a model | AUTHOR_NEW | No capability registers a model. | book_library_mgmt::CC_REGISTER_BOOK_V0 was examined as the worked form and rejected as catalog semantics. | S2 gaps #2 |
| Place a model in service, and withdraw it | AUTHOR_NEW | No capability opens or closes a time in service. | book_library_mgmt::CC_RETIRE_BOOK_RECORD_V0 and book_library_mgmt::CC_REINSTATE_BOOK_RECORD_V0 were examined as worked forms of a state change and rejected as catalog semantics. | S2 gaps #2 |
| Submit a user prompt and release or refuse the model response | AUTHOR_NEW | No capability accepts a user prompt. | ai_governance::WF_GOVERN_AGENT_ACTION_V0 was examined and rejected: it judges a finished proposal. | S2 gaps #2 |
| Retrieve a user prompt record | AUTHOR_NEW | No capability reads the subdomain's records. | book_library_mgmt::CC_RESOLVE_BOOK_IDENTITY_V0 was examined as the worked form of a governed read and rejected as catalog semantics. | S2 gaps #2 |
| Record each performed operation in the subdomain's own trail | AUTHOR_NEW | The subdomain owns its traceability and its stores. | book_library_mgmt::CC_APPEND_CATALOG_OPERATION_V0 was examined as the worked form and rejected as appending to the catalog's store. | S2 architectural_observations #6 |
| Declare the subdomain's stores and bind its operations to them | AUTHOR_NEW | A subdomain declares its own stores and bindings. | book_library_mgmt::STRUCTURE_CATALOG_STORAGE_V0 and book_library_mgmt::RB_CATALOG_BINDINGS_V0 were examined as worked forms and rejected as the catalog's own. | S2 architectural_observations #1 |
| A governed entry point for each operation | AUTHOR_NEW | Each operation is requested through its own entry point, and none exists. | book_library_mgmt::IN_REGISTER_BOOK_V0 was examined as the worked form and rejected as a catalog request. | S2 gaps #2 |
| A business moment for each of the five events | AUTHOR_NEW | Five business moments are declared and none is recognised anywhere in the composition. | book_library_mgmt::EV_BOOK_REGISTERED_V0 was examined as the worked form and rejected as a catalog moment. | S2 gaps #5 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| NEW_SUBDOMAIN | model_response | The composition carries no artifact in the causal_language_model namespace and nothing that registers a model or governs how one writes, so there is no subdomain to extend. It is the first of six functions the project will govern; the remaining five are declared adjacent rather than touched. | S2 belief_verification #1 · S1 governance_scope #1 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All five CRITICAL gaps carried from Stage 2 have an authoring decision: records, operations, word-by-word writing with visible rule decisions, actors and business moments. |
| No open analyst questions | SATISFIED | Stage 2 carried three open questions; the business owner answered the first, and the second and third are answered by evidence, closed as S3 analysis_findings #4, #1 and #2. |
| No dependency expansion in the last pass | SATISFIED | The dependency register closed at thirteen entries — seven reused, one extended, five authored — and re-reading the composition at this stage surfaced no further dependency. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Eight items re-verified against the composition, all CONFIRMED, none OVERTURNED. |
| Every INFERRED finding promoted, accepted or carried forward with a reason | SATISFIED | Stage 2's three INFERRED concerns are re-grounded here as OBSERVED. Two findings raised here stay INFERRED and are carried forward to Stage 7 with their obligations: the seed as a recorded input of the rules' step, and the test model as a realization supplied outside the domain's pure transforms. |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | analysis_findings · verification_results · dependency_discoveries · impact_analysis · authoring_decisions · placement_decision · saturation |
