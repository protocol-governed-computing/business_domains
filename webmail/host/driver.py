"""The mail host — outside PGC, holding no authority.

The host reaches a person's mail provider over IMAP with the person's credentials, and calls the
mailbox acts. It reports what the provider returned: identifiers, read state and the parts a message
has, never a subject, a sender or text. PGC answers with decisions, and the host shows the person the
content those decisions name and carries out the change they decide. Nothing in PGC calls the host.

- **List a folder.** The host reports the folder's identifiers in the order the provider received
  them; PGC chooses the page; the host shows the summaries of exactly those messages, in that order.
- **Open a message.** The host reads it without marking it (`BODY.PEEK`) and reports its parts; PGC
  chooses the plain-text part and decides that the message becomes read; the host shows the part,
  sets the flag, and reports whether the provider accepted it.
- **Mark a message.** The host reports its read state and the state asked for; PGC decides the change,
  or that nothing changes; the host carries out a decided change and reports it.

The credentials are read from `<data_root>/secrets/imap/<account>.json`:

    {"host": "imap.gmail.com", "port": 993, "user": "you@gmail.com", "password": "<app password>"}

They are never handed to an act. One connection serves one request, and none is kept between them.

Run:  python business_domains/webmail/host/driver.py --data-root <path> --account <name> list INBOX [--page 2]
      ... open INBOX <uid>
      ... mark INBOX <uid> read|unread
"""

from __future__ import annotations

import email
import imaplib
import json
import re
import socket
import sys
from dataclasses import dataclass, field
from email import policy
from email.message import EmailMessage
from pathlib import Path
from typing import Callable

NS = "webmail::"
LIST, OPEN, MARK, REPORT = (NS + "WF_LIST_FOLDER_V0", NS + "WF_OPEN_MESSAGE_V0",
                            NS + "WF_MARK_MESSAGE_V0", NS + "WF_REPORT_CHANGE_OUTCOME_V0")
ANSWERED = "ANSWERED"
CREDENTIALS_REJECTED, UNREACHABLE = "CREDENTIALS_REJECTED", "UNREACHABLE"
NO_SUCH_FOLDER, NO_SUCH_MESSAGE = "NO_SUCH_FOLDER", "NO_SUCH_MESSAGE"
TIMEOUT = 30  # seconds a provider has to answer
SUMMARY = "(FLAGS BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE CONTENT-TYPE)])"


@dataclass
class Account:
    host: str
    port: int
    user: str
    password: str
    tls: bool = True


def load_account(data_root: str | Path, name: str) -> Account:
    """The person's credentials, from the place they control under the data root."""
    path = Path(data_root) / "secrets" / "imap" / f"{name}.json"
    stated = json.loads(path.read_text())
    return Account(stated["host"], int(stated.get("port", 993)), stated["user"], stated["password"],
                   bool(stated.get("tls", True)))


class ProviderRefused(Exception):
    """The provider did not answer the request; `answer` says how."""

    def __init__(self, answer: str):
        super().__init__(answer)
        self.answer = answer


class Provider:
    """One IMAP connection for one request."""

    def __init__(self, account: Account, timeout: float = TIMEOUT):
        self.account, self.timeout, self.conn = account, timeout, None

    def __enter__(self) -> "Provider":
        a = self.account
        try:
            cls = imaplib.IMAP4_SSL if a.tls else imaplib.IMAP4
            self.conn = cls(a.host, a.port, timeout=self.timeout)
        except (OSError, imaplib.IMAP4.abort):
            raise ProviderRefused(UNREACHABLE)
        try:
            self.conn.login(a.user, a.password)
        except imaplib.IMAP4.error:
            raise ProviderRefused(CREDENTIALS_REJECTED)
        except (OSError, imaplib.IMAP4.abort):
            raise ProviderRefused(UNREACHABLE)
        return self

    def __exit__(self, *exc) -> None:
        if self.conn is not None:
            try:
                self.conn.logout()
            except (OSError, imaplib.IMAP4.error):
                pass

    def _call(self, *args):
        try:
            return self.conn.uid(*args)
        except (OSError, imaplib.IMAP4.abort):
            raise ProviderRefused(UNREACHABLE)

    def select(self, folder: str) -> None:
        try:
            typ, _ = self.conn.select(_quote(folder))
        except (OSError, imaplib.IMAP4.abort):
            raise ProviderRefused(UNREACHABLE)
        if typ != "OK":
            raise ProviderRefused(NO_SUCH_FOLDER)

    def identifiers(self) -> list[int]:
        """The folder's identifiers in the order the provider received the messages: ascending UIDs."""
        typ, data = self._call("SEARCH", None, "ALL")
        return [int(u) for u in (data[0] or b"").split()] if typ == "OK" else []

    def summaries(self, uids: list[int]) -> dict[int, dict]:
        if not uids:
            return {}
        typ, data = self._call("FETCH", ",".join(map(str, uids)), SUMMARY)
        out = {}
        for meta, body in _fetched(data):
            uid = _uid(meta)
            if uid is None:
                continue
            h = email.message_from_bytes(body or b"", policy=policy.default)
            out[uid] = {"uid": uid, "from": str(h.get("From", "")), "subject": str(h.get("Subject", "")),
                        "date": str(h.get("Date", "")), "seen": "\\Seen" in _flags(meta),
                        "flagged": "\\Flagged" in _flags(meta),
                        "has_attachments": h.get_content_type() == "multipart/mixed"}
        return out

    def seen(self, uid: int) -> bool:
        typ, data = self._call("FETCH", str(uid), "(FLAGS)")
        metas = [m for m, _ in _fetched(data) if _uid(m) == uid]
        if typ != "OK" or not metas:
            raise ProviderRefused(NO_SUCH_MESSAGE)
        return "\\Seen" in _flags(metas[0])

    def message(self, uid: int) -> tuple[bool, EmailMessage]:
        """The message and its read state, read without marking it."""
        typ, data = self._call("FETCH", str(uid), "(FLAGS BODY.PEEK[])")
        found = [(m, b) for m, b in _fetched(data) if _uid(m) == uid and b is not None]
        if typ != "OK" or not found:
            raise ProviderRefused(NO_SUCH_MESSAGE)
        meta, body = found[0]
        return "\\Seen" in _flags(meta), email.message_from_bytes(body, policy=policy.default)

    def set_read(self, uid: int, read: bool) -> str:
        typ, _ = self._call("STORE", str(uid), "+FLAGS" if read else "-FLAGS", "(\\Seen)")
        return ANSWERED if typ == "OK" else NO_SUCH_MESSAGE


def _quote(folder: str) -> str:
    return '"' + folder.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _fetched(data) -> list[tuple[str, bytes | None]]:
    """imaplib's FETCH answer as (metadata, literal) pairs, metadata joined across its pieces."""
    out: list[list] = []
    for item in data or []:
        if isinstance(item, tuple):
            out.append([item[0].decode(errors="replace"), item[1]])
        elif isinstance(item, bytes) and item.strip() not in (b"", b")"):
            if out and item.startswith(b" "):
                out[-1][0] += item.decode(errors="replace")
            else:
                out.append([item.decode(errors="replace"), None])
        elif isinstance(item, bytes) and out:
            out[-1][0] += item.decode(errors="replace")
    return [(m, b) for m, b in out]


def _uid(meta: str) -> int | None:
    found = re.search(r"\bUID (\d+)", meta)
    return int(found.group(1)) if found else None


def _flags(meta: str) -> str:
    found = re.search(r"FLAGS \(([^)]*)\)", meta)
    return found.group(1) if found else ""


def parts(msg: EmailMessage) -> list[tuple[str, EmailMessage]]:
    """A message's leaf parts with their IMAP part numbers: 1, 2, 1.1 …"""
    def walk(m: EmailMessage, prefix: str) -> list[tuple[str, EmailMessage]]:
        if not m.is_multipart():
            return [(prefix or "1", m)]
        out = []
        for i, sub in enumerate(m.iter_parts(), 1):
            out += walk(sub, f"{prefix}.{i}" if prefix else str(i))
        return out
    return walk(msg, "")


@dataclass
class Answer:
    """What a request came to, as the host shows it."""
    outcome: str                          # ANSWERED or REFUSED, as recorded; REJECTED when nothing was
    entry: dict = field(default_factory=dict)
    rows: list[dict] = field(default_factory=list)
    headers: dict = field(default_factory=dict)
    text: str | None = None
    reported: dict | None = None          # the record entry of a change's reported outcome


class Host:
    """Drives the mailbox acts for one mailbox. `act(wf_fqdn, payload)` dispatches a governed act."""

    def __init__(self, act: Callable, provider: Callable[[], Provider], mailbox: str,
                 host_id: str = "mail-host-01"):
        self.act, self.provider, self.mailbox, self.host_id = act, provider, mailbox, host_id

    def _base(self, folder: str, answer: str) -> dict:
        return {"host_id": self.host_id, "mailbox": self.mailbox, "folder": folder,
                "provider_answer": answer}

    def _entry(self, result) -> dict:
        return (getattr(result, "surface", None) or {}).get("entry") or {}

    def list_folder(self, folder: str, page: int = 1) -> Answer:
        try:
            with self.provider() as p:
                p.select(folder)
                ids = p.identifiers()
                entry = self._entry(self.act(LIST, {**self._base(folder, ANSWERED),
                                                    "message_ids": ids, "page": page}))
                if entry.get("outcome") != ANSWERED:
                    return Answer(entry.get("outcome", "REJECTED"), entry)
                found = p.summaries(entry["page_ids"])
                return Answer(ANSWERED, entry, [found[u] for u in entry["page_ids"] if u in found])
        except ProviderRefused as r:
            entry = self._entry(self.act(LIST, {**self._base(folder, r.answer), "message_ids": [],
                                                "page": page}))
            return Answer(entry.get("outcome", "REJECTED"), entry)

    def open_message(self, folder: str, uid: int) -> Answer:
        try:
            with self.provider() as p:
                p.select(folder)
                seen, msg = p.message(uid)
                numbered = parts(msg)
                entry = self._entry(self.act(OPEN, {
                    **self._base(folder, ANSWERED), "message_id": uid, "seen": seen,
                    "parts": [{"part": n, "kind": m.get_content_type()} for n, m in numbered]}))
                if entry.get("outcome") != ANSWERED:
                    return Answer(entry.get("outcome", "REJECTED"), entry)
                headers = {h: str(msg.get(h, "")) for h in entry["shown_headers"]}
                text = None
                if entry["text_displayable"]:
                    text = dict(numbered)[entry["text_part"]].get_content()
                answer = Answer(ANSWERED, entry, headers=headers, text=text)
                answer.reported = self._carry_out(p, folder, uid, entry["change"])
                return answer
        except ProviderRefused as r:
            entry = self._entry(self.act(OPEN, {**self._base(folder, r.answer), "message_id": uid,
                                                "seen": False, "parts": []}))
            return Answer(entry.get("outcome", "REJECTED"), entry)

    def mark(self, folder: str, uid: int, read: bool) -> Answer:
        try:
            with self.provider() as p:
                p.select(folder)
                seen = p.seen(uid)
                entry = self._entry(self.act(MARK, {**self._base(folder, ANSWERED), "message_id": uid,
                                                    "seen": seen, "wanted_read": read}))
                if entry.get("outcome") != ANSWERED:
                    return Answer(entry.get("outcome", "REJECTED"), entry)
                answer = Answer(ANSWERED, entry)
                answer.reported = self._carry_out(p, folder, uid, entry["change"])
                return answer
        except ProviderRefused as r:
            entry = self._entry(self.act(MARK, {**self._base(folder, r.answer), "message_id": uid,
                                                "seen": False, "wanted_read": read}))
            return Answer(entry.get("outcome", "REJECTED"), entry)

    def _carry_out(self, p: Provider, folder: str, uid: int, change: str) -> dict | None:
        """Carry out the change PGC decided, and report whether the provider accepted it."""
        if change == "NONE":
            return None
        try:
            answer = p.set_read(uid, change == "SET_READ")
        except ProviderRefused as r:
            answer = r.answer
        return self._entry(self.act(REPORT, {**self._base(folder, answer), "message_id": uid,
                                             "change": change}))


def _show(answer: Answer) -> None:
    e = answer.entry
    if answer.outcome != ANSWERED:
        print(f"REFUSED — {e.get('reason', 'nothing was recorded')}")
        return
    if e.get("request") == "LIST_FOLDER":
        if e["folder_empty"]:
            print(f"{e['folder']} is empty.")
            return
        print(f"{e['folder']} — page {e['page']}, {e['message_count']} message(s)"
              + ("; more exist" if e["more_exist"] else ""))
        for r in answer.rows:
            mark = ("  " if r["seen"] else "● ") + ("⚑ " if r["flagged"] else "  ") + \
                   ("📎 " if r["has_attachments"] else "   ")
            print(f"{mark}{r['uid']:>7}  {r['date'][:25]:<25}  {r['from'][:30]:<30}  {r['subject'][:60]}")
        return
    if e.get("request") == "OPEN_MESSAGE":
        for h, v in answer.headers.items():
            if v:
                print(f"{h.capitalize()}: {v}")
        print()
        print(answer.text if e["text_displayable"] else "[This message's text cannot be displayed yet.]")
    print(f"\nread now: {e['read_now']}  (change decided: {e['change']})")
    if answer.reported is not None:
        print(f"provider: {answer.reported.get('provider_answer')} — recorded as {answer.reported.get('outcome')}")


def main(argv: list[str]) -> int:
    import argparse

    here = Path(__file__).resolve()
    workspace = here.parents[3]
    for root in (workspace / "software_governance", workspace / "business_domains"):
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
    from runtime import api

    ap = argparse.ArgumentParser(prog="webmail host")
    ap.add_argument("--data-root", required=True)
    ap.add_argument("--account", required=True, help="name of <data-root>/secrets/imap/<name>.json")
    ap.add_argument("--snapshot", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)
    ls = sub.add_parser("list"); ls.add_argument("folder"); ls.add_argument("--page", type=int, default=1)
    op = sub.add_parser("open"); op.add_argument("folder"); op.add_argument("uid", type=int)
    mk = sub.add_parser("mark"); mk.add_argument("folder"); mk.add_argument("uid", type=int)
    mk.add_argument("state", choices=["read", "unread"])
    args = ap.parse_args(argv)

    account = load_account(args.data_root, args.account)
    host = Host(lambda wf, payload: api.run_workflow(wf_fqdn=wf, payload=payload,
                                                     data_root=args.data_root,
                                                     snapshot_root=args.snapshot),
                lambda: Provider(account), account.user)
    if args.cmd == "list":
        answer = host.list_folder(args.folder, args.page)
    elif args.cmd == "open":
        answer = host.open_message(args.folder, args.uid)
    else:
        answer = host.mark(args.folder, args.uid, args.state == "read")
    _show(answer)
    return 0 if answer.outcome == ANSWERED else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
