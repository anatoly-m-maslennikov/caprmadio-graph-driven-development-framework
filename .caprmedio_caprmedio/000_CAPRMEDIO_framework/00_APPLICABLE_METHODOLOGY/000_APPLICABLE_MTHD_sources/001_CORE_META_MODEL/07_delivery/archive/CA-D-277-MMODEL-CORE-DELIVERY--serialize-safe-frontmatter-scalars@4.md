---
atom_id: CA-D-277
cce_version: cce_1
cce_form: serialization
subjects:
  governs:
    continuant:
      - Markdown Atom Carrier/YAML Frontmatter/Scalar
  depends_on:
    continuant:
      - Markdown Atom Carrier/Main Content
version: 4
updated_at: 2026-09-04 03:36:02 +0400
relations: {}
---
# Serialize Safe Frontmatter Scalars

the YAML Frontmatter of a Markdown Atom Carrier **must** serialize registered YAML-safe controlled string values as plain scalars **and** **must** place uncontrolled human prose **in** Main Content.
