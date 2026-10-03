---
atom_id: CA-E-441
cce_version: "cce_1"
cce_form: "evaluation"
version: 4
updated_at: "2026-09-15 23:04:21 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-O-024"
    - "CA-O-016"
    - "CA-M-268"
subjects:
  governs: "Project/Implementation/retry"
  depends_on:
    - "Implementation Retry Control"
    - "Operator"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
    - "Project"
---
# Evaluate retry budget and escalation

the retry-policy Evaluation **must** return `fail` **if** **any** of the following occurs:

- the initial failed Evaluation consumes a retry.
- an automatic retry exceeds the Operator-configured limit **or** the default governed by CA-O-024.
- starting a permitted fix-and-evaluate round is **not** counted once, **or** checking its permission again consumes another retry.
- a changed failure set **or** automatic next loop silently resets the budget.
- the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator.
- retrying bypasses a confidence gate, governing-Atom approval rule, **or** additional Operator constraint.
- successful completion under CA-O-016 still triggers another automatic repair retry.

earlier escalation required by governing authority **must not** be rejected merely because retries remain.
