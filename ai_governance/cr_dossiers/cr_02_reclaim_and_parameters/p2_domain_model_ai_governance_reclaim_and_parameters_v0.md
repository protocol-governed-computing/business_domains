# Stage 2 — Domain Model Verification: ai_governance / reclaim and parameter result

**Stage:** 2 — Domain Model Verification
**CR:** cr_02_reclaim_and_parameters
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The registry's
declaration was read for the answers its removal can give, the reclaim contract for the answers its
removal step handles, and the reclaim act for where it sends each answer.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Assignment | The registry's record that a license belongs to an employee. | One registry, one entry per employee, unchanged by this change. | OBSERVED | S1 business_vocabulary #2 |
| The Reclaim | Taking back a license gone unused for the threshold of days. | Not stored; an act. Announced when it removes an assignment. | OBSERVED | S1 business_vocabulary #1 |
| The Governed Action | An agent's proposed action, judged and recorded by the business. | Recorded in the governance audit. Unchanged by this change. | OBSERVED | S1 business_vocabulary #4 |
| The Parameter Check | The step that checks an action's parameters against the rules declared for its tool. | Not stored; run by the governed action. | OBSERVED | S1 business_vocabulary #5 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Assignment | The registry's answer to a removal | Removed, not found, refused, or unreachable. | OBSERVED | S2 belief_verification #1 |
| The Parameter Check | Its result | What it reports: today always empty. | OBSERVED | S2 belief_verification #3 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Reclaim an unused license | The business, on its schedule | The license is reclaimed, stays active, or the reclaim ends in error. | OBSERVED | S1 known_facts #1 |
| Govern an agent's action | An agent | The action is authorized and recorded, or denied and audited. | OBSERVED | S1 requested_outcomes #3 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Reclaim an unused license | 1 | Check whether the license has gone unused for the threshold of days, and refuse if not. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Reclaim an unused license | 2 | Remove the employee's assignment from the registry. | The assignment, removed. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Reclaim an unused license | 3 | Record that the license was revoked. | An audit entry. | OBSERVED | S2 pps_baseline_fqdns #2 |
| Govern an agent's action | 1 | Look up the rules declared for the tool. | None. | OBSERVED | S2 belief_verification #3 |
| Govern an agent's action | 2 | Check the parameters against them; a broken rule denies the action. | None. | OBSERVED | S2 belief_verification #3 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The step that removes an assignment does not answer a refused removal. | VERIFIED | capability_side_effects::CS_REGISTRY_V0 declares SUCCESS, NOT_FOUND, VIOLATION and BACKEND_ERROR for DEREGISTER. The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 answers SUCCESS, NOT_FOUND and BACKEND_ERROR, and not VIOLATION. | S1 system_beliefs #1 |
| The reclaim already ends as still active for a license that is not inactive. | VERIFIED | The inactivity check reports VIOLATION for a license still in use. ai_governance::WF_AUTO_RECLAIM_V0 routes the contract's VIOLATION to EXIT_ACTIVE, and the contract already declares VIOLATION among the outcomes it can end with. | S1 system_beliefs #2 |
| The parameter check reads its result from a place the check underneath never writes. | VERIFIED | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 maps `validation_result` from the check's `value`. capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 declares two outputs, `valid`, always true when it returns, and `failed_rule`, always null, and raises when a rule fails. Running the governed action, the result was empty every time. | S1 system_beliefs #3 |
| Both acts this change touches were published in v5. | VERIFIED | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 and ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 are each in the sealed v5 composition. | S1 system_beliefs #4 |
| One workflow runs each of the two contracts. | VERIFIED | ai_governance::WF_AUTO_RECLAIM_V0 runs the reclaim at one place, by short code, and is the only artifact whose declaration names it; ai_governance::IN_RECLAIM_LICENSE_V0 reaches it only by a routing edge. The composition's record names one artifact whose declaration names the parameter check: ai_governance::WF_GOVERN_AGENT_ACTION_V0, which runs it at one place, by short code. Inspection also reports ai_governance::CC_BIND_LICENSE_TO_TOOL_SURFACE_V0, through the workflow's route from the place it runs to this one; its declaration does not name the check. | S1 system_beliefs #5 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Reclaiming a license | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Checks inactivity, then removes the assignment. | PARTIAL | Its removal step does not answer a refused removal. |
| Recording the revocation | ai_governance::WF_AUTO_RECLAIM_V0 | Runs the reclaim and records a revocation when it succeeds. | PARTIAL | It already routes VIOLATION to still active; it names the published reclaim. |
| Checking parameters | ai_governance::CC_VALIDATE_TOOL_PARAMETERS_V0 | Looks up the tool's rules and checks the parameters against them. | PARTIAL | Reports a result it never receives. |
| Checking against rules | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Returns that every rule passed, or denies. | EXACT | Nothing for this purpose. |
| Looking up a tool's rules | capability_transforms::CT_PURE_LOOKUP_V0 | Returns the rules declared for a tool. | EXACT | Nothing for this purpose. |
| Governing an action | ai_governance::WF_GOVERN_AGENT_ACTION_V0 | Runs the five governance steps and audits each decision. | PARTIAL | It names the published parameter check; it runs whichever check it names. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The removal step does not answer a refused removal. | MAJOR | A reclaim the registry refused would carry on, and be recorded as a revocation. | OBSERVED | S2 belief_verification #1 |
| The parameter check reports a result it never receives. | CRITICAL | Once the platform refuses a result that was never received, every governed action is refused. | OBSERVED | S2 belief_verification #3 |
| Two published acts would mean something v5 did not say if changed in place. | CRITICAL | A citation of v5 would name a reclaim and a parameter check that answer differently. | OBSERVED | S2 belief_verification #4 |
| Two workflows run the published acts. | MAJOR | Once the acts are stood down, they would still be run. | OBSERVED | S2 belief_verification #5 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| One answer ends the reclaim two ways. | A refused removal and a license still in use both end the contract with VIOLATION, so both reach EXIT_ACTIVE. Both leave the license assigned, which is what that ending says. | OBSERVED | S2 belief_verification #2 |
| The open standard now requires the closure. | `v1` Change 3 of the Open PGC Standard requires a composed step to answer every outcome its capability declares. | OBSERVED | S2 belief_verification #1 |
| The governed action names the check at one place, and labels and routes to that place by the same spelling. | Its place, its route and the check it runs are all written `CC_VALIDATE_TOOL_PARAMETERS_V0`; only the last names the check. | OBSERVED | S2 belief_verification #5 |
| A workflow's place keeps its label when the contract it runs is replaced. | The compiler maps each place's label to the contract it runs, so a binding that reads a place keeps working when only the contract's identity changes. | OBSERVED | S2 belief_verification #5 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The reclaim has never been stated in a design. | The first licensing change reused the reclaim unchanged, so this change states it whole for the first time. | MINOR | OBSERVED | S2 pps_baseline_fqdns #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
