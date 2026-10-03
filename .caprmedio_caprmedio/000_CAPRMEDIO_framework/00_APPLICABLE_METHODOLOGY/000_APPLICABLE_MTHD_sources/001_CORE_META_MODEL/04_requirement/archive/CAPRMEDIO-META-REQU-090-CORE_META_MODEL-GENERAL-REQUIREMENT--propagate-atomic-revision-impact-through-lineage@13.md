---
atom_id: CAPRMEDIO-META-REQU-090
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - lifecycle-traceability
version: 13
updated_at: "2026-09-10 06:29:38 +0400"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-E-002
---
# Propagate atomic revision impact through lineage

**when** an Atom receives a new committed revision, is replaced by a successor, **or** moves to the archive, CAPRMEDIO **must** assess **every** reachable descendant lineage branch recursively **until** **every** branch has an explicit impact disposition.
