---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "AI Agent Delegation"
version: 1
updated_at: "2026-09-17 04:33:34 +0000"
relations:
  child_of:
    - CA-P-034
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Require active delegation for AI Agent actions

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** while an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
