---
atom_id: CA-C-463
content_role: Concern
type: Question
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 05:49:29 +0000"
subjects:
  governs: "Which carriers belong in a complete Release package"
  depends_on: [Tool, Manifest, Evaluation, Runtime]
relations:
  concern_about: [CA-P-1689]
---
# Summary

Which carriers belong in a complete Release package

## Concern

The current Engine inventory includes .caprmedio_tmp test receipt files, treating transient state as distributable source. Choose all persistent declared Framework resources, excluding known ephemeral caches, temporary state and .DS_Store, and refusing secret-named carriers before any byte read. Alternatives were include every physical file or maintain a second hand-authored inventory. The selected shared classifier at89% confidence preserves complete source/package ownership without transient or credential delivery and avoids duplicate collectors. P1689 implements and verifies that choice; no secret file is read to test it.

## Evidences

Live Engine .caprmedio_tmp contains two disposable receipts; both current inventory collectors recursively select all regular files.

## Blast radius

Release inventory only, not canonical authoring authority or historical Journal relocation.
