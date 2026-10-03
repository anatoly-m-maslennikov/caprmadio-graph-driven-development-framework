---
atom_id: CAPRMEDIO-META-REQU-090
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - lifecycle-traceability
version: 12
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-E-002
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-META-REQU-090-CORE_META_MODEL-CORE-REQUIREMENT--propagate-atomic-revision-impact-through-lineage.md
---
# Propagate atomic revision impact through lineage

**when** an Atom receives a new committed revision, is replaced by a successor, **or** moves to the archive, CAPRMEDIO **must** assess **every** reachable descendant lineage branch recursively **until** **every** branch has an explicit impact disposition.
