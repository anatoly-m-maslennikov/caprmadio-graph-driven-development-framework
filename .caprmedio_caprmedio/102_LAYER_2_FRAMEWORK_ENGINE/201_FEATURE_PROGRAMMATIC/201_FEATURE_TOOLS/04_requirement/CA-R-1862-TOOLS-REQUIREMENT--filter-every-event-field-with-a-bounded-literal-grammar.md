---
atom_id: CA-R-1862
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
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/filter"
  depends_on: [Event, Tool]
relations:
  relates_to: [CA-R-1850, CA-O-162, CA-M-335, CA-E-575]
---
# Summary

Map canonical Event fields to the shared query filter

## Scope

The Journal-specific selector namespace for QUERY_FILTER.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** expose every canonical Event field as a valid selector to CA-R-1850's shared QUERY_FILTER contract.

## Details

The namespace is the top-level canonical Event object plus dot-qualified object
fields. The Tool retains this selector mapping only; equality, inequality, NOT,
IN, boolean precedence, missing/null, and type semantics are exactly CA-R-1850.
