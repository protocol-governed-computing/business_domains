# Stage 6 — Governance Intent: blockchain / identity

**Stage:** 6 — Governance Intent

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of a correction. Nothing moves and nothing is added: the step being corrected already
belongs to the function that owns the record it writes. What is placed here is the rule the
correction realises — which of a person's details a decision may change — and it is placed with the
subdomain that holds them.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Record a decision against a registered person | identity | OWNED |  | S5 scope_boundary Record a decision against a registered person |
| State which of a person's details a decision may change | identity | OWNED |  | S5 scope_boundary State which of a person's details a decision may change |
| Change part of a held record without replacing it | identity | SATISFIED | capability_side_effects::CS_MUTABLE_JSON_V0 | S4 capability_graph Change part of a held record without replacing it |
| Resolve the actor before a decision is recorded | identity | SATISFIED | blockchain::CC_RESOLVE_ACTOR_V0 | S4 capability_graph Resolve the actor before a decision is recorded |
| Reach the decision from outside | identity | SATISFIED | blockchain::TI_ACCEPT_ACTOR_V0 | S4 capability_graph Reach the decision from outside |
| Restore details already lost | identity | SATISFIED | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | S4 capability_graph Restore details already lost |
| Assemble the record a decision writes | identity, in a later change | DEFERRED |  | S5 scope_boundary Assemble the record a decision writes |
| Say which artifacts consume a store | the components that build the composition's indexes, not a business domain | DEFERRED |  | S5 scope_boundary Say which artifacts consume a store |
| Restoring details lost from records already thinned | nowhere; the business declines it | DEFERRED |  | S5 scope_boundary Restoring details lost from records already thinned |
| Correcting a person's own details | identity, in a later change | DEFERRED |  | S5 scope_boundary Correcting a person's own details |
| Enforcing that a rejection states grounds inside the business | identity, in a later change | DEFERRED |  | S5 scope_boundary Enforcing that a rejection states grounds inside the business |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every person the business knows, carrying both what they were admitted with and what was decided about them | Unchanged by this change, and named because what changes is how it is written. The business requires one authoritative record per person; a decision changes three fields of it and must leave the rest as they are | identity | S5 business_objects Actor record |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Changing part of a held record without replacing it | identity -> platform | capability_side_effects::CS_MUTABLE_JSON_V0 | SATISFIED | S4 dependency_graph capability_side_effects::CS_MUTABLE_JSON_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Present and reached by both decision workflows; its fifth step writes a whole record where it must change part of one | EXTEND | S4 dependency_graph blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | Present and reused unchanged; a different operation of the same capability is called | REUSE | S4 dependency_graph capability_side_effects::CS_MUTABLE_JSON_V0 |
| blockchain::RB_IDENTITY_BINDINGS_V0 | Present and reused unchanged; it binds the capability, not the operation | REUSE | S4 dependency_graph blockchain::RB_IDENTITY_BINDINGS_V0 |
| blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Present and reused unchanged; the store, its path and its declaration are untouched | REUSE | S4 dependency_graph blockchain::STRUCTURE_IDENTITY_STORAGE_V0 |
| blockchain::CC_RESOLVE_ACTOR_V0 | Present and reused unchanged; the only reader of the store, unaffected by fields being restored | REVIEW | S4 dependency_graph blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Present and unchanged; it composes the amended contract and routes on a result status this change preserves | REUSE | S4 dependency_graph blockchain::WF_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::TI_ACCEPT_ACTOR_V0 | Present and unchanged; it names the workflow, not the contract | REUSE | S4 dependency_graph blockchain::TI_ACCEPT_ACTOR_V0 |
| blockchain::TI_REJECT_ACTOR_V0 | Present and unchanged; the same | REUSE | S4 dependency_graph blockchain::TI_REJECT_ACTOR_V0 |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_DECISION_CHANGES_THREE_THINGS | A decision sets the person's state, the authority that decided and the grounds stated. Every other field of the record is absent from what it writes, and absence is how the rule is enforced rather than asserted. | S4 design_decisions #2 |
| ADMITTED_DETAILS_ARE_NOT_THE_BUSINESS_TO_CHANGE | No act of this subdomain that records a decision may write a detail the person supplied. Changing those is a different act, and one this subdomain has deferred. | S5 invariants No decision alters a detail the person supplied themselves. |
| WRITE_WHAT_DOES_NOT_EXIST_UPDATE_WHAT_DOES | A whole-value write is correct where a record is being created and wrong where one is being changed. Admitting a person writes; deciding about them updates. A step that writes a record it did not create is the defect this change corrects, and the store offers both so that neither needs the other's shape. | S4 design_decisions #1 |
| A_DECISION_CREATES_NOBODY | No act of this subdomain may bring a person into existence by deciding about them. A decision reaches a person the store already holds, or it refuses. | S4 design_decisions #4 |
| THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN | A record already written is left as it is, including one this defect has already thinned. No act of this change repairs history. | S4 design_decisions #6 |
| A_CORRECTION_IS_INVISIBLE_ABOVE_THE_CONTRACT | What a caller sends and is told is declared by the boundary, which names a workflow; the workflow routes on a result status. A change within a contract that preserves its statuses is observable to neither. | S3 analysis_findings Q7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Record a decision against a registered person | identity | S6 ownership Record a decision against a registered person |
| State which of a person's details a decision may change | identity | S6 ownership State which of a person's details a decision may change |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
