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
