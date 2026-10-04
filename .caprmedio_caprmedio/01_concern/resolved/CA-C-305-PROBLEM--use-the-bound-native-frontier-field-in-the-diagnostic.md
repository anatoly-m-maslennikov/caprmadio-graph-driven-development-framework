---
atom_id: CA-C-305
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

Use the bound native frontier field in the diagnostic

## Concern

The P1284 provenance diagnostic used first_native instead of the bundle schema's actual first field for its final frontier assertion.

## Evidences

All preceding native snapshots/messages/parts/context, saved100dispositions, current/next binding and disjointness assertions passed before KeyError. The caller was corrected to first/path, and the exact frontier bytes passed at07:48:30Z. No binding, evidence or implementation bytes were changed. Strict127Plans/69supportingCarriers and whitespace passed; finalsavedreceipt07:48:31Z remains within the07:49:50deadline.

## Blast radius

Only this temporary diagnostic invocation. No source failure, fabricated coverage or need to implement a framework Tool.
