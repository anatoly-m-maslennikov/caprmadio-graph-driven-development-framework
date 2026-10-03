---
atom_id: CAPRMEDIO-GOV-REQU-362
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - Framework Instance Settings/Artifact Timestamp Timezone
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
version: 12
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-1402
    - CA-R-1054
---
# Configure the Artifact timestamp timezone

the Framework Instance Settings Artifact **may** set `[artifact_timestamps].timezone` to `local`, `UTC`, **or** an IANA timezone name, with `local` as the default; **every** emitted `updated_at` value uses `YYYY-MM-DD HH:MM:SS`, **and** the setting supplies its timezone interpretation.
