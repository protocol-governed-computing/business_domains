# Stage 5 — Business Intent: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p5
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P5_V0
registers:
  subdomain_purpose: |2

    The AI Licensing subdomain governs the business's licenses for AI tools: provisioning a license to an
    employee while licenses remain under the business's cap and once the employee has completed the
    required training, and reclaiming a license that has gone unused for the business's threshold of
    days. Each of its checks refuses when its answer is no. It does not govern what an agent may do,
    which employees exist, or which tools the business licenses.
  purpose_provenance:
  - source: CR seed §0 Subdomain Purpose
    disposition: INHERITED
    refinement: ''
  subdomain_purposes:
  - subdomain: ai_licensing
    purpose: Governs the business's AI tool licenses, and now proves each check it decides them by.
    source_finding: {phase: p4, register: bm_entities, key: The Case}
  scope_boundary:
  - capability: Prove the license check
    status: IN_SCOPE
    notes: Stated with its cases; decides nothing new.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-01}
  - capability: Prove the training check
    status: IN_SCOPE
    notes: Stated with its cases; decides nothing new.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-02}
  - capability: Prove the inactivity check
    status: IN_SCOPE
    notes: Stated with its cases; decides nothing new.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-03}
  - capability: Compile the cases stated beside each check
    status: IN_SCOPE
    notes: Reached through its generator.
    source_finding: {phase: p4, register: authoring_scope, key: GAP-04}
  business_objects: []
  identity_semantics: []
  invariants:
  - invariant: No check answers no; a no is a refusal.
    business_reason: A check that answered no would let its act continue.
    source_finding: {phase: p1, register: business_invariants, row: 1}
  - invariant: Every check is proven on every build by the cases stated beside it.
    business_reason: A check nothing proves can change unseen.
    source_finding: {phase: p1, register: business_invariants, row: 2}
  actions:
  - action: Prove
    object: Each check, by its cases
    trigger: Every build
    status: IN_SCOPE
    source_finding: {phase: p4, register: capability_graph, key: Prove the license check}
  provisional_codes: null
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
