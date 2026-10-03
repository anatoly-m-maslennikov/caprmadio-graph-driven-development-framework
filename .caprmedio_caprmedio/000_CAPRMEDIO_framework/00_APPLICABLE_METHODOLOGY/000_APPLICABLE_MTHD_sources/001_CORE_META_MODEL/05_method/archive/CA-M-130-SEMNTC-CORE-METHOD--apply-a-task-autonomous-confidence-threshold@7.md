---
atom_id: CA-M-130
subjects:
  governs:
    occurrent:
      - Autonomous Confidence Threshold Application
  depends_on:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
      - AI Agent/Confidence
cce_version: cce_1
cce_form: method
version: 7
updated_at: 2026-08-29 04:33:13 +0400
relations: {}
---
# Apply a Task Autonomous Confidence Threshold

**if** an AI Agent's confidence **in** correct Task execution is below its Autonomous Confidence Threshold, **then** the AI Agent **must** request Operator disposition **before** continuing; **otherwise** the AI Agent **may** continue autonomously.
