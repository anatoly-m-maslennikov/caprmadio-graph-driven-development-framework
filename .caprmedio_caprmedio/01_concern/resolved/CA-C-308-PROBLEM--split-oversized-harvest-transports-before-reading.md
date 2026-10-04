---
atom_id: CA-C-308
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest transport integrity"
  depends_on:
    - "Project"
version: 1
updated_at: "2026-10-04 11:59:15 +0400"
relations:
  concerns:
    - CA-P-1271
---
# Summary

Split oversized harvest transports before reading

## Concern

Two P1271 transport attempts exceeded the output limit: the first combined Plan/parent/binding/evidence JSON; the second still combined too much binding metadata and native text.

## Evidences

The first was rejected at JSON parse because the truncation warning replaced the complete JSON; the second was rejected explicitly on original_token_count. Neither became read or saved semantic evidence. Separate complete binding/context and two24-record halves then parsed/read fully, with every raw/hash/text/part checked. A989 preserves all48whole records andsevencompletecontexts.

## Blast radius

Temporary read transport only. No native or carrier data deleted, no truncated text counted, no new framework implementation.
