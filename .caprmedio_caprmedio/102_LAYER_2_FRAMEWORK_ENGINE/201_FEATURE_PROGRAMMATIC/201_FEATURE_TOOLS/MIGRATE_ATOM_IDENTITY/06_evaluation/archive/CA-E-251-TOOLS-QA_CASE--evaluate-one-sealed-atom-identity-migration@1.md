---
subject_scopes:
  - artifact-operations
version: 1
updated_at: 2026-08-23 12:00:00
relations:
  evaluation_for:
    - CA-R-1048
---
# Evaluate one sealed Atom identity migration

Given identityless legacy, existing-ID carrier-token-correction, duplicate-ID-repair, and same-path relation/frontmatter-update temporary active Atom carriers with complete sealed requests, evaluate `MIGRATE_ATOM_IDENTITY` in dry-run mode twice per request. Both receipts must be byte-for-byte identical, name the expected source and result digests, list only declared frontmatter and relation changes, omit derived `atom_id` and `tier` from the result bytes, and state that Journal and Git were not performed.

Evaluate failure handling separately with a changed source digest, wrong version, duplicate target ID, occupied destination, old-identity mismatch, and missing relation target. Each case must fail before a source or destination carrier changes.
