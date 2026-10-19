"""The host of a model in service — outside PGC, holding no authority.

A hosted response is written by three governed acts, and the host drives them. It begins a request on
the requester's behalf and receives what the model reads. It then asks its model for the likeliest
next tokens and offers them, one step at a time. Finally, once the business has chosen an end, it asks
for release. The business chooses every token, records every step and releases the text it built; the
host only relays. Nothing in PGC calls the host, so no act waits on a model.

A model here is anything that answers `offer(reading, text)` with candidates and the number of tokens
it read, and names its `fingerprint`:

- `OllamaModel` — a pretrained model served locally by Ollama, asked for its top candidates one token at
  a time with thinking turned off. Its fingerprint is the digest Ollama reports.
- `TestModel` — the business's test model, the same one the unhosted way consults, offering whole
  words as tokens. It lets the hosted way be proven without a model installed.

Run:  python business_domains/causal_language_model/host/driver.py [--model qwen3:8b | --model test] [--ungrounded]
"""

from __future__ import annotations

import json
import math
import sys
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Protocol

NS = "causal_language_model::"
BEGIN, OFFER, RELEASE = (NS + "WF_BEGIN_HOSTED_RESPONSE_V0", NS + "WF_OFFER_NEXT_TOKENS_V0",
                         NS + "WF_RELEASE_HOSTED_RESPONSE_V0")
END = "<end>"


class Model(Protocol):
    fingerprint: str

    def offer(self, reading: dict, text: str) -> tuple[list[dict], int]: ...


class OllamaModel:
    """A model Ollama serves, asked for its likeliest next tokens with thinking off."""

    ENDS = {"<|im_end|>", "<|endoftext|>", ""}

    def __init__(self, name: str = "qwen3:8b", url: str = "http://localhost:11434", top: int = 5):
        self.name, self.url, self.top = name, url, top
        tags = self._call("/api/tags", None)["models"]
        self.fingerprint = next(m["digest"] for m in tags if m["name"] == name)
        self._reading_size: int | None = None

    def _call(self, path: str, body: dict | None) -> dict:
        request = urllib.request.Request(self.url + path, data=json.dumps(body).encode() if body else None,
                                         headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(request, timeout=120) as response:
            return json.load(response)

    @staticmethod
    def prompt(reading: dict) -> str:
        user = reading["question"]
        if reading.get("supporting_material"):
            user += "\n\n" + reading["supporting_material"]
        return (f"<|im_start|>system\n{reading['system_prompt']}<|im_end|>\n"
                f"<|im_start|>user\n{user} /no_think<|im_end|>\n"
                "<|im_start|>assistant\n<think>\n\n</think>\n\n")

    def offer(self, reading: dict, text: str) -> tuple[list[dict], int]:
        out = self._call("/api/generate", {
            "model": self.name, "prompt": self.prompt(reading) + text, "raw": True, "stream": False,
            "logprobs": True, "top_logprobs": self.top, "keep_alive": "10m",
            "options": {"num_predict": 1, "temperature": 0}})
        if self._reading_size is None:
            # What the model reads, counted once, before anything is written.
            self._reading_size = out["prompt_eval_count"] + out.get("prompt_eval_cached_count", 0)
        step = (out.get("logprobs") or [{}])[0]
        top = step.get("top_logprobs") or []
        if not top:
            top = [{"token": END if out.get("done_reason") == "stop" else out["response"], "logprob": 0.0}]
        return ([{"token": END if t["token"] in self.ENDS else t["token"], "likelihood": math.exp(t["logprob"])}
                 for t in top], self._reading_size)


class TestModel:
    """The business's test model, offering its words as tokens."""

    fingerprint = "fp-test-model"

    def offer(self, reading: dict, text: str) -> tuple[list[dict], int]:
        from causal_language_model.implementation.capability_transforms.atoms import ct_impure_offer_next_words_v0
        words = ct_impure_offer_next_words_v0.execute(
            {"reading": reading, "text": text, "finished": False, "stopped_by": "none"})["candidates"]
        size = len(" ".join(str(v) for v in reading.values()).split())
        return ([{"token": c["word"] if c["word"] == END or not text else " " + c["word"],
                  "likelihood": c["likelihood"]} for c in words], size)


@dataclass
class Outcome:
    """How a hosted request ended, as the host saw it."""
    status: str               # RESPONDED or REFUSED, as recorded; REJECTED when nothing was recorded
    act: str                  # the act that ended it
    text: str = ""
    steps: list[dict] = field(default_factory=list)
    surface: dict = field(default_factory=dict)


class Host:
    """Drives the three acts for one model. `act(wf_fqdn, payload)` dispatches a governed act."""

    def __init__(self, act: Callable, model: Model, host_id: str = "host-01"):
        self.act, self.model, self.host_id = act, model, host_id

    def respond(self, request: dict) -> Outcome:
        begun = self.act(BEGIN, request)
        if "opening_record" not in begun.surface:
            return self._ended(begun, "begin", "", [])
        reading = begun.surface["opening_record"]["reading"]
        upid, text, steps = request["user_prompt_id"], "", []
        while True:
            candidates, size = self.model.offer(reading, text)
            offered = self.act(OFFER, {"user_prompt_id": upid, "host_id": self.host_id,
                                       "fingerprint": self.model.fingerprint,
                                       "reported_reading_size": size, "candidates": candidates})
            if "step_record" not in offered.surface:
                return self._ended(offered, "offer", text, steps)
            step = offered.surface["step_record"]
            steps.append(step)
            if step["finished"]:
                break
            text += step["chosen"]
        return self._ended(self.act(RELEASE, {"user_prompt_id": upid, "host_id": self.host_id}),
                           "release", text, steps)

    @staticmethod
    def _ended(result, act: str, text: str, steps: list[dict]) -> Outcome:
        """An act ends a request by recording it closed; any other ending changed nothing."""
        record = result.surface.get("user_prompt_record") or {}
        return Outcome(record.get("outcome") or "REJECTED", act, record.get("response") or text, steps,
                       result.surface)


def _demo() -> int:
    here = Path(__file__).resolve()
    workspace = here.parents[3]
    for root in (workspace / "software_governance", workspace / "business_domains"):
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
    sys.path.insert(0, str(here.parents[1] / "testbed" / "hosted_model"))
    from execution_validation import demo  # noqa: E402
    return demo(sys.argv[1:])


if __name__ == "__main__":
    raise SystemExit(_demo())
