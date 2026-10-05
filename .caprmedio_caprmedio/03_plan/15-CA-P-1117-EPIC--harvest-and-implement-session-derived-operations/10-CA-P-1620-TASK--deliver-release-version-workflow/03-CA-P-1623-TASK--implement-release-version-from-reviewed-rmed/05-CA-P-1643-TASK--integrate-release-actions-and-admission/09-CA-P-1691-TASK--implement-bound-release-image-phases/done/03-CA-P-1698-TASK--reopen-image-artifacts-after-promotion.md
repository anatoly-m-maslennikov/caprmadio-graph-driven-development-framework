---
atom_id: CA-P-1698
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
subjects:
  governs: "Reopen image artifacts after promotion"
  depends_on: [Tool, Image, Manifest, Runtime, Evaluation]
version: 1
updated_at: "2026-10-05 06:56:25 +0000"
relations:
  is_decomposition_of: [CA-P-1691]
  blocks: [CA-P-1693, CA-P-1697]
---
# Summary

Reopen image artifacts after promotion

## Objective

Within <=10 minutes, expose the selector-independent retained image-artifact verifier needed after promotion.

## Details

Own only release_image.py and its focused tests. Factor exact receipt/context/command/output/immutable-ID/canary proof below the pre-promotion current-N gate. Initial image admission still requires current N and the full suite; post-promotion consumers independently prove current N+1 and call the artifact verifier without replaying old-N selection. Reject test-double, changed or mismatched evidence; no caller post_promoted flag or image/promotion verifier cycle. No actual Docker effect, source/Plan/Git changes or C449 workaround. Coordinate P1693's concrete reader call; preserve all other changes.

## Definition of Done

Focused pre/post-selector, tamper and test-double refusal cases pass with exact hashes, without weakening initial image admission.

### Current completed result

release_image.py `c437eef1a88ef1f3c9ab2ae930d59feacd5ee68622482aff7d753a9d5919327e`; tests `238c74e7fa178da2696b949478b4e8f264e3868b8589b8edd126ff201bd9b303`. Twenty-five focused cases passed in the designated development worker, including pre/post-selection reads and tampered, rehashed, forged and test-double refusals. The retained-artifact reader does not read the current selector or invoke Docker; initial admission still requires current N and the bound full suite. All image command output was mocked. P1693 must independently validate current candidate/source/package/selection/Skill/intent before consuming this reader. No actual image or Release execution is proven.
