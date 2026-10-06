# Stage 2 — Domain Model Verification: blockchain / identity and wallet

**Stage:** 2 — Domain Model Verification
**CR:** cr_06_routing_closure
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. What is
verified here is what each identity and wallet act does when a record it touches fails. Each
contract's steps were read for the outcomes their stores declare and the outcomes each step answers
for. Each act's routing was read for the outcomes its contracts can end with. The acceptance's
failed lookup was run directly against the pinned composition, with the address registry made
unreadable, on a scratch data root.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Person's Record | What the business holds about a person: their registration, their state and the decision made about them. | One keyed store, one record per contact address, unchanged by this change. | OBSERVED | S1 business_vocabulary #1 |
| The Claimed Address | The contact address a person holds, which no one else may hold. | One registry, one entry per address, unchanged by this change. | OBSERVED | S1 business_vocabulary #1 |
| The Trail | The moments in a person's or a wallet's history. | Append-only, unchanged by this change. | OBSERVED | S1 business_vocabulary #1 |
| The Wallet | The wallet an accepted person is given, and its claimed identity. | One keyed store and one registry, unchanged by this change. | OBSERVED | S1 business_vocabulary #1 |
| A Failed Record | A record that could not be read or written. | Not stored; it is an answer a store gives. | OBSERVED | S1 business_vocabulary #2 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| A Failed Record | The store's answer | BACKEND_ERROR: the store was unreachable or answered with an error. Every store identity and wallet use declares it. | OBSERVED | S2 belief_verification #1 |
| The Person's Record | State | Unverified, accepted or rejected. Unchanged by this change. | OBSERVED | S1 lifecycle_states #1 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a person | The person | A complete registration is recorded unverified; anything else is refused. | OBSERVED | S1 requested_outcomes #1 |
| Accept a person | An authority | An unverified person is recorded accepted; anything else is refused. | OBSERVED | S1 requested_outcomes #1 |
| Reject a person | An authority | An unverified person is recorded rejected, with grounds; anything else is refused. | OBSERVED | S1 requested_outcomes #1 |
| Create a wallet | An accepted person | A wallet is recorded for an accepted person; anything else is refused. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a person | 1 | Check the registration. | None. | OBSERVED | S2 pps_baseline_fqdns #5 |
| Register a person | 2 | Claim the contact address. | The claimed address. | OBSERVED | S2 pps_baseline_fqdns #2 |
| Register a person | 3 | Record the person unverified. | The person's record. | OBSERVED | S2 pps_baseline_fqdns #3 |
| Register a person | 4 | Record that they registered. | A moment on the trail. | OBSERVED | S2 pps_baseline_fqdns #4 |
| Accept or reject a person | 1 | Look the person up by their address, and read their record. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Accept or reject a person | 2 | Record the decision. | The person's record, in its decided parts. | OBSERVED | S2 pps_baseline_fqdns #6 |
| Accept or reject a person | 3 | Record that it occurred. | A moment on the trail. | OBSERVED | S2 pps_baseline_fqdns #4 |
| Create a wallet | 1 | Look the person up, and require them accepted. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Create a wallet | 2 | Claim the wallet's identity. | The claimed wallet identity. | OBSERVED | S2 pps_baseline_fqdns #7 |
| Create a wallet | 3 | Record the wallet. | The wallet. | OBSERVED | S2 pps_baseline_fqdns #8 |
| Create a wallet | 4 | Record that it was created. | A moment on the wallet's trail. | OBSERVED | S2 pps_baseline_fqdns #9 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Most identity and wallet acts stop without a declared ending when a record fails. | VERIFIED | Every store identity and wallet use declares BACKEND_ERROR for each operation they call. Thirteen act nodes run a contract that can end with BACKEND_ERROR, and none of the four acts routes it: blockchain::WF_REGISTER_ACTOR_V0 at three nodes, blockchain::WF_ACCEPT_ACTOR_V0 at three, blockchain::WF_REJECT_ACTOR_V0 at three, and blockchain::WF_CREATE_WALLET_V0 at four. The runtime refuses an unrouted outcome when one arises, so the act stops, but nothing the business declared says how it ended. | S1 system_beliefs #1 |
| When an acceptance's lookup of the person fails, identity carries on and records the acceptance. | VERIFIED | blockchain::CC_RESOLVE_ACTOR_V0's lookup step answers for SUCCESS, NOT_FOUND and VIOLATION, and its store, capability_side_effects::CS_REGISTRY_V0, also declares BACKEND_ERROR for RESOLVE. Run against the pinned composition with the address registry corrupted, the lookup answered BACKEND_ERROR; the runtime carried on to read the person's record, the contract reported SUCCESS, and the acceptance was recorded. The trace recorded neither the lookup's answer nor the decision to carry on. | S1 system_beliefs #2 |
| Three of wallet's steps carry on past a failed record in the same way. | VERIFIED | blockchain::CC_CLAIM_WALLET_IDENTITY_V0's claim step, blockchain::CC_CREATE_WALLET_RECORD_V0's write step and blockchain::CC_APPEND_WALLET_OCCURRENCE_V0's append step each omit BACKEND_ERROR, which their stores declare. Identity's reading step in blockchain::CC_RESOLVE_ACTOR_V0 omits it too. Five steps in four contracts. | S1 system_beliefs #3 |
| Each act already has a rejected ending. | VERIFIED | All four acts declare EXIT_REJECTED, and route every refusal they answer for there. | S1 system_beliefs #4 |
| Every identity and wallet act this change touches was published in v5. | VERIFIED | The four contracts whose steps change (blockchain::CC_RESOLVE_ACTOR_V0, blockchain::CC_CLAIM_WALLET_IDENTITY_V0, blockchain::CC_CREATE_WALLET_RECORD_V0, blockchain::CC_APPEND_WALLET_OCCURRENCE_V0) and the four acts whose routing changes (blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0, blockchain::WF_CREATE_WALLET_V0) are each in the sealed v5 composition. The four contracts that already end with BACKEND_ERROR keep what they declare. | S1 system_beliefs #5 |
| Entrances and intents name the workflows they start, and workflows name the contracts they run. | VERIFIED | The four contracts are run by blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_CREATE_WALLET_V0, all replaced here, and by blockchain::WF_RECORD_VERIFICATION_DECISION_V0, stood down before v5. The acts are named by blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 in handler.workflow, and by blockchain::IN_ACTOR_REGISTERED_V0, blockchain::IN_ACTOR_ACCEPTANCE_V0, blockchain::IN_ACTOR_REJECTION_V0 and blockchain::IN_WALLET_CREATION_V0 in workflow, by short code. Outside the composition, the identity and wallet execution validations and the RUNBOOK run the acts by full name. | S1 system_beliefs #6 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Looking a person up | blockchain::CC_RESOLVE_ACTOR_V0 | Resolves a contact address to the person's record, and reads it. | PARTIAL | Neither step answers for a failed record, so a failed lookup is carried past. |
| Claiming a contact address | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Claims the address a registration names. | PARTIAL | It ends with BACKEND_ERROR on a failed claim, and no act routes it. |
| Recording a person | blockchain::CC_REGISTER_ACTOR_V0 | Writes the person's record. | PARTIAL | It ends with BACKEND_ERROR on a failed write, and no act routes it. |
| Recording a moment on a person's trail | blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Appends a moment to the person's trail. | PARTIAL | It ends with BACKEND_ERROR on a failed append, and no act routes it. |
| Checking a registration | blockchain::CC_VALIDATE_REGISTRATION_V0 | Refuses an incomplete registration. | EXACT | Nothing for this purpose; it touches no record. |
| Recording a decision | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Records the decision it checked. | PARTIAL | It ends with BACKEND_ERROR on a failed write, and no act routes it. |
| Claiming a wallet's identity | blockchain::CC_CLAIM_WALLET_IDENTITY_V0 | Claims the identity a wallet is given. | PARTIAL | Its step does not answer for a failed claim, so the act carries past it. |
| Recording a wallet | blockchain::CC_CREATE_WALLET_RECORD_V0 | Writes the wallet's record. | PARTIAL | Its write step does not answer for a failed write. |
| Recording a moment on a wallet's trail | blockchain::CC_APPEND_WALLET_OCCURRENCE_V0 | Appends a moment to the wallet's trail. | PARTIAL | Its append step does not answer for a failed append. |
| Registration act | blockchain::WF_REGISTER_ACTOR_V0 | Checks, claims, records and announces a registration. | PARTIAL | Three nodes leave a failed record unrouted. |
| Acceptance act | blockchain::WF_ACCEPT_ACTOR_V0 | Looks the person up, records the acceptance and announces it. | PARTIAL | Three nodes leave a failed record unrouted. |
| Rejection act | blockchain::WF_REJECT_ACTOR_V0 | Requires grounds, looks the person up, records the rejection and announces it. | PARTIAL | Three nodes leave a failed record unrouted. |
| Wallet act | blockchain::WF_CREATE_WALLET_V0 | Looks the person up, claims and records a wallet, and announces it. | PARTIAL | Four nodes leave a failed record unrouted. |
| Registration entrance | blockchain::TI_REGISTER_ACTOR_V0 | Admits a caller's registration and starts the act it names. | PARTIAL | Names the published registration act. |
| Acceptance entrance | blockchain::TI_ACCEPT_ACTOR_V0 | Admits a caller's acceptance and starts the act it names. | PARTIAL | Names the published acceptance act. |
| Rejection entrance | blockchain::TI_REJECT_ACTOR_V0 | Admits a caller's rejection and starts the act it names. | PARTIAL | Names the published rejection act. |
| Registration intent | blockchain::IN_ACTOR_REGISTERED_V0 | Starts the registration act. | PARTIAL | Names the published registration act. |
| Acceptance intent | blockchain::IN_ACTOR_ACCEPTANCE_V0 | Starts the acceptance act. | PARTIAL | Names the published acceptance act. |
| Rejection intent | blockchain::IN_ACTOR_REJECTION_V0 | Starts the rejection act. | PARTIAL | Names the published rejection act. |
| Wallet intent | blockchain::IN_WALLET_CREATION_V0 | Starts the wallet act. | PARTIAL | Names the published wallet act. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Five steps carry on past a failed record. | CRITICAL | A person was accepted whose lookup had failed. The same can happen in wallet when a claim, a write or an append fails. | OBSERVED | S2 belief_verification #2 |
| Thirteen act nodes leave a failed record without a declared ending. | MAJOR | The act stops, and nothing the business declared says how it ended. The caller cannot tell a refusal from a failure nobody planned for. | OBSERVED | S2 belief_verification #1 |
| Eight published acts would mean something v5 did not say if changed in place. | CRITICAL | A citation of v5 would name acts that answer a failed record v5 left unanswered. | OBSERVED | S2 belief_verification #5 |
| Seven entrances and intents name the published acts. | MAJOR | Once the acts are stood down, they would still be started. | OBSERVED | S2 belief_verification #6 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The two gaps feed each other. When a step answers for a failed record, the contract can then end with it, and every act running that contract must route it. | Closing the five step gaps adds BACKEND_ERROR to two contracts that do not end with it today, and the act nodes running them gain a failed record to route. | OBSERVED | S2 belief_verification #3 |
| The stores already say they can fail. Nothing new is needed to name the failure. | Every store's operations declare BACKEND_ERROR among their outcomes. | OBSERVED | S2 entity_attributes #1 |
| Each act already has the ending a failed record should reach. | All four acts declare EXIT_REJECTED. | OBSERVED | S2 belief_verification #4 |
| The open standard now requires both closures. | `v1` Changes 3 and 4 of the Open PGC Standard require a composed step to answer for every outcome its store declares (CP-13), and construction to refuse an outcome no route answers (GC-15). This change makes identity and wallet meet both. | OBSERVED | S2 belief_verification #1 |
| A workflow's place keeps its label when the contract it runs is replaced. | The compiler maps each place's label to the contract it runs, so a binding that reads a place keeps working when only the contract's identity changes. | OBSERVED | S2 belief_verification #6 |
| A stood-down act may name a stood-down act. | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 runs the published lookup and is out of reach; it is not re-pointed. | OBSERVED | S2 belief_verification #6 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| An act that fails after recording something leaves that record in place. | A registration whose trail append fails has already recorded the person. The business decided a refusal changes no record, and that records made before a failure stay as they were. | MINOR | OBSERVED | S1 constraints #2 |
| A superseded act carries the same gap. | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 is superseded and no longer dispatched, so nothing reaches its two unrouted nodes. | MINOR | OBSERVED | S2 belief_verification #1 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
