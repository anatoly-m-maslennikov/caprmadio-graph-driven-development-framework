---
atom_id: CA-M-339
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 10:15:24 +0000"
subjects:
  governs: "MCP/selected Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  method_for: [CA-R-1882]
---
# Summary

Derive and publish one additive Release manifest successor

## Scope

the construction of initial additive Release publication and its guarded, operation-specific source-pin refresh.

## Claim

the publisher **must** derive and publish the exact admitted additive Release manifest through the existing trusted lifecycle adapter, binding each initial or refresh attempt to its exact canonical input, current D572 source frontier, candidate bytes and canonical Journal evidence.

## Details

1. choose the explicit operation. initial publication uses the normal strict loader and requires fifteen routes with no Release admission. refresh uses the separate narrow refresh-input validator and requires sixteen current routes plus **=1** stale Release admission. the ordinary loader remains strict.
2. derive the current Release route and admission solely through D572's source-owned parser. for refresh, require equality of the Release route and equality of the old admission's complete non-Version/non-digest structure. refuse malformed pins, changed identities or paths, changed occurrences, other stale inputs and no-drift attempts.
3. copy all existing route, query-admission and registry values unchanged. initial publication appends the admitted Release values; refresh replaces **only** its admission. recompute the selected-binding digest and canonical Manifest digest through their existing algorithms.
4. return a byte-preserving plan by default. a refresh plan carries the explicit `publication_operation: refresh` marker; legacy initial plans retain their existing schema. the trusted host validates the registered human Operator and seals the operation, root, raw input digest, current source frontier and exact candidate serialization. caller booleans or callbacks do not grant authority.
5. acquire the existing canonical carrier Journal lock; freshly recheck the input and sources; store one closed pending intent; freshly recheck them again **before** same-directory atomic replacement. preserve the operation marker in refresh intents while keeping historical initial intents unchanged.
6. strictly reopen the complete published bytes through the normal loader, then finalize the existing completed governed-project-change event and its prior-event link. the Journal carrier revision does not give the Projection an independent Version.
7. **after** a recording failure or restart, reopen the exact pending intent and physical target. matching candidate bytes permit finalizing that same event once without a replacement. nonmatching bytes or changed sources retain pending evidence and a truthful blocked/ambiguous result. recovery never grants pre-write authority.
