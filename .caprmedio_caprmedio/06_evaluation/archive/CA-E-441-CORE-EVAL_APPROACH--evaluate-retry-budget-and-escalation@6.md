---
cce_version: "cce_1"
cce_form: "evaluation"
version: 6
updated_at: "2026-09-17 14:50:12 +0000"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-O-024","CA-O-016","CA-O-061"]}
subjects:
  governs: "Project/Implementation/retry"
  depends_on:
    - "Implementation Retry Control"
    - "Operator"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
    - "Project"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
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
