---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan/Backlog/Carrier"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Status"
    - "Atom Collection"
version: 4
updated_at: "2026-10-02 19:44:54 +0400"
relations: {"relates_to": ["CA-D-469", "CA-R-1542", "CA-R-1576"]}
atom_id: "CA-D-475"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-475-CORE_META_MODEL-STANDARD--serialize-the-plan-backlog-directory.md
  source_atom_id: CA-D-475
  source_atom_revision: 4
  source_sha256: ca52f96efabd9dada8b13bb3e7a7ef52f21be88988d95d1b216069854122417e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Serialize the Plan Backlog directory

## Scope

the Plan Backlog Directory and version-labeled Plan Carrier locations.

## Claim

the Plan Backlog Directory **must** be `03_plan/001_backlog`; it is a Status container, **not** a Plan Atom. a Version-labeled Plan uses the ordinary Plan Carrier grammar under CA-D-469-CORE_META_MODEL-DELIVERY--serialize-plan-carrier-stems rather than an independently identified Version Plan Collection **or** special `version-<VERSION>` container.

## Details
