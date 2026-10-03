---
version: 8
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - CA-R-815
  method_for:
    - CA-R-818
subjects:
  governs: "Project/active rule set selection"
  depends_on:
    - "Project"
    - "Operator"
cce_version: cce_1
cce_form: method
atom_id: CA-M-096
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Select the active rule set at its declared priority

select which optional rules **and** rule groups are active for the affected scope **and** Project stage according **to** the current Operator-declared active-rule-set priority **without** disabling mandatory authority.
