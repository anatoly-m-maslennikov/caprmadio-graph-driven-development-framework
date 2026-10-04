---
atom_id: CA-R-1869
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
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

A valid Event selector is exactly `event:/` (only for full-Event query) or
`event:/` followed by an RFC6901 pointer; bad pointer escapes, absent paths,
and dot-qualified traversal are rejected locally. SQL, code, grammar, boolean
precedence, literal validity, and structural comparison remain exclusively
governed by CA-R-1850; this Requirement adds no second expression grammar.
