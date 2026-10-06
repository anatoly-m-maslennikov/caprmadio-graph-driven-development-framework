---
atom_id: CAPRMEDIO-META-REQU-090
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "lifecycle-traceability"
  depends_on: []
version: 16
updated_at: "2026-09-14 06:21:07 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
    - CA-E-002
---
# Propagate atomic revision impact through lineage

**when** an Atom receives a new accepted Revision, is replaced by a successor, **or** moves to the archive, CAPRMEDIO **must** assess **every** reachable descendant lineage branch recursively **until** **every** branch has an explicit impact disposition.
