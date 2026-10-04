# Delivery — cr_02_hosted_model

**Authorized by:** Gate 1 and Gate 2, at P7 and P8, against composition `b8dd7145232e…`
**Delivered:** a pretrained model hosted outside PGC answers customers under the business's rules.
The host proposes each next token; the business chooses, records and releases. Qwen3 8B, served by
Ollama, is the first hosted model.
**Validated:** hosted-model execution validation 15/15 in the regression (Qwen3 8B not exercised
there), 16/16 with `--qwen`; transform conformance for causal_language_model 10 proven, 0 unproven,
32 cases; full regression 59/59 on a clean rebuild.

---

## What this change added

Three acts, beside the test model's way, which is unchanged:

- **Begin.** A requester's request is admitted under the test model's conditions, and its record
  opens with what the model reads, the rules in force, the limits and the admitted fingerprint.
- **Offer.** The host offers the model's likeliest next tokens with the model's fingerprint and the
  size of what it read. The business checks both, stops forbidden tokens, chooses one and records the
  step. A request with no permitted token, or past its permitted length, is refused and closed.
- **Release.** A complete response is released with the text the business's record holds.

A hosted request's record trail is its state: no store was added. The host is a driver outside PGC
(`causal_language_model/host/driver.py`), holding no authority; nothing in PGC calls it.

---

## What it took

**Qwen shaped the change before it was delivered.** The first delivery was run against Qwen3 8B
asking for a spouse's account number it had read. It wrote seven of the eight digits one token at a
time, offered a subscript `₁` for the eighth, and once both were stopped made up a number instead.
The change was withdrawn from the composition and redone from P0 with three things it had lacked:

- **Grounding.** A time in service may require every number in a response to be one the model read,
  matched on its digits. The opening entry carries the rule from the stored response rules, so no
  existing artifact changed, and a time in service that does not set it behaves as before.
- **A number's beginning is judged.** The model may not begin a forbidden number it read unless the
  digits could still become a permitted one.
- **Lookalikes are the characters they look like.** Text is judged in its compatibility form.

**A permitted length counts written tokens.** The end marker is not one of them, so a response of
exactly the permitted length can still end.

**A vector states every declared output.** The first emission failed conformance until each case
stated all five of the choice's outputs; they are derived from the transform and checked against
those the author stated.

---

## What is carried

- **A grounded number is not a true one.** With grounding set, Qwen, still asked for the spouse's
  number, gave the customer's own: a number it read, attributed wrongly. The business does not claim
  truth, and P0 says so; judging what a number is said to be is a later change.
- **Numbers only.** Numbers written as words, and claims that are not numbers, are not judged.
- **Rules are only as good as their patterns.** Stopped on "guaranteed", Qwen offered "Guaranteed";
  the business's patterns must be written for that (the suite's is case-insensitive).
- **The host is not authenticated.** Its name is recorded against each offer; a false offer is
  refused on the admitted request's own facts.
