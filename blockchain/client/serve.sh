#!/usr/bin/env bash
#
# blockchain/identity client — composition launcher.
#
# PURPOSE: a stable, externally observable surface for exercising the COMPLETE PGC execution path
# for blockchain/identity against a KNOWN warm-boot snapshot. It is bound to that snapshot by
# design — not a production application, and it does not generalize across snapshots.
#
#   Assembled snapshot (software_governance + business_domains + workloads)
#         |
#         +-- blockchain identity client   (this surface)
#
# This script is where domain-resident knowledge lives: it points the DOMAIN-NEUTRAL transport HTTP
# adapter at this domain's roots — the web client and the HTTP binding table. Boundary declarations
# (TI/TE) are read from the sealed snapshot, never from here.
#
set -euo pipefail
CLIENT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"     # …/business_domains/blockchain/client
DOMAINS="$(cd "$CLIENT/../.." && pwd)"                     # business_domains/
UMBRELLA="$(cd "$DOMAINS/.." && pwd)"                      # protocol-governed-computing/

export PGC_RUNTIME_ROOT="$UMBRELLA/protocol_runtime"
# The transport engine knows three handler kinds; both interfaces are provisioned even for a
# composition that only executes.
export PGC_INSPECTOR_ROOT="$UMBRELLA/snapshot_inspector"
export PGC_IMPL_ROOTS="$UMBRELLA/software_governance:$DOMAINS"    # capability_*.* + blockchain.*
export PGC_HTTP_BINDINGS="$CLIENT/bindings/http.json"
export PGC_SNAPSHOT_ROOT="${PGC_SNAPSHOT_ROOT:-$UMBRELLA/snapshot}"
export PGC_DATA_ROOT="${PGC_DATA_ROOT:-$UMBRELLA/data/blockchain_client}"
# Static mounts (all READ-ONLY, config-driven). Three roots:
#   /          the web client (splash + identity's two screens)
#   /traces    live per-run evidence from the instance data root (transient)
#   /snapshot  live inspection of the assembled snapshot (compiled artifacts)
# The answer's evidence reference resolves under /traces, so the record of what happened is one
# click from the answer that reports it.
export PGC_STATIC_MOUNTS="/=$CLIENT/web;/traces=$PGC_DATA_ROOT/traces;/snapshot=$PGC_SNAPSHOT_ROOT"
export PGC_HTTP_PORT="${PGC_HTTP_PORT:-8000}"

echo "PGC blockchain/identity client (snapshot-bound)"
echo "  client   : $CLIENT"
echo "  snapshot : $PGC_SNAPSHOT_ROOT"
echo "  data     : $PGC_DATA_ROOT"
echo "  port     : $PGC_HTTP_PORT"
echo

exec "$UMBRELLA/protocol_transport/run_http.sh"
