---
atom_id: CA-C-520
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 23:52:40 +0000"
subjects:
  governs: "Release Version/Source publication recovery"
  depends_on: [Workflow Run, Action Run, Methodology, Journal, Framework Package, Operator]
relations:
  concern_about: [CA-P-1620, CA-P-1823, CA-R-1878, CA-D-567]
---
# Summary

Resolve the stopped N22 source publication

## Concern

How should the stopped N22 source publication be resolved without replaying uncertain effects or weakening atomic publication and release gates?

## Evidences

- The `.DS_Store` validation fixes passed focused checks and the actual complete-package/MCP canary. The original restoration has canonical completed evidence; its raw result and selected runtime are unchanged after recording-only recovery.
- Fresh MCP Run `release-epic-resume-20261008-N22` was independently previewed and sealed at snapshot `5b01c267e93dff8be6e21467406170a86f19be67446a7bebadc9ecaf5a5955d0`. Freeze and validation completed. Its source-delivery phase returned `blocked`, reason `phase stopped: release-copy-failed`; no Unit or later release gate ran.
- The exact Action result is `.caprmedio_install/workflow_orchestrator/runs/release-epic-resume-20261008-N22/release-epic-resume-20261008-N22:step:3:action:1.json`. Retained paths are `101_LAYER_1_FRAMEWORK_METHODOLOGY/.release-sources-5b01c267e93d-jxs3217k`, `.release-sources-prior-zc2rtmuu` and the unchanged prior `sources` directory. The new predecessor reservation is still empty. The implementation removes that empty reservation immediately before renaming the old tree; retained state points to that pre-publication boundary, but the stored result does not expose the underlying OS error.
- The native effect outcome is absent. Canonical interrupted-pending receipts, not release success, were saved for the Action, Step and Workflow. Workflow interruption Event is `event-b3a25dda-a8c2-4c14-a443-10070bdd9aac`, digest `00e755906c8d233c59e799dbd56761cd48202bf0bf010506f97fb6b63a292287`. Scheduler `SUCCESS` means its function returned, not that release passed.

## Selected approach

Retain the original N22 result, sealed request, staging trees and canonical interrupted history. Do not replay N22, promote its candidate or waive gates. Resolve the source-publication failure under its existing ownership and atomic-publication contract before admitting any fresh release; do not infer an unavailable OS error or relabel the interrupted effect as passed. The complete status response is saved at `.caprmedio_tmp/epic-resume-release/N22/selected-status-result.json`.

## Subsequent evidence

- P1827 completed the prospective retained-wrapper/absent-child refinement under M332@4 and D567@6. Thirty delivery fixtures passed in isolated Linux, including actual atomic publication and rollback; D572@27 passed fourteen source-admission checks and its exact binding refresh was journaled. This removes unnecessary empty-reservation deletion, not the required atomic moves.
- A fresh host fixture attempt observed actual `PermissionError: [Errno 1] Operation not permitted` at staging-to-`sources` directory rename before the new replacement assertion. This confirms a current host atomic-directory publication restriction; it does not supply the absent original N22 errno. No host permission bypass or incremental-publication fallback was used.
- Docker is accessible and the selected immutable baseline image remains present. The separate image/initialization Linux diagnostic failed at fixture setup because the engine-only snapshot omitted `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`; those seventy-nine cases remain non-passing until exact source-admitted fixture inputs are supplied.
- MCP was reloaded after the successful binding refresh, and CA-O-164 is currently bound to `release_version`. N22 still reports canonical interrupted-pending Action, Step and Workflow outcomes. No fresh N23 is queued and no Unit, E2E, Full Gate or promotion is inferred from the focused fixture results.

## Blast radius

The selected working N package/image and project-local Skill remain available. N22 did not reach compilation or tests; complete Linux Unit and subsequent release/closure acceptance remain outstanding. Temporary-directory cleanup is waived, not required publication or proof.
