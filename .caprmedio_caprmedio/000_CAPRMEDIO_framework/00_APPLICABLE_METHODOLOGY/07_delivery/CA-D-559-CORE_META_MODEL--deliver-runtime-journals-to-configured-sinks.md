---
atom_id: CA-D-559
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Runtime Journal/Carrier"
  depends_on: [Implementation, Projection, Journal, Carrier]
version: 1
updated_at: 2026-10-04 22:33:01
relations: {relates_to: [CA-R-1745, CA-R-1720, CA-D-549, CA-D-504]}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-559-CORE_META_MODEL--deliver-runtime-journals-to-configured-sinks.md
  source_atom_id: CA-D-559
  source_atom_revision: 1
  source_sha256: a0efc0dc67bbac626021e6137567d953f20314e8102c926099f8e4f2d71fd7fa
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Deliver runtime Journals to configured sinks

## Scope

technical and business runtime Journal Carriers.

## Claim

runtime technical **and** business Journals **may** be delivered **to** an explicitly configured local database, remote database, **or** governed logging sink. these Carriers **need not** reside under `.caprmedio_<project_name>/_journal/` **or** `.caprmedio_runtime/`.

## Details

Journal classification and recorded-history authority are independent of storage technology. The configuration identifies the intended sink; applicable production logging policy remains in force. The shared Project-control Work Journal and persistent view Projections retain their separate _journal and _projection locations. Runtime cleanup and sink migration must preserve accepted Journal history; this Delivery does not authorize history deletion or change retention policy.
