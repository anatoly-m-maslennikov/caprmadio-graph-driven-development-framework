---
atom_id: CA-R-1445
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Atom/Content Role: Plan/Type: Task/Claim/Structural Entity"
  depends_on:
    - "Scope Unit"
    - "Atom Collection/Type: Epic"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Default Task Target to the Enclosing Scope Unit

a Task Atom with a containing Scope Unit **and** **without** an explicit Claim Structural Entity **must** use its nearest containing Scope Unit as its Claim Structural Entity, independently of containment **in** an Epic **or** nested Epics.
