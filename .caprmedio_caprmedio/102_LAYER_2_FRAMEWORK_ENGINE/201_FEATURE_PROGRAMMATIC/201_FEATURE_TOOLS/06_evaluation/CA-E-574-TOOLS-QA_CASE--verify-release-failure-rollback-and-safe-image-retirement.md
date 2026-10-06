---
atom_id: CA-E-574
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-06 14:47:41 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Recovery QA"
  depends_on: [Tool, Runtime, Image, Journal, Workflow Run, Action Run]
relations:
  evaluation_for: [CA-R-1880, CA-M-333]
---
# Summary

Verify release failure, rollback, and safe image retirement

## Scope

Failure after candidate effects, recording uncertainty, and eventual exact old-image retirement.

## Claim

The QA case **must** inject bounded install, Skill, test, image, and result-recording failures and prove preservation or restoration of N, source/settings/Journal bytes, and truthful shared Run/Action evidence; it **must** prove that only the exact verified unused old image is removed after all promotion gates pass.

## Details

Assert no effect replay after uncertain recording, no broad prune, and no removal while a container or rollback reference retains the old image. A blocked recovery remains blocked rather than being reported complete.

Add the source-copy predecessor cases. After a completed normal copy at the fixed target `101_LAYER_1_FRAMEWORK_METHODOLOGY/sources`, inject a later compiler, suite, image, recording, or promotion failure and allow the candidate to remain unpromoted. Reopen the predecessor proof and require the old frozen manifest SHA-256, expected and actual old copy SHA-256, same executing N, complete old-tree source paths with byte SHA-256 and modes, exact old-tree currentness before and after the check, and authenticated canonical Journal plus Action/Run and sealed CA-D-574 checkpoint/proof references. Presence of arbitrary old JSON, an unknown/tampered/unrecorded/unsafe proof, wrong N or identity, mode drift, or any old-tree mutation must return blocked and retain N. Separately verify that the new candidate seals and revalidates its own current source/settings/frontier/authority, performs a fresh normal copy, and requires new actual equals new expected; old and new source/frontier/settings digests need not match. No predecessor proof may authorize a new candidate, reuse output, or replay an old effect. These checks add no public request, schema, CLI, route, or graph member.
