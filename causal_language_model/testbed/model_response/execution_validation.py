"""Execution validation — run model_response against the acceptance criteria its CR declared.

`tc construction check` proves the design determines its artifacts, and conformance proves each
transform against its vectors. Neither proves the business gets what it asked for: that a model is
consulted only while in service, only on what it may read, and that no word it offers reaches a
customer unless the rules in force permit it. This reads behaviour — every criterion dispatches real
workflows through `protocol_runtime` against a fresh data root.

The model here is the test model. It tries to break the rules on every word: it offers another
customer's account number first, then the next word of the supporting material, then the end. So a
response that equals the material, and a trace in which the account number was offered on every
word, is the evidence that the rules — not the model's restraint — decided what was written.

The model's step is declared not determined by its inputs, so every offer it makes is recorded, and
a replay substitutes the records rather than consulting the model. Criterion 14 replays a response
and compares the two executions.

State accumulates deliberately — a model must be registered and placed in service before a user
prompt reaches it — so the order is part of the evidence and the run is not idempotent. That is why it
starts from an empty data root every time.

Run:  python business_domains/causal_language_model/testbed/model_response/execution_validation.py [snapshot]
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
from runtime.replay import determinative  # noqa: E402

NS = "causal_language_model::"
STORE = "causal_language_model/model_response"
RESPONDED, REFUSED = NS + "EV_USER_PROMPT_RESPONDED_V0", NS + "EV_USER_PROMPT_REFUSED_V0"

# The test model's standing attempt at a number that is not the customer's.
ANOTHER_CUSTOMERS_ACCOUNT = "87654321"
OWN_ACCOUNT = "12345678"
MATERIAL = f"Account {OWN_ACCOUNT} balance 40."

STAFF = {"staff_credentials": {"staff_id": "staff-01", "role": "model_staff"}, "staff_id": "staff-01"}
NOT_STAFF = {"staff_credentials": {"staff_id": "clerk-01", "role": "clerk"}, "staff_id": "clerk-01"}


def rules(longest: int = 8) -> dict:
    return {"forbidden": [{"rule": "no_guarantees", "pattern": r"\bguaranteed\b"}],
            "account_number_pattern": "[0-9](?:[ -]?[0-9]){7}",
            "freedom": 0, "longest_response": longest}


def registration(name: str, capacity: int, fingerprint: str, staff: dict = STAFF) -> dict:
    return {**staff, "description": {"name": name, "reading_capacity": capacity},
            "fingerprint": fingerprint}


def identity_key(name: str, capacity: int, fingerprint: str) -> str:
    """The model's identity as the business forms it: its description, canonical, and its fingerprint."""
    description = json.dumps({"name": name, "reading_capacity": capacity}, sort_keys=True,
                             separators=(",", ":"))
    return f"{description}|{fingerprint}"


def placement(key: str, tis: str, longest: int = 8) -> dict:
    return {**STAFF, "identity_key": key, "time_in_service_id": tis, "ceiling": "confidential",
            "system_prompt": "Answer only from the supporting material.",
            "response_rules": rules(longest)}


def prompt(upid: str, key: str, material: str = MATERIAL, kind: str = "internal",
           customer: str = "customer-01", seed: int = 7) -> dict:
    return {"user_prompt_id": upid, "requester_id": "agent-01",
            "permitted_customers": ["customer-01"], "customer_id": customer,
            "account_numbers": [OWN_ACCOUNT], "identity_key": key, "kind": kind,
            "question": "What is my balance?", "supporting_material": material, "seed": seed}


class Run:
    """Dispatched workflows, and the stores they left behind."""

    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root = snapshot, data_root

    def __call__(self, wf: str, payload: dict, replay_trace: Path | None = None):
        return api.run_workflow(wf_fqdn=NS + wf, payload=payload, snapshot_root=str(self.snapshot),
                                data_root=str(self.data_root), replay_trace=replay_trace)

    def _read(self, name: str) -> str:
        path = self.data_root / STORE / name
        return path.read_text() if path.is_file() else ""

    def _json(self, name: str) -> dict:
        text = self._read(name)
        return json.loads(text) if text else {}

    def _lines(self, name: str) -> list[dict]:
        return [json.loads(line) for line in self._read(name).splitlines() if line.strip()]

    def models(self) -> dict:
        return self._json("models.json")

    def times_in_service(self) -> dict:
        return self._json("times_in_service.json")

    def prompt_records(self, upid: str | None = None) -> list[dict]:
        return [e["record"] for e in self._lines("user_prompt_records.jsonl")
                if upid is None or e.get("stream_id") == upid]

    def operations(self) -> list[dict]:
        return [e["record"] for e in self._lines("model_operations.jsonl")]


def trace_events(result) -> list[dict]:
    return [json.loads(line) for f in sorted(Path(result.trace_dir).glob("*.jsonl"))
            for line in f.read_text().splitlines() if line.strip()]


def announced(result) -> list[str]:
    return [e["detail"]["ev_fqdn"] for e in trace_events(result) if e.get("event_type") == "EVENT"]


def offered_words(result) -> list[str]:
    return [c["word"] for e in trace_events(result)
            if e.get("event_type") == "CT_STEP" and (e.get("detail") or {}).get("purity") == "ct_impure"
            for c in (e["detail"].get("outcome") or {}).get("candidates", [])]


# The one content a replay cannot reproduce: the identity an append-only store gives a record is read
# from the clock when it is written. It sits inside `detail`, which the platform's evidence
# classification declares determinative while stating it does not claim a caller-filled detail holds
# only determinative content. Until that classification separates it, the comparison names it rather
# than ignoring it silently: every other difference fails.
STORE_ASSIGNED = "record_id"


def differences(a, b, path: str = "") -> list[str]:
    """Every path at which two decoded JSON values differ."""
    if isinstance(a, dict) and isinstance(b, dict):
        return [d for k in sorted(set(a) | set(b)) for d in differences(a.get(k), b.get(k), f"{path}.{k}")]
    if isinstance(a, list) and isinstance(b, list) and len(a) == len(b):
        return [d for i, (x, y) in enumerate(zip(a, b)) for d in differences(x, y, f"{path}[{i}]")]
    return [] if a == b else [path]


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
        data_root = Path(tempfile.mkdtemp(prefix="pgc_model_response_validation_"))
    else:
        stores = keep / STORE
        if stores.exists() and any(stores.iterdir()):
            print(f"{stores} is not empty — this run accumulates state and must start from no "
                  f"model_response stores.\nRemove that directory, or name a root without one.")
            return 1
        keep.mkdir(parents=True, exist_ok=True)
        data_root = keep

    run = Run(snapshot, data_root)
    replay_root: Path | None = None
    results: list[tuple[str, bool | None, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, held, detail))

    def refusal(upid: str) -> tuple[str | None, str | None]:
        records = run.prompt_records(upid)
        return (records[0].get("outcome"), records[0].get("reason")) if len(records) == 1 else (None, None)

    try:
        # 1 — registration
        key = identity_key("teller", 40, "fp-teller")
        r = run("WF_REGISTER_MODEL_V0", registration("teller", 40, "fp-teller"))
        model = run.models().get(key, {})
        check("model staff register a model, and it is held as registered under its identity",
              r.status == "SUCCESS" and len(run.models()) == 1 and model.get("state") == "REGISTERED",
              f"status {r.status}, {len(run.models())} model(s), state {model.get('state')}")

        # 2 — the same model registered twice, its description written in another order
        again = registration("teller", 40, "fp-teller")
        again["description"] = {"reading_capacity": 40, "name": "teller"}
        r = run("WF_REGISTER_MODEL_V0", again)
        check("the same model is not registered twice, however its description is written",
              r.status != "SUCCESS" and len(run.models()) == 1, f"status {r.status}")

        # 3 — placed in service
        r = run("WF_PLACE_MODEL_IN_SERVICE_V0", placement(key, "tis-01"))
        tis = run.times_in_service().get("tis-01", {})
        check("a registered model is placed in service, with a time in service that is open",
              r.status == "SUCCESS" and run.models()[key].get("state") == "IN_SERVICE"
              and tis.get("state") == "OPEN" and run.models()[key].get("time_in_service_id") == "tis-01",
              f"status {r.status}, model {run.models()[key].get('state')}, time in service {tis.get('state')}")

        # 4 — placed again while in service
        r = run("WF_PLACE_MODEL_IN_SERVICE_V0", placement(key, "tis-02"))
        check("a model already in service is not placed in service again",
              r.status != "SUCCESS" and "tis-02" not in run.times_in_service(), f"status {r.status}")

        # The stores as the first user prompt finds them, kept for its replay.
        replay_root = Path(tempfile.mkdtemp(prefix="pgc_model_response_replay_"))
        shutil.copytree(data_root / STORE, replay_root / STORE)

        # 5 — a user prompt answered
        responded = run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-01", key))
        record = (run.prompt_records("up-01") or [{}])[0]
        check("a user prompt is answered, and its record says it was responded to",
              responded.status == "SUCCESS" and record.get("outcome") == "RESPONDED",
              f"status {responded.status}, outcome {record.get('outcome')}")
        check("no word the model offered reached the response unless the rules permitted it",
              record.get("response") == MATERIAL and ANOTHER_CUSTOMERS_ACCOUNT not in record.get("response", "")
              and offered_words(responded).count(ANOTHER_CUSTOMERS_ACCOUNT) == len(MATERIAL.split()),
              f"response {record.get('response')!r}; another customer's number offered "
              f"{offered_words(responded).count(ANOTHER_CUSTOMERS_ACCOUNT)} time(s)")
        rif = record.get("rules_in_force") or {}
        check("the record keeps what the model read and the rules in force, seed included",
              record.get("reading") == {"system_prompt": "Answer only from the supporting material.",
                                        "question": "What is my balance?", "supporting_material": MATERIAL}
              and rif.get("seed") == 7 and rif.get("freedom") == 0
              and any(f.get("except") == [OWN_ACCOUNT] for f in rif.get("forbidden", []))
              and record.get("time_in_service_id") == "tis-01",
              f"rules in force {rif}")

        # 6 — refusals, each recorded with its reason
        cases = []
        cases.append(("up-02", "a user prompt for a customer the requester is not permitted to act for",
                      prompt("up-02", key, customer="customer-99"), "requester_not_permitted_for_customer"))
        cases.append(("up-03", "a user prompt to a model the business never registered",
                      prompt("up-03", identity_key("ghost", 40, "fp-ghost")), "model_not_registered"))
        cases.append(("up-04", "a user prompt carrying information above the model's ceiling",
                      prompt("up-04", key, kind="restricted"), "kind_above_sensitivity_ceiling"))
        cases.append(("up-05", "a user prompt longer than the model can read at once",
                      prompt("up-05", key, material=" ".join(["word"] * 40)),
                      "reading_longer_than_model_can_read"))
        cases.append(("up-06", "a response in which no word the model offered is permitted",
                      prompt("up-06", key, material="Returns are guaranteed always"),
                      "another_customers_account_number"))
        refused_results = {}
        for upid, criterion, payload, reason in cases:
            refused_results[upid] = run("WF_SUBMIT_USER_PROMPT_V0", payload)
            outcome, got = refusal(upid)
            check(f"{criterion} is refused, and recorded with its reason",
                  outcome == "REFUSED" and got == reason, f"outcome {outcome}, reason {got}")
        stopped = (run.prompt_records("up-06") or [{}])[0]
        check("a response a rule stopped is not given, not even the words written before the stop",
              stopped.get("response") in (None, "") and stopped.get("reason") == "another_customers_account_number",
              f"response {stopped.get('response')!r}")

        # 7 — a user prompt identity claimed twice
        before = len(run.prompt_records("up-01"))
        r = run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-01", key, material="Account balance 99."))
        check("a user prompt identity already claimed is refused, and its record is not written twice",
              r.status != "SUCCESS" and len(run.prompt_records("up-01")) == before == 1
              and run.prompt_records("up-01")[0].get("response") == MATERIAL, f"status {r.status}")

        # 8 — the longest response
        short_key = identity_key("brief", 40, "fp-brief")
        run("WF_REGISTER_MODEL_V0", registration("brief", 40, "fp-brief"))
        run("WF_PLACE_MODEL_IN_SERVICE_V0", placement(short_key, "tis-brief", longest=2))
        run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-07", short_key))
        outcome, reason = refusal("up-07")
        check("a response that reaches the longest the business allows is refused, not cut short",
              outcome == "REFUSED" and reason == "longest_response_reached", f"outcome {outcome}, reason {reason}")

        # 9 — several models in service at once
        in_service = [k for k, m in run.models().items() if m.get("state") == "IN_SERVICE"]
        r = run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-08", key, material="Balance 40."))
        check("several models are in service at once, and each answers its own user prompts",
              len(in_service) == 2 and refusal("up-08")[0] == "RESPONDED"
              and (run.prompt_records("up-07") or [{}])[0].get("time_in_service_id") == "tis-brief",
              f"{len(in_service)} in service")

        # 10 — a model registered but never placed
        idle_key = identity_key("idle", 40, "fp-idle")
        run("WF_REGISTER_MODEL_V0", registration("idle", 40, "fp-idle"))
        run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-09", idle_key))
        outcome, reason = refusal("up-09")
        check("a user prompt to a model not in service is refused",
              outcome == "REFUSED" and reason == "model_not_in_service", f"outcome {outcome}, reason {reason}")

        # 11 — retrieval
        r = run("WF_RETRIEVE_USER_PROMPT_RECORD_V0", {**STAFF, "user_prompt_id": "up-01"})
        got = r.surface.get("user_prompt_record")
        got = got[0] if isinstance(got, list) and got else got
        got = (got or {}).get("record", got) if isinstance(got, dict) else got
        check("model staff retrieve a user prompt record, and are handed the record",
              r.status == "SUCCESS" and isinstance(got, dict) and got.get("response") == MATERIAL,
              f"status {r.status}, surface keys {sorted(r.surface)}")
        ops_before = len(run.operations())
        r_clerk = run("WF_RETRIEVE_USER_PROMPT_RECORD_V0", {**NOT_STAFF, "user_prompt_id": "up-01"})
        r_reg = run("WF_REGISTER_MODEL_V0", registration("rogue", 40, "fp-rogue", staff=NOT_STAFF))
        check("anyone who is not model staff is refused retrieval and registration, and leaves no trail",
              r_clerk.status != "SUCCESS" and r_reg.status != "SUCCESS"
              and identity_key("rogue", 40, "fp-rogue") not in run.models()
              and len(run.operations()) == ops_before,
              f"retrieve {r_clerk.status}, register {r_reg.status}")

        # 12 — withdrawal
        r = run("WF_WITHDRAW_MODEL_FROM_SERVICE_V0", {**STAFF, "identity_key": key})
        check("a model withdrawn from service is registered again, and its time in service is closed",
              r.status == "SUCCESS" and run.models()[key].get("state") == "REGISTERED"
              and run.times_in_service()["tis-01"].get("state") == "CLOSED",
              f"status {r.status}, model {run.models()[key].get('state')}, "
              f"time in service {run.times_in_service()['tis-01'].get('state')}")
        run("WF_SUBMIT_USER_PROMPT_V0", prompt("up-10", key))
        outcome, reason = refusal("up-10")
        check("a user prompt to a withdrawn model is refused as not in service",
              outcome == "REFUSED" and reason == "model_not_in_service", f"outcome {outcome}, reason {reason}")

        # 13 — a new time in service, never an old one again
        r_old = run("WF_PLACE_MODEL_IN_SERVICE_V0", placement(key, "tis-01"))
        r_new = run("WF_PLACE_MODEL_IN_SERVICE_V0", placement(key, "tis-03"))
        check("a withdrawn model returns under a new time in service, never a closed one",
              r_old.status != "SUCCESS" and r_new.status == "SUCCESS"
              and run.times_in_service()["tis-01"].get("state") == "CLOSED"
              and run.models()[key].get("time_in_service_id") == "tis-03",
              f"old id {r_old.status}, new id {r_new.status}")

        # 14 — the trail and the moments
        ops = [o.get("operation") for o in run.operations()]
        check("every staff operation that completed is in the operation trail",
              ops.count("REGISTER_MODEL") == 3 and ops.count("PLACE_MODEL_IN_SERVICE") == 3
              and ops.count("WITHDRAW_MODEL_FROM_SERVICE") == 1
              and ops.count("RETRIEVE_USER_PROMPT_RECORD") == 1, f"trail {ops}")
        check("a responded user prompt announces that it was responded to, and nothing else",
              announced(responded) == [RESPONDED], f"announced {announced(responded)}")
        refused_announced = {u: announced(x) for u, x in refused_results.items()}
        check("every refused user prompt announces that it was refused",
              all(a == [REFUSED] for a in refused_announced.values()), f"announced {refused_announced}")

        # 15 — replay
        trace_file = next(Path(responded.trace_dir).glob("*.jsonl"))
        try:
            # Replayed against the stores as the original found them, so it reads what the original
            # read; only the model's offers come from the record rather than the model.
            replayed = api.run_workflow(wf_fqdn=NS + "WF_SUBMIT_USER_PROMPT_V0", payload=prompt("up-01", key),
                                        snapshot_root=str(snapshot), data_root=str(replay_root),
                                        replay_trace=trace_file)
            replay_record = (Run(snapshot, replay_root).prompt_records("up-01") or [{}])[0]
            original_events = determinative(trace_file)
            replayed_events = determinative(next(Path(replayed.trace_dir).glob("*.jsonl")))
            paths = [f"event {n}{d}" for n, (x, y) in enumerate(zip(original_events, replayed_events))
                     for d in differences(x, y)]
            other = [p for p in paths if not p.endswith(f".{STORE_ASSIGNED}")]
            held = len(original_events) == len(replayed_events) and not other
            detail = (f"{len(original_events)} vs {len(replayed_events)} events; differing: {other[:5]}"
                      if not held else f"{len(paths)} store-assigned record identities differ")
            replayed_offers = [e for e in trace_events(replayed) if e.get("event_type") == "CT_STEP"
                               and (e.get("detail") or {}).get("purity") == "ct_impure"]
            check("a replay reproduces the response from the recorded offers, without consulting the model",
                  replayed.status == "SUCCESS" and replay_record.get("response") == MATERIAL
                  and all(e["detail"].get("replayed") for e in replayed_offers),
                  f"status {replayed.status}, response {replay_record.get('response')!r}")
            check("the replay and the original agree on every determinative event but the store's "
                  "clock-assigned record identity", held, detail)
        finally:
            shutil.rmtree(replay_root, ignore_errors=True)

    finally:
        if replay_root is not None:
            shutil.rmtree(replay_root, ignore_errors=True)
        width = max(len(c) for c, _, _ in results) if results else 0
        for criterion, held, detail in results:
            mark = "SKIP" if held is None else ("OK  " if held else "FAIL")
            print(f"  {mark}  {criterion}")
            if detail and held is not True:
                print(f"          {detail}")
        exercised = [h for _, h, _ in results if h is not None]
        print(f"\n  {sum(exercised)}/{len(exercised)} criteria hold")
        if keep is None:
            shutil.rmtree(data_root, ignore_errors=True)
        else:
            print(f"  stores left at {data_root}")

    return 0 if results and all(h is not False for _, h, _ in results) else 1


if __name__ == "__main__":
    sys.exit(main())
