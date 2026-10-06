---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Actor"
  depends_on:
    - "Operator"
    - "AI Agent"
    - "Project"
    - "Atom/Local Tier: Principle"
    - "AI Agent Delegation"
    - "Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-17 04:33:10 +0000"
relations:
  child_of:
    - CA-R-1058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reserve Principle-conflict resolution to the Operator

- **only** an Operator **may** resolve a conflict between active Project Principles, **and** that decision is non-delegable.
- an AI Agent **may** detect, analyze, **and** propose resolutions for that conflict but **must not** choose one.
- an AI Agent **may** resolve a conflict that does **not** involve two active Project Principles **only** **when** its active Operator delegation permits **every** required action **and** the configured confidence requirements are satisfied.
