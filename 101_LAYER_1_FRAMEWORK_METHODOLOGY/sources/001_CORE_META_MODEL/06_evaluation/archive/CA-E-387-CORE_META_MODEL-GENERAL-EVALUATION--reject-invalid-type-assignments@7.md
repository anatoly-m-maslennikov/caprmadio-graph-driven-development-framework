---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Type Assignment Evaluation"
  depends_on:
    - "Entity"
    - "Subject Expression"
    - "Type"
version: 7
updated_at: "2026-09-10 05:28:44 +0400"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reject Invalid Type Assignments

the Evaluation **must** reject a Type assignment **if** one Entity occurrence has **`>1`** direct Type values, the selected value is **not** allowed by its most-specific applicable qualified Type Subject, **or** qualified Type Subjects create **`>1`** Type Property slots for the occurrence.
