---
subject_scopes:
  - artifact-model
version: 5
updated_at: 2026-08-21 04:43:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-110--bind-governed-transactions-to-stable-artifact-revisions
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Keep Atom identity independent of its mutable summary

An Atom's filename Summary is mutable Carrier metadata and is not part of its stable identity. A draft may change its Summary while it has no assigned Atom ID. An accepted role-classified Atom may change its Summary through a governed Revision while preserving the exact assigned Atom-ID segment in its Carrier filename.

Every committed Revision remains immutable and recoverable through governed
history. A Summary change that still describes the same role-specific atomic
unit updates the Carrier filename and H1 without creating a successor Atom.

A change to the primary atomic meaning, rather than a filename or Summary change by itself, requires a successor Atom and a new Atom ID.
