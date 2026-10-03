---
subjects:
  governs: "Applicable Methodology"
  depends_on:
    - "Applicable Methodology/Conflict"
    - "Applicable Methodology/Source Frontier Digest"
    - "Operator"
    - "Journal/Record"
    - "Methodology Source/Expansion Boundary"
version: 11
updated_at: "2026-10-02 22:05:04 +0400"
relations:
  relates_to:
    - CA-O-007
    - CA-O-011
atom_id: "CA-R-1317"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Fail Closed on Unresolved Methodology Conflicts

## Scope

unresolved conflicts in Applicable Methodology **and** their required Operator approvals.

## Claim

**if** an Applicable Methodology conflict remains unresolved **or** its required Operator approval is missing, stale, partial, ambiguous, **or** mismatched, **then** compilation **must** fail **without** changing Applicable Methodology membership.

## Details

qualifying approval **must** be the Operator's actual decision recorded **in** the Journal under CA-O-007 **and** bound **to** the exact conflict **and** source-frontier digest under CA-O-011. a Project Configuration approval Atom, an LLM judgment, **or** the mere presence of a Journal record **must not** substitute for that decision **or** bypass the Core expansion boundary.
