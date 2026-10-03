---
cce_version: cce_1
cce_form: placement
subjects:
  governs: "Atom/Content Role: Plan/Carrier Placement"
  depends_on:
    - "Atom/Content Role: Plan/Status"
    - "Atom/Content Role: Plan/Authoritative Carrier Bundle"
version: 1
updated_at: "2026-09-20 23:55:10 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-R-1539", "CA-R-1540", "CA-R-1541"]}
---
# Place Plan Carriers by Status

**every** Plan Atom Carrier Bundle **must** be placed under its Atom Scope's `03_plan` directory as follows: within the current branch outside the reserved lifecycle subtrees for Active; anywhere below `03_plan/031_backlog` for Backlog; below `03_plan/done` for Done; below `03_plan/canceled` for Canceled; **and** below `03_plan/archived` for Archived. `031_backlog`, `done`, `canceled`, **and** `archived` are the reserved lifecycle directories directly below `03_plan`.
