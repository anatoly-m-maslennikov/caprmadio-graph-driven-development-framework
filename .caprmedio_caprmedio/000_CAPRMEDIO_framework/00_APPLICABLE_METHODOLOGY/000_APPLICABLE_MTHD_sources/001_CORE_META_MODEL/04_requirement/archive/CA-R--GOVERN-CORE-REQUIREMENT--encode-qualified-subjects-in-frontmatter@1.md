---
subjects:
  declared:
    continuant:
      - subject-frontmatter-schema
  prerequisite:
    continuant:
      - subject-path
      - claim-subject-relation
      - subject-temporal-form
      - carrier-format
      - atom-boundary
cce_version: cce_1
cce_form: requirement
version: 1
updated_at: 2026-08-25 01:09:39
relations: {}
---
# Encode Qualified Subjects in Frontmatter

every active or draft Markdown Atom carrier must encode its Subjects under `subjects.claim_subject_relation.subject_temporal_form` as non-empty YAML block sequences of distinct Subject Paths, must use only the lowercase keys `governs`, `depends_on`, `continuant`, and `occurrent`, must encode exactly one Subject Path in each present `governs` temporal-form sequence, must omit every empty branch, and must encode each Subject Path as exact canonical Base Entity and Dependent Entity references separated by `/`.
