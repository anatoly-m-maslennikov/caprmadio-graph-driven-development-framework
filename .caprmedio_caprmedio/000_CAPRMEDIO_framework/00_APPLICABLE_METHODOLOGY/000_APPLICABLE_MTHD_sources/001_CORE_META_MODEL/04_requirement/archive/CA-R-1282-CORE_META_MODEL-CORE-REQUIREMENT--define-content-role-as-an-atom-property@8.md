---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Atom/Content Role"
  depends_on:
    - "Atom"
    - "Property"
    - "Atom/Claim"
    - "Action"
    - "Workflow"
    - "Actor"
    - "Tool"
    - "Implementation"
    - "Carrier"
version: 8
updated_at: "2026-09-20 23:33:27 +0000"
relations: {"relates_to": ["CA-O-069"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define Content Role as an Atom Property

Content Role **means** the Atom Property that classifies the primary contribution of one Atom Claim, **not** **only** the Operation **or** Actor that the Claim mentions.

- definitions **and** reusable rules constituting the Operations model belong **to** Operations under CA-O-069, rather than being classified as Requirement merely because they define a concept **or** state a constraint.
- a Claim specifying an executor's **or** Tool's Implementation retains its applicable RMED role; mentioning **or** consuming an operational definition does **not** make that implementation specification an Operations definition.

the content contribution **must** be distinguished from the represented Entity, its Carrier, **and** its actual execution.
