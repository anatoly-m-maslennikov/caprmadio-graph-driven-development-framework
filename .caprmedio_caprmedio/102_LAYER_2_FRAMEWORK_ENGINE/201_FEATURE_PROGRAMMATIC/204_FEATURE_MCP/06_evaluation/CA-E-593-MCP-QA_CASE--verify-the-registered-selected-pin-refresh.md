---
atom_id: CA-E-593
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:27:56 +0000"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Atom, Source Carrier]
relations:
  relates_to: [CA-P-1800, CA-D-588]
---
# Summary

Verify the registered selected pin refresh

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

the accepted selected-source refresh **must** pass the declared exact-successor and no-effect refusal checks.

## Details

- the registered prior binding yields **=1** successor with eight declared pin replacements, unchanged capability and graph structure, current validated pins and a canonical digest.
- malformed or duplicate registration fields, wrong versions or identities, wrong input/source/archive hashes, unsafe paths, source drift, wrong occurrence counts, unregistered routes and altered topology are rejected before effects.
- publication requires the existing trusted current Operator context; stale candidates or inputs refuse. successful readback is exact and its Journal receipt is real.
- test publication and recording failure separately; pending evidence remains recoverable without replay. all unrelated query admissions and historical Events remain intact.

