"""Execution validation — run the reclaim against the criteria `cr_02_reclaim_closure` declared.

The change answers one question for the reclaim: what happens when the registry refuses to remove
the assignment. The business answered it: the reclaim ends as still active, the license stays
assigned, and no revocation is announced.

Each criterion provisions a license on a fresh data root, then dispatches a real reclaim through
`protocol_runtime` and reads three things back:

- the ending the trace records;
- whether the trace announces anything;
- whether the registry still holds the assignment.

The registry refuses a removal only when it is handed no key, and the contract refuses that earlier,
at its own inputs. So criterion 1 stands in for the registry's removal, for that run only, and has
it answer VIOLATION. Criteria 2 and 3 replace nothing.

Run:  python business_domains/ai_governance/testbed/routing_closure/execution_validation.py [snapshot]
Exit: 0 if every exercised criterion holds, 1 otherwise.
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
LICENSING = DOMAIN / "testbed" / "ai_licensing" / "test_payloads"
SEED = DOMAIN / "testbed" / "agent_governance" / "seed_data" / "license_facts.json"

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from capability_side_effects.implementation.CS_REGISTRY_V0.impl.executor import (  # noqa: E402
    RegistryExecutor)

NS = "ai_governance::"
STORE = "ai_governance/ai_licensing"
EMPLOYEE = "e-7526"
LICENSE = "lic-7526"


def reclaim(last_active: str) -> dict:
    return {"license_id": LICENSE, "threshold_days": 30,
            "context": {"employee_id": EMPLOYEE, "last_active_date": last_active,
                        "evaluation_date": "2026-06-01T00:00:00Z", "days_inactive": 151}}


INACTIVE = "2026-01-01T00:00:00Z"
ACTIVE = "2026-05-25T00:00:00Z"


class Case:
    """One fresh data root, with one license provisioned on it."""

    def __init__(self, snapshot: Path):
        self.snapshot = snapshot
        self.root = Path(tempfile.mkdtemp(prefix="pgc_reclaim_closure_"))
        (self.root / STORE).mkdir(parents=True)
        shutil.copy(SEED, self.root / STORE)
        self.run("WF_PROVISION_AI_LICENSING_V0",
                 json.loads((LICENSING / "provision_ai_licensing_payload.json").read_text()))

    def run(self, wf: str, body: dict) -> list[dict]:
        result = api.run_workflow(wf_fqdn=NS + wf, payload=body,
                                  snapshot_root=str(self.snapshot), data_root=str(self.root))
        lines: list[dict] = []
        for f in sorted(Path(result.trace_dir).glob("*.jsonl")):
            lines += [json.loads(line) for line in f.read_text().splitlines() if line.strip()]
        return lines

    def assigned(self) -> bool:
        """Whether the registry's latest entry for the employee still holds the license."""
        path = self.root / STORE / "license_registry.json"
        entries = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        latest = [e for e in entries if e.get("key") == EMPLOYEE][-1:]
        return bool(latest) and not latest[0].get("tombstone") and latest[0].get("target_ref") == LICENSE

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

    # 1 — a reclaim the registry refuses ends as still active, and nothing is announced
    c = Case(snapshot)
    real = RegistryExecutor.deregister
    RegistryExecutor.deregister = lambda self, payload: {"result_status": "VIOLATION"}
    try:
        ev = c.run("WF_AUTO_RECLAIM_V0", reclaim(INACTIVE))
    finally:
        RegistryExecutor.deregister = real
    try:
        check("a reclaim the registry refuses ends as still active, the license stays assigned, and "
              "no revocation is announced",
              ending(ev) == "EXIT_ACTIVE" and c.assigned() and not announced(ev) and not errors(ev),
              f"ending {ending(ev)}, assigned {c.assigned()}, {announced(ev)} announcement(s), "
              f"{errors(ev)} error(s)")
        check("the reclaim stops at the refused removal, and nothing after it runs",
              started(ev) == 1, f"contracts started: {started(ev)}")
    finally:
        c.close()

    # 2 — a reclaim the registry does not refuse ends as it did before
    c = Case(snapshot)
    try:
        ev = c.run("WF_AUTO_RECLAIM_V0", reclaim(INACTIVE))
        check("a reclaim the registry accepts ends as reclaimed, the license is released, and the "
              "revocation is announced",
              ending(ev) == "EXIT_RECLAIMED" and not c.assigned() and announced(ev) == 1
              and not errors(ev),
              f"ending {ending(ev)}, assigned {c.assigned()}, {announced(ev)} announcement(s)")
    finally:
        c.close()

    # 3 — a license still in use ends as still active, as it did before
    c = Case(snapshot)
    try:
        ev = c.run("WF_AUTO_RECLAIM_V0", reclaim(ACTIVE))
        check("a license still in use ends as still active, and stays assigned",
              ending(ev) == "EXIT_ACTIVE" and c.assigned() and not announced(ev) and not errors(ev),
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
