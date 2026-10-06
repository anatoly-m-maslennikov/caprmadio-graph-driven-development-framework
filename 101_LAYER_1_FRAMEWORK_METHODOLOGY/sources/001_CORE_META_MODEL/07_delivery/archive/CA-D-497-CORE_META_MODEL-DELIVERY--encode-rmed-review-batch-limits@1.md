---
atom_id: CA-D-497
content_role: Delivery
type: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-09-28 16:14:59 +0400"
subjects:
  governs: "Framework Instance Settings"
  depends_on:
    - "Workflow Run"
    - "Default Settings"
    - "Operator"
relations: {"relates_to":[]}
---
# Summary

Encode RMED review batch limits

## Scope

the `rmed_review` parameter group **in** Framework Instance Settings **and** Default Settings.

## Claim

RMED review batch limits **must** use these TOML parameters:

| Parameter | Encoding |
|---|---|
| `rmed_review.max_atoms` | positive integer; maximum selected Atoms per batch |
| `rmed_review.target_minutes` | positive integer; estimated total selection, evaluation, repair, **and** recheck work per batch **in** minutes |

resolve **every** parameter independently from explicit Operator Run input, **then** Framework Instance Settings, **then** Default Settings. report the selected value **and** source; do **not** silently coerce invalid values **or** store the same default **in** prompt text as independent authority.

## Details

the time value is an estimate for planning, **not** a guaranteed deadline **or** permission **to** omit checks. an individually oversized Atom remains explicit deferred work requiring a smaller work boundary **or** an Operator-approved budget.
