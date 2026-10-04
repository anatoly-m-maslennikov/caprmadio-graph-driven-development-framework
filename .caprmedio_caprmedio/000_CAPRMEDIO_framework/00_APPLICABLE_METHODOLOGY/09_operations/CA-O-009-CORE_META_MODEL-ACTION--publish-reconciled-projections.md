---
subjects:
  governs: "Publish Reconciled Projection"
  depends_on:
    - "Action"
    - "Projection/Type: Reconciled Projection"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Carrier"
    - "Atom/Content Role: Delivery"
version: 5
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
atom_id: "CA-O-009"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-009-CORE_META_MODEL-ACTION--publish-reconciled-projections.md
---
# Publish reconciled projections

Publish Reconciled Projection **means** the reusable Action that publishes a Reconciled Projection from the exact final selected source Revisions **only** **when** the applicable required checks are complete, no conflict remains unresolved under those checks, **and** required resolution approvals remain valid for that frontier. **before** changing live output, it **must** recheck that the exact current selected sources match the assessed frontier **and** required approval bindings; unresolved **or** indeterminate checks **or** a changed frontier block publication **without** changing that output. it **must** preserve the selected source content, identities, **and** Revisions **without** Claim synthesis **or** merge **and** use the applicable Delivery authority for representation, source traceability, **and** publication. failure **must** be reported **without** claiming a completed publication; prior published state **and** recovery remain governed by applicable authority. the Action does **not** fix source conflicts by editing the result **or** gain source authority through publication.
