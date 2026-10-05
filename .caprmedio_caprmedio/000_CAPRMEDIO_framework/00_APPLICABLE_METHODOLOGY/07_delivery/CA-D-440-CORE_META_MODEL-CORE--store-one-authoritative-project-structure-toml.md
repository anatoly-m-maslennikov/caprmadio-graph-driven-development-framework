---
subjects:
  governs: "Project Structure"
  depends_on:
    - "Project Settings"
    - "Carrier"
    - "Scope Unit"
version: 5
updated_at: "2026-10-02 19:36:21 +0400"
relations:
  relates_to:
    - "CA-R-1483"
    - "CA-R-862"
atom_id: "CA-D-440"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-440-CORE_META_MODEL-CORE--store-one-authoritative-project-structure-toml.md
  source_atom_id: CA-D-440
  source_atom_revision: 5
  source_sha256: 589da503b1318f4e7150f1499b7ae6636a364f1b28101f542798f07cdf213569
  original_relations_sha256: 966790aed439082bc112a837c866f12d7b99b17679663bf5b164a38efeab0818
---
# Summary

Store one authoritative Project Structure TOML

## Scope

the authoritative Project Structure Carrier.

## Claim

the authoritative Project Structure Carrier **must** be **`=1`** UTF-8 TOML file named `project_structure.toml` directly inside the owning `.caprmedio_<project_name>/` directory. `<project_name>` resolves from the owning Project Settings. this non-Atom Carrier **must not** carry an Atom ID, Atom Content Role, Atom Frontmatter, **or** non-authoritative Projection metadata. concrete unit paths belong **only** **to** this file, while Delivery Atoms retain general Carrier schema **and** representation authority.

## Details
