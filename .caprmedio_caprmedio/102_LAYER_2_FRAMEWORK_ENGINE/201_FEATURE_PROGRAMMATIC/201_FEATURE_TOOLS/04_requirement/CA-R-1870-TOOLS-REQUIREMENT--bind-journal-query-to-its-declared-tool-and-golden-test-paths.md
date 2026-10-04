---
atom_id: CA-R-1870
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:30:00 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/delivery paths"
  depends_on: [Tool, Delivery, Evaluation]
relations:
  relates_to: [CA-D-555, CA-D-558]
---
# Summary

Bind Journal query to declared Tool and golden-test paths

## Scope

The query implementation location.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** be delivered only at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/` with its golden test at `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/FIND_AND_FETCH_JOURNAL_EVENTS/tests/test_find_and_fetch_journal_events.py`.

## Details

This declaration does not create the implementation or register an MCP route.
