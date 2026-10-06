---
atom_id: CA-D-270
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Revision/Frontmatter
  depends_on:
    continuant:
      - Atom/Revision/Version
      - Atom/Revision/Updated At
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Serialize Atom Revision Metadata in Frontmatter

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.
