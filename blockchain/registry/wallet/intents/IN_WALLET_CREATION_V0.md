# IN_WALLET_CREATION_V0

## 1. Intent

Admits a request naming the person a wallet is for, and refuses one that names nobody

---

## Machine

```yaml
fqdn: blockchain::IN_WALLET_CREATION_V0
artifact_kind: INTENT
version: v0
governed_by: intent::CONSTITUTION_INTENT_V0
authority: pgc.platform
concern: wallet
core:
  summary: Admits a request naming the person a wallet is for, and refuses one that names nobody
  workflow: WF_CREATE_WALLET_V0
  inputs:
    contact_address:
      type: string
      required: true
    key_material:
      type: string
      required: true
    wallet_id_prefix:
      type: string
      required: true
  outcomes:
    ACK:
      description: Request accepted for processing
    NACK:
      description: Request rejected
```
