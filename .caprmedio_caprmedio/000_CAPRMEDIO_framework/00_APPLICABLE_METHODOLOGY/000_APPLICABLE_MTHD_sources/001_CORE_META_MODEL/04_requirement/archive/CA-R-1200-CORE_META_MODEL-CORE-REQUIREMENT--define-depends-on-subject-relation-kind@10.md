---
cce_version: cce_1
cce_form: definition
subjects:
  governs: "DEPENDS_ON"
  depends_on:
    - "Relation Kind"
    - "Atom"
    - "Subject"
    - "Workflow"
    - "Atom/Content Role: Plan/Type: Task"
    - "Entity"
    - "Action"
    - "Atom/Claim"
version: 10
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Define DEPENDS_ON Subject Relation Kind

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** the canonical Entity, Action, **or** Workflow that its Claim requires **without** making the Atom authoritative about that target. it does **not** establish Workflow control flow **or** an execution order; Task prerequisite relations remain separately governed by CA-R-1007 **and** CA-R-1026.
