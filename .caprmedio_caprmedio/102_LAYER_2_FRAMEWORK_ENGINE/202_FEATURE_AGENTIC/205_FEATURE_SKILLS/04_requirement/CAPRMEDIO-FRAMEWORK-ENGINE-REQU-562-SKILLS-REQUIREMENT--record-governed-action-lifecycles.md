---
subject_scopes:
  - session-engine
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 6
updated_at: "2026-09-10 07:33:47 +0400"
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-339
    - CAPRMEDIO-GOV-REQU-340
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-522--append-work-journal-events
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-523--reconcile-work-journal-coverage
---
# Record governed action lifecycles

the session engine **and** **every** Skill that performs governed work **must** use deterministic Tools **to** record its start **and** terminal outcome **and** **to** reconcile missing Work Journal coverage **after** session initialization **or** context recovery.
