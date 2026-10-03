---
subjects:
  governs: "Project Configuration"
  depends_on:
    - "Project"
    - "Extension"
    - "Framework Instance Settings"
version: 13
updated_at: "2026-09-11 23:47:49 +0400"
relations: {}
atom_id: "CA-R-1207"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Separate Project Configuration Rules from Current Settings

the Project Configuration **must** own Project-specific expansion rules, constraints, **and** defaults **only** **where** the Core Meta-Model permits expansion; current Extension activation **and** selected Extension revisions **must** remain owned by the Framework Instance Settings Artifact, **not** duplicated **in** Project Configuration Atoms.
