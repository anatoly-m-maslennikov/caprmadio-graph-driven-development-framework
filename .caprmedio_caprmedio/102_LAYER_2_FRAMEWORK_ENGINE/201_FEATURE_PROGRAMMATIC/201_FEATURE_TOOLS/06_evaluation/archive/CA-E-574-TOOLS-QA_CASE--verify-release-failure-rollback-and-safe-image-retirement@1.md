---
atom_id: CA-E-574
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
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
