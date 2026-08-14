"""Execution validation — run the catalog against the acceptance criteria its CR declared.

`tc construction check` proves a design determines its artifacts. `construction_acceptance.py` proves
the artifacts built are the ones the design determines. Neither proves the composition *does what the
business asked for*, because both read documents and this reads behaviour: every criterion in the CR's
§15 is exercised by dispatching real workflows through `protocol_runtime` against a fresh data root.

Each scenario is stated as the criterion it proves, so a failure names a business promise rather than
a workflow. State accumulates deliberately — a book must be registered before a copy can be refused
for duplicating its barcode — so the order is part of the evidence and the run is not idempotent.
That is why it starts from an empty data root every time.

Run:  python business_domains/book_library_mgmt/testbed/catalog/execution_validation.py [snapshot]
      ... --data-root <path>     keep the stores instead of discarding them
Exit: 0 if every criterion holds, 1 otherwise.

Without `--data-root` the run works in a temp directory and removes it, because the evidence is the
criteria and nothing else. With it, the stores are left where they were written so the catalog can be
read after the fact — the same run, persisted. The path must be empty or absent: this run is not
idempotent, and starting it over state from a previous run proves nothing about either.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve()
DOMAIN = HERE.parents[2]
WORKSPACE = DOMAIN.parents[1]

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402

NS = "book_library_mgmt::"
STORE = "book_library_mgmt/catalog"

# Authorization is read, never granted: the caller supplies the credentials and the rules they are
# checked against, because deciding who is authorized is deferred to the staff function. An
# unauthorized attempt is the same call with credentials that fail the same rules.
RULES = [{"field": "staff_id", "op": "not_null"}, {"field": "authorized", "op": "eq", "value": True}]
STAFF = {"staff_id": "s-101", "authorized": True}
INTRUDER = {"staff_id": "s-999", "authorized": False}


def auth(staff=None) -> dict:
    return {"staff_credentials": staff or STAFF, "authorization_rules": RULES,
            "staff_id": (staff or STAFF)["staff_id"]}


ODYSSEY = {"title": "The Odyssey", "author": "Homer", "publication_year": 1614}
ILIAD = {"title": "The Iliad", "author": "Homer", "publication_year": 1611}


BOOK_SCHEMA = {
    "title": {"required": True, "type": "string"},
    "author": {"required": True, "type": "string"},
    "publication_year": {"required": True, "type": "integer"},
    "subject": {"required": True, "type": "array"},
}


def book_payload(book, barcode, subjects=("epic", "poetry"), staff=None) -> dict:
    return {**auth(staff), **book, "book_schema": BOOK_SCHEMA,
            "book_fields": {**book, "subject": list(subjects), "state": "REGISTERED"},
            "barcode": barcode,
            "copy_fields": {"barcode": barcode, "state": "REGISTERED", **book}}


class Run:
    """One dispatched workflow, and the store state it left behind."""

    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root = snapshot, data_root

    def __call__(self, wf: str, payload: dict):
        return api.run_workflow(wf_fqdn=NS + wf, payload=payload,
                                snapshot_root=str(self.snapshot), data_root=str(self.data_root))

    def store(self, name: str) -> dict:
        path = self.data_root / STORE / name
        return json.loads(path.read_text()) if path.is_file() else {}

    def trail(self) -> list[dict]:
        path = self.data_root / STORE / "catalog_operations.jsonl"
        if not path.is_file():
            return []
        return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def main() -> int:
    args = sys.argv[1:]
    keep: Path | None = None
    if "--data-root" in args:
        i = args.index("--data-root")
        if i + 1 >= len(args):
            print("--data-root needs a path")
            return 1
        keep = Path(args[i + 1]).expanduser()
        del args[i:i + 2]

    snapshot = Path(args[0]) if args else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1

    if keep is None:
        data_root = Path(tempfile.mkdtemp(prefix="pgc_catalog_validation_"))
    else:
        # Refused rather than emptied: the caller named this directory, and deleting what is in it
        # is not this script's decision to make.
        # Only this suite's own stores must be absent. One data root holds every domain, each under
        # its own name, so refusing a non-empty root would force a root per suite — and a domain's
        # records would then exist in more than one of them.
        own = keep / STORE
        if own.exists() and any(own.iterdir()):
            print(f"{own} is not empty — this run accumulates state and must start from no stores "
                  f"of its own.\nRemove that directory, or name a root without one.")
            return 1
        keep.mkdir(parents=True, exist_ok=True)
        data_root = keep

    run = Run(snapshot, data_root)
    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    try:
        # 1 — a book is registered with its first copy, and the catalog holds one record for it
        r = run("WF_REGISTER_BOOK_V0", book_payload(ODYSSEY, "BC-0001"))
        books = run.store("books.json")
        check("register a book with at least one copy; exactly one record results",
              r.status == "SUCCESS" and len(books) == 1,
              f"status {r.status}, {len(books)} book record(s)")
        check("the copy registered with the book is recorded",
              len(run.store("physical_copies.json")) == 1,
              f"{len(run.store('physical_copies.json'))} copy record(s)")

        # 2 — the same three identifying attributes are refused
        r = run("WF_REGISTER_BOOK_V0", book_payload(ODYSSEY, "BC-0002"))
        check("a registration matching title, author and publication year is refused",
              r.status != "SUCCESS" and len(run.store("books.json")) == 1,
              f"status {r.status}")

        # 2b — case and spacing do not make a different book
        variant = {"title": "  the   odyssey ", "author": "HOMER", "publication_year": 1614}
        r = run("WF_REGISTER_BOOK_V0", book_payload(variant, "BC-0003"))
        check("case and spacing do not produce a second record",
              r.status != "SUCCESS" and len(run.store("books.json")) == 1,
              f"status {r.status}")

        # 3, 4 — a registration missing a copy or a subject is refused
        no_copy = book_payload(ILIAD, "BC-0010")
        no_copy["barcode"] = ""
        no_copy["copy_fields"] = {}
        r = run("WF_REGISTER_BOOK_V0", no_copy)
        check("a registration offering no physical copy is refused", r.status != "SUCCESS",
              f"status {r.status}")

        r = run("WF_REGISTER_BOOK_V0", book_payload(ILIAD, "BC-0011", subjects=()))
        check("a registration carrying no subject is refused", r.status != "SUCCESS",
              f"status {r.status}")

        # 5 — a further copy against a registered book, recorded against that book only
        second = auth() | {"identity_key": "the odyssey|homer|1614", "barcode": "BC-0004",
                           "copy_fields": {"barcode": "BC-0004", "state": "REGISTERED",
                                           **ODYSSEY}}
        r = run("WF_REGISTER_PHYSICAL_COPY_V0", second)
        copies = run.store("physical_copies.json")
        check("a further copy is registered against the book", r.status == "SUCCESS" and len(copies) == 2,
              f"status {r.status}, {len(copies)} copy record(s)")

        # 6 — a barcode the library already owns is refused
        r = run("WF_REGISTER_PHYSICAL_COPY_V0", second)
        check("a copy registration duplicating an owned barcode is refused",
              r.status != "SUCCESS" and len(run.store("physical_copies.json")) == 2,
              f"status {r.status}")

        # 7 — an unauthorized staff member performs nothing
        # "Performs nothing" is a statement about what this call changed, not about how many records
        # the scenarios before it happened to leave. Counting from a literal made the criterion fail
        # whenever an earlier scenario legitimately added a record.
        before = run.store("books.json")
        r = run("WF_REGISTER_BOOK_V0", book_payload(ILIAD, "BC-0020", staff=INTRUDER))
        check("an unauthorized staff member cannot perform an operation",
              r.status != "SUCCESS" and run.store("books.json") == before,
              f"status {r.status}, catalog {'unchanged' if run.store('books.json') == before else 'changed'}")

        ODYSSEY_KEY = "the odyssey|homer|1614"

        # 8 — bibliographic information is updated, and a later retrieval returns the new version
        r = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", auth() | {
            **ODYSSEY, "identity_key": ODYSSEY_KEY,
            "updated_fields": {**ODYSSEY, "subject": ["epic", "poetry", "greek"],
                               "state": "REGISTERED"}})
        updated = run.store("books.json").get(ODYSSEY_KEY, {})
        check("an update is recorded, and a later read returns the updated version",
              r.status == "SUCCESS" and "greek" in (updated.get("subject") or []),
              f"status {r.status}, subject {updated.get('subject')}")

        # 9 — a search by subject finds the book; a search by title finds it too
        # What the search must return is every registered book carrying a subject, which is a
        # question for the store rather than a number written here: the scenarios above leave a
        # varying set behind, and a literal count asserts their history instead of the search.
        r = run("WF_SEARCH_CATALOG_V0", auth() | {"search_criteria": {"subject": "present",
                                                                     "state": "REGISTERED"}})
        found = (r.surface or {}).get("matching_books") or []
        with_subject = [b for b in run.store("books.json").values()
                        if b.get("state") == "REGISTERED" and b.get("subject") is not None]
        check("a search by subject locates registered books of that kind",
              r.status == "SUCCESS" and len(found) == len(with_subject),
              f"status {r.status}, {len(found)} match(es) against {len(with_subject)} registered")

        r = run("WF_SEARCH_CATALOG_V0", auth() | {
            "search_criteria": {"title": "The Odyssey", "state": "REGISTERED"}})
        by_title = (r.surface or {}).get("matching_books") or []
        check("a search by title locates a registered book by name",
              r.status == "SUCCESS" and len(by_title) == 1,
              f"status {r.status}, {len(by_title)} match(es)")
        check("a search returns bibliographic information and nothing about copies",
              all("barcode" not in b for b in by_title), f"{len(by_title)} match(es) inspected")

        # 10 — complete details include the copies the library holds
        r = run("WF_RETRIEVE_BOOK_DETAILS_V0", auth() | {"identity_key": ODYSSEY_KEY})
        surface = r.surface or {}
        check("complete details are retrieved, including the copies held",
              r.status == "SUCCESS" and len(surface.get("copies_held") or []) == 2,
              f"status {r.status}, {len(surface.get('copies_held') or [])} copy/copies")

        # 11 — retiring a copy leaves the book record alone
        r = run("WF_RETIRE_PHYSICAL_COPY_V0", auth() | {"barcode": "BC-0004"})
        copies = run.store("physical_copies.json")
        check("a copy is retired, and the book record is unaffected",
              r.status == "SUCCESS" and copies.get("BC-0004", {}).get("state") == "RETIRED"
              and run.store("books.json")[ODYSSEY_KEY]["state"] == "REGISTERED",
              f"status {r.status}, copy {copies.get('BC-0004', {}).get('state')}")

        # 12 — and reinstating it puts it back
        r = run("WF_REINSTATE_PHYSICAL_COPY_V0", auth() | {"barcode": "BC-0004"})
        check("a retired copy is returned to the registered state",
              r.status == "SUCCESS"
              and run.store("physical_copies.json")["BC-0004"]["state"] == "REGISTERED",
              f"status {r.status}")

        # 13 — retiring the book leaves its copies alone
        r = run("WF_RETIRE_BOOK_RECORD_V0", auth() | {"identity_key": ODYSSEY_KEY})
        books, copies = run.store("books.json"), run.store("physical_copies.json")
        check("a book is retired, and its physical copies are unaffected",
              r.status == "SUCCESS" and books[ODYSSEY_KEY]["state"] == "RETIRED"
              and all(c["state"] == "REGISTERED" for c in copies.values()),
              f"status {r.status}, book {books[ODYSSEY_KEY]['state']}")

        # 14 — a retired book is out of search, and still retrievable
        r = run("WF_SEARCH_CATALOG_V0", auth() | {
            "search_criteria": {"title": "The Odyssey", "state": "REGISTERED"}})
        check("a retired book does not appear in search results",
              not ((r.surface or {}).get("matching_books") or []),
              f"{len((r.surface or {}).get('matching_books') or [])} match(es)")

        r = run("WF_RETRIEVE_BOOK_DETAILS_V0", auth() | {"identity_key": ODYSSEY_KEY})
        check("a retired book's details can still be retrieved", r.status == "SUCCESS",
              f"status {r.status}")

        # 15 — a copy may be registered against a retired book
        r = run("WF_REGISTER_PHYSICAL_COPY_V0", auth() | {
            "identity_key": ODYSSEY_KEY, "barcode": "BC-0005",
            "copy_fields": {"barcode": "BC-0005", "state": "REGISTERED", **ODYSSEY}})
        check("a copy is registered against a retired book",
              r.status == "SUCCESS" and "BC-0005" in run.store("physical_copies.json"),
              f"status {r.status}")

        # 16 — and reinstating the book puts it back in search
        r = run("WF_REINSTATE_BOOK_RECORD_V0", auth() | {"identity_key": ODYSSEY_KEY})
        reinstated = r.status == "SUCCESS"
        r = run("WF_SEARCH_CATALOG_V0", auth() | {
            "search_criteria": {"title": "The Odyssey", "state": "REGISTERED"}})
        check("a retired book is returned to registered and appears in search again",
              reinstated and len((r.surface or {}).get("matching_books") or []) == 1,
              f"reinstated {reinstated}, {len((r.surface or {}).get('matching_books') or [])} match(es)")

        # 17 — an update that would duplicate another registered book is refused
        run("WF_REGISTER_BOOK_V0", book_payload(ILIAD, "BC-0100"))
        r = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", auth() | {
            **ODYSSEY, "identity_key": "the iliad|homer|1611",
            "updated_fields": {**ODYSSEY, "subject": ["epic"], "state": "REGISTERED"}})
        check("an update that would duplicate another registered book is refused",
              r.status != "SUCCESS", f"status {r.status}")

        # 18 — every performed operation is on the audit trail
        trail = run.trail()
        check("every performed operation is traceable afterwards", len(trail) >= 12,
              f"{len(trail)} trail entr(ies)")

    finally:
        if keep is None:
            shutil.rmtree(data_root, ignore_errors=True)

    width = max(len(c) for c, _, _ in results)
    print(f"execution validation — {len(results)} criteria, snapshot {snapshot}\n")
    for criterion, held, detail in results:
        print(f"  {'PASS' if held else 'FAIL'}  {criterion:<{width}}   {detail}")
    passed = sum(1 for _, held, _ in results if held)
    print(f"\n  {passed}/{len(results)} criteria hold")

    if keep is not None:
        print(f"\n  stores kept at {data_root / STORE}")
        for path in sorted((data_root / STORE).glob("*")):
            print(f"    {path.name:<28} {_describe(path)}")
    return 0 if passed == len(results) else 1


def _describe(path: Path) -> str:
    """How many records a store holds, whichever shape it was written in.

    `CS_MUTABLE_JSON_V0` writes one JSON object keyed by store key; `CS_REGISTRY_V0` and
    `CS_APPENDONLY_JSONL_V0` write JSON Lines. The extensions say so, but nothing enforces the
    correspondence — a design may name a JSONL store `.json` and no rule refuses it, which this
    catalog did until it was caught. Parse, and fall back to counting lines: the content decides.
    """
    text = path.read_text()
    try:
        loaded = json.loads(text)
    except json.JSONDecodeError:
        lines = [l for l in text.splitlines() if l.strip()]
        return f"{len(lines)} entr{'y' if len(lines) == 1 else 'ies'} (json lines)"
    return f"{len(loaded)} record(s)"


if __name__ == "__main__":
    raise SystemExit(main())
