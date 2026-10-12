# Stage 5 — Business Intent: causal_language_model / model_response

## Machine

```yaml
document:
  phase: p5
  domain: causal_language_model
  subdomain: model_response
  cr: cr_02_hosted_model
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The Model Response subdomain governs how a business's language model responds to a customer's
    question about the customer's own accounts, under rules that apply while the model writes and with
    a record of every answer and refusal. This change lets a pretrained model the business runs on its
    own machine, Qwen3 8B, answer under the same rules and record-keeping as the test model. The model's
    host asks the model for candidate tokens and passes them to the business; the business chooses what
    may be written, records every offer and choice, and alone releases a response. The test model's
    existing way of answering stays as it is.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: model_response
    purpose: Governs model responses under rules applied while the model writes, now through a hosted model as well as the test model.
    source_finding: {phase: p4, register: bm_entities, key: Hosted Request}
  scope_boundary:
  - capability: Begin a hosted request
    status: IN_SCOPE
    notes: Admitted as the test model's way admits.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Confirm a hosted reading fits
    status: IN_SCOPE
    notes: The reported size against the capacity.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Open the record of a hosted request
    status: IN_SCOPE
    notes: The opening entry of the trail.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Read the state of a hosted request
    status: IN_SCOPE
    notes: Reduced from the trail.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  - capability: Choose a permitted token
    status: IN_SCOPE
    notes: The test model's rules, on tokens.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-05}
  - capability: Offer the next candidates
    status: IN_SCOPE
    notes: One act per step.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-06}
  - capability: Release a hosted response
    status: IN_SCOPE
    notes: Only the business releases.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-07}
  - capability: Authenticate the host
    status: DEFERRED
    notes: Out of scope by the author's answer.
    source_finding: {phase: p4, register: authoring_scope, key: Authenticate the host}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: No token is written that a response rule forbids, including a pattern split across several tokens.
    business_reason: The rules apply while the model writes.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: No token is written except one the business chose from what was offered.
    business_reason: The host cannot override the choice.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  - invariant: No hosted response is released that is not complete.
    business_reason: An unfinished response is not released.
    source_finding: {phase: p1, register: business_invariants, row: 3}
  - invariant: No hosted response is released that is longer than its permitted length.
    business_reason: The limits are in force.
    source_finding: {phase: p1, register: business_invariants, row: 4}
  - invariant: No offer is accepted for a model other than the one the request was admitted for.
    business_reason: The record attributes every offer to the admitted model.
    source_finding: {phase: p1, register: business_invariants, row: 5}
  - invariant: Every hosted request is recorded from its admission, with every offer and choice.
    business_reason: Every request is recorded, answered, refused or abandoned.
    source_finding: {phase: p1, register: business_invariants, row: 6}
  - invariant: Only the business releases a response.
    business_reason: The host cannot send text to a customer.
    source_finding: {phase: p1, register: business_invariants, row: 7}
  actions:
  - action: Begin
    object: A hosted request
    trigger: An authorized requester submits a request to a hosted model
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Begin a hosted request}
  - action: Offer
    object: The next candidates
    trigger: The host passes what the model could write next
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Offer the next candidates}
  - action: Release
    object: A completed hosted response
    trigger: The host asks for release
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Release a hosted response}
  provisional_codes:
  - subdomain: model_response
    provisional_code: AC_MODEL_HOST_V0
    family: AC
    summary: The host of a model in service, which proposes and holds no authority
    source_finding: {phase: p4, register: actors, key: Host}
  - subdomain: model_response
    provisional_code: IN_BEGIN_HOSTED_RESPONSE_V0
    family: IN
    summary: A request to a hosted model on behalf of a customer
    source_finding: {phase: p4, register: capability_graph, key: Begin a hosted request}
  - subdomain: model_response
    provisional_code: WF_BEGIN_HOSTED_RESPONSE_V0
    family: WF
    summary: Admitting a hosted request and opening its record, or refusing it
    source_finding: {phase: p4, register: capability_graph, key: Begin a hosted request}
  - subdomain: model_response
    provisional_code: IN_OFFER_NEXT_TOKENS_V0
    family: IN
    summary: The candidates a hosted model could write next, naming its fingerprint
    source_finding: {phase: p4, register: capability_graph, key: Offer the next candidates}
  - subdomain: model_response
    provisional_code: WF_OFFER_NEXT_TOKENS_V0
    family: WF
    summary: Choosing a permitted token from an offer and recording the step, or refusing the request
    source_finding: {phase: p4, register: capability_graph, key: Offer the next candidates}
  - subdomain: model_response
    provisional_code: IN_RELEASE_HOSTED_RESPONSE_V0
    family: IN
    summary: A request to release a completed hosted response
    source_finding: {phase: p4, register: capability_graph, key: Release a hosted response}
  - subdomain: model_response
    provisional_code: WF_RELEASE_HOSTED_RESPONSE_V0
    family: WF
    summary: Releasing a completed hosted response from the record
    source_finding: {phase: p4, register: capability_graph, key: Release a hosted response}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_HOSTED_READING_FITS_V0
    family: CC
    summary: Refuse an offer whose reported reading size exceeds the model's capacity
    source_finding: {phase: p4, register: capability_graph, key: Confirm a hosted reading fits}
  - subdomain: model_response
    provisional_code: CC_OPEN_HOSTED_RECORD_V0
    family: CC
    summary: Form the rules in force and open the record of a hosted request
    source_finding: {phase: p4, register: capability_graph, key: Open the record of a hosted request}
  - subdomain: model_response
    provisional_code: CC_READ_HOSTED_STATE_V0
    family: CC
    summary: Read a hosted request's trail and reduce it to the response as built
    source_finding: {phase: p4, register: capability_graph, key: Read the state of a hosted request}
  - subdomain: model_response
    provisional_code: CC_CONFIRM_OFFER_FOR_MODEL_V0
    family: CC
    summary: Refuse an offer naming another model's fingerprint
    source_finding: {phase: p4, register: capability_graph, key: Offer the next candidates}
  - subdomain: model_response
    provisional_code: CC_CHOOSE_PERMITTED_TOKEN_V0
    family: CC
    summary: Choose a permitted token from an offer under the rules in force
    source_finding: {phase: p4, register: capability_graph, key: Choose a permitted token}
  - subdomain: model_response
    provisional_code: CC_RECORD_HOSTED_STEP_V0
    family: CC
    summary: Record an offer and the choice made from it in the request's trail
    source_finding: {phase: p4, register: capability_graph, key: Choose a permitted token}
  - subdomain: model_response
    provisional_code: CT_PURE_READ_HOSTED_STATE_V0
    family: CT
    summary: Reduce a hosted request's trail to its state
    source_finding: {phase: p4, register: capability_graph, key: Read the state of a hosted request}
  - subdomain: model_response
    provisional_code: CT_PURE_CHOOSE_PERMITTED_TOKEN_V0
    family: CT
    summary: Stop forbidden tokens and choose a permitted one
    source_finding: {phase: p4, register: capability_graph, key: Choose a permitted token}
  cross_subdomain_refs: []
```

---

## 1. Subdomain Purpose

---

## 2. Scope Boundary

---

## 3. Business Objects

---

## 4. Identity Semantics

---

## 5. Invariants

---

## 6. Actions

---

## 7. Provisional Codes

---

## 8. Cross-Subdomain References
