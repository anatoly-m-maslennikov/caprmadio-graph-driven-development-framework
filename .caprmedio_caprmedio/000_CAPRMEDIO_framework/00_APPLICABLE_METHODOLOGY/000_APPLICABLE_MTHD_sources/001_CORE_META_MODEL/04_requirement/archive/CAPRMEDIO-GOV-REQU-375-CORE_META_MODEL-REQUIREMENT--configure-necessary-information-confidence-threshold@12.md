---
atom_id: CAPRMEDIO-GOV-REQU-375
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings
version: 12
updated_at: 2026-09-06 01:45:12 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-035-CORE-REQUIREMENT--identify-necessary-information-by-confidence
---
# Configure necessary-information confidence threshold

the Framework Instance Settings Artifact **must** expose `confidence.necessary_information_threshold_percent` as an integer percentage from 0 through 100 with an initial value of 95.
