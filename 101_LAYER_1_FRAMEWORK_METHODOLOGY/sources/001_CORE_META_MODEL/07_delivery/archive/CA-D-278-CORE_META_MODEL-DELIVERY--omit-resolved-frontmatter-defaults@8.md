---
atom_id: CA-D-278
cce_version: cce_1
cce_form: omission
subjects:
  governs: "Markdown Atom Carrier/YAML Frontmatter/Default"
  depends_on:
    - "Artifact/Property/Default"
    - "Property"
version: 8
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Omit Resolved Frontmatter Defaults

**if** a Markdown Atom Carrier Frontmatter Property's resolved value **`=`** its applicable registered default **and** omission preserves its value-selection **and** inheritance behavior, **then** a writer **must** omit that Property; a reader **must** resolve the omission from the same authority.
