---
subjects:
  governs: "Materialized Representation/Carrier"
  depends_on:
    - "Artifact/Revision"
version: 12
updated_at: "2026-10-02 19:05:39 +0400"
relations: {}
atom_id: "CA-D-309"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Bind Materialized Representations to Regeneration Sources

## Scope

admitted materialized representation Carriers.

## Claim

**every** admitted materialized representation Carrier **must** have a recoverable binding **to** its exact canonical source Revision **and** **`=1`** deterministic regeneration **or** reconciliation rule.

the binding **may** be recovered through the selected authoritative source frontier **and** governing derivation authority; it does **not** require source metadata **to** be embedded **in** **every** resulting Carrier. an applicable Carrier specification determines whether **and** how **any** explicit binding is serialized.

for Applicable Methodology projected Atom Carriers, CA-D-305 requires an explicit one-way binding **to** the original source Atom Carrier while preserving its authored content, identity, **and** Revision. that specific binding **must not** create duplicate source authority **or** impose a blanket persisted source frontier on other Projections contrary **to** CA-R-1494.

## Details
