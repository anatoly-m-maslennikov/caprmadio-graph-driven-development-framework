---
atom_id: CA-C-519
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: resolved
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 23:11:27 +0000"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Terminal recording recovery"
  depends_on: [Tool, Action Run, Journal, Framework Package, Docker Image, Operator]
relations:
  concern_about: [CA-P-1826, CA-R-1897, CA-M-353, CA-E-596, CA-D-591]
---
# Summary

Record a verified restoration after terminal validation failure

## Concern

How should the already verified restoration receive its canonical terminal when duplicate proof-path references were rejected before a pending Event was sealed?

## Evidences

- Fresh Run `direct-action:73f4a7a3303e0ddc63a3ff340f5d40c19040f522f8d93eeba97c73c7e54dcbdb` has canonical started evidence. Actual build, immutable-image inspection and the complete package/MCP canary passed.
- The unchanged retained package is selected with verified image `sha256:7be9efd4dfc85db8ee1ff6b6a165e778d10aa402a5fae543ac02b822632744d9`; current selector SHA is `8d600f02633ebee76865e24c96f0297c401c4dd7d1b9bd47f793c7744a03a23b`.
- Its immutable result is restored, but attempt and canonical proof both refer to `bootstrap-image-evidence/bfeb5e5566de938f7e913b7d87c31f674e57db9d74be414744b59dc61669efc4`. That path appears twice in effect_refs; the Journal rejects duplicate references before sealing a terminal Event.
- The CLI truthfully returned recording_pending/direct-action-invalid-effects. No terminal receipt or N+1 gate is claimed.

## Selected approach

Under the Epic's authority to choose the best bounded repair and retain a Question, implement the recording-only recovery in CA-M-353/CA-D-591. Normalize validated identical path strings, preserve the raw result and started history, independently verify the actual selected image/proof, and append only the original Run's terminal. Do not rebuild, rerun the canary, publish a selector or start another Action. Keep this Question open until actual canonical recording succeeds.

## Blast radius

The baseline image works and its canonical recording is now complete. N21 remains unknown and unreplayed; all release gates remain required.

## Resolution

The explicit recording-only recovery independently revalidated the actual selected image, retained proof, package and public Skill, then recorded only the original Run's terminal `direct-action:73f4a7a3303e0ddc63a3ff340f5d40c19040f522f8d93eeba97c73c7e54dcbdb:terminal:eb106986e8467589478c479a9919206795c863c9b1af60d0560b3011b162b514`. Canonical Event digest is `731c1a575faf49d71885e636bf39e2be0af48b0383fd3e2954e2685e43c62a17`, appended at line 4 of `_journal/anatoly-m-2026-10-07-part-1.ndjson`. The raw result SHA `c7f9f9382e59dd17a31c8d09b0cc4ab0a604967b4a5c3520ecd206fd0adaaa23` and selected selector SHA `8d600f02633ebee76865e24c96f0297c401c4dd7d1b9bd47f793c7744a03a23b` remain unchanged. No build, canary, selector publication or new Action start occurred during recording recovery.
