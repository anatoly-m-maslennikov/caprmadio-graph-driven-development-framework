---
subjects:
  governs: "Journal"
  depends_on:
    - "Artifact"
    - "Journal/Record"
    - "Atom/Claim"
version: 17
updated_at: "2026-10-04 22:04:35 +0000"
relations: {}
atom_id: "CA-R-1745"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1745-CORE_META_MODEL-CORE--define-journal-artifact-form.md
  source_atom_id: CA-R-1745
  source_atom_revision: 17
  source_sha256: 0b7947c66a02af2ea3cf77a3d23b5b3a8b450e98742e2c67c4ab8a8291097d90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Journal Artifact form

## Scope

Journal Artifacts and their recorded histories, including technical and business runtime logs.

## Claim

a Journal, also called an Event Log, **means** an authoritative Artifact whose recorded history forms **`=1`** logically ordered table of admitted records about events. technical **and** business runtime logs **are** Journals. a record describes an event **and** its recorded evidence; the record is **not** the event itself **or** automatic proof of its asserted outcome. accepted records **must not** be edited, reordered, **or** removed; corrections append new traceable records **without** rewriting accepted history. Journal authority concerns recorded history **and** does **not** independently redefine governing Atom Claims.

## Details

Journal is a logical Artifact classification, not a required storage technology or directory. Its Carrier may be files, a local database, a remote database, or a governed logging sink according to applicable Delivery and configuration. Project-control Journal files use the registered _journal directory; runtime log classification does not force every runtime sink into that directory. Views and queries of a Journal remain Projections.
