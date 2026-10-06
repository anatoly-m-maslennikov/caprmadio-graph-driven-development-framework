---
atom_id: CA-C-483
content_role: Concern
type: Problem
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 03:53:17 +0000"
subjects:
  governs: "Repair Release suite scratch and fixture isolation"
  depends_on: [Tool, Implementation, Evaluation, Workflow Run, Journal]
relations:
  concern_about: [CA-P-1755]
---
# Summary

Repair Release suite scratch and fixture isolation

## Concern

N5 has 701 testcase errors and 61 failures; most originate from fixture writes under the read-only candidate workspace, flat import collisions and stale source fixtures.

## Evidences

`release-first-cut-20261006-N5`, candidate snapshot `802ad2f6c604fef46d4405130b90222847855af8e95d1f7e42638293ade50182`: `.caprmedio_runtime/release_suite/802ad2f6c604fef46d4405130b90222847855af8e95d1f7e42638293ade50182/attempt-u02q5q4p/receipt.json`, `coverage.xml` and `output/release-suite-qe2phofb/` hold the terminal testcase results.

Source/mock results do not establish actual release completion.

## Blast radius

The affected selected Workflow, full release gate and CA-P-1655 final acceptance.

## Disposition

Provide fixed bounded in-container scratch and child import isolation; preserve sealed source bytes, no network and no Docker socket. Run the full gate again only with a fresh source-bound Run.

CA-P-1755 owns the bounded repair. Keep this Problem active until its regression and independent acceptance establish the repair.
