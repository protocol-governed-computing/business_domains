# Business Problem Statement

**Project Name:** causal_language_model

## 1. Context

This is a new project. It is not part of the current software baseline.

The proposed name of the project is causal_language_model.

A bank wants to use a language model to answer customers' questions about their own accounts. A
language model writes an answer one word at a time, and each word depends on the words before it.
Nobody can predict the exact answer in advance. Asked the same question twice, it may answer
differently.

The bank must still be able to show a regulator, for any answer, which model wrote it, who asked,
what the model was given to read, which rules applied while it wrote, and whether an answer was
refused and why.

The project scope includes the following functions:

- answer — asking a model a question and getting an answer under the bank's rules
- registry — the full record of the models the bank holds, and their retirement
- disclosure — reviewing a finished answer before it is released
- action — letting a model propose an action, such as a transfer, that someone must authorize
- substitution — replacing the model in service with another
- reporting — the record a regulator examines

The scope of this CR-1 is limited to "answer" only. It includes only as much of the registry as an
answer needs.

## 2. Problem Statement

Today, staff paste customers' questions into a model and copy its answer back. Nobody can say
afterwards which model answered, what it was shown, or whether anything stopped it from writing
something it should not have written. A check made after the answer is written can catch a problem
only once the model has already produced it.

The bank requires answers written under rules. The rules apply while the model writes, not
afterwards.

### Models

Before a model can answer anything, authorized model staff register it. A registration describes
how the model is built, including the amount of text it can read at once, and carries a fingerprint
of its training supplied by whoever provided it. Two registrations with the same description and the
same fingerprint are the same model, and the bank holds one record for it.

The fingerprint is the provider's claim. The bank records it and does not verify how the model was
trained.

A registered model does not answer anyone until authorized model staff place it in service. When
they do, they state the most sensitive kind of information the model may read. The kinds, from least
to most sensitive, are public, internal, confidential, and restricted.

### Answer rules

When authorized model staff place a model in service, they also set its answer rules:

- words and patterns the model must never write, such as any account number other than the
  customer's own
- how freely the model may choose its words, from always choosing the most likely word to choosing
  more adventurously
- the longest answer the model may write

A rule belongs here only if it can be applied while the model writes. A rule that can only be
judged once an answer is finished is not an answer rule. Such rules belong to a later review of
finished answers, which this release does not include.

"Another customer's account number" depends on who the customer is. The rule is applied for each
request, using the account numbers of the customer the request is for.

The requester cannot change the answer rules. They belong to the model's time in service.

When the model is about to write a word a rule forbids, the rule stops that word and the model
continues with a permitted one. If the model cannot finish an answer without breaking a rule, it
gives no answer. The request is refused, and the record says which rule stopped it.

An answer that reaches its longest permitted length before it is finished is not released. The
request is refused, and the record says so.

### Asking a question

An authorized requester asks a question on behalf of one customer. The request carries the question
and any supporting material, such as the customer's recent transactions. It names the model and
states the most sensitive kind of information the question and its material contain.

The requester must be permitted to act for that customer. Deciding which requesters may act for
which customers is the bank's existing business and is not decided here. Naming a customer does not
by itself give the requester access to that customer's accounts.

What the model reads is exactly the question, the supporting material, and the bank's standing
instructions for the model in service. Nothing else reaches the model.

A request is refused before the model sees it when:

- the model is not registered
- the model is not in service
- the request contains a more sensitive kind of information than the model may read
- the request is longer than the model can read at once

Every request is recorded, whether answered or refused, with:

- who asked, and for which customer
- which model, and its time in service
- exactly what the model read: the question, the supporting material, and the standing instructions
- the kind of information it contained
- the answer rules in force
- the answer, or the reason it was refused

The record keeps what the model read, not only a summary or fingerprint of it.

The bank does not claim that an answer is true. It claims only that the answer was written by the
recorded model, from the recorded material, under the recorded rules.

### The test model

Until a real model is available, the bank uses a test model. The test model deliberately tries to
break the rules. It tries to write another customer's account number, and it answers from material
it was not given. This lets the bank see the rules hold before a real model is trusted with them.
The same rules govern the test model, and its answers are recorded in the same way.

### What staff and requesters can do

The system shall allow authorized model staff to:

- register a model
- place a registered model in service, with its answer rules and standing instructions
- withdraw a model from service
- retrieve the record of any request

The system shall allow authorized requesters to:

- ask a question of a model in service, on behalf of a customer

Every business operation shall be traceable and auditable.

The bank starts with no models registered.

This release excludes retiring models, reviewing an answer after it is written, letting a model
propose actions, replacing the model in service, and regulator reporting.

Those capabilities are expected to be introduced through future governed change requests rather
than being designed into the initial solution.
