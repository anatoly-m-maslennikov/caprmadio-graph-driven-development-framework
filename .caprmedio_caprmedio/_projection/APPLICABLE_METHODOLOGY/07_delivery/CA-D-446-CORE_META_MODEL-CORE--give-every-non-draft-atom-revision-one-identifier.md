---
subjects:
  governs: "Atom/Revision/Identifier"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Version"
    - "Atom/Revision/Status: Draft"
version: 6
updated_at: "2026-10-02 19:44:54 +0400"
relations:
  relates_to:
    - CA-D-378
    - CA-D-292
atom_id: "CA-D-446"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-446-CORE_META_MODEL-CORE--give-every-non-draft-atom-revision-one-identifier.md
  source_atom_id: CA-D-446
  source_atom_revision: 6
  source_sha256: 6d956e10812bb5bbf9b5a671c58ce2639a26832e364a0446360a5514dbebb7e0
  original_relations_sha256: b17be253479843ef6dd3db281ba4b0df0d9ef1c54b95463e807c1b4fdfc085bd
---
# Summary

Give Every Non-Draft Atom Revision One Identifier

## Scope

non-Draft Atom Revisions and Draft Carriers.

## Claim

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.

- carry the assigned Atom Identity as the top-level String `atom_id` **and** Version as `version`; their pair identifies this Revision **without** another `identifier` field.
- a Draft Carrier **must not** carry an assigned `atom_id`; a filename, path, **or** temporary locator **must not** silently allocate one.

## Details
