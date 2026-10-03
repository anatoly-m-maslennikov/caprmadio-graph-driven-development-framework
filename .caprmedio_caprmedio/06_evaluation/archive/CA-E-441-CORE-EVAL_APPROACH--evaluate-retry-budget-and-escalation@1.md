---
atom_id: CA-E-441
cce_version: "cce_1"
cce_form: "evaluation"
subjects:
  governs:
    occurrent:
      - "Project/Implementation/retry"
  depends_on:
    continuant:
      - "Operator"
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Implementation"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-05 18:40:03 +0400"
relations:
  child_of:
    - "CA-E-001"
  evaluation_for:
    - "CA-M-269"
    - "CA-M-267"
    - "CA-M-268"
---
# Evaluate retry budget and escalation

the retry-policy Evaluation **must** return `fail` **if** the initial failed evaluation consumes a retry, an automatic retry exceeds the Operator-configured limit **or** the default governed by CA-M-269, a changed failure set **or** next loop silently resets the budget, **or** the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator. it **must** also return `fail` **if** retrying bypasses a confidence **or** approval gate, **or** successful completion under CA-M-267 still triggers another automatic repair retry. earlier escalation required by governing authority **must not** be rejected merely because retries remain.
