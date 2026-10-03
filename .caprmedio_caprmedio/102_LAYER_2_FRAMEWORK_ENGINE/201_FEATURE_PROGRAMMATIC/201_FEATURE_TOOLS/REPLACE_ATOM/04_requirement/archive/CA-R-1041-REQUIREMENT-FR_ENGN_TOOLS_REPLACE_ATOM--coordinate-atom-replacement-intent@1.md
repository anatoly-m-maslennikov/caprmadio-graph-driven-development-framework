---
atom_id: CA-R-1041
subject_scopes:
  - artifact-operations
tier: core
version: 1
updated_at: 2026-08-23 02:45:35
---
# Coordinate Atom replacement intent

`REPLACE_ATOM` must accept one exact active predecessor Atom ID, one exact active successor Atom ID, and explicit action context. It must reject missing, duplicate, inactive, or identical IDs; verify that the successor is already admitted as an active carrier; and return one replacement intent that names the successor admission and predecessor archive intent.

The Tool must not infer, create, or write Atom relations. It must hand the supplied IDs and action context to the commit pipeline only as a deferred lifecycle-intent contract. Until `COMMIT_CONTEXT`, `APPEND_CHANGE_RECORDS`, and `COMMIT_CHANGE_SET` accept that contract and serialize it in the Journal, `--apply` must fail before mutating Atoms, Journals, Git, or runtime state. Omitting `--apply` must return the complete mutation-free intent.
