# Delivery — cr_01_model_response

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `3c360d983b20…`
**Delivered:** the model response function entire. Model staff register a model, place it in service
under a ceiling, a system prompt and response rules, and withdraw it. A user prompt is answered
only by a model in service, only on what that model may read, and only in words the rules in force
permit. Every user prompt is recorded with what the model read, the rules in force and its outcome,
and model staff retrieve those records.
**Validated:** 27/27 criteria, by running the five workflows against a composition built from this
design, with the test model as the model

---

## What this dossier is

It is the first dossier in which a step is **not determined by its inputs**. The model offers
words, and nothing about the model is governed. What is governed is everything around it:

- which model may be consulted;
- what it reads;
- which of the words it offers may be written;
- what is kept afterwards.

So the design splits the response into two steps a word at a time:

- **the model's step, which offers.** It is declared non-deterministic, so the platform records
  every offer.
- **the rules' step, which chooses.** It is pure: given the same offer, rules, seed and response so
  far, it chooses the same word.

A response is therefore a loop of offer-then-choose, bounded by the longest response the business
allows. It is written as a molecule over the two atoms.

The test model stands in for a real one, and it is built to break the rules. It offers another
customer's account number on every word, ahead of the word it should write. A response equal to the
supporting material is therefore evidence that the rules decided what was written, not that the
model held back.

**P7 and P8 were generated, not typed.** Scripts wrote them from P5 and P6, and the phase checks
admitted them as they would admit the same text written by hand. The scripts are kept, as they ran,
in `.github/process/notes/clm-generators/`. After generation, one decision was made by hand in P7:
retrieval records the operation before reading the record.

---

## What it took

Seven gaps in the design language and the platform surfaced here, and none was specific to CLM.
Each was fixed on the platform, with a test, before this change used it.

**One contract at several places in a workflow.**
- The submission records its outcome at ten places: one responds, the others refuse for their own
  reasons. It confirms a response is releasable at two places.
- **Keyed nodes (P7 §5).** The node is now a key, and a `Runs` column names the contract.
- **Acyclicity per node.** It is now checked over node keys. Checked over contracts, two places
  running one contract in sequence read as a cycle.
- **Routing, endings and announcements.** Built from these keyed nodes, they were still indexed by
  contract. The last place sealed stood for every place running that contract:
  - every submission ended where the last record node did, and announced nothing;
  - a rule stop would have been recorded as the longest response being reached.
- **All three are now keyed by node.** ai_governance had the same collision in two workflows, and
  nobody had caught it.

**A refusal is a moment.** An ending that refuses may now announce, but only an event declared a
refusal moment. A refused user prompt is announced as refused. It is not left silent, and it is not
dressed as a success.

**Molecules reach atoms that no contract names.** The transform surface is closed by derivation.
V0 counted only what a contract's pipeline names, and refused the molecule's own atoms as unreached.
V1 closes the count over molecule steps.

**Two runtime defects.**
- **Arguments.** The executor dropped an atom argument whose name matched a step key (`kind`).
- **Missing implementations.** Conformance crashed on a missing implementation instead of reporting
  it.

**Retrieval did not hand back what it retrieved.** A workflow answers with its last contract's
result. Retrieval read the record and then wrote the operation trail, so the caller got the trail
entry. It now records the retrieval first and reads second, so the record is the answer. A retrieval
of a record that does not exist is still on the trail, as an attempt.

---

## What the composition holds

```
WF_SUBMIT_USER_PROMPT_V0
  IN                          ACK       -> CLAIM_USER_PROMPT_IDENTITY
  CLAIM_USER_PROMPT_IDENTITY  SUCCESS   -> REQUIRE_PERMITTED          ALREADY_EXISTS -> EXIT_REJECTED
  REQUIRE_PERMITTED           SUCCESS   -> ADMIT                      VIOLATION      -> RECORD_REFUSED (not permitted)
  ADMIT                       SUCCESS   -> CONFIRM_WITHIN_CEILING     NOT_FOUND / VIOLATION -> RECORD_REFUSED (not registered / not in service)
  CONFIRM_WITHIN_CEILING      SUCCESS   -> CONFIRM_READING_FITS       VIOLATION      -> RECORD_REFUSED (above ceiling)
  CONFIRM_READING_FITS        SUCCESS   -> WRITE_MODEL_RESPONSE       VIOLATION      -> RECORD_REFUSED (too long to read)
  WRITE_MODEL_RESPONSE        SUCCESS   -> CONFIRM_NO_RULE_STOPPED    VIOLATION      -> RECORD_FAILED (writing)
  CONFIRM_NO_RULE_STOPPED     SUCCESS   -> CONFIRM_FINISHED           VIOLATION      -> RECORD_REFUSED (the rule's name)
  CONFIRM_FINISHED            SUCCESS   -> RECORD_RESPONDED           VIOLATION      -> RECORD_REFUSED (longest response reached)
  RECORD_RESPONDED            SUCCESS   -> EXIT_RESPONDED   announces EV_USER_PROMPT_RESPONDED_V0
  RECORD_REFUSED …            SUCCESS   -> EXIT_REFUSED     announces EV_USER_PROMPT_REFUSED_V0
```

Also in the composition:
- **The other four workflows:** register, place in service, withdraw and retrieve. Each confirms
  model staff first, and each writes the operation trail.
- **In total:** 51 artifacts in all, and six implementations.
  - **The atoms:** four pure atoms, plus the test model.
  - **The rules' step:** one pure chooser.
- **Conformance:** eight transforms proven against 17 cases.

---

## What it proved, by running

```
OK  model staff register a model, and it is held as registered under its identity
OK  the same model is not registered twice, however its description is written
OK  a registered model is placed in service, with a time in service that is open
OK  a model already in service is not placed in service again
OK  a user prompt is answered, and its record says it was responded to
OK  no word the model offered reached the response unless the rules permitted it
OK  the record keeps what the model read and the rules in force, seed included
OK  a user prompt for a customer the requester is not permitted to act for is refused, and recorded with its reason
OK  a user prompt to a model the business never registered is refused, and recorded with its reason
OK  a user prompt carrying information above the model's ceiling is refused, and recorded with its reason
OK  a user prompt longer than the model can read at once is refused, and recorded with its reason
OK  a response in which no word the model offered is permitted is refused, and recorded with its reason
OK  a response a rule stopped is not given, not even the words written before the stop
OK  a user prompt identity already claimed is refused, and its record is not written twice
OK  a response that reaches the longest the business allows is refused, not cut short
OK  several models are in service at once, and each answers its own user prompts
OK  a user prompt to a model not in service is refused
OK  model staff retrieve a user prompt record, and are handed the record
OK  anyone who is not model staff is refused retrieval and registration, and leaves no trail
OK  a model withdrawn from service is registered again, and its time in service is closed
OK  a user prompt to a withdrawn model is refused as not in service
OK  a withdrawn model returns under a new time in service, never a closed one
OK  every staff operation that completed is in the operation trail
OK  a responded user prompt announces that it was responded to, and nothing else
OK  every refused user prompt announces that it was refused
OK  a replay reproduces the response from the recorded offers, without consulting the model
OK  the replay and the original agree on every determinative event but the store's clock-assigned record identity
```

The responded prompt's trace shows another customer's account number offered on every word, and
the response does not contain it.

The replay runs against the stores as the original found them. It substitutes every recorded offer
and consults no model, and it writes the same response.

---

## What this change did not do

**It does not make the replay agree entirely.**
- **What differs.** An append-only store gives each record an identity read from the clock. That
  identity reaches the trace inside `detail`, which the evidence classification declares
  determinative.
- **What the classification already says.** It states that it does not claim a caller-filled
  `detail` holds only determinative content.
- **How the criterion handles it.** It names that one field and fails on any other difference. The
  classification separating store-assigned content is a platform change.

**It does not govern the model.** The model is whatever offers the words. A real model joins later
as a second realization of the same declared step. Its capacity is in tokens, whereas the reading
here is counted in words. That count is exact for the test model and a simulation for a real one.

**The name of a rule stop.** When no offered word is permitted, the rule named is the one that
stopped the most likely word. With the test model that is always the account-number rule, even when
the material's own word broke another rule.

**Left open:**
- **Refusal moments.** `moment: refusal` is checked at P7, but the event artifact does not carry it.
- **Vector cases.** P7 does not check that its vector cases parse.
- **Emit help.** `tc construction emit --help` is out of date about how a manifest is created.
