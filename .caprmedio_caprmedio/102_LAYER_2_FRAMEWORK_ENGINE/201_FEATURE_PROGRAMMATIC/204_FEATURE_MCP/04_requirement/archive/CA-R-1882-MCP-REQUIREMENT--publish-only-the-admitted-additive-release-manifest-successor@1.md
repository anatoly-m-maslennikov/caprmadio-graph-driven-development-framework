---
atom_id: CA-R-1882
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:18:46 +0400"
subjects:
  governs: "MCP/selected Release manifest publisher"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1847, CA-R-1848, CA-D-572, CA-P-1622]
---
# Summary

Publish only the admitted additive Release manifest successor

## Scope

The Project-local MCP capability that derives one selected-workflow manifest successor from the current canonical fifteen-route Projection.

## Claim

MCP **must** provide a plan-first publisher that admits explicit authorized execution only to transform the current canonical fifteen-route selected-workflow manifest into its exact sixteen-route successor by appending `release_version` and D572's one Release source-admission record while preserving every existing route, the selected-source freshness fields and binding reference, and every query-source admission.

## Details

The publisher loads only `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` through the existing loader. It requires exactly fifteen existing route rows and no `release_version` row. It derives the one new row and the one `release_source_admissions` record solely from the active D572@5 admission and its accepted P1622@2 frontier, including D572's complete current O164 Workflow, ordered Step/Action occurrences, and Release RMED frontier. It neither repairs nor independently admits a source.

Planning is the default and writes nothing. An explicit execute requires exact current Operator authorization and unchanged input bindings. It recomputes the existing binding and canonical manifest digests, publishes only the exact successor, and proves the published bytes by reopening them through the existing loader. The publisher does not dispatch O164, create a Release Version Run, queue work, build or retire an image, install a runtime, or claim full-release acceptance.

The publisher is non-dispatching source-projection support, not another Workflow. An execute uses the existing MCP operation and canonical Journal support for its Run and recording; the publisher does not create a parallel executor, Run writer, or Journal writer. If publication is observed but the shared recording is unavailable, it returns the actual partial state and recording requirement rather than a completed result.

The compiled Methodology source is the canonical `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/` carrier. The obsolete `.caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY` carrier is not admitted as a source or output.
