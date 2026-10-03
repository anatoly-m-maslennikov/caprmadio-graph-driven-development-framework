---
cce_version: cce_1
cce_form: cardinality
subjects:
  governs: "Atom/Revision/Identifier"
  depends_on:
    - "Atom/Identity"
    - "Atom/Revision/Version"
    - "Atom/Revision/Status: Draft"
version: 3
updated_at: "2026-09-24 14:16:19 +0000"
relations:
  relates_to:
    - CA-D-378
    - CA-D-292
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Give Every Non-Draft Atom Revision One Identifier

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.

- carry the assigned Atom Identity as the top-level String `atom_id` **and** Version as `version`; their pair identifies this Revision **without** another `identifier` field.
- a Draft Carrier **must not** carry an assigned `atom_id`; a filename, path, **or** temporary locator **must not** silently allocate one.
