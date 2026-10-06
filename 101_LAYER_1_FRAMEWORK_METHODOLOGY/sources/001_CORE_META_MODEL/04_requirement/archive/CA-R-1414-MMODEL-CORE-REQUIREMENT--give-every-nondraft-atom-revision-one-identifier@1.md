---
atom_id: CA-R-1414
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Atom/Revision/Identifier
  depends_on:
    continuant:
      - Atom/Identity
      - Atom/Revision/Version
      - "Atom/Revision/Status: Draft"
version: 1
updated_at: 2026-09-04 23:45:00 +0400
relations: {}
---
# Give Every Non-Draft Atom Revision One Identifier

**every** non-Draft Atom Revision **must** have **`=1`** Identifier composed from its Atom Identity **and** Version.
