# Business Problem Statement

**Project Name:** causal_language_model

## 1. Context

This is a new project. It is not part of the current software baseline.

The proposed name of the project is causal_language_model.

A business wants to use a language model to respond to its customers' questions about their own
accounts. A bank answering questions about its customers' bank accounts is one example. A language
model writes a response one word at a time, and each word depends on the words before it. Nobody can
predict the exact response in advance. Given the same question twice, it may respond differently.

The business must still be able to show a regulator, for any model response, which model wrote it,
who asked, what the model was given to read, which rules applied while it wrote, and whether a
response was refused and why.

The project scope includes the following functions:

- model_response — asking a model a question and getting its response under the business's rules
- registry — the full record of the models the business holds, and their retirement
- disclosure — reviewing a finished model response before it is released
- action — letting a model propose an action, such as a payment, that someone must authorize
- substitution — replacing the model in service with another
- reporting — the record a regulator examines

The scope of this CR-1 is limited to "model_response" only. It includes only as much of the
registry as a model response needs.

## 2. Problem Statement

Today, staff paste customers' questions into a model and copy its response back. Nobody can say
afterwards which model responded, what it was shown, or whether anything stopped it from writing
something it should not have written. A check made after the response is written can catch a
problem only once the model has already produced it.

The business requires model responses written under rules. The rules apply while the model writes,
not afterwards.

### Models

Before a model can respond to anything, authorized model staff register it. A registration describes
how the model is built, including the amount of text it can read at once, and carries a fingerprint
of its training supplied by whoever provided it. Two registrations with the same description and the
same fingerprint are the same model, and the business holds one record for it.

The fingerprint is the provider's claim. The business records it and does not verify how the model
was trained.

A registered model does not respond to anyone until authorized model staff place it in service. When
they do, they state the most sensitive kind of information the model may read. The kinds, from least
to most sensitive, are public, internal, confidential, and restricted.

### Response rules

When authorized model staff place a model in service, they also set its system prompt and its
response rules. The system prompt is the business's standing instructions to the model, which it
reads with every user prompt. The response rules are:

- words and patterns the model must never write, such as any account number other than the
  customer's own
- how freely the model may choose its words, from always choosing the most likely word to choosing
  more adventurously
- the longest response the model may write

A rule belongs here only if it can be applied while the model writes. A rule that can only be
judged once a response is finished is not a response rule. Such rules belong to a later review of
finished responses, which this release does not include.

"Another customer's account number" depends on who the customer is. The rule is applied for each
user prompt, using the account numbers of the customer the user prompt is for.

The requester cannot change the response rules or the system prompt. They belong to the model's
time in service.

When the model is about to write a word a rule forbids, the rule stops that word and the model
continues with a permitted one. If the model cannot finish a response without breaking a rule, it
gives no response. The user prompt is refused, and the record says which rule stopped it.

A response that reaches its longest permitted length before it is finished is not released. The
user prompt is refused, and the record says so.

### Asking a question

An authorized requester submits a user prompt on behalf of one customer. The user prompt carries the
question and any supporting material, such as the customer's recent transactions. It also names the
model and states the most sensitive kind of information the question and its material contain.

The requester must be permitted to act for that customer. Deciding which requesters may act for
which customers is the business's existing business and is not decided here. Naming a customer does
not by itself give the requester access to that customer's accounts.

What the model reads is exactly the question, the supporting material, and the system prompt of the
model's time in service. Nothing else reaches the model.

A user prompt is refused before the model sees it when:

- the model is not registered
- the model is not in service
- the user prompt contains a more sensitive kind of information than the model may read
- what the model would read is longer than the model can read at once

Every user prompt is recorded, whether responded to or refused, with:

- who asked, and for which customer
- which model, and its time in service
- exactly what the model read: the question, the supporting material, and the system prompt
- the kind of information it contained
- the response rules in force
- the model response, or the reason the user prompt was refused

The record keeps what the model read, not only a summary or fingerprint of it.

The business does not claim that a model response is true. It claims only that the response was
written by the recorded model, from the recorded material, under the recorded rules.

### The test model

Until a real model is available, the business uses a test model. The test model deliberately tries
to break the rules: it tries to write another customer's account number. This lets the business see
the rules hold before a real model is trusted with them. The same rules govern the test model, and
its responses are recorded in the same way.

### What staff and requesters can do

The system shall allow authorized model staff to:

- register a model
- place a registered model in service, with its system prompt and response rules
- withdraw a model from service
- retrieve the record of any user prompt

The system shall allow authorized requesters to:

- submit a user prompt to a model in service, on behalf of a customer

Every business operation shall be traceable and auditable.

The business starts with no models registered.

This release excludes retiring models, reviewing a model response after it is written, letting a
model propose actions, replacing the model in service, and regulator reporting.

Those capabilities are expected to be introduced through future governed change requests rather
than being designed into the initial solution.

## 3. Clarifications answered by the business author

In this release the test model does not respond from material it was not given. The business can
show only that nothing else reached the model, and the record shows that. Catching a response made
up from nothing needs the finished response, and belongs to the later review of finished responses.

Registering a model that is already registered is refused, because the model already has its record.

A withdrawn model may be placed in service again. That begins a new time in service, with its
system prompt and response rules set afresh.

Several models may be in service at the same time. A model that is already in service cannot be
placed in service again; staff withdraw it first. Each time in service has exactly one system prompt
and one set of response rules.

Deciding which staff are authorized model staff is the business's existing business and is not
decided here.
