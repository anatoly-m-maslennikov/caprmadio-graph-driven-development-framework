---
atom_id: CA-M-266
cce_version: "cce_1"
cce_form: "method"
version: 4
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - "CA-M-261"
  relates_to:
    - "CA-M-262"
subjects:
  governs: "Project/Implementation/mode selection"
  depends_on:
    - "Operator"
    - "Spec"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Requirement"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Delivery"
    - "Project"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Follow the Operator-selected implementation mode

**to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
