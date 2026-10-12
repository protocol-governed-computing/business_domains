# Stage 4 — Business Model: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p4
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P4_V0
registers:
  actors:
  - actor: Authorized Requester
    role: Submits a request on behalf of a customer to a hosted model in service.
    authority_class: Business role
    source_finding: {phase: p2, register: business_processes, row: 2}
  - actor: Host
    role: Offers the candidates a hosted model could write next, and asks for release. Holds no authority.
    authority_class: External party
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  - actor: Model Response
    role: Admits, chooses, records and releases.
    authority_class: Owning subdomain
    source_finding: {phase: p3, register: placement_decision, key: EXTEND}
  bm_entities:
  - entity: Hosted Request
    description: A request answered step by step by a hosted model.
    store_model: 'Its record trail: an opening entry, a step entry per offer, and a closing entry.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
  - entity: Offer
    description: The candidates passed at one step, naming the model's fingerprint.
    store_model: Kept in the step entry with the choice made from it.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
  resources:
  - resource: The user prompt records
    description: The trail every request is recorded in, per request.
    source_finding: {phase: p3, register: dependency_discoveries, key: The record trail}
  events:
  - event: User Prompt Responded
    trigger: The business releases a completed hosted response.
    lifecycle_meaning: The hosted request is released.
    source_finding: {phase: p1, register: business_events, row: 1}
  - event: User Prompt Refused
    trigger: A hosted request yields no response.
    lifecycle_meaning: The hosted request is refused.
    source_finding: {phase: p1, register: business_events, row: 2}
  relationships:
  - subject: Authorized Requester
    verb: begins
    object: a hosted request
    capability_need: Begin a hosted request
    source_finding: {phase: p3, register: authoring_decisions, key: Begin a hosted request}
  - subject: Host
    verb: offers
    object: the next candidates
    capability_need: Offer the next candidates
    source_finding: {phase: p3, register: authoring_decisions, key: Offer the next candidates}
  - subject: Host
    verb: asks to release
    object: a completed response
    capability_need: Release a hosted response
    source_finding: {phase: p3, register: authoring_decisions, key: Release a hosted response}
  capability_graph:
  - capability: Begin a hosted request
    source_finding: {phase: p3, register: authoring_decisions, key: Begin a hosted request}
    status: CRITICAL
    gap_register_entry: GAP-01
    notes: Admits as the test model's way does.
  - capability: Confirm a hosted reading fits
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a hosted reading fits}
    status: CRITICAL
    gap_register_entry: GAP-02
    notes: The reported size against the capacity.
  - capability: Open the record of a hosted request
    source_finding: {phase: p3, register: authoring_decisions, key: Open the record of a hosted request}
    status: CRITICAL
    gap_register_entry: GAP-03
    notes: The trail is the state.
  - capability: Read the state of a hosted request
    source_finding: {phase: p3, register: authoring_decisions, key: Read the state of a hosted request}
    status: CRITICAL
    gap_register_entry: GAP-04
    notes: Reduced from the trail.
  - capability: Choose a permitted token
    source_finding: {phase: p3, register: authoring_decisions, key: Choose a permitted token}
    status: CRITICAL
    gap_register_entry: GAP-05
    notes: The test model's rules, on tokens.
  - capability: Offer the next candidates
    source_finding: {phase: p3, register: authoring_decisions, key: Offer the next candidates}
    status: CRITICAL
    gap_register_entry: GAP-06
    notes: One act per step.
  - capability: Release a hosted response
    source_finding: {phase: p3, register: authoring_decisions, key: Release a hosted response}
    status: CRITICAL
    gap_register_entry: GAP-07
    notes: Only the business releases.
  - capability: Record a hosted request
    source_finding: {phase: p3, register: authoring_decisions, key: Record a hosted request}
    status: SATISFIED
    gap_register_entry: null
    notes: The existing record closes it.
  dependency_graph:
  - from: model_response
    to: causal_language_model::CC_CLAIM_USER_PROMPT_IDENTITY_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Admission}
  - from: model_response
    to: causal_language_model::CC_CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Admission}
  - from: model_response
    to: causal_language_model::CC_ADMIT_USER_PROMPT_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Admission}
  - from: model_response
    to: causal_language_model::CC_CONFIRM_WITHIN_CEILING_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Admission}
  - from: model_response
    to: causal_language_model::CT_PURE_FORM_RESPONSE_RULES_V0
    dependency_type: reused transform
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Forming the rules in force}
  - from: model_response
    to: causal_language_model::CC_CONFIRM_READING_FITS_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Assembling what the model reads}
  - from: model_response
    to: causal_language_model::CC_CONFIRM_RESPONSE_RELEASABLE_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Releasability and the record}
  - from: model_response
    to: causal_language_model::CC_RECORD_USER_PROMPT_V0
    dependency_type: reused contract
    pps_status: SATISFIED
    source_finding: {phase: p3, register: dependency_discoveries, key: Releasability and the record}
  constraint_register:
  - number: '1'
    constraint: The test model's existing way of answering must not change.
    source_finding: {phase: p1, register: constraints, row: 1}
    source: The business author
  - number: '2'
    constraint: The host cannot decide which text is permitted, override a choice, or send text to a customer.
    source_finding: {phase: p1, register: constraints, row: 2}
    source: The business author
  - number: '3'
    constraint: Only a completed response held in the business's record, which passed the controls, is released.
    source_finding: {phase: p1, register: constraints, row: 3}
    source: The business author
  - number: '4'
    constraint: The business must not claim a response is true, or that the candidates came from the model.
    source_finding: {phase: p1, register: constraints, row: 4}
    source: The business author
  gap_register:
  - gap_code: GAP-01
    source_finding: {phase: p3, register: authoring_decisions, key: Begin a hosted request}
    capability: Begin a hosted request
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-02
    source_finding: {phase: p3, register: authoring_decisions, key: Confirm a hosted reading fits}
    capability: Confirm a hosted reading fits
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-03
    source_finding: {phase: p3, register: authoring_decisions, key: Open the record of a hosted request}
    capability: Open the record of a hosted request
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-04
    source_finding: {phase: p3, register: authoring_decisions, key: Read the state of a hosted request}
    capability: Read the state of a hosted request
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-05
    source_finding: {phase: p3, register: authoring_decisions, key: Choose a permitted token}
    capability: Choose a permitted token
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-06
    source_finding: {phase: p3, register: authoring_decisions, key: Offer the next candidates}
    capability: Offer the next candidates
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  - gap_code: GAP-07
    source_finding: {phase: p3, register: authoring_decisions, key: Release a hosted response}
    capability: Release a hosted response
    owner_subdomain: model_response
    resolution: AUTHOR_NEW
  design_decisions:
  - number: '1'
    decision: A hosted response is written one act per step, driven by the host; the business never calls the host.
    source_finding: {phase: p3, register: analysis_findings, key: Q1}
    rationale: Acts are acyclic, and the host holds no authority.
    constraints_imposed: The host offers and asks; it never chooses or releases.
  - number: '2'
    decision: A hosted request is admitted by the test model's four admission contracts, unchanged.
    source_finding: {phase: p3, register: analysis_findings, key: Q2}
    rationale: The same conditions admit both ways.
    constraints_imposed: No admission contract is redeclared.
  - number: '3'
    decision: Admission assembles the reading as for the test model; the host reports its token count with each offer, compared with the capacity before choosing.
    source_finding: {phase: p3, register: analysis_findings, key: Q3}
    rationale: Capacity is in tokens, counted by the host once it has the reading.
    constraints_imposed: The count is the host's claim, recorded with the step.
  - number: '4'
    decision: 'The record trail is the hosted request''s state: an opening entry, a step entry per offer, a closing entry.'
    source_finding: {phase: p3, register: analysis_findings, key: Q4}
    rationale: One truth; an abandoned request stays visibly open.
    constraints_imposed: No store holds a second copy of the state.
  - number: '5'
    decision: A token is chosen by the test model's rules, joined as it is.
    source_finding: {phase: p3, register: analysis_findings, key: Q5}
    rationale: A pattern split across tokens is judged on the text as built.
    constraints_imposed: The word transform is unchanged.
  - number: '6'
    decision: The permitted length is the smaller of the registered maximum and the rules' longest response.
    source_finding: {phase: p3, register: analysis_findings, key: Q6}
    rationale: The author answered.
    constraints_imposed: A step past it refuses the request as unfinished.
  - number: '7'
    decision: An offer for another model's fingerprint refuses the request; the host is not authenticated.
    source_finding: {phase: p3, register: analysis_findings, key: Q7}
    rationale: The author answered.
    constraints_imposed: The fingerprint is compared at every step.
  - number: '8'
    decision: Release closes the record with the text the business chose.
    source_finding: {phase: p3, register: analysis_findings, key: Q8}
    rationale: The host never supplies what is released.
    constraints_imposed: Release refuses a response not complete, or stopped.
  - number: '9'
    decision: Grounding is a response rule of the time in service, carried into the opening entry and applied by the token choice.
    source_finding: {phase: p3, register: analysis_findings, key: Q9}
    rationale: The author set it per time in service; the stored rules already carry it.
    constraints_imposed: Unset, it is off; no existing artifact changes.
  - number: '10'
    decision: The choice judges the compatibility form of the text, and does not begin a forbidden number the model read.
    source_finding: {phase: p3, register: analysis_findings, key: Q10}
    rationale: A rule judged only on completion lets a beginning through.
    constraints_imposed: A number the model did not read is judged when it is complete, unless grounding refuses it first.
  authoring_scope:
  - capability: Begin a hosted request
    gap_register_ref: GAP-01
  - capability: Confirm a hosted reading fits
    gap_register_ref: GAP-02
  - capability: Open the record of a hosted request
    gap_register_ref: GAP-03
  - capability: Read the state of a hosted request
    gap_register_ref: GAP-04
  - capability: Choose a permitted token
    gap_register_ref: GAP-05
  - capability: Offer the next candidates
    gap_register_ref: GAP-06
  - capability: Release a hosted response
    gap_register_ref: GAP-07
```

Consolidation of Stages 1–3. Every capability committed at Stage 3 appears here with the status its
decision implies. Nothing is re-litigated and nothing new is decided.

---

## 1. Discovery Summary

### Actors (actors)

### Entities (bm_entities)

### Resources

### Events (events)

### Relationships (Candidate Capabilities)

## 2. Capability Graph (capability_graph)

## 3. Dependency Graph (dependency_graph)

## 4. Constraint Register (constraint_register)

## 5. Gap Register (gap_register)

## 6. Design Decisions (design_decisions)

## 7. Authoring Scope (authoring_scope)

### In Scope — This CR

### Deferred — Future CR
| Capability | Deferred Reason |
|-----------|-----------------|
| Authenticate the host | Out of scope by the author's answer. |

## Pipeline Provenance

| Stage | Output | Status |
|-------|--------|--------|
| Stage 4 — Business Model | This document | COMPLETE |

---

## gov_projection — Governed Handoff to Stage 5

| Direction | Fields |
|-----------|--------|
| **Emits** → Stage 5 | actors · bm_entities · events · capability_graph · dependency_graph · constraint_register · gap_register · design_decisions · authoring_scope |
