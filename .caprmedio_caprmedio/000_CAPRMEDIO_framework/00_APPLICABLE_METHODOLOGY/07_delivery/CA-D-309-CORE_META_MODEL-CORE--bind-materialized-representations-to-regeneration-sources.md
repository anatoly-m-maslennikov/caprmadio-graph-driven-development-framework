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
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-309-CORE_META_MODEL-CORE--bind-materialized-representations-to-regeneration-sources.md
  source_atom_id: CA-D-309
  source_atom_revision: 12
  source_sha256: 08d9a70a3f6edc6ad973af0c23f47639b9fa1e299a258e068a0cf12aa18f59ee
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
