---
subjects:
  - development-flow
  - carrier-format
atom_id: CA-R-1083
cce_version: cce_1
cce_form: permission
version: 1
updated_at: 2026-08-23 12:52:33
relations:
  child_of:
    - CA-R-1079
    - CA-R-1081
---
# Encode explicit Task Assignee overrides

A Task Atom MAY declare top-level frontmatter property `assignee` with exactly one identified Actor to override its default Assignee, and omission MUST preserve the default Assignee.
