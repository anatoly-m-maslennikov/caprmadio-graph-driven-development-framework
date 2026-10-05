---
subjects:
  governs: "Atom/Content Role: Operations"
  depends_on:
    - "Action"
    - "Workflow"
    - "Methodology"
    - "Methodology Source"
    - "Scope Unit"
    - "Tool"
    - "Core Meta-Model"
    - "Extension"
    - "Project Configuration"
    - "Atom/Content Role: Implementation"
version: 5
updated_at: "2026-10-02 23:59:06 +0400"
relations:
  relates_to: [CA-M-002, CA-R-1530, CA-R-1222]
atom_id: "CA-R-1515"
content_role: "Requirement"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1515-PROJECT_CONFIGURATION-GENERAL-REQUIREMENT--keep-canonical-actions-and-workflows-in-methodology.md
  source_atom_id: CA-R-1515
  source_atom_revision: 5
  source_sha256: 198406a9363d62164bdf9bd7edb52448a74c95dbd8aebaa89acc79f84fafe950
  original_relations_sha256: de61e7999cee53d072b99dfe97e51bb9b3051fc8ae35683a243a90c39dd7c0d8
---
# Summary

Keep canonical Actions and Workflows in methodology

## Scope

the canonical O definitions of Actions and Workflows used by TOOLS in the caprmedio Project.

## Claim

**in** the caprmedio Project, the canonical O definitions of Actions **and** Workflows used by TOOLS **must** belong **to** methodology source Scope Units.

## Details

- a Tool references the applicable canonical definition rather than independently defining the same Action **or** Workflow **in** its own Scope Unit.
- the owning methodology source **may** be Core Meta-Model, an admitted Extension, **or** Project Configuration according **to** the definition's actual applicability; this allocation rule does **not** make project-specific behavior universal Core authority.
- Implementation code **and** prompts **may** realize the definition **without** becoming another independently maintained operational definition.
