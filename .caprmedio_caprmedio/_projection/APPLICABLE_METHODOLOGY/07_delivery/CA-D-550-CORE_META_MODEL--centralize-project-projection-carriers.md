---
atom_id: CA-D-550
content_role: Delivery
current_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Projection/Carrier Root"
  depends_on: ["Project","Projection","Carrier","Applicable Methodology","Journal","Atom","Methodology Source","Project Settings","Project Structure"]
version: 2
updated_at: "2026-10-04 22:09:37 +0000"
relations: {}
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-550-CORE_META_MODEL--centralize-project-projection-carriers.md
  source_atom_id: CA-D-550
  source_atom_revision: 2
  source_sha256: 1594d7a92f03d382d46756ee90d2d5b798b7c9b3acad374f3fb9c4e854f761ef
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Centralize Project Projection Carriers

## Scope

persistent non-authoritative view Projection Carriers belonging to a Project.

## Claim

**all** persistent view Projection Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_projection/`.

## Details

- Graphs, Applicable Methodology, and derived Journal views use this root or named subdirectories beneath it.
- Authoritative Atoms, Methodology Sources, Project Settings, and Project Structure retain their own authoritative locations.
- Temporary build stages and intermediate reports remain ephemeral; publication places the delivered view Projection under this root.
- The derivation RMED → using O → I does not relocate native Implementation into _projection: native I uses its governed Delivery place and may supply actual-state source facts. Views subsequently generated from I use _projection.
