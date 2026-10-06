---
atom_id: CA-D-288
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - "Atom/Revision/Status: Draft/Filename"
  depends_on:
    continuant:
      - Atom/Identifier
version: 4
updated_at: 2026-09-04 23:37:00 +0400
relations: {}
---
# Serialize Draft Atom Filenames with an Empty Number

**every** Project-owned Draft Atom filename **must** use `<PROJECT_PREFIX>-<CONTENT_ROLE_LETTER>--` **before** its mutable components **and** **must not** carry an assigned Atom ID.
