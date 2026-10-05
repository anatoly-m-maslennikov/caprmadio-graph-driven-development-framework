---
subjects:
  governs: "Atom/Revision/Identifier"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Version"
    - "Atom/Revision/Status: Draft"
version: 7
updated_at: "2026-10-05 07:04:56 +0400"
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
---
# Summary

Give Every Non-Draft Atom Revision One Identifier

## Scope

non-Draft Atom Revisions and Draft Carriers.

## Claim

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.

- carry the assigned Atom Identity as the top-level String `atom_id` **and** Version as `version`; their pair identifies this Revision **without** another `identifier` field.
- a Draft Carrier **must not** carry an assigned `atom_id`; a filename, path, **or** temporary locator **must not** silently allocate one.
- when an identified Atom is changed to Draft, its Draft Carrier remains a Revision of that same Atom: remove `atom_id` from the Draft Carrier's complete frontmatter **and** its assigned filename number under CA-D-288-CORE_META_MODEL-DELIVERY--serialize-draft-atom-filenames-with-an-empty-number; do **not** create another Draft Atom **or** represent the change as a replacement.
- preserve that Draft Revision's Summary, meaning, Version, **and** identified predecessor history. this rule does **not** allocate **or** reuse an Atom Identity for a later Revision leaving Draft.

## Details
