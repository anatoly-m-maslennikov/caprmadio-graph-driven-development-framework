---
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - settings
version: 9
updated_at: 2026-08-29 02:40:41 +0400
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-035--identify-necessary-information-by-confidence
---
# Configure necessary-information confidence threshold

The Project Configuration Atom **must** expose `confidence.necessary_information_threshold_percent` as an integer percentage from 0 through 100 with an initial value of 95.
