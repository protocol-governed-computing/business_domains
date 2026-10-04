# Architecture — `causal_language_model`

This document explains how the domain meets the claims in its [`README.md`](README.md). It assumes
no familiarity with Protocol-Governed Computing (PGC). Each PGC term is explained where it first
appears.

For the domains around this one, see [`../ARCHITECTURE.md`](../ARCHITECTURE.md). For the platform,
see **https://github.com/protocol-governed-computing**.

---

## 1. What this domain is

`causal_language_model` has one subdomain, `model_response`. It governs how a business's language
model answers a customer's question about the customer's own accounts.

Like every PGC domain, it consists of **declarations, not an application.** The domain declares:

- its acts (workflows);
- the requests each act admits (intents);
- the steps each act takes (contracts);
- the pure functions those steps call (transforms);
- the stores it writes (a storage structure);
- the moments it announces (events).

The platform compiles these declarations into a sealed snapshot and executes them. The domain
implements no admission, routing, storage or auditing of its own.

Only two small pure functions in Python decide anything about a hosted answer. One reads a request's
record. The other chooses a token. Everything else is declared.

## 2. Where it sits

```
                      ┌──────────────────── PGC ────────────────────┐
                      │                                             │
   requester ───────► │   sealed snapshot  ◄── compiler ◄── this    │
                      │         │                           domain's│
                      │         ▼                           declara-│
   host  ◄──────────► │      runtime ──► stores (records)   tions   │
    │                 │         │                                   │
    ▼                 │         └──► trace (evidence)               │
  model               └─────────────────────────────────────────────┘
 (Ollama)
```

- **The requester** is a person or system that acts for a customer, such as a service
  representative.
- **The host** is a small program outside PGC: `host/driver.py`. It runs the model, asks it for
  candidates, and calls PGC's acts. It holds no authority.
- **The model** is Qwen3 8B, which Ollama serves on the same machine. PGC never calls it.
- **The snapshot** is the compiled, hash-verified form of every declaration. The runtime executes
  only what the snapshot holds. A rule that is not in the snapshot does not exist.

## 3. The central idea: invert control

### Who chooses the next token

A language model writes one token at a time. At each step it scores every token it knows and picks
one, usually by sampling from its top few candidates. That pick is non-deterministic, and it happens
inside the model, where nobody can review it.

This domain takes the pick away from the model. At each step the host asks the model for its top
*k* candidates (five, here) and passes them to PGC. PGC chooses among them with a pure function,
under declared rules. The same text so far and the same candidates always give the same choice, and
PGC records every step. The model keeps the job of proposing. PGC takes the job of deciding.

### Why the loop runs outside PGC

A PGC act runs once, from start to end. Its graph has no cycles. Only declared steps that the
platform owns can have effects, such as writing a record. A transform never has effects.

A model writes in a loop: offer, choose, offer again. To run that loop inside an act, PGC would need
either a cycle in the graph or an effect inside a transform. PGC allows neither, for good reason:
both would hide behavior from the declarations.

So the loop moves outside. **The host runs the loop, and PGC decides each turn of it.**

```
   host                                   PGC (one act per call)
   ────                                   ──────────────────────
   begin(request) ──────────────────────► admit · open the record
                  ◄────────────────────── what the model reads
   loop:
     ask the model for its top 5 next tokens
     offer(candidates, fingerprint, size) ► check · choose · record the step
                  ◄────────────────────── the chosen token
     append the token; stop when the end is chosen
   release() ───────────────────────────► confirm complete · record · announce
                  ◄────────────────────── the released answer, from PGC's record
```

This inversion is what makes the host powerless. The host may call the acts in any order, as often
as it likes, with any content. PGC judges every call against the record the business keeps. The host
can turn a token into part of an answer only if the business chose that token.

## 4. The business objects

| Object | What it is | Where it lives |
|---|---|---|
| **Model** | A registered model: a description (name, reading capacity, maximum response length) and a fingerprint. Together, the description and fingerprint are its identity. | `MODELS`, `MODEL_IDENTITY_REGISTRY` |
| **Time in service** | One period in which a model is in service, with a sensitivity ceiling, a system prompt and **response rules**. | `TIMES_IN_SERVICE`, `TIME_IN_SERVICE_REGISTRY` |
| **Response rules** | Forbidden words and patterns, the shape of an account number, the freedom of choice, the longest response, and optionally a rule that numbers must come from the reading. | Inside the time in service |
| **User prompt record** | The trail of one request: an opening entry, one entry per step, and a closing entry. | `USER_PROMPT_RECORDS` (append-only) |

For Qwen3 8B, the fingerprint is the digest that Ollama reports for the model's stored weights. The
host supplies it, and the business records it as the host's claim.

## 5. The acts

| Act | Who calls it | What it does |
|---|---|---|
| `WF_REGISTER_MODEL_V0` | model staff | Registers a model. Refuses to register the same model twice. |
| `WF_PLACE_MODEL_IN_SERVICE_V0` | model staff | Opens a time in service, with its ceiling, system prompt and response rules. |
| `WF_WITHDRAW_MODEL_FROM_SERVICE_V0` | model staff | Closes a time in service. |
| `WF_SUBMIT_USER_PROMPT_V0` | requester | The test model's way: admits a request and writes the whole answer in one act. |
| `WF_BEGIN_HOSTED_RESPONSE_V0` | host | The hosted way: admits a request and opens its record. |
| `WF_OFFER_NEXT_TOKENS_V0` | host | Checks an offer, chooses a token and records the step. |
| `WF_RELEASE_HOSTED_RESPONSE_V0` | host | Releases a complete answer from the record. |
| `WF_RETRIEVE_USER_PROMPT_RECORD_V0` | requester | Reads a request's record, and records that someone read it. |

Each act starts at an **intent**, which declares what a request must contain. The platform refuses a
request that lacks a required field before the act begins.

## 6. One hosted answer, step by step

### Begin

```
IN_BEGIN_HOSTED_RESPONSE
  → CLAIM_USER_PROMPT_IDENTITY        the request's id is claimed once; a repeat is rejected
  → CONFIRM_REQUESTER_ACTS_FOR_CUSTOMER    ✗ → refused: requester_not_permitted_for_customer
  → ADMIT_USER_PROMPT                 ✗ → refused: model_not_registered / model_not_in_service
  → CONFIRM_WITHIN_CEILING            ✗ → refused: kind_above_sensitivity_ceiling
  → CONFIRM_READING_FITS              ✗ → refused: reading_longer_than_model_can_read
  → OPEN_HOSTED_RECORD                forms the rules in force; appends the opening entry
  → EXIT_WRITING                      returns the opening entry, including what the model reads
```

The first five steps are the test model's own admission contracts, reused unchanged. So both ways
admit a request by the same checks. The act **records every refusal before it ends**, with its
reason, and announces `EV_USER_PROMPT_REFUSED`.

The opening entry fixes everything the rest of the request depends on. It holds:

- what the model reads: the system prompt, the question and the supporting material;
- the rules in force, including the seed and the customer's own account numbers as exceptions;
- whether numbers must be grounded;
- the admitted model's fingerprint and reading capacity;
- the permitted length: the smaller of the model's registered maximum and the rules' longest
  response.

### Offer, once per token

```
IN_OFFER_NEXT_TOKENS
  → READ_HOSTED_STATE          reads the trail; rejects a request not being written
  → CONFIRM_OFFER_FOR_MODEL    ✗ → refused: offer_for_another_model
  → CONFIRM_HOSTED_READING_FITS ✗ → refused: reading_longer_than_model_can_read
  → CHOOSE_PERMITTED_TOKEN     the rules' choice (section 7)
  → CONFIRM_NO_RULE_STOPPED    ✗ → record the step, then refused: <the rule's name>
  → CONFIRM_WITHIN_LENGTH      ✗ → record the step, then refused: longest_response_reached
  → RECORD_STEP                appends the offer, the choice and every stop
  → EXIT_CHOSEN                returns the step
```

**The record is the only state.** On every call, `READ_HOSTED_STATE` rebuilds the answer so far
from the trail: first the opening entry, then each step in order. A record with no opening entry, or
a closed record, belongs to a request that is not being written. An offer against it changes nothing.

When a step ends the request, the act records that step first. So the record keeps the offer that
ended the request.

### Release

```
IN_RELEASE_HOSTED_RESPONSE
  → READ_HOSTED_STATE
  → CONFIRM_FINISHED           ✗ → rejected; nothing changes, the request stays open
  → RECORD_RESPONDED           closes the record with the text the trail holds
  → EXIT_RESPONDED             announces EV_USER_PROMPT_RESPONDED
```

The host asks for release, but it never supplies the text. The business rebuilds the answer from
its own record and releases that.

## 7. The choice: how a token is judged

`CT_PURE_CHOOSE_PERMITTED_TOKEN_V0` is a pure function. It takes the state (the opening entry and
the text so far) and the offered candidates. Given the same inputs, it always makes the same choice.
It takes the candidates in order, most likely first, and asks five questions of each.

**1. Does a forbidden pattern match?** The rule reads *the text so far joined to the candidate*, not
the candidate alone. A match counts only if it reaches into the candidate, because the earlier text
was already judged. So after `" 8765"`, the function stops `"4321"`, although neither token is an
account number on its own. The customer's own account numbers are exceptions.

**2. Is it a lookalike?** The function judges text in its Unicode compatibility form. So the
subscript `₁` and the full-width `１` count as the digit `1`. Qwen3 found this gap when the rules
stopped its plain digit.

**3. Does it begin a forbidden number that the model read?** The function collects every number in
what the model read. It matches numbers on their digits, and ignores spaces, commas, dots and dashes
between them. Suppose a candidate writes digits that begin a number some rule forbids, and begin no
other number the model read. The function stops that candidate at its first digit. This closes the
digit-by-digit leak. When the spouse's `87654321` is in the reading, the function stops `"8"`. It
allows `"2"`, because `"2"` also begins the balance.

**4. Is the number grounded?** The function asks this only when the time in service sets
`ground_numbers`. A number may begin only if some number the model read begins with its digits. A
number may end only if it equals a number the model read. A number ends in one of two ways: the next
candidate follows it with something other than a digit or a single separator, or the end marker is
chosen.
So `2,410` may continue to `2,410.55` and end there. `2410.5` may not end, and `7` may not begin. A
candidate stopped this way is stopped by the rule `numbers_from_the_reading`.

**5. Is it within length?** The end marker is not a token of the answer. A candidate that would take
the answer past its permitted length leaves the answer outside its length. The act then refuses the
request as unfinished.

Then the function chooses. It narrows the permitted candidates, most likely first, to the first
*freedom + 1*. It picks the one at position *(seed + step)* modulo their count. With freedom 0, it
always picks the most likely permitted token. If no candidate is permitted, it picks nothing and
names the rule that stopped the most likely candidate. That name becomes the refusal's reason.

## 8. How each claim is met

| Claim | Mechanism |
|---|---|
| **The business writes only what the rules permit** | The choice judges the text as built, in compatibility form, and stops the beginnings of forbidden numbers that the model read (§7, questions 1–3). A stopped candidate never reaches the record's text. |
| **Numbers come from the reading** | Grounding, set per time in service and carried into the opening entry (§7, question 4). A time in service without it behaves as before. |
| **The host holds no power** | Inverted control (§3). PGC compares the fingerprint on every offer, and compares the reported reading size with the admitted capacity. Release uses the record's text, not the host's. |
| **Admission before any word** | The begin act runs the same four admission contracts as the test model's way, plus the reading check, before it opens the record (§6). |
| **A complete record** | The record opens at admission. It gets one entry per step: the candidates, the choice, every stop with its rule, the host's name and the reported size. It closes on release or refusal. An abandoned request stays open. |
| **Sealed rules** | The compiler seals the rules, the acts and the choice function into a hash-verified snapshot. The runtime refuses a snapshot that does not verify. Only a change request can change them (§10). |
| **Every choice reproducible** | The choice is pure and seeded, and the record holds every offer. Offering the recorded candidates again reproduces every choice. In the test model's way, the runtime itself replays a run: it substitutes the recorded offers for the model and compares the two executions. |

Every act also writes a trace, one line per node and step, in the platform's trace schema. The
record answers *what happened to this request*. The trace answers *what the platform did to decide
it*.

## 9. Two ways, one set of rules

```
                         shared
   ┌──────────────────────────────────────────────────────────┐
   │ registration · placement · admission contracts ·         │
   │ response rules · user prompt records · events            │
   └──────────────────────────────────────────────────────────┘
          │                                   │
   the test model's way                 the hosted way
   WF_SUBMIT_USER_PROMPT                BEGIN · OFFER · RELEASE
   one act writes the whole answer      one act per token
   the model is a declared step         the model is outside PGC
   inside a pure molecule
```

In the test model's way, the model is a transform declared **not determined by its inputs**
(`ct_impure`). The platform records every offer that transform makes. A replay uses the recorded
offers and does not call the model. The loop runs inside a *molecule*: a transform made only of
declared steps, with no effects. This works for a scripted model. It cannot work for a real model,
because a real model runs in another process, and calling it is an effect. That is why the hosted way
exists.

The test model also drives the hosted way, through the same host (`TestModel` in `host/driver.py`).
It offers another customer's account number before every word. So the suite proves the hosted
controls deterministically, with no model installed.

## 10. A change to this domain is itself governed

The domain's artifacts are generated from the designs in its change requests. Nobody writes them by
hand. Each change request has nine phases, P0 to P8. A machine checks each phase against the sealed
rule set before the next phase begins:

- **P0:** the business states the problem in its own words. Only a person writes this.
- **P1–P6:** the change is analysed against the composition as it stands: what exists, what is
  missing, what can be reused, and who owns what.
- **P7:** the design is laid out: every act's graph, every step's inputs and outputs, and every pure
  function's test cases.
- **P8:** the design is ordered into a build.
- **Construction:** a generator produces the artifacts from the design. A check confirms that the
  design determines every fact of every artifact.

A person approves the phases. The dossiers are in `cr_dossiers/`:

- **`cr_01_model_response`** built the test model's way.
- **`cr_02_hosted_model`** built the hosted way. The first delivery was then run against Qwen3 8B.
  The model exposed the partial-number leak, the lookalike and the invented number. So the change was
  withdrawn and redone from P0, with grounding added. `delivery.md` tells that story.

## 11. Layout

```
causal_language_model/
├── README.md, ARCHITECTURE.md
├── registry/model_response/     the declarations: workflows, intents, contracts,
│                                transforms, test data, events, actors, storage, bindings
├── implementation/              the pure functions the transforms name
│   └── capability_transforms/atoms/
├── host/driver.py               the host: OllamaModel, TestModel, Host (outside PGC)
├── testbed/
│   ├── model_response/          execution validation of the test model's way
│   └── hosted_model/            execution validation of the hosted way
├── cr_dossiers/                 the governed record of each change
└── doc/                         background notes
```

## 12. Rules this domain keeps

- **PGC never calls the model.** The host calls PGC. PGC never calls the host.
- **Transforms are pure.** The functions that read the trail and choose a token do no input or
  output. Every effect is a declared step on a declared store.
- **The record is the only state.** No store holds a second copy of a hosted request.
- **The host is untrusted.** PGC records the host's fingerprint, reading size and name as claims,
  and checks them against the admitted request.
- **The hosted way changed no existing act.** The test model's way is exactly as it was.

## 13. How to know it works

| Check | What it proves | Command |
|---|---|---|
| Transform conformance | Every transform against its declared test cases | runs at build |
| Construction check | The design determines every artifact | `tc construction check cr_dossiers/cr_02_hosted_model …` |
| Test model's way | 27 acceptance criteria, including replay | `testbed/model_response/execution_validation.py` |
| Hosted way | 15 acceptance criteria with the test model and a scripted model; the 16th with Qwen3 8B | `testbed/hosted_model/execution_validation.py [--qwen]` |
| Full regression | Clean rebuild, every check, every domain | `bash .github/process/regression.sh --all` |

The hosted suite uses a scripted model that makes exactly the offers each criterion needs:

- an account number split across tokens;
- an offer that names another model;
- a reading that is too large;
- an offer in which nothing is permitted;
- a response that is too long;
- a made-up number;
- a host that stops offering.

Each criterion reads the record that the acts left, not the host's view of it.

## 14. Limits

- **Grounded does not mean true.** Grounding proves that the model read a number, not that the
  number is in the right place. With grounding on, Qwen3 8B gave the customer's own number when
  asked for the spouse's.
- **Numbers only.** The rules do not judge numbers written as words, or claims that are not numbers.
- **Top five only.** When all five candidates are forbidden, the business refuses the request.
- **Rules are only as good as their patterns.** A rule against "guaranteed" must also catch
  "Guaranteed".
- **The host's claims stay claims.** The business cannot prove that the candidates came from the
  model.
