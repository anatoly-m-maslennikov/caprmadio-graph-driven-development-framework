---
atom_id: CA-R-1869
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/filter safety"
  depends_on: [Tool, Event]
relations:
  relates_to: [CA-R-1850, CA-R-1862, CA-R-1864, CA-E-575]
---
# Summary

Reject Event selectors outside the canonical namespace

## Scope

The Journal-specific selector admission boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** reject every selector that does not resolve to one unambiguous canonical Event field before passing the expression to CA-R-1850.

## Details

SQL, code, grammar, boolean precedence, and literal validity remain exclusively
governed by CA-R-1850; this Requirement adds no second expression grammar.
