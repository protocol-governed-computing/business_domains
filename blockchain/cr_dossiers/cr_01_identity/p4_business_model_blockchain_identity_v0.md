# Stage 4 — Business Model: blockchain / identity

**Stage:** 4 — Business Model
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies: what is reused already exists, what is authored is a declared gap. Nothing is
re-litigated and nothing new is decided. One gap is owned outside this subdomain, which the register
records rather than hides.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The person registering | Supplies their own identifying details and is admitted unverified. | Ordinary participant | S1 authority_boundaries The details an actor registers with |
| The authority | Records a decision accepting or rejecting a registered actor. Identified outside this function and never resolved by it. | External business authority | S1 authority_boundaries Verification Decision |
| Identity | Holds the actor, its state and the record of occurrences against it. | Owning subdomain | S1 authority_boundaries Actor |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| Actor | A person known to the system, whether or not the business has accepted them. | A keyed store holding the actor and its current state, read at the moment of deciding. | S3 analysis_findings Q4 |
| Contact Address | The address a person registers with; what identifies them as an actor. | A registry claiming the address, which reports rather than accepts an address already held. | S3 analysis_findings Q6 |
| Verification Decision | The outcome an authority states against a registered actor, with who stated it, when, and on what grounds. | Held as the actor's state, and recorded as an occurrence that is never rewritten. | S3 analysis_findings Q7 |
| Occurrence | A recorded moment in an actor's history, written when it happens and never rewritten. | An append-only trail offering no update and no delete. | S3 analysis_findings Q3 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| Actor Registered Unverified | A person supplies their identifying details and is admitted. | The business knows of the person and trusts them with nothing. It is the occurrence a decision is made against. | S1 business_events Actor Registered Unverified |
| Actor Registered Again | A person already known registers a second time. | The actor is unchanged; that the person registered twice is kept. | S1 business_events Actor Registered Again |
| Actor Accepted | An authority records a decision to trust a registered actor. | The actor becomes trusted, and the other functions may name them. | S1 business_events Actor Accepted |
| Actor Rejected | An authority records a decision not to trust a registered actor. | The actor remains trusted with nothing, and can afterwards be listed among those rejected. | S1 business_events Actor Rejected |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| A person | registers | themselves as an actor | Admit a person's registration and record them unverified | S3 authoring_decisions Admit a person's registration and record them unverified |
| An actor | is identified by | a contact address | Claim and resolve the contact address | S3 authoring_decisions Claim and resolve the contact address |
| An authority | decides about | a registered actor | Record an authority's decision against a registered actor | S3 authoring_decisions Record an authority's decision against a registered actor |
| An occurrence | is recorded against | an actor | Hold the trail of occurrences | S3 authoring_decisions Hold the trail of occurrences |
| An occurrence | carries | the time it happened | Determine the time an occurrence happened | S3 authoring_decisions Determine the time an occurrence happened |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Hold the trail of occurrences | S3 authoring_decisions Hold the trail of occurrences | SATISFIED |  | Reused as-is; the capability offers no update and no delete, which is what enforces the requirement. |
| Hold an actor's current state | S3 authoring_decisions Hold an actor's current state | SATISFIED |  | Reused as-is; read at the moment of deciding rather than derived from the trail. |
| Claim and resolve the contact address | S3 authoring_decisions Claim and resolve the contact address | SATISFIED |  | Reused as-is; an already-held address is reported, which is the repeated-registration outcome. |
| Read a registration for absent or malformed details | S3 authoring_decisions Read a registration for absent or malformed details | SATISFIED |  | Reused as-is; the business drew the refusal boundary at absence and form, which is what it reads. |
| Determine the time an occurrence happened | S3 authoring_decisions Determine the time an occurrence happened | CRITICAL | GAP-01 | Owned by the substrate, not by this subdomain. Nothing in the composition supplies a time and a clock cannot be a transform. |
| Declare the actors of this business | S3 authoring_decisions Declare the actors of this business | CRITICAL | GAP-02 | One actor for the ordinary participant. The authority is not an actor of this function. |
| Declare the stores identity owns | S3 authoring_decisions Declare the stores identity owns | CRITICAL | GAP-03 | Three stores: the actor and its state, the address registry, the trail. |
| Bind identity's workflows to the stores they use | S3 authoring_decisions Bind identity's workflows to the stores they use | CRITICAL | GAP-04 | Without it the workflows cannot reach the stores they declare. |
| Recognise the moments an actor is registered, accepted and rejected | S3 authoring_decisions Recognise the moments an actor is registered, accepted and rejected | CRITICAL | GAP-05 | Three distinct occurrences, so a rejected actor can never be read as accepted. |
| Record an acceptance and a rejection | S3 authoring_decisions Record an acceptance and a rejection | CRITICAL | GAP-06 | Two records, not one carrying an outcome field. |
| Admit a person's registration and record them unverified | S3 authoring_decisions Admit a person's registration and record them unverified | CRITICAL | GAP-07 | The first business operation; composes the reused claim, state and trail capabilities. |
| Record an authority's decision against a registered actor | S3 authoring_decisions Record an authority's decision against a registered actor | CRITICAL | GAP-08 | The second business operation, and the one carrying every refusal the business declared. |
| Admit a request to register a person | S3 authoring_decisions Admit a request to register a person | CRITICAL | GAP-09 | The boundary registration is reached through, stating what it requires before any work begins. |
| Admit a request to record a verification decision | S3 authoring_decisions Admit a request to record a verification decision | CRITICAL | GAP-10 | A distinct admission surface, because what a decision requires differs from what a registration requires. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| identity | capability_side_effects::CS_APPENDONLY_JSONL_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| identity | capability_side_effects::CS_MUTABLE_JSON_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_side_effects::CS_MUTABLE_JSON_V0 |
| identity | capability_side_effects::CS_REGISTRY_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_side_effects::CS_REGISTRY_V0 |
| identity | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| identity | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| identity | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_transforms::CT_PURE_COMPARE_EQUAL_V0 |
| identity | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| identity | capability_transforms::CT_PURE_EXTRACT_V0 | capability call | SATISFIED | S3 dependency_discoveries capability_transforms::CT_PURE_EXTRACT_V0 |
| identity | actor::CONSTITUTION_ACTOR_IDENTITY_V0 | governance | SATISFIED | S3 dependency_discoveries actor::CONSTITUTION_ACTOR_IDENTITY_V0 |
| identity | transport::CONSTITUTION_TRANSPORT_INGRESS_V0 | governance | SATISFIED | S3 dependency_discoveries transport::CONSTITUTION_TRANSPORT_INGRESS_V0 |
| identity | the substrate capability supplying the current time | capability call | GAP | S3 dependency_discoveries A capability side effect supplying the current time |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|-----------|----------------|--------|
| 1 | Registration and the verification decision are separate acts, by different parties at different times. | S1 constraints Registration and the verification decision are separate acts | domain knowledge |
| 2 | An unverified or rejected actor may hold no wallet and submit no transaction. | S1 constraints An unverified or rejected actor may hold no wallet | domain knowledge |
| 3 | A recorded occurrence may never be altered or removed. | S1 constraints A recorded occurrence may never be altered or removed | invariant |
| 4 | The time of an occurrence is determined at the moment it occurs. | S1 constraints The time of an occurrence is determined at the moment it occurs | invariant |
| 5 | Identity governs who an actor is and whether they are trusted, and nothing about what a trusted actor may do. | S1 constraints Identity governs who an actor is and whether they are trusted | governance rule |
| 6 | Two actors never share a contact address, and an actor is identified by exactly one. | S1 business_invariants Two actors never share a contact address | invariant |
| 7 | An actor is decided about once, and is never accepted and rejected both. | S1 business_invariants An actor is decided about once | invariant |
| 8 | A person never makes the verification decision about themselves. | S1 business_invariants A person never makes the verification decision about themselves | invariant |
| 9 | A rejection states grounds, and every decision names the authority that made it. | S1 business_invariants A rejection states grounds | invariant |
| 10 | An authority is identified outside this function and is never resolved by it. | S1 known_facts An authority is identified outside the identity function | governance rule |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Determine the time an occurrence happened | Determine the time an occurrence happened | substrate — the neutral capability surface, not identity | NEW |
| GAP-02 | S3 authoring_decisions Declare the actors of this business | Declare the actors of this business | identity | NEW |
| GAP-03 | S3 authoring_decisions Declare the stores identity owns | Declare the stores identity owns | identity | NEW |
| GAP-04 | S3 authoring_decisions Bind identity's workflows to the stores they use | Bind identity's workflows to the stores they use | identity | NEW |
| GAP-05 | S3 authoring_decisions Recognise the moments an actor is registered, accepted and rejected | Recognise the moments an actor is registered, accepted and rejected | identity | NEW |
| GAP-06 | S3 authoring_decisions Record an acceptance and a rejection | Record an acceptance and a rejection | identity | NEW |
| GAP-07 | S3 authoring_decisions Admit a person's registration and record them unverified | Admit a person's registration and record them unverified | identity | NEW |
| GAP-08 | S3 authoring_decisions Record an authority's decision against a registered actor | Record an authority's decision against a registered actor | identity | NEW |
| GAP-09 | S3 authoring_decisions Admit a request to register a person | Admit a request to register a person | identity | NEW |
| GAP-10 | S3 authoring_decisions Admit a request to record a verification decision | Admit a request to record a verification decision | identity | NEW |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | The trail rests on the append-only capability and never on the mutable one. | S3 analysis_findings Q3 | The append-only capability offers no update and no delete, so unrewritability is a property of the mechanism rather than a discipline over it. | No operation may read the trail to decide anything; state is read from the state store. |
| 2 | An actor's state is held as a value, not derived from the occurrences. | S3 analysis_findings Q4 | The refusal that an actor is decided about once needs the state at the moment of deciding, not a reconstruction of it. | The trail is evidence and is never the source of truth for state. |
| 3 | The contact address is the identifier; no second identifier is generated. | S3 analysis_findings Q5 | Two registrations carrying the same address are the same person, which makes the address the key. | Identifier generation is not used, and nothing resolves an actor by anything but its address. |
| 4 | Acceptance and rejection are recorded as two occurrences, not one carrying an outcome. | S3 analysis_findings Q9 | The business must be able to list who was rejected and must never read a rejected actor as accepted; two records make both structural. | No operation may write a single decision record and distinguish the outcome by a field. |
| 5 | The time capability is a gap owned by the substrate, not authored here. | S3 analysis_findings Q2 | Determining the current time is a side effect and cannot be a transform; it is neutral mechanism and does not belong to a business domain. | This change cannot complete until the substrate offers it; no identity artifact may invent a time. |
| 6 | The authority is recorded and never resolved. | S1 known_facts An authority is identified outside the identity function | The business states an authority is part of the business rather than a participant admitted through this door. | No store holds authorities, and the self-verification refusal compares two names rather than resolving one. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Declare the actors of this business | GAP-02 |
| Declare the stores identity owns | GAP-03 |
| Bind identity's workflows to the stores they use | GAP-04 |
| Recognise the moments an actor is registered, accepted and rejected | GAP-05 |
| Record an acceptance and a rejection | GAP-06 |
| Admit a person's registration and record them unverified | GAP-07 |
| Record an authority's decision against a registered actor | GAP-08 |
| Admit a request to register a person | GAP-09 |
| Admit a request to record a verification decision | GAP-10 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Determine the time an occurrence happened | GAP-01 is owned by the substrate. It is a prerequisite of this change and not a part of it: a business domain may not author a neutral capability, and this change cannot be built until the substrate offers one. |
| Re-application by a rejected actor | Deferred by the business until this change states what a rejection means. |
| Revocation of an accepted actor | Deferred by the business to a governed change of its own. |
| Governing which persons may be an authority | Deferred by the business; identity records the name and does not resolve it. |
| Holding the material an authority examined | Deferred by the business with its retention and privacy consequences. |
| Correcting an actor's own details after registration | Deferred by the business until a verification decision is defined. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 1 — Change Request & Input Elicitation | Classification + Problem + Outcome + Known Facts | COMPLETE |
| Stage 2 — Domain Model Discovery | Actors, Entities, Resources, Events, Relationships | COMPLETE |
| Stage 3 — Analysis Loop | Capability Graph, Dependency Graph, Constraints, Gap Register | COMPLETE — SATURATED |
| Stage 4 — Business Model | This document | COMPLETE |
| Stage 4b — Authoring Scope | IN/FUTURE CR boundary | PENDING |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · constraints · business_invariants · authority_boundaries · out_of_scope |
| **Consumes** ← Stage 2 | entities · entity_attributes · business_processes · pps_baseline_fqdns |
| **Consumes** ← Stage 3 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
