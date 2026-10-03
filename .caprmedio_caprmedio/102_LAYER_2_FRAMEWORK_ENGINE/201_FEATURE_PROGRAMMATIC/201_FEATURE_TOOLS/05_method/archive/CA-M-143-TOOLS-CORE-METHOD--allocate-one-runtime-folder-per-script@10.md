---
subjects:
  governs: "runtime"
  depends_on: []
version: 10
updated_at: "2026-09-16 23:48:40 +0000"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  method_for:
    - CA-R-1065
  derived_from:
    - CA-A-057
---
# Allocate one runtime folder per script

Give each CAPRMEDIO script or executable tool that persists runtime files one dedicated directory beneath the caprmedio runtime root. Keep its runtime files inside that directory; concurrent runs may use bounded run-specific descendants.

Do not scatter runtime files, write into another script's directory, or depend on an unowned shared directory. A shared runtime service owns its own directory and clients use its service contract rather than its files.
