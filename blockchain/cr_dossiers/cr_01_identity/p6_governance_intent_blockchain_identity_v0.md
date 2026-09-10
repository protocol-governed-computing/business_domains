# Stage 6 — Governance Intent: blockchain / identity

**Stage:** 6 — Governance Intent
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 7 — Design Intent

Placement only. Every capability declared in scope is given an owner, every store is placed with the
subdomain that holds it, and the one capability this change needs and does not own is declared as a
crossing rather than quietly placed here.

---

## 1. Subdomain Boundary — Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Declare the actors of this business | identity | OWNED |  | S5 scope_boundary Declare the actors of this business |
| Declare the stores identity owns | identity | OWNED |  | S5 scope_boundary Declare the stores identity owns |
| Bind identity's workflows to the stores they use | identity | OWNED |  | S5 scope_boundary Bind identity's workflows to the stores they use |
| Recognise the moments an actor is registered, accepted and rejected | identity | OWNED |  | S5 scope_boundary Recognise the moments an actor is registered, accepted and rejected |
| Record an acceptance and a rejection | identity | OWNED |  | S5 scope_boundary Record an acceptance and a rejection |
| Admit a person's registration and record them unverified | identity | OWNED |  | S5 scope_boundary Admit a person's registration and record them unverified |
| Record an authority's decision against a registered actor | identity | OWNED |  | S5 scope_boundary Record an authority's decision against a registered actor |
| Admit a request to register a person | identity | OWNED |  | S5 scope_boundary Admit a request to register a person |
| Admit a request to record a verification decision | identity | OWNED |  | S5 scope_boundary Admit a request to record a verification decision |
| Hold the trail of occurrences | identity | SATISFIED | capability_side_effects::CS_APPENDONLY_JSONL_V0 | S4 capability_graph Hold the trail of occurrences |
| Hold an actor's current state | identity | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph Hold an actor's current state |
| Claim and resolve the contact address | identity | SATISFIED | capability_side_effects::CS_REGISTRY_V0 | S4 capability_graph Claim and resolve the contact address |
| Read a registration for absent or malformed details | identity | SATISFIED | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | S4 capability_graph Read a registration for absent or malformed details |
| Determine the time an occurrence happened | capability_side_effects | DEFERRED |  | S5 scope_boundary Determine the time an occurrence happened |
| Re-application by a rejected actor | identity | DEFERRED |  | S5 scope_boundary Re-application by a rejected actor |
| Revocation of an accepted actor | identity | DEFERRED |  | S5 scope_boundary Revocation of an accepted actor |
| Governing which persons may be an authority | identity | DEFERRED |  | S5 scope_boundary Governing which persons may be an authority |
| Holding the material an authority examined | identity | DEFERRED |  | S5 scope_boundary Holding the material an authority examined |
| Correcting an actor's own details after registration | identity | DEFERRED |  | S5 scope_boundary Correcting an actor's own details after registration |

---

## 2. Storage Governance Requirements

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every person the business knows, carrying whether it has accepted them | The business requires one authoritative record per actor, whose state changes once and in place when a decision is recorded, so that the state can be read at the moment of deciding | identity | S5 business_objects Actor record |
| An atomic claim on each contact address | Two registrations carrying the same address must resolve to one actor, and only a claim taken at the moment of registration can guarantee it | identity | S5 business_objects Contact address registry |
| An unamendable trail of every occurrence recorded against an actor | An occurrence that has happened cannot be un-happened, so its record is never amended and never removed, and the business can afterwards show who registered, who decided, what was decided and when | identity | S5 business_objects Actor occurrence trail |

---

## 3. Cross-Subdomain Dependency Declaration

<!-- register:cross_subdomain_deps optional business_language=dependency -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Holding the trail of occurrences unamendably | identity -> capability_side_effects | capability_side_effects::CS_APPENDONLY_JSONL_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| Holding an actor's current state addressably | identity -> capability_side_effects | capability_side_effects::CS_MUTABLE_JSON_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_MUTABLE_JSON_V0 |
| Claiming and resolving the contact address | identity -> capability_side_effects | capability_side_effects::CS_REGISTRY_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_REGISTRY_V0 |
| Reading a registration for absent or malformed details | identity -> capability_transforms | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| Reading a value against a declared admitted set | identity -> capability_transforms | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| Comparing the authority named on a decision against the actor it names | identity -> capability_transforms | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_COMPARE_EQUAL_V0 |
| Assembling the record each occurrence appends | identity -> capability_transforms | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| Extracting named values from a registration or a decision | identity -> capability_transforms | capability_transforms::CT_PURE_EXTRACT_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_EXTRACT_V0 |
| Determining the time an occurrence happened | identity -> capability_side_effects | | GAP | S4 dependency_graph the substrate capability supplying the current time |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| capability_side_effects::CS_APPENDONLY_JSONL_V0 | Present and reused unchanged; impacted by 58 artifacts | REUSE | S4 dependency_graph capability_side_effects::CS_APPENDONLY_JSONL_V0 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | Present and reused unchanged; impacted by 51 artifacts | REUSE | S4 dependency_graph capability_side_effects::CS_MUTABLE_JSON_V0 |
| capability_side_effects::CS_REGISTRY_V0 | Present and reused unchanged; impacted by 47 artifacts | REUSE | S4 dependency_graph capability_side_effects::CS_REGISTRY_V0 |
| capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_COMPARE_EQUAL_V0 |
| capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |
| capability_transforms::CT_PURE_EXTRACT_V0 | Present and reused unchanged | REUSE | S4 dependency_graph capability_transforms::CT_PURE_EXTRACT_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| IDENTITY_OWNS_ITS_STORES | Every store identity reads or writes is declared by identity, and no identity operation writes into a store another subdomain owns. | S4 design_decisions #1 |
| THE_TRAIL_IS_NEVER_READ_TO_DECIDE | No operation reads the occurrence trail to decide anything; an actor's state is read from the state store, and the trail is evidence only. | S4 design_decisions #2 |
| EVERY_CLAIM_PRECEDES_EVERY_WRITE | A registration claims the contact address before it writes the actor record, so a refused registration leaves nothing behind. | S4 design_decisions #3 |
| AUTHORITY_IS_RECORDED_NEVER_RESOLVED | Identity records the authority named on a decision and resolves it against nothing. No store holds authorities, and the self-verification refusal compares two names. | S4 design_decisions #6 |
| ACCEPTANCE_AND_REJECTION_ARE_DISTINCT | No operation writes one decision record and distinguishes the outcome by a field; the two outcomes are recorded as two occurrences. | S4 design_decisions #4 |
| NO_TIME_IS_INVENTED | No identity operation supplies a time it did not receive from the capability that determines one. Until the substrate offers that capability this change cannot be built. | S4 design_decisions #5 |
| IDENTITY_GRANTS_NO_PERMISSION | Identity says who an actor is and whether it is trusted; it declares nothing about what a trusted actor may do, which belongs to the functions that name the actor. | S4 constraint_register #5 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional business_language=capability -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Declare the actors of this business | identity | S6 ownership Declare the actors of this business |
| Declare the stores identity owns | identity | S6 ownership Declare the stores identity owns |
| Bind identity's workflows to the stores they use | identity | S6 ownership Bind identity's workflows to the stores they use |
| Recognise the moments an actor is registered, accepted and rejected | identity | S6 ownership Recognise the moments an actor is registered, accepted and rejected |
| Record an acceptance and a rejection | identity | S6 ownership Record an acceptance and a rejection |
| Admit a person's registration and record them unverified | identity | S6 ownership Admit a person's registration and record them unverified |
| Record an authority's decision against a registered actor | identity | S6 ownership Record an authority's decision against a registered actor |
| Admit a request to register a person | identity | S6 ownership Admit a request to register a person |
| Admit a request to record a verification decision | identity | S6 ownership Admit a request to record a verification decision |

---

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | p4_business_model_blockchain_identity_v0.md | COMPLETE |
| Stage 5 — Business Intent | p5_business_intent_blockchain_identity_v0.md | COMPLETE |
| Stage 6 — Governance Intent | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
