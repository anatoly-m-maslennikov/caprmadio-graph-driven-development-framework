---
cce_version: cce_1
cce_form: permission
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "Exploration Mode"
    - "Atom/Content Role: Concern"
version: 1
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CAPRMEDIO-META-REQU-114"]}
---
# Keep conflict discovery in Exploration Mode

an AI Agent **must** keep a discovered conflict **in** Exploration Mode; it **may** create a Concern for that conflict **only** **when** the Operator requests persistence **or** defers its resolution.
