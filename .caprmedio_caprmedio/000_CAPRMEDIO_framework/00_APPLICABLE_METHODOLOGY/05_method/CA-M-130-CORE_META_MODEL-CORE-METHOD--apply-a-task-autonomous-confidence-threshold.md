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
version: 8
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-130-CORE_META_MODEL-CORE-METHOD--apply-a-task-autonomous-confidence-threshold.md
---
# Apply a Task Autonomous Confidence Threshold

**if** an AI Agent's confidence **in** correct Task execution is below its Autonomous Confidence Threshold, **then** the AI Agent **must** request Operator disposition **before** continuing; **otherwise** the AI Agent **may** continue autonomously.
