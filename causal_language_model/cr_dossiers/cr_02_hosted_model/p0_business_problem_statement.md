# Business Problem Statement

**Project Name:** causal_language_model — model_response

## 1. Context

The business answers customers' questions about their own accounts using a language model. The model must follow rules while it writes, and every answer or refusal must be recorded.

The first version used a test model. This model deliberately tried to break the rules. It allowed the business to test whether the controls worked before using a real model.

The business now wants to use **Qwen3 8B**, a pretrained model that runs on its own machine. The business did not build or train this model. A program called the *host* loads the model and asks it to generate a response.

The business wants to use Qwen3 under the same rules and record-keeping requirements as the test model. The existing test-model implementation must continue to work.

## 2. Problem Statement

A pretrained model can produce an answer even when it has not been given the information needed to answer the question. For example, a customer might ask for their account balance, but the model might make up a number.

The business must not release such an answer simply because the model produced it.

**The business must control what the model is allowed to write and release.** The model's host may request text from the model, but it cannot decide which text is permitted or send an answer directly to a customer.

The business requires every response to be governed by the rules in force for the model at the time of the request.

### How the model produces a response

The model does not produce its entire response at once. It generates small pieces of text, called tokens, one at a time.

At each step, the host asks the model what it could write next. The model provides a set of candidate tokens, each with a score indicating how likely the model considers that token.

The host passes these candidates to the business. The business applies the response rules and chooses an allowed candidate. The host then gives that choice back to the model, which uses it to generate the next set of candidates.

The process continues until the response is complete or the business must refuse it.

The business records the candidates offered at each step and the candidate it chose. The host cannot override that choice.

The host also cannot send text directly to a customer. The business releases only the completed response held in its own record, after the response has passed the required controls.

### What the business can prove

The business cannot inspect the model's internal computations. It therefore cannot prove that the model itself produced the candidates reported by the host.

Instead, the business records:

* Which model was in service.
* Which response rules applied.
* What candidates the host offered at each step.
* Which candidate the business selected at each step.
* What response, if any, the business released.

The business can then show that the released response was built from candidates selected under the recorded rules, for the recorded model.

It does not claim that the model's answer is true, or that the candidates came from the model as claimed by the host.

### Registering a model

A hosted model must be registered before it can be used.

Its registration includes a description and a fingerprint supplied by the host. The fingerprint identifies the stored model as reported by the host; it is not independent proof of the model's origin or training history.

The description states two limits, measured in tokens:

* How much text the model can read in one request.
* The maximum length of a response it may produce.

Each candidate offer must identify the fingerprint of the model from which it is claimed to have come. If that fingerprint does not match the model selected for the request, the business refuses the request.

The first hosted model is **Qwen3 8B**, running with its thinking mode turned off. It is registered using the fingerprint supplied by its host.

### Applying the response rules

The same response rules used by the test model apply to the hosted model.

As the response is built, the business must:

* Prevent prohibited words or patterns from appearing in the response, including patterns split across several tokens.
* Use the configured degree of freedom to choose among permitted candidates.
* Count the response length in tokens.

If every candidate offered at a step is forbidden, the model cannot continue. The business refuses the request and records the rule that prevented further progress.

If the response reaches the maximum permitted length before it is complete, the business does not release it.

### Numbers come from what the model read

A time in service may require that every number in a response is one the model read. When it does, the business will not let the model begin a number that no number in the reading begins, nor end one that is not a number in the reading.

Numbers match on their digits, so the model may write `$2,410.55` as `2410.55` but may not change a value.

A response in which every candidate would write an ungrounded number is refused, like any other response with no permitted token.

Numbers written as words, and claims that are not numbers, are not judged. A time in service that does not ask for grounding behaves as before.

### Admitting a request

A request to the hosted model is admitted under the same conditions as a request to the test model.

The business checks that:

* The model is registered and in service.
* The requester is authorized to act for the customer.
* The information classification of the request is permitted for that model.
* The request fits within the model's reading capacity.

The host reports how many tokens the model would need to read. The business records that count. If the count exceeds the registered limit, the request is refused before the model begins generating a response.

Every request is recorded, whether it is answered or refused. For hosted-model requests, the record also includes the candidates offered and the choices made at each generation step.

### Keeping the test model

The existing way of submitting requests to the test model remains unchanged.

The test model must also be usable through the hosted-model interface. This allows the same governance rules to be exercised through both paths.

The system shall allow authorized requesters to:

* Submit a request on behalf of a customer to a hosted model that is in service.

The system shall allow the host of a model in service to:

* Offer the next candidates for a response being generated.
* Request release of the completed response.

Every business operation must be traceable and auditable.

### Scope exclusions

This change does not attempt to:

* Prove that a candidate offer came from the model.
* Replace a model while it is in service.
* Review a completed response through a separate review process.
* Govern or verify what the host does before it presents candidates to the business.

## 3. Clarifications

The following decisions define the scope of this change:

* **Model identity:** The registered fingerprint is supplied by the host. The business records and relies on that claim; it does not independently verify the model's origin.
* **Text limits:** Reading capacity and response length are measured in tokens. The host reports the input size, and the business records that report.
* **Existing behavior:** The test model's current request path remains unchanged. The hosted-model path is added alongside it.
* **First hosted model:** Qwen3 8B, running with thinking mode turned off, is the first model registered for this implementation.
* **An abandoned response:** The record of a hosted request opens when the request is admitted and closes when the response is released or refused. A response the host stops offering for stays open in the record, visibly not released.
* **Maximum response length:** A hosted response may be no longer than the smaller of the model's registered maximum and the longest response set in the response rules for its time in service.
* **When the reading size is reported:** The host learns what the model reads only once the business admits the request, so it reports the count with its first offer. A request whose count exceeds the model's reading capacity is refused before any token is chosen or written.
* **The host's authority:** Any caller that names the request and the fingerprint of the model in service may offer candidates. The host holds no authority: it only proposes, and every offer is recorded against the request. Authenticating the host is out of scope.
* **Grounded numbers:** Grounding is set per time in service, as one of its response rules, and applies to hosted responses. A number is grounded when its digits, ignoring the separators between them, are the digits of a number the model read. A grounded number is not thereby true: the business does not claim that.
