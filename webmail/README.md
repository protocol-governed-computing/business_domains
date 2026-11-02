# webmail

Read the mail you already have, the way established webmail does (Roundcube is the behavioral
reference), with every decision about your mailbox made by PGC and recorded.

| Subdomain | What it does |
|---|---|
| `mailbox` | List a folder a page of 50 at a time, newest received first. Open a message and show its plain text, which makes it read. Mark a message read or unread. Refuse rejected credentials, an unreachable or silent provider, an unknown folder and an unknown message. Record every request, answered or refused. |

## How it works

The mail provider is reached by a **host** outside PGC, `host/driver.py`, as the
`causal_language_model` domain reaches its model. The host holds the IMAP connection and your
credentials. It holds no authority.

```
   you ──► host (imaplib) ─────────────► IMAP provider (Gmail …)
             │   ▲
   reports   │   │  decisions: which messages make the page,
   ids, read │   │  which part is the text, which flag changes
   state,    ▼   │
   parts     PGC acts (one per call) ──► mailbox record · trace
```

- **The host reports** identifiers, read state and which parts a message has. It never hands PGC a
  subject, a sender or text.
- **PGC decides** which messages make the page, which part is the plain text, and whether the read
  state changes. It records every request and its outcome.
- **The host shows you** the content those decisions name. It reads a message without marking it
  (`BODY.PEEK`), and changes a flag only when PGC decided a change. It then reports whether the
  provider accepted it, and PGC records that too.

No act is handed mail content, so no record, event or trace can hold any.

| Act | The host reports | PGC answers |
|---|---|---|
| `WF_LIST_FOLDER_V0` | the folder's identifiers in received order, the page asked for | the page's identifiers, newest first; whether more exist; whether the folder is empty |
| `WF_OPEN_MESSAGE_V0` | the message's read state and its parts (number and kind) | the plain-text part, or that none can be displayed; the headers shown; the read-state change |
| `WF_MARK_MESSAGE_V0` | the message's read state and the state asked for | `SET_READ`, `SET_UNREAD` or `NONE` |
| `WF_REPORT_CHANGE_OUTCOME_V0` | whether the provider accepted a decided change | the record entry |

Each act first confirms the provider answered. A provider that refused is recorded as a refusal with
its reason and announced by `EV_MAILBOX_REQUEST_REFUSED_V0`.

## Try it with your Gmail

1. Turn on 2-Step Verification for the account, then create an **app password** at
   <https://myaccount.google.com/apppasswords>. IMAP is on by default for Gmail.
2. Write your credentials where only you can read them, under a data root of your choosing:

   ```bash
   DATA=~/protocol-governed-computing/data/webmail_live
   mkdir -p $DATA/secrets/imap && chmod 700 $DATA/secrets
   cat > $DATA/secrets/imap/gmail.json <<'EOF'
   {"host": "imap.gmail.com", "port": 993, "user": "you@gmail.com", "password": "abcd efgh ijkl mnop"}
   EOF
   chmod 600 $DATA/secrets/imap/gmail.json
   ```

3. Run the host from the workspace root, in the workspace venv:

   ```bash
   H="python business_domains/webmail/host/driver.py --data-root $DATA --account gmail"
   $H list INBOX                 # the newest 50
   $H list INBOX --page 2        # the next 50
   $H open INBOX <uid>           # shows the message and makes it read
   $H mark INBOX <uid> unread    # or: read
   ```

4. See what the business kept:

   ```bash
   cat $DATA/webmail/mailbox/mailbox_records.jsonl     # identifiers, decisions, provider answers
   ls  $DATA/traces/webmail/                           # one trace per act
   ```

Opening a message marks it read in Gmail, as Roundcube does. Mark it unread again with `mark … unread`.

## Execution validation

```bash
python business_domains/webmail/testbed/mailbox/execution_validation.py
```

15 criteria, one for each acceptance criterion of `cr_01_read_mail`. They run against
`testbed/mailbox/imap_server.py`, a small IMAP server in the standard library that holds known mail
and counts what reaches it. One criterion scans every file the acts wrote for the test mail's
subjects, senders, text and password.

## Limits of this slice

- Reading only. No sending, drafts, HTML display, attachments, search, folder management or contacts.
- Password sign-in only (an app password for Gmail); no OAuth.
- The attachment indicator is read from the message's top-level kind (`multipart/mixed`).
- A change the host reports is recorded as reported. PGC does not yet check it against the decision
  that called for it.
