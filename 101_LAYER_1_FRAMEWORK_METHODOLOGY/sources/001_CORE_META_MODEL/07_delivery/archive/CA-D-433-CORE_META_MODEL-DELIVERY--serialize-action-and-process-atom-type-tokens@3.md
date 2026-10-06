---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    - "Carrier"
version: 3
updated_at: 2026-09-15 05:51:38
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Serialize Action and Process Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type component as `ACTION` **if** its Type is Action **or** as `PROCESS` **if** its Type is Process, within the Atom filename grammar governed by CA-D-283 **and** CA-D-284.
