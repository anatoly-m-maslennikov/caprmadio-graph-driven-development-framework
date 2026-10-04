---
atom_id: CA-D-529
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 22:25:44 +0400"
subjects:
  governs: "WORKFLOW_OPERATIONS/RUN_SUPPORT/delivery placement"
  depends_on: [Tool, Journal, Workflow, Action, Implementation]
relations:
  delivery_for: [CA-D-527, CA-D-528]
---
# Summary

Place shared selected Run support at the existing TOOLS boundary

## Scope

Implementation placement for the shared service and its existing Journal
dependency. No new Scope Unit, executable Tool, workflow, or Journal is
declared by this Delivery.

## Claim

Shared selected-Run support **must** be delivered as the non-executable library
`102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py`,
beside the existing non-executable `work_journal.py`, and callers must use that
one library rather than adapter-local Run/Journaling implementations.

## Details

- The library owns only request validation, currentness admission, Run
  provenance shaping, pending-recording recovery, and use of `work_journal`.
  Selected route executors, MCP adapters, and prompt/runtime components retain
  their existing ownership and inject their effects/results through the shared
  contract.
- Its only durable historical authority is the Project Work Journal configured
  by Project settings. Its runtime pending/receipt state is under the existing
  `.caprmedio_runtime/state/work_journal/` boundary and must not be projected
  as a competing Journal.
- No caller receives an implicit worker start, background run, new source
  campaign, or authority to mutate from importing the library. A later
  separately approved delivery may add route implementations only after this
  RMED packet has independent review.

