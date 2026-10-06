---
cce_version: "cce_1"
cce_form: "evaluation"
version: 8
updated_at: "2026-09-17 23:40:00 +0000"
relations: {"child_of":["CA-E-001"],"evaluation_for":["CA-O-024","CA-O-016","CA-O-061","CA-M-295"]}
subjects:
  governs: "Implementation Retry Control"
  depends_on:
    - "Operator"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
    - "Project"
    - "Implementation Retry Limit"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate retry budget and escalation

the retry-policy Evaluation **must** return `fail` **if** **any** of the following occurs:

- the initial failed Evaluation consumes a retry.
- an automatic retry exceeds the effective Implementation Retry Limit resolved under CA-M-295 **and** enforced by CA-O-024.
- starting a permitted fix-and-evaluate round is **not** counted once, **or** checking its permission again consumes another retry.
- a changed failure set **or** automatic next loop silently resets the budget.
- the last permitted retry fails **without** pausing **and** reporting remaining failures **to** the Operator.
- retrying bypasses a confidence gate, governing-Atom approval rule, **or** additional Operator constraint.
- successful completion under CA-O-016 still triggers another automatic repair retry.

earlier escalation required by governing authority **must not** be rejected merely because retries remain.
