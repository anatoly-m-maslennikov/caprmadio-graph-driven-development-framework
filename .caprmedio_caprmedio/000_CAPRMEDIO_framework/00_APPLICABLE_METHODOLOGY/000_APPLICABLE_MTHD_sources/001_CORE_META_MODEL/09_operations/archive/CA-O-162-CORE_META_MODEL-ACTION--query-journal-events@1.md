---
atom_id: CA-O-162
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:30:00 +0400"
subjects:
  governs: "Journal Event query"
  depends_on: [Journal, Event, Tool, Action Run]
relations:
  relates_to: [CA-O-161, CA-O-163, CA-R-1850, CA-R-1861, CA-R-1862, CA-R-1863, CA-R-1864, CA-R-1865, CA-R-1866, CA-R-1867, CA-R-1868, CA-R-1869, CA-R-1870, CA-R-1871, CA-R-1872, CA-M-334, CA-M-335, CA-M-336, CA-M-337, CA-E-575, CA-E-576, CA-E-577, CA-E-578, CA-E-579, CA-E-580, CA-D-555, CA-D-556, CA-D-557, CA-D-558]
---
# Summary

Query Journal Events

## Operation

The Journal Event query Action **must** read one stable snapshot of the selected Project's canonical Events Journal, evaluate only its bounded literal filter grammar, and return Event IDs by default or only caller-selected Event fields or full Events on request.

## Details

The Action reuses CA-R-1850's one shared literal filter grammar. It neither writes Events nor creates a competing Journal, Projection, SQL interpreter, arbitrary-code evaluator, credential reader, mutation authority, or invented Run. It reports exact malformed, missing, duplicate, incomplete, changed-source, coverage, pagination, and filter diagnostics rather than skipping or passing them.

