---
cce_version: cce_1
cce_form: prohibition
subjects:
  governs: "Atom/Content Role: Requirement/Type: Demand/Direction"
  depends_on:
    - "Local Order"
    - "Scope Unit/Type: Ordered"
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Prohibit Demands to Later Ordered Siblings

a Demand Atom owned by an Ordered Scope Unit **must not** target a later Ordered sibling under the same direct parent.
