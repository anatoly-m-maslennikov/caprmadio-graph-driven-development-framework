---
subject_scopes:
  - artifact-catalog
version: 3
updated_at: 2026-08-22 05:30:00
relations:
  child_of:
    - CAPRMEDIO-META-REQU-084--relational-artifacts-declare-endpoints
---
# Encode relational semantic shape

Every relational Atom must declare `semantic_shape: relational` in frontmatter. A standalone Atom uses the default `standalone` semantic shape and omits the default-valued property. Missing `semantic_shape` on an Atom that owns an independently governed relationship, or `semantic_shape: relational` without exact registered endpoint descriptors, is invalid.
