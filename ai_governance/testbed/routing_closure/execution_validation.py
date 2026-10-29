"""Execution validation — run the reclaim against its routing-closure criteria.

The change answers one question for the reclaim: what happens when the registry refuses to release
the license. The business answered it: the license stays assigned and active, and no revocation is
announced. The derived reclaim releases the license before it moves it, so a refused release ends
the reclaim there, as rejected, before anything is changed.

Each criterion licenses one employee on a fresh data root through AI licensing's own acts, then
dispatches a real reclaim through `protocol_runtime` and reads back:

- the ending the trace records;
- whether the trace announces anything;
- whether the business still holds the license, assigned and active.

The registry refuses a release only when it is handed no key, and the contract refuses that earlier,
at its own inputs. So criterion 1 stands in for the registry's removal, for that run only, and has
it answer VIOLATION. A license unused for 30 days is stood in by moving every time the business
recorded 40 days back.

Run:  python business_domains/ai_governance/testbed/routing_closure/execution_validation.py [snapshot]
Exit: 0 if every exercised criterion holds, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timedelta
from pathlib import Path

HERE = Path(__file__).resolve()
DOMAIN = HERE.parents[2]
WORKSPACE = DOMAIN.parents[1]

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation_compilers"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from capability_side_effects.implementation.CS_REGISTRY_V0.impl.executor import (  # noqa: E402
    RegistryExecutor)

NS = "ai_governance::"
STORE = "ai_governance/ai_licensing"
EMPLOYEE = "e-7526"
STAMP = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})?")


class Case:
    """One fresh data root, with one employee licensed on it."""

    def __init__(self, snapshot: Path):
        self.snapshot = snapshot
        self.root = Path(tempfile.mkdtemp(prefix="pgc_reclaim_closure_"))
        self.run("WF_SET_LICENSE_CAP_V0", {"cap": 10})
        self.run("WF_REGISTER_EMPLOYEE_V0", {"employee_id": EMPLOYEE})
        self.run("WF_RECORD_TRAINING_COMPLETED_V0", {"employee_id": EMPLOYEE})
        self.run("WF_PROVISION_LICENSE_V0", {"employee_id": EMPLOYEE, "tier": "standard"})

    def run(self, wf: str, body: dict) -> list[dict]:
        result = api.run_workflow(wf_fqdn=NS + wf, payload=body,
                                  snapshot_root=str(self.snapshot), data_root=str(self.root))
        lines: list[dict] = []
        for f in sorted(Path(result.trace_dir).glob("*.jsonl")):
            lines += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
        return lines

    def reclaim(self) -> list[dict]:
        return self.run("WF_RECLAIM_LICENSE_V0", {"employee_id": EMPLOYEE})

    def age(self, days: int) -> None:
        """Stand in a license unused for `days`: move every time the business recorded back."""
        def back(m):
            text = m.group(0)
            moved = (datetime.fromisoformat(text.replace("Z", "+00:00")) - timedelta(days=days)).isoformat()
            return moved.replace("+00:00", "Z") if text.endswith("Z") else moved
        for p in (self.root / STORE).rglob("*"):
            if p.is_file() and p.suffix in (".json", ".jsonl"):
                p.write_text(STAMP.sub(back, p.read_text()))

    def assigned(self) -> bool:
        """Whether the business still holds the employee's license, claimed and active."""
        licenses = json.loads((self.root / STORE / "licenses.json").read_text())
        held = [lic for lic in licenses.values() if lic.get("employee_id") == EMPLOYEE]
        path = self.root / STORE / "license_identity_registry.jsonl"
        claims = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        claimed = {c["key"] for c in claims if not c.get("tombstone")} - {c["key"] for c in claims if c.get("tombstone")}
        return bool(held) and held[0].get("state") == "ACTIVE" and held[0]["license_id"] in claimed

    def close(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


def ending(events: list[dict]) -> str | None:
    routes = [e for e in events if e.get("event_type") == "WF_ROUTE"]
    return routes[-1].get("detail", {}).get("to_node") if routes else None


def announced(events: list[dict]) -> int:
    return sum(e.get("event_type") == "EVENT" for e in events)


def started(events: list[dict]) -> int:
    return sum(e.get("event_type") == "CC_START" for e in events)


def errors(events: list[dict]) -> int:
    return sum(e.get("event_type") == "ERROR" for e in events)


def main() -> int:
    snapshot = Path(sys.argv[1]) if len(sys.argv) > 1 else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1

    results: list[tuple[str, bool | None, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    # 1 — a reclaim the registry refuses leaves the license assigned, and nothing is announced
    c = Case(snapshot)
    c.age(40)
    real = RegistryExecutor.deregister
    RegistryExecutor.deregister = lambda self, payload: {"result_status": "VIOLATION"}
    try:
        ev = c.reclaim()
    finally:
        RegistryExecutor.deregister = real
    try:
        check("a reclaim the registry refuses ends as rejected, the license stays assigned and active, "
              "and no revocation is announced",
              ending(ev) == "EXIT_REJECTED" and c.assigned() and not announced(ev) and not errors(ev),
              f"ending {ending(ev)}, assigned {c.assigned()}, {announced(ev)} announcement(s), "
              f"{errors(ev)} error(s)")
        check("the reclaim stops at the refused release, and nothing after it runs",
              started(ev) == 3, f"contracts started: {started(ev)}")
    finally:
        c.close()

    # 2 — a reclaim the registry does not refuse reclaims the license
    c = Case(snapshot)
    c.age(40)
    try:
        ev = c.reclaim()
        check("a reclaim the registry accepts ends as completed, the license is released, and the "
              "revocation is announced",
              ending(ev) == "EXIT_COMPLETED" and not c.assigned() and announced(ev) == 1
              and not errors(ev),
              f"ending {ending(ev)}, assigned {c.assigned()}, {announced(ev)} announcement(s)")
    finally:
        c.close()

    # 3 — a license used within 30 days ends as still active
    c = Case(snapshot)
    try:
        c.run("WF_RECORD_LICENSE_USAGE_V0", {"employee_id": EMPLOYEE})
        ev = c.reclaim()
        check("a license still in use ends as still active, and stays assigned",
              ending(ev) == "EXIT_STILL_ACTIVE" and c.assigned() and not announced(ev) and not errors(ev),
              f"ending {ending(ev)}, assigned {c.assigned()}, {announced(ev)} announcement(s)")
    finally:
        c.close()

    held = 0
    for criterion, ok, detail in results:
        tag = "SKIP" if ok is None else ("OK  " if ok else "FAIL")
        print(f"  {tag}  {criterion}")
        if detail:
            print(f"          {detail}")
        held += ok is True
    exercised = sum(ok is not None for _, ok, _ in results)
    print(f"\n  {held}/{exercised} criteria hold  ({len(results) - exercised} not exercised)")
    return 0 if held == exercised else 1


if __name__ == "__main__":
    sys.exit(main())
