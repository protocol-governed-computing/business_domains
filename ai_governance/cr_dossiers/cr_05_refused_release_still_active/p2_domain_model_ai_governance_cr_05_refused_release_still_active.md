# Stage 2 — Domain Model — ai_governance / ai_licensing, agent_governance

## Machine

```yaml
document:
  phase: p2
  domain: ai_governance
  subdomain:
  - ai_licensing
  - agent_governance
  cr: cr_05_refused_release_still_active
  rule_set: transformation.schemas.REGISTER_SCHEMA_P2_V0
registers:
  entities:
  - entity: Employee
    description: Licenses go only to employees the business has registered, and only once their training is recorded.
    store_model: One durable record per employee, addressed by its employee id, updated in place.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 1}
  - entity: License cap
    description: The business limits how many licenses may be assigned at once, across both tiers.
    store_model: One durable record of the license cap.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: License
    description: The business keeps which employee holds which tier of license, when it was last used, and whether it was taken back.
    store_model: One durable record per license, addressed by its employee id, updated in place, carrying its own state (active and reclaimed).
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Action
    description: The business keeps each action an agent was authorized to take, registered once however often it is proposed.
    store_model: One durable record per action, addressed by its tool name, requesting user id and domain context.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 4}
  entity_attributes:
  - entity: Employee
    attribute: Employee id
    meaning: What identifies an employee.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 1}
  - entity: License cap
    attribute: Cap key
    meaning: What identifies the license cap.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 2}
  - entity: License cap
    attribute: Cap
    meaning: Required when a license cap is recorded, as an integer.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 2}
  - entity: License
    attribute: Employee id
    meaning: What identifies a license.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 3}
  - entity: License
    attribute: Tier
    meaning: Required when a license is recorded, as a string.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: business_vocabulary, row: 3}
  - entity: Action
    attribute: Tool name
    meaning: What identifies an action.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 4}
  - entity: Action
    attribute: Requesting user id
    meaning: What identifies an action.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 4}
  - entity: Action
    attribute: Domain context
    meaning: What identifies an action.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: identity_and_sameness, row: 4}
  business_processes:
  - process: Register employee
    initiator: System
    outcome: Records a new employee.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Record training completed
    initiator: System
    outcome: Changes an employee's training completed.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Set license cap
    initiator: System
    outcome: Records a new license cap.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Provision license
    initiator: Employee
    outcome: Records a new license.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Record license usage
    initiator: Employee
    outcome: Changes a license's last used at.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Reclaim license
    initiator: System
    outcome: Moves a license from active to reclaimed.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Govern agent action
    initiator: Agent
    outcome: Records a new action.
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  process_steps:
  - process: Register employee
    step: '1'
    action: Refuse when an employee that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 1}
  - process: Register employee
    step: '2'
    action: Records a new employee
    record_produced: The employee record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Register employee
    step: '3'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  - process: Record training completed
    step: '1'
    action: Refuse when the employee is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 2}
  - process: Record training completed
    step: '2'
    action: Changes an employee's training completed
    record_produced: The employee record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Record training completed
    step: '3'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 2}
  - process: Set license cap
    step: '1'
    action: Records a new license cap
    record_produced: The license cap record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Set license cap
    step: '2'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 3}
  - process: Provision license
    step: '1'
    action: Refuse when a license that is the same is already recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 3}
  - process: Provision license
    step: '2'
    action: Refuse when training completed does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 4}
  - process: Provision license
    step: '3'
    action: Refuse when tier admitted does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 5}
  - process: Provision license
    step: '4'
    action: Refuse when cap set does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 6}
  - process: Provision license
    step: '5'
    action: Refuse when under the cap does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 7}
  - process: Provision license
    step: '6'
    action: Records a new license
    record_produced: The license record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Provision license
    step: '7'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 4}
  - process: Record license usage
    step: '1'
    action: Refuse when the license is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 8}
  - process: Record license usage
    step: '2'
    action: Changes a license's last used at
    record_produced: The license record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Record license usage
    step: '3'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 5}
  - process: Reclaim license
    step: '1'
    action: Refuse when the license is not recorded
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 9}
  - process: Reclaim license
    step: '2'
    action: Refuse when the license is not active
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 10}
  - process: Reclaim license
    step: '3'
    action: Moves a license from active to reclaimed
    record_produced: The license record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Reclaim license
    step: '4'
    action: Record the operation on the ai_licensing trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 6}
  - process: Govern agent action
    step: '1'
    action: Refuse when tool declared does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 11}
  - process: Govern agent action
    step: '2'
    action: Refuse when license active does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 12}
  - process: Govern agent action
    step: '3'
    action: Refuse when tier grants tool does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 13}
  - process: Govern agent action
    step: '4'
    action: Refuse when parameters satisfy rules does not hold
    record_produced: A refusal, and nothing recorded
    evidence_status: INFERRED
    source_finding: {phase: p1, register: operation_refusals, row: 14}
  - process: Govern agent action
    step: '5'
    action: Records a new action
    record_produced: The action record
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  - process: Govern agent action
    step: '6'
    action: Record the operation on the agent_governance trail
    record_produced: A trail entry
    evidence_status: INFERRED
    source_finding: {phase: p1, register: requested_outcomes, row: 7}
  belief_verification:
  - belief: The current ai_licensing design names the records, entrances and requests its callers use today.
    result: VERIFIED
    evidence: The baseline design names ai_governance::RB_LICENSE_BINDINGS_V1, ai_governance::IN_PROVISION_LICENSE_V0 and ai_governance::IN_RECLAIM_LICENSE_V1, and the derived design carries them.
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - belief: The current agent_governance design names the records, entrances and requests its callers use today.
    result: VERIFIED
    evidence: The baseline design names ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1 and ai_governance::IN_AGENT_ACTION_REQUESTED_V1, and the derived design carries them.
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  pps_baseline_fqdns:
  - capability: Appendonly jsonl side effect, as the platform declares it
    fqdn: capability_side_effects::CS_APPENDONLY_JSONL_V0
    what_it_does: Provide an append-only JSONL persistence layer with ordered event history.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Clock side effect, as the platform declares it
    fqdn: capability_side_effects::CS_CLOCK_V0
    what_it_does: Answers the time now.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Mutable json side effect, as the platform declares it
    fqdn: capability_side_effects::CS_MUTABLE_JSON_V0
    what_it_does: Provide a mutable key-addressable JSON state store with last-write-wins semantics.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Registry side effect, as the platform declares it
    fqdn: capability_side_effects::CS_REGISTRY_V0
    what_it_does: Provide a registry capability for stable indirection by binding symbolic keys to opaque addresses and underlying storage references.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Assemble record transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0
    what_it_does: Combines multiple input values into a single structured record object.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Generate id transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_GENERATE_ID_V0
    what_it_does: Generates a deterministic unique identifier based on input data using Keccak-256 hashing.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Lookup transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_LOOKUP_V0
    what_it_does: Returns the value associated with a key from a provided key-value mapping object.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate parameter rules transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0
    what_it_does: Evaluate declarative parameter constraint rules against a parameter map.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate record structure transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0
    what_it_does: Validate a record against a provided schema of field validation rules.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  - capability: Validate set membership transform, as the platform declares it
    fqdn: capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0
    what_it_does: Validate that a value is a member of a declared set.
    fit: EXACT
    cannot_do: 'Nothing this design asks of it: every step the derived design binds to it uses an operation it declares.'
  gaps:
  - gap: 1 artifacts the composition holds mean something other than the ledger decides.
    severity: MAJOR
    impact: Each takes the next unused version and names its predecessor as superseded.
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  architectural_observations:
  - observation: The ai_licensing design keeps its records through one binding, and the derived design carries its name.
    evidence: ai_governance::RB_LICENSE_BINDINGS_V1 · ai_governance::STRUCTURE_AI_LICENSING_STORAGE_V1
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 1}
  - observation: The agent_governance design keeps its records through one binding, and the derived design carries its name.
    evidence: ai_governance::RB_AGENT_GOVERNANCE_BINDINGS_V1 · ai_governance::STRUCTURE_AGENT_GOVERNANCE_STORAGE_V1
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: system_beliefs, row: 2}
  - observation: 58 artifacts the composition holds mean what the ledger decides, and keep their identity.
    evidence: ai_governance::AC_AGENT_V0 · ai_governance::AC_EMPLOYEE_V1 · ai_governance::AC_SYSTEM_V0
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  discovery_concerns:
  - concern: 1 artifacts change meaning, so a caller that dispatches by identity must follow supersedes.
    evidence: ai_governance::WF_RECLAIM_LICENSE_V0 · ai_governance::WF_RECLAIM_LICENSE_V1
    severity: MAJOR
    evidence_status: OBSERVED
    source_finding: {phase: p1, register: requested_outcomes, row: 1}
  open_questions: []
```

Projected from what the derivation observed: the baseline design, the derived design and the composition the inspector reads. Every row cites the change-request row it models.

---

## 1. Business Entities

---

## 2. Business Processes

---

## 3. Belief Verification — THE SPINE (fill this register FIRST)

---

## 4. PPS Baseline — What Already Exists

---

## 5. Gap Analysis — What Is Missing

---

## 6. Architectural Observations

---

## 7. Discovery Concerns

---

## 8. Open Questions for Stage 3

---

## gov_projection — Governed Handoff to Stage 3

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | architectural_observations · belief_verification · business_processes · discovery_concerns · entities · entity_attributes · gaps · open_questions · pps_baseline_fqdns · process_steps |
| **Emits** → Stage 3 | entities · entity_attributes · business_processes · process_steps · belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
