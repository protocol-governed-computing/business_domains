"""Execution validation — run identity against the acceptance criteria its CR declared.

`tc construction check` proves a design determines its artifacts. Neither it nor the phase oracle
proves the composition *does what the business asked for*, because both read documents and this
reads behaviour: every criterion in the CR's §15 is exercised by dispatching real workflows through
`protocol_runtime` against a fresh data root.

Each scenario is stated as the criterion it proves, so a failure names a business promise rather
than a workflow. State accumulates deliberately — an actor must be registered before a decision
against them can be recorded, and decided once before a second decision can be refused — so the
order is part of the evidence and the run is not idempotent. That is why it starts from an empty
data root every time.

Two criteria are deliberately unexercised and reported as such: whether an unverified actor holds
no wallet is a claim about functions this change does not build, and it cannot be tested until they
exist. Stating them as skipped is the difference between a criterion that holds and one nobody
looked at.

Run:  python business_domains/blockchain/testbed/identity/execution_validation.py [snapshot]
      ... --data-root <path>     keep the stores instead of discarding them
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

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains",
             WORKSPACE / "conformance_workloads", WORKSPACE / "transformation"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402

NS = "blockchain::"
STORE = "blockchain/identity"

# What the business asks of a registration: a name and a contact address, read for absence and for
# form. Everything else is belief, which is the verification decision's business.
SCHEMA = {"name": {"required": True, "type": "string"},
          "contact_address": {"required": True, "type": "string"}}
ADA, BOB = "ada@example.test", "bob@example.test"
AUTHORITY = "authority-01"


def registration(name: str, address: str, **overrides) -> dict:
    record = {"name": name, "contact_address": address,
              "currency_preference": "BACHI", "language": "en", "state": "UNVERIFIED"}
    record.update(overrides.pop("record", {}))
    return {"actor_record": record, "registration_schema": SCHEMA,
            "address_path": "contact_address", "address_type": "string",
            "stream_id": "ACTOR_OCCURRENCES",
            "occurrence_fields": {"occurrence": "ACTOR_REGISTERED_UNVERIFIED",
                                  "contact_address": address},
            **overrides}


# The rules the rejection path checks its grounds against, before anything is recorded. Stated here
# because the boundary states them: the caller sends grounds, and what makes grounds sufficient is the
# business's rule rather than the caller's opinion.
GROUNDS_RULES = [{"field": "grounds", "op": "not_null"},
                 {"field": "grounds", "op": "neq", "value": ""}]


def decision(address: str, outcome: str, grounds: str = "", authority: str = AUTHORITY) -> dict:
    return {"contact_address": address, "verifying_authority": authority,
            "decision": outcome, "grounds": grounds,
            "grounds_parameters": {"grounds": grounds},
            "grounds_rules": GROUNDS_RULES,
            # A decider is not the person being decided about. Stated at the boundary because the
            # rule is the business's and the values are the caller's.
            "self_check_parameters": {"verifying_authority": authority,
                                      "contact_address": address},
            "self_check_rules": [{"field": "verifying_authority", "op": "neq", "value": address}],
            "states_admitting_a_decision": ["UNVERIFIED"],
            "admitted_outcomes": ["ACCEPTED", "REJECTED"],
            "decided_actor_fields": {"contact_address": address, "state": outcome,
                                     "verifying_authority": authority, "grounds": grounds},
            "stream_id": "ACTOR_OCCURRENCES",
            "occurrence_fields": {"occurrence": f"ACTOR_{outcome}", "contact_address": address,
                                  "verifying_authority": authority, "grounds": grounds}}


def deciding_workflow(outcome: str) -> str:
    """Which act records this outcome.

    One workflow decided both outcomes until the change that split them, so that each announces its
    own moment and the rejection path can require grounds throughout. The criteria below are the same
    statements about the business; only the act they are made against has changed.
    """
    return "WF_ACCEPT_ACTOR_V0" if outcome == "ACCEPTED" else "WF_REJECT_ACTOR_V0"


class Run:
    """One dispatched workflow, and the store state it left behind."""

    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root = snapshot, data_root

    def __call__(self, wf: str, payload: dict):
        return api.run_workflow(wf_fqdn=NS + wf, payload=payload,
                                snapshot_root=str(self.snapshot), data_root=str(self.data_root))

    def actors(self) -> dict:
        path = self.data_root / STORE / "actors.json"
        return json.loads(path.read_text()) if path.is_file() else {}

    def trail(self) -> list[dict]:
        path = self.data_root / STORE / "actor_occurrences.jsonl"
        if not path.is_file():
            return []
        return [json.loads(line).get("record", {})
                for line in path.read_text().splitlines() if line.strip()]

    def occurrences(self, address: str, kind: str | None = None) -> list[dict]:
        return [r for r in self.trail()
                if r.get("contact_address") == address
                and (kind is None or r.get("occurrence") == kind)]


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
        data_root = Path(tempfile.mkdtemp(prefix="pgc_identity_validation_"))
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
    results: list[tuple[str, bool | None, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    def skip(criterion: str, why: str) -> None:
        results.append((criterion, None, why))

    try:
        # 1 — a person supplying a name and an address is admitted, and is unverified
        r = run("WF_REGISTER_ACTOR_V0", registration("Ada Lovelace", ADA))
        actors = run.actors()
        check("a person supplying a name and a contact address is admitted, and is unverified",
              r.status == "SUCCESS" and actors.get(ADA, {}).get("state") == "UNVERIFIED",
              f"status {r.status}, state {actors.get(ADA, {}).get('state')}")

        # 2 — a registration the business cannot read leaves nothing behind
        r = run("WF_REGISTER_ACTOR_V0",
                registration("No Address", "x", record={"contact_address": None}))
        check("a person supplying no contact address is refused, and no actor exists afterwards",
              r.status != "SUCCESS" and len(run.actors()) == 1,
              f"status {r.status}, {len(run.actors())} actor(s)")

        # 3 — the same person twice is one actor and two recorded registrations
        r = run("WF_REGISTER_ACTOR_V0", registration("Ada Lovelace", ADA))
        registrations = run.occurrences(ADA, "ACTOR_REGISTERED_UNVERIFIED")
        check("a person registering twice is one actor, with two registrations shown against them",
              r.status == "SUCCESS" and len(run.actors()) == 1 and len(registrations) == 2,
              f"status {r.status}, {len(run.actors())} actor(s), {len(registrations)} registration(s)")

        # 4 — a decision needs a registration to be about
        r = run(deciding_workflow("ACCEPTED"), decision("ghost@example.test", "ACCEPTED"))
        check("a decision against a person who never registered is refused",
              r.status != "SUCCESS", f"status {r.status}")

        # 5 — an acceptance is shown with its authority and the time the composition determined
        r = run(deciding_workflow("ACCEPTED"), decision(ADA, "ACCEPTED"))
        actor = run.actors().get(ADA, {})
        accepted = run.occurrences(ADA, "ACTOR_ACCEPTED")
        check("an accepted actor is shown as accepted, with the deciding authority and the time",
              r.status == "SUCCESS" and actor.get("state") == "ACCEPTED"
              and actor.get("verifying_authority") == AUTHORITY
              and bool(accepted and accepted[0].get("occurred_at")),
              f"status {r.status}, state {actor.get('state')}, "
              f"occurred_at {accepted[0].get('occurred_at') if accepted else None}")

        # 6 — decided once, and no second decision may disturb it
        r = run(deciding_workflow("REJECTED"), decision(ADA, "REJECTED", "second attempt"))
        check("a decision against an actor already decided about is refused",
              r.status != "SUCCESS" and run.actors().get(ADA, {}).get("state") == "ACCEPTED",
              f"status {r.status}, state {run.actors().get(ADA, {}).get('state')}")

        # 7 — a rejection is its own occurrence, and is never readable as an acceptance
        run("WF_REGISTER_ACTOR_V0", registration("Bob Kahn", BOB))
        r = run(deciding_workflow("REJECTED"),
                decision(BOB, "REJECTED", "identity not established"))
        bob = run.actors().get(BOB, {})
        rejected = run.occurrences(BOB, "ACTOR_REJECTED")
        check("a rejected actor is shown as rejected, with authority, grounds and time",
              r.status == "SUCCESS" and bob.get("state") == "REJECTED"
              and bob.get("grounds") and bool(rejected and rejected[0].get("occurred_at")),
              f"status {r.status}, state {bob.get('state')}")
        check("a rejected actor cannot be read as accepted by any means",
              not run.occurrences(BOB, "ACTOR_ACCEPTED") and bob.get("state") != "ACCEPTED",
              f"{len(run.occurrences(BOB, 'ACTOR_ACCEPTED'))} acceptance(s) against a rejected actor")

        # 8 — the business can ask who has been rejected
        listed = [a for a, v in run.actors().items() if v.get("state") == "REJECTED"]
        check("the business can list the actors that have been rejected",
              listed == [BOB], f"rejected: {listed}")

        # 9 — a rejection is refused when it states nothing
        run("WF_REGISTER_ACTOR_V0", registration("Grace Hopper", "grace@example.test"))
        r = run(deciding_workflow("REJECTED"), decision("grace@example.test", "REJECTED"))
        check("a rejection stating no grounds is refused", r.status != "SUCCESS",
              f"status {r.status}")

        # 10 — an outcome outside the two the business admits is refused
        #
        # Now refused twice over, and the second is the stronger. There is no act that records an
        # arbitrary outcome: the deciding workflow was split into an acceptance and a rejection, so a
        # third outcome has nowhere to be recorded at all. What remains checkable is that the
        # contract still refuses one if a caller smuggles it through an act that does exist — driven
        # through the acceptance path so the outcome gate is what answers, not the grounds gate.
        r = run(deciding_workflow("ACCEPTED"), decision("grace@example.test", "MAYBE"))
        check("an outcome that is neither acceptance nor rejection is refused",
              r.status != "SUCCESS", f"status {r.status}")

        # 11 — a person never decides about themselves
        r = run(deciding_workflow("ACCEPTED"),
                decision("grace@example.test", "ACCEPTED", authority="grace@example.test"))
        check("a person may not make the verification decision about themselves",
              r.status != "SUCCESS", f"status {r.status}")

        # 12 — every occurrence carries a time, and the composition determined all of them
        trail = run.trail()
        check("every recorded occurrence carries the time it occurred",
              bool(trail) and all(r.get("occurred_at") for r in trail),
              f"{sum(1 for r in trail if not r.get('occurred_at'))} of {len(trail)} without a time")

        # 13 — the trail only ever grew: every refusal above left it untouched
        check("no operation changed or removed an occurrence already recorded",
              len(trail) == 6,
              f"{len(trail)} occurrence(s); expected 6 — three registrations, one acceptance, "
              f"one rejection, and one repeat registration")

        # Two criteria this change cannot exercise, named rather than passed over.
        skip("two occurrences at different moments carry different times",
             "the run completes inside one clock second, so this needs a timed test, not a fast one")
        # 14 — the criterion that waited for a wallet to exist. It does now, and the act refuses a
        # person nobody accepted, so the half of this claim that concerns wallets is testable here
        # rather than only in wallet's own suite. Grace is registered and undecided.
        r = run("WF_CREATE_WALLET_V0", {
            "contact_address": "grace@example.test",
            "key_material": "04" + "a" * 128,
            "wallet_id_prefix": "wal",
            "wallet_fields": {"holder": "grace@example.test"},
            "stream_id": "WALLET_OCCURRENCES",
            "occurrence_fields": {"occurrence": "WALLET_CREATED"}})
        wallets = run.data_root / "blockchain" / "wallet" / "wallets.json"
        check("an unverified actor holds no wallet",
              r.status != "SUCCESS" and not wallets.is_file(),
              f"status {r.status}, wallet store {'written' if wallets.is_file() else 'absent'}")

        skip("an unverified or rejected actor has submitted no transaction",
             "transaction is a later function; there is nothing yet to submit")

    finally:
        if keep is None:
            shutil.rmtree(data_root, ignore_errors=True)

    failed = [c for c, held, _ in results if held is False]
    for criterion, held, detail in results:
        mark = "SKIP" if held is None else ("OK  " if held else "FAIL")
        print(f"  {mark}  {criterion}" + (f"\n          {detail}" if detail and held is not True else ""))
    exercised = sum(1 for _, held, _ in results if held is not None)
    print(f"\n  {exercised - len(failed)}/{exercised} criteria hold"
          f"  ({sum(1 for _, h, _ in results if h is None)} not exercised)")
    if keep is not None:
        print(f"  stores left at {keep}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
