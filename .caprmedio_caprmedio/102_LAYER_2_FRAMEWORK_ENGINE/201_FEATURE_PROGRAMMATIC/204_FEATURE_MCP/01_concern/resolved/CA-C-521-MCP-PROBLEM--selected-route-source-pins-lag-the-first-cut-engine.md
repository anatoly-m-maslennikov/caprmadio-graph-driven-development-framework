---
atom_id: CA-C-521
content_role: Concern
type: Problem
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-08 11:14:11 +0000"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Source Carrier]
relations:
  concern_about: [CA-P-1612, CA-P-1123, CA-P-1124, CA-D-588]
---
# Summary

Selected route source pins lag the first cut Engine

## Concern

the first closure check found that Project selected-route admission rejected the repaired first-cut Engine because two declared private-source pins were stale. The connection could not admit an ordinary selected-route status change even when its target Plan had sufficient completion evidence.

## Evidences

- on 2026-10-08, read-only `load_selected_manifest` against the current Project returned `release-source-pin-stale: source pin is stale: 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/backend.py`.
- MCP discovery remained available, but the exact CA-O-127 context returned `context_complete: false`, `input_schema: null` and no selected execution binding. A context request for `change_atom_status` failed.
- the separate source-bound disposable Docker/stdio status corpus passed all eight roles; those accepted test results do not update the live Project binding or authorize mutation with stale pins.

## Blast Radius

selected-route context and dispatch admission, including recording closure of P1615, P1616 and P1612, were affected until the upstream source declarations were corrected. Source-only declarations and callable tool names are not proof of executable current context.

## Disposition

resolved by the accepted source-first correction in `5fab36806`: D572@29 now declares the exact current backend and Docker test bytes, and its existing reader pins that exact revision. Fourteen focused admission cases passed. The normal current admission equals the existing public admission, so the guarded refresh planner correctly reports no drift; no Manifest replacement or Journal publication was needed or performed.

the explicit MCP reload changed generation from `d2132e7b428fbf4375d1a2f4228db6265f587e1bada52b3d5dc7063ba5dee20d` to `b15c00ca6d8663b2651253cfc57d7580ef0ca26addaea5c12689924da7704434`. Actual discovery now reports `change_atom_status` as MCP-available, and its context is complete with the exact native request schema. Strict loading admits the unchanged sixteen routes at canonical Manifest digest `2235d03cdb904942c9b26118a867769696fbe3dfc650eebb6c2e8d49b19bbc4e`. No Workflow was dispatched, Plan status changed, deferred Release executed or installed runtime promoted by this repair.
