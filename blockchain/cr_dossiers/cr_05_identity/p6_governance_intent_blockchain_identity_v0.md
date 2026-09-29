# Stage 6 — Governance Intent: blockchain / identity

**Stage:** 6 — Governance Intent

**CR:** cr_05_identity

**Status:** DRAFT

**Feeds:** Stage 7 — Design Intent

Placement of rules. Nothing moves and nothing is added: every step that changes already belongs to
identity. What is placed here is each of identity's rules, with the step that applies it, so that
identity holds them however it is reached.

---

## 1. Ownership

<!-- register:ownership business_language=capability -->
| Capability | Owner Subdomain | Disposition (OWNED, SATISFIED, DEFERRED) | Existing Artifact | Source Finding |
|------------|-----------------|------------------------------------------|-------------------|----------------|
| Check a registration and refuse an incomplete one | identity | OWNED |  | S5 scope_boundary Check a registration and refuse an incomplete one |
| Record a decision only about an unverified person, and only an acceptance or a rejection | identity | OWNED |  | S5 scope_boundary Record a decision only about an unverified person, and only an acceptance or a rejection |
| Refuse an authority deciding about themselves | identity | OWNED |  | S5 scope_boundary Refuse an authority deciding about themselves |
| Refuse a rejection stating no grounds | identity | OWNED |  | S5 scope_boundary Refuse a rejection stating no grounds |
| Fix the decision each act records | identity | OWNED |  | S5 scope_boundary Fix the decision each act records |
| Register a person unverified | identity | OWNED |  | S5 scope_boundary Register a person unverified |
| Reach identity from outside | identity | OWNED |  | S5 scope_boundary Reach identity from outside |
| Admit an acceptance with its grounds | identity | OWNED |  | S5 scope_boundary Admit an acceptance with its grounds |
| Admit a registration without the schema identity holds | identity | OWNED |  | S5 scope_boundary Admit a registration without the schema identity holds |
| Record the moment of each act | identity | SATISFIED | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | S4 capability_graph Record the moment of each act |
| Record the moment of each act as the act's own | identity, in a later change | DEFERRED |  | S5 scope_boundary Record the moment of each act as the act's own |
| Records made under a request's own rules | nowhere; the business declines to rewrite them | DEFERRED |  | S5 scope_boundary Records made under a request's own rules |

---

## 2. Storage Governance

<!-- register:storage_governance business_language=storage_need,purpose -->
| Storage Need | Purpose | Subdomain | Source Finding |
|--------------|---------|-----------|----------------|
| A durable record of every person the business knows, with their registration, their state and the decision made about them | Unchanged by this change, and named because what may be written into it changes: a registration only as unverified, a decision only as the one identity checked | identity | S5 business_objects Actor record |

---

## 3. Cross-Subdomain Dependencies

<!-- register:cross_subdomain_deps optional -->
| Dependency | Direction | Existing Artifact | Status (SATISFIED, GAP) | Source Finding |
|------------|-----------|-------------------|-------------------------|----------------|
| Checking a record's structure | identity -> platform | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 |
| Refusing on a list of rules | identity -> platform | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 |
| Refusing a value outside a set | identity -> platform | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 |
| Comparing two values | identity -> platform | capability_transforms::CT_PURE_COMPARE_EQUAL_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_COMPARE_EQUAL_V0 |
| Assembling a record from fields | identity -> platform | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 | SATISFIED | S4 dependency_graph capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0 |

---

## 4. PPS Artifacts Requiring Action

<!-- register:pps_artifacts_requiring_action optional -->
| FQDN | Current Status | Action (REPLACE, REVIEW, REUSE, EXTEND) | Source Finding |
|------|----------------|----------------------------------|----------------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | Present; takes its schema from the request and refuses nothing | EXTEND | S4 dependency_graph blockchain::CC_VALIDATE_REGISTRATION_V0 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Present; takes its sets and self-decision rule from the request, and records a state the request supplies | EXTEND | S4 dependency_graph blockchain::CC_RECORD_VERIFICATION_DECISION_V0 |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Present; takes its rules from the request | EXTEND | S4 dependency_graph blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 |
| blockchain::WF_REGISTER_ACTOR_V0 | Present; binds the schema from the request and writes the state it is handed | EXTEND | S3 dependency_discoveries The three acts |
| blockchain::WF_ACCEPT_ACTOR_V0 | Present; binds the rules and the decision from the request | EXTEND | S3 dependency_discoveries The three acts |
| blockchain::WF_REJECT_ACTOR_V0 | Present; binds the rules and the decision from the request | EXTEND | S3 dependency_discoveries The three acts |
| blockchain::TI_REGISTER_ACTOR_V0 | Present; supplies the schema and the state identity will hold | EXTEND | S3 dependency_discoveries The three entrances |
| blockchain::TI_ACCEPT_ACTOR_V0 | Present; supplies the rules and the decided record identity will hold | EXTEND | S3 dependency_discoveries The three entrances |
| blockchain::TI_REJECT_ACTOR_V0 | Present; supplies the rules and the decided record identity will hold | EXTEND | S3 dependency_discoveries The three entrances |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | Present; does not declare the grounds an acceptance may carry | EXTEND | S3 dependency_discoveries The acceptance gate |
| blockchain::CC_RESOLVE_ACTOR_V0 | Present and reused unchanged | REUSE | S4 dependency_graph blockchain::CC_RESOLVE_ACTOR_V0 |
| blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Present and reused unchanged | REUSE | S4 dependency_graph blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 |
| blockchain::CC_REGISTER_ACTOR_V0 | Present and reused unchanged | REUSE | S4 dependency_graph blockchain::CC_REGISTER_ACTOR_V0 |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Present and reused unchanged | REUSE | S4 dependency_graph blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 |
| blockchain::IN_ACTOR_REGISTERED_V0 | Present; requires the schema identity now holds | EXTEND | S3 dependency_discoveries The registration gate |

---

## 5. Governance Boundary Rules

<!-- register:boundary_rules optional -->
| Rule Name | Statement | Source Finding |
|-----------|-----------|----------------|
| A_RULE_IS_HELD_WHERE_IT_IS_APPLIED | Each of identity's rules is a fixed value of the step that applies it. No act and no request hands identity a rule. | S4 design_decisions #1 |
| A_CHECK_THAT_FINDS_REFUSES | A report of what a registration lacks is consumed by a rule that refuses when it lacks anything. The platform check reports; identity decides. | S4 design_decisions #2 |
| THE_RECORD_IS_THE_DECISION | The state a decision writes is the decision identity checked. Only the authority and the grounds come from the request. | S4 design_decisions #4 |
| REGISTRATION_LEADS_TO_UNVERIFIED | A registration writes the state unverified, whatever the request carries. | S4 design_decisions #5 |
| THE_ENTRANCE_CHANGES_NOTHING_A_CALLER_SEES | The entrances drop what identity holds; every request they admit today reaches the same outcome, and every answer is the same. | S4 design_decisions #6 |
| THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN | Records made before this change are left as they are. | S4 design_decisions #7 |

---

## 6. Governance Outcome

<!-- register:governance_outcome optional -->
| Capability | Owner Subdomain | Source Finding |
|------------|-----------------|----------------|
| Check a registration and refuse an incomplete one | identity | S6 ownership Check a registration and refuse an incomplete one |
| Record a decision only about an unverified person, and only an acceptance or a rejection | identity | S6 ownership Record a decision only about an unverified person, and only an acceptance or a rejection |
| Refuse an authority deciding about themselves | identity | S6 ownership Refuse an authority deciding about themselves |
| Refuse a rejection stating no grounds | identity | S6 ownership Refuse a rejection stating no grounds |
| Fix the decision each act records | identity | S6 ownership Fix the decision each act records |
| Register a person unverified | identity | S6 ownership Register a person unverified |
| Reach identity from outside | identity | S6 ownership Reach identity from outside |
| Admit an acceptance with its grounds | identity | S6 ownership Admit an acceptance with its grounds |
| Admit a registration without the schema identity holds | identity | S6 ownership Admit a registration without the schema identity holds |

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
