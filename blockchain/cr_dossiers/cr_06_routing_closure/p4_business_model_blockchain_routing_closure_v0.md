# Stage 4 — Business Model: blockchain / identity and wallet

**Stage:** 4 — Business Model

**CR:** cr_06_routing_closure

**Status:** DRAFT

**Feeds:** Stage 5 — Business Intent

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided. Every capability that changes
is an extension of one identity or wallet already has: each step keeps doing what it does, and
answers for the failed record its store can report.

---

## 1. Discovery Summary

<!-- register:actors business_language -->
### Actors (actors)
| Actor | Role | Authority Class | Source Finding |
|-------|------|-----------------|----------------|
| The person | Registers, and is given a wallet once accepted. Unchanged by this change. | Ordinary participant | S1 business_vocabulary #3 |
| The authority | Accepts or rejects a person. Unchanged by this change. | External business authority | S1 business_vocabulary #3 |
| Identity | Ends each of its acts as rejected when a record fails. | Owning subdomain | S3 placement_decision EXTEND |
| Wallet | Ends its act as rejected when a record fails. | Owning subdomain | S3 placement_decision EXTEND |

<!-- register:bm_entities business_language -->
### Entities (bm_entities)
| Entity | Description | Store Model | Source Finding |
|--------|-------------|-------------|----------------|
| The Person's Record | A person's registration, state and decision. | One keyed store, one record per contact address, unchanged. | S2 entities #1 |
| The Claimed Address | The contact address a person holds. | One registry, unchanged. | S2 entities #2 |
| The Trail | The moments in a person's or a wallet's history. | Append-only, unchanged. | S2 entities #3 |
| The Wallet | An accepted person's wallet and its claimed identity. | One keyed store and one registry, unchanged. | S2 entities #4 |
| A Failed Record | A record that could not be read or written. | Not stored; an answer a store gives. | S2 entities #5 |

<!-- register:resources optional business_language -->
### Resources
| Resource | Description | Source Finding |
|----------|-------------|----------------|
| NONE IDENTIFIED |

<!-- register:events business_language -->
### Events (events)
| Event | Trigger | Lifecycle Meaning | Source Finding |
|-------|---------|-------------------|----------------|
| NONE IDENTIFIED | This change recognises no new moment. | The moments identity and wallet announce are unchanged, and none is announced when a record fails. | S1 business_events #1 |

<!-- register:relationships optional business_language -->
### Relationships (Candidate Capabilities)
| Subject | Verb | Object | Capability Need | Source Finding |
|---------|------|--------|-----------------|----------------|
| Identity | stops | a lookup whose record failed | Stop a lookup at a failed record | S3 authoring_decisions Stop a lookup at a failed record |
| Wallet | stops | a step whose record failed | Stop a wallet step at a failed record | S3 authoring_decisions Stop a wallet step at a failed record |
| Identity and wallet | end | an act whose record failed, as rejected | End every act as rejected on a failed record | S3 authoring_decisions End every act as rejected on a failed record |

## 2. Capability Graph (capability_graph)

<!-- register:capability_graph business_language -->
| Capability | Source Finding | Status | Gap Register Entry | Notes |
|-----------|----------------|--------|--------------------|-------|
| Stop a lookup at a failed record | S3 authoring_decisions Stop a lookup at a failed record | CRITICAL | GAP-01 | The lookup and the read each end the contract on a failed record. |
| Stop a wallet step at a failed record | S3 authoring_decisions Stop a wallet step at a failed record | CRITICAL | GAP-02 | The claim, the write and the append each end their contract on a failed record. |
| End every act as rejected on a failed record | S3 authoring_decisions End every act as rejected on a failed record | CRITICAL | GAP-03 | Thirteen act nodes route a failed record to the rejected ending. |
| Leave records made before a failure in place | S3 authoring_decisions Leave records made before a failure in place | SATISFIED |  | Unchanged; nothing removes what an act recorded before it failed. |

## 3. Dependency Graph (dependency_graph)

<!-- register:dependency_graph -->
| From | To | Dependency Type | PPS Status | Source Finding |
|------|----|-----------------|------------|----------------|
| identity | blockchain::CC_RESOLVE_ACTOR_V0 | amended contract | SATISFIED | S3 dependency_discoveries Looking a person up |
| wallet | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | amended contract | SATISFIED | S3 dependency_discoveries Claiming a wallet's identity |
| wallet | blockchain::CC_CREATE_WALLET_RECORD_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording a wallet |
| wallet | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | amended contract | SATISFIED | S3 dependency_discoveries Recording a moment on a wallet's trail |
| identity | capability_side_effects::CS_REGISTRY_V0 | platform store | SATISFIED | S3 dependency_discoveries The stores |
| identity | capability_side_effects::CS_MUTABLE_JSON_V0 | platform store | SATISFIED | S3 dependency_discoveries The stores |
| wallet | capability_side_effects::CS_APPENDONLY_JSONL_V0 | platform store | SATISFIED | S3 dependency_discoveries The stores |
| identity | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | capability contract | SATISFIED | S3 dependency_discoveries The contracts that already answer for a failed record |
| identity | blockchain::CC_REGISTER_ACTOR_V0 | capability contract | SATISFIED | S3 dependency_discoveries The contracts that already answer for a failed record |
| identity | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | capability contract | SATISFIED | S3 dependency_discoveries The contracts that already answer for a failed record |
| identity | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | capability contract | SATISFIED | S3 dependency_discoveries The contracts that already answer for a failed record |

## 4. Constraint Register (constraint_register)

<!-- register:constraint_register -->
| # | Constraint | Source Finding | Source |
|---|------------|----------------|--------|
| 1 | Nothing changes for an act whose records are all read and written. | S1 constraints #1 | The business author |
| 2 | Records made before a failure stay as they were made. | S1 constraints #2 | The business author |
| 3 | No ending is added. | S1 constraints #3 | The business author |
| 4 | A failed record ends the act. Nothing retries. | S1 known_facts #4 | The business author |

## 5. Gap Register (gap_register)

<!-- register:gap_register business_language -->
| Gap Code | Source Finding | Capability | Owner Subdomain | Resolution |
|----------|----------------|-----------|-----------------|------------|
| GAP-01 | S3 authoring_decisions Stop a lookup at a failed record | Stop a lookup at a failed record | identity | EXTEND |
| GAP-02 | S3 authoring_decisions Stop a wallet step at a failed record | Stop a wallet step at a failed record | wallet | EXTEND |
| GAP-03 | S3 authoring_decisions End every act as rejected on a failed record | End every act as rejected on a failed record | identity, wallet | EXTEND |

## 6. Design Decisions (design_decisions)

<!-- register:design_decisions -->
| # | Decision | Source Finding | Rationale | Constraints Imposed |
|---|----------|----------------|-----------|---------------------|
| 1 | Each step whose store can fail ends its contract on a failed record. | S3 analysis_findings Q1 | A step that carries on past a failed record decides something the business never said. | Every step answers for every outcome its store declares. |
| 2 | Each act routes a failed record to its rejected ending. | S3 analysis_findings Q3 | The business keeps two endings, and a failed record is not a success. | Every outcome an act's contract can end with has a route. |
| 3 | A contract that can now end with a failed record says so. | S3 analysis_findings Q4 | A contract states every outcome it can end with. | No contract ends with an outcome it does not declare. |
| 4 | Records made before a failure are left as they are. | S3 analysis_findings Q5 | The record is added to and never rewritten. | No compensation, repair or backfill step may be authored. |

## 7. Authoring Scope (authoring_scope)

<!-- register:authoring_scope -->
### In Scope — This CR
| Capability | Gap Register Ref |
|-----------|-----------------|
| Stop a lookup at a failed record | GAP-01 |
| Stop a wallet step at a failed record | GAP-02 |
| End every act as rejected on a failed record | GAP-03 |

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Tell a refusal apart from a failure | Declined for now by the business: it keeps two endings. |
| The superseded act's unrouted nodes | Not dispatched; nothing reaches them. |

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
