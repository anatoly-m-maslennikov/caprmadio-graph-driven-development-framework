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
version: 9
updated_at: "2026-09-09 02:24:28 +0400"
relations:
  child_of:
    - CA-R-989
---
# Require one effective Autonomous Confidence Threshold per Task

**every** Task Atom **must** resolve **`=1`** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source.
