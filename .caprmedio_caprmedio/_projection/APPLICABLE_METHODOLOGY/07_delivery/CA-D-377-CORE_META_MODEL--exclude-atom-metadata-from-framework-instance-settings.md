---
subjects:
  governs: "Framework Instance Settings/Carrier/Atom metadata exclusion"
  depends_on:
    - "Framework Instance Settings"
    - "Atom"
    - "Artifact/Revision"
version: 7
updated_at: "2026-10-02 19:27:36 +0400"
relations:
  child_of:
    - "CA-D-361"
atom_id: "CA-D-377"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-377-CORE_META_MODEL--exclude-atom-metadata-from-framework-instance-settings.md
  source_atom_id: CA-D-377
  source_atom_revision: 7
  source_sha256: 1eb64a26f700a11193563752a1d25cd1fcc715ede996b59d2cd6cb58208d2faa
  original_relations_sha256: dbd41c990ca96026d80a7c6e36e3203724208ce3569ca634233af924bbbfab2f
---
# Summary

Exclude Atom metadata from Framework Instance Settings

## Scope

Atom metadata in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must not** contain Atom Frontmatter, Atom ID, Atom Revision metadata, Atom relations, rationale, **or** provenance; its Revision binding follows CA-D-360.

## Details
