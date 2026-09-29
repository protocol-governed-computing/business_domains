# Stage 2 — Domain Model Verification: blockchain / identity

**Stage:** 2 — Domain Model Verification
**CR:** cr_05_identity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. The function
exists, runs and is reached from outside. What is verified here is where each of identity's rules is
read from, and what identity does with what its registration check finds. Each belief about behaviour
was established by running identity's acts directly against the pinned composition, on a scratch
data root, bypassing the public entrance.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Record | What the business holds about a person: what they registered with, their state, and the decision made about them. | One keyed store, one record per contact address, unchanged by this change. | OBSERVED | S1 system_beliefs #3 |
| The Registration | What a person supplies to become known: their name and the address they are reached at. | Held in the person's record when they are registered. | OBSERVED | S1 known_facts #1 |
| The Decision | What an authority records about an unverified person: acceptance or rejection, the authority, and the grounds. | Written into the person's record; the rest of the record is left as it was. | OBSERVED | S1 known_facts #3 |
| The Business's Rules | What a registration must contain, which people may be decided about, which decisions may be recorded, that a rejection states grounds, and that an authority does not decide about themselves. | Held nowhere in identity today. Each travels with the request that is judged by it. | OBSERVED | S2 belief_verification #2 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| The Registration | Name | What the person is called. Required. | OBSERVED | S1 known_facts #1 |
| The Registration | Contact Address | The address the person is reached at. Required. | OBSERVED | S1 known_facts #1 |
| The Decision | State | Unverified, accepted or rejected. | OBSERVED | S1 lifecycle_states #1 |
| The Decision | Verifying Authority | The authority the decision names. | OBSERVED | S1 known_facts #5 |
| The Decision | Grounds | The reason stated. Required on a rejection. | OBSERVED | S1 known_facts #4 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Register a person | The person | A complete registration is recorded unverified; an incomplete one is refused. | OBSERVED | S1 requested_outcomes #1 |
| Accept a person | An authority within the business | An unverified person is recorded accepted; anyone else is refused. | OBSERVED | S1 requested_outcomes #2 |
| Reject a person | An authority within the business | An unverified person is recorded rejected, with grounds; anyone else, or a rejection without grounds, is refused. | OBSERVED | S1 requested_outcomes #2 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Register a person | 1 | Check the registration against what it must contain. | None. | OBSERVED | S2 belief_verification #4 |
| Register a person | 2 | Claim the contact address, refusing one already held. | None. | OBSERVED | S2 pps_baseline_fqdns #2 |
| Register a person | 3 | Record the person unverified, and record that they registered. | The person's record, and a moment on the trail. | OBSERVED | S1 lifecycle_transitions #1 |
| Accept or reject a person | 1 | Resolve the person the address names, refusing if none is found. | None. | OBSERVED | S2 pps_baseline_fqdns #4 |
| Accept or reject a person | 2 | Refuse unless the person's state admits a decision, the decision is one the business allows, and the authority is not the person. | None. | OBSERVED | S2 belief_verification #3 |
| Accept or reject a person | 3 | Record the decision, and record that it occurred. | The person's record, changed in its decided parts only, and a moment on the trail. | OBSERVED | S1 lifecycle_transitions #2 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The public entrance supplies the business's rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded. | VERIFIED | blockchain::TI_REGISTER_ACTOR_V0 maps each request onto a payload carrying `registration_schema` — name and contact address, both required. blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 carry `states_admitting_a_decision` as UNVERIFIED and `admitted_outcomes` as ACCEPTED and REJECTED. All are constants of the boundary declaration, not values the caller sends. The two decision boundaries also carry `self_check_rules`, and the rejection boundary `grounds_rules`, in the same way. | S1 system_beliefs #1 |
| Identity takes each of those rules from the request rather than holding them itself. | VERIFIED | blockchain::WF_REGISTER_ACTOR_V0 binds `registration_schema` from the payload into blockchain::CC_VALIDATE_REGISTRATION_V0. blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 bind `states_admitting_a_decision`, `admitted_outcomes` and `self_check_rules` from the payload into blockchain::CC_RECORD_VERIFICATION_DECISION_V0, and the rejection workflow binds `grounds_rules` from the payload into blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0. None of these is declared by the intents that admit the requests — blockchain::IN_ACTOR_ACCEPTANCE_V0 and blockchain::IN_ACTOR_REJECTION_V0 declare only the contact address, the authority and the grounds — so the gate neither requires nor restricts them. | S1 system_beliefs #2 |
| A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded. | VERIFIED | Run directly against the pinned composition: a person accepted under the business's rules and accepted again under the same rules is refused, and accepted again with `states_admitting_a_decision` widened to include ACCEPTED succeeds. A decision of SUSPENDED is refused under the business's outcomes and recorded when the request widens `admitted_outcomes` to include it; the person's state is SUSPENDED afterwards, a state the business does not have. A request that sends no `self_check_rules` records an authority accepting themselves. | S1 system_beliefs #3 |
| Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway. | VERIFIED | blockchain::CC_VALIDATE_REGISTRATION_V0 has one step, which runs capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 and publishes the violations it finds. That transform reports and never refuses, and nothing in the contract or the workflow reads the violations, so the step always succeeds. Run directly: a registration with no name, checked against a schema requiring one, is registered, and the person is held unverified with no name. | S1 system_beliefs #4 |
| Through the public entrance an incomplete registration is refused before identity checks it. | VERIFIED | blockchain::TI_REGISTER_ACTOR_V0 declares `name` and `contact_address` as required inputs, and the transport resolver refuses a request missing a required input with INPUT_MISSING before any workflow is dispatched. The fault in identity's registration check cannot be reached from outside. | S1 system_beliefs #5 |
| The wallet function holds its own rule about who may have a wallet, rather than taking it from the request. | VERIFIED | blockchain::WF_CREATE_WALLET_V0 hands blockchain::CC_REQUIRE_ACCEPTED_HOLDER_V0 `states_admitting_a_wallet` as the literal set ACCEPTED, written in the workflow, and the holder's state from the resolved record. Nothing in the request can widen it. | S1 system_beliefs #6 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Checking a registration | blockchain::CC_VALIDATE_REGISTRATION_V0 | Checks a registration against a schema and publishes the violations. | PARTIAL | It refuses nothing, and it takes the schema from the request. |
| Claiming a contact address | blockchain::CC_CLAIM_CONTACT_ADDRESS_V0 | Claims the address a registration names, reporting one already held. | EXACT | Nothing for this purpose; unchanged by this change. |
| Recording a decision | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Refuses a state that admits no decision, an outcome not admitted and an authority deciding about themselves, then records the decided parts of the record. | PARTIAL | Every refusal it makes is against a set or a rule handed to it; it holds none of them. |
| Requiring grounds for a rejection | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Refuses a rejection whose grounds fail the rules handed to it. | PARTIAL | It holds no rule of its own; the rules come from the request. |
| Resolving a person | blockchain::CC_RESOLVE_ACTOR_V0 | Resolves a contact address to the person's record. | EXACT | Nothing for this purpose. |
| Registration act | blockchain::WF_REGISTER_ACTOR_V0 | Checks, claims, records and announces a registration. | PARTIAL | It binds the registration schema from the request, and continues past a check that found violations. |
| Acceptance act | blockchain::WF_ACCEPT_ACTOR_V0 | Resolves the person, records the acceptance and announces it. | PARTIAL | It binds the admitted states, the admitted outcomes and the self-decision rule from the request. |
| Rejection act | blockchain::WF_REJECT_ACTOR_V0 | Requires grounds, resolves the person, records the rejection and announces it. | PARTIAL | It binds the grounds rules, the admitted states, the admitted outcomes and the self-decision rule from the request. |
| Public registration entrance | blockchain::TI_REGISTER_ACTOR_V0 | Admits a registration request and supplies the schema and the rest of the act's constants. | EXACT | Nothing for this purpose. It stops supplying rules identity will hold itself. |
| Public acceptance entrance | blockchain::TI_ACCEPT_ACTOR_V0 | Admits an acceptance request and supplies the admitted states, outcomes and self-decision rule. | EXACT | Nothing for this purpose. It stops supplying rules identity will hold itself. |
| Public rejection entrance | blockchain::TI_REJECT_ACTOR_V0 | Admits a rejection request and supplies the admitted states, outcomes, self-decision rule and grounds rules. | EXACT | Nothing for this purpose. It stops supplying rules identity will hold itself. |
| Membership check | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0 | Refuses a value that is not in a given set. | EXACT | Nothing; the set it is given is what this change fixes. |
| Rule check | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 | Refuses parameters that fail a given list of rules. | EXACT | Nothing; it can refuse on a check's violations, as another domain already does. |
| Structure check | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0 | Reports every way a record fails a schema. | PARTIAL | It reports and never refuses. Refusing on what it reports is the calling contract's business (ruled for v5). |
| Holding a rule in the act | blockchain::WF_CREATE_WALLET_V0 | Hands its refusal the admitted states as a literal written in the workflow. | EXACT | Nothing; it is the precedent this change follows. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Identity holds none of its own rules; each comes with the request it judges. | CRITICAL | Anything reaching identity other than through the public entrance can record a second decision, a decision the business never allowed, or an authority deciding about themselves. | OBSERVED | S2 belief_verification #3 |
| A registration identity finds incomplete is registered anyway. | MAJOR | A person can be held with no name. Unreachable through the public entrance, reachable any other way. | OBSERVED | S2 belief_verification #4 |
| Nothing records which of identity's rules are the business's own. | MINOR | The rules are stated in the business's documents and in the public entrance's constants, and nowhere identity itself reads. | OBSERVED | S2 belief_verification #2 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The public entrance holds the rules correctly, so nothing seen from outside is wrong, and nothing seen from outside can show the fault. | Every constant the entrances supply is the business's rule, and the entrance refuses an incomplete registration before identity is reached. The fault is in what identity accepts from anything else. | OBSERVED | S2 belief_verification #5 |
| Wallet closed the same hole by writing the rule into the act. | The wallet act's refusal is handed a literal set; the request carries no rule at all. | OBSERVED | S2 belief_verification #6 |
| A check that reports is made to refuse by a rule that follows it. | Another domain's registration check follows the structure check with a rule step requiring the violations to be empty, and refuses otherwise. The same composition applies here without any new capability. | OBSERVED | S2 pps_baseline_fqdns #13 |
| The admission gates are silent on the rules, so moving them into the acts changes no gate. | Neither decision intent declares a rule field; the rules pass through the gate undeclared. Holding them in the acts removes fields nothing admits against. | OBSERVED | S2 belief_verification #2 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| Two more of identity's rules travel with the request than the change request names. | The rule that an authority does not decide about themselves, and the rule that a rejection states its grounds, are each handed to identity by the request, and the first was shown widened by a request that sends none. The change request names what a registration must contain, who may be decided about and which decisions may be recorded; its invariants state that every business rule of identity's is held by identity, which covers these two as well. Put to the business author, who answered that identity holds all five. | MAJOR | OBSERVED | S2 belief_verification #2 |
| The two rule sets a decision is checked against are also used to compose the record it writes and the moment it records. | The decided record and the occurrence are assembled from request fields as well, and the recorded state is taken from them rather than from the decision. Whether the record could disagree with the decision is not what this change asks, and it is not examined here. | MINOR | OBSERVED | S2 belief_verification #3 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
