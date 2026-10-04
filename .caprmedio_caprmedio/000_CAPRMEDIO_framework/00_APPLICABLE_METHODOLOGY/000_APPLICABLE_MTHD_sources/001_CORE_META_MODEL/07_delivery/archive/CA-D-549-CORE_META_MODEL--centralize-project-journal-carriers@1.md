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
version: 1
updated_at: "2026-10-05 00:25:37 +0400"
relations: {}
---
# Summary

Centralize Project Journal Carriers

## Scope

Journal Carriers belonging to a Project.

## Claim

**all** persistent Journal Carriers of a Project **must** reside under **`=1`** Directory Carrier: `.caprmedio_<project_name>/_journal/`.

## Details

- Journal segments use this root **or** its subdirectories.
- Artifact Change Log **and** Workflow Execution Log views **are** Projections, **not** separate authoritative Journals.
- Runtime locks, receipts, **and** pending-recording state remain runtime state, **not** canonical Journal Carriers.
