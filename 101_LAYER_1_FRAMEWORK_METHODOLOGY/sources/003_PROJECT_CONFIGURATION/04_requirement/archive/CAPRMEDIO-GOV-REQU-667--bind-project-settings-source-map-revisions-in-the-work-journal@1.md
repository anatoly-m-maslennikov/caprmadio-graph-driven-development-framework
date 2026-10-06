---
subject_scopes:
  - settings
version: 1
updated_at: 2026-08-18 07:37:18
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
    - CAPRMEDIO-META-REQU-165--atoms-have-version-and-updated-at
---
# Bind Project Settings Source Map revisions in the Work Journal

Every admitted revision of `CAPRMEDIO-PROJECT-SETTINGS-SOURCE-MAP` must have one append-only Work Journal binding containing its monotonic version, `updated_at`, canonical carrier address, and content digest. The latest valid binding whose address and digest match the canonical carrier establishes its current revision; a missing or mismatched binding leaves currentness unknown.
