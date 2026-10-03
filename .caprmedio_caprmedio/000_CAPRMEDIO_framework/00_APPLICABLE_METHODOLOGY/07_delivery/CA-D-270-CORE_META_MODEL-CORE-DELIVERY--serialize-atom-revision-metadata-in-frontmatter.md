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
version: 4
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-270-CORE_META_MODEL-CORE-DELIVERY--serialize-atom-revision-metadata-in-frontmatter.md
---
# Serialize Atom Revision Metadata in Frontmatter

**every** Markdown Atom Revision Carrier **must** serialize its positive integer Version as `version` **and** its Project-time Updated At value as `updated_at` **in** YAML frontmatter.
