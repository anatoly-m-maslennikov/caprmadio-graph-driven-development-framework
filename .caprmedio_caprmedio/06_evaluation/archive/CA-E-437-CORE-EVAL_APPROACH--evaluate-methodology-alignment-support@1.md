---
atom_id: "CA-E-437"
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    occurrent:
      - "CAPRMEDIO Framework Instance/alignment support"
  depends_on:
    continuant:
      - "CAPRMEDIO Framework Instance"
      - "Applicable Methodology"
      - "Operator"
      - "Tool"
      - "Artifact"
version: 1
updated_at: "2026-09-05 03:48:00 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-R-1424"
---
# Evaluate methodology alignment support

the methodology alignment support Evaluation **must** return `fail` **if** the available Tools cannot assess the governed instance against the current Applicable Methodology, omit known nonconformance, cannot support an authorized repair, **or** mutate authority **without** Operator permission; a targeted check **may** use a bounded affected Scope **and** its dependencies. an unresolved finding **or** Operator-created orphan **must not** by itself establish failure of the required support capability **or** be reported as conformance.
