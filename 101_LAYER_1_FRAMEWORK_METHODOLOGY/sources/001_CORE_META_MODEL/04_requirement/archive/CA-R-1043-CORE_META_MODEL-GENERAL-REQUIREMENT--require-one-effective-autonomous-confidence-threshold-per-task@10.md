---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
  depends_on:
    continuant:
      - "Autonomous Confidence Threshold"
      - "Confidence Threshold/source"
atom_id: CA-R-1043
cce_version: cce_1
cce_form: obligation
version: 10
updated_at: "2026-09-10 06:39:08 +0400"
relations:
  child_of:
    - CA-R-989
---
# Require one effective Autonomous Confidence Threshold per Task

**every** Task Atom **must** resolve **`=1`** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source.
