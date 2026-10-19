# business_domains

**Real business work, declared as governed protocol.**

Registering a participant, cataloguing a book, licensing an AI agent, answering a customer through a
language model — work that would be worth doing whether or not this platform existed. Each domain here is a directory of declarations: a
workflow graph, the contracts its nodes name, the intents that admit a request, the events it
announces, the store it writes to. No domain implements admission, routing, persistence, auditing
or refusal. It declares them, and the platform enforces what it declared.

> **New here?** Start with [`ARCHITECTURE.md`](ARCHITECTURE.md) — what this repository is, what it
> owns, and a hands-on walkthrough. For the whole picture, see the
> [organization profile](https://github.com/protocol-governed-computing).

---

## The domains

| Domain | Subdomains | What it does |
|---|---|---|
| **`blockchain`** | `identity`, `wallet` | Register a participant, then accept or reject them — keeping a durable record of what they registered with. An accepted person is then given exactly one wallet, whose creation is recorded as a moment on its own trail. Reachable over HTTP and the command line, with a web client. |
| **`book_library_mgmt`** | `catalog` | Register works, editions and physical copies; retire and reinstate them; update bibliographic information; search. Ten workflows — the largest surface here — of which six announce the business moments they complete. |
| **`ai_governance`** | `agent_governance`, `ai_licensing` | Admit or deny an AI agent's action; provision, deny and reclaim licences. Two subdomains sharing one namespace. |
| **`causal_language_model`** | `model_response` | Register a language model and place it in service under a ceiling, a system prompt and response rules. A customer's question is answered only by a model in service, only on what it may read, and only in text the rules in force permit. A pretrained model, Qwen3 8B, runs outside PGC and proposes each next token; the business chooses, records and releases, and can require every number to be one the model read. Every request is recorded, answered or refused. |

A **domain is a namespace**; a **subdomain is a division within it**. `ai_governance` is the case
that makes the distinction concrete — two subdomains, one compiled domain, neither a fork of the
other.

Maturity differs, and it is stated rather than implied. `blockchain::identity` is functionally
complete; three of its validated criteria are not exercised. Two wait on a function that does not
exist yet — a timed test, and the transaction half of the wallet claim — and one asks about records
older than a run that starts from none. `blockchain::wallet` is
delivered and validated, and it is the domain that demonstrates **consulting** another subdomain's
records without writing them. `book_library_mgmt` announces: six of its ten acts emit the moments
they complete, from the ending that completes them. Both `identity` and the catalog hold every
rule they apply, so a request never states the rules it is judged by. `causal_language_model` answers
through two ways: a test model built to break the rules, and a pretrained model (Qwen3 8B) whose host
proposes each token while the business decides it. The test model's step is not determined by its
inputs, so the domain holds the platform to molecules, recorded outcomes, replay and refusal
moments; the hosted way shows a model outside PGC governed token by token. It has its own
[`README.md`](causal_language_model/README.md) and [`ARCHITECTURE.md`](causal_language_model/ARCHITECTURE.md). `ai_governance` governs
an agent's actions and provisions licences, and it is the least exercised of the four.

**The language model is also where the platform's own defect was found.** Its submission runs one
contract at ten places. Running it showed the platform sealed each such contract's routing once, for
whichever place came last — a collision `ai_governance` had carried unnoticed in two workflows, with
every phase check passing. The compiler now refuses a sealed dispatch that does not realize every
declared transition at its own node.

**The wallet is also where a defect and its repair are on the record.** Its validation once read 7/9
because the suite registered the same people identity's suite registers, so a shared data root left
the unverified-person criterion testing someone already accepted. The suite now seeds people of its
own. Both blockchain suites run into one data root, because a domain has one place its records live.

## Where this sits

```
software_governance          conformance_workloads       business_domains
what is GOVERNED             what PROVES the guarantee   what is DONE  ← here
       └──────────────────────────┼──────────────────────────┘
                                  │
                          compiler → assembler
                                  │
                         ┌────────▼────────┐
                         │ sealed snapshot │
                         └────┬───────┬────┘
                              ▼       ▼
                         runtime   inspector
```

A domain is compiled **against** an already-compiled governance surface. Governance is never edited
to admit a domain — compiling one leaves the platform's identity unchanged. A domain declares its
own sources in its own build manifest, so adding one is a sibling directory and nothing upstream is
touched.

## Run one

```bash
./blockchain/client/serve.sh          # http://localhost:8000
```

Register a name and contact address, then verify that address — accepting or rejecting it. The same
path without the browser:

```bash
curl -s -X POST http://localhost:8000/blockchain -H 'Content-Type: application/json' \
  -d '{"operation":"blockchain.register_actor",
       "params":{"name":"Ada","contact_address":"ada@example.com"}}'
```

```json
{ "outcome": "SUCCESS", "result_class": "SUCCESS",
  "result": { "contact_address": "ada@example.com",
              "occurrence": "ACTOR_REGISTERED_UNVERIFIED", "sequence_number": 1 },
  "evidence": [ "trace:traces/blockchain/WF_REGISTER_ACTOR_V0/…" ] }
```

Accepting an unknown address returns a governed `NOT_FOUND` without writing anything; registering
twice succeeds twice and advances the sequence, because registration is idempotent **by
declaration**. Every response points at the trace for that exact run.

To run a workflow directly against the sealed snapshot, without any web surface:

```bash
cd ../protocol_runtime
./run.sh run --wf blockchain::WF_REGISTER_ACTOR_V0 \
             --payload ../business_domains/blockchain/testbed/identity/test_payloads/01_register_actor.json \
             --data-root /tmp/pgc_instance
```

## Layout

```
blockchain/
  registry/identity/     workflows · intents · contracts · events · actors ·
                         storage structure · runtime bindings · transport contracts
  client/                web client, HTTP binding table, composition launcher
  design/                the design of record: P7 and P8, generated from the registry
  testbed/               payloads, including ones that must be refused

book_library_mgmt/       same shape; subdomain `catalog`; plus implementation/ transforms
ai_governance/           same shape; two subdomains in one namespace
causal_language_model/   same shape; subdomain `model_response`; implementation/ holds the pure
                         transforms and the test model; host/ the driver for a hosted model,
                         outside PGC; doc/ holds the idea and the CR sequence
```

Every domain has an **execution validation** under `testbed/` — a suite that
dispatches its workflows against a fresh data root, one criterion per acceptance criterion, and
prints which hold. The workspace regression runs all of them on every build.

## A change to a domain is itself governed

Each domain carries its **design of record** in `design/`: the P7 design intent and the P8 authoring
mandate, generated from its registry, so the design always states what the domain is. A change is
authored as a **change dossier** in `cr_dossiers/cr_NN_<subject>/`, from the business problem as
stated (P0) through to the authoring mandate (P8). Each phase must be admissible before the next may
be authored. A dossier pins the composition it was approved against, and that pin stays historical:
a completed change is never re-pinned forward. Each phase document carries its registers as data, in
one `## Machine` block.

A change need not author anything. A defect correction may produce a two-line diff, fully evidenced,
with every phase admissible. A lifecycle that can only describe creation cannot describe maintenance.

## What this repository is not

- **Not the platform.** The governance surface is `software_governance`; the runtime that executes
  these domains is `protocol_runtime`, and it contains no knowledge of any domain here.
- **Not a set of examples.** Conformance workloads (`conformance_workloads`) exist to prove a
  guarantee; these exist because the work is worth doing. That both compile by the identical path,
  with no privilege on either side, is the claim.
- **Not a place for platform mechanisms.** When a domain needs something neutral the substrate
  lacks, the substrate gains it — a domain that compensates with a private rule produces a promise
  stated nowhere and copied everywhere.

## Rules

- A domain declares; it does not implement admission, routing, persistence or auditing.
- No import of the compiler, the assembler, the runtime, or another domain. Implementations are
  leaves; cross-domain reference happens through compiled identity.
- Capability transforms have no effects, and are deterministic unless declared otherwise. Every
  effect is a declared capability; every non-deterministic result is recorded and replayable.
- All references are by fully-qualified identity, resolved at compile time. No short names.

## License

Apache-2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
