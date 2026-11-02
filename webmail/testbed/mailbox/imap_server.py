"""A small IMAP server for the execution validation — standard library only.

It speaks the part of IMAP4rev1 the mail host uses: LOGIN, SELECT, UID SEARCH ALL, UID FETCH (FLAGS,
BODY.PEEK[...] and BODY[...]), UID STORE ±FLAGS and LOGOUT. It keeps its mailboxes in memory and
counts what it was asked to do, so a criterion can see not only the answer but what reached the
provider: a fetch without PEEK marks a message read, as a real provider does, and is counted.
"""

from __future__ import annotations

import re
import socket
import socketserver
import threading
from dataclasses import dataclass, field


@dataclass
class Message:
    raw: bytes
    flags: set[str] = field(default_factory=set)


@dataclass
class State:
    user: str
    password: str
    folders: dict[str, dict[int, Message]]
    counts: dict[str, int] = field(default_factory=lambda: {"store": 0, "marking_fetch": 0})


def _headers(raw: bytes, names: list[str]) -> bytes:
    head = raw.split(b"\r\n\r\n", 1)[0].split(b"\r\n")
    wanted, out, keep = {n.lower() for n in names}, [], False
    for line in head:
        if line[:1] in (b" ", b"\t"):
            if keep:
                out.append(line)
            continue
        keep = line.split(b":", 1)[0].decode().strip().lower() in wanted
        if keep:
            out.append(line)
    return b"\r\n".join(out) + b"\r\n\r\n"


def _uids(spec: str, known: list[int]) -> list[int]:
    out = []
    for piece in spec.split(","):
        if ":" in piece:
            lo, hi = piece.split(":")
            lo = int(lo)
            hi = max(known, default=0) if hi == "*" else int(hi)
            out += [u for u in known if lo <= u <= hi]
        else:
            out.append(int(piece))
    return out


class _Handler(socketserver.StreamRequestHandler):
    def setup(self):
        super().setup()
        self.state: State = self.server.state
        self.folder: dict[int, Message] | None = None

    def send(self, data: bytes | str) -> None:
        self.wfile.write(data if isinstance(data, bytes) else data.encode())

    def handle(self):
        self.send("* OK IMAP4rev1 ready\r\n")
        while True:
            line = self.rfile.readline()
            if not line:
                return
            tag, _, rest = line.decode().rstrip("\r\n").partition(" ")
            cmd, _, args = rest.partition(" ")
            cmd = cmd.upper()
            if cmd == "CAPABILITY":
                self.send(f"* CAPABILITY IMAP4rev1\r\n{tag} OK done\r\n")
            elif cmd == "LOGIN":
                user, password = [a.strip('"') for a in re.findall(r'"(?:[^"\\]|\\.)*"|\S+', args)][:2]
                ok = user == self.state.user and password == self.state.password
                self.send(f"{tag} OK logged in\r\n" if ok else f"{tag} NO [AUTHENTICATIONFAILED] invalid\r\n")
            elif cmd == "SELECT":
                name = args.strip().strip('"')
                self.folder = self.state.folders.get(name)
                if self.folder is None:
                    self.send(f"{tag} NO no such mailbox\r\n")
                else:
                    self.send(f"* {len(self.folder)} EXISTS\r\n* 0 RECENT\r\n"
                              f"* FLAGS (\\Seen \\Flagged)\r\n{tag} OK [READ-WRITE] selected\r\n")
            elif cmd == "UID":
                self.uid(tag, args)
            elif cmd == "LOGOUT":
                self.send(f"* BYE\r\n{tag} OK bye\r\n")
                return
            else:
                self.send(f"{tag} OK\r\n")

    def uid(self, tag: str, args: str) -> None:
        sub, _, rest = args.partition(" ")
        sub, known = sub.upper(), sorted(self.folder or {})
        if sub == "SEARCH":
            self.send(f"* SEARCH {' '.join(map(str, known))}\r\n{tag} OK search\r\n")
        elif sub == "FETCH":
            spec, _, items = rest.partition(" ")
            for uid in _uids(spec, known):
                if uid in self.folder:
                    self.fetch(known.index(uid) + 1, uid, self.folder[uid], items)
            self.send(f"{tag} OK fetch\r\n")
        elif sub == "STORE":
            spec, op, flags = rest.split(" ", 2)
            self.state.counts["store"] += 1
            for uid in _uids(spec, known):
                msg = self.folder.get(uid)
                if msg is None:
                    continue
                named = set(flags.strip("()").split())
                msg.flags = msg.flags | named if op.startswith("+") else msg.flags - named
            self.send(f"{tag} OK store\r\n")
        else:
            self.send(f"{tag} BAD unknown\r\n")

    def fetch(self, seq: int, uid: int, msg: Message, items: str) -> None:
        literal = None
        found = re.search(r"BODY(\.PEEK)?\[([^\]]*)\]", items)
        if found:
            peek, section = found.group(1), found.group(2)
            if not peek:
                self.state.counts["marking_fetch"] += 1
                msg.flags.add("\\Seen")
            if section.upper().startswith("HEADER.FIELDS"):
                names = re.search(r"\(([^)]*)\)", section).group(1).split()
                literal = (f"BODY[{section}]", _headers(msg.raw, names))
            else:
                literal = (f"BODY[{section}]", msg.raw)
        flags = f"FLAGS ({' '.join(sorted(msg.flags))})"
        if literal:
            name, data = literal
            self.send(f"* {seq} FETCH (UID {uid} {flags} {name} {{{len(data)}}}\r\n".encode() + data + b")\r\n")
        else:
            self.send(f"* {seq} FETCH (UID {uid} {flags})\r\n")


class _Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


class ImapServer:
    """Serves `state` on a free local port until stopped."""

    def __init__(self, state: State):
        self.server = _Server(("127.0.0.1", 0), _Handler)
        self.server.state = state
        self.port = self.server.server_address[1]
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self) -> "ImapServer":
        self.thread.start()
        return self

    def __exit__(self, *exc) -> None:
        self.server.shutdown()
        self.server.server_close()


class SilentServer:
    """Accepts a connection and never answers: a provider that does not answer in time."""

    def __init__(self):
        self.sock = socket.socket()
        self.sock.bind(("127.0.0.1", 0))
        self.sock.listen()
        self.port = self.sock.getsockname()[1]

    def __enter__(self) -> "SilentServer":
        return self

    def __exit__(self, *exc) -> None:
        self.sock.close()


def closed_port() -> int:
    """A local port nothing listens on: a provider that cannot be reached."""
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()
    return port
