---
subjects:
  - provenance
project_graph_state:
  artifacts:
    enabled_types:
      - work_journal
  paths:
    journal_root: .caprmedio/work_journal
version: 10
updated_at: 2026-08-23 01:44:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-META-REQU-158--make-journals-canonical-for-governed-provenance
  replacement_of:
    - CAPRMEDIO-GOV-REQU-484--keep-governed-journals-in-role-folders
---
# Register the Project Work Journal

GOVERNANCE must register `.caprmedio/work_journal/` as the canonical home of one project-wide logical Work Journal composed of append-only NDJSON segments. New events are partitioned first by their full GitHub author username, then by their calendar date in the configured Artifact timestamp timezone, and then into segments of at most 100 events named `<author>-<YYYY-MM-DD>-part-<N>.ndjson`, where `N` is a positive decimal integer starting at `1`. The current segment for one author and date remains open until its hundredth accepted event; the next accepted event opens the next numbered segment. Accepted records and sealed segments must never be edited, reordered, or deleted, and deterministic replay uses event occurrence time followed by carrier name and line position as tie-breakers. Previously admitted segment names remain replayable under their declared schema but receive no new events.
