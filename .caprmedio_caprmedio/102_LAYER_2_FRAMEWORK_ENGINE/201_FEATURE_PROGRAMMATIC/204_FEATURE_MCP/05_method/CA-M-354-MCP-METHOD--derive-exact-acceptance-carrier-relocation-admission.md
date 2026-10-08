---
atom_id: CA-M-354
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-08 17:31:41 +0000"
subjects:
  governs: "MCP/exact acceptance-carrier relocation admission"
  depends_on: [MCP, Projection, Operator, Run, Journal, Source Carrier]
relations:
  relates_to: [CA-P-1117, CA-D-592]
---
# Summary

Derive exact acceptance-carrier relocation admission

## Scope

the one registered relocation of three acceptance carriers under the current Epic.

## Claim

**to** admit the exact acceptance-carrier relocations, derive one candidate from the current binding and the closed CA-D-592-MCP-DELIVERY--register-exact-acceptance-carrier-relocations registration before applying the existing authorized publication lifecycle.

## Details

1. reopen CA-D-592-MCP-DELIVERY--register-exact-acceptance-carrier-relocations, its exact canonical input bytes and the three retained current source carriers; require each current carrier's bytes, identity, version and digest to match its registration.
2. replace only the three registered source-path occurrences from the listed prior path to the listed current path. retain every other manifest field, route, graph, registry pin and source digest unchanged except the resulting canonical serialization and its derived `canonical_manifest_sha256`; the route-identical `selected_binding_digest` remains unchanged.
3. validate the whole candidate against current source pins and the existing selected-route schema. reject any changed topology, alias, unregistered path or mismatched occurrence before intent.
4. seal and publish only through the existing typed Operator context, lock, pending intent, rederivation and atomic readback lifecycle; record the actual result through the existing Work Journal.
5. retain pending publication or recording evidence for recovery. when the exact registered original input, sealed intent and current sources still match, an interrupted pre-effect attempt may retry the same candidate once under the existing lock. once that exact candidate exists, recovery is recording-only and performs no rewrite; ambiguous bytes refuse. historical evidence and installed runtime remain unchanged.
