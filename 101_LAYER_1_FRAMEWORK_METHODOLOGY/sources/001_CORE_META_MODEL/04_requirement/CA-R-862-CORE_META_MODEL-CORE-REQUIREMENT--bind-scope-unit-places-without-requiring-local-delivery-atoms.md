---
subjects:
  governs: "Scope Unit"
  depends_on:
    - "Project Structure"
    - "Implementation Folder"
    - "Carrier"
    - "Atom/Content Role: Delivery"
version: 16
updated_at: "2026-10-02 20:52:00 +0400"
relations:
  child_of:
    - CA-R-1484
atom_id: "CA-R-862"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Bind Scope Unit Places **without** Requiring Local Delivery Atoms

## Scope

non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have its authority place **and** Implementation Folder bound by its authoritative Project Structure declaration. concrete bindings **must not** be independently maintained **in** Delivery Atoms; applicable Delivery authority governs the representation, placement, **and** general Carrier conventions rather than repeating a unit's selected paths.

## Details
