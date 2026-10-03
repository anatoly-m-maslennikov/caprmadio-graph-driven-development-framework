---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "ACTION_PROMPTS/Goal"
  depends_on:
    - "PROMPTS"
    - "Action"
version: 1
updated_at: "2026-09-23 04:20:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Implement Actions as Agent Instructions

ACTION_PROMPTS **must** own self-contained agent-facing prompt implementations of methodology Actions. An ACTION_PROMPT supplies executable instructions **and** invocation context but does **not** own the Action meaning, Workflow state, Step transition, **or** Operator authority.
