"""Execution validation — run the mailbox acts against their acceptance criteria.

Every criterion is one of the fifteen in `cr_dossiers/cr_01_read_mail/p0_business_problem_statement.md`,
in its words. Each dispatches the mailbox acts through `protocol_runtime` against a fresh data root,
driven by the mail host in `webmail/host/driver.py`, against a local IMAP server holding known mail
(`imap_server.py`). A criterion reads what the person was shown, what reached the provider, and what
the record kept.

Run:  python business_domains/webmail/testbed/mailbox/execution_validation.py [snapshot]
      ... --data-root <path>     keep the stores and traces instead of discarding them
Exit: 0 if every criterion holds, 1 otherwise.
"""

from __future__ import annotations

import json
import shutil
import sys
import tempfile
from email.message import EmailMessage
from pathlib import Path

HERE = Path(__file__).resolve()
DOMAIN = HERE.parents[2]
WORKSPACE = DOMAIN.parents[1]
for root in (WORKSPACE / "software_governance", WORKSPACE / "business_domains", HERE.parent):
    if str(root) not in sys.path:
        sys.path.insert(0, str(root))

from runtime import api  # noqa: E402
from webmail.host.driver import (ANSWERED, Account, Host, Provider, load_account)  # noqa: E402
from imap_server import ImapServer, Message, SilentServer, State, closed_port  # noqa: E402

STORE = "webmail/mailbox/mailbox_records.jsonl"
USER, PASSWORD = "person@example.com", "app-password-for-the-test"
PLAIN = "Lunch on Thursday works for me."


def message(subject: str, sender: str, date: str, plain: str | None = None, html: str | None = None,
            attachment: bool = False) -> bytes:
    m = EmailMessage()
    m["From"], m["To"], m["Cc"], m["Subject"], m["Date"] = sender, USER, "", subject, date
    if plain is not None:
        m.set_content(plain)
    if html is not None:
        if plain is None:
            m.set_content(html, subtype="html")
        else:
            m.add_alternative(html, subtype="html")
    if attachment:
        m.add_attachment(b"%PDF-1.4 test", maintype="application", subtype="pdf", filename="invoice.pdf")
    return bytes(m)


# The mail the provider holds. Identifiers are given out of date order on purpose: the order a
# folder is shown in is the order the provider received the mail, never the date a message carries.
SENSITIVE = ["Quarterly numbers", "Lunch?", "Newsletter", "Invoice 4471", "alice@example.org",
             "bob@example.org", "news@example.org", "billing@example.org", PLAIN, PASSWORD]


def mailboxes() -> dict:
    inbox = {
        3: Message(message("Quarterly numbers", "alice@example.org", "Mon, 05 Oct 2026 09:00:00 +0000",
                           plain="See attached figures."), {"\\Seen"}),
        7: Message(message("Lunch?", "bob@example.org", "Wed, 01 Jan 2025 12:00:00 +0000",
                           plain=PLAIN, html=f"<p>{PLAIN}</p>"), {"\\Flagged"}),
        9: Message(message("Newsletter", "news@example.org", "Fri, 09 Oct 2026 08:00:00 +0000",
                           html="<h1>News</h1>")),
        12: Message(message("Invoice 4471", "billing@example.org", "Sat, 10 Oct 2026 10:00:00 +0000",
                            plain="Your invoice is attached.", attachment=True)),
    }
    big = {u: Message(message(f"Note {u}", "notes@example.org", "Thu, 01 Oct 2026 00:00:00 +0000",
                              plain="note")) for u in range(101, 161)}
    return {"INBOX": inbox, "Big": big, "Empty": {}}


def records(data_root: Path) -> list[dict]:
    path = data_root / STORE
    return [json.loads(l)["record"] for l in path.read_text().splitlines() if l.strip()] if path.exists() else []


def main() -> int:
    args = sys.argv[1:]
    keep = None
    if "--data-root" in args:
        i = args.index("--data-root")
        keep = Path(args[i + 1]).resolve()
        del args[i:i + 2]
    snapshot = Path(args[0]).resolve() if args else WORKSPACE / "snapshot"
    data_root = keep or Path(tempfile.mkdtemp(prefix="webmail_"))
    if keep and keep.exists():
        shutil.rmtree(keep)
    data_root.mkdir(parents=True, exist_ok=True)

    results: list[tuple[str, bool, str]] = []

    def check(criterion: str, held: bool, detail: str = "") -> None:
        results.append((criterion, bool(held), detail))

    def act(wf: str, payload: dict):
        return api.run_workflow(wf_fqdn=wf, payload=payload, data_root=data_root, snapshot_root=snapshot)

    requests = 0

    def host_for(account: Account, timeout: float = 30) -> Host:
        return Host(act, lambda: Provider(account, timeout=timeout), account.user)

    state = State(USER, PASSWORD, mailboxes())
    with ImapServer(state) as server:
        # The person's credentials, in the place they control; the host reads them from there.
        secrets = data_root / "secrets" / "imap"
        secrets.mkdir(parents=True)
        (secrets / "test.json").write_text(json.dumps({"host": "127.0.0.1", "port": server.port,
                                                       "user": USER, "password": PASSWORD, "tls": False}))
        account = load_account(data_root, "test")
        host = host_for(account)
        inbox = state.folders["INBOX"]

        a = host.list_folder("INBOX"); requests += 1
        ids = [r["uid"] for r in a.rows]
        fields = all({"from", "subject", "date", "seen", "flagged", "has_attachments"} <= set(r) for r in a.rows)
        by = {r["uid"]: r for r in a.rows}
        check("Listing a folder shows its newest messages first, with sender, subject, date, read state, "
              "flag state and attachment indicator for each.",
              ids == [12, 9, 7, 3] and fields and by[3]["seen"] and not by[9]["seen"]
              and by[7]["flagged"] and by[12]["has_attachments"] and not by[3]["has_attachments"],
              f"shown {ids}")

        p1, p2 = host.list_folder("Big", 1), host.list_folder("Big", 2); requests += 2
        check("Listing a folder with more messages than a page shows one page, and says that more exist.",
              len(p1.rows) == 50 and p1.entry["more_exist"] and p1.rows[0]["uid"] == 160
              and len(p2.rows) == 10 and not p2.entry["more_exist"],
              f"page 1: {len(p1.rows)}, more {p1.entry.get('more_exist')}; page 2: {len(p2.rows)}")

        e = host.list_folder("Empty"); requests += 1
        check("Listing an empty folder answers that it is empty.",
              e.outcome == ANSWERED and e.entry["folder_empty"] and e.rows == [])

        before = dict(state.counts)
        o = host.open_message("INBOX", 7); requests += 2
        check("Opening a message shows its sender, recipients, subject, date and plain text.",
              o.outcome == ANSWERED and o.headers.get("from") == "bob@example.org"
              and o.headers.get("to") == USER and o.headers.get("subject") == "Lunch?"
              and o.headers.get("date") and (o.text or "").strip() == PLAIN,
              f"text {o.text!r}")
        reported = o.reported or {}
        check("Opening an unread message makes it read at the provider, and the record says so.",
              "\\Seen" in inbox[7].flags and o.entry["change"] == "SET_READ"
              and reported.get("request") == "REPORT_CHANGE_OUTCOME" and reported.get("outcome") == ANSWERED
              and state.counts["marking_fetch"] == before["marking_fetch"],
              f"flags {sorted(inbox[7].flags)}; reads that marked: "
              f"{state.counts['marking_fetch'] - before['marking_fetch']}")

        h = host.open_message("INBOX", 9); requests += 2
        check("Opening a message with no plain-text part says its text cannot be displayed yet.",
              h.outcome == ANSWERED and not h.entry["text_displayable"] and h.text is None)

        m = host.mark("INBOX", 12, True); requests += 2
        check("Marking an unread message as read makes it read at the provider.",
              "\\Seen" in inbox[12].flags and m.entry["change"] == "SET_READ" and m.entry["read_now"])

        m = host.mark("INBOX", 3, False); requests += 2
        check("Marking a read message as unread makes it unread at the provider.",
              "\\Seen" not in inbox[3].flags and m.entry["change"] == "SET_UNREAD" and not m.entry["read_now"])

        stores = state.counts["store"]
        m = host.mark("INBOX", 3, False); requests += 1
        check("Marking a message with the state it already has reports that state and changes nothing.",
              m.outcome == ANSWERED and m.entry["change"] == "NONE" and not m.entry["read_now"]
              and m.reported is None and state.counts["store"] == stores)

        wrong = Account("127.0.0.1", server.port, USER, "wrong-password", tls=False)
        r = host_for(wrong).list_folder("INBOX"); requests += 1
        check("Rejected credentials are refused, and the refusal says so.",
              r.outcome == "REFUSED" and r.entry.get("reason") == "CREDENTIALS_REJECTED")

        r1 = host_for(Account("127.0.0.1", closed_port(), USER, PASSWORD, tls=False)).list_folder("INBOX")
        with SilentServer() as silent:
            r2 = host_for(Account("127.0.0.1", silent.port, USER, PASSWORD, tls=False),
                          timeout=1).open_message("INBOX", 7)
        requests += 2
        check("An unreachable or silent provider is refused, and the refusal says so.",
              r1.entry.get("reason") == "UNREACHABLE" and r2.entry.get("reason") == "UNREACHABLE"
              and r1.outcome == r2.outcome == "REFUSED")

        r = host.list_folder("Archive"); requests += 1
        check("A folder that does not exist is refused, and the refusal says so.",
              r.outcome == "REFUSED" and r.entry.get("reason") == "NO_SUCH_FOLDER")

        r1, r2 = host.open_message("INBOX", 999), host.mark("INBOX", 999, True); requests += 2
        check("A message that does not exist in the folder is refused, and the refusal says so.",
              r1.entry.get("reason") == r2.entry.get("reason") == "NO_SUCH_MESSAGE")

    kept = records(data_root)
    check("Every request, answered or refused, is in the record.",
          len(kept) == requests, f"{len(kept)} entries for {requests} requests")

    leaked = []
    for path in data_root.rglob("*"):
        if path.is_file() and secrets not in path.parents:
            text = path.read_text(errors="replace")
            leaked += [f"{s!r} in {path.relative_to(data_root)}" for s in SENSITIVE if s in text]
    check("No record holds a subject, a sender, message text or a credential.", not leaked,
          "; ".join(leaked[:3]))

    print(f"webmail mailbox — {len(results)} criteria, data root {data_root}")
    for criterion, held, detail in results:
        print(f"  {'OK  ' if held else 'FAIL'}  {criterion}" + (f"  [{detail}]" if detail and not held else ""))
    if keep is None:
        shutil.rmtree(data_root, ignore_errors=True)
    failed = [c for c, held, _ in results if not held]
    print(f"\n{len(results) - len(failed)}/{len(results)} criteria hold")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
