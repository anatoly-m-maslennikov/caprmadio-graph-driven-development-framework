---
atom_id: CA-E-582
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 10:15:24 +0000"
subjects:
  governs: "MCP/additive Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1882, CA-M-339, CA-D-576]
---
# Summary

Verify additive Release manifest publication

## Scope

functional proof of initial additive Release publication, guarded refresh, exact readback and non-dispatch boundaries.

## Claim

all publisher realizations **must** prove that planning is effect-free and operation-specific trusted execution publishes **only** the exact admitted initial successor or narrow Release-admission refresh with truthful, recoverable canonical Journal evidence.

## Details

1. retain the existing initial fifteen-to-sixteen golden cases and refusal cases. verify that unchanged historical plans and sealed intents retain their original normalization and recovery identity.
2. start refresh fixtures from a genuinely admitted sixteen-route Manifest, then advance an accepted source pin. the ordinary loader **must** reject its stale admission; refresh planning **must** write nothing; authorized refresh **must** preserve all sixteen route rows, query admissions and registry values, replace **only** the Release admission and derived digests, and pass strict output readback.
3. refuse current/no-drift input, fifteen-route input to refresh, sixteen-route input to initial publication, malformed pins, changed Atom identity/source path/ordered occurrence, duplicate JSON members, bad canonical or binding digest, symlink carriers, stale non-Release routes, query-admission drift and registry drift **before** replacement.
4. refuse forged or unregistered Actor contexts and grants for another operation, root, raw input, source frontier or candidate. verify both directions of initial/refresh grant separation.
5. inject source and Manifest drift before authorization, before intent sealing and after intent sealing. verify no unapproved replacement and truthful pending evidence once sealed. require the same carrier lock through final freshness checks and replacement.
6. inject post-write readback and recording failures. recover matching candidate bytes to the same original event exactly once with atomic replacement patched to fail if called. refuse tampered candidate or changed sources and retain the sealed evidence. verify prior-state and successor Journal linkage without another ledger or Run.
7. prove that neither operation dispatches Release, starts a worker, builds an image, changes installed N or claims full-release acceptance. these functional fixtures are not a substitute for the actual complete Release gates.
