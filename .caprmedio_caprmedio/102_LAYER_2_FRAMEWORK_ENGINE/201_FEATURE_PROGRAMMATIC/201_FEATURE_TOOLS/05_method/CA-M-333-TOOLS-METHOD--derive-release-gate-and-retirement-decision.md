---
atom_id: CA-M-333
content_role: Method
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 06:21:05 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Gate construction"
  depends_on: [Tool, Manifest, Evaluation, Image, Journal]
relations:
  method_for: [CA-R-1879, CA-R-1880]
---
# Summary

Derive the Release Version gate and retirement decision

## Scope

Construction of the exact promotion, rollback, and old-image-retirement predicates.

## Claim

The Tool derives promotion only from matching sealed candidate evidence in the required order: compilation, declared full suite, separately retained complete runtime package, no-hook Skill delivery, and actual candidate image; it derives old-image retirement only from the exact verified prior image identity and unused/rollback-free evidence.

## Details

Missing, stale, partial, mismatched, or recording-uncertain evidence yields a blocked or pending decision. This construction neither changes a selection nor removes an image.
