---
subjects:
  governs: "Select Reconciliation Sources"
  depends_on:
    - "Action"
    - "Projection/Type: Reconciled Projection"
    - "Artifact/Revision"
    - "Atom/Claim"
version: 5
updated_at: "2026-09-14 01:36:43 +0400"
relations: {}
atom_id: "CA-O-004"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-004-CORE_META_MODEL-ACTION--select-reconciliation-sources.md
---
# Select reconciliation sources

Select Reconciliation Sources **means** the reusable Action that resolves the complete source selection required by applicable governing authority **and** returns the exact selected source identities **and** Revisions as one source frontier. it **must** preserve source-selection constraints, include **every** eligible source, **and** retain unresolved selection ambiguity as a reported failure rather than silently choosing **or** discarding a source. selection does **not** change source authority **or** publish a Projection.
