# business_domains

**Real business work, declared as governed protocol.**

Registering a participant, cataloguing a book, licensing an AI agent — work that would be worth
doing whether or not this platform existed. Each domain here is a directory of declarations: a
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
| **`blockchain`** | `identity` | Register a participant, then accept or reject them — keeping a durable record of what they registered with. Reachable over HTTP and the command line, with a web client. |
| **`book_library_mgmt`** | `catalog` | Register works, editions and physical copies; retire and reinstate them; update bibliographic information; search. Ten workflows — the largest surface here. |
| **`ai_governance`** | `agent_governance`, `ai_licensing` | Admit or deny an AI agent's action; provision, deny and reclaim licences. Two subdomains sharing one namespace. |

A **domain is a namespace**; a **subdomain is a division within it**. `ai_governance` is the case
that makes the distinction concrete — two subdomains, one compiled domain, neither a fork of the
other.

Maturity differs, and it is stated rather than implied: `blockchain::identity` is functionally
complete, with three declared rules deliberately deferred to the first function that will consume
its state; `book_library_mgmt` declares events no exit yet announces; `ai_governance` carries no
change dossier and is the least exercised.

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
  cr_dossiers/           the governed record of each change, with its baseline pin
  testbed/               payloads, including ones that must be refused

book_library_mgmt/       same shape; subdomain `catalog`; plus implementation/ transforms
ai_governance/           same shape; two subdomains in one namespace
```

## A change to a domain is itself governed

Each domain carries **change dossiers** — the record of a change from the business problem as stated
(P0) through to the authoring mandate (P8), each phase admissible before the next may be authored.
Every dossier pins the baseline it was approved against, and that pin stays historical: a completed
change is never re-pinned forward.

A change need not author anything. One dossier here produces a **two-line diff** — a defect
correction, fully evidenced, every phase admissible. A lifecycle that can only describe creation
cannot describe maintenance.

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
- Capability transforms are pure and deterministic. Every effect is a declared capability.
- All references are by fully-qualified identity, resolved at compile time. No short names.

## License

Apache-2.0. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE).
