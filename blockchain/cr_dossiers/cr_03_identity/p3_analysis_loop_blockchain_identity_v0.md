# Stage 3 — Analysis Loop: blockchain / identity

**Stage:** 3 — Analysis Loop

**CR:** cr_03_identity

**Status:** DRAFT

**Feeds:** Stage 4 — Business Model

Each gap and concern carried from Stage 2 is driven to a committed decision against the pinned
composition. One step of one contract changes. Every question here is about that step: which
operation it should use, what the substitution costs, and what must be true for it to be safe.

---

## 1. Analysis Findings

<!-- register:analysis_findings -->
| Question Id | Finding | Impact | Evidence Status (OBSERVED, INFERRED, OPEN) | Confidence (HIGH, MEDIUM, LOW) | Resolution Status (CLOSED, OPEN) | Evidence |
|-------------|---------|--------|-----------------|------------|-------------------|----------|
| Q1 | The defect is one step and not a design error. The deciding contract's first four steps refuse what the business asked to be refused and assemble what the business asked to be recorded; all four are correct. Its fifth writes the assembled record over the record held, and that is the whole of the fault. Nothing about the contract's inputs, its refusals or its result statuses is wrong. | The correction is one step of one artifact. No workflow, boundary declaration, store, actor or event changes, and no phase of the earlier changes is reopened beyond the single step. | OBSERVED | HIGH | CLOSED | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 declares five steps; the first three validate and the fourth assembles, all through pure transforms, and only the fifth reaches a store |
| Q2 | The operation the step should use exists and is already published on the surface identity uses. A partial update takes a filter and a set of fields to change, sets only those fields on every record the filter matches, and leaves the rest of each record as it was. The change is a substitution within one capability, not a new capability and not a new binding. | Nothing is authored. The domain's runtime binding already binds this capability, because the same capability's whole-value write is what the step uses today. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE_WHERE alongside WRITE, and blockchain::RB_IDENTITY_BINDINGS_V0 already binds that capability for this subdomain |
| Q3 | Both operations address the record by the key that identifies it, so the correction depends on nothing the domain must promise. An earlier reading of this question relied on a filtered update and therefore on identity's rule that two actors never share a contact address; that reliance is gone. The store's operations now cover both ways of addressing a record and both amounts of it to change, and the one this correction needs is the one it uses. | The substitution rests on the operation rather than on a business rule, so the correction carries no condition into any domain that copies it. | OBSERVED | HIGH | CLOSED | capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE, taking a key and the fields to set, reporting a violation where the key is not held |
| Q4 | What the step changes is exactly what a decision is entitled to change. The business names three things — the person's state, the authority who decided, and the grounds stated — and those three become the fields the update sets. Everything the person supplied is absent from that set and therefore survives, which is the correction stated positively rather than as an absence. | The set of updated fields is the business rule, written where it can be read. What is not in the set is what a decision may not touch. | OBSERVED | HIGH | CLOSED | S1 known_facts #10 names the three; S1 business_invariants #2 states that a decision changes those and nothing else |
| Q5 | The contract already receives everything the new operation needs and receives one thing it will no longer use. The decided fields it is given carry the state, the authority and the grounds, and the contact address it is given is what the filter matches on. The record its fourth step assembles becomes unnecessary, because the update sets fields rather than writing a value. | The assembling step has no consumer once the write becomes an update. Leaving a step whose output nothing reads would be a step that does not participate, which is what an unbound capability already teaches against. | OBSERVED | HIGH | CLOSED | blockchain::CC_RECORD_VERIFICATION_DECISION_V0 declares assemble_decided_actor with output record, consumed only by write_decided_actor |
| Q6 | The two operations disagree about a subject that is absent, and the disagreement moves the contract in the safer direction. A whole-value write to a key nothing holds creates it and reports success. A partial update whose filter matches nothing changes nothing and reports a violation. The deciding workflow resolves the actor before the contract runs, so neither case should arise. | If the resolution step were ever bypassed, today's contract would invent an actor and tomorrow's would refuse. The change removes a way for this subdomain to hold a person nobody registered. | OBSERVED | HIGH | CLOSED | The whole-value write sets the value at the key unconditionally; the partial update reports a violation with no matched keys; blockchain::CC_RESOLVE_ACTOR_V0 precedes the deciding contract in both workflows that reach it |
| Q7 | Nothing observes the change above the contract. The workflow routes on the contract's result status, which keeps the same admitted values. The boundary declarations name the workflow rather than any contract, and what a caller is told is projected from the workflow's result surface. A caller sending what they send today reaches the same act and is told the same thing. | The business's promise that this change is invisible from outside is a property of how the layers are declared, not an intention anyone must uphold. | OBSERVED | HIGH | CLOSED | S2 belief_verification #5; the contract's result_status_contract admits SUCCESS, VIOLATION and BACKEND_ERROR, and the partial update surfaces those same statuses |
| Q8 | Nothing depends on the shape a decision currently leaves. One artifact reads the store, reads the record whole, and the workflow consumes a single field of it. No artifact enumerates the record's fields, asserts their number, or reads a name or a preference. | Restoring fields to a record is unobservable to every reader in the composition. The correction cannot break a consumer because there is no consumer of what it restores — yet. | OBSERVED | HIGH | CLOSED | S2 belief_verification #4; blockchain::CC_RESOLVE_ACTOR_V0 publishes the record as one object and the deciding workflows read state from it |
| Q9 | Records already thinned stay thinned, and this is a decision rather than an omission. The business declines to rewrite what it has recorded, and the rule that a record is added to and never rewritten holds even when what was written is thin. A person decided about before this change carries no name and will carry none. | No migration, no backfill, no repair step. A record written before this change and one written after it will differ, and the business has accepted that. | OBSERVED | HIGH | CLOSED | S1 known_facts #15 through #18; S1 out_of_scope #4 |
| Q10 | The composition cannot say which artifacts consume a store, and this change needed exactly that. The index that answers it joins a runtime binding to a store by a concrete path, and only one binding in the composition names a path; every other names a storage declaration instead. The answer was established by reading the contracts that name the store. | The finding is recorded and the fact it was needed for was obtained another way. Repairing the index is a change against the components that build and publish it, and this change authors neither. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns The composition cannot answer which artifacts consume a store |
| Q11 | This is the second rule in this subdomain that the business stated and no artifact realises. The first is that a rejection states grounds; the second is that a person keeps what they were admitted with. Both passed every document check, because a rule that no step consults is a true statement about an artifact rather than a property of one. | Neither is a phase-rule failure, and adding a phase rule would not have caught either. What catches them is executing the function and reading what it left behind, which is what an execution validation is for. | OBSERVED | HIGH | CLOSED | S2 discovery_concerns A rule the business states in its own documents is realised in no artifact |

## 2. Verification Results

<!-- register:verification_results -->
| Item | Origin | Result (CONFIRMED, OVERTURNED) | Evidence |
|------|--------|--------------------------------|----------|
| The business author believes recording a decision replaces the person's record rather than adding to it. | S2 belief_verification #1 | CONFIRMED | Resolved in Q1: the fifth step writes the assembled record whole, over the record held |
| The business author believes the platform can already change named fields of a stored record while leaving its other fields as they are. | S2 belief_verification #2 | CONFIRMED | Resolved in Q2: the capability publishes a partial update and the domain already binds that capability |
| The business author believes a person's admitted details are held in one place, so that not overwriting them is enough to keep them. | S2 belief_verification #3 | CONFIRMED | One store, one path, one declaring artifact; three contracts name it and only one reads it |
| The business author believes nothing else in the composition depends on the shape a decision currently leaves behind. | S2 belief_verification #4 | CONFIRMED | Resolved in Q8: the single reader reads the record whole and one field is consumed |
| The business author believes what a caller sends and is told is declared apart from how a decision is performed. | S2 belief_verification #5 | CONFIRMED | Resolved in Q7: the boundary names the workflow, the workflow routes on a result status, and neither changes |
| Recording a decision writes a whole record where it should change part of one. | S2 gaps #1 | CONFIRMED | Resolved in Q1 and Q4 |
| Nothing in the composition states which of a person's details a decision may change. | S2 gaps #2 | CONFIRMED | Resolved in Q4: the updated set becomes that statement, and Q11 records why nothing caught its absence |
| The composition cannot answer which artifacts consume a store. | S2 discovery_concerns #1 | CONFIRMED | Resolved in Q10 and carried as a change against other components |
| A rule the business states is realised in no artifact and checked by nothing. | S2 discovery_concerns #2 | CONFIRMED | Resolved in Q11 |
| The occurrence a decision records carries less than the business describes. | S2 discovery_concerns #3 | CONFIRMED | Untouched by this change; the trail is unchanged by constraint |
| The store's operations divide by how a record is addressed and by how much of it is changed, and one of the four was missing. | S2 architectural_observations #2 | CONFIRMED | Resolved in Q3: the missing operation was added to the capability surface, and the correction uses it rather than a filtered update |

## 3. Dependency Discoveries

<!-- register:dependency_discoveries -->
| Dependency | Type | Disposition (EXISTING, REUSE, AUTHOR_NEW, INVESTIGATE) | Evidence |
|------------|------|------------------------|----------|
| Partial update of a held record at a key | Capability operation | REUSE | capability_side_effects::CS_MUTABLE_JSON_V0 publishes UPDATE, taking a key and a set of updates |
| The store the decision writes | Store declaration | REUSE | blockchain::STRUCTURE_IDENTITY_STORAGE_V0, unchanged |
| The binding that reaches the store | Runtime binding | REUSE | blockchain::RB_IDENTITY_BINDINGS_V0 already binds the capability the step uses today |
| Resolving the actor before deciding | Capability contract | REUSE | blockchain::CC_RESOLVE_ACTOR_V0, unchanged, and the reason the absent-subject disagreement never arises |
| The workflows that compose the deciding contract | Workflow | REUSE | blockchain::WF_RECORD_VERIFICATION_DECISION_V0, unchanged; it routes on a result status this change preserves |
| What a caller may send and is told | Boundary declarations | REUSE | The four blockchain transport artifacts, unchanged; none names a contract |
| The step that assembles the decided record | Contract step | INVESTIGATE | Its only consumer is the step this change replaces; Q5 records that it is left without one |
| Which artifacts consume a store | Inspection operation | INVESTIGATE | Answers for one store in fifteen; the fact was obtained by reading contracts instead |

## 4. Impact Analysis

<!-- register:impact_analysis -->
| Artifact | Impact Scope | Consumer Count | Evidence |
|----------|--------------|----------------|----------|
| blockchain::CC_RECORD_VERIFICATION_DECISION_V0 | Amended — one step changes operation, and the step feeding it loses its consumer | 3 | si.topology.impact impacted_count 3 |
| capability_side_effects::CS_MUTABLE_JSON_V0 | Reused unchanged; a different operation of the same capability is called | 51 | The capability publishes both operations; the change selects between them |
| blockchain::WF_RECORD_VERIFICATION_DECISION_V0 | Composes the amended contract; not itself amended | 0 | si.topology.impact impacted_count 0 |
| blockchain::CC_RESOLVE_ACTOR_V0 | Reused unchanged; the only reader of the store, and unaffected by fields being restored | 2 | Reads the record whole and asserts nothing about its shape |
| blockchain::RB_IDENTITY_BINDINGS_V0 | Reused unchanged; already binds the capability | 0 | The binding names the capability, not the operation |
| blockchain::STRUCTURE_IDENTITY_STORAGE_V0 | Reused unchanged | 0 | The store, its path and its declaration are untouched |
| blockchain::TI_ACCEPT_ACTOR_V0 | Not changed; names the workflow, not the contract | 0 | si.topology.impact impacted_count 0 |
| blockchain::TI_REJECT_ACTOR_V0 | Not changed; the same | 0 | si.topology.impact impacted_count 0 |

## 5. Authoring Decisions

<!-- register:authoring_decisions business_language=capability -->
| Capability | Decision (REUSE, EXTEND, AUTHOR_NEW) | Rationale | Alternatives Checked | Source Finding |
|------------|----------|-----------|----------------------|----------------|
| Record a decision against a registered person | EXTEND | The contract is right in every respect but one: it writes a whole record where it must change part of one. Its refusals, its inputs and its result statuses are unchanged, and one step is replaced. | Authoring a second contract was checked and rejected: it would leave two contracts recording a decision, one of them wrong, and nothing to say which a workflow should reach. Leaving the defect was checked and rejected by the business. | S3 analysis_findings Q1 |
| Change part of a held record without replacing it | REUSE | The capability already publishes a partial update, and the domain already binds that capability because the step uses its whole-value write today. | Reading the record and writing it back whole was checked and rejected: it is two steps where one suffices, and between the read and the write nothing holds the record still. Asking for a new capability was checked and rejected — one exists. | S3 analysis_findings Q2 |
| State which of a person's details a decision may change | REUSE | The three the business named become the fields the update sets. What is not in that set is what a decision may not touch, so the rule is written where a reader can see it rather than asserted in a document nothing consults. | Declaring the rule as an invariant alone was checked and rejected: that is exactly what has been true since the function was built, and it caught nothing. | S3 analysis_findings Q4 |
| Assemble the record a decision writes | REUSE | Retained unchanged in this change. Its output loses its consumer when the write becomes an update, which is recorded rather than resolved here. | Removing it was checked and deferred: a step's removal changes the contract's shape more than the defect requires, and the business asked for the smallest correction that ends the data loss. | S3 analysis_findings Q5 |
| Resolve the actor before a decision is recorded | REUSE | Unchanged, and the reason the two operations' disagreement about an absent subject never arises. | Nothing; the step is correct. | S3 analysis_findings Q6 |
| Reach the decision from outside | REUSE | The four boundary declarations are untouched. They name the workflow, and the workflow is untouched. | Nothing; the layers are already separated, which is what makes the change invisible. | S3 analysis_findings Q7 |
| Restore details already lost | REUSE | Nothing is authored. The business declines to rewrite records already written, thin ones included. | A repair step was checked and rejected by the business: the record is added to and never rewritten. | S3 analysis_findings Q9 |

## 6. Placement Decision

<!-- register:placement_decision business_language=rationale -->
| Decision (NEW_SUBDOMAIN, EXTEND) | Subdomain | Rationale | Source Finding |
|----------|-----------|-----------|----------------|
| EXTEND | identity | The step being corrected belongs to the function that owns the record it writes. Nothing moves, nothing is added, and no other subdomain holds a person's details or decides about them. | S3 analysis_findings Q1 |

## 7. Saturation Assessment

<!-- register:saturation business_language=criterion -->
| Criterion | Status (SATISFIED, NOT_SATISFIED) | Evidence |
|-----------|--------|----------|
| No unresolved CRITICAL gaps | SATISFIED | The one CRITICAL gap resolves to a committed decision: the deciding contract's fifth step changes from a whole-value write to a partial update, setting the three fields a decision is entitled to change |
| No open analyst questions | SATISFIED | All eleven findings are CLOSED. The seed carried no clarification requests, and this stage raised no question for the business author |
| No dependency expansion in the last pass | SATISFIED | The eight dependencies were established in one pass against the contract, its capability and the layers above it; re-reading them surfaced nothing further. Two are recorded INVESTIGATE and neither is a prerequisite: an assembling step left without a consumer, and an inspection operation that answers for one store in fifteen |
| Verification pass complete, no OVERTURNED item unresolved | SATISFIED | All eleven items re-grounded and CONFIRMED, including every Stage 2 belief and all three of its discovery concerns |
| Every INFERRED finding promoted to OBSERVED, explicitly accepted, or carried forward with a reason | SATISFIED | Stage 2's single INFERRED row is promoted to OBSERVED rather than carried: it recorded that a filtered update coincided with a keyed one only because of a business rule, and the capability now publishes the keyed update the correction needs, so no coincidence is relied upon. Every finding in this stage is OBSERVED |

---

## gov_projection — Governed Handoff to Stage 4

| Direction | Fields |
|-----------|--------|
| **Consumes** ← Stage 1 | cr_type · assumptions · business_invariants · lifecycle_states · business_events · authority_boundaries · out_of_scope · constraints |
| **Consumes** ← Stage 2 | belief_verification · pps_baseline_fqdns · gaps · architectural_observations · discovery_concerns · open_questions |
| **Emits** → Stage 4 | authoring_decisions · dependency_discoveries · placement_decision · saturation |
