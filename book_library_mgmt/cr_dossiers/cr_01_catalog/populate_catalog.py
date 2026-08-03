"""Populate a working catalog by running the real workflows, and show what persisted.

`execution_validation.py` proves each acceptance criterion in isolation and resets between them, so
it never leaves a catalog anyone can look at. This drives the same governed workflows with a small
made-up collection and then prints the stores, which is the only way to see what the composition
actually holds rather than what it reports.

Nothing here writes a store directly except the staff register. Authorization is **read, never
granted** — CR-1 deferred granting to a `patron` subdomain that does not exist yet, so seeding the
staff store stands in for the subdomain that will own it. Every other byte in these files was
written by a workflow.

Run:  python populate_catalog.py [snapshot_root] [data_root]
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[4]

LIBRARIAN = "staff-001"
ASSISTANT = "staff-002"
VOLUNTEER = "staff-777"          # never authorized — every attempt must be refused

WORKS = [
    ("work-001", "The Odyssey", "Homer", 1614, ["epic", "poetry"]),
    ("work-002", "One Hundred Years of Solitude", "Gabriel García Márquez", 1967, ["fiction"]),
    ("work-003", "The Left Hand of Darkness", "Ursula K. Le Guin", 1969, ["science fiction"]),
    ("work-004", "Things Fall Apart", "Chinua Achebe", 1958, ["fiction"]),
    ("work-005", "The Master and Margarita", "Mikhail Bulgakov", 1967, ["fiction", "satire"]),
    ("work-006", "A Field Guide to Bewilderment", "Anonymous", 1901, ["reference"]),
]

# Several works hold more than one copy; one holds none, because a catalogued work the library does
# not yet own a copy of is an ordinary state and the stores should be able to show it.
COPIES = [
    ("copy-001", "work-001"), ("copy-002", "work-001"), ("copy-003", "work-001"),
    ("copy-004", "work-002"), ("copy-005", "work-002"),
    ("copy-006", "work-003"),
    ("copy-007", "work-004"), ("copy-008", "work-004"),
    ("copy-009", "work-005"),
]


def store(data_root: Path) -> Path:
    return data_root / "book_library_mgmt" / "catalog"


def reset(data_root: Path) -> None:
    if data_root.exists():
        shutil.rmtree(data_root)
    s = store(data_root)
    s.mkdir(parents=True)
    (s / "catalog_staff.json").write_text(json.dumps({
        LIBRARIAN: {"staff_id": LIBRARIAN, "authorized": True},
        ASSISTANT: {"staff_id": ASSISTANT, "authorized": True},
        VOLUNTEER: {"staff_id": VOLUNTEER, "authorized": False},
    }, indent=2))
    (s / "bibliographic_works.json").write_text("{}")
    (s / "physical_copies.json").write_text("{}")
    (s / "catalog_operations.jsonl").write_text("")


def run(wf: str, payload: dict, snapshot_root: str, data_root: Path) -> str:
    path = data_root / "_payload.json"
    path.write_text(json.dumps(payload))
    proc = subprocess.run(
        [str(WORKSPACE / "protocol_runtime" / "run.sh"), "run",
         "--wf", f"book_library_mgmt::{wf}",
         "--payload", str(path),
         "--data-root", str(data_root),
         "--snapshot", snapshot_root],
        capture_output=True, text=True,
    )
    for line in proc.stdout.splitlines():
        if line.startswith("Status:"):
            return line.split(":", 1)[1].strip()
    return "UNKNOWN"


def main() -> int:
    snapshot_root = sys.argv[1] if len(sys.argv) > 1 else str(WORKSPACE / "snapshot")
    data_root = Path(sys.argv[2]) if len(sys.argv) > 2 else WORKSPACE / "data" / "book_library_mgmt"
    reset(data_root)
    s = store(data_root)

    print(f"populating catalog\n  snapshot  {snapshot_root}\n  data root {data_root}\n")

    for work_id, title, author, year, subjects in WORKS:
        st = run("WF_REGISTER_BOOK_V0", {
            "staff_id": LIBRARIAN, "work_id": work_id,
            "bibliographic_information": {"title": title, "author": author,
                                          "year": year, "subjects": subjects},
        }, snapshot_root, data_root)
        print(f"  register  {work_id}  {title[:38]:<38} {st}")

    for copy_id, work_id in COPIES:
        st = run("WF_REGISTER_PHYSICAL_COPY_V0", {
            "staff_id": ASSISTANT, "copy_id": copy_id, "work_id": work_id,
        }, snapshot_root, data_root)
        print(f"  copy      {copy_id} → {work_id}                             {st}")

    st = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", {
        "staff_id": LIBRARIAN, "work_id": "work-001",
        "bibliographic_information": {"title": "The Odyssey", "author": "Homer",
                                      "year": 1614, "subjects": ["epic", "poetry"],
                                      "translator": "George Chapman"},
    }, snapshot_root, data_root)
    print(f"\n  update    work-001 gains a translator                     {st}")

    st = run("WF_RETIRE_CATALOG_RECORD_V0",
             {"staff_id": LIBRARIAN, "work_id": "work-006"}, snapshot_root, data_root)
    print(f"  retire    work-006 is obsolete                            {st}")

    st = run("WF_SEARCH_CATALOG_V0",
             {"staff_id": ASSISTANT, "search_terms": {"subjects": "fiction"}},
             snapshot_root, data_root)
    print(f"  search    subjects=fiction                                {st}")

    st = run("WF_RETRIEVE_BOOK_DETAILS_V0",
             {"staff_id": LIBRARIAN, "work_id": "work-002"}, snapshot_root, data_root)
    print(f"  retrieve  work-002                                        {st}")

    # The refusal path, so the journal can be read against what was attempted.
    st = run("WF_REGISTER_BOOK_V0", {
        "staff_id": VOLUNTEER, "work_id": "work-999",
        "bibliographic_information": {"title": "Unauthorized Addition", "author": "Nobody"},
    }, snapshot_root, data_root)
    print(f"  register  work-999 by an unauthorized volunteer           {st}   ← must refuse")

    st = run("WF_REGISTER_BOOK_V0", {
        "staff_id": LIBRARIAN, "work_id": "work-001",
        "bibliographic_information": {"title": "The Odyssey (duplicate)", "author": "Homer"},
    }, snapshot_root, data_root)
    print(f"  register  work-001 a second time                          {st}   ← must refuse")

    works = json.loads((s / "bibliographic_works.json").read_text() or "{}")
    copies = json.loads((s / "physical_copies.json").read_text() or "{}")
    journal = [json.loads(l) for l in
               (s / "catalog_operations.jsonl").read_text().splitlines() if l.strip()]

    print(f"\n  bibliographic_works.json   {len(works)} record(s)")
    print(f"  physical_copies.json       {len(copies)} record(s)")
    print(f"  catalog_operations.jsonl   {len(journal)} entr(ies)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
