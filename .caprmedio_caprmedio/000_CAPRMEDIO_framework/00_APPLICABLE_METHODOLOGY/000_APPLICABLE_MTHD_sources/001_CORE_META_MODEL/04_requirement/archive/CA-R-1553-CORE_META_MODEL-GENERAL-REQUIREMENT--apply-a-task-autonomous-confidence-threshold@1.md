---
subjects:
  governs: "AI Agent/authorization"
  depends_on:
    - "AI Agent"
    - "Operator"
    - "Autonomous Confidence Threshold"
    - "Confidence Threshold/source"
    - "AI Agent/Confidence"
    - "Operator/authority"
cce_version: cce_1
cce_form: obligation
version: 1
updated_at: "2026-09-21 00:39:50 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Apply a Task Autonomous Confidence Threshold

an AI Agent's autonomous continuation on a Task **must** satisfy this authorization policy:

- resolve the effective Autonomous Confidence Threshold according **to** CA-M-271.
- **if** confidence **in** correct Task execution is below that value, **then** request Operator disposition **before** continuing.
- **otherwise**, the AI Agent **may** continue **only** within its existing authority. meeting the threshold does **not** grant additional authority.
