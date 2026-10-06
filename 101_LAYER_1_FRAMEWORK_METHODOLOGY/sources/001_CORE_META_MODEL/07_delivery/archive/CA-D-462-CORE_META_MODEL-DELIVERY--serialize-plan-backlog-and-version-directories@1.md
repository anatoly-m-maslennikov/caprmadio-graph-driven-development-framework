---
cce_version: cce_1
cce_form: grammar
subjects:
  governs: "Atom/Content Role: Plan/Backlog/Carrier Placement"
  depends_on:
    - "Atom/Content Role: Plan/Backlog"
    - "Atom Collection/Type: Version Plan"
    - "Directory Carrier"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1542", "CA-R-1543"]}
---
# Serialize Plan Backlog and Version Directories

the Plan Backlog Directory **must** be named `031_backlog`; each Version Plan Collection Directory directly below it **must** be named `version-<VERSION>`; ungrouped Backlog Objective Atoms **may** be placed directly below `031_backlog`; **and** Version membership **must not** create another `planned` directory **or** Status.
