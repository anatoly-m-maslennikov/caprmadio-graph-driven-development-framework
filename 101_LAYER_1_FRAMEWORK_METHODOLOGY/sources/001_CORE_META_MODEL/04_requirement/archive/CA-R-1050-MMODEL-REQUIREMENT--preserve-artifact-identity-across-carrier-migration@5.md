---
subjects:
  - artifact-model
version: 5
updated_at: "2026-08-23 11:37:28"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-128--separate-artifact-carrier-and-revision
---
# Preserve Artifact identity across Carrier migration

An Artifact retains its stable identity across a Carrier move or format-preserving migration only while its governed meaning and identity remain unchanged. For a role-classified Atom, the immutable Atom-ID segment of its canonical Carrier basename encodes Artifact identity; the complete basename and other physical address components, extension when applicable, digest, and Git commit may resolve a Revision but do not replace that identity.
