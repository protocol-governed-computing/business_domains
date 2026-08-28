"""Write one dispatchable payload per catalog workflow, derived from the validation suite.

`execution_validation.py` builds its payloads in process, which proves the criteria but leaves
nothing to dispatch a single workflow with. These are the same payloads, written to disk — derived
from the same helpers rather than hand-authored, so a change to the intents' input surface moves
both together instead of leaving these to rot.

They are a **sequence**, not nine independent cases: 01 registers the book the rest operate on, and
the numbering is the order they must run in against one data root. Run out of order, a payload is
still well-formed and its workflow will refuse it — which is the catalog behaving correctly, not a
broken payload.

Run:  python business_domains/book_library_mgmt/testbed/catalog/emit_payloads.py
"""

from __future__ import annotations

import json
from pathlib import Path

from execution_validation import ODYSSEY, auth, book_payload

HERE = Path(__file__).resolve().parent
OUT = HERE / "test_payloads"

# The key the registry forms from title, author and publication year — case-folded and
# whitespace-collapsed by CT_PURE_FORM_BOOK_IDENTITY_KEY_V0. Written out because a payload that
# addresses a book by key has to state the key the catalog actually holds.
KEY = "the odyssey|homer|1614"

PAYLOADS = {
    "01_register_book": book_payload(ODYSSEY, "BC-0001"),
    "02_register_physical_copy": auth() | {
        "identity_key": KEY, "barcode": "BC-0002",
        "copy_fields": {"barcode": "BC-0002", "state": "REGISTERED", **ODYSSEY}},
    "03_update_bibliographic_information": auth() | {
        **ODYSSEY, "identity_key": KEY,
        "updated_fields": {**ODYSSEY, "subject": ["epic", "poetry", "greek"],
                           "state": "REGISTERED"}},
    "04_search_catalog": auth() | {
        "search_criteria": {"title": "The Odyssey", "state": "REGISTERED"}},
    "05_retrieve_book_details": auth() | {"identity_key": KEY},
    "06_retire_physical_copy": auth() | {"barcode": "BC-0002"},
    "07_reinstate_physical_copy": auth() | {"barcode": "BC-0002"},
    "08_retire_book_record": auth() | {"identity_key": KEY},
    "09_reinstate_book_record": auth() | {"identity_key": KEY},
}

WORKFLOW = {
    "01_register_book": "WF_REGISTER_BOOK_V0",
    "02_register_physical_copy": "WF_REGISTER_PHYSICAL_COPY_V0",
    "03_update_bibliographic_information": "WF_UPDATE_BIBLIOGRAPHIC_INFORMATION_V0",
    "04_search_catalog": "WF_SEARCH_CATALOG_V0",
    "05_retrieve_book_details": "WF_RETRIEVE_BOOK_DETAILS_V0",
    "06_retire_physical_copy": "WF_RETIRE_PHYSICAL_COPY_V0",
    "07_reinstate_physical_copy": "WF_REINSTATE_PHYSICAL_COPY_V0",
    "08_retire_book_record": "WF_RETIRE_BOOK_RECORD_V0",
    "09_reinstate_book_record": "WF_REINSTATE_BOOK_RECORD_V0",
}


def main() -> int:
    OUT.mkdir(exist_ok=True)
    for name, payload in PAYLOADS.items():
        (OUT / f"{name}.json").write_text(json.dumps(payload, indent=2) + "\n")
        print(f"  {name}.json  ->  book_library_mgmt::{WORKFLOW[name]}")
    print(f"\n{len(PAYLOADS)} payload(s) written to {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
