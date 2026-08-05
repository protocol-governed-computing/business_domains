# P0 — Elicitation Record

Where each statement in the seed came from. Two passes produced it: **observation**, which reads
every fact the pinned baseline can answer so it is never asked of a person, and **elicitation**,
which asks for what only the business owner holds and never infers it.

---

## Observed — read from the baseline, never asked

Pinned baseline `7789a543…` — 292 artifacts across `ai_governance`, `inspection`, `platform`,
`transformation`, `workload`.

| Observation | Result |
|---|---|
| Is `book_library_mgmt` present in the baseline? | No — no artifact carries the namespace |
| Does baseline vocabulary claim *book*, *copy*, *title*, *isbn*, *identifier*, *retire*, *duplicate*? | No — zero identities for each |
| Does baseline vocabulary claim *catalog* or *search*? | Only as snapshot-inspection operations (`inspection::TI_SI_CATALOG_V0`, `inspection::TI_SI_VOCAB_SEARCH_V0`) — unrelated to a library catalog |
| Declared stores | 5, in `ai_governance` and `platform`; none library-related |
| Existing subdomains | `ai_governance/{agent_governance, ai_licensing}`, `transformation/{design, build}`, plus platform and inspection surfaces |
| Record-handling capability available for reuse | `capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0`, `CT_PURE_VALIDATE_RECORD_STRUCTURE_V0`, `CT_PURE_FILTER_RECORDS_V0` |
| Audit capability available for reuse | `ai_governance::CC_APPEND_AUDIT_EVENT_V0` |

Whether the last two are reused is a P2/P3 decision. Recording them here keeps it from being a P0 one.

---

## Elicited — asked of the business author, answered by them

Each answer was written into the problem statement, so every seed row traces to a sentence a person
wrote rather than to a conversation.

| Asked | Answered |
|---|---|
| Is "bibliographic work" the right term for the catalog's central object? | No — the term is confusing. The object is the **book**; bibliographic information is its metadata. |
| What is the minimum bibliographic information that supports searching by kind of book? | Title, author, publication year, and subject. At least one subject, possibly several. |
| What identifies a book, and when are two the same? | Title, author and publication year together. A book record is therefore an edition, not a timeless title. |
| Do non-book materials have a place in the catalog? | "Book" is the general term for anything the library catalogs. |
| Can a single physical copy be retired on its own? | Yes — lost or damaged, independently of its book. |
| Must a book have a copy to be registered? | Yes — a book is never registered without at least one copy. |
| Does any retirement follow automatically from another? | No. Staff retire each record explicitly; no cascade in either direction. |
| What identifies a physical copy? | The barcode the library assigns to it. |
| May a copy be registered against a retired book? | Yes. |
| What happens when staff register a book that already exists? | Refused — the book exists, and a further copy is what staff register instead. |
| Is a retired book still findable? | Excluded from search; its details remain retrievable. |
| Does "complete book details" include the copies? | Yes — bibliographic information and the copies the library holds. |
| Do search and retrieval raise business events? | No. All operations are audited; only the five state-changing moments are events. |
| Does registering a book raise one event or two? | One. Nothing yet exists that would consume a separate copy event. |
| Who grants staff their authorization? | Not the catalog. Deferred to the `staff` function, which governs library employees. |
| Is a staff function missing from the project scope? | Yes — the ten functions now include `staff`. Patrons are library users, not employees, so staff authorization does not belong to `patron` (where CR-1 placed it) or to `policy`. |
| Are the nine remaining project functions in the governance scope? | Yes, as `ADJACENT` — named and planned, not governed here. |
| Are the existing manual records imported? | No. The catalog starts empty. |
| Are the three assumptions true as written? | Confirmed: no performance requirement, one collection, the nine remaining functions establish future scope only. |
| Is `NEW_SUBDOMAIN` the right classification? | Confirmed. |
| May a retired book or copy return to the registered state? | Yes — authorized staff may reinstate either. Retirement final would leave a re-acquired book's copies invisible to search, and a found copy with nothing to come back as. |
| May an update change the title, author or publication year? | Yes, and the update is refused when the result would match another registered book. Forbidding it would force retire-and-re-register, which orphans the copies. |

---

## Knowledge provenance

| Source | Count | What it covers |
|---|---|---|
| **Observed** — read from the baseline | 7 | namespace absence, vocabulary collisions, stores, subdomains, reusable capabilities |
| **Provided** — answered by the business author | 22 | every question above, each written into the statement |
| **Quoted** — restated from the statement | all remaining seed rows | reorganization, not enrichment |
| **Inferred** — asserted by the pipeline and not validated | 0 | — |

The three rows in §6 Assumptions are inferences by nature; each was put to the author and confirmed,
which is what keeps the inferred count at zero.

---

## What the language learned

Four registers were added to P0 and P1 because the walk needed them and the template had nowhere to
put the answers:

| Register | Why it was missing | What it now holds |
|---|---|---|
| §16 Identity and Sameness | Identity blocked every other question and had been landing in Known Facts, where no phase reads it as a rule | Book identified by title + author + publication year; copy by barcode |
| §17 Lifecycle Transitions | §9 records states but not what moves between them, so a deliberate *no cascade* decision had nowhere to live and a later phase would be free to invent one | Six transitions, each declaring its cascade as none |
| §18 Operation Refusals | Refusals were scattered between Known Facts and Constraints; an omitted refusal becomes a path that succeeds where the business requires failure | Seven refusals |
| §19 Authority Deferrals | §11 can only name an owner, so a deferral was indistinguishable from ownership and P6 would place against a function that does not exist | Staff authorization deferred to `staff` |

The elicitation table in the P0 template gained a question for each — none of the four was among the
sixteen it previously asked.

The last two answers came from a cold reproduction rather than from the walk: a worker authoring the
same seed with no access to the elicitation raised both as blocking, and the statement was silent on
each. See `p0_cold_reproduction.md`.

**Verdict:** ADMISSIBLE, 0 findings over 80 declared rules, figure of merit ★★★★★ 5/5 with no open
clarifications.