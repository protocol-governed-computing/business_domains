# Stage 2 — Domain Model Discovery: blockchain / wallet
**Stage:** 2 — Domain Model Discovery
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief carried from Stage 1 was grounded against the pinned snapshot through the inspection
interface. What was searched is recorded, not only what was found.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| Wallet | Where an accepted person holds value. | None. No store holds a wallet anywhere in the composition. | NOT_FOUND | S1 business_vocabulary #1 |
| Holder | The accepted person a wallet belongs to. Already held by the business as a person. | A record of people, keyed by the address they registered with. | VERIFIED | S1 business_vocabulary #2 |
| Balance | What a wallet carries. | None. | NOT_FOUND | S1 business_vocabulary #3 |
| Address | What others may pay to. | None. | NOT_FOUND | S1 business_vocabulary #6 |
| Occurrence | A moment the business recorded, added to and never rewritten. | A trail of occurrences against a person. | VERIFIED | S1 business_vocabulary #9 |

### Entity Attributes

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Wallet | Its own identity | Distinguishes one wallet from another. | NOT_FOUND | S1 identity_and_sameness #1 |
| Wallet | Holder | The one person it belongs to. | NOT_FOUND | S1 business_invariants #1 |
| Wallet | Balance | What it carries. Zero when created, never negative. | NOT_FOUND | S1 known_facts #14 |
| Wallet | Denomination | The currency the balance is expressed in. | NOT_FOUND | S1 known_facts #16 |
| Wallet | Classification | What kind of wallet it is. Default for every wallet this change creates. | NOT_FOUND | S1 known_facts #15 |
| Wallet | Address | What others may pay to. | NOT_FOUND | S1 known_facts #7 |
| Wallet | State | Active when created; may become inactive; may be closed. | NOT_FOUND | S1 lifecycle_states #1 |
| Holder | Registered details | What the person supplied and keeps. | VERIFIED | S1 system_beliefs #2 |
| Holder | State | Whether the business has accepted, rejected, or not yet decided about them. | VERIFIED | S1 system_beliefs #1 |
| Occurrence | What occurred, and when | The moment and its time. | VERIFIED | S1 known_facts #19 |

---

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Giving an accepted person a wallet | The acceptance of a person | The person holds a wallet, and the moment is on the trail. | NOT_FOUND | S1 requested_outcomes #1 |
| Registering a person | The person | The person is held, unverified. | VERIFIED | S1 system_beliefs #1 |
| Recording a decision about a person | An authority | The person is accepted or rejected, keeping the details they registered with. | VERIFIED | S1 system_beliefs #1 |

### Process Steps

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Giving an accepted person a wallet | 1 | Establish that the person is one the business holds and has accepted. | None. | NOT_FOUND | S1 operation_refusals #1 |
| Giving an accepted person a wallet | 2 | Determine the wallet's identity, and stop if the person already holds one. | None. | NOT_FOUND | S1 operation_refusals #3 |
| Giving an accepted person a wallet | 3 | Establish the address others may pay to, from key material supplied to the business. | None. | NOT_FOUND | S1 known_facts #18 |
| Giving an accepted person a wallet | 4 | Record the wallet, with a balance of zero, its denomination and its classification. | The wallet. | NOT_FOUND | S1 known_facts #14 |
| Giving an accepted person a wallet | 5 | Record that the wallet was created, for whom, and when. | An occurrence on the trail. | NOT_FOUND | S1 requested_outcomes #4 |
| Recording a decision about a person | 1 | Establish the person exists and has not already been decided about. | None. | VERIFIED | S1 system_beliefs #1 |
| Recording a decision about a person | 2 | Record the decision, the authority, and the grounds where stated. | The person's state, and an occurrence. | VERIFIED | S1 system_beliefs #4 |

---

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them. | VERIFIED | Twenty-three artifacts are held for this domain, all owned by identity, including `blockchain::WF_REGISTER_ACTOR_V0` and `blockchain::WF_RECORD_VERIFICATION_DECISION_V0`, reachable through `blockchain::TI_REGISTER_ACTOR_V0`, `blockchain::TI_ACCEPT_ACTOR_V0` and `blockchain::TI_REJECT_ACTOR_V0`. | S1 system_beliefs #1 |
| A person keeps the details they registered with when a decision is recorded about them. | VERIFIED | Exercising the function against the pinned composition shows an accepted person still carrying the name and preferences they registered with, alongside the deciding authority and the time. | S1 system_beliefs #2 |
| Identity declares that it announces an acceptance, and does not actually announce it. | VERIFIED | Three moments are declared — `blockchain::EV_ACTOR_ACCEPTED_V0`, `blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0`, `blockchain::EV_ACTOR_REJECTED_V0`. Each reports a reference count of zero: nothing in the composition refers to any of them, so no announcement can be made from anywhere. | S1 system_beliefs #3 |
| A rejection stating no grounds is currently accepted and recorded rather than refused. | VERIFIED | Grounds are declared as required where a rejection is admitted at the boundary, and no step of the contract that records a decision reads them. Exercising the function, a rejection stating no grounds succeeds and the person is rejected. | S1 system_beliefs #4 |
| No wallet exists anywhere in the business today. | NOT_FOUND | Searching the composition's whole vocabulary for the term returns no match. No entity, store, process or moment concerning a wallet is held anywhere. | S1 system_beliefs #5 |
| A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail. | INSUFFICIENT_EVIDENCE | Nothing of that design is present in this composition, so the snapshot cannot confirm or refute it. What the business still holds to was established by the business itself and is recorded as truth in the change request rather than as a finding here. | S1 system_beliefs #6 |

---

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Records a decision about a person | blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Accepts or rejects a person, keeping their registered details. | PARTIAL | Announces nothing, so nothing can follow acceptance. Does not require grounds on a rejection. |
| Registers a person | blockchain::WF_REGISTER_ACTOR_V0 | Admits a person unverified on their own claim. | EXACT | Nothing about a wallet. |
| Holds people | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Declares where people and their occurrences are held. | PARTIAL | Declares nowhere to hold a wallet. |
| Declares the acceptance moment | blockchain::EV_ACTOR_ACCEPTED_V0 | Names the moment a person is accepted. | PARTIAL | Is referenced by nothing and is therefore never announced. |
| Declares the registration moment | blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | Names the moment a person is admitted unverified. | PARTIAL | Is referenced by nothing. |
| Declares the rejection moment | blockchain::EV_ACTOR_REJECTED_V0 | Names the moment a person is rejected. | PARTIAL | Is referenced by nothing. |
| Admits a rejection | blockchain::TI_REJECT_ACTOR_V0 | Admits a rejection at the boundary, declaring grounds as required. | PARTIAL | Requiring grounds at the boundary is not the same as refusing a rejection that states none; no step reads them. |
| Holds a changing record | capability_side_effects::CS_MUTABLE_JSON_V0 | Holds records that change. | EXACT | Nothing specific to a wallet. |
| Holds a trail | capability_side_effects::CS_APPENDONLY_JSONL_V0 | Holds a trail added to and never rewritten. | EXACT | Nothing specific to a wallet. |
| Claims an identity | capability_side_effects::CS_REGISTRY_V0 | Claims a key so two things cannot share one identity. | EXACT | Nothing specific to a wallet. |
| Supplies the time | capability_side_effects::CS_CLOCK_V0 | Supplies the current time. | EXACT | Nothing specific to a wallet. |
| Determines an identity | capability_transforms::CT_PURE_GENERATE_ID_V0 | Derives an identity from what it is given. | EXACT | Nothing specific to a wallet. |

---

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Nothing holds a wallet. | CRITICAL | The whole of this change. There is nowhere to record that a person holds value. | NOT_FOUND | S1 system_beliefs #5 |
| No moment is ever announced, so nothing can follow an acceptance. | CRITICAL | A wallet follows acceptance. If acceptance is never announced, wallet creation has nothing to follow. | VERIFIED | S1 system_beliefs #3 |
| A rejection stating no grounds is not refused. | CRITICAL | The business's own rule is unenforced, and refusals are on record with no reason attached. | VERIFIED | S1 system_beliefs #4 |
| There is no way to establish an address others may pay to. | CRITICAL | A wallet must have one. | NOT_FOUND | S1 known_facts #7 |
| Nothing declares where a wallet would be held. | CRITICAL | A record with nowhere to live cannot be written. | NOT_FOUND | S1 system_beliefs #5 |
| The business's own currency is not named anywhere in the composition. | OPEN QUESTION | Every wallet is denominated in it. | NOT_FOUND | S1 assumptions #3 |

---

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| Every artifact this domain holds belongs to identity. Wallet would be the domain's second function. | Twenty-three artifacts, all recorded against the identity subdomain. | VERIFIED | S1 system_beliefs #1 |
| A declared moment that nothing refers to is indistinguishable, from the outside, from a moment the business never declared. | All three declared moments report a reference count of zero. | VERIFIED | S1 system_beliefs #3 |
| A requirement stated where a request is admitted is not the same as a rule the business enforces. Grounds are declared required at the boundary and read by nothing thereafter. | The contract that records a decision does not mention grounds. | VERIFIED | S1 system_beliefs #4 |
| Everything a wallet needs in order to be held, identified, timed and trailed already exists in the platform's closed set. Nothing new of that kind is required. | Five capabilities cover holding, trailing, claiming an identity, timing and deriving an identity. | VERIFIED | S1 system_beliefs #5 |
| The business already holds people and their trail in named places. A wallet is a third thing to hold, not a change to either. | Two stores are declared for this domain. | VERIFIED | S1 system_beliefs #1 |

---

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The business believed it announced three moments and announces none. Nothing reported a fault, because nothing checks. | Reference count of zero on all three declared moments. | CRITICAL | VERIFIED | S1 system_beliefs #3 |
| The way a wallet's address is established is the one thing this change needs that the platform has no means for. | Nothing in the closed set of things the platform can do produces an address. | MAJOR | VERIFIED | S1 system_beliefs #5 |
| Wallet creation following acceptance means a second function depends on a moment identity has never actually announced. If that dependency is built before the announcement is real, wallet cannot run at all. | Reference count of zero on the acceptance moment. | MAJOR | VERIFIED | S1 system_beliefs #3 |
| The business's own currency has no name anywhere in the composition, and every wallet is denominated in it. | No vocabulary match. | MINOR | NOT_FOUND | S1 assumptions #3 |

---

## 8. Open Questions for Stage 3

<!-- register:open_questions business_language optional -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
| What is the business's currency called? | business | Every wallet is denominated in it, and the composition does not name it. | S1 assumptions #3 |
| Is establishing an address from supplied key material something the business does itself, or something the platform must be given the means to do? | governance | The platform's set of things it can do is closed, and nothing in it produces an address. | S1 known_facts #18 |