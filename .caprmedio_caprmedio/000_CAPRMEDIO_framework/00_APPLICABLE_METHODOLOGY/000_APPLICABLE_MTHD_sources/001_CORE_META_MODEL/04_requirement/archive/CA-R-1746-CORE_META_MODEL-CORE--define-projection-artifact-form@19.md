---
subjects:
  governs: "Projection"
  depends_on:
    - "Artifact"
    - "Artifact/Revision"
    - "Atom"
    - "Atom/Claim"
    - "Scope Unit"
    - "Structural Entity"
    - "Project Structure"
    - "Journal"
    - "Single Source of Truth"
version: 19
updated_at: "2026-10-03 02:55:14 +0400"
relations: {}
atom_id: "CA-R-1746"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Projection Artifact form

## Scope

Projection Artifacts and the authoritative sources represented in their derived views.

## Claim

a Projection **means** a non-authoritative generated view reproducibly derived from its declared selection of authoritative sources **or** other Projections. source authority follows Single Source of Truth under CA-R-1470: Atoms carry governing Claims, Project Structure owns declared Scope Unit facts, Structural Entity Carriers supply materialization observations, **and** Journals preserve recorded historical facts; other admitted source kinds retain the authority established for their facts by applicable governing Claims.

**every** represented fact retains traceability through **any** upstream Projections **to** its appropriate authoritative sources. a Projection's source specification governs the Projection's required behavior **without** making its derived contents authoritative. multiple Projections of the same source facts, further derived views, **and** the choice of generation mechanism do **not** create another independent authority for those facts.

the declared selection identifies the sources actually used; it does **not** require **every** Projection **to** consume **every** source kind.

## Details
