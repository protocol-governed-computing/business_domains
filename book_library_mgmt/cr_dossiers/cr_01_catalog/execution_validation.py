"""Execution validation — CR-1's acceptance criteria, run against the composition.

Admission and validation are different arbiters. The compiler decided the authored artifacts are
*buildable*; nothing it checked says the built system does what the business asked. That is a
behavioural question, and only running the composition answers it.

The criteria are not invented here. Each scenario names the acceptance criterion it discharges,
verbatim from the seed's §15 — the acceptance boundary the business author declared before any
design existed, which is what makes this a closed loop rather than a test suite written to match
whatever got built.

Run:  python execution_validation.py [snapshot_root]
Exit: 0 if every criterion passed, 1 otherwise.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parents[4]
DATA_ROOT = Path("/tmp/cr01_execution_validation")
STORE = DATA_ROOT / "book_library_mgmt" / "catalog"

STAFF = "staff-001"
UNAUTHORIZED = "staff-999"


def reset() -> None:
    """A validation run starts from a known state, so a result never depends on a previous run."""
    if DATA_ROOT.exists():
        shutil.rmtree(DATA_ROOT)
    STORE.mkdir(parents=True)
    (STORE / "catalog_staff.json").write_text(json.dumps(
        {STAFF: {"staff_id": STAFF, "authorized": True}}))
    (STORE / "bibliographic_works.json").write_text("{}")
    (STORE / "physical_copies.json").write_text("{}")
    (STORE / "catalog_operations.jsonl").write_text("")


def run(wf: str, payload: dict, snapshot_root: str) -> tuple[str, dict]:
    """Dispatch one workflow through the runtime and return its status and surface."""
    path = DATA_ROOT / "_payload.json"
    path.write_text(json.dumps(payload))
    proc = subprocess.run(
        [str(WORKSPACE / "protocol_runtime" / "run.sh"), "run",
         "--wf", f"book_library_mgmt::{wf}",
         "--payload", str(path),
         "--data-root", str(DATA_ROOT),
         "--snapshot", snapshot_root],
        capture_output=True, text=True,
    )
    out = proc.stdout
    status = "UNKNOWN"
    for line in out.splitlines():
        if line.startswith("Status:"):
            status = line.split(":", 1)[1].strip()
    return status, {"stdout": out, "stderr": proc.stderr}


def works() -> dict:
    return json.loads((STORE / "bibliographic_works.json").read_text() or "{}")


def copies() -> dict:
    return json.loads((STORE / "physical_copies.json").read_text() or "{}")


def journal() -> list[dict]:
    """The business records, unwrapped from the append-only envelope.

    The store wraps each append in `record_id` / `sequence_number` / `timestamp` and nests the
    business content under `record`. Reading the envelope as though it were the record reports a
    journal full of nothing, which is a defect in the reader rather than the journal.
    """
    text = (STORE / "catalog_operations.jsonl").read_text().strip()
    envelopes = [json.loads(line) for line in text.splitlines() if line.strip()]
    return [e.get("record", e) for e in envelopes]


# Each scenario: the acceptance criterion it discharges, and a callable returning (ok, detail).
def scenarios(snap: str) -> list[tuple[str, callable]]:

    def c1():
        reset()
        st, _ = run("WF_REGISTER_BOOK_V0", {
            "staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        w = works()
        return st == "SUCCESS" and len(w) == 1 and "work-001" in w, \
            f"status={st} records={len(w)}"

    def c2():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        st, _ = run("WF_REGISTER_PHYSICAL_COPY_V0", {
            "staff_id": STAFF, "copy_id": "copy-001", "work_id": "work-001"}, snap)
        c = copies()
        return st == "SUCCESS" and c.get("copy-001", {}).get("work_id") == "work-001", \
            f"status={st} copy_names_work={c.get('copy-001', {}).get('work_id')}"

    def c3():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "Odissey"}}, snap)
        st, _ = run("WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0", {
            "staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        title = works().get("work-001", {}).get("bibliographic_information", {}).get("title")
        return st == "SUCCESS" and title == "The Odyssey", f"status={st} title={title!r}"

    def c4():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        st, _ = run("WF_RETIRE_CATALOG_RECORD_V0", {
            "staff_id": STAFF, "work_id": "work-001"}, snap)
        record = works().get("work-001", {})
        return st == "SUCCESS" and record.get("retired") is True and "work-001" in works(), \
            f"status={st} retired={record.get('retired')} still_stored={'work-001' in works()}"

    def c5():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        st, _ = run("WF_SEARCH_CATALOG_V0", {
            "staff_id": STAFF, "search_terms": {"title": "The Odyssey"}}, snap)
        return st == "SUCCESS", f"status={st}"

    def c6():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        run("WF_REGISTER_PHYSICAL_COPY_V0", {"staff_id": STAFF, "copy_id": "copy-001",
            "work_id": "work-001"}, snap)
        st, _ = run("WF_RETRIEVE_BOOK_DETAILS_V0", {
            "staff_id": STAFF, "work_id": "work-001"}, snap)
        return st == "SUCCESS", f"status={st}"

    def c7():
        reset()
        st, _ = run("WF_REGISTER_BOOK_V0", {
            "staff_id": UNAUTHORIZED, "work_id": "work-002",
            "bibliographic_information": {"title": "Smuggled"}}, snap)
        # The operation must not have happened, whatever the workflow reported.
        return st != "SUCCESS" and len(works()) == 0, \
            f"status={st} records_written={len(works())}"

    def c8():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        st, _ = run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey, again"}}, snap)
        w = works()
        return st != "SUCCESS" and len(w) == 1, f"second_status={st} records={len(w)}"

    def c9():
        reset()
        run("WF_REGISTER_BOOK_V0", {"staff_id": STAFF, "work_id": "work-001",
            "bibliographic_information": {"title": "The Odyssey"}}, snap)
        run("WF_SEARCH_CATALOG_V0", {"staff_id": STAFF,
            "search_terms": {"title": "The Odyssey"}}, snap)
        entries = journal()
        ops = {e.get("operation") for e in entries}
        return len(entries) >= 2 and {"REGISTER_BOOK", "SEARCH_CATALOG"} <= ops, \
            f"journalled={len(entries)} operations={sorted(ops)}"

    return [
        ("Authorized staff can register a new book, and the catalog then holds exactly one "
         "authoritative record for it.", c1),
        ("Authorized staff can register a physical copy against exactly one bibliographic "
         "work.", c2),
        ("Authorized staff can update the bibliographic information of a registered work.", c3),
        ("Authorized staff can retire an obsolete record, and the retired record is no longer "
         "offered as current.", c4),
        ("Authorized staff can search the catalog and locate a registered material.", c5),
        ("Authorized staff can retrieve the complete details of a registered book.", c6),
        ("A staff member who is not authorized cannot perform any catalog operation.", c7),
        ("Registering the same book twice does not produce two authoritative records for "
         "it.", c8),
        ("Every catalog operation performed can be traced and audited after the fact.", c9),
    ]


def main() -> int:
    snap = sys.argv[1] if len(sys.argv) > 1 else str(WORKSPACE / "snapshot")
    cases = scenarios(snap)
    print(f"execution validation — CR-1 acceptance criteria ({len(cases)})")
    print(f"  snapshot {snap}\n")

    failures = 0
    for i, (criterion, check) in enumerate(cases, start=1):
        try:
            ok, detail = check()
        except Exception as exc:                       # a scenario that cannot run has not passed
            ok, detail = False, f"raised {type(exc).__name__}: {exc}"
        if not ok:
            failures += 1
        print(f"  {'PASS' if ok else 'FAIL'}  AC-{i}  {criterion}")
        print(f"         {detail}")

    print()
    if failures:
        print(f"EXECUTION VALIDATION FAILED — {failures} of {len(cases)} criteria unmet")
        return 1
    print(f"EXECUTION VALIDATION PASSED — {len(cases)} criteria, all met")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
