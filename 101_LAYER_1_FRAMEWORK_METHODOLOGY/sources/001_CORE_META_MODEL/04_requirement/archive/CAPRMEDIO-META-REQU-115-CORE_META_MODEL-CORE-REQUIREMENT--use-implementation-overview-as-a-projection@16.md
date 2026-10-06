---
subjects:
  governs: "Projection/Type: Implementation Overview"
  depends_on:
    - "Projection"
    - "Atom"
    - "Artifact/Revision"
    - "Implementation Binding"
    - "Journal"
    - "Implementation"
    - "Verification"
    - "Atom/Content Role"
version: 16
updated_at: "2026-09-15 05:51:38"
relations: {}
atom_id: "CAPRMEDIO-META-REQU-115"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
global_tier: 9
---
# Use Implementation Overview as a Projection

an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CAPRMEDIO-META-REQU-105; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.

it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.

the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.

## Primary claim

CAPRMEDIO represents the current view of project realization through an Implementation Overview Projection rather than an Implementation Atom.
