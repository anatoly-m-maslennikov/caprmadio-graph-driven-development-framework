---
atom_id: CA-C-306
content_role: Concern
type: Problem
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: resolved
subjects:
  governs: "Harvest execution integrity"
  depends_on:
    - "Project"
    - "Operations"
version: 1
updated_at: "2026-10-04 11:51:00 +0400"
relations:
  concerns:
    - CA-P-1118
---
# Summary

Retain the Agent capacity limit without skipping harvest

## Concern

The third fresh harvest Agent could not be spawned because the available Agent thread limit was reached.

## Evidences

Two fresh leaf Agents1269/1270 were created successfully. A third request returned agent thread limit reached; live inventory confirms root, completed1200 and two running leaves. Root will execute the independent1271 leaf as its one assigned Agent rather than report a nonexistent third worker or bypass source coverage.

## Blast radius

Dispatch capacity only. No change to Epic scope or completed-source counts; root's1271 task must retain its own firstclock/input/output/frontier and bounded estimate.
