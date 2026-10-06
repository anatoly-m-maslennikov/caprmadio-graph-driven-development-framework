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
version: 2
updated_at: "2026-09-20 23:33:27 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1512"], "relates_to": ["CA-D-456"]}
---
# Serialize Action, Workflow, and Actor Atom Type tokens

an Operations Atom File Carrier **must** serialize its Type component using the following mapping **within** the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Action: `ACTION`.
- Workflow: `WORKFLOW`.
- Actor: `ACTOR`.

the additional Foundation **and** Rule filename tokens are governed by CA-D-456; this mapping does **not** define the Operations Local Tiers.
