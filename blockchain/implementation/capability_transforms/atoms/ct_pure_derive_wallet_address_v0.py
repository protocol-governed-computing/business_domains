"""
CT_PURE_DERIVE_WALLET_ADDRESS_V0

Pure Capability Transform (Atom)

Purpose:
    Derive a wallet's address from public key material the caller supplies.

    The address is a function of the key and nothing else: the same key material always yields the
    same address, and no two distinct keys yield the same one. That is what lets the wallet subdomain
    claim an address as an identity rather than store one somebody chose.

Key material is supplied, never generated:
    This transform takes a public key and computes from it. It does not create entropy, a mnemonic,
    a seed, or any private key, and it holds no secret at any point. That is a decision of the change
    that authored it, and it is what keeps this a *pure* transform — key generation needs entropy,
    entropy is a side effect, and a side effect here would put secret material inside the one layer
    the platform declares has none.

    RI-0's `CT_PURE_DERIVE_WALLET_KEYPAIRS_V0` did generate: BIP39 entropy, an HD seed, and two
    derived keypairs. Only its address step is carried over. The rest is deliberately absent.

Inputs:
    key_material — string; an uncompressed secp256k1 public key as hex, with or without the `0x`
                   prefix, and with or without the leading `04` SEC1 tag

Outputs:
    address — string; `0x`-prefixed, the last 20 bytes of the Keccak-256 hash of the 64-byte key
"""

from typing import Any, Dict

# Keccak-256, not SHA3-256. The two differ in padding and produce different digests for the same
# input, so `hashlib.sha3_256` is not a substitute — it would yield a plausible-looking address that
# no other tool would agree with. `pycryptodome` carries the original Keccak and is already declared
# in `.github/process/requirements-domains.txt`.
from Crypto.Hash import keccak

# An uncompressed secp256k1 public key is 64 bytes: a 32-byte X followed by a 32-byte Y. SEC1 writes
# it with a leading 0x04 tag, which is a marker rather than key material and is dropped before
# hashing — including it would change every address this produces.
KEY_BYTES = 64
SEC1_UNCOMPRESSED_TAG = 0x04
ADDRESS_BYTES = 20


class CTExecutionError(RuntimeError):
    """The supplied key material is not a public key this can derive an address from."""


def _key_bytes(inputs: Dict[str, Any]) -> bytes:
    if "key_material" not in inputs:
        raise CTExecutionError(
            "CT_PURE_DERIVE_WALLET_ADDRESS_V0: requires input 'key_material'"
        )
    value = inputs["key_material"]
    if not isinstance(value, str):
        raise CTExecutionError(
            f"CT_PURE_DERIVE_WALLET_ADDRESS_V0: 'key_material' must be a string, "
            f"got {type(value).__name__}"
        )

    text = value.strip()
    if text[:2].lower() == "0x":
        text = text[2:]
    if not text:
        raise CTExecutionError(
            "CT_PURE_DERIVE_WALLET_ADDRESS_V0: 'key_material' is empty — an address is derived "
            "from a key, and there is no key here"
        )
    try:
        raw = bytes.fromhex(text)
    except ValueError as exc:
        raise CTExecutionError(
            f"CT_PURE_DERIVE_WALLET_ADDRESS_V0: 'key_material' is not hexadecimal — {exc}"
        ) from exc

    if len(raw) == KEY_BYTES + 1 and raw[0] == SEC1_UNCOMPRESSED_TAG:
        raw = raw[1:]
    if len(raw) != KEY_BYTES:
        raise CTExecutionError(
            f"CT_PURE_DERIVE_WALLET_ADDRESS_V0: 'key_material' is {len(raw)} byte(s); an "
            f"uncompressed public key is {KEY_BYTES}, or {KEY_BYTES + 1} with the 0x04 tag. "
            f"Refused rather than padded, because a padded key derives an address nobody owns"
        )
    return raw


def execute(inputs: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    raw = _key_bytes(inputs)

    digest = keccak.new(digest_bits=256)
    digest.update(raw)
    address = "0x" + digest.digest()[-ADDRESS_BYTES:].hex()

    return {"result_status": "SUCCESS", "address": address}
