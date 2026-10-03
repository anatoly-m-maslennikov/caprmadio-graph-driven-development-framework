---
atom_id: CA-E-248
subject_scopes:
  - concern-resolution
version: 2
updated_at: 2026-08-23 02:55:00
---
# Reject unadmitted Concern closure application

Given one active Concern Atom ID, a terminal disposition, explicit action context, and any supplied active resolver or subject IDs, `CLOSE_ATOM` dry run must return the corresponding closure intent and deferred commit-pipeline handoff. Applying the same input before lifecycle-intent serialization is admitted must return an apply-blocked diagnostic and leave every Atom carrier, Journal, Git index, Git history, and runtime file unchanged.
