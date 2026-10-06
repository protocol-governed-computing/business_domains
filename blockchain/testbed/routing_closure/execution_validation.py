"""Execution validation — run identity and wallet against the criteria `cr_06_routing_closure` declared.

The change answers one question for every identity and wallet act: what happens when a record the act
needs cannot be read or written. The business answered it: the act ends as rejected, at the step
whose record failed, and nothing after that step runs.

Each criterion makes a store fail on purpose. It appends a line no store can parse to the file the
store reads, on a fresh data root, so the store answers BACKEND_ERROR. Then it dispatches a real
workflow through `protocol_runtime` and reads three things back:

- the ending the trace records, which must be the declared EXIT_REJECTED;
- the contracts the trace shows starting, which must stop at the failed one;
- the records, which must not show the act's effect.

Criterion 1 is case O3 of the SoSyM study: before this change, an acceptance whose lookup failed was
recorded as an acceptance.

Run:  python business_domains/blockchain/testbed/routing_closure/execution_validation.py [snapshot]
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
PAYLOADS = DOMAIN / "testbed" / "identity" / "test_payloads"

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from blockchain.testbed.wallet.execution_validation import (  # noqa: E402
    acceptance, creation, registration)

NS = "blockchain::"
IDENTITY = "blockchain/identity"
WALLET = "blockchain/wallet"


def payload(name: str) -> dict:
    return json.loads((PAYLOADS / name).read_text())


class Case:
    """One fresh data root, the acts that set it up, and one store made to fail."""

    def __init__(self, snapshot: Path):
        self.snapshot = snapshot
        self.root = Path(tempfile.mkdtemp(prefix="pgc_routing_closure_"))

    def run(self, wf: str, body: dict):
        return api.run_workflow(wf_fqdn=NS + wf, payload=body,
                                snapshot_root=str(self.snapshot), data_root=str(self.root))

    def corrupt(self, relative: str) -> None:
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a") as fh:
            fh.write("{corrupt\n")

    def read(self, relative: str):
        path = self.root / relative
        if not path.is_file():
            return None
        try:
            return json.loads(path.read_text())
        except json.JSONDecodeError:
            return None

    def close(self) -> None:
        shutil.rmtree(self.root, ignore_errors=True)


def trace(result) -> list[dict]:
    lines = []
    for f in sorted(Path(result.trace_dir).glob("*.jsonl")):
        lines += [json.loads(l) for l in f.read_text().splitlines() if l.strip()]
    return lines


def ending(events: list[dict]) -> str | None:
    routes = [e for e in events if e.get("event_type") == "WF_ROUTE"]
    return routes[-1].get("detail", {}).get("to_node") if routes else None


def started(events: list[dict]) -> list[str]:
    return [str(e.get("detail", {}).get("cc_fqdn") or e.get("cc_fqdn") or e.get("cc_addr"))
            for e in events if e.get("event_type") == "CC_START"]


def errors(events: list[dict]) -> list[dict]:
    return [e for e in events if e.get("event_type") == "ERROR"]


def main() -> int:
    snapshot = Path(sys.argv[1]) if len(sys.argv) > 1 else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1

    results: list[tuple[str, bool | None, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    # 1 — case O3: an acceptance whose lookup fails is rejected, and no acceptance is recorded
    c = Case(snapshot)
    try:
        c.run("WF_REGISTER_ACTOR_V1", payload("01_register_actor.json"))
        c.corrupt(f"{IDENTITY}/contact_address_registry.jsonl")
        r = c.run("WF_ACCEPT_ACTOR_V1", payload("04_accept_actor.json"))
        ev = trace(r)
        state = (c.read(f"{IDENTITY}/actors.json") or {}).get("ada@example.test", {}).get("state")
        check("an acceptance whose lookup of the person fails is rejected, and no acceptance is recorded",
              ending(ev) == "EXIT_REJECTED" and state == "UNVERIFIED" and not errors(ev),
              f"ending {ending(ev)}, state {state}, {len(errors(ev))} error(s)")
        check("the acceptance stops at the failed lookup, and nothing after it runs",
              len(started(ev)) == 1, f"contracts started: {len(started(ev))}")
    finally:
        c.close()

    # 2 — a rejection whose lookup fails is rejected, and no decision is recorded
    c = Case(snapshot)
    try:
        c.run("WF_REGISTER_ACTOR_V1", payload("07_register_bob.json"))
        c.corrupt(f"{IDENTITY}/contact_address_registry.jsonl")
        r = c.run("WF_REJECT_ACTOR_V1", payload("08_reject_actor.json"))
        ev = trace(r)
        state = (c.read(f"{IDENTITY}/actors.json") or {}).get("bob@example.test", {}).get("state")
        check("a rejection whose lookup of the person fails is rejected, and no decision is recorded",
              ending(ev) == "EXIT_REJECTED" and state == "UNVERIFIED" and not errors(ev),
              f"ending {ending(ev)}, state {state}, {len(errors(ev))} error(s)")
    finally:
        c.close()

    # 3 — a registration whose address claim fails is rejected, and no person is recorded
    c = Case(snapshot)
    try:
        c.corrupt(f"{IDENTITY}/contact_address_registry.jsonl")
        r = c.run("WF_REGISTER_ACTOR_V1", payload("01_register_actor.json"))
        ev = trace(r)
        actors = c.read(f"{IDENTITY}/actors.json") or {}
        check("a registration whose address claim fails is rejected, and no person is recorded",
              ending(ev) == "EXIT_REJECTED" and "ada@example.test" not in actors and not errors(ev),
              f"ending {ending(ev)}, {len(actors)} person(s) recorded, {len(errors(ev))} error(s)")
    finally:
        c.close()

    # 4 — a wallet whose identity claim fails is rejected, and no wallet is recorded
    holder = "routing-holder@example.test"
    c = Case(snapshot)
    try:
        c.run("WF_REGISTER_ACTOR_V1", registration("Routing Holder", holder))
        c.run("WF_ACCEPT_ACTOR_V1", acceptance(holder))
        c.corrupt(f"{WALLET}/wallet_identity_registry.jsonl")
        r = c.run("WF_CREATE_WALLET_V1", creation(holder))
        ev = trace(r)
        wallets = c.read(f"{WALLET}/wallets.json") or {}
        check("a wallet whose identity claim fails is rejected, and no wallet is recorded",
              ending(ev) == "EXIT_REJECTED" and not wallets and not errors(ev),
              f"ending {ending(ev)}, {len(wallets)} wallet(s), {len(errors(ev))} error(s)")
    finally:
        c.close()

    # 5 — a wallet whose holder lookup fails is rejected
    c = Case(snapshot)
    try:
        c.run("WF_REGISTER_ACTOR_V1", registration("Routing Holder", holder))
        c.run("WF_ACCEPT_ACTOR_V1", acceptance(holder))
        c.corrupt(f"{IDENTITY}/contact_address_registry.jsonl")
        r = c.run("WF_CREATE_WALLET_V1", creation(holder))
        ev = trace(r)
        wallets = c.read(f"{WALLET}/wallets.json") or {}
        check("a wallet whose holder lookup fails is rejected, and nothing after the lookup runs",
              ending(ev) == "EXIT_REJECTED" and not wallets and len(started(ev)) == 1 and not errors(ev),
              f"ending {ending(ev)}, {len(wallets)} wallet(s), contracts started {len(started(ev))}")
    finally:
        c.close()

    results.append(("every act whose records are all read and written ends as it did before", None,
                    "exercised by identity/execution_validation.py and wallet/execution_validation.py"))
    results.append(("records made before a failure are unchanged by it", None,
                    "the change authors no compensation, repair or backfill, so nothing it adds can "
                    "write to a record made before the failure"))

    held = 0
    for criterion, ok, detail in results:
        tag = "SKIP" if ok is None else ("OK  " if ok else "FAIL")
        print(f"  {tag}  {criterion}")
        if detail:
            print(f"          {detail}")
        held += ok is True
    exercised = sum(ok is not None for _, ok, _ in results)
    skipped = len(results) - exercised
    print(f"\n  {held}/{exercised} criteria hold  ({skipped} not exercised)")
    return 0 if held == exercised else 1


if __name__ == "__main__":
    sys.exit(main())
