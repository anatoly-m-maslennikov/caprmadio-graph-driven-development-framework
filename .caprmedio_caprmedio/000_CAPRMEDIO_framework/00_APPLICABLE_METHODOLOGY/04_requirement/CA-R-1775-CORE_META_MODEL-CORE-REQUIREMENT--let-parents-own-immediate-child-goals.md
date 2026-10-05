---
version: 16
updated_at: "2026-10-03 03:43:56 +0400"
relations:
  child_of:
    - CA-M-001
subjects:
  governs: "Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    - "Scope Unit"
    - "Atom"
    - "Owned Atoms"
    - "Targeting Atoms"

atom_id: "CA-R-1775"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CA-R-1775-CORE_META_MODEL-CORE-REQUIREMENT--let-parents-own-immediate-child-goals.md
  source_atom_id: CA-R-1775
  source_atom_revision: 16
  source_sha256: cff47475dc22afd5423709d4c31cbdf4bcd91e5cb639260fa0a04c41497e7510
  original_relations_sha256: 2f95e55e3d0a844c858c40eeab601ef29e88bfb9f5c8b9fd17a85ccd2af662a7
---
# Summary

Let Parents Own Immediate Child Goals

## Scope

parent Scope Units and their immediate child Scope Units.

## Claim

**every** parent Scope Unit **must** own the Goal Atoms for its immediate child Scope Units under CA-R-926; those Goal Atoms belong **to** the parent's Owned Atoms **and** the child's Targeting Atoms **without** transferring their ownership.

## Details
