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
version: 2
updated_at: "2026-10-04 12:27:44 +0400"
relations:
  concerns:
    - CA-P-1271
    - CA-P-1288
---
# Summary

Split oversized harvest transports before reading

## Concern

Two P1271 transport attempts exceeded the output limit: the first combined Plan/parent/binding/evidence JSON; the second still combined too much binding metadata and native text.

## Evidences

The first was rejected at JSON parse because the truncation warning replaced the complete JSON; the second was rejected explicitly on original_token_count. Neither became read or saved semantic evidence. Separate complete binding/context and two24-record halves then parsed/read fully, with every raw/hash/text/part checked. A989 preserves all48whole records andsevencompletecontexts.

## Blast radius

P1288's next-binding transport also exceeded its initial output limit. It was rejected before parsing, read accounting or saving. Repeating the read-only binding with sufficient output capacity returned the complete object, verified against native bytes; no truncated message was counted.

Temporary read transport only. No native or carrier data deleted, no truncated text counted, no new framework implementation.
