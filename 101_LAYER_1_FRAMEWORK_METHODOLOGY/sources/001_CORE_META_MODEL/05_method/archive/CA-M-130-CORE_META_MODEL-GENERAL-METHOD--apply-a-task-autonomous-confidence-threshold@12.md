---
atom_id: CA-M-130
subjects:
  governs: "Autonomous Confidence Threshold Application"
  depends_on:
    - "Autonomous Confidence Threshold"
    - "Confidence Threshold/source"
    - "AI Agent/Confidence"
    - "Operator/authority"
cce_version: cce_1
cce_form: method
version: 12
updated_at: "2026-09-10 05:28:44 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Apply a Task Autonomous Confidence Threshold

**to** apply a Task's Autonomous Confidence Threshold, an AI Agent **must** resolve the effective value according **to** CA-M-271; **if** confidence **in** correct Task execution is below that value, **then** the AI Agent **must** request Operator disposition **before** continuing; **otherwise** the AI Agent **may** continue **only** within its existing authority.
