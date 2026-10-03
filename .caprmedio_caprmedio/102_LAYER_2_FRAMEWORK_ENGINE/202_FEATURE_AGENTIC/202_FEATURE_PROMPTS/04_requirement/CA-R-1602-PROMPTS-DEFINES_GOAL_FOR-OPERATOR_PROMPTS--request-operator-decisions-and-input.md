---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "OPERATOR_PROMPTS/Goal"
  depends_on:
    - "PROMPTS"
    - "Operator"
version: 1
updated_at: "2026-09-23 04:20:00 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Request Operator Decisions and Input

OPERATOR_PROMPTS **must** own user-facing prompts that request an Operator decision, authorization, clarification, **or** input. They **must not** be treated as agent-executable Action implementations **or** as substitutes for the Operator's response.
