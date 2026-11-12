"""Execution validation — the owner's decisions, delivered as cr_06 to cr_09.

cr_06 derived the catalog's design from its ledger with today's behavior, and three corrections the
ledger has no shape to avoid. cr_07 to cr_09 each deliver one decision of the owner's. Every
criterion below is one of those, read from behavior: answers, announcements and the stores.

Run:  python business_domains/book_library_mgmt/testbed/catalog/execution_validation_owner_decisions.py [snapshot]
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
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation_compilers"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402

NS = "book_library_mgmt::"
STORE = "book_library_mgmt/catalog"
RULES = [{"field": "staff_id", "op": "not_null"}, {"field": "authorized", "op": "eq", "value": True}]
STAFF = {"staff_id": "s-101", "authorized": True}
BOOK_SCHEMA = {
    "title": {"required": True, "type": "string"},
    "author": {"required": True, "type": "string"},
    "publication_year": {"required": True, "type": "integer"},
    "subject": {"required": True, "type": "array"},
}
ODYSSEY = {"title": "The Odyssey", "author": "Homer", "publication_year": 1614}
ILIAD = {"title": "The Iliad", "author": "Homer", "publication_year": 1611}
AENEID = {"title": "The Aeneid", "author": "Virgil", "publication_year": 1697}


def auth() -> dict:
    return {"staff_credentials": STAFF, "authorization_rules": RULES, "staff_id": STAFF["staff_id"]}


def book_payload(book, barcode, subjects=("epic",)) -> dict:
    return {**auth(), **book, "book_schema": BOOK_SCHEMA,
            "book_fields": {**book, "subject": list(subjects), "state": "REGISTERED"},
            "barcode": barcode, "copy_fields": {"barcode": barcode, "state": "REGISTERED", **book}}


def key(book) -> str:
    return "|".join((book["title"].casefold(), book["author"].casefold(), str(book["publication_year"])))


class Outcome:
    def __init__(self, status: str, surface: dict, announced: set[str]):
        self.status, self.surface, self.announced = status, surface or {}, announced


class Run:
    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root = snapshot, data_root

    def __call__(self, wf: str, payload: dict) -> Outcome:
        r = api.run_workflow(wf_fqdn=NS + wf, payload=payload,
                             snapshot_root=str(self.snapshot), data_root=str(self.data_root))
        announced = set()
        for f in sorted(Path(r.trace_dir).glob("*.jsonl")):
            for line in f.read_text().splitlines():
                e = json.loads(line) if line.strip() else {}
                if e.get("event_type") == "EVENT":
                    announced.add(str(e.get("detail", {}).get("ev_fqdn")))
        return Outcome(r.status, r.surface, announced)

    def store(self, name: str) -> dict:
        path = self.data_root / STORE / name
        return json.loads(path.read_text()) if path.is_file() else {}

    def trail(self) -> list[dict]:
        path = self.data_root / STORE / "catalog_operations.jsonl"
        return [json.loads(l) for l in path.read_text().splitlines() if l.strip()] if path.is_file() else []


def found(surface: dict) -> list[dict]:
    """Every book a search answered with, across its groups."""
    for field in ("matching_works", "grouped", "matching_books"):
        value = surface.get(field)
        if isinstance(value, list):
            return [m for g in value for m in (g.get("records") or [g])]
    return []


def announced(r: Outcome, word: str) -> bool:
    return any(word in name for name in r.announced)


def main() -> int:
    snapshot = Path(sys.argv[1]) if len(sys.argv) > 1 else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1
    data_root = Path(tempfile.mkdtemp(prefix="pgc_catalog_owner_decisions_"))
    run = Run(snapshot, data_root)
    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    try:
        run("WF_REGISTER_BOOK_V1", book_payload(ODYSSEY, "BC-0001"))
        run("WF_REGISTER_BOOK_V1", book_payload(ILIAD, "BC-0002"))

        # cr_06 — a transition checks the state it moves from
        run("WF_RETIRE_BOOK_RECORD_V1", auth() | {"identity_key": key(ILIAD)})
        again = run("WF_RETIRE_BOOK_RECORD_V1", auth() | {"identity_key": key(ILIAD)})
        check("cr_06: retiring a book that is already retired is refused",
              again.status != "SUCCESS", f"status {again.status}")

        # cr_06 — the trail names every operation's subject by its identity
        registered = [e for e in run.trail() if "REGISTER_BOOK" in json.dumps(e)]
        check("cr_06: the trail records a registered book under its identity, not its title",
              bool(registered) and any(key(ODYSSEY) in json.dumps(e) for e in registered),
              f"{len(registered)} registration entr(ies)")

        # cr_06 — an update may change a book's identity (P0's rule)
        corrected = {**ODYSSEY, "publication_year": 1616}
        r = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V1", auth() | {
            "identity_key": key(ODYSSEY), "updated_fields": {**corrected, "subject": ["epic"], "state": "REGISTERED"}})
        books = run.store("books.json")
        check("cr_06: correcting a book's publication year moves it to its new identity and frees the old one",
              r.status == "SUCCESS" and key(corrected) in books and key(ODYSSEY) not in books,
              f"status {r.status}")

        # cr_07 — a search never answers with a retired book, and a caller cannot ask it to
        s = run("WF_SEARCH_CATALOG_V3", auth() | {"search_criteria": {"author": "Homer"}})
        retired = [b for b in found(s.surface) if str(b.get("state", "")).upper() == "RETIRED"]
        check("cr_07: a search answers with no retired book",
              s.status == "SUCCESS" and found(s.surface) and not retired,
              f"status {s.status}, {len(found(s.surface))} found, {len(retired)} retired")
        s = run("WF_SEARCH_CATALOG_V3", auth() | {"search_criteria": {"author": "Homer", "state": "RETIRED"}})
        check("cr_07: a search asking for retired books answers with none of them",
              not [b for b in found(s.surface) if str(b.get("state", "")).upper() == "RETIRED"],
              f"status {s.status}, {len(found(s.surface))} found")

        # cr_08 — a search that matches nothing answers with no books
        s = run("WF_SEARCH_CATALOG_V3", auth() | {"search_criteria": {"title": "No Such Title"}})
        check("cr_08: a search that matches nothing answers with no books, and is not refused",
              s.status == "SUCCESS" and not found(s.surface), f"status {s.status}")

        # cr_09 — reinstatement announces, as retirement does
        r = run("WF_REINSTATE_BOOK_RECORD_V2", auth() | {"identity_key": key(ILIAD)})
        check("cr_09: reinstating a book announces that the book was reinstated",
              r.status == "SUCCESS" and announced(r, "BOOK_REINSTATED"), f"status {r.status}, {sorted(r.announced)}")
        run("WF_REGISTER_BOOK_V1", book_payload(AENEID, "BC-0003"))
        run("WF_RETIRE_PHYSICAL_COPY_V1", auth() | {"barcode": "BC-0003"})
        r = run("WF_REINSTATE_PHYSICAL_COPY_V2", auth() | {"barcode": "BC-0003"})
        check("cr_09: reinstating a physical copy announces that the copy was reinstated",
              r.status == "SUCCESS" and announced(r, "PHYSICAL_COPY_REINSTATED"),
              f"status {r.status}, {sorted(r.announced)}")
    finally:
        shutil.rmtree(data_root, ignore_errors=True)

    print(f"execution validation — {len(results)} criteria, snapshot {snapshot}\n")
    for criterion, held, detail in results:
        print(f"  {'OK  ' if held else 'FAIL'}  {criterion}" + (f"  ({detail})" if detail and not held else ""))
    held = sum(1 for _, ok, _ in results if ok)
    print(f"\n  {held}/{len(results)} criteria hold")
    return 0 if held == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())
