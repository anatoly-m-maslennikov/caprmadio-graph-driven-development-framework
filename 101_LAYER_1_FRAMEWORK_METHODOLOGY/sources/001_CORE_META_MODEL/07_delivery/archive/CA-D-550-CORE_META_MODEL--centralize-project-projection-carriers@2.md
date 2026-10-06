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
