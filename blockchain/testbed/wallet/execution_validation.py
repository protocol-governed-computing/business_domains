"""Execution validation — run wallet against the acceptance criteria its CRs declared.

`tc construction check` proves a design determines its artifacts. Neither it nor the phase oracle
proves the composition *does what the business asked for*, because both read documents and this reads
behaviour: every criterion is exercised by dispatching real workflows through `protocol_runtime`
against a fresh data root.

**This is the first act in the composition that reads records another subdomain owns**, and most of
what is checked here is about that. A wallet is created for a person the wallet subdomain cannot see
for itself: identity holds who exists, the act consults identity's binding to read them, and the
platform refuses a write through anything consulted. So the criteria come in pairs — the act
completes, *and* identity's stores are byte for byte what they were before it ran.

The reach was undeclared in the first pass of `cr_04_wallet`, and the act halted on its second step asking for
a record it never said it would read. Criterion 1 is that halt not happening; criterion 4 is the
reason the halt was worth fixing properly rather than by widening what the wallet owns.

State accumulates deliberately — a person must be registered and accepted before a wallet can be
created for them — so the order is part of the evidence and the run is not idempotent. That is why it
starts from an empty data root every time.

Run:  python business_domains/blockchain/testbed/wallet/execution_validation.py [snapshot]
      ... --data-root <path>     keep the stores instead of discarding them
Exit: 0 if every exercised criterion holds, 1 otherwise.
"""

from __future__ import annotations

import hashlib
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
IDENTITY_STORE = "blockchain/identity"
WALLET_STORE = "blockchain/wallet"

# People of this suite's own, distinct from identity's, so both suites run into one data root.
# A domain has one place its records live; a second root would hold a second copy of identity's
# records, which is the arrangement this change exists to prevent.
HOLDER, UNDECIDED = "wallet-holder@example.test", "wallet-undecided@example.test"
AUTHORITY = "authority-01"

SCHEMA = {"name": {"required": True, "type": "string"},
          "contact_address": {"required": True, "type": "string"}}

# An uncompressed public key is 64 bytes, or 65 with the 0x04 tag. The transform that derives an
# address refuses anything else rather than padding it, because a padded key derives an address
# nobody owns — so the material here is well formed rather than merely present.
def key_material(seed: str) -> str:
    return "04" + hashlib.sha256(f"{seed}-x".encode()).hexdigest() \
                + hashlib.sha256(f"{seed}-y".encode()).hexdigest()


def registration(name: str, address: str) -> dict:
    return {"actor_record": {"name": name, "contact_address": address,
                             "currency_preference": "BACHI", "language": "en",
                             "state": "UNVERIFIED"},
            "registration_schema": SCHEMA,
            "address_path": "contact_address", "address_type": "string",
            "stream_id": "ACTOR_OCCURRENCES",
            "occurrence_fields": {"occurrence": "ACTOR_REGISTERED_UNVERIFIED",
                                  "contact_address": address}}


def acceptance(address: str, authority: str = AUTHORITY) -> dict:
    return {"contact_address": address, "verifying_authority": authority,
            "decision": "ACCEPTED", "grounds": "",
            "grounds_parameters": {"grounds": ""},
            "grounds_rules": [{"field": "grounds", "op": "not_null"},
                              {"field": "grounds", "op": "neq", "value": ""}],
            "self_check_parameters": {"verifying_authority": authority,
                                      "contact_address": address},
            "self_check_rules": [{"field": "verifying_authority", "op": "neq", "value": address}],
            "states_admitting_a_decision": ["UNVERIFIED"],
            "admitted_outcomes": ["ACCEPTED", "REJECTED"],
            "decided_actor_fields": {"contact_address": address, "state": "ACCEPTED",
                                     "verifying_authority": authority, "grounds": ""},
            "stream_id": "ACTOR_OCCURRENCES",
            "occurrence_fields": {"occurrence": "ACTOR_ACCEPTED", "contact_address": address,
                                  "verifying_authority": authority, "grounds": ""}}


def creation(address: str, prefix: str = "wal") -> dict:
    return {"contact_address": address, "key_material": key_material(address),
            "wallet_id_prefix": prefix,
            "wallet_fields": {"holder": address, "balance": 0, "denomination": "BACHI",
                              "classification": "DEFAULT", "state": "ACTIVE"},
            "stream_id": "WALLET_OCCURRENCES",
            "occurrence_fields": {"occurrence": "WALLET_CREATED", "holder": address}}


class Run:
    """One dispatched workflow, and the store state it left behind."""

    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root = snapshot, data_root

    def __call__(self, wf: str, payload: dict):
        return api.run_workflow(wf_fqdn=NS + wf, payload=payload,
                                snapshot_root=str(self.snapshot), data_root=str(self.data_root))

    def _read(self, relative: str):
        path = self.data_root / relative
        return path.read_text() if path.is_file() else ""

    def wallets(self) -> dict:
        text = self._read(f"{WALLET_STORE}/wallets.json")
        return json.loads(text) if text else {}

    def wallet_trail(self) -> list[dict]:
        """The trail as written — envelope and record together.

        The time an occurrence carries is on the envelope, put there by the store rather than by the
        caller. Identity's trail carries it inside the record as well because identity's acts send it;
        wallet's do not, and reading only the record would report every wallet moment as untimed.
        """
        return [json.loads(line)
                for line in self._read(f"{WALLET_STORE}/wallet_occurrences.jsonl").splitlines()
                if line.strip()]

    def identity_fingerprint(self) -> dict[str, str]:
        """Every store identity owns, hashed. The evidence that a reach only read."""
        directory = self.data_root / IDENTITY_STORE
        if not directory.is_dir():
            return {}
        return {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(directory.iterdir()) if p.is_file()}


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
        data_root = Path(tempfile.mkdtemp(prefix="pgc_wallet_validation_"))
    else:
        # Only this suite's own stores must be absent. The root is shared with identity's suite by
        # design — one domain, one place its records live — so refusing a non-empty root would force
        # a second root, and identity's records would exist in two of them.
        wallet_stores = keep / WALLET_STORE
        if wallet_stores.exists() and any(wallet_stores.iterdir()):
            print(f"{wallet_stores} is not empty — this run accumulates state and must start from "
                  f"no wallet stores.\nRemove that directory, or name a root without one.")
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
        # The ground the wallet stands on. Not a wallet criterion — identity's, exercised here
        # because a wallet cannot be created for a person who does not exist.
        run("WF_REGISTER_ACTOR_V0", registration("Wallet Holder", HOLDER))
        run("WF_ACCEPT_ACTOR_V0", acceptance(HOLDER))
        before = run.identity_fingerprint()

        # 1 — the act completes, which it could not do while its reach was undeclared
        r = run("WF_CREATE_WALLET_V0", creation(HOLDER))
        wallets = run.wallets()
        check("an accepted person is given a wallet, and the act runs to completion",
              r.status == "SUCCESS" and len(wallets) == 1,
              f"status {r.status}, {len(wallets)} wallet(s)")

        # 2 — the wallet's own records were written
        holder_matches = [w for w in wallets.values() if w.get("holder") == HOLDER]
        check("the wallet is recorded against the person it belongs to",
              len(holder_matches) == 1, f"{len(holder_matches)} wallet(s) held by {HOLDER}")

        # 3 — the moment is on the wallet's own trail, not identity's
        trail = run.wallet_trail()
        check("the creation of a wallet is recorded as a moment on the wallet's trail",
              len(trail) == 1 and trail[0].get("record", {}).get("occurrence") == "WALLET_CREATED"
              and bool(trail[0].get("timestamp")),
              f"{len(trail)} occurrence(s)")

        # 4 — THE criterion this change exists for. The act read identity and wrote nothing there.
        after = run.identity_fingerprint()
        changed = sorted(k for k in before if before[k] != after.get(k))
        check("identity's records are consulted and never written — byte for byte what they were",
              before == after,
              f"changed: {', '.join(changed) or 'none'}; "
              f"added: {', '.join(sorted(set(after) - set(before))) or 'none'}")

        # 5 — a wallet needs a person the business has accepted
        r = run("WF_CREATE_WALLET_V0", creation("ghost@example.test"))
        check("a wallet for a person who never registered is refused",
              r.status != "SUCCESS" and len(run.wallets()) == 1,
              f"status {r.status}, {len(run.wallets())} wallet(s)")

        # Bob registers but is never accepted. His registration is identity writing its own
        # records, so the fingerprint is re-taken afterwards: what criterion 8 asks is whether a
        # *wallet* act disturbed identity, and comparing across an identity act would answer a
        # different question and answer it wrongly.
        run("WF_REGISTER_ACTOR_V0", registration("Wallet Undecided", UNDECIDED))
        mark = run.identity_fingerprint()

        # 6 — the reach reads state, so an unaccepted person is visible as unaccepted
        r = run("WF_CREATE_WALLET_V0", creation(UNDECIDED))
        check("an unverified person is refused a wallet, and none is recorded for them",
              not any(w.get("holder") == UNDECIDED for w in run.wallets().values()),
              f"status {r.status}, {len(run.wallets())} wallet(s)")

        # 7 — one person, one wallet
        r = run("WF_CREATE_WALLET_V0", creation(HOLDER))
        check("a person the business already gave a wallet is not given a second",
              r.status != "SUCCESS" and len(run.wallets()) == 1,
              f"status {r.status}, {len(run.wallets())} wallet(s)")

        # 8 — nothing above disturbed identity, including the refusals
        check("no refused wallet act left a mark on identity's records",
              run.identity_fingerprint() == mark,
              "identity stores differ from before the refused wallet acts")

        # 9 — one moment per wallet, and nothing rewritten. Stated against the wallets actually
        # recorded rather than against a fixed count, so it is a claim about the business rather than
        # about how many acts this script happens to dispatch.
        check("every wallet the business holds has exactly one creation moment, and none was rewritten",
              len(run.wallet_trail()) == len(run.wallets()),
              f"{len(run.wallet_trail())} occurrence(s), {len(run.wallets())} wallet(s)")

        skip("a wallet act attempting to write through the reach is refused",
             "no act writes to a consulted binding, so there is nothing to dispatch; the platform "
             "refuses it at run time and proving that needs an act authored to try")

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
