---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Subject Expression Writing"
  depends_on:
    - "Subject Path"
    - "Entity"
    - "Action"
    - "Workflow"
    - "Relation"
    - "Term"
    - "Subject"
    - "GOVERNS"
    - "DEPENDS_ON"
version: 10
updated_at: "2026-09-18 14:16:20 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Write Subject Expressions with Bearer and Value Qualification

**to** write a Subject Expression, start with a canonical Entity, Action, **or** Workflow reference **and** apply `/` **or** `:` qualification **only** **where** the registered relation admits the exact endpoints. `/` retains bearer qualification **and** `:` retains allowed-value qualification; resolve **every** named component, including names **before** **and** **after** the separators, as a Term reference under CA-R-1321. the resulting qualified path identifies its existing canonical target **without** copying it; connecting the Atom **to** that target through GOVERNS **or** DEPENDS_ON creates the Subject Relation, **not** another target Entity.
