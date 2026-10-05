---
atom_id: CA-C-477
content_role: Concern
type: Problem
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 21:52:49 +0000"
subjects:
  governs: "Release Workflow/Gate admission"
  depends_on: [Workflow, Step, Action, Atom, Summary, Evaluation, Journal]
relations:
  concern_about: [CA-P-1743, CA-O-164, CA-O-169]
---
# Summary

Repair Release Operation gate admission

## Concern

The amended Release Operation graph is not yet admitted: Step identity and direct promotion admission do not fully preserve the approved Unit/E2E gate.

## Evidences

1. the independent Operation review rejected retained CA-O-174 and CA-O-177 IDs after their Summaries changed.
2. CA-O-169 still allowed direct promotion with evidence through the image canary, rather than requiring the complete passing Full Gate aggregate.
3. the Unit, Candidate E2E and aggregate definitions lacked explicit non-pass conditions for skipped, excluded, missing or zero-case coverage.

## Blast radius

Release Operation source acceptance, source-frontier binding and actual promotion. The existing public manifest remains retained, not proof of fresh admission after these source changes. The already accepted bootstrap and E2E RMED slices are separate.

## Disposition

Replace the renamed Steps with unused IDs while retaining exact predecessor history. Rewire the active graph, require the exact candidate/frozen-N-bound passing aggregate for direct promotion, and explicitly require complete terminal passing testcase coverage. Obtain independent review before source binding or dispatch. Actual runtime execution remains separately gated; no permission bypass or new public Workflow is authorized.

## Resolution

The independent bounded re-review accepts the repaired source graph and carriers. O185/O186 replace renamed O174/O177; the retired current carriers are archive-only @3 records. O169 requires O184's exact passing Full Gate aggregate even on direct promotion. Unit, E2E and aggregate source rules reject skipped, excluded, missing and zero-case coverage. Eight original active HEAD blobs match their preserved predecessor archives exactly. This resolves source/carrier admission only; private executor acceptance, current manifest rebind and actual runtime gates remain open.
