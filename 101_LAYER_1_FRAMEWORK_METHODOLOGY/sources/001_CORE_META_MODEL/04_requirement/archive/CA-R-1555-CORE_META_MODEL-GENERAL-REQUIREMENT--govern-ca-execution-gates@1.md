---
cce_version: cce_1
cce_form: permission
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Autonomous Confidence Threshold"
    - "Operator"
    - "AI Agent Delegation"
version: 1
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CAPRMEDIO-META-REQU-144"]}
---
# Govern CA execution gates

an identified AI Agent **may** omit clarification **only** **when** confidence **in** **every** following item meets its applicable configured requirement:

- intent;
- scope;
- route;
- entry criteria.

confidence **must not** create delegated authority **or** bypass per-action Operator approval **when** active authority requires it.
