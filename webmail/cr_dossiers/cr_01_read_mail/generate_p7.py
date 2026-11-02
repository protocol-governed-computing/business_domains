"""Write this dossier's P7 from the design stated below.

The design is the tables in this file: acts, contracts, transforms, events and cases. The script
expands them into the registers the design language reads, row by row, and writes
`p7_design_intent_webmail_mailbox_v0.md`. It decides nothing the tables do not state.

    python generate_p7.py
"""

from pathlib import Path

import yaml

D = "webmail"
SUB = "mailbox"
HERE = Path(__file__).resolve().parent
OUT = HERE / "p7_design_intent_webmail_mailbox_v0.md"

RB = f"{D}::RB_MAILBOX_BINDINGS_V0"
STRUCT = f"{D}::STRUCTURE_MAILBOX_STORAGE_V0"
APPEND = "capability_side_effects::CS_APPENDONLY_JSONL_V0"
ASSEMBLE = "capability_transforms::CT_PURE_ASSEMBLE_RECORD_V0"
MEMBER = "capability_transforms::CT_PURE_VALIDATE_SET_MEMBERSHIP_V0"
STORE = "MAILBOX_RECORDS"
HOST = f"{D}::AC_MAIL_HOST_V0"


def fq(code):
    return code if "::" in code else f"{D}::{code}"


def cite(phase, register, row):
    return {"phase": phase, "register": register, "row": row}


# ── P5 rows each artifact answers to ──────────────────────────────────────────────────────────

P5_CODE_ROW = {  # provisional_codes row, 1-based, in P5's order
    "AC_MAIL_HOST_V0": 1, "WF_LIST_FOLDER_V0": 2, "WF_OPEN_MESSAGE_V0": 3, "WF_MARK_MESSAGE_V0": 4,
    "WF_REPORT_CHANGE_OUTCOME_V0": 5, "IN_LIST_FOLDER_V0": 6, "IN_OPEN_MESSAGE_V0": 7,
    "IN_MARK_MESSAGE_V0": 8, "IN_REPORT_CHANGE_OUTCOME_V0": 9, "CC_CONFIRM_PROVIDER_ANSWERED_V0": 10,
    "CC_CHOOSE_FOLDER_PAGE_V0": 11, "CC_CHOOSE_MESSAGE_TEXT_V0": 12, "CC_DECIDE_READ_STATE_V0": 13,
    "CC_RECORD_MAILBOX_REQUEST_V0": 14, "CT_PURE_CHOOSE_FOLDER_PAGE_V0": 15,
    "CT_PURE_CHOOSE_MESSAGE_TEXT_V0": 16, "CT_PURE_DECIDE_READ_STATE_V0": 17, "EV_FOLDER_LISTED_V0": 18,
    "EV_MESSAGE_OPENED_V0": 19, "EV_READ_STATE_CHANGED_V0": 20, "EV_MAILBOX_REQUEST_REFUSED_V0": 21,
    "STRUCTURE_MAILBOX_STORAGE_V0": 22, "RB_MAILBOX_BINDINGS_V0": 23,
}
CAPABILITY = {  # the business capability each family serves, from P6's ownership
    "WF_LIST_FOLDER_V0": "List a folder", "IN_LIST_FOLDER_V0": "List a folder",
    "CC_CHOOSE_FOLDER_PAGE_V0": "List a folder", "CT_PURE_CHOOSE_FOLDER_PAGE_V0": "List a folder",
    "EV_FOLDER_LISTED_V0": "List a folder",
    "WF_OPEN_MESSAGE_V0": "Open a message", "IN_OPEN_MESSAGE_V0": "Open a message",
    "CC_CHOOSE_MESSAGE_TEXT_V0": "Open a message", "CT_PURE_CHOOSE_MESSAGE_TEXT_V0": "Open a message",
    "EV_MESSAGE_OPENED_V0": "Open a message",
    "WF_MARK_MESSAGE_V0": "Mark a message as read or unread",
    "IN_MARK_MESSAGE_V0": "Mark a message as read or unread",
    "CC_DECIDE_READ_STATE_V0": "Mark a message as read or unread",
    "CT_PURE_DECIDE_READ_STATE_V0": "Mark a message as read or unread",
    "WF_REPORT_CHANGE_OUTCOME_V0": "Report a change's outcome",
    "IN_REPORT_CHANGE_OUTCOME_V0": "Report a change's outcome",
    "EV_READ_STATE_CHANGED_V0": "Report a change's outcome",
}
SHARED = "Every mailbox act"


def p5(code):
    return cite("p5", "provisional_codes", P5_CODE_ROW[code])


# ── The design ────────────────────────────────────────────────────────────────────────────────

S, I, B, A, O = "string", "integer", "boolean", "array", "object"

ACTOR = {"code": "AC_MAIL_HOST_V0",
         "summary": "The program that reaches a person's mail provider; it reports and carries out, and holds no authority",
         "attributes": [("host_id", S, "Which host is calling")]}

COMMON_IN = [("host_id", S, "Which host reports"),
             ("mailbox", S, "The mailbox the request concerns, which also says who asked"),
             ("folder", S, "The folder the request concerns"),
             ("provider_answer", S, "What the provider answered: ANSWERED, CREDENTIALS_REJECTED, UNREACHABLE, NO_SUCH_FOLDER or NO_SUCH_MESSAGE")]

INTENTS = {
    "IN_LIST_FOLDER_V0": ("A host's report of a folder's message identifiers and the page asked for",
                          COMMON_IN + [("message_ids", A, "The folder's message identifiers, in the order the provider received them"),
                                       ("page", I, "The page asked for, counting from 1")]),
    "IN_OPEN_MESSAGE_V0": ("A host's report of the read state and the parts of a message the person asked to open",
                           COMMON_IN + [("message_id", I, "The message asked for"),
                                        ("seen", B, "Whether the provider holds the message as read"),
                                        ("parts", A, "The message's parts, each with its part number and kind, and none of its content")]),
    "IN_MARK_MESSAGE_V0": ("A host's report of a message's read state and the state the person asked for",
                           COMMON_IN + [("message_id", I, "The message asked for"),
                                        ("seen", B, "Whether the provider holds the message as read"),
                                        ("wanted_read", B, "Whether the person asked for the message to be read")]),
    "IN_REPORT_CHANGE_OUTCOME_V0": ("A host's report of whether the provider accepted a decided change",
                                    COMMON_IN + [("message_id", I, "The message the change concerned"),
                                                 ("change", S, "The change the business decided: SET_READ or SET_UNREAD")]),
}

TRANSFORMS = {
    "CT_PURE_CHOOSE_FOLDER_PAGE_V0": {
        "summary": "Orders identifiers newest received first and cuts the page asked for",
        "operation": "CHOOSE_FOLDER_PAGE",
        "in": [("message_ids", A, "The folder's message identifiers, in the order the provider received them"),
               ("page", I, "The page asked for, counting from 1"),
               ("page_size", I, "How many messages make one page")],
        "out": [("page_ids", A, "The identifiers of the page, newest received first"),
                ("more_exist", B, "Whether messages exist beyond this page"),
                ("folder_empty", B, "Whether the folder holds no messages"),
                ("message_count", I, "How many messages the folder holds")],
    },
    "CT_PURE_CHOOSE_MESSAGE_TEXT_V0": {
        "summary": "Chooses a message's plain-text part from its parts, or says its text cannot be displayed yet",
        "operation": "CHOOSE_MESSAGE_TEXT",
        "in": [("parts", A, "The message's parts, each with its part number and kind")],
        "out": [("text_part", S, "The part number of the plain text shown, or empty when there is none"),
                ("text_displayable", B, "Whether the message has plain text to show"),
                ("shown_headers", A, "The headers shown with the message")],
    },
    "CT_PURE_DECIDE_READ_STATE_V0": {
        "summary": "Decides a change of read state from the state held and the state asked for",
        "operation": "DECIDE_READ_STATE",
        "in": [("seen", B, "Whether the provider holds the message as read"),
               ("wanted_read", B, "Whether the message is to be read")],
        "out": [("change", S, "SET_READ, SET_UNREAD or NONE"),
                ("read_now", B, "Whether the message is read once the decision is carried out")],
    },
}

# CC: (summary, inputs, outputs, statuses, steps). A step: (name, capability, kind, op, store,
#      consumes, produces, routing, input bindings {field: bound_to}, output bindings {field: bound_to})
CONTRACTS = {
    "CC_CONFIRM_PROVIDER_ANSWERED_V0": (
        "Confirms the provider answered, refusing otherwise",
        [("provider_answer", S, "What the provider answered")],
        [("answered", B, "Whether the provider answered")],
        ["SUCCESS", "VIOLATION"],
        [("confirm_answered", MEMBER, "CT", None, None, ["value", "allowed_set"], ["is_member"],
          {"SUCCESS": "exit", "VIOLATION": "exit"},
          {"value": "inputs.provider_answer", "allowed_set": {"literal": ["ANSWERED"]}},
          {"answered": "capability_result.is_member"})]),
    "CC_CHOOSE_FOLDER_PAGE_V0": (
        "Chooses a page of a folder's identifiers, newest received first",
        [("message_ids", A, "The folder's message identifiers, in received order"),
         ("page", I, "The page asked for")],
        [("page_ids", A, "The identifiers of the page"), ("more_exist", B, "Whether more exist"),
         ("folder_empty", B, "Whether the folder is empty"), ("message_count", I, "How many the folder holds")],
        ["SUCCESS", "VIOLATION"],
        [("choose_page", fq("CT_PURE_CHOOSE_FOLDER_PAGE_V0"), "CT", None, None,
          ["message_ids", "page", "page_size"], ["page_ids", "more_exist", "folder_empty", "message_count"],
          {"SUCCESS": "exit", "VIOLATION": "exit"},
          {"message_ids": "inputs.message_ids", "page": "inputs.page", "page_size": {"literal": 50}},
          {f: f"capability_result.{f}" for f in ("page_ids", "more_exist", "folder_empty", "message_count")})]),
    "CC_CHOOSE_MESSAGE_TEXT_V0": (
        "Chooses the plain-text part of a message to show, or says none can be displayed",
        [("parts", A, "The message's parts")],
        [("text_part", S, "The plain-text part shown"), ("text_displayable", B, "Whether there is plain text"),
         ("shown_headers", A, "The headers shown")],
        ["SUCCESS", "VIOLATION"],
        [("choose_text", fq("CT_PURE_CHOOSE_MESSAGE_TEXT_V0"), "CT", None, None,
          ["parts"], ["text_part", "text_displayable", "shown_headers"],
          {"SUCCESS": "exit", "VIOLATION": "exit"},
          {"parts": "inputs.parts"},
          {f: f"capability_result.{f}" for f in ("text_part", "text_displayable", "shown_headers")})]),
    "CC_DECIDE_READ_STATE_V0": (
        "Decides whether a message becomes read, becomes unread or stays as it is",
        [("seen", B, "Whether the message is read"), ("wanted_read", B, "Whether it is to be read")],
        [("change", S, "The change decided"), ("read_now", B, "Whether it is read once carried out")],
        ["SUCCESS", "VIOLATION"],
        [("decide_read_state", fq("CT_PURE_DECIDE_READ_STATE_V0"), "CT", None, None,
          ["seen", "wanted_read"], ["change", "read_now"],
          {"SUCCESS": "exit", "VIOLATION": "exit"},
          {"seen": "inputs.seen", "wanted_read": "inputs.wanted_read"},
          {"change": "capability_result.change", "read_now": "capability_result.read_now"})]),
    "CC_RECORD_MAILBOX_REQUEST_V0": (
        "Adds an entry to the mailbox record",
        [("entry", O, "What was asked, decided and answered, by identifier only"),
         ("host_id", S, "Which host reported")],
        [("entry", O, "The entry added"), ("record_id", S, "The entry's record identifier"),
         ("sequence_number", I, "The entry's place in the record")],
        ["SUCCESS", "VIOLATION", "BACKEND_ERROR"],
        [("assemble_entry", ASSEMBLE, "CT", None, None, ["fields"], ["record"],
          {"SUCCESS": "continue"},
          {"fields": "inputs.entry"}, {"entry": "capability_result.record"}),
         ("append_entry", APPEND, "CS", "APPEND", STORE, ["record", "stream_id", "actor_id"],
          ["record_id", "sequence_number"],
          {"SUCCESS": "exit", "VIOLATION": "exit", "BACKEND_ERROR": "exit"},
          {"record": "results.assemble_entry.entry", "stream_id": {"literal": STORE},
           "actor_id": "inputs.host_id"},
          {"record_id": "capability_result.record_id",
           "sequence_number": "capability_result.sequence_number"})]),
}

EVENTS = {
    "EV_FOLDER_LISTED_V0": ("A folder's page was chosen for the person", None),
    "EV_MESSAGE_OPENED_V0": ("A message was opened for the person", None),
    "EV_READ_STATE_CHANGED_V0": ("The provider accepted a decided change of read state", None),
    "EV_MAILBOX_REQUEST_REFUSED_V0": ("A request was refused", "refusal"),
}
EVENT_FIELDS = [("entry", O, "The record entry, by identifier only"),
                ("sequence_number", I, "The entry's place in the record")]

P = "$.payload."


def entry(request, outcome, **extra):
    e = {"request": request, "mailbox": P + "mailbox", "folder": P + "folder", "outcome": outcome,
         "provider_answer": P + "provider_answer"}
    e.update(extra)
    return e


def record(node, request, outcome, ok, **extra):
    return (node, "CC_RECORD_MAILBOX_REQUEST_V0",
            {"SUCCESS": ok, "VIOLATION": "EXIT_REJECTED", "BACKEND_ERROR": "EXIT_REJECTED"},
            {"host_id": "payload.host_id", "entry": {"literal": entry(request, outcome, **extra)}})


def refusals(request, with_message):
    m = {"message_id": P + "message_id"} if with_message else {}
    return [
        record("RECORD_REFUSED", request, "REFUSED", "EXIT_REFUSED", reason=P + "provider_answer", **m),
        record("RECORD_REPORT_REFUSED", request, "REFUSED", "EXIT_REFUSED", reason="REPORT_NOT_VALID", **m),
    ]


def confirm(next_ok):
    return ("CONFIRM_ANSWERED", "CC_CONFIRM_PROVIDER_ANSWERED_V0",
            {"SUCCESS": next_ok, "VIOLATION": "RECORD_REFUSED"},
            {"provider_answer": "payload.provider_answer"})


PAGE = "$.results.CC_CHOOSE_FOLDER_PAGE_V0."
TEXT = "$.results.CC_CHOOSE_MESSAGE_TEXT_V0."
READ = "$.results.CC_DECIDE_READ_STATE_V0."

# WF: (summary, intent, nodes [(key, cc, routing, inputs)], exits {exit: event|None}, P5 action row)
WORKFLOWS = {
    "WF_LIST_FOLDER_V0": (
        "Chooses which messages make the page of a folder the person asked for, newest received first",
        "IN_LIST_FOLDER_V0",
        [confirm("CC_CHOOSE_FOLDER_PAGE_V0"),
         ("CC_CHOOSE_FOLDER_PAGE_V0", "CC_CHOOSE_FOLDER_PAGE_V0",
          {"SUCCESS": "RECORD_LISTED", "VIOLATION": "RECORD_REPORT_REFUSED"},
          {"message_ids": "payload.message_ids", "page": "payload.page"}),
         record("RECORD_LISTED", "LIST_FOLDER", "ANSWERED", "EXIT_LISTED", page=P + "page",
                page_ids=PAGE + "page_ids", more_exist=PAGE + "more_exist",
                folder_empty=PAGE + "folder_empty", message_count=PAGE + "message_count"),
         *refusals("LIST_FOLDER", False)],
        {"EXIT_LISTED": "EV_FOLDER_LISTED_V0", "EXIT_REFUSED": "EV_MAILBOX_REQUEST_REFUSED_V0",
         "EXIT_REJECTED": None},
        1),
    "WF_OPEN_MESSAGE_V0": (
        "Chooses what of a message is shown and decides that it becomes read",
        "IN_OPEN_MESSAGE_V0",
        [confirm("CC_CHOOSE_MESSAGE_TEXT_V0"),
         ("CC_CHOOSE_MESSAGE_TEXT_V0", "CC_CHOOSE_MESSAGE_TEXT_V0",
          {"SUCCESS": "CC_DECIDE_READ_STATE_V0", "VIOLATION": "RECORD_REPORT_REFUSED"},
          {"parts": "payload.parts"}),
         ("CC_DECIDE_READ_STATE_V0", "CC_DECIDE_READ_STATE_V0",
          {"SUCCESS": "RECORD_OPENED", "VIOLATION": "RECORD_REPORT_REFUSED"},
          {"seen": "payload.seen", "wanted_read": {"literal": True}}),
         record("RECORD_OPENED", "OPEN_MESSAGE", "ANSWERED", "EXIT_OPENED",
                message_id=P + "message_id", text_part=TEXT + "text_part",
                text_displayable=TEXT + "text_displayable", shown_headers=TEXT + "shown_headers",
                change=READ + "change", read_now=READ + "read_now"),
         *refusals("OPEN_MESSAGE", True)],
        {"EXIT_OPENED": "EV_MESSAGE_OPENED_V0", "EXIT_REFUSED": "EV_MAILBOX_REQUEST_REFUSED_V0",
         "EXIT_REJECTED": None},
        2),
    "WF_MARK_MESSAGE_V0": (
        "Decides a change of a message's read state, or that nothing changes",
        "IN_MARK_MESSAGE_V0",
        [confirm("CC_DECIDE_READ_STATE_V0"),
         ("CC_DECIDE_READ_STATE_V0", "CC_DECIDE_READ_STATE_V0",
          {"SUCCESS": "RECORD_MARKED", "VIOLATION": "RECORD_REPORT_REFUSED"},
          {"seen": "payload.seen", "wanted_read": "payload.wanted_read"}),
         record("RECORD_MARKED", "MARK_MESSAGE", "ANSWERED", "EXIT_MARKED",
                message_id=P + "message_id", wanted_read=P + "wanted_read",
                change=READ + "change", read_now=READ + "read_now"),
         *refusals("MARK_MESSAGE", True)],
        {"EXIT_MARKED": None, "EXIT_REFUSED": "EV_MAILBOX_REQUEST_REFUSED_V0", "EXIT_REJECTED": None},
        3),
    "WF_REPORT_CHANGE_OUTCOME_V0": (
        "Records whether the provider accepted a change the business decided",
        "IN_REPORT_CHANGE_OUTCOME_V0",
        [confirm("RECORD_CHANGED"),
         record("RECORD_CHANGED", "REPORT_CHANGE_OUTCOME", "ANSWERED", "EXIT_CHANGED",
                message_id=P + "message_id", change=P + "change"),
         refusals("REPORT_CHANGE_OUTCOME", True)[0]],
        {"EXIT_CHANGED": "EV_READ_STATE_CHANGED_V0", "EXIT_REFUSED": "EV_MAILBOX_REQUEST_REFUSED_V0",
         "EXIT_REJECTED": None},
        4),
}

# Cases: CT -> [(case, outcome, {input}, {expected})]
CASES = {
    "CT_PURE_CHOOSE_FOLDER_PAGE_V0": [
        ("first_page_is_newest_received_first", "SUCCESS",
         {"message_ids": [3, 7, 9, 12], "page": 1, "page_size": 2},
         {"page_ids": [12, 9], "more_exist": True, "folder_empty": False, "message_count": 4}),
        ("last_page_says_no_more_exist", "SUCCESS",
         {"message_ids": [3, 7, 9, 12], "page": 2, "page_size": 2},
         {"page_ids": [7, 3], "more_exist": False, "folder_empty": False, "message_count": 4}),
        ("received_order_decides_not_the_identifier", "SUCCESS",
         {"message_ids": [40, 5, 22], "page": 1, "page_size": 50},
         {"page_ids": [22, 5, 40], "more_exist": False, "folder_empty": False, "message_count": 3}),
        ("empty_folder_answers_empty", "SUCCESS",
         {"message_ids": [], "page": 1, "page_size": 50},
         {"page_ids": [], "more_exist": False, "folder_empty": True, "message_count": 0}),
        ("a_page_before_the_first_is_refused", "VIOLATION",
         {"message_ids": [1, 2], "page": 0, "page_size": 50}, {}),
        ("an_identifier_that_is_not_a_number_is_refused", "VIOLATION",
         {"message_ids": [1, "two"], "page": 1, "page_size": 50}, {}),
    ],
    "CT_PURE_CHOOSE_MESSAGE_TEXT_V0": [
        ("plain_text_part_is_chosen", "SUCCESS",
         {"parts": [{"part": "1", "kind": "text/plain"}, {"part": "2", "kind": "text/html"}]},
         {"text_part": "1", "text_displayable": True,
          "shown_headers": ["from", "to", "cc", "subject", "date"]}),
        ("first_plain_text_part_wins", "SUCCESS",
         {"parts": [{"part": "1.1", "kind": "text/plain"}, {"part": "2", "kind": "text/plain"}]},
         {"text_part": "1.1", "text_displayable": True,
          "shown_headers": ["from", "to", "cc", "subject", "date"]}),
        ("kind_is_read_without_regard_to_case", "SUCCESS",
         {"parts": [{"part": "1", "kind": "TEXT/PLAIN"}]},
         {"text_part": "1", "text_displayable": True,
          "shown_headers": ["from", "to", "cc", "subject", "date"]}),
        ("html_only_cannot_be_displayed_yet", "SUCCESS",
         {"parts": [{"part": "1", "kind": "text/html"}]},
         {"text_part": "", "text_displayable": False,
          "shown_headers": ["from", "to", "cc", "subject", "date"]}),
        ("a_part_without_a_kind_is_refused", "VIOLATION",
         {"parts": [{"part": "1"}]}, {}),
    ],
    "CT_PURE_DECIDE_READ_STATE_V0": [
        ("unread_asked_read_becomes_read", "SUCCESS",
         {"seen": False, "wanted_read": True}, {"change": "SET_READ", "read_now": True}),
        ("read_asked_unread_becomes_unread", "SUCCESS",
         {"seen": True, "wanted_read": False}, {"change": "SET_UNREAD", "read_now": False}),
        ("read_asked_read_changes_nothing", "SUCCESS",
         {"seen": True, "wanted_read": True}, {"change": "NONE", "read_now": True}),
        ("unread_asked_unread_changes_nothing", "SUCCESS",
         {"seen": False, "wanted_read": False}, {"change": "NONE", "read_now": False}),
        ("a_state_that_is_not_true_or_false_is_refused", "VIOLATION",
         {"seen": "yes", "wanted_read": True}, {}),
    ],
}

# P0 operation_refusals, discharged per act at the step that refuses.
ALL_ACTS = "list a folder, open a message, mark a message"
REFUSALS = [  # (P0 row, operation, refused_when), exactly as P0 states them
    (1, ALL_ACTS, "the provider rejects the person's credentials"),
    (2, ALL_ACTS, "the provider cannot be reached, or does not answer in time"),
    (3, ALL_ACTS, "the folder does not exist"),
    (4, "open a message, mark a message", "the message does not exist in the folder"),
]
REFUSAL_ACTS = {1: ["WF_LIST_FOLDER_V0", "WF_OPEN_MESSAGE_V0", "WF_MARK_MESSAGE_V0"],
                2: ["WF_LIST_FOLDER_V0", "WF_OPEN_MESSAGE_V0", "WF_MARK_MESSAGE_V0"],
                3: ["WF_LIST_FOLDER_V0", "WF_OPEN_MESSAGE_V0", "WF_MARK_MESSAGE_V0"],
                4: ["WF_OPEN_MESSAGE_V0", "WF_MARK_MESSAGE_V0"]}
REUSED = [
    (APPEND, "Append-only persistence with ordered history", "The record is only ever added to."),
    (ASSEMBLE, "Combines input values into a single record", "Each entry is assembled before it is added."),
    (MEMBER, "Validates that a value is a member of a declared set",
     "Each act confirms with it that the provider answered."),
]
OPERATION = {"WF_LIST_FOLDER_V0": "list a folder", "WF_OPEN_MESSAGE_V0": "open a message",
             "WF_MARK_MESSAGE_V0": "mark a message"}


# ── Expansion into registers ──────────────────────────────────────────────────────────────────

def field_rows(artifact, direction, fields):
    return [{"artifact": fq(artifact), "direction": direction, "field": n, "type": t,
             "required": "YES", "default": None, "meaning": m} for n, t, m in fields]


def build():
    r = {k: [] for k in (
        "design_resolution", "existing_inventory", "new_artifacts", "rb_declarations",
        "execution_topology", "cc_composition", "step_bindings", "interface_fields",
        "implementation_bindings", "vocabulary_extensions", "runtime_policies",
        "artifact_properties", "structure_stores", "transport_bindings", "artifact_summary",
        "generation_provenance", "declared_reach", "refusal_discharge", "refusal_deferrals",
        "refusal_governance_discharge", "molecule_steps", "molecule_step_bindings", "test_cases",
        "test_case_values")}

    def new(code, family, summary):
        r["new_artifacts"].append({
            "capability": CAPABILITY.get(code, SHARED), "family": family, "code": fq(code),
            "summary": summary, "owner_subdomain": SUB, "status": "NEW", "source_finding": p5(code)})

    for n, (code, summary, reason) in enumerate(REUSED, 1):
        r["existing_inventory"].append({"fqdn": code, "action": "REUSE", "summary": summary,
                                        "reason": reason,
                                        "source_finding": cite("p3", "dependency_discoveries", n)})

    new(ACTOR["code"], "AC", ACTOR["summary"])
    r["interface_fields"] += field_rows(ACTOR["code"], "ATTRIBUTE", ACTOR["attributes"])
    r["artifact_properties"].append({"artifact": fq(ACTOR["code"]), "property": "type",
                                     "value": "system", "source_finding": p5(ACTOR["code"])})

    for code, (summary, fields) in INTENTS.items():
        new(code, "IN", summary)
        r["interface_fields"] += field_rows(code, "INPUT", fields)

    for code, t in TRANSFORMS.items():
        new(code, "CT", t["summary"])
        r["interface_fields"] += field_rows(code, "INPUT", t["in"]) + field_rows(code, "OUTPUT", t["out"])
        r["implementation_bindings"].append({
            "ct_code": fq(code), "callable": "execute", "operation": t["operation"], "kind": "atom",
            "purity": "ct_pure", "refusal": "raises", "source_finding": p5(code)})
        for case, outcome, given, expected in CASES[code]:
            r["test_cases"].append({"ct_code": fq(code), "case": case, "expected_outcome": outcome,
                                    "source_finding": p5(code)})
            for role, values in (("INPUT", given), ("EXPECTED", expected)):
                for f, v in values.items():
                    r["test_case_values"].append({"ct_code": fq(code), "case": case, "role": role,
                                                  "field": f, "value": v, "source_finding": p5(code)})

    for code, (summary, ins, outs, statuses, steps) in CONTRACTS.items():
        new(code, "CC", summary)
        r["interface_fields"] += field_rows(code, "INPUT", ins) + field_rows(code, "OUTPUT", outs)
        for n, (name, cap, kind, op, store, consumes, produces, routing, bind_in, bind_out) in enumerate(steps, 1):
            r["cc_composition"].append({
                "cc_code": fq(code), "step": str(n), "step_name": name, "capability": cap, "kind": kind,
                "operation": op, "store": store, "consumes": consumes, "produces": produces,
                "routing": routing, "interpreted_by": None, "semantic_status": "SUCCESS",
                "interface": {"in": {c: c for c in consumes},
                              "out": {b.split(".")[-1]: f for f, b in bind_out.items()}}})
            for f, b in bind_in.items():
                r["step_bindings"].append({"owner": fq(code), "step": name, "direction": "INPUT",
                                           "field": f, "bound_to": b, "source_finding": p5(code)})
            for f, b in bind_out.items():
                r["step_bindings"].append({"owner": fq(code), "step": name, "direction": "OUTPUT",
                                           "field": f, "bound_to": b, "source_finding": p5(code)})

    for code, (summary, moment) in EVENTS.items():
        new(code, "EV", summary)
        r["interface_fields"] += field_rows(code, "OUTPUT", EVENT_FIELDS)
        if moment:
            r["artifact_properties"].append({"artifact": fq(code), "property": "moment",
                                             "value": moment, "source_finding": p5(code)})

    for code, (summary, intent, nodes, exits, action_row) in WORKFLOWS.items():
        new(code, "WF", summary)
        src = cite("p5", "actions", action_row)
        # A node named by the contract it runs is written by its full name; a place keyed apart
        # from its contract keeps its key and names the contract under `runs`.
        named = {key for key, cc, _, _ in nodes if key == cc}

        def place(key):
            return fq(key) if key in named else key

        first = nodes[0][0]
        r["execution_topology"].append({"workflow": fq(code), "node": fq(intent), "node_type": "IN",
                                        "routing": {"ACK": place(first), "NACK": "EXIT_REJECTED"},
                                        "source_finding": src})
        for key, cc, routing, inputs in nodes:
            row = {"workflow": fq(code), "node": place(key), "node_type": "CC",
                   "routing": {o: place(d) for o, d in routing.items()}, "source_finding": src}
            if key != cc:
                row["runs"] = fq(cc)
            r["execution_topology"].append(row)
            for f, b in inputs.items():
                r["step_bindings"].append({"owner": fq(code), "step": place(key), "direction": "INPUT",
                                           "field": f, "bound_to": b, "source_finding": src})
        for ex, ev in exits.items():
            kind = "EXIT" if ex in ("EXIT_REFUSED", "EXIT_REJECTED") else "EXIT_SUCCESS"
            r["execution_topology"].append({"workflow": fq(code), "node": ex, "node_type": kind,
                                            "routing": None, "source_finding": src})
            if ev:
                r["artifact_properties"].append({"artifact": fq(code), "property": f"emit.{ex}",
                                                 "value": [fq(ev)], "source_finding": src})
        r["artifact_properties"].append({"artifact": fq(code), "property": "actor_context",
                                         "value": HOST, "source_finding": src})
        r["rb_declarations"].append({"rb_code": RB, "binds_wf": fq(code), "cs_bindings": [APPEND],
                                     "storage_structure": STRUCT, "source_finding": p5("RB_MAILBOX_BINDINGS_V0")})

    new("STRUCTURE_MAILBOX_STORAGE_V0", "STRUCTURE", "Declares the mailbox record and the path it occupies")
    r["artifact_properties"].append({"artifact": STRUCT, "property": "layer", "value": "DOMAINS",
                                     "source_finding": p5("STRUCTURE_MAILBOX_STORAGE_V0")})
    r["structure_stores"].append({"store_name": STORE, "storage_type": "CS_APPENDONLY_JSONL_V0",
                                  "proposed_path": f"{D}/{SUB}/mailbox_records.jsonl",
                                  "used_by": fq("CC_RECORD_MAILBOX_REQUEST_V0"), "structure": STRUCT,
                                  "source_finding": cite("p6", "storage_governance", 1)})
    new("RB_MAILBOX_BINDINGS_V0", "RB", "Binds every mailbox act to the record it appends to")
    r["runtime_policies"].append({"rb_code": RB, "capability": APPEND, "key": "structure",
                                  "value": STRUCT, "source_finding": p5("RB_MAILBOX_BINDINGS_V0")})

    for row, operation, when in REFUSALS:
        for wf in REFUSAL_ACTS[row]:
            r["refusal_discharge"].append({
                "operation": operation, "refused_when": when, "act": fq(wf),
                "step": "RECORD_REFUSED", "outcome": "SUCCESS",
                "source_finding": cite("p0", "operation_refusals", row)})

    codes = sorted(a["code"] for a in r["new_artifacts"])
    r["artifact_summary"].append({"action": "NEW", "subdomain": SUB, "count": str(len(codes)),
                                  "artifacts": ", ".join(codes)})
    r["withdrawn_facts"] = None
    return r


def main():
    doc = {"document": {"phase": "p7", "domain": D, "subdomain": SUB, "cr": "cr_01_read_mail",
                        "rule_set": "transformation.schemas.REGISTER_SCHEMA_P7_V0"},
           "registers": build()}
    body = yaml.safe_dump(doc, sort_keys=False, allow_unicode=True, width=120)
    OUT.write_text(
        "# Design Intent — webmail / mailbox\n\n## Machine\n\n```yaml\n" + body + "```\n\n"
        "Generated by `generate_p7.py` in this dossier from the design tables it states. Every row "
        "cites the P5, P6 or P0 row it realises.\n")
    print(f"wrote {OUT.name}")


if __name__ == "__main__":
    main()
