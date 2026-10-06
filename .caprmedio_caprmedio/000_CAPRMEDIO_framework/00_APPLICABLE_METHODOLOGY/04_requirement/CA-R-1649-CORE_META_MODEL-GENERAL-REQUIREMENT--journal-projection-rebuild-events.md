---
subjects:
  governs: "Projection Rebuild"
  depends_on:
    - "Work Journal/Action"
    - "Projection"
    - "Journal/Record"
version: 19
updated_at: "2026-10-03 01:31:08 +0400"
relations: {}
atom_id: "CA-R-1649"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1649-CORE_META_MODEL-GENERAL-REQUIREMENT--journal-projection-rebuild-events.md
  source_atom_id: CA-R-1649
  source_atom_revision: 19
  source_sha256: e955bf3d0d5506d326d761c8372d0c9d1b1a9c0c73c3475adb5891a1e812542b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Journal Projection Rebuild Events

## Scope

Projection Rebuilds and their Work Journal Actions and terminal Events.

## Claim

**every** Projection Rebuild **must** have **`=1`** Work Journal Action whose terminal Event records the rebuild outcome.

## Details

acceptance of that Event into the Journal does **not**, by itself, make the Projection current. currentness remains subject **to** the Projection's applicable source **and** validation requirements; the accepted Event preserves the observed outcome **without** replacing those requirements.
