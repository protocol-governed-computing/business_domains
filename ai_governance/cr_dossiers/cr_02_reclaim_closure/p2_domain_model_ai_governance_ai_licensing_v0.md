# Stage 2 — Domain Model Verification: ai_governance / ai_licensing

**Stage:** 2 — Domain Model Verification
**CR:** cr_02_reclaim_closure
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

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Assignment | The registry's answer to a removal | Removed, not found, refused, or unreachable. | OBSERVED | S2 belief_verification #1 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Reclaim an unused license | The business, on its schedule | The license is reclaimed, stays active, or the reclaim ends in error. | OBSERVED | S1 known_facts #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Reclaim an unused license | 1 | Check whether the license has gone unused for the threshold of days, and refuse if not. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Reclaim an unused license | 2 | Remove the employee's assignment from the registry. | The assignment, removed. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Reclaim an unused license | 3 | Record that the license was revoked. | An audit entry. | OBSERVED | S2 pps_baseline_fqdns #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The step that removes an assignment does not answer a refused removal. | VERIFIED | capability_side_effects::CS_REGISTRY_V0 declares SUCCESS, NOT_FOUND, VIOLATION and BACKEND_ERROR for DEREGISTER. The deregister_license step of ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 answers SUCCESS, NOT_FOUND and BACKEND_ERROR, and not VIOLATION. | S1 system_beliefs #1 |
| The reclaim already ends as still active for a license that is not inactive. | VERIFIED | The inactivity check reports VIOLATION for a license still in use. ai_governance::WF_AUTO_RECLAIM_V0 routes the contract's VIOLATION to EXIT_ACTIVE, and the contract already declares VIOLATION among the outcomes it can end with. | S1 system_beliefs #2 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Reclaiming a license | ai_governance::CC_RECLAIM_UNUSED_LICENSE_V0 | Checks inactivity, then removes the assignment. | PARTIAL | Its removal step does not answer a refused removal. |
| Recording the revocation | ai_governance::WF_AUTO_RECLAIM_V0 | Runs the reclaim and records a revocation when it succeeds. | EXACT | Nothing for this purpose; it already routes VIOLATION to still active. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| The removal step does not answer a refused removal. | MAJOR | A reclaim the registry refused would carry on, and be recorded as a revocation. | OBSERVED | S2 belief_verification #1 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| One answer ends the reclaim two ways. | A refused removal and a license still in use both end the contract with VIOLATION, so both reach EXIT_ACTIVE. Both leave the license assigned, which is what that ending says. | OBSERVED | S2 belief_verification #2 |
| The open standard now requires the closure. | `v1` Change 3 of the Open PGC Standard requires a composed step to answer every outcome its capability declares. | OBSERVED | S2 belief_verification #1 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The reclaim has never been stated in a design. | The first licensing change reused the reclaim unchanged, so this change states it whole for the first time. | MINOR | OBSERVED | S2 pps_baseline_fqdns #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
