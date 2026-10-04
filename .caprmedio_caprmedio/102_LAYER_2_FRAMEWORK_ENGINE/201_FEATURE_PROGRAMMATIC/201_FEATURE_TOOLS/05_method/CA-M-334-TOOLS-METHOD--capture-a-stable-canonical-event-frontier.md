---
atom_id: CA-M-334
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 01:20:00 +0400"
subjects:
  governs: "FIND_AND_FETCH_JOURNAL_EVENTS/source snapshot"
  depends_on: [Journal, Event, Tool]
relations:
  method_for: [CA-R-1861, CA-R-1866]
---
# Summary

Capture a stable canonical Event frontier

## Scope

Source snapshot construction.

## Claim

To capture the query source, the adapter **must**, before any workflow/action-start
recording or Action dispatch, read and seal the canonical Journal byte-prefix,
enumerate its Event carriers once, reject raw duplicate object keys before
parsing, and seal ordered references, member byte hashes, and unique Event IDs
into one opaque snapshot token. A standalone Action captures before its own Run
evidence and consumes exactly that token.

## Details

The method enforces configured member and byte maxima, detects changed, deleted,
truncated, unreadable, duplicate-ID, or malformed members, and never silently
extends the frontier. Every continuation revalidates the original prefix and
members; later append outside the prefix remains permitted.
