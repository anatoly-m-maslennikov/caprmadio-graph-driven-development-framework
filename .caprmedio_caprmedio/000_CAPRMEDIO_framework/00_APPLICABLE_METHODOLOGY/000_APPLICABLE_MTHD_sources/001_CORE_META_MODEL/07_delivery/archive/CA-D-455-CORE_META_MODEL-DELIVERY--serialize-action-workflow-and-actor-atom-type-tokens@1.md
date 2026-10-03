---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Atom/Content Role: Operations/Type"
  depends_on:
    - "Artifact/Carrier"
    - "Type"
    - "Action"
    - "Workflow"
    - "Actor"
version: 1
updated_at: "2026-09-18 14:16:20 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1512"]}
---
# Serialize Action, Workflow, and Actor Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type component using the following mapping within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Action: `ACTION`.
- Workflow: `WORKFLOW`.
- Actor: `ACTOR`.
