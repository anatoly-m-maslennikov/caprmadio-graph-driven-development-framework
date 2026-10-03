---
atom_id: CA-E-429
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Markdown Atom Carrier Validation
  depends_on:
    continuant:
      - Atom/Revision
      - Markdown Atom Carrier
      - Project
version: 2
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-429-CORE_META_MODEL-CORE-EVALUATION--validate-authoritative-markdown-atom-carriers.md
---
# Validate Authoritative Markdown Atom Carriers

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does not contain YAML Frontmatter followed by Main Content, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.
