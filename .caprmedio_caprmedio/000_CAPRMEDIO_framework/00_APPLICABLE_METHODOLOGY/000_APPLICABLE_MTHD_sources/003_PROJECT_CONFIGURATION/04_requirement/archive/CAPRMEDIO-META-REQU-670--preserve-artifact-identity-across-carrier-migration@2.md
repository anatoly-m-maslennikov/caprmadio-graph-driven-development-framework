---
subject_scopes:
  - artifact-model
version: 2
updated_at: 2026-08-21 04:43:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Preserve Artifact identity across Carrier migration

An Artifact retains its stable identity across a Carrier move or format-preserving migration only while its governed meaning and identity remain unchanged. For a role-classified Atom, the immutable Atom-ID segment of its canonical Carrier filename encodes Artifact identity; the complete filename and other physical address components, extension, digest, and Git commit may resolve a Revision but do not replace that identity.
