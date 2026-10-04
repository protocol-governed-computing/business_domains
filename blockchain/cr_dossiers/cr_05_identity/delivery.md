# Delivery — cr_05_identity

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `dcfed76f7eec…`
**Delivered:** identity holds every rule it applies. A registration missing its name or address is
refused; a decision is made only about an unverified person, only as an acceptance or a rejection,
never by the person themselves; a rejection states its grounds; each act fixes what it records; the
entrances stop supplying what identity holds
**Validated:** identity 22/22 (3 not exercised), wallet 9/9; full regression 56/56 on a clean rebuild,
composition `61952a220a77…`

---

## What this change closed

Every rule identity applied was handed to it by the request. The public entrance supplied the right
values, so a caller going through transport saw correct behaviour; anything reaching the workflows
directly could widen the rules. Run against the pinned composition, a registration with no name was
registered, a registration carrying ACCEPTED was held accepted, a person was decided about twice, an
authority decided about themselves, and a decision checked as ACCEPTED recorded SUSPENDED.

Now each rule is a fixed value of the step that applies it: the registration schema, the states a
decision may be made from, the decisions admitted, the self-decision rule and the grounds rules. A
request stating rules of its own is judged by identity's, and is not refused for stating them.
Eleven artifacts were redeclared whole; nothing was created.

---

## What it took

**The design language could add and could not remove.** This is the first change that takes
anything away from an existing artifact, and it met two limits:

- `NODE_INPUT_UNBOUND` joined a contract's pinned inputs to the design's, so an input a redeclared
  contract withdrew still read as required. Where the design composes a contract's steps, its
  interface now stands alone.
- Construction's narrowing guard refused every fact an amendment omitted, intended or not. P7 gained
  `withdrawn_facts`, where a design states what it removes; 39 withdrawals are declared here. A
  withdrawal covering nothing is refused, and an omission without one still is. The same guard
  misread a value refined into a list as lost; that is fixed.

Both are rulings in `.github/process/rulings.md`, with tests in `keyed_node_design_test` and
`withdrawal_design_test`.

**The first run found what every check passed.** After emit, every registration through the
entrance was refused at admission. P3 had found that the entrances and the acceptance gate change,
and said no gate declared a rule field; the registration gate requires the schema. With the
entrance no longer sending it, the gate refused everything. All phases, and construction at 100%,
admitted the design. The dossier was re-authored from P3: the registration gate became an eleventh
artifact, with the schema withdrawn. No rule yet checks that an entrance supplies what the gate it
reaches requires.

**A reading of one criterion, ruled by the author.** *"A decision other than an acceptance or a
rejection is refused, whatever the request says about which decisions are allowed."* Each act now
fixes its own decision, so a request naming a third decision has it ignored, as any rule a request
states is ignored. The criterion holds because no record can carry a third decision; the suite
proves that rather than a refusal.

---

## What is carried

- **The moment and stream each act records** still come from the request (GAP-09). A direct caller
  can name a different occurrence from the one that happened. Deferred; no business rule names it.
- **Records made under a request's own rules** are left as they were made. Declined by the business.
- **Admission fidelity** reports twelve under-declared gate fields, down from twenty-six; the ten on
  blockchain gates are the moment, stream, address and wallet fields above.
