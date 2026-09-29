# Architecture — `causal_language_model`

This document explains how the domain meets the claims its [`README.md`](README.md) makes. It
assumes no familiarity with Protocol-Governed Computing (PGC). Where a term is PGC's own, it is
explained where it first appears.

For the domains around this one, see [`../ARCHITECTURE.md`](../ARCHITECTURE.md). For the platform,
see **https://github.com/protocol-governed-computing**.

---

## 1. What this domain is

`causal_language_model` has one subdomain, `model_response`. It governs how a business's language
model answers a customer's question about the customer's own accounts.

It is written the way every PGC domain is written: **as declarations, not as an application.** The
domain declares its acts (workflows), the requests each act admits (intents), the steps each act
takes (contracts), the pure functions those steps call (transforms), the stores it writes (a
storage structure) and the moments it announces (events). The platform compiles those declarations
into a sealed snapshot and executes them. The domain implements no admission, routing, storage or
auditing of its own.

Two small pure functions are the only Python that decides anything about a hosted answer. One reads
a request's record; the other chooses a token. Everything else is declared.

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

- **The requester** is a person or system acting for a customer, such as a service representative.
- **The host** is a small program outside PGC: `host/driver.py`. It runs the model, asks it for
  candidates, and calls PGC's acts. It holds no authority.
- **The model** is Qwen3 8B, served by Ollama on the same machine. PGC never calls it.
- **The snapshot** is the compiled, hash-verified form of every declaration. The runtime executes
  only what the snapshot holds. A rule not in the snapshot does not exist.

## 3. The central idea: invert control

A PGC act runs once, from start to end. Its graph has no cycles. Effects, such as writing a record,
happen only in declared steps the platform owns, never inside a transform.

A model writes in a loop: offer, choose, offer again. Putting that loop inside an act would need
either a cycle in the graph or an effect inside a transform. PGC allows neither, and for good
reason: both would hide behaviour from the declarations.

So the loop moves outside. **The host runs the loop; PGC decides each turn of it.**

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

This inversion is what makes the host powerless. It can call the acts in any order, as often as it
likes, with any content. Every call is judged against the record the business keeps, and nothing
the host sends becomes an answer unless the business chose it.

## 4. The business objects

| Object | What it is | Where it lives |
|---|---|---|
| **Model** | A registered model: a description (name, reading capacity, maximum response length) and a fingerprint. Its identity is the description and fingerprint together. | `MODELS`, `MODEL_IDENTITY_REGISTRY` |
| **Time in service** | One period a model is in service, with a sensitivity ceiling, a system prompt and **response rules**. | `TIMES_IN_SERVICE`, `TIME_IN_SERVICE_REGISTRY` |
| **Response rules** | Forbidden words and patterns, the shape of an account number, the freedom of choice, the longest response, and optionally that numbers come from the reading. | Inside the time in service |
| **User prompt record** | The trail of one request: an opening entry, one entry per step, a closing entry. | `USER_PROMPT_RECORDS` (append-only) |

The fingerprint for Qwen3 8B is the digest Ollama reports for the model's stored weights. It is the
host's claim, and the business records it as a claim.

## 5. The acts

| Act | Who calls it | What it does |
|---|---|---|
| `WF_REGISTER_MODEL_V0` | model staff | Registers a model; refuses the same model twice. |
| `WF_PLACE_MODEL_IN_SERVICE_V0` | model staff | Opens a time in service, with its ceiling, system prompt and response rules. |
| `WF_WITHDRAW_MODEL_FROM_SERVICE_V0` | model staff | Closes a time in service. |
| `WF_SUBMIT_USER_PROMPT_V0` | requester | The test model's way: admits a request and writes the whole answer in one act. |
| `WF_BEGIN_HOSTED_RESPONSE_V0` | host | The hosted way: admits a request and opens its record. |
| `WF_OFFER_NEXT_TOKENS_V0` | host | Checks an offer, chooses a token and records the step. |
| `WF_RELEASE_HOSTED_RESPONSE_V0` | host | Releases a complete answer from the record. |
| `WF_RETRIEVE_USER_PROMPT_RECORD_V0` | requester | Reads a request's record, and records that it was read. |

Each act starts at an **intent**, which declares what a request must contain. A request missing a
required field is refused before the act begins.

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

The first five steps are the test model's own admission contracts, reused unchanged. Both ways
admit a request by the same checks. Every refusal is **recorded before the act ends**, with its
reason, and announces `EV_USER_PROMPT_REFUSED`.

The opening entry is the request's constitution. It holds:
- what the model reads (system prompt, question, supporting material);
- the rules in force, including the customer's own account numbers as exceptions and the seed;
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

**There is no state outside the record.** `READ_HOSTED_STATE` rebuilds the answer so far from the
trail on every call: the opening entry, then each step in order. A record with no opening entry, or
one already closed, is not being written, and the offer changes nothing.

When a step ends the request, its step is recorded first. The record keeps the offer that ended it.

### Release

```
IN_RELEASE_HOSTED_RESPONSE
  → READ_HOSTED_STATE
  → CONFIRM_FINISHED           ✗ → rejected; nothing changes, the request stays open
  → RECORD_RESPONDED           closes the record with the text the trail holds
  → EXIT_RESPONDED             announces EV_USER_PROMPT_RESPONDED
```

The host asks for release. It never supplies the text. The released answer is the business's text,
rebuilt from the business's record.

## 7. The choice: how a token is judged

`CT_PURE_CHOOSE_PERMITTED_TOKEN_V0` is a pure function. It takes the state (the opening entry and
the text so far) and the offered candidates. Given the same inputs it always makes the same choice.
For each candidate, most likely first, it asks five questions.

**1. Does a forbidden pattern match?** The rule reads *the text so far joined to the candidate*, not
the candidate alone. A match counts only if it reaches into the candidate; the text before it was
judged already. So `" 8765"` followed by `"4321"` is stopped at `"4321"`, although neither token is
an account number alone. The customer's own account numbers are exceptions.

**2. Is it a lookalike?** Text is judged in its Unicode compatibility form, so the subscript `₁` and
a full-width `１` are the digit `1`. This is the gap Qwen3 found when its plain digit was stopped.

**3. Does it begin a forbidden number the model read?** The choice collects every number in what
the model read. Numbers match on their digits, ignoring spaces, commas, dots and dashes between
them. If a candidate writes digits that begin a number some rule forbids, and begin no other number
the model read, it is stopped at the first digit. This closes the digit-by-digit leak: `"8"` is
stopped when the spouse's `87654321` is in the reading. `"2"` is not, because it also begins the
balance.

**4. Is the number grounded?** Only when the time in service sets `ground_numbers`. A number may
not be begun unless a number the model read begins with its digits. It may not be ended unless it
is one. A number ends when a candidate follows it with anything but a digit or a lone separator,
or when the end marker is chosen. So `2,410` may continue to `2,410.55` and end. `2410.5` may not
end, and `7` may not begin. The rule's name is `numbers_from_the_reading`.

**5. Is it within length?** The end marker is not a token of the answer. A candidate that would
take the answer past its permitted length leaves it outside its length, and the act refuses the
request as unfinished.

Then it chooses. The permitted candidates, most likely first, are narrowed to the first
*freedom + 1*. The one at position *(seed + step)* modulo their count is chosen. With freedom 0, the
most likely permitted token is always chosen. If no candidate is permitted, nothing is chosen, and
the rule that stopped the most likely candidate is named. That name becomes the refusal's reason.

## 8. How each claim is met

| Claim | Mechanism |
|---|---|
| **Nothing forbidden is written** | The choice judges text as built, in compatibility form, and stops the beginnings of forbidden numbers it read (§7, questions 1–3). A stopped candidate never reaches the record's text. |
| **Numbers come from the reading** | Grounding, set per time in service and carried into the opening entry (§7, question 4). A time in service without it behaves as before. |
| **The host holds no power** | Inverted control (§3). The fingerprint is compared on every offer. The reported reading size is compared with the admitted capacity. Release uses the record's text, not the host's. |
| **Admission before any word** | The begin act runs the same four admission contracts as the test model's way, plus the reading check, before the record opens (§6). |
| **A complete record** | The record opens at admission and gets one entry per step: candidates, choice, every stop with its rule, the host's name and reported size. It closes on release or refusal. An abandoned request stays open. |
| **Rules are sealed** | Rules, acts and choice are compiled into a hash-verified snapshot, and the runtime refuses a snapshot that does not verify. They change only through a change request (§10). |
| **Every choice reproducible** | The choice is pure and seeded, and the record holds every offer. Re-offering the recorded candidates reproduces every choice. The test model's way is replayed by the runtime itself, which substitutes recorded offers for the model and compares the two executions. |

Every act also writes a trace: one line per node and step, conforming to the platform's trace
schema. The record answers *what happened to this request*. The trace answers *what the platform
did to decide it*.

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
(`ct_impure`). The platform records every offer it makes. A replay substitutes the recorded offers
rather than calling the model. The loop runs inside a *molecule*: a transform made only of declared
steps, with no effects. This works for a scripted model. It cannot work for a real one, because the
model lives in another process and calling it is an effect. That is why the hosted way exists.

The test model also drives the hosted way, through the same host (`TestModel` in `host/driver.py`).
It offers another customer's account number before every word, so the hosted controls are proven
deterministically, with no model installed.

## 10. A change to this domain is itself governed

The domain's artifacts are generated from the designs of its change requests, not written by hand.
Each change request has nine phases, P0 to P8, each checked by machine against the sealed rule set
before the next begins:

- **P0:** the business states the problem in its own words. Only a person writes this.
- **P1–P6:** the change is analysed against the composition as it stands: what exists, what is
  missing, what is reused, who owns what.
- **P7:** the design is laid out: every act's graph, every step's inputs and outputs, every pure
  function's test cases.
- **P8:** the design is ordered into a build.
- **Construction:** the artifacts are generated from the design, and a check confirms the design
  determines every fact of every artifact.

A person approves the phases. The dossiers are in `cr_dossiers/`:

- **`cr_01_model_response`** built the test model's way.
- **`cr_02_hosted_model`** built the hosted way. It was delivered once, then run against Qwen3 8B.
  The model exposed the partial-number leak, the lookalike and the invented number, so the change
  was withdrawn and redone from P0 with grounding. `delivery.md` tells that story.

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

- **The model is never called from inside PGC.** The host calls PGC; PGC never calls the host.
- **Transforms are pure.** Reading the trail and choosing a token do no input or output. Every
  effect is a declared step on a declared store.
- **The record is the only state.** No store holds a second copy of a hosted request.
- **The host is not trusted.** Its fingerprint, reading size and name are recorded as claims and
  checked against the admitted request.
- **No existing act changed for the hosted way.** The test model's way is exactly as it was.

## 13. How to know it works

| Check | What it proves | Command |
|---|---|---|
| Transform conformance | Every transform against its declared test cases | runs at build |
| Construction check | The design determines every artifact | `tc construction check cr_dossiers/cr_02_hosted_model …` |
| Test model's way | 27 acceptance criteria, including replay | `testbed/model_response/execution_validation.py` |
| Hosted way | 15 acceptance criteria with the test model and a scripted model; the 16th with Qwen3 8B | `testbed/hosted_model/execution_validation.py [--qwen]` |
| Full regression | Clean rebuild, every check, every domain | `bash .github/process/regression.sh --all` |

The scripted model in the hosted suite makes exactly the offers a criterion needs: an account number
split across tokens, an offer naming another model, a reading too large, an offer with nothing
permitted, a response too long, a made-up number, and a host that stops offering. Each criterion
reads the record the acts left, not the host's view of it.

## 14. Limits

- **Grounded is not true.** Grounding proves a number was read, not that it is placed correctly.
  Asked for the spouse's number with grounding on, Qwen3 8B wrote the customer's own.
- **Numbers only.** Numbers written as words, and claims that are not numbers, are not judged.
- **Top five only.** When all five candidates are forbidden, the request is refused.
- **Rules are only as good as their patterns.** A rule against "guaranteed" must be written to
  catch "Guaranteed".
- **The host's claims are claims.** The business cannot prove the candidates came from the model.
