# Stage 3 — Analysis Loop: blockchain / identity

**Stage:** 3 — Analysis Loop

**CR:** cr_05_identity

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. The question throughout is one: where each of identity's rules is held, and what
identity does with what it finds. Two further places where the request decides what identity
records were found by running the acts directly, and are resolved here under the change request's
own invariant that a business rule of identity's is held by identity.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | Every rule identity applies is handed to it by the request, and the public entrance is the only thing supplying the business's values. There are five: what a registration must contain, which states admit a decision, which decisions may be recorded, that an authority does not decide about themselves, and that a rejection states its grounds. | Moving each into identity closes the gap whichever way identity is reached, and removes those values from the entrances, which no longer need to supply them. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 and #2; the author answered that identity holds all five (S2 discovery_concerns #1) |
| Q2 | The registration check reports and nothing acts on the report. The structure check publishes its violations; the contract's single step succeeds whatever it found. A rule step requiring the violations to be empty, following the check, turns the report into a refusal, and a composition in another domain already does exactly this. | The registration contract gains one step. The platform check stays a reporter, as ruled for v5. | OBSERVED | HIGH | CLOSED | blockchain::CC_VALIDATE_REGISTRATION_V0 has one step; causal_language_model::CC_CLAIM_MODEL_IDENTITY_V0 follows the same check with capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 requiring `violations` to equal an empty list |
| Q3 | Four of the five rules are fixed values and can be written where they are used: the registration schema, the admitted states, the admitted outcomes and the grounds rules. Written in the contracts that apply them, they hold for every act composing those contracts, and no act or request can widen them. Wallet wrote its rule in the act rather than the contract; here the deciding contract is shared by the acceptance and rejection acts, and the rules are the same for both, so the contract is the one place that holds them for both. | Three contracts change what they take and what they hold. The acts stop binding the rules from the request. | OBSERVED | HIGH | CLOSED | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 is composed by blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 with the same sets; blockchain::WF_CREATE_WALLET_V0 hands its contract a literal set |
| Q4 | The fifth rule — an authority does not decide about themselves — compares two values of the request, and the rule checker compares a field only against a fixed value. Comparing the authority with the person, then requiring that they are not equal, holds the rule with nothing taken from the request, using two platform transforms the composition already publishes. | The deciding contract replaces its request-supplied self-check with a comparison and a fixed rule on its result. | OBSERVED | HIGH | CLOSED | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0 supports not_null, eq, neq, in and numeric comparisons against a rule's value, and no comparison between fields; capability_transforms::CT_PURE_COMPARE_EQUAL_V0 returns whether two values are equal |
| Q5 | The state a decision records is taken from the request, not from the decision the contract checked. Run directly against the pinned composition, a request whose decision is ACCEPTED, and so admitted, records the state SUSPENDED. And the decision itself is the request's: the acceptance act records whatever decision it is handed, so a rejection can be recorded through it without the grounds the rejection act requires. Holding which decisions may be recorded therefore needs the record to be built from the checked decision, and each act to fix the decision it records. | The deciding contract builds the decided record from its own inputs — the decision, the authority and the grounds — and each act hands it its own decision as a fixed value. | OBSERVED | HIGH | CLOSED | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 assembles the record from `decided_actor_fields`, a request field whose `state` is independent of `decision`; run directly, ACCEPTED was checked and SUSPENDED recorded |
| Q6 | Registration records whatever state the request hands it. Run directly against the pinned composition, a registration carrying the state ACCEPTED is registered accepted, with no decision and no authority, and the wallet function would then give that person a wallet. The business's lifecycle has one way in, a complete registration, and it leads to unverified. | The registration act writes the state unverified as its own fixed value, whatever the request carries. | OBSERVED | HIGH | CLOSED | blockchain::WF_REGISTER_ACTOR_V0 writes `actor_record` from the payload, whose `state` blockchain::TI_REGISTER_ACTOR_V0 sets to UNVERIFIED as a constant; run directly with ACCEPTED, the person was held accepted |
| Q7 | Nothing a caller sees through the public entrance changes. Every value the entrances supply today is the business's rule and becomes identity's own, so every request admitted there reaches the same outcome, and what the caller is told is projected from result surfaces that do not change. The entrances only stop supplying what identity now holds. | The entrances are amended to drop their rule constants. No input a caller sends, and no answer a caller receives, changes. | OBSERVED | HIGH | CLOSED | S2 belief_verification #1 and #5; the TE declarations are untouched |
| Q8 | The acceptance and rejection gates declare none of the rule fields. The registration gate requires the schema, so once the entrance stops supplying it, every registration through the entrance would be refused at admission. The acceptance gate does not declare the grounds an acceptance may carry, although the entrance accepts them and the act will read them. | The registration intent stops requiring the schema identity now holds. The acceptance intent declares grounds as optional, so the gate states what the act reads. | OBSERVED | HIGH | CLOSED | blockchain::IN_ACTOR_REGISTERED_V0 requires actor_record and registration_schema; blockchain::IN_ACTOR_ACCEPTANCE_V0 declares contact_address and verifying_authority; blockchain::TI_ACCEPT_ACTOR_V0 accepts grounds as optional |
| Q9 | The moment each act records, and the stream it records to, also come from the request. A direct caller can record a moment that names a different occurrence from the one that happened. The trail is outside what this change asks, and no rule of the business's names it. | Recorded and carried; not changed here. | OBSERVED | HIGH | CLOSED | blockchain::WF_ACCEPT_ACTOR_V0, blockchain::WF_REJECT_ACTOR_V0 and blockchain::WF_REGISTER_ACTOR_V0 bind occurrence_fields and stream_id from the payload |
| Q10 | Records made under a request's own rules stay as they were made. The business adds to its record and does not rewrite it, so a person registered or decided about under a widened rule keeps that record. | No repair, no backfill. | OBSERVED | HIGH | CLOSED | S1 constraints #2; S1 out_of_scope #4 |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The public entrance supplies the business's rules to identity with each request: what a registration must contain, who may be decided about, and which decisions may be recorded. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1 and Q7 |
| Identity takes each of those rules from the request rather than holding them itself. | S2 belief_verification #2 | CONFIRMED | Resolved in Q1, Q3 and Q4 |
| A request that states a wider rule is judged by it: a second decision about an accepted person, or a decision the business never allowed, is recorded. | S2 belief_verification #3 | CONFIRMED | Resolved in Q3 and Q5; Q5 adds that the recorded state need not be the checked decision |
| Identity checks a registration against what it must contain, finds what is missing, and registers the person anyway. | S2 belief_verification #4 | CONFIRMED | Resolved in Q2 |
| Through the public entrance an incomplete registration is refused before identity checks it. | S2 belief_verification #5 | CONFIRMED | Resolved in Q7 |
| The wallet function holds its own rule about who may have a wallet, rather than taking it from the request. | S2 belief_verification #6 | CONFIRMED | Resolved in Q3 |
| Identity holds none of its own rules; each comes with the request it judges. | S2 gaps #1 | CONFIRMED | Resolved in Q1 through Q6 |
| A registration identity finds incomplete is registered anyway. | S2 gaps #2 | CONFIRMED | Resolved in Q2 |
| Two more of identity's rules travel with the request than the change request names. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q1 and Q4, per the author's answer |
| The two rule sets a decision is checked against are also used to compose the record it writes and the moment it records. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q5 for the record, and carried in Q9 for the moment |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Checking a record's structure | Platform transform | REUSE | capability_transforms::CT_PURE_VALIDATE_RECORD_STRUCTURE_V0, unchanged |
| Refusing on a list of rules | Platform transform | REUSE | capability_transforms::CT_PURE_VALIDATE_PARAMETER_RULES_V0, unchanged |
| Refusing a value outside a set | Platform transform | REUSE | capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0, unchanged |
| Comparing two values | Platform transform | REUSE | capability_transforms::CT_PURE_COMPARE_EQUAL_V0, unchanged |
| Assembling a record from fields | Platform transform | REUSE | capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0, unchanged |
| Checking a registration | Capability contract | EXTEND | blockchain::CC_VALIDATE_REGISTRATION_V0 holds its schema and refuses on violations |
| Recording a decision | Capability contract | EXTEND | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 holds its sets and self-decision rule, and builds its record from the decision |
| Requiring rejection grounds | Capability contract | EXTEND | blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 holds its rules |
| The three acts | Workflows | EXTEND | blockchain::WF_REGISTER_ACTOR_V0, blockchain::WF_ACCEPT_ACTOR_V0 and blockchain::WF_REJECT_ACTOR_V0 stop binding rules from the request, and fix the state or decision each records |
| The three entrances | Transport ingress | EXTEND | blockchain::TI_REGISTER_ACTOR_V0, blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0 stop supplying what identity holds |
| The acceptance gate | Intent | EXTEND | blockchain::IN_ACTOR_ACCEPTANCE_V0 declares optional grounds |
| The registration gate | Intent | EXTEND | blockchain::IN_ACTOR_REGISTERED_V0 stops requiring the schema |
| Resolving the person, claiming the address, writing the record, appending the moment | Capability contracts | REUSE | blockchain::CC_RESOLVE_ACTOR_V0, blockchain::CC_CLAIM_CONTACT_ADDRESS_V0, blockchain::CC_REGISTER_ACTOR_V0 and blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0, unchanged |
| The moment each act records | Workflow bindings | INVESTIGATE | Carried in Q9; outside this change |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| blockchain::CC_VALIDATE_REGISTRATION_V0 | Amended — holds its schema, gains a refusal step | 2 | si.topology.impact impacted_count 2 |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Amended — holds its sets and self-decision rule, builds its record from the decision | 10 | si.topology.impact impacted_count 10 |
| blockchain::CC_REQUIRE_REJECTION_GROUNDS_V0 | Amended — holds its rules | 2 | si.topology.impact impacted_count 2 |
| blockchain::WF_REGISTER_ACTOR_V0 | Amended — stops binding the schema, writes the state unverified | 0 | si.topology.impact impacted_count 0 |
| blockchain::WF_ACCEPT_ACTOR_V0 | Amended — stops binding the rules, fixes its decision | 0 | si.topology.impact impacted_count 0 |
| blockchain::WF_REJECT_ACTOR_V0 | Amended — stops binding the rules, fixes its decision | 0 | si.topology.impact impacted_count 0 |
| blockchain::TI_REGISTER_ACTOR_V0 | Amended — drops the schema and the state it supplied | 0 | si.topology.impact impacted_count 0 |
| blockchain::TI_ACCEPT_ACTOR_V0 | Amended — drops the rules and the decided record it supplied | 0 | si.topology.impact impacted_count 0 |
| blockchain::TI_REJECT_ACTOR_V0 | Amended — drops the rules and the decided record it supplied | 0 | si.topology.impact impacted_count 0 |
| blockchain::IN_ACTOR_ACCEPTANCE_V0 | Amended — declares optional grounds | 1 | si.topology.impact impacted_count 1 |
| blockchain::IN_ACTOR_REGISTERED_V0 | Amended — stops requiring the schema | 1 | si.topology.impact impacted_count 1 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Check a registration and refuse an incomplete one | EXTEND | The check already finds what is missing. It holds what a registration must contain, and a rule following it refuses when anything is found, as another part of the business already does. | Making the platform check refuse was checked and rejected by ruling: a check that decides can no longer be used only to report. Refusing at the entrance alone was checked and rejected: that is today's arrangement, and it holds nothing against any other way in. | S3 analysis_findings Q2 |
| Record a decision only about an unverified person, and only an acceptance or a rejection | EXTEND | The deciding step holds which states admit a decision and which decisions may be recorded, and builds the record from the decision it checked. | Holding the sets in each act, as wallet did, was checked and rejected: both acts share one deciding step with the same sets, and holding them there covers every act that composes it. Checking the request's record against the decision was checked and rejected: it keeps the record the request's to state. | S3 analysis_findings Q3 |
| Refuse an authority deciding about themselves | EXTEND | The deciding step compares the authority with the person and refuses when they are the same, taking nothing from the request but the two values. | A new rule operation comparing two fields was checked and rejected: the comparison the platform already offers, followed by a fixed rule, says the same thing without changing the platform. | S3 analysis_findings Q4 |
| Refuse a rejection stating no grounds | EXTEND | The grounds step holds its own rules: grounds are present and not empty. | Nothing else was needed; the step existed and took its rules from the request. | S3 analysis_findings Q3 |
| Fix the decision each act records | EXTEND | The acceptance act records an acceptance and the rejection act a rejection, each as its own fixed value. | Leaving the decision to the request was checked and rejected: a rejection could then be recorded through the acceptance act without grounds. | S3 analysis_findings Q5 |
| Register a person unverified | EXTEND | The registration act records the state unverified as its own fixed value. | Checking the requested state was checked and rejected: there is only one state a registration may lead to, so there is nothing to check, only something to write. | S3 analysis_findings Q6 |
| Reach identity from outside | EXTEND | The entrances stop supplying what identity now holds. A caller sends and is told exactly what they are today. | Leaving the constants in place was checked and rejected: they would be values nothing reads, and a reader would take them for the rule. | S3 analysis_findings Q7 |
| Admit an acceptance with its grounds | EXTEND | The acceptance gate declares the optional grounds the entrance already accepts and the act now reads. | Nothing else was needed. | S3 analysis_findings Q8 |
| Admit a registration without the schema identity holds | EXTEND | The registration gate stops requiring the schema, which identity now holds and the entrance no longer supplies. | Leaving the gate as it is was checked and rejected: every registration through the entrance would be refused at admission. | S3 analysis_findings Q8 |
| Record the moment of each act | REUSE | Unchanged. The moment and its stream remain the request's to name; recorded as a finding and outside this change. | Holding the moment in each act was checked and deferred: no rule of the business names it, and the change request does not ask. | S3 analysis_findings Q9 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | identity | Every rule held here is identity's own, and every step that changes belongs to identity. Nothing moves and no other subdomain changes. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap resolves to committed decisions: each of the five rules is held by the step that applies it, and the record and the decision each act writes are its own |
| No open analyst questions | SATISFIED | All ten findings are CLOSED. The one question Stage 2 raised was answered by the business author |
| No dependency expansion in the last pass | SATISFIED | A second pass, running the acts directly, added the recorded state and the registered state; a third pass over what each act writes found only the recorded moment, carried as outside this change |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All ten items re-grounded and CONFIRMED |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Every finding is OBSERVED; four were established by running the acts against the pinned composition |
