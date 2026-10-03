---
atom_id: "CA-M-265"
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs: "Atom/Content Role: Evaluation/grouping"
  depends_on:
    - "Atom/Content Role"
    - "Evaluation For Relation"
version: 4
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Derive evaluation groups from checked authority

**to** derive Er, Em, **and** Ed groups, resolve the Content Role of **every** `evaluation_for` target **and** include the Evaluation **in** the corresponding Requirement, Method, **or** Delivery group; **if** targets span multiple roles, **then** include it **in** **every** applicable group **without** assigning a new Content Role **or** persisting a duplicate target-role field. absence of individual targets on a Core **or** General Evaluation policy admitted by CA-R-1018 **must not** require an invented classification.
