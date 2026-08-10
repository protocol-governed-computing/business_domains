# Architecture — `business_domains`

**Release 5.** This document is frozen for this release. It describes what this repository is, what
it owns, and what it must never do. It is written to be read before any code, and assumes no prior
familiarity with Protocol-Governed Computing.

For the big picture — what PGC is and how the repositories compose — see
**https://github.com/protocol-governed-computing**.

---

## 1. What this repo is

This is where **actual businesses** are declared. Registering a person, cataloguing a book, granting
an AI agent a licence — work someone would want done whether or not this platform existed.

> Everything else in the composition exists so that a domain here can be written **entirely as
> declaration**. No domain in this repository implements admission, routing, persistence,
> auditing or refusal. It declares them, and the platform enforces what it declared.

The measure of the architecture is how little is left once that is true. A domain here is a
directory of artefacts — a workflow graph, the contracts its nodes name, the intents that admit a
request, the events it announces, the store it writes to — plus, occasionally, a few pure functions
for arithmetic the platform has no opinion about.

**What this repo is not.** It is not the platform, and it is not a set of examples. A conformance
workload exists to prove a guarantee; a domain here exists because the work is worth doing. That
they compile by the identical path, with no privilege on either side, is the claim.

## 2. Where it sits

```
   software_governance          conformance_workloads       business_domains
   what is GOVERNED             what PROVES the             what is DONE
                                guarantee                   (← YOU ARE HERE)
          └──────────────────────────┼─────────────────────────┘
                                     │
                                compiler → assembler
                                     │
                            ┌────────▼────────┐
                            │ sealed snapshot │
                            └────┬───────┬────┘
                                 ▼       ▼
                            runtime   inspector
                          (executes)  (answers about it)
```

A domain here is compiled **against** an already-compiled governance surface. Governance is never
edited to admit a domain — if it were, every domain would be a special case, and "governed" would
mean "accommodated".

## 3. The central idea: a domain declares, it does not implement

The distinction that explains every design choice in this repository:

```
   AN APPLICATION                        A GOVERNED DOMAIN

   validate() in code                    an INTENT declares what is admissible
   if/else routing in code               a GRAPH declares where each outcome goes
   a repository class writing            a CAPABILITY the platform owns performs
   to a database                         the effect, on a declared store
   a logger someone remembered           an EVENT declared at the exit that
   to call                               announces it
        │                                     │
        │  the rule is wherever               │  the rule is one artefact,
        │  someone wrote it                   │  compiled, sealed, and readable
        ▼                                     ▼
   to know the rules, read                to know the rules, read the
   all the code                           declarations — there is nowhere else
                                          for a rule to hide
```

Two consequences are worth stating outright, because they are what the model buys:

**A rule cannot be bypassed by a caller, because there is no other way in.** An inadmissible
request is refused by a declaration, not by code that remembered to check.

**A rule stated in a document and realised in no artefact is checked by nothing.** The inverse of
the above, and the characteristic defect of this repository: it is entirely possible to write a
domain document describing a rule, compile a domain that does not carry it, and have every test
pass. Only executing the function and reading what it left behind catches that.

## 4. The three domains

| domain | subdomains | what it does |
|---|---|---|
| **blockchain** | `identity` | register a participant, then accept or reject them — with a durable record of what they registered with |
| **book_library_mgmt** | `catalog` | register works, editions and physical copies; retire and reinstate them; search |
| **ai_governance** | `agent_governance`, `ai_licensing` | admit or deny an AI agent's action; provision, deny and reclaim licences |

**A domain is a namespace; a subdomain is a division within it.** `ai_governance` is the case that
makes the distinction concrete: two subdomains, one namespace, one compiled domain. They are not two
domains that happen to be filed together, and neither is a fork of the other.

Maturity differs, and pretending otherwise would be the wrong kind of documentation:

- **identity** is functionally complete and reachable over both transport and the command line. Three
  rules it declares are enforced at its boundary but not within it, deliberately deferred to the
  first function that will consume its state.
- **book_library_mgmt** is the largest surface — ten workflows — and has events it declares that no
  exit yet announces.
- **ai_governance** has no change dossier and is the least exercised of the three.

## 5. What it owns, and what it must never do

**It owns:**

- **domain artefacts** — workflows, intents, contracts, transforms, events, actors, storage
  structures, runtime bindings, and each domain's own build manifest;
- **boundary contracts** — the ingress/egress pairs that publish an operation to the outside world;
- **pure implementations** — leaf functions for domain arithmetic;
- **change dossiers** — the governed record of how each domain came to be what it is;
- **clients** — a small web surface where one exists.

**It must never:**

- **import the compiler, the assembler, the runtime, or another domain.** Implementations are
  leaves; cross-domain reference happens through compiled identity, never through Python.
- **have effects inside a transform.** Transforms are pure and deterministic. Every effect is a
  declared capability the platform owns.
- **carry its own copy of a platform mechanism.** When a domain needs something neutral the
  substrate lacks, **the substrate gains it** — a domain that compensates with a private invariant
  produces a rule that travels wherever it is copied and is stated nowhere.
- **change the governance surface to be admitted.** Compiling a domain leaves the platform's
  identity unchanged.

## 6. Try it — register someone, then accept them

Two commands, no prior knowledge:

```bash
cd business_domains
./blockchain/client/serve.sh                  # http://localhost:8000
```

The screens are **Register** and **Verify**. Register a name and a contact address; then verify
that address, accepting or rejecting it. The same thing without the browser:

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

Then accept them:

```bash
curl -s -X POST http://localhost:8000/blockchain -H 'Content-Type: application/json' \
  -d '{"operation":"blockchain.accept_actor",
       "params":{"contact_address":"ada@example.com","verifying_authority":"REGISTRAR"}}'
```

### Four things to notice

**1. The record kept what the person registered with.** Look at the stored actor after acceptance:

```json
{ "contact_address": "ada@example.com", "name": "Ada", "state": "ACCEPTED",
  "currency_preference": "BACHI", "language": "en", "verifying_authority": "REGISTRAR" }
```

Recording a decision **merged into** the record rather than replacing it. That is not an
implementation detail — it is the difference between an operation declared as *write this value* and
one declared as *update these fields*, and getting it wrong silently erased everything the person
registered with while succeeding every time. **Write what does not exist; update what does.**

**2. An unknown address is `NOT_FOUND`, not a crash.** Try accepting `nobody@example.com`. The
refusal is a governed result class, produced without anything being written.

**3. Registering twice succeeds twice, and the sequence number advances.** Registration is
idempotent by declaration: the second call records a further occurrence rather than a duplicate
actor or an error.

**4. Every response carries its own evidence.** The `evidence` field points at the trace for that
exact run — the path actually taken through the compiled graph. You can see the graph itself: the
compiled projection of each workflow is rendered under the snapshot's `behavior_logic/blockchain/`,
and the running server mounts it, so the picture and the run are the same object.

To see the whole composition rather than one domain, run the inspection surface from
`snapshot_inspector` instead — same snapshot, same boundary, different question.

## 7. A change to a domain is itself governed

This is the part of the repository with no counterpart in ordinary software. Each domain carries
**change dossiers**: the record of a change from statement of the business problem through to the
artefacts it produced, each phase admissible before the next may proceed.

```
   P0  the business problem, stated
   P1  the change request                     ┐
   P2  the domain model                       │
   P3  the analysis loop                      │  each phase ADMISSIBLE
   P4  the business model                     │  before the next may
   P5  the business intent                    │  be authored
   P6  the governance intent                  │
   P7  the design intent                      │
   P8  the authoring mandate                  ┘
        │
        ▼
   artefacts — which are then compiled like any others
```

Every dossier pins the **baseline** it was approved against. That pin is historical and stays
historical: a completed change is not re-pinned to today's snapshot, because approving a decision
against facts that arrived later asserts a re-reading of a decision nobody made.

And a change need not author anything. One dossier in this repository emits a **two-line diff** — a
defect correction, fully evidenced, all phases admissible. A lifecycle that can only describe
creation cannot describe maintenance, which is most of what happens to software.

## 8. Layout

```
blockchain/
    registry/identity/      workflows · intents · contracts · events · actors ·
                            storage structure · runtime bindings · transport contracts
    client/                 web client, HTTP binding table, composition launcher
    cr_dossiers/            the governed record of each change, with its baseline pin
    testbed/                payloads, including ones that must be refused

book_library_mgmt/          same shape; subdomain `catalog`; plus implementation/ transforms
ai_governance/              same shape; two subdomains in one namespace
```

Each domain also carries its own build manifest, declaring its sources under **this** repository.
Adding a domain is a sibling directory; nothing upstream is touched.

## 9. Rules this repo enforces

1. **A domain declares; it does not implement** admission, routing, persistence or auditing.
2. **A domain declares its own sources** in its own build manifest and edits nothing upstream.
3. **No import of compiler, assembler, runtime, or another domain.**
4. **Transforms are pure and deterministic**; every effect is a declared capability.
5. **A domain never carries a private copy of a platform mechanism** — the substrate gains it
   instead.
6. **All references are by fully-qualified identity**, resolved at compile time. No short names.
7. **A change is governed by a dossier** whose phases are admissible in order and whose baseline pin
   is historical.
8. **A domain leaves the governance surface's identity unchanged.**

## 10. How to know it works

Each domain has a testbed of payloads, including ones that **must** be refused. Run a workflow
against the sealed snapshot:

```bash
cd ../protocol_runtime
./run.sh run --wf blockchain::WF_REGISTER_ACTOR_V0 \
             --payload ../business_domains/blockchain/testbed/identity/test_payloads/01_register_actor.json \
             --data-root /tmp/pgc_instance
```

A good result is not simply a success. The check that matters for this repository is the one that
catches the characteristic defect in section 3:

> **Execute the function, then read what it left behind.** Compare the stored record against what the
> domain's own documents say the rule is. A rule that is written down and realised in no artefact
> passes every other test there is.

Defect discovery here is a **coverage** property, not a maturity one — a domain is correct where it
has been exercised and unverified everywhere else, and that is true no matter how long it has
existed.

## 11. Where the architecture is explained

This document describes *this repository*. The architecture it realizes is developed in the papers
indexed at **https://github.com/protocol-governed-computing**:

- **An Architecture for Closed-Loop Governed Transformation** — the lifecycle the change dossiers
  are the output of, and why a change to a domain is itself a governed act.
- **An Architecture for Deterministic Declarative Execution** — how a declared domain becomes a
  compiled graph a domain-blind runtime executes.
- **Realizing the Normative Platform and Its Governed Transformation** — what it takes for real
  business work to be expressed entirely as declaration, and what realization surfaced when it was.
