---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Assignee/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "File Carrier"
version: 4
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-R-1584", "CA-R-1585"]}
atom_id: "CA-D-473"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-473-CORE_META_MODEL-STANDARD--serialize-explicit-plan-assignees.md
  source_atom_id: CA-D-473
  source_atom_revision: 4
  source_sha256: 455da0a987be070e4f4c2a2034c2fcebef3d1eeeb3d3576b3d248fbab4897fab
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize explicit Plan Assignees

## Scope

explicit Plan Assignee overrides in Plan File Carriers.

## Claim

a Plan File Carrier **may** serialize **`=1`** explicit Assignee override as top-level frontmatter `assignee`; omission **must** preserve CA-R-1585-CORE_META_MODEL-GENERAL-REQUIREMENT--default-plan-work-assignment-to-an-ai-agent for its own work rather than copying the default.

## Details
