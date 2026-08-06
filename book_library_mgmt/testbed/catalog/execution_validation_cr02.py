"""Execution validation for CR-2 — the catalog run against the criteria the edition change declared.

`execution_validation.py` runs CR-1's criteria and proves this change broke nothing. It cannot prove
this change *did* anything: every one of its twenty-three criteria was satisfied before the work
existed. This runs CR-2's own §15 — editions grouped under a work, a further edition registered
against a work the catalog already holds, a search that answers once per work, a retrieval that
carries the work — and the promise that cost the most to state, which is about data rather than
behaviour.

**The existing-records promise is tested against a record this change did not write.** At P2 the
belief that records written under the previous change exist and are readable came back
INSUFFICIENT_EVIDENCE, because a sealed snapshot declares stores and never their contents. The only
way to settle it is to put a pre-change record in the store and operate on it, which is what §3 does:
a book record with no work, exactly as the previous catalog wrote one, seeded straight into the data
root before any workflow runs. If the extended catalog cannot serve that record, the change did not
keep its promise, however green everything upstream is.

State accumulates deliberately and the run is not idempotent, so it starts from an empty data root.

Run:  python business_domains/book_library_mgmt/testbed/catalog/execution_validation_cr02.py [snapshot]
      ... --data-root <path>     keep the stores instead of discarding them
Exit: 0 if every criterion holds, 1 otherwise.
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

RULES = [{"field": "staff_id", "op": "not_null"}, {"field": "authorized", "op": "eq", "value": True}]
STAFF = {"staff_id": "s-101", "authorized": True}


def auth(staff=None) -> dict:
    return {"staff_credentials": staff or STAFF, "authorization_rules": RULES,
            "staff_id": (staff or STAFF)["staff_id"]}


# One work, three editions: the case the library complained about seeing three times in a search.
DUNE_1965 = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1965}
DUNE_1984 = {"title": "Dune", "author": "Frank Herbert", "publication_year": 1984}
DUNE_2005 = {"title": "Dune", "author": "Frank Herbert", "publication_year": 2005}

WORK_KEY = "dune|frank herbert"

# The record the previous change would have written: no work, because there were no works.
LEGACY = {"title": "Emma", "author": "Jane Austen", "publication_year": 1815}
LEGACY_KEY = "emma|jane austen|1815"

BOOK_SCHEMA = {
    "title": {"required": True, "type": "string"},
    "author": {"required": True, "type": "string"},
    "publication_year": {"required": True, "type": "integer"},
    "subject": {"required": True, "type": "array"},
}
WORK_SCHEMA = {"title": {"required": True, "type": "string"},
               "author": {"required": True, "type": "string"}}


def book_payload(book, barcode, subjects=("science fiction",), staff=None) -> dict:
    """A registration through the existing entry point — unchanged from what CR-1's callers send."""
    return {**auth(staff), **book, "book_schema": BOOK_SCHEMA,
            "book_fields": {**book, "subject": list(subjects), "state": "REGISTERED"},
            "barcode": barcode,
            "copy_fields": {"barcode": barcode, "state": "REGISTERED", **book}}


def edition_payload(book, subjects=("science fiction",), staff=None) -> dict:
    """A further edition of a work the catalog already holds."""
    return {**auth(staff), **book,
            "subject": list(subjects),
            "edition_schema": BOOK_SCHEMA, "work_schema": WORK_SCHEMA,
            "edition_fields": {**book, "subject": list(subjects), "state": "REGISTERED"},
            "work_fields": {"title": book["title"], "author": book["author"]}}


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

    def seed_legacy_record(self) -> None:
        """Write a record the way the previous change wrote one, before anything runs.

        No work key, because the previous catalog had no works. This is the whole of the
        existing-records promise: not that the catalog compiles, but that a record already on disk is
        still served by every operation the library had.
        """
        catalog = self.data_root / STORE
        catalog.mkdir(parents=True, exist_ok=True)
        (catalog / "books.json").write_text(json.dumps({
            LEGACY_KEY: {**LEGACY, "identity_key": LEGACY_KEY,
                         "subject": ["romance"], "state": "REGISTERED"},
        }, indent=2))
        (catalog / "physical_copies.json").write_text(json.dumps({
            "BC-LEGACY": {"barcode": "BC-LEGACY", "identity_key": LEGACY_KEY,
                          "state": "REGISTERED", **LEGACY},
        }, indent=2))
        (catalog / "book_identity_registry.jsonl").write_text(json.dumps({
            "key": LEGACY_KEY, "address": "ADDR_legacy_emma",
            "target_cs": "CS_MUTABLE_JSON_V0", "target_ref": "BOOKS"}) + "\n")


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
        data_root = Path(tempfile.mkdtemp(prefix="pgc_cr02_validation_"))
    else:
        if keep.exists() and any(keep.iterdir()):
            print(f"{keep} is not empty — this run accumulates state and must start from an empty "
                  f"root.\nRemove it, or name a path that does not exist yet.")
            return 1
        keep.mkdir(parents=True, exist_ok=True)
        data_root = keep

    run = Run(snapshot, data_root)
    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    try:
        # A pre-change record is on disk before anything runs, exactly as the library's would be.
        run.seed_legacy_record()

        # 1 — a work enters the catalog with the edition that evidences it
        r = run("WF_REGISTER_BOOK_V0", book_payload(DUNE_1965, "BC-0001"))
        works, books = run.store("works.json"), run.store("books.json")
        check("registering an edition of an unheld work creates the work and the edition",
              r.status == "SUCCESS" and WORK_KEY in works and len(books) == 2,
              f"status {r.status}, {len(works)} work(s), {len(books)} edition(s)")

        # 2 — the edition record names the work it belongs to
        check("the edition record carries the work it belongs to",
              books.get(_key(DUNE_1965), {}).get("work_key") == WORK_KEY,
              f"work_key {books.get(_key(DUNE_1965), {}).get('work_key')!r}")

        # 3 — a further edition of a work the catalog already holds
        r = run("WF_REGISTER_ADDITIONAL_EDITION_V0", edition_payload(DUNE_1984))
        works, books = run.store("works.json"), run.store("books.json")
        check("an additional edition of an existing work is registered",
              r.status == "SUCCESS" and _key(DUNE_1984) in books,
              f"status {r.status}")
        check("the additional edition joins the work rather than creating another",
              len(works) == 1 and books[_key(DUNE_1984)]["work_key"] == WORK_KEY,
              f"{len(works)} work(s)")

        # 4 — and a third, so a search has three editions to answer once for
        r = run("WF_REGISTER_ADDITIONAL_EDITION_V0", edition_payload(DUNE_2005))
        books = run.store("books.json")
        editions = [b for b in books.values() if b.get("work_key") == WORK_KEY]
        check("three editions of one work are held, grouped under one work",
              r.status == "SUCCESS" and len(editions) == 3 and len(run.store("works.json")) == 1,
              f"{len(editions)} edition(s), {len(run.store('works.json'))} work(s)")

        # 5 — a registration repeating an edition's identity is refused
        r = run("WF_REGISTER_ADDITIONAL_EDITION_V0", edition_payload(DUNE_1984))
        check("a registration repeating an edition's identity is refused",
              r.status != "SUCCESS" and len(run.store("books.json")) == 4,
              f"status {r.status}, {len(run.store('books.json'))} edition(s)")

        # 6 — search answers once per work, not once per edition
        r = run("WF_SEARCH_CATALOG_V0", auth() | {
            "search_criteria": {"title": "Dune", "state": "REGISTERED"}})
        groups = _groups(r.surface)
        check("a search for a work with three editions returns one result, not three",
              r.status == "SUCCESS" and len(groups) == 1,
              f"status {r.status}, {len(groups)} result(s)")

        # 7 — and the one result carries the editions to choose between
        members = groups[0].get("records", []) if groups else []
        check("the search result carries the work's editions to choose from",
              len(members) == 3 and {m.get("publication_year") for m in members} ==
              {1965, 1984, 2005},
              f"{len(members)} edition(s) in the result")

        # 8 — an edition registered as a further edition holds no copy until one is registered,
        #     and the catalog must still be able to answer about it
        r = run("WF_RETRIEVE_BOOK_DETAILS_V0", auth() | {"identity_key": _key(DUNE_1984)})
        check("an edition holding no copies is still retrievable",
              r.status == "SUCCESS",
              f"status {r.status} — a further edition requires no copy, so this is reachable")

        # 9 — a copy belongs to the edition it was registered against
        r = run("WF_REGISTER_PHYSICAL_COPY_V0", auth() | DUNE_1984 | {
            "barcode": "BC-0002", "identity_key": _key(DUNE_1984),
            "copy_fields": {"barcode": "BC-0002", "state": "REGISTERED", **DUNE_1984}})
        copies = run.store("physical_copies.json")
        check("a physical copy is registered against exactly one edition",
              r.status == "SUCCESS"
              and copies.get("BC-0002", {}).get("identity_key") == _key(DUNE_1984),
              f"status {r.status}")

        # 9b — retrieval answers about one edition, its copies, and the work it belongs to
        r = run("WF_RETRIEVE_BOOK_DETAILS_V0", auth() | {"identity_key": _key(DUNE_1984)})
        surface = r.surface or {}
        check("an edition's complete details are retrieved, with the copies held",
              r.status == "SUCCESS" and (surface.get("book_record") or {}).get("publication_year")
              == 1984 and len(surface.get("copies_held") or []) == 1,
              f"status {r.status}, {len(surface.get('copies_held') or [])} copy/copies")
        check("the retrieval carries the work the edition belongs to",
              (surface.get("work_record") or {}).get("title") == "Dune",
              f"work_record {surface.get('work_record')!r}")

        # 10 — retiring one edition leaves the work's other editions alone
        r = run("WF_RETIRE_BOOK_RECORD_V0", auth() | {"identity_key": _key(DUNE_1984)})
        books = run.store("books.json")
        siblings = [b for k, b in books.items()
                    if b.get("work_key") == WORK_KEY and k != _key(DUNE_1984)]
        check("an edition is retired and the work's other editions are unaffected",
              r.status == "SUCCESS" and books[_key(DUNE_1984)]["state"] == "RETIRED"
              and all(b["state"] == "REGISTERED" for b in siblings),
              f"status {r.status}, {len(siblings)} sibling(s) untouched")

        # 11 — a work is never retired, whatever happens to its editions
        check("the work survives its edition's retirement",
              WORK_KEY in run.store("works.json"),
              f"{len(run.store('works.json'))} work(s)")

        # 12 — and the edition comes back
        r = run("WF_REINSTATE_BOOK_RECORD_V0", auth() | {"identity_key": _key(DUNE_1984)})
        check("a retired edition is returned to the registered state",
              r.status == "SUCCESS"
              and run.store("books.json")[_key(DUNE_1984)]["state"] == "REGISTERED",
              f"status {r.status}")

        # --- the existing-records promise: everything below operates on the seeded record ---

        # 13 — a record written before this change is still found by search
        r = run("WF_SEARCH_CATALOG_V0", auth() | {
            "search_criteria": {"title": "Emma", "state": "REGISTERED"}})
        found = [m for g in _groups(r.surface) for m in g.get("records", [])
                 if m.get("identity_key") == LEGACY_KEY]
        check("a record written before this change is found by search, without recreation",
              r.status == "SUCCESS" and len(found) == 1,
              f"status {r.status}, {len(found)} match(es)")

        # 14 — and retrieved in full
        r = run("WF_RETRIEVE_BOOK_DETAILS_V0", auth() | {"identity_key": LEGACY_KEY})
        surface = r.surface or {}
        check("a record written before this change is retrieved in full, without recreation",
              r.status == "SUCCESS"
              and (surface.get("book_record") or {}).get("title") == "Emma",
              f"status {r.status}")

        # 15 — and updated
        r = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", auth() | {
            "identity_key": LEGACY_KEY,
            "updated_fields": {**LEGACY, "subject": ["romance", "classic"],
                               "state": "REGISTERED"}})
        check("a record written before this change can be updated",
              r.status == "SUCCESS"
              and run.store("books.json")[LEGACY_KEY]["subject"] == ["romance", "classic"],
              f"status {r.status}")

        # 16 — and retired
        r = run("WF_RETIRE_BOOK_RECORD_V0", auth() | {"identity_key": LEGACY_KEY})
        check("a record written before this change can be retired",
              r.status == "SUCCESS" and run.store("books.json")[LEGACY_KEY]["state"] == "RETIRED",
              f"status {r.status}")

        # 17 — and reinstated
        r = run("WF_REINSTATE_BOOK_RECORD_V0", auth() | {"identity_key": LEGACY_KEY})
        check("a record written before this change can be reinstated",
              r.status == "SUCCESS"
              and run.store("books.json")[LEGACY_KEY]["state"] == "REGISTERED",
              f"status {r.status}")

        # 18 — every operation this change performed is in the trail
        trail = run.trail()
        performed = {_op(e) for e in trail}
        check("every business operation performed is traceable afterwards",
              "REGISTER_ADDITIONAL_EDITION" in performed
              and {"REGISTER_BOOK", "SEARCH_CATALOG", "REGISTER_PHYSICAL_COPY",
                   "UPDATE_BIBLIOGRAPHIC_INFORMATION"} <= performed,
              f"{len(trail)} trail entr(ies), {len(performed)} distinct operation(s)")

    finally:
        if keep is None:
            shutil.rmtree(data_root, ignore_errors=True)

    width = max(len(c) for c, _, _ in results)
    print()
    for criterion, held, detail in results:
        print(f"  {'PASS' if held else 'FAIL'}  {criterion:<{width}}   {detail}")
    passed = sum(1 for _, held, _ in results if held)
    print(f"\n  {passed}/{len(results)} criteria hold")

    if keep is not None:
        print(f"\n  stores kept at {data_root / STORE}")
    return 0 if passed == len(results) else 1


def _key(book: dict) -> str:
    """The identity the catalog forms for an edition, as the transform forms it."""
    return "|".join((book["title"].casefold(), book["author"].casefold(),
                     str(book["publication_year"])))


def _groups(surface) -> list[dict]:
    """The work-level results a search returns."""
    surface = surface or {}
    for field in ("matching_works", "grouped", "matching_books"):
        value = surface.get(field)
        if isinstance(value, list):
            return value
    return []


def _op(entry: dict) -> str:
    record = entry.get("record", entry)
    return record.get("operation", "")


if __name__ == "__main__":
    raise SystemExit(main())
