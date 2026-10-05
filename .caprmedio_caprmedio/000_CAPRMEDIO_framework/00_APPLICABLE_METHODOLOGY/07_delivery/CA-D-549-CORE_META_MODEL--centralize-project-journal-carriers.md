---
atom_id: CA-D-549
content_role: Delivery
current_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Journal/Carrier Root"
  depends_on: ["Project","Journal","Carrier","Projection","Workflow"]
version: 2
updated_at: "2026-10-04 21:55:27 +0000"
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-549-CORE_META_MODEL--centralize-project-journal-carriers.md
  source_atom_id: CA-D-549
  source_atom_revision: 2
  source_sha256: 27fc7b533f6ad42b288d5d39d7c19ccef96591b32098ec50188dbb6d8e0a3ea4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Centralize Project Journal Carriers

## Scope

persistent File Carriers of a Project's shared Work Journal and other project-control Journals.

## Claim

**all** persistent project-control Journal File Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.

Technical and business runtime logs are Journals too, but their configured local database, remote database, or logging sink Carriers are not required to reside in this Directory Carrier. Journal classification does not impose one physical storage technology.
