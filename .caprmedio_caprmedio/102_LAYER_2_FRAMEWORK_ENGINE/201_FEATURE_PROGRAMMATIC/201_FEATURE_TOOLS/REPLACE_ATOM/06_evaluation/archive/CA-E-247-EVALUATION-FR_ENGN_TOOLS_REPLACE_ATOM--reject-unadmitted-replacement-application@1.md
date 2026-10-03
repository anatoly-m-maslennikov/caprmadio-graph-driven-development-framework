---
atom_id: CA-E-247
subject_scopes:
  - artifact-operations
version: 1
updated_at: 2026-08-23 02:45:35
---
# Reject unadmitted replacement application

Given two distinct active Atom IDs and action context, `REPLACE_ATOM` dry run must return their explicit replacement intent and a deferred commit-pipeline handoff. Applying the same input before lifecycle-intent serialization is admitted must return an apply-blocked diagnostic and leave every Atom carrier, Journal, Git index, Git history, and runtime file unchanged.
