---
subjects:
  governs: "Atom/Content Role: Plan/Carrier Placement"
  depends_on:
    - "Atom/Content Role: Plan/Status"
    - "Atom/Content Role: Plan/Authoritative Carrier Bundle"
version: 6
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-R-1539", "CA-D-483", "CA-R-1541"]}
atom_id: "CA-D-461"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-461-CORE_META_MODEL-CORE--place-plan-carriers-by-status.md
  source_atom_id: CA-D-461
  source_atom_revision: 6
  source_sha256: e0135ae3093130e3a40f091882d53942f42c83ec5302788a8f4bc718bcf83390
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Plan Carriers by Status

## Scope

Plan Carrier Bundle placement by carried Status.

## Claim

**every** Plan Carrier Bundle **must** represent its carried Status **in** its local Plan container under the following mapping:

- Active: directly **in** that local container.
- Backlog: **in** its `001_backlog` subdirectory.
- Done: **in** its `done` subdirectory.
- Canceled: **in** its `canceled` subdirectory.
- Archived: **in** its `archived` subdirectory.

the local container is the matching Directory Carrier of its declared immediate decomposition target **when** that folder is used, **or** the owning Scope Unit's `03_plan`. reserved Status directories are **not** Plan nodes. validate folder nesting under CA-D-481; placement does **not** declare decomposition.

read Status from the Plan's own Markdown file under CA-D-483 **and** check its local placement. moving a Hub **must not** silently change descendant Status; a cascade requires an explicit authorized change for **every** affected Plan.

## Details
