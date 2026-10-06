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
version: 1
updated_at: "2026-10-05 00:25:37 +0400"
relations: {}
---
# Summary

Centralize Project Projection Carriers

## Scope

Projection Carriers belonging to a Project.

## Claim

**all** persistent Projection Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_projection/`.

## Details

- Graphs, Applicable Methodology, **and** derived Journal views use this root **or** named subdirectories beneath it.
- Authoritative Atoms, Methodology Sources, Project Settings, **and** Project Structure retain their own authoritative locations.
- Temporary build stages **and** intermediate reports remain ephemeral; publication places the delivered Projection under this root.
