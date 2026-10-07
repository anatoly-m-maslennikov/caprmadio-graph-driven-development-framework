---
atom_id: CA-C-518
content_role: Concern
type: Question
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 22:25:26 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Retained-package Image Restoration"
  depends_on: [Operator, Framework Package, Docker Image, Carrier, Journal, Action]
relations:
  concern_about: [CA-P-1820, CA-R-1897, CA-M-353, CA-E-596, CA-D-591]
---
# Summary

Authorize a metadata-safe baseline image restoration retry

## Concern

May the approved restoration use a sealed, metadata-filtered Docker context transport and one separately authorized fresh attempt, while preserving the original package, proof, failed attempt, selected binding and every release gate?

## Evidences

- The real O187 Action `direct-action:58179677a5837b6f8ca48afe0a0fe79673f00d517a9d2bc0e9d131b9694e0559` recorded started before its build, then terminal outcome `partial`.
- Build and immutable-image inspection passed for `sha256:35f92e1b88a198627fd3b730aceccd4ae8d69d6ddd6c82395f1e227d8a197802`. The fixed canary failed its exact package-file inventory before reaching MCP.
- A read-only container probe found 15,141 actual files versus 15,136 expected: no missing files and five extra `.DS_Store` files. The disposable host context later had six extra metadata files. Its persistent digest still equals the authenticated original context.
- Filtering during the initial copy is insufficient when filesystem metadata can appear before Docker transfers that directory. The proposed transport must emit only authenticated persistent files; it must not weaken the canary or modify retained N.
- The selected selector remains SHA-256 `23c17beeab33e1a281c68bfbd492d6ea27b6e5e36c275744c7cb56bdc98c9fdc`. The original package and proof are unchanged. No canonical replacement proof was published.
- The completed partial attempt is retained at `.caprmedio_runtime/framework/bootstrap-image-evidence/attempt-58j0x8pk`; its result is `.caprmedio_runtime/framework_image_restoration/6a65c1ed382a36738abb58c2a6061749b532d23e95387b06b28128bf169c2365/result.json`. It must not be replayed or rewritten as successful.

## Blast radius

The missing selected image still prevents the fresh Release Unit gate and later release gates. A bounded retry requires reviewed transport/attempt authority and tests first. No change to N's package, original proof, public ca Skill, exact canary meaning, release gate coverage or historical Journal is proposed.
