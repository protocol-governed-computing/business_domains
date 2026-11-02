# Business Problem Statement

**Project Name:** webmail — mailbox

## 1. Context

The business offers people a web-based way to read the mail they already have. A person's mail is
kept by their mail provider, such as Gmail, in a mailbox the person owns. The business does not keep
the mail. It reads the mailbox when the person asks, shows what they asked to see, and changes the
mailbox only in the ways the person asked for.

The behavior the business wants is the behavior people already know from established webmail, with
Roundcube as the reference: a list of messages in a folder, a message opened to read, and a message
marked as read or unread.

This is the first part of the service. It covers reading only. Sending mail comes later.

## 2. Problem Statement

A webmail service holds a person's mail password and can do anything to their mailbox that the
person could do: read every message, mark them, move them, delete them. People must trust that the
service does only what they asked.

**The business must decide every change made to a person's mailbox, and keep a record of it.** The
program that connects to the mail provider, called the *host*, may read the mailbox and report what
the provider said. It may not decide what the person is shown or what is changed in the mailbox.

### How the service reaches a mailbox

The mailbox is reached over IMAP, the standard way mail programs read mail from a provider. The host
connects to the provider, signs in with the person's credentials, and carries out one request at a
time.

The host reports to the business what the provider returned. The business decides what the person
sees and which change, if any, is due. The host then carries out that change and reports whether the
provider accepted it. The business records the outcome.

The business never holds the person's credentials. The host reads them from a place the person
controls, and they appear in no record the business keeps.

### Listing a folder

A person asks to see a folder, such as the inbox. The business shows the newest messages first, a
page of 50 at a time. Newest means most recently received by the provider, as established webmail
orders a folder; the date a message carries is not used to order it. For each message it shows who sent it, its subject, its date, whether it has been
read, whether it is flagged, and whether it has attachments.

A folder with no messages is shown as empty. That is an answer, not a failure.

### Opening a message

A person asks to open one message in a folder. The business shows its sender, recipients, subject,
date and its text. Opening a message marks it as read, as established webmail does. The business
records that the message was opened and that it became read.

Only the plain text of a message is shown. A message that has no plain-text part is shown with a
statement that its text cannot be displayed yet.

### Marking a message as read or unread

A person may mark a message as read or as unread. The business records the request and the
provider's answer, and shows the state the message is now in.

Marking a message with the state it already has is not an error. The business reports the state, and
records that nothing changed.

### What is refused

The business refuses a request, and records the refusal, when:

* the provider rejects the person's credentials;
* the provider cannot be reached, or does not answer within 30 seconds;
* the folder does not exist;
* the message does not exist in the folder.

A refusal tells the person which of these happened. It never shows a partial result as if it were
complete.

### What the record keeps

The business keeps a record of every request: who asked, what was asked, which folder and message it
concerned, what was decided, and what the provider answered.

**The record does not keep the content of mail.** It identifies messages; it does not copy their
subjects, senders or text. A person's mail stays with their provider.

## 3. What the system shall allow

The system shall allow a person to:

* list a folder of their mailbox, a page at a time, newest first;
* open a message and read its text, which marks it as read;
* mark a message as read or as unread.

The system shall allow the host to:

* report what the provider returned for a request;
* receive the business's decision about what to show and what to change;
* report whether the provider accepted a change.

## 4. Acceptance criteria

1. Listing a folder shows its newest messages first, with sender, subject, date, read state, flag
   state and attachment indicator for each.
2. Listing a folder with more messages than a page shows one page, and says that more exist.
3. Listing an empty folder answers that it is empty.
4. Opening a message shows its sender, recipients, subject, date and plain text.
5. Opening an unread message makes it read at the provider, and the record says so.
6. Opening a message with no plain-text part says its text cannot be displayed yet.
7. Marking an unread message as read makes it read at the provider.
8. Marking a read message as unread makes it unread at the provider.
9. Marking a message with the state it already has reports that state and changes nothing.
10. Rejected credentials are refused, and the refusal says so.
11. An unreachable or silent provider is refused, and the refusal says so.
12. A folder that does not exist is refused, and the refusal says so.
13. A message that does not exist in the folder is refused, and the refusal says so.
14. Every request, answered or refused, is in the record.
15. No record holds a subject, a sender, message text or a credential.

## 5. Out of scope

* Sending, replying, forwarding and drafts.
* Displaying HTML mail, and opening or saving attachments.
* Searching, sorting by other columns, and threads.
* Creating, renaming or deleting folders; moving, copying or deleting messages.
* Contacts, identities, signatures and settings.
* Sign-in methods other than a password for IMAP, such as OAuth.
* Keeping a connection to the provider open between requests.
