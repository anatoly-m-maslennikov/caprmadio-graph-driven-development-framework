---
atom_id: CA-D-269
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Atom/Subjects/Frontmatter
  depends_on:
    continuant:
      - Subject/Relation Kind
      - Subject/Temporal Form
      - Subject Path
version: 5
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/07_delivery/CA-D-269-CORE_META_MODEL-CORE-DELIVERY--serialize-atom-subjects-in-frontmatter.md
---
# Serialize Atom Subjects in Frontmatter

**every** Markdown Atom Carrier **must** serialize **every** Subject as one Subject Path **in** `subjects.<governs|depends_on>.<continuant|occurrent>` so the mapping keys encode **`=1`** Relation Kind **and** **`=1`** Temporal Form **and** the list item encodes **`=1`** Entity reference.
