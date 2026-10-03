---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Method"
  depends_on:
    - "Evaluation"
    - "TOOLS"
    - "PROMPTS"
version: 1
updated_at: "2026-09-23 04:25:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Separate Code and Prompt Method-Evaluation Authority

A Method **or** Evaluation that applies only to executable code **must** be owned by TOOLS **or** its applicable code Scope Unit. A Method **or** Evaluation that applies only to prompt implementations **must** be owned by PROMPTS, ACTION_PROMPTS, OPERATOR_PROMPTS, **or** its applicable prompt Scope Unit. Cross-implementation authority **must** remain at the lowest common Scope Unit and state both implementation classes explicitly.
