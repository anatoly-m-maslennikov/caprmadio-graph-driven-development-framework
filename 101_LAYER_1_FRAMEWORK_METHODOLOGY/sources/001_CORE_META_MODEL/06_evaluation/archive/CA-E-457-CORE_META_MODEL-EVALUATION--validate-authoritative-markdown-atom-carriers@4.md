---
atom_id: CA-E-457
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
version: 4
updated_at: "2026-09-11 20:58:34 +0400"
relations:
  evaluation_for:
    - CA-D-355
    - CA-D-356
---
# Validate Authoritative Markdown Atom Carriers

the Evaluation **must** reject an Atom Revision **if** it has other than **`=1`** authoritative Markdown Atom Carrier on the Project filesystem, its authoritative Carrier does not contain YAML Frontmatter followed by Main Content, **or** a TOML, YAML, JSON, database, **or** projected copy is treated as authoritative for that Atom Revision.
