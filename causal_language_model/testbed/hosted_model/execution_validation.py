"""Execution validation — run the hosted way against the acceptance criteria cr_02 declared.

A hosted model proposes and the business decides. Every criterion here dispatches the three hosted
acts through `protocol_runtime` against a fresh data root, driven by the host in
`causal_language_model/host/driver.py`, and reads the record trail the acts left.

Three models drive it:

- the test model, which offers another customer's account number before every word, so a response
  equal to the supporting material is evidence the rules decided what was written;
- a scripted model, which makes the offers a criterion needs and nothing else: an account number split
  across tokens, an offer with only forbidden tokens, a reported size too large, a stopped host;
- Qwen3 8B through Ollama, only with `--qwen`. Its words are not determined, so the regression leaves
  it out and its criterion is reported as not exercised.

Run:  python business_domains/causal_language_model/testbed/hosted_model/execution_validation.py [snapshot] [--qwen]
      ... --data-root <path>     keep the stores and traces instead of discarding them
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

for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains"):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from causal_language_model.host.driver import (BEGIN, END, OFFER, RELEASE, Host, OllamaModel,  # noqa: E402
                                               TestModel)

NS = "causal_language_model::"
STORE = "causal_language_model/model_response"
OWN, OTHER = "12345678", "87654321"
MATERIAL = f"Account {OWN} balance 40."
STAFF = {"staff_credentials": {"staff_id": "staff-01", "role": "model_staff"}, "staff_id": "staff-01"}
SYSTEM = "You are a bank assistant. Answer in one short sentence, only from the supporting material."


class ScriptedModel:
    """Offers what it is told, step by step, under the fingerprint it is given."""

    def __init__(self, fingerprint: str, script: list[list[str]], size: int = 20):
        self.fingerprint, self.script, self.size = fingerprint, list(script), size

    def offer(self, reading: dict, text: str) -> tuple[list[dict], int]:
        tokens = self.script.pop(0)
        return [{"token": t, "likelihood": round(0.9 - 0.1 * i, 2)} for i, t in enumerate(tokens)], self.size


def description(name: str, capacity: int, longest: int) -> dict:
    return {"name": name, "reading_capacity": capacity, "maximum_response_length": longest}


def identity_key(desc: dict, fingerprint: str) -> str:
    return json.dumps(desc, sort_keys=True, separators=(",", ":")) + "|" + fingerprint


def rules(longest: int = 40, grounded: bool = False) -> dict:
    stated = {"forbidden": [{"rule": "no_guarantees", "pattern": r"(?i)\bguarantee"}],
              "account_number_pattern": "[0-9](?:[ -]?[0-9]){7}", "freedom": 0, "longest_response": longest}
    return {**stated, "ground_numbers": True} if grounded else stated


def request(upid: str, key: str, material: str = MATERIAL, question: str = "What is my balance?", **extra) -> dict:
    return {"user_prompt_id": upid, "requester_id": "agent-01", "permitted_customers": ["customer-01"],
            "customer_id": "customer-01", "account_numbers": [OWN], "identity_key": key, "kind": "internal",
            "question": question, "supporting_material": material, "seed": 7, **extra}


class Stage:
    """A data root, the acts dispatched against it, and the trail they leave."""

    def __init__(self, snapshot: Path, data_root: Path):
        self.snapshot, self.data_root, self.traces = snapshot, data_root, []

    def act(self, wf: str, payload: dict):
        result = api.run_workflow(wf_fqdn=wf, payload=payload, snapshot_root=str(self.snapshot),
                                  data_root=str(self.data_root))
        self.traces.append(result.trace_dir)
        return result

    def serve(self, name: str, fingerprint: str, capacity: int = 400, longest: int = 40, tis: str = "",
              grounded: bool = False) -> str:
        desc = description(name, capacity, longest)
        key = identity_key(desc, fingerprint)
        assert "SUCCESS" == self.act(NS + "WF_REGISTER_MODEL_V0",
                                     {**STAFF, "description": desc, "fingerprint": fingerprint}).status
        assert "SUCCESS" == self.act(NS + "WF_PLACE_MODEL_IN_SERVICE_V0", {
            **STAFF, "identity_key": key, "time_in_service_id": tis or f"tis-{name}", "ceiling": "confidential",
            "system_prompt": SYSTEM, "response_rules": rules(grounded=grounded)}).status
        return key

    def trail(self, upid: str) -> list[dict]:
        path = self.data_root / STORE / "user_prompt_records.jsonl"
        entries = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        return [e["record"] for e in sorted(entries, key=lambda e: e["sequence_number"]) if e["stream_id"] == upid]


def run(snapshot: Path, with_qwen: bool, keep: Path | None = None) -> list[tuple[str, bool | None, str]]:
    data_root = keep or Path(tempfile.mkdtemp(prefix="pgc_hosted_validation_"))
    stage, results = Stage(snapshot, data_root), []

    def check(criterion: str, held: bool | None, detail: str = "") -> None:
        results.append((criterion, held, detail))

    def outcomes(upid: str) -> list[str]:
        return [r.get("outcome") for r in stage.trail(upid)]

    try:
        test = TestModel()
        key = stage.serve("test", test.fingerprint)
        host = Host(stage.act, test)

        # 1, 12 — admitted as the test model's requests are, and answered through the hosted way
        answered = host.respond(request("h-01", key))
        trail = stage.trail("h-01")
        check("an authorized requester's request to a hosted model in service is admitted, and its record opens",
              trail[0].get("outcome") == "WRITING" and trail[0].get("fingerprint") == test.fingerprint,
              f"trail {outcomes('h-01')}")
        check("the test model answers through the hosted way, under the same rules",
              answered.status == "RESPONDED" and answered.text == MATERIAL,
              f"{answered.status}, {answered.text!r}")
        refused_at_begin = {
            "h-02": (request("h-02", key, customer_id="customer-99"), "requester_not_permitted_for_customer"),
            "h-03": (request("h-03", identity_key(description("ghost", 400, 40), "fp-ghost")), "model_not_registered"),
            "h-04": (request("h-04", key, kind="restricted"), "kind_above_sensitivity_ceiling"),
            "h-05": (request("h-05", key, material=" ".join(["word"] * 400)), "reading_longer_than_model_can_read"),
        }
        got = {u: (host.respond(p).status, (stage.trail(u) or [{}])[-1].get("reason")) for u, (p, _) in refused_at_begin.items()}
        check("a hosted request is refused under the same conditions as a request to the test model",
              all(got[u] == ("REFUSED", reason) for u, (_, reason) in refused_at_begin.items()), f"{got}")

        # 3 — the offer and the choice are recorded at every step
        steps = [r for r in stage.trail("h-01") if r.get("outcome") == "STEP"]
        check("at each step a permitted candidate is chosen, and the record keeps the offer and the choice",
              len(steps) == len(MATERIAL.split()) + 1
              and all(s["candidates"] and s["chosen"] in [c["token"] for c in s["candidates"]] for s in steps)
              and all(any(x["token"].strip() == OTHER for x in s["stopped"]) for s in steps[:-1]),
              f"{len(steps)} step(s)")

        # 8 — released from the record, exactly as chosen
        closing = stage.trail("h-01")[-1]
        chosen = "".join(s["chosen"] for s in steps if s["chosen"] != END)
        check("a completed response is released from the business's record, exactly as the business chose it",
              closing.get("outcome") == "RESPONDED" and closing.get("response") == chosen == MATERIAL,
              f"released {closing.get('response')!r}, chosen {chosen!r}")

        # 2 — a reported reading too large, refused before any token is chosen
        big = Host(stage.act, ScriptedModel(test.fingerprint, [["Your"]], size=401))
        o = big.respond(request("h-06", key))
        check("a reported reading larger than the model's capacity is refused before any token is chosen",
              o.status == "REFUSED" and outcomes("h-06") == ["WRITING", "REFUSED"]
              and stage.trail("h-06")[-1].get("reason") == "reading_longer_than_model_can_read",
              f"trail {outcomes('h-06')}")

        # 4 — an account number split across tokens is not written; the customer's own is
        split = Host(stage.act, ScriptedModel(test.fingerprint, [["Account"], [" 8765"], ["4321", " is"], [END]]))
        o = split.respond(request("h-07", key))
        own = Host(stage.act, ScriptedModel(test.fingerprint, [["Account"], [" 1234"], ["5678"], [END]]))
        p = own.respond(request("h-08", key))
        check("an account number split across tokens is not written, and the customer's own is",
              o.status == "RESPONDED" and o.text == "Account 8765 is" and p.text == f"Account {OWN}",
              f"{o.text!r}, {p.text!r}")

        # 5 — an offer for another model
        other = Host(stage.act, ScriptedModel("fp-other", [["Your"]]))
        o = other.respond(request("h-09", key))
        check("an offer naming another model's fingerprint is refused",
              o.status == "REFUSED" and stage.trail("h-09")[-1].get("reason") == "offer_for_another_model",
              f"trail {outcomes('h-09')}")

        # 6 — every candidate forbidden
        forbidden = Host(stage.act, ScriptedModel(test.fingerprint, [["Returns"], [" guaranteed", " Guaranteed"]]))
        o = forbidden.respond(request("h-10", key))
        check("when every candidate is forbidden the request is refused, and the record names the rule",
              o.status == "REFUSED" and stage.trail("h-10")[-1].get("reason") == "no_guarantees"
              and stage.trail("h-10")[-1].get("response") in (None, ""),
              f"trail {outcomes('h-10')}, reason {stage.trail('h-10')[-1].get('reason')}")

        # 7 — the permitted length reached unfinished
        short = stage.serve("short", "fp-short", longest=2)
        long = Host(stage.act, ScriptedModel("fp-short", [["Your"], [" balance"], [" is"]]))
        o = long.respond(request("h-11", short))
        check("a response that reaches its permitted length before it is complete is refused, not released",
              o.status == "REFUSED" and stage.trail("h-11")[-1].get("reason") == "longest_response_reached",
              f"trail {outcomes('h-11')}")

        # grounding — numbers come from what the model read
        grounded = stage.serve("grounded", "fp-grounded", grounded=True)
        read = Host(stage.act, ScriptedModel("fp-grounded", [["Balance"], [" 9", " 4"], ["1", "0"], [" dollars"], [END]]))
        o = read.respond(request("h-13", grounded))
        made_up = Host(stage.act, ScriptedModel("fp-grounded", [["Balance"], [" 7"]]))
        p = made_up.respond(request("h-14", grounded))
        check("where grounding is set, a number is written only if the model read it, and one it did not refuses the request",
              o.status == "RESPONDED" and o.text == "Balance 40 dollars"
              and p.status == "REFUSED" and stage.trail("h-14")[-1].get("reason") == "numbers_from_the_reading",
              f"{o.status} {o.text!r}; {p.status} {stage.trail('h-14')[-1].get('reason')}")

        # 9 — the host stops offering
        stage.act(BEGIN, request("h-12", key))
        stage.act(OFFER, {"user_prompt_id": "h-12", "host_id": "host-01", "fingerprint": test.fingerprint,
                          "reported_reading_size": 20, "candidates": [{"token": "Your", "likelihood": 0.9}]})
        early = stage.act(RELEASE, {"user_prompt_id": "h-12", "host_id": "host-01"})
        check("a response the host stops offering for stays open, and is never released",
              outcomes("h-12") == ["WRITING", "STEP"] and "user_prompt_record" not in early.surface,
              f"trail {outcomes('h-12')}")

        # 10 — every hosted request has a record from its admission
        upids = ["h-01", "h-06", "h-07", "h-08", "h-09", "h-10", "h-11", "h-12", "h-13", "h-14"]
        check("every hosted request, released, refused or abandoned, has a record from its admission",
              all(outcomes(u)[0] == "WRITING" for u in upids)
              and all(outcomes(u) == ["REFUSED"] for u in refused_at_begin), "")

        # 11 — the test model's own way
        r = stage.act(NS + "WF_SUBMIT_USER_PROMPT_V0", request("u-01", key))
        check("the test model's existing way of answering behaves as before",
              r.status == "SUCCESS" and outcomes("u-01") == ["RESPONDED"]
              and stage.trail("u-01")[0].get("response") == MATERIAL, f"trail {outcomes('u-01')}")

        # 13 — Qwen3 8B
        if with_qwen:
            qwen = OllamaModel("qwen3:8b")
            qkey = stage.serve("Qwen3 8B", qwen.fingerprint, capacity=4096, longest=60, grounded=True)
            o = Host(stage.act, qwen).respond(request(
                "q-01", qkey, material=f"Checking account {OWN}, balance $2,410.55.",
                question="What is my checking balance?"))
            record = stage.trail("q-01")[-1]
            check("Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way",
                  o.status == "RESPONDED" and record.get("response") == o.text and "2,410.55" in o.text,
                  f"{o.status}: {o.text!r}")
        else:
            check("Qwen3 8B, registered with its host's fingerprint, answers a customer through the hosted way",
                  None, "run with --qwen and Ollama serving qwen3:8b")

        # 14 — traced
        check("every act performed left a trace to audit",
              all(any(Path(t).glob("*.jsonl")) for t in stage.traces), f"{len(stage.traces)} act(s)")
    finally:
        if keep is None:
            shutil.rmtree(data_root, ignore_errors=True)
    return results


def demo(args: list[str]) -> int:
    """Answer one question through the hosted way and show every step."""
    name = args[args.index("--model") + 1] if "--model" in args else "qwen3:8b"
    data_root = Path(tempfile.mkdtemp(prefix="pgc_hosted_demo_"))
    stage = Stage(WORKSPACE / "snapshot", data_root)
    model = TestModel() if name == "test" else OllamaModel(name)
    grounded = "--ungrounded" not in args
    key = stage.serve(name, model.fingerprint, capacity=4096, longest=60, grounded=grounded)
    o = Host(stage.act, model).respond(request(
        "demo-01", key, material=f"Checking account {OWN}, balance $2,410.55. Spouse account {OTHER}.",
        question="What are my balance and my spouse's account number?"))
    for s in o.steps:
        stopped = ", ".join(f"{x['token']!r} by {x['rule']}" for x in s["stopped"])
        print(f"  {s['position']:>3}  {s['chosen']!r:<16} {('stopped ' + stopped) if stopped else ''}")
    reason = o.surface.get("user_prompt_record", {}).get("reason")
    print(f"\n  {o.status}{' (' + reason + ')' if reason else ''}: {o.text!r}"
          f"   [numbers {'grounded' if grounded else 'not grounded'}]")
    print(f"  record at {data_root / STORE / 'user_prompt_records.jsonl'}")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--qwen"]
    keep: Path | None = None
    if "--data-root" in args:
        i = args.index("--data-root")
        keep = Path(args[i + 1]).expanduser()
        del args[i:i + 2]
        if (keep / STORE).exists() and any((keep / STORE).iterdir()):
            print(f"{keep / STORE} is not empty — this run must start from no model_response stores")
            return 1
        keep.mkdir(parents=True, exist_ok=True)
    snapshot = Path(args[0]) if args else WORKSPACE / "snapshot"
    if not (snapshot / "manifest.json").is_file():
        print(f"no assembled snapshot at {snapshot}")
        return 1
    results = run(snapshot, "--qwen" in sys.argv, keep)
    for criterion, held, detail in results:
        print(f"  {'SKIP' if held is None else ('OK  ' if held else 'FAIL')}  {criterion}")
        if detail and held is not True:
            print(f"          {detail}")
    exercised = [h for _, h, _ in results if h is not None]
    skipped = len(results) - len(exercised)
    print(f"\n  {sum(exercised)}/{len(exercised)} criteria hold" + (f"  ({skipped} not exercised)" if skipped else ""))
    return 0 if all(h is not False for _, h, _ in results) else 1


if __name__ == "__main__":
    sys.exit(main())
