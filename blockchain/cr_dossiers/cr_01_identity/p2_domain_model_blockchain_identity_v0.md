# Stage 2 — Domain Model Verification: blockchain / identity

**Stage:** 2 — Domain Model Verification
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition, and every other
register projects from those resolutions. This is the first change request against a domain the
composition does not hold: what already exists here is platform capability and nothing of the
business, so the baseline is a register of mechanism rather than of prior behaviour.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Actor | A person known to the system, whether or not the business has accepted them. | None — the composition holds no store for an actor of this business. A registry capability and an append-only capability both exist and neither is declared over any actor store. | OBSERVED | S2 belief_verification #1 |
| Verification Decision | The outcome an authority states against a registered actor, together with who stated it, when, and on what grounds. | None — nothing in the composition records a decision of one actor about another. | OBSERVED | S2 belief_verification #1 |
| Occurrence | A recorded moment in an actor's history, written when it happens and never rewritten. | None for this business. An append-only capability exists that could hold one; no stream is declared over it for identity. | OBSERVED | S2 belief_verification #2 |
| Authority | A party within the business empowered to decide about an actor, identified outside the identity function. | None, and none required — the business states an authority is not held or resolved here, so what is modelled is the recording of its name, not the party. | OBSERVED | S1 known_facts #17 |
| Contact Address | The address a person registers with, which is what identifies them as an actor. | None — no uniqueness registry is declared over any address of this business. | OBSERVED | S2 belief_verification #3 |
| Preference | A convenience recorded at registration — preferred currency or preferred language — bearing on neither identity nor the verification decision. | None. | OBSERVED | S2 belief_verification #1 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Actor | Name | What the person is called, supplied by them at registration. | OBSERVED | S1 operation_refusals #1 |
| Actor | Contact Address | The address the person registers with; what identifies them as an actor. | OBSERVED | S1 identity_and_sameness #1 |
| Actor | State | Whether the actor is unverified, accepted or rejected. | OBSERVED | S1 lifecycle_states #1 |
| Actor | Preferred Currency | The currency the person prefers to be quoted in. Has a default. | OBSERVED | S1 known_facts #24 |
| Actor | Preferred Language | The language the person prefers to be addressed in. Has a default. | OBSERVED | S1 known_facts #24 |
| Verification Decision | Outcome | Acceptance or rejection; there is no third. | OBSERVED | S1 known_facts #13 |
| Verification Decision | Deciding Authority | The authority that stated the outcome, recorded on every decision. | OBSERVED | S1 known_facts #20 |
| Verification Decision | Grounds | The reason stated for the outcome; required for a rejection. | OBSERVED | S1 known_facts #19 |
| Occurrence | Time | The moment the occurrence happened, determined as it occurs. | OBSERVED | S1 known_facts #21 |
| Occurrence | Actor | The actor the occurrence was recorded against. | OBSERVED | S1 identity_and_sameness #3 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a person | The person themselves | The person is an actor of the system and is unverified, or is refused for details the business cannot read. | OBSERVED | S1 requested_outcomes #1 |
| Record a verification decision | An authority within the business | The registered actor is accepted or rejected, and the decision is held as evidence naming its author, its time and its grounds. | OBSERVED | S1 requested_outcomes #2 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a person | 1 | Read the details supplied and refuse if a name or a contact address is absent. | None — a refusal produces no actor. | OBSERVED | S1 operation_refusals #1 |
| Register a person | 2 | Determine whether the contact address already identifies an actor. | None. | OBSERVED | S1 identity_and_sameness #1 |
| Register a person | 3 | Admit the person as an actor if the address is new, leaving the existing actor unchanged if it is not. | The actor, unverified. | OBSERVED | S1 known_facts #8 |
| Register a person | 4 | Record that the registration occurred, whether or not it created the actor. | An occurrence carrying the time it happened. | OBSERVED | S1 known_facts #9 |
| Record a verification decision | 1 | Resolve the actor the decision names and refuse if no such registration exists. | None — a refusal produces no decision. | OBSERVED | S1 operation_refusals #4 |
| Record a verification decision | 2 | Refuse if the actor has already been decided about, if the deciding authority is the actor itself, if the outcome is neither acceptance nor rejection, if no authority is named, or if a rejection states no grounds. | None. | OBSERVED | S1 operation_refusals #5 |
| Record a verification decision | 3 | Move the actor from unverified to accepted or to rejected. | The actor in its decided state. | OBSERVED | S1 lifecycle_transitions #3 |
| Record a verification decision | 4 | Record that the decision occurred, distinctly for an acceptance and for a rejection. | An occurrence carrying the authority, the outcome, the grounds and the time. | OBSERVED | S1 known_facts #16 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The business author believes nothing in the blockchain domain exists yet, so identity is established rather than extended. | VERIFIED | The pinned composition declares six business and platform namespaces — ai_governance, book_library_mgmt, inspection, platform, transformation, workload — across 345 artifacts, and inspection of the artifact catalog for the blockchain namespace returns no artifact in that namespace. The belief holds: nothing of this domain exists, and the change establishes rather than extends. | S1 system_beliefs #1 |
| The business author believes the platform already offers a way to record occurrences that is added to and never rewritten. | VERIFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 is declared in the composition as a storage capability offering exactly two operations, APPEND and GET_ALL. It admits a record, a stream and the actor appending, and returns the position at which the record was written. It offers no update and no delete, which is what makes the requirement that the record is added to and never rewritten a property of the mechanism rather than a discipline over it. | S1 system_beliefs #2 |
| The business author believes the platform already offers a way to hold a registry of business objects that can be looked up by their identifier. | VERIFIED | capability_side_effects::CS_REGISTRY_V0 is declared in the composition offering REGISTER, RESOLVE, EXISTS, COUNT and DEREGISTER. Registering a key already held is reported rather than silently accepted, which is what a repeated registration of one contact address requires, and RESOLVE reports the absence of a key, which is what refusing a decision against an actor that never registered requires. | S1 system_beliefs #3 |
| The business author believes the platform already offers a way to generate an identifier for a newly admitted business object. | VERIFIED | capability_transforms::CT_PURE_GENERATE_ID_V0 is declared in the composition as a neutral capability transform, alongside capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, which read a supplied record for absent fields and a supplied value against an admitted set. | S1 system_beliefs #4 |
| The business author believes the platform already distinguishes a kind of actor empowered to act on the business's behalf from an ordinary participant. | VERIFIED | actor::CONSTITUTION_ACTOR_IDENTITY_V0 governs how an actor is declared and authority::CONSTITUTION_AUTHORITY_GOVERNANCE_V0 governs authority over execution. actor::INVARIANT_IDENTITY_AUTHORITY_SEPARATION_V0 and authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 hold the two apart as a platform rule, and every domain in the composition declares its own actors against them — ai_governance::AC_SYSTEM_V0 beside ai_governance::AC_EMPLOYEE_V0, and book_library_mgmt::AC_LIBRARY_STAFF_V0. The distinction is available; no actor of this business exists to carry it. | S1 system_beliefs #5 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Append-only recording | capability_side_effects::CS_APPENDONLY_JSONL_V0 | Appends a record to a named stream and reads the stream whole. Offers no update and no delete. | EXACT | It records occurrences; it holds no current state, so the state of an actor cannot be read from it without reading every occurrence against them. |
| Identifier registry | capability_side_effects::CS_REGISTRY_V0 | Registers a key against a value, resolves a key, reports whether one exists, counts and deregisters. | EXACT | It holds identity, not history. It cannot say that a key was registered twice, only that it is held. |
| Mutable record storage | capability_side_effects::CS_MUTABLE_JSON_V0 | Writes, reads, updates, selects and deletes keyed records. | PARTIAL | It permits update and delete, which the record of occurrences must not; it is fit for an actor's current state and unfit for the trail. |
| Identifier generation | capability_transforms::CT_PURE_GENERATE_ID_V0 | Generates an identifier for a newly admitted object. | EXACT | It generates an identifier; it neither derives one from a contact address nor decides whether an address is already held. |
| Record structure validation | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Reads a supplied record for fields the declaration requires and for the form they must take. | EXACT | It reads a record for absence and for form, which is exactly the boundary the business drew; it judges nothing about belief, which the business placed with the verification decision. |
| Set membership validation | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Reads a supplied value against a declared admitted set. | EXACT | Nothing for this purpose; the outcome of a decision is one of two admitted values. |
| Record assembly | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Assembles a record from supplied fields. | EXACT | Nothing for this purpose. |
| Value extraction | capability_transforms::CT_PURE_EXTRACT_V0 | Extracts a named value from a supplied structure. | EXACT | Nothing for this purpose. |
| Actor identity governance | actor::CONSTITUTION_ACTOR_IDENTITY_V0 | Governs how an actor is declared and what an actor declaration must carry. | EXACT | It governs the form of an actor declaration; it declares no actor of this business. |
| Authority governance | authority::CONSTITUTION_AUTHORITY_GOVERNANCE_V0 | Governs authority over execution and holds actor and authority apart. | EXACT | It governs who may execute; it does not govern one actor deciding about another, which is what a verification decision is. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| No store holds an actor of this business. | CRITICAL | A person cannot be admitted, and nothing can be looked up afterwards. | OBSERVED | S2 belief_verification #1 |
| No store holds the occurrences recorded against an actor. | CRITICAL | The business could not show who registered, who decided, what was decided or when, which is a requested outcome in its own right. | OBSERVED | S2 belief_verification #2 |
| Nothing claims a contact address so that two actors cannot share one. | CRITICAL | Two registrations of one person would create two actors, and the identity rule the business stated would not hold. | OBSERVED | S2 belief_verification #3 |
| Nothing declares the actors of this business. | CRITICAL | A person registering and an authority deciding are different kinds of party, and without the ordinary participant declared neither operation has an actor to admit. | OBSERVED | S2 belief_verification #5 |
| Nothing holds an actor's state, so unverified, accepted and rejected are not represented. | CRITICAL | The whole change turns on an unverified actor being a distinct thing; without a state it is a label on nothing. | OBSERVED | S2 belief_verification #1 |
| Nothing records a verification decision, its author or its grounds. | CRITICAL | Neither requested outcome concerning the decision can be met. | OBSERVED | S2 belief_verification #1 |
| No capability determines the time at which an occurrence happens. | CRITICAL | Every occurrence must carry the time it actually happened, and the business regards a record whose times do not advance as no record at all. Nothing observed in the composition supplies a time. | OBSERVED | S2 architectural_observations #3 |
| No capability distinguishes a rejection from an acceptance in what it records. | MAJOR | The business must be able to ask who has been rejected and receive an answer, and must never be able to read a rejected actor as accepted. | OBSERVED | S2 belief_verification #1 |
| No capability refuses an operation on the ground that a decision has already been made. | MAJOR | An actor is decided about once, and nothing observed enforces it. | OBSERVED | S2 belief_verification #3 |
| Re-application after rejection, revocation, authority over verifiers, identity evidence and correction of an actor's details are absent from the composition. | MINOR | Each is deferred by the change request to a governed change of its own and is not modelled here. | OBSERVED | S1 out_of_scope #4 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The requirement that the record is never rewritten is satisfiable by choosing the capability rather than by disciplining its use. | capability_side_effects::CS_APPENDONLY_JSONL_V0 offers APPEND and GET_ALL and nothing else, while capability_side_effects::CS_MUTABLE_JSON_V0 offers update and delete. A trail placed on the first cannot be rewritten; one placed on the second could be. | OBSERVED | S2 pps_baseline_fqdns #1 |
| An actor's current state and the trail of occurrences against it are different storage problems and the composition offers a different capability for each. | The registry resolves a key to a value and holds no history; the append-only stream holds history and answers no question about current state without being read whole. | OBSERVED | S2 pps_baseline_fqdns #2 |
| Repeated registration is expressible without a bespoke capability, because registering a key already held is reported rather than accepted silently. | capability_side_effects::CS_REGISTRY_V0 declares REGISTER among its operations and reports the outcome of one, so an existing key is a reportable outcome and not a failure. | INFERRED | S2 pps_baseline_fqdns #2 |
| Every domain in the composition declares its own actors rather than drawing them from a shared set. | ai_governance declares five actors including ai_governance::AC_SYSTEM_V0, book_library_mgmt declares book_library_mgmt::AC_LIBRARY_STAFF_V0, and no actor is declared outside a domain. | OBSERVED | S2 belief_verification #5 |
| Nothing observed in the capability surface supplies the current time. | The five capabilities declared are capability_side_effects::CS_APPENDONLY_JSONL_V0, capability_side_effects::CS_MUTABLE_JSON_V0, capability_side_effects::CS_REGISTRY_V0, capability_side_effects::CS_SNAPSHOT_QUERY_V0 and capability_side_effects::CS_TEXT_ARTIFACT_V0, and none declares an operation returning a time. | OBSERVED | S2 gaps #7 |
| The composition already carries governed transport boundary artifacts, so a business function reached from outside is an established shape rather than a new one. | The pinned composition carries eighteen transport ingress and eighteen transport egress artifacts, all in the inspection namespace. | OBSERVED | S2 belief_verification #1 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The business requires every occurrence to carry the time it actually happened, and no capability observed in the composition supplies a time. | No operation of the five declared capabilities returns a time, and no capability transform observed derives one. | CRITICAL | OBSERVED | S2 gaps #7 |
| An occurrence recorded against an actor is required to be unalterable, and the append-only capability enforces that only for what is placed on it. | capability_side_effects::CS_MUTABLE_JSON_V0 is equally available and permits update and delete. Nothing observed prevents a trail being placed on it. | MAJOR | OBSERVED | S2 architectural_observations #1 |
| The business requires that a person may never verify themselves while also stating that an authority is never resolved here, so the refusal must rest on a name the function does not hold. | authority::INVARIANT_ACTOR_AUTHORITY_SEPARATION_V0 and authority::INVARIANT_AUTHORITY_REQUIRED_FOR_EXECUTION_V0 govern who may execute a workflow, which is not the same question as whether the subject of a decision is its author. Comparing an unresolved authority name against the actor decided about is the only observed means of expressing it. | MAJOR | OBSERVED | S1 known_facts #17 |
| The business requires an actor to be decided about once, and neither observed storage capability expresses a transition permitted only from one state. | The registry resolves and registers; the append-only stream appends. Neither declares a conditional transition. | MAJOR | INFERRED | S2 gaps #9 |
| The change request states that an unverified or rejected actor may hold no wallet and submit no transaction, and neither function exists to be constrained. | No artifact of the blockchain namespace is held by the composition. | MINOR | OBSERVED | S2 belief_verification #1 |

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| Where does the time of an occurrence come from, given that no observed capability supplies one? | Capability | The business regards a record whose times do not advance as no record at all, and nothing observed can satisfy it. | S2 discovery_concerns #1 |
| Is an actor's state held as a value that is read and replaced, or derived by reading the occurrences recorded against them? | Modelling | The two available storage capabilities answer different questions, and the choice decides how "decided about once" is enforced. | S2 architectural_observations #2 |
| Is the contact address itself the actor's identifier, or is a generated identifier held against it? | Modelling | Identifier generation exists and so does a registry; whether both are needed depends on whether the business address is the key. | S2 pps_baseline_fqdns #4 |

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | business_vocabulary · known_facts · system_beliefs · lifecycle_states · business_events · governance_scope · out_of_scope · constraints · business_invariants · authority_boundaries · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
