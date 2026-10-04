---
atom_id: CA-C-438
content_role: Concern
type: Conflict
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: resolved
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 01:45:00 +0400"
subjects:
  governs: "Journal Event selector absence semantics"
  depends_on: [Tool, Event, QUERY_FILTER]
relations:
  concern_about: [CA-R-1850, CA-R-1869, CA-E-575, CA-P-1533]
---
# Summary

Align missing Event field filter semantics

## Concern

CA-R-1869 version 2 rejected an absent Event pointer locally, conflicting with
CA-R-1850's shared comparison rule that an absent selector compares false and
that explicit `null` remains a value.

## Resolution

CA-R-1869 version 3 limits local rejection to selector namespace, RFC6901
escaping or syntax, and dot-qualified traversal. A syntactically valid Event
pointer absent from an individual Event now reaches CA-R-1850 unchanged.
CA-E-575 version 3 records the explicit missing-versus-null fixture. This
resolves only the source conflict; it makes no runtime implementation claim.
