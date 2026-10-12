# Stage 6 — Governance Intent: ai_governance / ai_licensing

## Machine

```yaml
document:
  phase: p6
  domain: ai_governance
  subdomain: ai_licensing
  cr: cr_01_licensing
  rule_set: transformation.schemas.REGISTER_SCHEMA_P6_V0
registers:
  ownership:
  - capability: Prove the license check
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Prove the license check}
  - capability: Prove the training check
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Prove the training check}
  - capability: Prove the inactivity check
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Prove the inactivity check}
  - capability: Compile the cases stated beside each check
    owner_subdomain: ai_licensing
    disposition: OWNED
    existing_artifact: ''
    source_finding: {phase: p5, register: scope_boundary, key: Compile the cases stated beside each check}
  storage_governance: []
  cross_subdomain_deps: []
  pps_artifacts_requiring_action:
  - fqdn: ai_governance::CT_PURE_CHECK_QUOTA_AVAILABLE_V0
    current_status: Present; unproven
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The license check}
  - fqdn: ai_governance::CT_PURE_CHECK_TRAINING_STATUS_V0
    current_status: Present; unproven
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The training check}
  - fqdn: ai_governance::CT_PURE_EVALUATE_INACTIVITY_V0
    current_status: Present; unproven
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The inactivity check}
  - fqdn: ai_governance::STRUCTURE_BUILD_AI_GOVERNANCE_CONFIG_V0
    current_status: Present; does not compile stated cases
    action: EXTEND
    source_finding: {phase: p3, register: dependency_discoveries, key: The build configuration}
  - fqdn: ai_governance::CC_VALIDATE_ELIGIBILITY_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The acts using the checks}
  - fqdn: ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0
    current_status: Present and reused unchanged
    action: REUSE
    source_finding: {phase: p3, register: dependency_discoveries, key: The acts using the checks}
  boundary_rules:
  - rule_name: A_CHECK_IS_PROVEN_BESIDE_ITSELF
    statement: Each check's cases are stated with it and run on every build.
    source_finding: {phase: p4, register: design_decisions, row: 1}
  - rule_name: A_NO_IS_A_REFUSAL
    statement: Every no case expects a refusal.
    source_finding: {phase: p4, register: design_decisions, row: 2}
  - rule_name: THE_CONFIGURATION_IS_GENERATED
    statement: The build configuration is reached through its generator.
    source_finding: {phase: p4, register: design_decisions, row: 4}
  governance_outcome:
  - capability: Prove the license check
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Prove the license check}
  - capability: Prove the training check
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Prove the training check}
  - capability: Prove the inactivity check
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Prove the inactivity check}
  - capability: Compile the cases stated beside each check
    owner_subdomain: ai_licensing
    source_finding: {phase: p6, register: ownership, key: Compile the cases stated beside each check}
```

Nothing moves and nothing is added: each check stays where it is and gains the cases that prove it.

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
