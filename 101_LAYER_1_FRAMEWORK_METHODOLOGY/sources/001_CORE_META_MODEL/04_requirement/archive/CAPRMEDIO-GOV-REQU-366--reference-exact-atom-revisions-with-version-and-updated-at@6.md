---
subject_scopes:
  - provenance
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
version: 6
updated_at: 2026-08-22 02:12:36
relations:
  child_of:
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
    - CA-R-888
---
# Reference exact Atom revisions with version and updated at

An exact identified role-classified Atom Revision reference uses `<ATOM_ID>@<version>,<updated_at>`, where the Atom ID derived from the canonical Carrier filename's immutable leading segment and both Revision-property values exactly match the target governed history. An exact Intent Revision reference uses `CA-intent@<version>,<updated_at>`. An exact draft Revision reference may use `<CURRENT_DRAFT_FILENAME_STEM>@<version>,<updated_at>` as a provisional locator while no Atom ID is assigned. Carrier filenames contain neither `version` nor `updated_at`; filename changes must preserve an assigned Atom-ID segment.
