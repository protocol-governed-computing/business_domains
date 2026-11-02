# Delivery — cr_01_read_mail

**Decided by:** the domain owner, in `p0_business_problem_statement.md`, confirmed at Gate 0, with
the design approved at Gate 1 and the mandate at Gate 2.
**Designed against:** composition `8ad89baa75ce…` (`baseline.json`), which holds no webmail domain.
**Delivered:**
- A new business domain, `webmail`, with one subdomain, `mailbox`. A person lists a folder a page of
  50 at a time, newest received first; opens a message and reads its plain text, which makes it read;
  and marks a message read or unread. Every request, answered or refused, is recorded.
- A host outside the composition, `webmail/host/driver.py`, reaches the mail provider over IMAP. It
  reports and carries out; the business decides.

**Validated:**
- Phase documents P0 to P8 admissible. Construction 852/852 determined; 26 artifacts emitted.
- The three new transforms proven by their 16 cases at compile.
- Execution validation 15/15: every acceptance criterion of P0, against a local IMAP server.

---

## How the design got here

- **Mail content never enters an act.** An act's answer is the last contract's output, and the same
  output is announced as the event's payload. An answer carrying mail would have carried it into the
  trace. So the host reports identifiers, read state and a message's parts, and the business answers
  with decisions. P3 to P5 were re-authored for this before P7 was written.
- **Listing is one act, not two.** With content kept out, the business chooses the page from the
  identifiers and the host shows the summaries of exactly those, in that order.
- **The domain is `webmail`, not `email`.** A domain's name is its import package, and `email` is a
  standard library package.

## Generated documents

`p7_design_intent_webmail_mailbox_v0.md` is written by `generate_p7.py` from the design tables it
states, and `p8_authoring_mandate_webmail_mailbox_v0.md` by `generate_p8.py` from P7. Both generators
are kept here as they ran. Construction measured the generated design at 100%.

## Outside the domain

A new domain is registered where the workspace enumerates domains: `pyproject.toml` (the package),
`write_baseline_designs.py` and `construction_acceptance.py` (designs of record), and
`regression.sh`, `expectations.yaml` and `RUNBOOK.md` (the regression).

## Not done in this change

- A reported change is recorded as reported. The business does not yet check it against the
  decision that called for it.
- The attachment indicator reads the message's top-level kind only.
