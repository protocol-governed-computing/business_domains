"""
CT_PURE_FORM_RESPONSE_RULES_V0

Pure Capability Transform (Atom)

Purpose:
    Form the response rules in force for one user prompt. The time in service fixes the forbidden
    words and patterns, the account-number shape, the freedom of word choice and the longest response;
    the user prompt brings the customer's own account numbers and the seed. "Another customer's
    account number" depends on who the customer is, so that rule is formed here, per user prompt: the
    account-number shape is forbidden, except the customer's own numbers.

    It also forms the positions the writing loop runs over, one per word up to the longest response.

Inputs:
    response_rules  — object; forbidden [{rule, pattern}], account_number_pattern, freedom, longest_response
    account_numbers — array; the customer's own account numbers
    seed            — integer; the seed each adventurous choice is drawn from

Outputs:
    rules_in_force — object; forbidden (with the account rule last), freedom, seed
    positions      — array; 1 .. longest_response
"""

import re
from typing import Any, Dict

ACCOUNT_RULE = "another_customers_account_number"


class CTExecutionError(RuntimeError):
    """The time in service's rules cannot be formed into rules in force."""


def _integer(value: Any, name: str, minimum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < minimum:
        raise CTExecutionError(f"CT_PURE_FORM_RESPONSE_RULES_V0: {name!r} must be an integer of at least {minimum}")
    return value


def _pattern(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise CTExecutionError(f"CT_PURE_FORM_RESPONSE_RULES_V0: {name!r} must be a non-empty pattern")
    try:
        re.compile(value)
    except re.error as exc:
        raise CTExecutionError(f"CT_PURE_FORM_RESPONSE_RULES_V0: {name!r} is not a pattern: {exc}") from exc
    return value


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    for field in ("response_rules", "account_numbers", "seed"):
        if field not in inputs:
            raise CTExecutionError(f"CT_PURE_FORM_RESPONSE_RULES_V0: requires input {field!r}")
    rules = inputs["response_rules"]
    if not isinstance(rules, dict):
        raise CTExecutionError("CT_PURE_FORM_RESPONSE_RULES_V0: 'response_rules' must be an object")
    accounts = inputs["account_numbers"]
    if not isinstance(accounts, list) or not all(isinstance(a, str) for a in accounts):
        raise CTExecutionError("CT_PURE_FORM_RESPONSE_RULES_V0: 'account_numbers' must be an array of strings")

    forbidden = []
    for entry in rules.get("forbidden") or []:
        if not isinstance(entry, dict) or not entry.get("rule"):
            raise CTExecutionError("CT_PURE_FORM_RESPONSE_RULES_V0: each forbidden entry names its rule")
        forbidden.append({"rule": entry["rule"], "pattern": _pattern(entry.get("pattern"), entry["rule"])})
    forbidden.append({
        "rule": ACCOUNT_RULE,
        "pattern": _pattern(rules.get("account_number_pattern"), "account_number_pattern"),
        "except": list(accounts),
    })

    longest = _integer(rules.get("longest_response"), "longest_response", 1)
    return {
        "rules_in_force": {
            "forbidden": forbidden,
            "freedom": _integer(rules.get("freedom"), "freedom", 0),
            "seed": _integer(inputs["seed"], "seed", 0),
        },
        "positions": list(range(1, longest + 1)),
    }
