---
atom_id: CA-E-438
cce_version: "cce_1"
cce_form: "evaluation"
version: 2
updated_at: "2026-09-05 23:00:00 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-M-266"
    - "CA-M-262"
subjects:
  governs:
    occurrent:
      - "Project/Implementation/mode selection"
  depends_on:
    continuant:
      - "Operator"
      - "Spec"
      - "Atom/Content Role: Plan/Type: Task"
      - "Atom/Content Role: Implementation"
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Requirement"
      - "Atom/Content Role: Method"
      - "Atom/Content Role: Delivery"
      - "Project"
---
# Evaluate implementation mode conformance

the implementation mode Evaluation **must** return `fail` **if** execution replaces the Operator-selected mode **without** authorization, treats an evaluation-and-fix request as permission for a full rebuild, exceeds Task permissions, **or** exempts the selected mode from the governing RMED. authorized rewriting **or** different source-code bytes **must not** by themselves cause failure **when** reconstruction equivalence under CA-M-262 is preserved.
