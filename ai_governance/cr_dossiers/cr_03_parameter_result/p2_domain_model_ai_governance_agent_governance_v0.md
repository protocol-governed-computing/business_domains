# Stage 2 — Domain Model Verification: ai_governance / agent_governance

**Stage:** 2 — Domain Model Verification
**CR:** cr_03_parameter_result
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The parameter
check's declaration was read for what it reports and where it reads it, the check underneath for what
it returns, and inspection was asked what names the parameter check.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Governed Action | An agent's proposed action, judged and recorded by the business. | Recorded in the governance audit. Unchanged by this change. | OBSERVED | S1 business_vocabulary #1 |
| The Parameter Check | The step that checks an action's parameters against the rules declared for its tool. | Not stored; run by the governed action. | OBSERVED | S1 business_vocabulary #2 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Parameter Check | Its result | What it reports: today always empty. | OBSERVED | S2 belief_verification #1 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Govern an agent's action | An agent | The action is authorized and recorded, or denied and audited. | OBSERVED | S1 requested_outcomes #3 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Govern an agent's action | 1 | Look up the rules declared for the tool. | None. | OBSERVED | S2 belief_verification #1 |
| Govern an agent's action | 2 | Check the parameters against them; a broken rule denies the action. | None. | OBSERVED | S2 belief_verification #1 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The parameter check reads its result from a place the check underneath never writes. | VERIFIED | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 maps `validation_result` from the check's `value`. capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 declares two outputs, `valid`, always true when it returns, and `failed_rule`, always null, and raises when a rule fails. Running the governed action, the result was empty every time. | S1 system_beliefs #1 |
| Only the governed action runs the parameter check. | VERIFIED | The composition's record names one artifact whose declaration names the parameter check: ai_governance::WF_GOVERN_AGENT_ACTION_V0, which runs it at one place, by short code. Inspection also reports ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0, through the workflow's route from the place it runs to this one; its declaration does not name the check. | S1 system_beliefs #2 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Checking parameters | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | Looks up the tool's rules and checks the parameters against them. | PARTIAL | Reports a result it never receives. |
| Checking against rules | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Returns that every rule passed, or denies. | EXACT | Nothing for this purpose. |
| Looking up a tool's rules | capability_transforms::CT_PURE_LOOKUP_V0 | Returns the rules declared for a tool. | EXACT | Nothing for this purpose. |
| Governing an action | ai_governance::WF_GOVERN_AGENT_ACTION_V0 | Runs the five governance steps and audits each decision. | EXACT | Nothing; it runs whichever parameter check it names. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The parameter check reports a result it never receives. | CRITICAL | Once the platform refuses a result that was never received, every governed action is refused. | OBSERVED | S2 belief_verification #1 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The governed action names the check at one place, and labels and routes to that place by the same spelling. | Its place, its route and the check it runs are all written `CC_VALIDATE_TOOL_PARAMETERS_V0`; only the last names the check. | OBSERVED | S2 belief_verification #2 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| NONE IDENTIFIED | | | | |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
