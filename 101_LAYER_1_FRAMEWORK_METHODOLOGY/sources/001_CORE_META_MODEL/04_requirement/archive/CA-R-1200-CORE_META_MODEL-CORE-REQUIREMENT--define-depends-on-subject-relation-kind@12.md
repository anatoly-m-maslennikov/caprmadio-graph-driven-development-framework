---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Relation Kind"
    - "Atom"
    - "Subject"
    - "Atom/Content Role: Plan/Type: Plan"
    - "Entity"
    - "Atom/Claim"
    - "Workflow"
version: 12
updated_at: "2026-09-22 20:07:50 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define DEPENDS_ON Subject Relation Kind

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** the canonical Entity that its Claim requires **without** making the Atom authoritative about that target. it does **not** establish Workflow control flow **or** an execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580.
