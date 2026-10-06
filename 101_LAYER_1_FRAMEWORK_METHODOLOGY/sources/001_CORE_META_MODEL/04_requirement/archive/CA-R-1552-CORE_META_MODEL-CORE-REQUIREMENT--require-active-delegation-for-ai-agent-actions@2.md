---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "AI Agent Delegation"
version: 2
updated_at: "2026-09-21 00:39:50 +0000"
relations:
  child_of:
    - CA-P-034
---
# Require active delegation for AI Agent actions

an AI Agent **may** perform **or** authorize a governed action **without** per-action Operator approval **only** while an active Operator-issued delegation authorizes that identified Agent, action, target scope, **and** applicable constraints.
