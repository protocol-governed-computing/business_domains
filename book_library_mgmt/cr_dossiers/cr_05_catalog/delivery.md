# Delivery — cr_05_catalog

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `34c8a0e8a3f2…`
**Delivered:** the catalog holds every rule it applies. Only staff the library's rules admit perform a
catalog operation, whatever rules a request states; a book, a work or a further edition lacking what
the library says it must contain is refused; what the catalog checks is what it records; a copy is
registered as registered; a correction keeps the record's state and meets the book description
**Validated:** catalog CR-1 23/23, CR-2 and this change 27/27; full regression 57/57 on a clean
rebuild, composition `25009fed290d…`

---

## What this change closed

The catalog has no transport entrance, so every caller invokes its acts directly — and every act
confirmed its staff against rules the request supplied. Run against the pinned composition, someone
the library had not authorized registered a book by sending an empty list of rules. That was the
whole of authorization in the catalog: a caller stating the rules it would be judged by.

The same shape held for the book's description. The checks found what a registration lacked and the
registration went ahead; the description itself came from the request; and what the submission
check examined was a copy the request sent beside the book, not the book the act recorded. Every book
the library's own exercise registered was recorded with no subject, because the act read the subject
where no caller sent it — the defect `cr_04_catalog` found and set aside.

Now the confirming contract holds the library's rules; the checking contracts hold the descriptions
and refuse on what they find; each registration checks the record it writes, with the subject callers
supply; a copy is written as registered; a correction keeps its state and is checked. Twenty-six
artifacts were redeclared whole and thirty-six facts withdrawn; nothing was created. Every request the
library's two existing exercises send is admitted with the same outcome as before.

---

## What it took

**The design was generated.** P7 redeclares ten workflows whole — 70 topology rows, 24 composition
steps, 147 bindings — and was written by `.github/process/notes/cr05-catalog-generators/
gen_catalog_p7.py`, which reads the artifacts as the pinned composition holds them and applies P3's
decisions in one function, `apply_decisions`. P8 was generated from it. Both are kept as evidence
under ruling C1. The phase checks admitted the documents on what they say, as they would a hand-written
one; construction measured them at 100% with nothing narrowed.

**Discovery widened the change twice, and the author ruled each time.** Measuring the problem found a
copy registered already retired. Reading every act found a correction that set a state the library
does not have and left a book with no subject, and the subject defect above. Each was put to the
business author before it entered the design.

**The fixture copy.** The catalog's construction acceptance replays maintained copies of its
dossiers; `fixture_dossiers/cr_05_catalog` is this change's.

---

## What is carried

- **Who a caller is.** The credentials a request presents are its own: the catalog now holds the rules
  they are judged by, and a request presenting `authorized: true` is still admitted. Authentication is
  outside the catalog (GAP-09).
- **Records made before this change** are left as they were made, including every book recorded
  without a subject.
- **An incomplete further edition** is refused at its gate, which types each field, before the
  catalog's own check is reached. The check is there for any edition the gate admits.
- **The superseded correction act** still names the rules its contract no longer takes. It is not in
  force.
