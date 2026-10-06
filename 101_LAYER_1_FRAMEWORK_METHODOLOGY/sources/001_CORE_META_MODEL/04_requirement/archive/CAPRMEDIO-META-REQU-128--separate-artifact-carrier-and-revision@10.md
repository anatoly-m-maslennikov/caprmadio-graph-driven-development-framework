---
cce_version: cce_1
cce_form: separation
subjects:
  - artifact-model
tier: core
version: 10
updated_at: 2026-08-23 12:02:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-D-003-PRINCIPLE-DELIVERY--provide-one-project-graph-as-the-operating-model
---
# Separate artifact carrier and revision

CAPRMEDIO distinguishes an Artifact from its Carrier and Revisions. An Artifact is a governed semantic object. An assigned Atom ID identifies an Atom Artifact rather than its Carrier or any one Revision. A role-classified Atom's Carrier filename canonically encodes that identity in an immutable Atom-ID segment; the remainder of the Carrier address, filename, and content MAY change without replacing the Atom while that segment remains unchanged. A Carrier is the Artifact's mutable physical representation in a native format at a governed project-relative address. A Revision is one exact recoverable Carrier state.
