---
atom_id: CA-R-1015
cce_version: cce_1
cce_form: requirement
subjects:
  declared:
    continuant:
      - subject-frontmatter-schema
  prerequisite:
    continuant:
      - subject
      - carrier-format
      - atom-boundary
version: 3
updated_at: 2026-08-23 15:21:35
relations:
  child_of:
    - CA-R-1013
    - CA-R-1091
    - CAPRMEDIO-GOV-REQU-308--plain-scalar-frontmatter-values
---
# Encode Subjects in Frontmatter

Every active or draft Markdown Atom carrier MUST encode its Subjects under subjects.claim_role.temporal_form as non-empty YAML block sequences of distinct Subject references, MUST encode exactly one value in each present declared temporal-form sequence, MUST use only lowercase keys declared, prerequisite, continuant, and occurrent, MUST omit every empty branch, and MUST encode each Subject reference as either an exact canonical governed-entity reference or a lowercase kebab-case term.
