# TEST_DATA_CT_PURE_DERIVE_WALLET_ADDRESS_V0

## Machine

```yaml
fqdn: blockchain::TEST_DATA_CT_PURE_DERIVE_WALLET_ADDRESS_V0
artifact_kind: TEST_DATA
version: V0
governed_by: conformance::CONSTITUTION_TEST_DATA_V0
authority: pgc.platform
concern: wallet
target: blockchain::CT_PURE_DERIVE_WALLET_ADDRESS_V0
cases:
- case_id: derives_the_address_of_the_generator_key
  expected_outcome: SUCCESS
  bindings:
    key_material: 79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
  expected:
    address: '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
- case_id: prefix_and_tag_derive_the_same_address
  expected_outcome: SUCCESS
  bindings:
    key_material: '0x0479be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8'
  expected:
    address: '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf'
```

## Intent

The address is the last 20 bytes of the key's Keccak-256 hash, with or without the 0x prefix and the 0x04 tag. The key is the secp256k1 generator, whose address is published.
