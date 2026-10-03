---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "Atom"
    - "Atom/Content Role: Evaluation"
    - "Atom/Claim/Target Scope Unit"
    - "Atom/Summary"
    - "Scope Expression"
    - "Scope Unit"
version: 17
updated_at: "2026-09-25 11:32:01 +0000"
relations:
  evaluation_for:
    - CA-R-1596
    - CA-R-1270
    - CA-R-1271
    - CA-R-1624
    - CA-R-1465
    - CA-R-1273
atom_id: "CA-E-384"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation"
global_tier: 10
---
# Summary

Validate Composite Claims and Derived Summaries

## Claim

the Evaluation **must** reject an Atom **if** **any** applicable content-boundary condition fails:

- the Atom has **`!=1`** Claims, **`!=1`** resolved Claim Target Scope Units, an independently replaceable component inside **`=1`** Claim, ambiguous composite grouping, **or** a non-deterministic Scope Expression.
- Details change, contradict, broaden, narrow, **or** add an independent contribution **to** the first body block instead of expanding it under CA-R-1624.
- Summary is **not** source-faithful **to** the finalized first body block under CA-R-1465 **and** CA-R-1273, including its applicability restrictions. a Summary sourced from Analysis Results **or** TLDR instead of Question fails this check.

evaluate restrictions **to** selected sibling Scope Units under CA-E-461 separately from these rejection criteria.

## Details
