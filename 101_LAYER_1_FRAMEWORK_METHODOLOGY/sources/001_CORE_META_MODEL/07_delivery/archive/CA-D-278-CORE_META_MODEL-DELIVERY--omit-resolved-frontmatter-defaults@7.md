---
atom_id: CA-D-278
cce_version: cce_1
cce_form: omission
subjects:
  governs:
    continuant:
      - "Markdown Atom Carrier/YAML Frontmatter/Default"
  depends_on:
    continuant:
      - "Artifact/Property/Default"
      - "Property"
version: 7
updated_at: "2026-09-10 02:49:14 +0400"
relations: {}
---
# Omit Resolved Frontmatter Defaults

**if** a Markdown Atom Carrier Frontmatter Property's resolved value **`=`** its applicable registered default **and** omission preserves its value-selection **and** inheritance behavior, **then** a writer **must** omit that Property; a reader **must** resolve the omission from the same authority.
