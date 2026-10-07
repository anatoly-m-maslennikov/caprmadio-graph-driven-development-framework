---
atom_id: CA-P-1826
content_role: Plan
type: Plan
label: Task
work_sequence_number: 6
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Done
version: 3
updated_at: "2026-10-07 23:11:27 +0000"
subjects:
  governs: "Verify and execute the authorized baseline restoration"
  depends_on: [Action, Tool, Framework Package, Docker Image, Journal, Operator]
relations:
  is_decomposition_of: [CA-P-1820]
---
# Summary

Verify and execute the authorized baseline restoration

## Objective

Independently review the assembled code against the accepted RMED/O, refresh necessary source admission, then execute the single Operator-authorized native restoration and verify its actual image/proof/selector/Journal result.

## Details

The original actual restoration ended partial because its package canary counted Finder metadata. Its exact Run, result, build/inspect observations and failed terminal remain unchanged. C518 records the Operator's explicit instruction that `.DS_Store` fail nothing, then continue. Apply CA-R-1898, review and test the metadata fix, then execute a separately authorized fresh Run referencing that known partial terminal through CA-D-591; do not replay the original Run.

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Actual immutable build/inspect/canary and canonical started/terminal receipts prove the selected unchanged N package works with the verified result. All retained identities/currentness checks pass. A new source-bound Release can be admitted; no Unit, E2E, Full Gate, promotion or Epic closure is implied.

## Completion evidence

- Independently accepted metadata and recording-only fixes passed 49 focused restoration/Session/bootstrap tests. Wider release regressions remain required under CA-P-1823.
- Actual build, immutable-image inspection and the complete 15,135-file package/MCP canary passed. The unchanged package `6f2e3a615a4f4d6da0f16831800f9e4b7ff84f89b89faeefc359f51711d28c57` is selected with verified image `sha256:7be9efd4dfc85db8ee1ff6b6a165e778d10aa402a5fae543ac02b822632744d9`.
- Original fresh Run `direct-action:73f4a7a3303e0ddc63a3ff340f5d40c19040f522f8d93eeba97c73c7e54dcbdb` now has canonical completed terminal `direct-action:73f4a7a3303e0ddc63a3ff340f5d40c19040f522f8d93eeba97c73c7e54dcbdb:terminal:eb106986e8467589478c479a9919206795c863c9b1af60d0560b3011b162b514`, Event digest `731c1a575faf49d71885e636bf39e2be0af48b0383fd3e2954e2685e43c62a17`.
- Recording recovery performed only fresh inspection and the missing terminal append. Raw restored result SHA `c7f9f9382e59dd17a31c8d09b0cc4ab0a604967b4a5c3520ecd206fd0adaaa23`, selector SHA `8d600f02633ebee76865e24c96f0297c401c4dd7d1b9bd47f793c7744a03a23b`, package/Skill and original partial history remain unchanged. The exact receipt is retained in `.caprmedio_tmp/epic-resume-release/N22/baseline-restoration-retry-result.json`.
