---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Artifact/Revision"
    - "Journal"
    - "Carrier"
version: 5
updated_at: "2026-10-01 21:24:33 +0400"
relations:
  child_of:
    - "CA-D-440"
atom_id: "CA-D-443"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-443-CORE_META_MODEL-DELIVERY--bind-project-structure-revisions-to-source-evidence.md
---
# Summary

Bind Project Structure revisions **to** source evidence

## Scope

Project Structure Revision bindings.

## Claim

a Project Structure Revision binding **must** identify the exact authoritative TOML bytes by SHA-256 Digest **and** the completed change event **in** the canonical Event Log under applicable Journal authority. the binding **must** distinguish the selected pre-change state, resulting state, **and** actual completion **or** failure; missing **or** conflicting event evidence leaves provenance currentness unknown. the TOML Carrier **must not** duplicate Atom Revision fields **or** store its own self-referential digest. a consumer **may** parse **and** validate the selected bytes **without** claiming completed change provenance **when** that provenance is unresolved.

## Details
