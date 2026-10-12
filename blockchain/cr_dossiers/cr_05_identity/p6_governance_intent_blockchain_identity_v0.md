# Stage 6 — Governance Intent: blockchain / identity

## Machine

```yaml
document:
  phase: p6
  domain: blockchain
  subdomain: identity
  cr: cr_05_identity
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Check a registration and refuse an incomplete one
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Check a registration and refuse an incomplete one}
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
  - capability: Refuse an authority deciding about themselves
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Refuse an authority deciding about themselves}
  - capability: Refuse a rejection stating no grounds
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Refuse a rejection stating no grounds}
  - capability: Fix the decision each act records
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Fix the decision each act records}
  - capability: Register a person unverified
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Register a person unverified}
  - capability: Reach identity from outside
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Reach identity from outside}
  - capability: Admit an acceptance with its grounds
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit an acceptance with its grounds}
  - capability: Admit a registration without the schema identity holds
    owner_subdomain: identity
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Admit a registration without the schema identity holds}
  - capability: Record the moment of each act
    owner_subdomain: identity
    disposition: SATISFIED
    existing_artifact: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    source_finding: {phase: p4, register: capability_graph, key: Record the moment of each act}
  - capability: Record the moment of each act as the act's own
    owner_subdomain: identity, in a later change
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Record the moment of each act as the act's own}
  - capability: Records made under a request's own rules
    owner_subdomain: nowhere; the business declines to rewrite them
    disposition: DEFERRED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Records made under a request's own rules}
  storage_governance:
  - storage_need: A durable record of every person the business knows, with their registration, their state and the decision made about them
    purpose: 'Unchanged by this change, and named because what may be written into it changes: a registration only as unverified, a decision only as the one identity checked'
    subdomain: identity
    source_finding: {phase: p5, register: business_objects, key: Actor record}
  cross_subdomain_deps:
  - dependency: Checking a record's structure
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0'}
  - dependency: Refusing on a list of rules
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0'}
  - dependency: Refusing a value outside a set
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0'}
  - dependency: Comparing two values
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_COMPARE_EQUAL_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_COMPARE_EQUAL_V0'}
  - dependency: Assembling a record from fields
    direction: identity -> platform
    existing_artifact: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    status: SATISFIED
    source_finding: {phase: p4, register: dependency_graph, key: 'capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0'}
  pps_artifacts_requiring_action:
  - fqdn: blockchain::CC_VALIDATE_REGISTRATION_V0
    current_status: Present; takes its schema from the request and refuses nothing
    action: EXTEND
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_VALIDATE_REGISTRATION_V0'}
  - fqdn: blockchain::CC_RECORD_VERIFICATION_DECISION_V0
    current_status: Present; takes its sets and self-decision rule from the request, and records a state the request supplies
    action: EXTEND
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RECORD_VERIFICATION_DECISION_V0'}
  - fqdn: blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0
    current_status: Present; takes its rules from the request
    action: EXTEND
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0'}
  - fqdn: blockchain::WF_REGISTER_ACTOR_V0
    current_status: Present; binds the schema from the request and writes the state it is handed
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three acts}
  - fqdn: blockchain::WF_ACCEPT_ACTOR_V0
    current_status: Present; binds the rules and the decision from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three acts}
  - fqdn: blockchain::WF_REJECT_ACTOR_V0
    current_status: Present; binds the rules and the decision from the request
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three acts}
  - fqdn: blockchain::TI_REGISTER_ACTOR_V0
    current_status: Present; supplies the schema and the state identity will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - fqdn: blockchain::TI_ACCEPT_ACTOR_V0
    current_status: Present; supplies the rules and the decided record identity will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - fqdn: blockchain::TI_REJECT_ACTOR_V0
    current_status: Present; supplies the rules and the decided record identity will hold
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The three entrances}
  - fqdn: blockchain::IN_ACTOR_ACCEPTANCE_V0
    current_status: Present; does not declare the grounds an acceptance may carry
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The acceptance gate}
  - fqdn: blockchain::CC_RESOLVE_ACTOR_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_RESOLVE_ACTOR_V0'}
  - fqdn: blockchain::CC_CLAIM_CONTACT_ADDRESS_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_CLAIM_CONTACT_ADDRESS_V0'}
  - fqdn: blockchain::CC_REGISTER_ACTOR_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_REGISTER_ACTOR_V0'}
  - fqdn: blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p4, register: dependency_graph, key: 'blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0'}
  - fqdn: blockchain::IN_ACTOR_REGISTERED_V0
    current_status: Present; requires the schema identity now holds
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The registration gate}
  boundary_rules:
  - rule_name: A_RULE_IS_HELD_WHERE_IT_IS_APPLIED
    statement: Each of identity's rules is a fixed value of the step that applies it. No act and no request hands identity a rule.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_CHECK_THAT_FINDS_REFUSES
    statement: A report of what a registration lacks is consumed by a rule that refuses when it lacks anything. The platform check reports; identity decides.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: THE_RECORD_IS_THE_DECISION
    statement: The state a decision writes is the decision identity checked. Only the authority and the grounds come from the request.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  - rule_name: REGISTRATION_LEADS_TO_UNVERIFIED
    statement: A registration writes the state unverified, whatever the request carries.
    source_finding: {phase: p4, register: design_decisions, row: 5}
  - rule_name: THE_ENTRANCE_CHANGES_NOTHING_A_CALLER_SEES
    statement: The entrances drop what identity holds; every request they admit today reaches the same outcome, and every answer is the same.
    source_finding: {phase: p4, register: design_decisions, row: 6}
  - rule_name: THE_RECORD_IS_ADDED_TO_NEVER_REWRITTEN
    statement: Records made before this change are left as they are.
    source_finding: {phase: p4, register: design_decisions, row: 7}
  governance_outcome:
  - capability: Check a registration and refuse an incomplete one
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Check a registration and refuse an incomplete one}
  - capability: Record a decision only about an unverified person, and only an acceptance or a rejection
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: 'Record a decision only about an unverified person, and only an acceptance or a rejection'}
  - capability: Refuse an authority deciding about themselves
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Refuse an authority deciding about themselves}
  - capability: Refuse a rejection stating no grounds
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Refuse a rejection stating no grounds}
  - capability: Fix the decision each act records
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Fix the decision each act records}
  - capability: Register a person unverified
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Register a person unverified}
  - capability: Reach identity from outside
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Reach identity from outside}
  - capability: Admit an acceptance with its grounds
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Admit an acceptance with its grounds}
  - capability: Admit a registration without the schema identity holds
    owner_subdomain: identity
    source_finding: {phase: p6, register: ownership, key: Admit a registration without the schema identity holds}
```

Placement of rules. Nothing moves and nothing is added: every step that changes already belongs to
identity. What is placed here is each of identity's rules, with the step that applies it, so that
identity holds them however it is reached.

---

## 1. Ownership

---

## 2. Storage Governance

---

## 3. Cross-Subdomain Dependencies

---

## 4. PPS Artifacts Requiring Action

---

## 5. Governance Boundary Rules

---

## 6. Governance Outcome

---

## gov_projection — Governed Handoff to Stage 7

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 5 | subdomain_purpose · scope_boundary · business_objects · identity_semantics · invariants · actions · provisional_codes · cross_subdomain_refs |
| **Emits** → Stage 7 | ownership · storage_governance · cross_subdomain_deps · pps_artifacts_requiring_action · boundary_rules · governance_outcome |
