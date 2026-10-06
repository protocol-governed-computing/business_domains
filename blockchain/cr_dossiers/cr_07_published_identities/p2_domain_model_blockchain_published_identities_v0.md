# Stage 2 — Domain Model Verification: blockchain / published identities

**Stage:** 2 — Domain Model Verification
**CR:** cr_07_published_identities
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition and against v5
as `pgc_release/snapshot` and the `v5` tag hold it. Every published identity of the domain was
compared with v5 by the platform's declaration of what carries meaning; the domain, its tests and the
workspace's process were searched for every name of the eight, by full name and by short code; and
construction acceptance was read for the design that determines each.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Published Act | An identity or wallet act v5 published. | Sealed in the release; not stored by this change. | OBSERVED | S1 business_vocabulary #2 |
| The Successor | The new identity that states what an act does today. | Sealed in the composition. | OBSERVED | S1 business_vocabulary #3 |
| A Failed Record | A record an act needs that cannot be read or written. | Not stored; it is an answer a store gives. | OBSERVED | S1 business_vocabulary #5 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Published Act | What it does with a failed record | In v5, nothing it declared; today, it reports and ends on it. | OBSERVED | S2 belief_verification #2 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Run an identity or wallet act | A caller, through an entrance or an intent | The act ends with an outcome; a failed record ends it. | OBSERVED | S1 requested_outcomes #4 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Run an identity or wallet act | 1 | An entrance or intent starts the workflow it names. | None. | OBSERVED | S2 belief_verification #3 |
| Run an identity or wallet act | 2 | The workflow runs its contracts; a failed record ends it at an error. | The records the act writes. | OBSERVED | S2 belief_verification #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Exactly eight published acts of this domain changed meaning since v5, all by cr_06. | VERIFIED | Of the domain's identities v5 published, the SU-11 sweep found eight whose declarations differ from v5 by the platform's declaration of what carries meaning: CC_RESOLVE_ACTOR_V0, CC_CLAIM_WALLET_IDENTITY_V0, CC_CREATE_WALLET_RECORD_V0, CC_APPEND_WALLET_OCCURRENCE_V0, WF_REGISTER_ACTOR_V0, WF_ACCEPT_ACTOR_V0, WF_REJECT_ACTOR_V0 and WF_CREATE_WALLET_V0. cr_06_routing_closure is the only dossier delivered after v5. | S1 system_beliefs #1 |
| Each of the eight differs from v5 only in how a failed record is reported and routed. | VERIFIED | Each contract's difference is a step's result_surface gaining BACKEND_ERROR and its on_result routing it; CC_RESOLVE_ACTOR_V0 and CC_CLAIM_WALLET_IDENTITY_V0 also allow it as an outcome. Each workflow's difference is BACKEND_ERROR routes from the places that run those contracts. Nothing else differs. | S1 system_beliefs #2 |
| The four workflows run the four contracts, and are named by the entrances and intents that start them. | VERIFIED | The contracts are named only by the four workflows, and by WF_RECORD_VERIFICATION_DECISION_V0, stood down before v5. The workflows are named by TI_REGISTER_ACTOR_V0, TI_ACCEPT_ACTOR_V0 and TI_REJECT_ACTOR_V0 in handler.workflow, and by IN_ACTOR_REGISTERED_V0, IN_ACTOR_ACCEPTANCE_V0, IN_ACTOR_REJECTION_V0 and IN_WALLET_CREATION_V0 in workflow, by short code; both are declared reference parts. The domain's identity, wallet and routing-closure execution validations and the runtime's determinism test run the workflows by full name. | S1 system_beliefs #3 |
| The domain's design of record states each of the eight fully. | VERIFIED | Construction acceptance reproduces all eight from cr_06_routing_closure with no field difference: the domain is compared whole, so each is determined by the design and nothing is authored by hand. | S1 system_beliefs #4 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Resolving an actor | blockchain::CC_RESOLVE_ACTOR_V0 | Answers which actor an address denotes, and ends on a failed record. | MISMATCH | Says more than v5 published under the published identity. |
| Registering an actor | blockchain::WF_REGISTER_ACTOR_V0 | Admits a person and routes a failed record to an ending. | MISMATCH | The same. |
| Starting an act | blockchain::TI_REGISTER_ACTOR_V0 | Admits a caller's request and starts the workflow it names. | PARTIAL | Names the published workflow. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Eight published identities do what v5 did not say. | CRITICAL | A citation of v5 names acts that now answer a failed record v5 left unanswered. | OBSERVED | S2 belief_verification #1; S2 belief_verification #2 |
| Seven artifacts in force, and the domain's tests, name the published workflows. | MAJOR | Once stood down, the published workflows would still be started. | OBSERVED | S2 belief_verification #3 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| A workflow's place keeps its label when the contract it runs changes. | The compiler maps each place's label to the contract it runs, so bindings that read a place keep working. | OBSERVED | S2 belief_verification #3 |
| A stood-down artifact may name a stood-down artifact. | WF_RECORD_VERIFICATION_DECISION_V0 has named the published contracts since before v5 and is out of reach. | OBSERVED | S2 belief_verification #3 |
| The successors can be built from the design of record. | cr_06 determines all eight; renamed, it determines their successors. | OBSERVED | S2 belief_verification #4 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Construction acceptance compares each identity with the latest design that determines it. | Restored to v5, the published identities no longer match cr_06, which determined their in-place change. | MAJOR | OBSERVED | S2 belief_verification #4 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
