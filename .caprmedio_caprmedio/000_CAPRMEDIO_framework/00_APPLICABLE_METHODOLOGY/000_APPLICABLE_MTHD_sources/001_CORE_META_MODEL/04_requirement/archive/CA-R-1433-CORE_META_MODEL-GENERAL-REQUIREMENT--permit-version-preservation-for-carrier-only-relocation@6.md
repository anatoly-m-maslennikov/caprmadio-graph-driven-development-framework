---
subjects:
  governs: "Atom/Revision/Version"
  depends_on:
    - "Atom"
    - "Artifact/Revision"
    - "Carrier-Only Recoding"
version: 6
updated_at: "2026-09-10 06:39:08 +0400"
relations: {}
atom_id: "CA-R-1433"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
type: "Requirement"
---
# Permit Version preservation for carrier-only relocation

a carrier-only move **or** rename of an Atom Carrier **may** preserve the current Version **only** **when** it does **not** change the Carrier's content **and** preserves Atom identity, Claim, Claim Scope, Atom Scope, **and** authored direct semantic relations under CA-D-304; a same-ID content change **must** create a new Revision under CA-R-1371.
