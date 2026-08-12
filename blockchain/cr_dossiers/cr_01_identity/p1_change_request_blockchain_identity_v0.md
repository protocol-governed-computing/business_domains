# Stage 1 — Change Request: Clarification & Fact Capture: blockchain / identity
**Stage:** 1 — Change Request (Clarification & Fact Capture)
**CR:** cr_01_identity
**Status:** DRAFT
**Feeds:** Stage 2 — Domain Model Discovery

Projected from the change seed. Every row is the seed's own, cited to the section it was
said in. S1 interrogates and does not author: a question raised by restating the seed
amends the seed and is projected again, so no row here states business content the seed
does not.

---

## 1. CR Type

<!-- register:cr_type business_language -->
| Subdomain | Classification (NEW_SUBDOMAIN, EXTEND_SUBDOMAIN, MODIFY, DEPRECATE) | Rationale | Source Finding |
|-----------|-------------------------------------------------------------------|---------|--------------|
| identity | NEW_SUBDOMAIN | The change establishes the identity function of the blockchain project. Nothing in this domain exists yet, so the change introduces a function rather than extending one. Identity is the first of the project's functions because every other one names an actor. | CR seed §1 CR Type #1 |

---

## 2. Business Vocabulary

<!-- register:business_vocabulary business_language -->
| Term | Definition | Source Finding |
|----|----------|--------------|
| blockchain | The project being established, across seven functions of which identity is the first. | CR seed §2 Business Vocabulary #1 |
| Identity | The function governing who an actor is and whether the business trusts them. | CR seed §2 Business Vocabulary #2 |
| Actor | A person known to the system, whether or not the business has accepted them. | CR seed §2 Business Vocabulary #3 |
| Registration | The act by which a person supplies their own details and is admitted to the system unverified. | CR seed §2 Business Vocabulary #4 |
| Unverified | The state of an actor the business has recorded and not yet accepted. Trusted with nothing. | CR seed §2 Business Vocabulary #5 |
| Verification Decision | The act by which an authority accepts or rejects a registered actor. | CR seed §2 Business Vocabulary #6 |
| Accepted | The outcome of a verification decision in which the authority trusts the actor. | CR seed §2 Business Vocabulary #7 |
| Rejected | The outcome of a verification decision in which the authority does not trust the actor. Trusted with nothing. | CR seed §2 Business Vocabulary #8 |
| Authority | A party within the business empowered to make a verification decision about an actor, identified outside the identity function and never registered through it. | CR seed §2 Business Vocabulary #9 |
| Contact Address | The address a person registers with, which is what identifies them as an actor. | CR seed §2 Business Vocabulary #10 |
| Grounds | The reason an authority states for a verification decision. | CR seed §2 Business Vocabulary #11 |
| Occurrence | A recorded moment in an actor's history, written when it happens and never rewritten. | CR seed §2 Business Vocabulary #12 |
| Preference | A convenience recorded at registration — preferred currency or preferred language — bearing on neither identity nor the verification decision. Absent, it is recorded as the default. | CR seed §2 Business Vocabulary #13 |
| Default Preference | BACHI for currency and English for language; what an actor is recorded as preferring when it states nothing. | CR seed §2 Business Vocabulary #14 |

---

## 3. Requested Outcomes

<!-- register:requested_outcomes business_language -->
| Outcome | Source Finding |
|-------|--------------|
| A person can register themselves, supplying their own identifying details, and is admitted in an unverified state. | CR seed §3 Requested Outcomes #1 |
| An authority can record a verification decision against a registered person, accepting or rejecting them. | CR seed §3 Requested Outcomes #2 |
| The business can show, for any actor, who registered and when, every time they registered, whether a decision was made, by which authority, what it was, when, and the grounds stated for it. | CR seed §3 Requested Outcomes #3 |
| An unverified or rejected actor is trusted with nothing and can be read as trusted with nothing. | CR seed §3 Requested Outcomes #4 |

---

## 4. Known Facts — Business Truths

<!-- register:known_facts business_language -->
| Fact | Certainty (HIGH, MEDIUM, LOW) | Source Finding |
|----|-----------------------------|--------------|
| An unverified actor is a claim the business has recorded and not yet accepted. | HIGH | CR seed §4 Known Facts — Business Truths #1 |
| An unverified actor may hold no wallet and submit no transaction. | HIGH | CR seed §4 Known Facts — Business Truths #2 |
| An unverified actor is not a lesser actor but a different thing; the business would rather say it has not decided than imply a decision it has not made. | HIGH | CR seed §4 Known Facts — Business Truths #3 |
| A person registers themselves; the details are their own claim about who they are. | HIGH | CR seed §4 Known Facts — Business Truths #4 |
| Registration may be refused only for details the business cannot read, such as a missing name or a missing contact address. | HIGH | CR seed §4 Known Facts — Business Truths #5 |
| A detail is unreadable when it is absent or is not of the form the business asked for; everything else is a matter of belief. | HIGH | CR seed §4 Known Facts — Business Truths #6 |
| Whether a person controls the address they registered with, and whether the name is theirs, are matters of belief and never of registration. | HIGH | CR seed §4 Known Facts — Business Truths #7 |
| An actor is identified by the contact address they register with. | HIGH | CR seed §4 Known Facts — Business Truths #8 |
| Two registrations carrying the same contact address are the same person. | HIGH | CR seed §4 Known Facts — Business Truths #9 |
| A repeated registration does not create a second actor and does not fail. | HIGH | CR seed §4 Known Facts — Business Truths #10 |
| A repeated registration is recorded as a distinct occurrence against the same actor. | HIGH | CR seed §4 Known Facts — Business Truths #11 |
| A repeated registration does not reset a decision already made. | HIGH | CR seed §4 Known Facts — Business Truths #12 |
| A second registration may carry details differing from the first, and the details the actor was admitted with prevail. | HIGH | CR seed §4 Known Facts — Business Truths #13 |
| The differing details of a second registration are recorded as part of the occurrence and change the actor in no respect. | HIGH | CR seed §4 Known Facts — Business Truths #14 |
| A verification decision is made by an authority within the business, acting as a distinct kind of actor from the person decided about. | HIGH | CR seed §4 Known Facts — Business Truths #15 |
| A person may never verify themselves. | HIGH | CR seed §4 Known Facts — Business Truths #16 |
| An authority is identified outside the identity function and is not an actor this function holds or resolves. | HIGH | CR seed §4 Known Facts — Business Truths #17 |
| A verification decision is either acceptance or rejection; there is no third outcome and no deferral. | HIGH | CR seed §4 Known Facts — Business Truths #18 |
| An authority that is not ready to decide has not decided, and the actor stays unverified. | HIGH | CR seed §4 Known Facts — Business Truths #19 |
| A verification decision may only be made against a registration that exists. | HIGH | CR seed §4 Known Facts — Business Truths #20 |
| A rejection is its own occurrence, distinct in kind from an acceptance. | HIGH | CR seed §4 Known Facts — Business Truths #21 |
| A rejected actor is trusted with nothing and is recorded among the actors the business has accepted in no sense whatever. | HIGH | CR seed §4 Known Facts — Business Truths #22 |
| An actor is decided about once. | HIGH | CR seed §4 Known Facts — Business Truths #23 |
| Grounds are required for a rejection and optional for an acceptance. | HIGH | CR seed §4 Known Facts — Business Truths #24 |
| The deciding authority is recorded on every decision, acceptance and rejection alike. | HIGH | CR seed §4 Known Facts — Business Truths #25 |
| Every recorded occurrence carries the time it actually happened, determined at the moment it occurs. | HIGH | CR seed §4 Known Facts — Business Truths #26 |
| A record whose times do not advance is regarded by the business as no record at all. | HIGH | CR seed §4 Known Facts — Business Truths #27 |
| The record is added to and never rewritten; a correction is a further occurrence, not an edit. | HIGH | CR seed §4 Known Facts — Business Truths #28 |
| Two preferences are collected at registration — preferred currency and preferred language — each having a default. | HIGH | CR seed §4 Known Facts — Business Truths #29 |
| The default preferred currency is BACHI and the default preferred language is English. | HIGH | CR seed §4 Known Facts — Business Truths #30 |
| A person who states no preference is recorded as preferring the defaults, rather than as having stated nothing. | HIGH | CR seed §4 Known Facts — Business Truths #31 |
| Preferences bear on neither identity nor the verification decision. | HIGH | CR seed §4 Known Facts — Business Truths #32 |
| Two registrations differing only in preference are the same person. | HIGH | CR seed §4 Known Facts — Business Truths #33 |

---

## 5. Existing-System Beliefs — Requiring Verification

<!-- register:system_beliefs business_language -->
| Belief | Why It Matters | Verification Goal | Source Finding |
|------|--------------|-----------------|--------------|
| The business author believes nothing in the blockchain domain exists yet, so identity is established rather than extended. | If any blockchain function is already governed, this change is an extension and its classification is wrong. | Establish whether the composition holds any artifact belonging to the blockchain domain. | CR seed §5 Existing-System Beliefs — Requiring Verification #1 |
| The business author believes the platform already offers a way to record occurrences that is added to and never rewritten. | The record being append-only is a business requirement; if the platform provides no such facility this change must ask for one rather than assume it. | Establish whether the composition offers an append-only recording capability identity can use. | CR seed §5 Existing-System Beliefs — Requiring Verification #2 |
| The business author believes the platform already offers a way to hold a registry of business objects that can be looked up by their identifier. | Resolving an actor from a contact address, and refusing a decision about an actor that does not exist, both depend on it. | Establish whether the composition offers a registry capability identity can use. | CR seed §5 Existing-System Beliefs — Requiring Verification #3 |
| The business author believes the platform already offers a way to generate an identifier for a newly admitted business object. | An actor is admitted before it has any identifier of its own beyond the details it supplied. | Establish whether the composition offers an identifier generation capability identity can use. | CR seed §5 Existing-System Beliefs — Requiring Verification #4 |
| The business author believes the platform already distinguishes a kind of actor empowered to act on the business's behalf from an ordinary participant. | A person may never verify themselves, which requires the two kinds to be distinguishable. | Establish whether the composition declares a system or authority actor distinct from an end-user actor. | CR seed §5 Existing-System Beliefs — Requiring Verification #5 |

---

## 6. Assumptions

<!-- register:assumptions business_language optional -->
| Assumption | Basis | Source Finding |
|----------|-----|--------------|
| A contact address supplied at registration is one the person controls. | The business admits the person unverified precisely because their claims are not yet established; the address is treated as identifying without being treated as proven. | CR seed §6 Assumptions #1 |
| A person will register before an authority has occasion to decide about them. | The business author states a decision may only be made against a registration that exists, and describes no path by which an authority would encounter a person otherwise. | CR seed §6 Assumptions #2 |
| The set of authorities is small enough that recording which one decided is meaningful without governing who may be one. | The business author defers authority over verifiers to a later change while still requiring the deciding authority to be recorded. | CR seed §6 Assumptions #3 |

---

## 7. Constraints

<!-- register:constraints business_language -->
| Constraint | Source | Source Finding |
|----------|------|--------------|
| Registration and the verification decision are separate acts, made by different parties at different times. | The business author's statement that treating them as one is what this change exists to prevent. | CR seed §7 Constraints #1 |
| An unverified or rejected actor may hold no wallet and submit no transaction. | The business author's statement of what an unverified actor is permitted to be. | CR seed §7 Constraints #2 |
| A recorded occurrence may never be altered or removed. | The business author's statement that the record is added to and never rewritten. | CR seed §7 Constraints #3 |
| The time of an occurrence is determined at the moment it occurs. | The business author's statement that a record whose times do not advance is no record at all. | CR seed §7 Constraints #4 |
| Identity governs who an actor is and whether they are trusted, and nothing about what a trusted actor may do. | The business author's statement of what identity does not decide. | CR seed §7 Constraints #5 |

---

## 8. Business Invariants

<!-- register:business_invariants business_language -->
| Invariant | Source Finding |
|---------|--------------|
| An actor is identified by exactly one contact address. | CR seed §8 Business Invariants #1 |
| Two actors never share a contact address. | CR seed §8 Business Invariants #2 |
| An actor is either unverified, accepted or rejected, and never more than one of those at a time. | CR seed §8 Business Invariants #3 |
| An actor that has not been decided about is unverified. | CR seed §8 Business Invariants #4 |
| A verification decision exists only against a registration that exists. | CR seed §8 Business Invariants #5 |
| A verification decision names the authority that made it. | CR seed §8 Business Invariants #6 |
| A rejection states grounds. | CR seed §8 Business Invariants #7 |
| An actor is never accepted and rejected both. | CR seed §8 Business Invariants #8 |
| A person never makes the verification decision about themselves. | CR seed §8 Business Invariants #9 |
| Neither an unverified nor a rejected actor is trusted with anything. | CR seed §8 Business Invariants #10 |
| Every recorded occurrence carries the time it occurred. | CR seed §8 Business Invariants #11 |
| No recorded occurrence is altered or removed once written. | CR seed §8 Business Invariants #12 |

---

## 9. Lifecycle States

<!-- register:lifecycle_states business_language -->
| Object | State | Meaning | Source Finding |
|------|-----|-------|--------------|
| Actor | Unverified | The business has recorded the person's claim about themselves and has not yet accepted it. The actor is trusted with nothing. | CR seed §9 Lifecycle States #1 |
| Actor | Accepted | An authority has reviewed the actor and trusts them. | CR seed §9 Lifecycle States #2 |
| Actor | Rejected | An authority has reviewed the actor and does not trust them. The actor is trusted with nothing. | CR seed §9 Lifecycle States #3 |
| Verification Decision | Recorded | An authority has stated an outcome against a registered actor, and the business holds it as evidence. | CR seed §9 Lifecycle States #4 |

---

## 10. Business Events

<!-- register:business_events business_language -->
| Event | When It Occurs | Significance | Source Finding |
|-----|--------------|------------|--------------|
| Actor Registered Unverified | A person supplies their identifying details and is admitted. | The business now knows of the person and trusts them with nothing. It is the occurrence a verification decision is made against. | CR seed §10 Business Events #1 |
| Actor Registered Again | A person already known registers a second time. | The actor is unchanged, but that the person registered twice is a fact about them the business keeps. | CR seed §10 Business Events #2 |
| Actor Accepted | An authority records a decision to trust a registered actor. | The actor becomes trusted. It is the moment from which the other blockchain functions may name them. | CR seed §10 Business Events #3 |
| Actor Rejected | An authority records a decision not to trust a registered actor. | The actor remains trusted with nothing, and the business can afterwards ask who has been rejected and receive an answer. | CR seed §10 Business Events #4 |

---

## 11. Authority Boundaries

<!-- register:authority_boundaries business_language -->
| Business Object | Authoritative Owner | Source Finding |
|---------------|-------------------|--------------|
| Actor | The identity function of the blockchain project. | CR seed §11 Authority Boundaries #1 |
| The details an actor registers with | The person themselves. | CR seed §11 Authority Boundaries #2 |
| Verification Decision | An authority within the business, through the identity function. The authority itself is owned outside it. | CR seed §11 Authority Boundaries #3 |
| The record of occurrences against an actor | The identity function of the blockchain project. | CR seed §11 Authority Boundaries #4 |

---

## 12. Out of Scope

<!-- register:out_of_scope business_language optional -->
| Item | Reason | Source Finding |
|----|------|--------------|
| What a trusted actor may then do | Identity says who an actor is and whether they are trusted, not what trust permits. | CR seed §12 Out of Scope #1 |
| Permissions and roles beyond the distinction between an ordinary participant and an authority | Named by the business author as outside this change. | CR seed §12 Out of Scope #2 |
| An actor's standing changing through their conduct | Named by the business author as outside this change. | CR seed §12 Out of Scope #3 |
| Re-application after rejection | Rests on what a rejection is taken to mean, which this change is the first to state. | CR seed §12 Out of Scope #4 |
| Revocation of a verified actor | A governed change of its own, including what happens to what the actor did while trusted. | CR seed §12 Out of Scope #5 |
| Which persons may be an authority, and how that permission is granted or removed | This change records which authority decided; it does not govern who may be one. | CR seed §12 Out of Scope #6 |
| The material an authority examined when deciding | A separate need with its own retention and privacy consequences. | CR seed §12 Out of Scope #7 |
| Correcting an actor's own details after registration | Not answerable until a decision is defined. | CR seed §12 Out of Scope #8 |
| Wallets, transactions, mempool, blocks, chain and consensus | Later functions of the project, excluded except where they depend on identity behaviour. | CR seed §12 Out of Scope #9 |

---

## 13. Governance Scope

<!-- register:governance_scope business_language -->
| Scope Item | Relationship (CREATED, EXTENDED, MODIFIED, DEPRECATED, ADJACENT) | Source Finding |
|----------|----------------------------------------------------------------|--------------|
| Identity | CREATED | CR seed §13 Governance Scope #1 |
| Wallet | ADJACENT | CR seed §13 Governance Scope #2 |
| Transaction | ADJACENT | CR seed §13 Governance Scope #3 |
| Mempool | ADJACENT | CR seed §13 Governance Scope #4 |
| Block | ADJACENT | CR seed §13 Governance Scope #5 |
| Chain | ADJACENT | CR seed §13 Governance Scope #6 |
| Consensus | ADJACENT | CR seed §13 Governance Scope #7 |

---

## 14. Clarification Requests

<!-- register:clarification_requests business_language optional -->
| Question | Why Needed | Blocking (YES, NO) | Owner (HUMAN, SNAPSHOT, GOVERNANCE) | Source Finding |
|--------|----------|------------------|-----------------------------------|--------------|
| NONE IDENTIFIED |

---

## 15. Acceptance Criteria

<!-- register:acceptance_criteria business_language -->
| Criterion | Source Finding |
|---------|--------------|
| A person who supplies a name and a contact address is admitted, and is afterwards unverified. | CR seed §15 Acceptance Criteria #1 |
| A person who supplies no contact address is refused, and no actor exists afterwards. | CR seed §15 Acceptance Criteria #2 |
| A person who registers twice is one actor afterwards, and the business can show two registrations against them. | CR seed §15 Acceptance Criteria #3 |
| A verification decision against a person who never registered is refused. | CR seed §15 Acceptance Criteria #4 |
| An accepted actor can be shown as accepted, with the deciding authority and the time recorded. | CR seed §15 Acceptance Criteria #5 |
| A rejected actor can be shown as rejected, with the deciding authority, the grounds and the time recorded, and cannot be read as accepted by any means. | CR seed §15 Acceptance Criteria #6 |
| The business can list the actors that have been rejected. | CR seed §15 Acceptance Criteria #7 |
| A rejection stating no grounds is refused. | CR seed §15 Acceptance Criteria #8 |
| Two occurrences recorded at different moments carry different times. | CR seed §15 Acceptance Criteria #9 |
| No sequence of operations changes or removes an occurrence already recorded. | CR seed §15 Acceptance Criteria #10 |
| A decision made against an actor already decided about is refused. | CR seed §15 Acceptance Criteria #11 |
| An actor that is unverified or rejected holds no wallet and has submitted no transaction. | CR seed §15 Acceptance Criteria #12 |

---

## 16. Identity and Sameness

<!-- register:identity_and_sameness business_language optional -->
| Business Object | Identified By | Two Are The Same When | Source Finding |
|---------------|-------------|---------------------|--------------|
| Actor | The contact address they register with. | Their contact addresses match, whatever else differs. | CR seed §16 Identity and Sameness #1 |
| Verification Decision | The actor it was made against. | They were made against the same actor, which is why there is only ever one. | CR seed §16 Identity and Sameness #2 |
| Occurrence | The actor it was recorded against and the moment it happened. | Never — two occurrences at different moments are different occurrences even when they say the same thing. | CR seed §16 Identity and Sameness #3 |

---

## 17. Lifecycle Transitions

<!-- register:lifecycle_transitions business_language optional -->
| Object | From State | To State | Triggered By | Cascade | Source Finding |
|------|----------|--------|------------|-------|--------------|
| Actor | — | Unverified | A person supplies their identifying details and is admitted. | None — admission grants nothing and obliges no authority to decide. | CR seed §17 Lifecycle Transitions #1 |
| Actor | Unverified | Unverified | The same person registers a second time. | None — the state is unchanged and any decision already made stands. A second occurrence is recorded. | CR seed §17 Lifecycle Transitions #2 |
| Actor | Unverified | Accepted | An authority records a decision to trust the actor. | None within identity. The actor becoming nameable by the other blockchain functions is a consequence those functions own, not one identity performs. | CR seed §17 Lifecycle Transitions #3 |
| Actor | Unverified | Rejected | An authority records a decision not to trust the actor. | None — nothing is removed, nothing is notified, and the actor remains recorded. | CR seed §17 Lifecycle Transitions #4 |
| Verification Decision | — | Recorded | An authority states an outcome against a registered actor. | None beyond the actor's state changing with it. | CR seed §17 Lifecycle Transitions #5 |

---

## 18. Operation Refusals

<!-- register:operation_refusals business_language optional -->
| Operation | Refused When | Business Reason | Source Finding |
|---------|------------|---------------|--------------|
| Register a person | No name is supplied. | Registration may be refused for details the business cannot read. | CR seed §18 Operation Refusals #1 |
| Register a person | No contact address is supplied. | An actor is identified by the contact address they register with, so without one there is no actor. | CR seed §18 Operation Refusals #2 |
| Register a person | The contact address supplied is not of the form the business asked for. | A detail is unreadable when it is absent or not of the form asked for. | CR seed §18 Operation Refusals #3 |
| Register a person | On the business's judgement of the person, including whether they control the address or the name is theirs. | Those are matters of belief, which is the verification decision's business; refusing on them here would be making that decision early and by the wrong party. | CR seed §18 Operation Refusals #4 |
| Record a verification decision | The actor it names never registered. | The decision is a decision on a registration; without one it is not an incomplete decision but a meaningless one. | CR seed §18 Operation Refusals #5 |
| Record a verification decision | The actor has already been decided about. | An actor is decided about once. | CR seed §18 Operation Refusals #6 |
| Record a verification decision | The authority making it is the actor being decided about. | A person may never verify themselves. | CR seed §18 Operation Refusals #7 |
| Record a verification decision | The outcome is neither acceptance nor rejection. | There is no third outcome and no deferral. | CR seed §18 Operation Refusals #8 |
| Record a verification decision | The deciding authority is not named. | A decision whose author is unknown is not evidence. | CR seed §18 Operation Refusals #9 |
| Record a rejection | No grounds are stated. | The grounds are the substance of a rejection. | CR seed §18 Operation Refusals #10 |
| Alter or remove a recorded occurrence | Always. | The record is added to and never rewritten; a correction is a further occurrence. | CR seed §18 Operation Refusals #11 |

---

## 19. Authority Deferrals

<!-- register:authority_deferrals business_language optional -->
| Business Object | Deferred To | Until | Source Finding |
|---------------|-----------|-----|--------------|
| Re-application by a rejected actor | A follow-on governed change for re-application | This change states what a rejection means. | CR seed §19 Authority Deferrals #1 |
| Revocation of an accepted actor | A follow-on governed change for revocation | The business chooses to take it up. | CR seed §19 Authority Deferrals #2 |
| Which persons may be an authority, and the resolution of an authority named on a decision | A follow-on governed change for authority over verifiers | The business chooses to take it up. Identity records the name and does not resolve it. | CR seed §19 Authority Deferrals #3 |
| The material an authority examined when deciding | A follow-on governed change for identity evidence | The business settles its retention and privacy consequences. | CR seed §19 Authority Deferrals #4 |
| Correcting an actor's own details after registration | A follow-on governed change for correction | This change defines a verification decision. | CR seed §19 Authority Deferrals #5 |
| What a trusted actor may do | The wallet, transaction and consensus functions | Those functions are taken up. | CR seed §19 Authority Deferrals #6 |

---

## gov_projection — Governed Handoff to Stage 2

| Direction | Fields |
|-----------|--------|
| **Consumes** ← CR seed | human elicitation answers (the seed) |
| **Emits** → Stage 2 | cr_type · business_vocabulary · requested_outcomes · known_facts · system_beliefs · assumptions · constraints · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · governance_scope · clarification_requests · acceptance_criteria · identity_and_sameness · lifecycle_transitions · operation_refusals · authority_deferrals |
