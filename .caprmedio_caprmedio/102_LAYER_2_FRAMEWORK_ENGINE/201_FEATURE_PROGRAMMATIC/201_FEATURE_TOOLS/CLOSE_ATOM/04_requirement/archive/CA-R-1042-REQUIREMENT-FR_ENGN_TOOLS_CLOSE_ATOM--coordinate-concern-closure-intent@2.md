---
atom_id: CA-R-1042
subject_scopes:
  - concern-resolution
tier: core
version: 2
updated_at: 2026-08-23 02:55:00
---
# Coordinate Concern closure intent

`CLOSE_ATOM` must accept one exact active Concern Atom ID, one explicit terminal disposition, optional explicit resolver and subject Atom-ID lists, and action context. It must reject a missing, non-Concern, inactive, or unresolved referenced Atom ID and return one closure intent targeting the Concern's `solved` state.

Resolver and subject IDs describe supplied intent only. The Tool must not infer relation kinds, role meanings, or a participant that was not supplied. It must hand those IDs and action context to the commit pipeline only as a deferred lifecycle-intent contract. Until the commit pipeline admits and serializes that contract in the Journal, `--apply` must fail before mutating Atoms, Journals, Git, or runtime state; dry run must remain mutation-free.
