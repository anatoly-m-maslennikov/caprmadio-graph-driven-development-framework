---
atom_id: CA-R-1015
cce_version: cce_1
cce_form: requirement
subjects:
  - subject
  - carrier-format
  - atom-boundary
version: 1
updated_at: 2026-08-23 01:44:00
relations:
  child_of:
    - CA-R-1013
    - CAPRMEDIO-GOV-REQU-308--plain-scalar-frontmatter-values
---
# Encode Subjects in Frontmatter

Every active or draft Markdown Atom carrier MUST encode its Subjects in the `subjects` frontmatter property as a non-empty YAML block sequence of lowercase kebab-case terms.
