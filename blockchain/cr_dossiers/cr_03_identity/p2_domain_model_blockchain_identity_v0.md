# Stage 2 — Domain Model Verification: blockchain / identity

**Stage:** 2 — Domain Model Verification
**CR:** cr_03_identity
**Status:** DRAFT
**Feeds:** Stage 3 — Analysis Loop

Every belief the change request declared is resolved against the pinned composition. This change
request is against a defect rather than an absence: the function exists, runs and is reached from
outside, and what is verified here is how one of its steps writes, what the platform offers instead,
and whether anything depends on what that step currently leaves behind.

---

## 1. Business Entities

<!-- register:entities business_language -->
| Entity | Description | Store Model | Evidence Status | Source Finding |
|--------|-------------|-------------|-----------------|----------------|
| The Record | What the business holds about a person: their admitted details together with their decided details. | One keyed store, holding one record per contact address, declared once by the subdomain's storage declaration and by nothing else. | OBSERVED | S2 belief_verification #3 |
| Admitted Details | The name, the contact address and the preferences a person supplied when they registered. | Held in the same record. Written when the person is admitted and, today, removed when a decision is recorded. | OBSERVED | S2 belief_verification #1 |
| Decided Details | The three things a decision is entitled to change: the person's state, the authority who decided, and the grounds stated. | Held in the same record, written by the deciding act. | OBSERVED | S1 known_facts #10 |
| The Trail | The occurrences recorded against a person, added to and never rewritten. | A separate append-only stream, untouched by this change. | OBSERVED | S1 constraints #6 |
| Thinned Record | A record from which a decision has already removed a person's admitted details. | The same store. Left as it is; the business declines to rewrite it. | OBSERVED | S1 known_facts #15 |

<!-- register:entity_attributes business_language -->
| Entity | Attribute | Meaning | Evidence Status | Source Finding |
|--------|-----------|---------|-----------------|----------------|
| Admitted Details | Name | What the person is called, supplied by them at registration. | OBSERVED | S1 known_facts #5 |
| Admitted Details | Contact Address | The address the person registered with, which identifies them and keys their record. | OBSERVED | S2 belief_verification #3 |
| Admitted Details | Preferred Currency | A convenience recorded at registration, having a default. | OBSERVED | S1 known_facts #5 |
| Admitted Details | Preferred Language | A convenience recorded at registration, having a default. | OBSERVED | S1 known_facts #5 |
| Decided Details | State | Whether the person is unverified, accepted or rejected. | OBSERVED | S2 belief_verification #4 |
| Decided Details | Verifying Authority | The authority the decision names. | OBSERVED | S1 known_facts #10 |
| Decided Details | Grounds | The reason stated for the decision. | OBSERVED | S1 known_facts #10 |

## 2. Business Processes

<!-- register:business_processes business_language -->
| Process | Initiator | Outcome | Evidence Status | Source Finding |
|---------|-----------|---------|-----------------|----------------|
| Record a decision about a person | An authority within the business | The person's state, the deciding authority and the grounds are recorded, and everything else the business holds about them is left as it was. | OBSERVED | S1 requested_outcomes #1 |

<!-- register:process_steps business_language -->
| Process | Step # | Action | Record Produced | Evidence Status | Source Finding |
|---------|--------|--------|-----------------|-----------------|----------------|
| Record a decision about a person | 1 | Resolve the person the address names, and refuse if none is found. | None. | OBSERVED | S2 belief_verification #4 |
| Record a decision about a person | 2 | Refuse every refusal the business declared — a state that admits no decision, an outcome that is not admitted, an authority deciding about itself. | None. | OBSERVED | S2 pps_baseline_fqdns #1 |
| Record a decision about a person | 3 | Change the person's state, the authority named and the grounds, leaving every other detail as it is. | The person's record, still carrying what they were admitted with. | OBSERVED | S1 business_invariants #2 |
| Record a decision about a person | 4 | Record that the decision occurred. | An occurrence, unchanged by this change. | OBSERVED | S1 constraints #6 |

## 3. Belief Verification — THE SPINE

<!-- register:belief_verification -->
| Belief | Result (VERIFIED, NOT_FOUND, INSUFFICIENT_EVIDENCE) | Evidence | Source Finding |
|--------|------------------------------------------------------|----------|----------------|
| The business author believes recording a decision replaces the person's record rather than adding to it. | VERIFIED | The fifth and last step of blockchain::CC_RECORD_VERIFICATION_DECISION_V0 writes to the ACTORS store with the operation WRITE, keyed on the contact address, and the value it writes is the record assembled by its own fourth step from the decided fields it was given. WRITE sets the whole value at the key, so whatever the assembled record does not carry ceases to be held. The assembled record carries the contact address, the state, the authority and the grounds, and nothing the person supplied. The belief holds exactly: the record is replaced, not added to. | S1 system_beliefs #1 |
| The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are. | VERIFIED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE alongside WRITE, READ, EXISTS, LIST, SELECT, DELETE, DELETE_MANY and UPDATE_WHERE. UPDATE takes a key and a set of updates, and sets only the named fields on the record held at that key, leaving its other fields as they were. It reports SUCCESS when the key was held and VIOLATION when it was not, so it changes a record and never creates one. The capability this change needs exists, addresses one record by the key that identifies it, and is published on the surface identity already uses. | S1 system_beliefs #2 |
| The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them. | VERIFIED | The composition declares exactly one store for this business's actors, blockchain::ACTORS, at one path, declared once by blockchain::STRUCTURE_IDENTITY_STORAGE_V0 and by no other artifact. Of the domain's six capability contracts, three name that store: one writes the actor when it is admitted, one writes it when a decision is recorded, and one reads it. No other artifact of any domain declares or writes it. Not overwriting is therefore sufficient. | S1 system_beliefs #3 |
| The business author believes nothing else in the composition depends on the shape a decision currently leaves behind. | VERIFIED | blockchain::CC_RESOLVE_ACTOR_V0 is the only reader of the store. It reads the record whole and publishes it as one object, and the deciding workflow consumes a single field of it — the state — to decide whether a decision is admitted. Nothing reads a name or a preference, and nothing enumerates the record's fields or asserts their number. Restoring what a decision currently removes adds fields to a value one consumer reads one field of, which no artifact can observe. | S1 system_beliefs #4 |
| The business author believes what a caller sends and is told is declared apart from how a decision is performed. | VERIFIED | What a caller may send is declared by blockchain::TI_ACCEPT_ACTOR_V0 and blockchain::TI_REJECT_ACTOR_V0, and what they are told by blockchain::TE_ACCEPT_ACTOR_V0 and blockchain::TE_REJECT_ACTOR_V0. Each names the workflow it dispatches to and maps the caller's values onto that workflow's payload; none of the four names a capability contract or a step. A change inside a contract the workflow composes is invisible to all four, and the answer a caller is told is projected from the workflow's result surface, which this change does not alter. | S1 system_beliefs #5 |

## 4. PPS Baseline — What Already Exists

<!-- register:pps_baseline_fqdns -->
| Capability | FQDN | What It Does | Fit (EXACT, PARTIAL, MISMATCH) | Cannot Do |
|-----------|------|--------------|--------------------------------|-----------|
| Recording a decision | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Refuses every declared refusal in three steps, assembles the decided record in a fourth, and writes it in a fifth. | PARTIAL | Its first four steps are correct and untouched by this change. Its fifth writes a whole record where it should change part of one, which is the defect. |
| Whole-value write | capability_side_effects::CS_MUTABLE_JSON_V0 WRITE | Sets the value held at a key, whatever was there before. | MISMATCH | It cannot preserve what the value it is given does not carry. It is the right operation for admitting a person, whose record does not yet exist, and the wrong one for deciding about them. |
| Partial update at a key | capability_side_effects::CS_MUTABLE_JSON_V0 UPDATE | Sets named fields on the record held at one key, leaving its other fields as they are, and reports whether that key was held. | EXACT | It changes a record and never creates one: a key nothing holds is reported as a violation. It addresses exactly the record the key identifies, so nothing about it depends on a rule of the domain that calls it. |
| Reading an actor | blockchain::CC_RESOLVE_ACTOR_V0 | Resolves a contact address to an actor and reads the record whole. | EXACT | Nothing for this purpose. It is the only reader, and it reads the whole record without asserting its shape. |
| The actor store | blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Declares the store holding this business's actors, at one path. | EXACT | Nothing for this purpose; the store is unchanged by this change. |
| Admitting a person | blockchain::CC_REGISTER_ACTOR_V0 | Writes the actor when they are admitted, carrying the details they supplied. | EXACT | Nothing for this purpose. It writes a record that does not yet exist, which is what a whole-value write is for. |

## 5. Gap Analysis — What Is Missing

<!-- register:gaps business_language -->
| Gap | Severity | Impact | Evidence Status | Source Finding |
|-----|----------|--------|-----------------|----------------|
| Recording a decision writes a whole record where it should change part of one. | CRITICAL | Every person accepted or rejected loses the name and the preferences they registered with. The business stated the opposite rule when the function was established and has been breaking it since. | OBSERVED | S2 belief_verification #1 |
| Nothing in the composition states which of a person's details a decision may change. | MAJOR | The rule is stated in the business's own documents and realised in no artifact, which is why the defect was invisible to every check the composition runs. | OBSERVED | S1 business_invariants #2 |
| Nothing restores the details already lost from records decided about before this change. | MINOR | Deliberately so — the business declines to rewrite what it has recorded, and would rather carry a thin old record than edit history. | OBSERVED | S1 out_of_scope #4 |

## 6. Architectural Observations

<!-- register:architectural_observations business_language -->
| Observation | Evidence | Evidence Status | Source Finding |
|-------------|----------|-----------------|----------------|
| The two writes to one store want different operations, because they answer different questions. | blockchain::CC_REGISTER_ACTOR_V0 writes a record that does not yet exist, for which a whole-value write is correct. blockchain::CC_RECORD_VERIFICATION_DECISION_V0 writes a record that does, for which it is not. Both use the same operation today, and only one of them should. | OBSERVED | S2 pps_baseline_fqdns #2 |
| The store's operations divide by how a record is addressed and by how much of it is changed, and one of the four was missing. | A whole-value write addresses one record by its key; a filtered update addresses a set by matching values. Nothing addressed one record by its key and changed part of it, which is exactly what recording a decision needs. The capability now publishes it, so the correction rests on the operation it needs rather than on a rule of the domain that calls it. | OBSERVED | S2 pps_baseline_fqdns #3 |
| The two operations disagree about a subject that is absent, and the disagreement is in the safe direction. | A whole-value write to a key nothing holds creates it and reports success. A partial update whose filter matches nothing changes nothing and reports a violation. A decision reaches its write only after the actor has been resolved, so neither case should arise; if it did, the current operation would invent an actor and the proposed one would refuse. | OBSERVED | S2 pps_baseline_fqdns #3 |
| Every operation on the actor store already serialises concurrent callers within one process. | The store's implementation takes a per-file lock around load, modify and save for each of its operations, so a partial update is not a weaker guarantee than the whole-value write it replaces. The lock is held per process, so it orders callers inside one server and not between a server and a separate run. | OBSERVED | S2 pps_baseline_fqdns #3 |
| The correction is invisible to every layer above the contract. | The workflow composing the contract routes on its result status, which is unchanged; the boundary declarations name the workflow, not the contract; and the answer a caller is told is projected from the workflow's result surface. Nothing between the caller and the changed step observes the change. | OBSERVED | S2 belief_verification #5 |

## 7. Discovery Concerns

<!-- register:discovery_concerns business_language -->
| Concern | Evidence | Severity | Evidence Status | Source Finding |
|---------|----------|----------|-----------------|----------------|
| The composition cannot answer which artifacts consume a store, for fourteen of the fifteen stores it holds. | The inspection operation that exists for this question reports no consumer for every store but one. The exception is a store whose runtime binding names a concrete path in its policy; every other binding names a storage declaration instead, and the index that answers the question joins a binding to a store by path alone. The domains that bind by declaration are every one the pipeline authored, plus the reference workload. This change needed exactly that answer — whether anything depends on the shape a decision leaves — and had to establish it by reading the contracts instead. | MAJOR | OBSERVED | S2 belief_verification #4 |
| A rule the business states in its own documents is realised in no artifact and therefore checked by nothing. | The business declared at the outset that a person keeps the details they were admitted with. No invariant, no contract step and no phase rule expresses it, so every document has passed and every build has succeeded while the function did the opposite. This is the second such rule found in this subdomain, after the requirement that a rejection states grounds. | MAJOR | OBSERVED | S2 gaps #2 |
| The occurrence a decision records carries less than the business describes. | An occurrence holds the contact address, the grounds, the time, what happened and the authority. A registration that differs from an earlier one is described by the business as recording the differing details, and the occurrence carries no name to record them in. This change does not touch the trail and does not correct it. | MINOR | OBSERVED | S1 constraints #6 |

## 8. Open Questions

<!-- register:open_questions -->
| Question | Category | Why It Matters | Source Finding |
|----------|----------|----------------|----------------|
