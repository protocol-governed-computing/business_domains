# Stage 3 — Analysis Loop: blockchain / wallet
**Stage:** 3 — Analysis Loop
**CR:** cr_04_wallet
**Status:** DRAFT
**Feeds:** Stage 4 — Business Model

Every gap Stage 2 recorded is resolved here, or carried with a stated reason. Every finding was
re-grounded against the pinned snapshot rather than inherited from Stage 2.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The business's currency is not named anywhere in the composition. The business denominates every wallet in one currency and the name is a business fact, not a discoverable one. It is carried as a business truth and stated once where a wallet is recorded. | Every wallet carries it. Nothing else depends on the name. | OBSERVED | HIGH | CLOSED | Searching the composition's vocabulary for the term returns no match. |
| Q2 | Establishing an address from key material the business is given is pure computation: the same material always yields the same address, and nothing outside the calculation is read or changed. It is therefore a way of working something out, not a way of touching the world, and the platform's set of ways to touch the world does not need to grow. | Decides whether this change is a domain change or a governance change. It is a domain change. | OBSERVED | HIGH | CLOSED | The business supplies the key material rather than the system generating it, so the calculation has no source of variation. The platform's closed set covers holding, trailing, claiming an identity, timing and deriving an identity; producing an address is none of those and needs none of them. |
| Q3 | A moment that nothing refers to cannot be announced from anywhere. Making the three declared moments real is a change to how a decision and a registration are recorded, not a new thing to declare. | Wallet follows acceptance and cannot be built on a moment that never occurs. | OBSERVED | HIGH | CLOSED | All three declared moments report a reference count of zero. |
| Q4 | Grounds are required where a rejection is admitted and read by nothing thereafter. Refusing a groundless rejection is a change to what the recording of a decision checks, not to what the boundary admits. | The identity a wallet depends on keeps its own stated rule. | OBSERVED | HIGH | CLOSED | The contract that records a decision does not mention grounds. |
| Q5 | Nothing in the composition holds a wallet, and nothing declares where one would be held. Both are authored new; neither displaces anything. | The substance of this change. | OBSERVED | HIGH | CLOSED | No vocabulary match for the term anywhere in the composition. |
| Q6 | A wallet is held as a changing record, and its creation is recorded on a trail that is added to and never rewritten. Both already exist in the platform's closed set and are used unchanged. | No new way of touching the world is needed. | OBSERVED | HIGH | CLOSED | Two of the six things the platform can do cover exactly this, and identity already uses both. |

---

## 2. Mandatory Verification Pass

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------|----------|
| Identity is built and reachable: a person registers and is admitted unverified, and an authority then accepts or rejects them. | S2 belief_verification #1 | CONFIRMED | Twenty-three artifacts for the domain, all owned by identity; the two operations and their boundary contracts are present. |
| A person keeps the details they registered with when a decision is recorded about them. | S2 belief_verification #2 | CONFIRMED | Re-exercised against the pinned composition; an accepted person still carries their registered name and preferences. |
| Identity declares that it announces an acceptance, and does not actually announce it. | S2 belief_verification #3 | CONFIRMED | Reference count of zero on each, re-read from the pinned snapshot. |
| A rejection stating no grounds is currently accepted and recorded rather than refused. | S2 belief_verification #4 | CONFIRMED | Re-exercised; the rejection succeeds and the person is rejected with nothing recorded as to why. |
| No wallet exists anywhere in the business today. | S2 belief_verification #5 | CONFIRMED | Vocabulary search returns no match. |
| A wallet design was worked out in an earlier system, including which of a wallet's details are the business's own and which were implementation detail. | S2 belief_verification #6 | CONFIRMED | Still absent. What the business holds to remains a business truth, not a finding. |
| Everything a wallet needs in order to be held, identified, timed and trailed already exists. | S2 architectural_observations #4 | CONFIRMED | Re-read; the five capabilities are present and unchanged. |
| The act that creates a wallet reads records identity owns and declares nothing about them. | S2 belief_verification #7 | CONFIRMED | The reused contract reads `CONTACT_ADDRESS_REGISTRY` and `ACTORS`; the act names only its own binding. |
| The business permits an act to declare the bindings it consults, and refuses a write through one. | S2 belief_verification #8 | CONFIRMED | The constitution states the model, the invariant holds it, and the composition seals both bindings with each record marked. |
| A person nobody accepted is given a wallet today. | S2 belief_verification #9 | CONFIRMED | Dispatching the act for an undecided person returns SUCCESS and records a wallet. |

---

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|-------------|----------|
| Holding a changing record | capability | REUSE | `capability_side_effects::CS_MUTABLE_JSON_V0` — already used by identity to hold people. |
| Holding a trail that is added to and never rewritten | capability | REUSE | `capability_side_effects::CS_APPENDONLY_JSONL_V0` — already used by identity for occurrences. |
| Claiming an identity so two things cannot share one | capability | REUSE | `capability_side_effects::CS_REGISTRY_V0`. |
| Supplying the time a moment occurred | capability | REUSE | `capability_side_effects::CS_CLOCK_V0`. |
| Deriving an identity from what it is given | capability | REUSE | `capability_transforms::CT_PURE_GENERATE_ID_V0` — the same means identity uses. |
| Establishing an address from supplied key material | capability | AUTHOR_NEW | Pure computation; nothing in the composition does it. Owned by the domain, not the platform. |
| Establishing whether a person is one the business holds, and has accepted | capability | REUSE | `blockchain::CC_RESOLVE_ACTOR_V0` resolves a person; the acceptance state is on the record it returns. |
| Recording that a moment occurred | capability | REUSE | `blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0` — nine consumers already depend on it, so it is a settled means. |
| Announcing the three declared moments | capability | EXISTING | The moments are declared and referenced by nothing; announcing them changes where they are referred to, not what they are. |
| Refusing a rejection that states no grounds | capability | EXISTING | Changes what the recording of a decision checks. |
| Somewhere to hold a wallet | storage | AUTHOR_NEW | Nothing declares it. |
| Somewhere to hold a wallet's trail | storage | AUTHOR_NEW | Nothing declares it. |
| The records identity owns | data | EXISTING | `blockchain::RB_IDENTITY_BINDINGS_V0` covers all three, and is the binding the act declares it consults. |
| Refusing a value outside the set the business admits | capability | REUSE | `capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0` raises, so a step that names it fails when the person was not accepted. |

---

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Nothing consumes it. Changing what it checks and what it announces reaches no other artifact. | 0 | `si.topology.impact` reports `impacted_count 0`. |
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Three consumers. The blast radius of adding a grounds check is confined to them. | 3 | `si.topology.impact` reports `impacted_count 3`. |
| blockchain::CC_APPEND_ACTOR_OCCURRENCE_V0 | Nine consumers. Reused unchanged by this CR; nothing about it is altered, which is why the count is recorded rather than acted on. | 9 | `si.topology.impact` reports `impacted_count 9`. |
| blockchain::EV_ACTOR_ACCEPTED_V0 | Nothing refers to it. Referring to it for the first time breaks nothing. | 0 | Reference count of zero. |
| blockchain::EV_ACTOR_REGISTERED_UNVERIFIED_V0 | Nothing refers to it. | 0 | Reference count of zero. |
| blockchain::EV_ACTOR_REJECTED_V0 | Nothing refers to it. | 0 | Reference count of zero. |

---

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Giving an accepted person a wallet | AUTHOR_NEW | Nothing in the composition does any part of it. | Nothing to reuse; the vocabulary search returned no match. | S2 gaps #1 |
| Holding a wallet | REUSE | A wallet is a record that changes. The platform already holds records that change, and identity uses the same means for people. | Holding it as a trail was rejected: a balance is current state, not a history. `capability_side_effects::CS_MUTABLE_JSON_V0` | S2 pps_baseline_fqdns #8 |
| Recording that a wallet was created | REUSE | The moment goes on a trail added to and never rewritten, exactly as identity's moments do. | `capability_side_effects::CS_APPENDONLY_JSONL_V0` | S2 pps_baseline_fqdns #9 |
| Determining a wallet's identity | REUSE | The business already derives an identity from what it is given, and one person holds one wallet, so the person is what it is derived from. | `capability_transforms::CT_PURE_GENERATE_ID_V0`; deriving from person and classification was rejected because one person holds one wallet. | S1 known_facts #17 |
| Ensuring two wallets never share an identity | REUSE | Claiming a key is exactly this, and refusing the claim is how a second wallet is refused. | `capability_side_effects::CS_REGISTRY_V0` | S1 business_invariants #3 |
| Establishing the address others may pay to | AUTHOR_NEW | Pure computation over key material the business supplies: the same material always yields the same address, nothing outside is read, nothing is changed. It is therefore a way of working something out, which the domain may author, and not a way of touching the world, which is closed. | Adding it to the platform's closed set was examined and rejected — it is not neutral, and it is not needed, because the calculation is pure. Generating the key material rather than being given it was rejected at the seed: it would make the same request produce a different wallet each time. | S1 known_facts #18 |
| Establishing that a person is held and accepted | REUSE | Identity already resolves a person and the acceptance state travels on the record returned. | `blockchain::CC_RESOLVE_ACTOR_V0` | S2 pps_baseline_fqdns #1 |
| Announcing the moment a person is registered, accepted or rejected | EXTEND | The moments are declared already. What is missing is anywhere referring to them, which is a change to how the two identity operations record what they did. | Declaring new moments was rejected: three already exist and a second set would split one meaning in two. | S2 gaps #2 |
| Refusing a rejection that states no grounds | EXTEND | The rule is the business's own and already stated. What changes is that the recording of a decision now checks it. | Requiring it only where the request is admitted was rejected: that is already so, and it is why the gap went unnoticed. | S2 gaps #3 |
| Supplying the time a moment occurred | REUSE | The platform supplies the time and identity already uses it. | `capability_side_effects::CS_CLOCK_V0` | S1 known_facts #19 |
| Declaring that the wallet act reads the records identity owns | EXTEND | The act exists and reads them already; what it lacks is the statement. | Keeping a copy of who exists inside the wallet's records was rejected by the business: a second copy of one truth can disagree with the thing it describes. | S2 gaps #7 |
| Refusing a wallet to a person the business has not accepted | AUTHOR_NEW | Nothing turns the state the act reads into a decision, so the refusal the business declared has no branch to route to. | Reading the state inside an existing step was rejected: a step that succeeds whatever it finds leaves the refusal unreachable, and the transform that refuses must be able to raise. | S2 gaps #8 |

---

## 6. Subdomain Placement Decision

<!-- register:placement_decision business_language=subdomain -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| NEW_SUBDOMAIN | wallet | A wallet is a thing the business holds in its own right, with its own identity, its own record and its own trail. It is owned by wallet and written only by wallet. Placing it inside identity would make identity the owner of value as well as of who a person is, and would leave the store of people written by a function that is not about people. | S1 authority_boundaries #1 |
| EXTEND | identity | The announcements and the grounds check are identity's own, on identity's own artifacts, written by identity. Wallet does not write them and does not own them; it depends on the first of them. | S1 authority_boundaries #4 |

---

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | All five critical gaps from Stage 2 are resolved: two by authoring new, two by extending identity, one by reusing what exists. |
| No open analyst questions | SATISFIED | Both questions carried from Stage 2 are closed — the currency is a business truth, and the address is pure computation the domain may author. |
| No dependency expansion in the last pass | SATISFIED | The twelve dependencies were established in one pass and re-verification surfaced none beyond them. |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | Seven items re-grounded against the pinned snapshot; all seven CONFIRMED, none overturned. |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried with a reason | SATISFIED | All six findings are OBSERVED. None rests on inference. |