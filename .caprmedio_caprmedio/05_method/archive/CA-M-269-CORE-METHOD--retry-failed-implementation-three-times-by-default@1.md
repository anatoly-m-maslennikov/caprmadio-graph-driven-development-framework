---
atom_id: CA-M-269
cce_version: "cce_1"
cce_form: "method"
subjects:
  governs:
    occurrent:
      - "Project/Implementation/retry"
  depends_on:
    continuant:
      - "Operator"
      - "Atom/Content Role: Evaluation"
      - "Atom/Content Role: Implementation"
      - "Atom/Content Role: Plan/Type: Task"
      - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
version: 1
updated_at: "2026-09-05 18:40:03 +0400"
relations:
  child_of:
    - "CA-M-261"
  relates_to:
    - "CA-M-267"
    - "CA-M-268"
    - "CA-M-130"
---
# Retry failed implementation three times by default

**to** recover from a failed implementation Evaluation, use the Operator-configured retry policy **or**, **when** no override applies, allow **`<=3`** additional fix-and-evaluate retries **after** the initial failed evaluation. the initial failure does **not** consume a retry. stop on successful completion under CA-M-267; **if** failure remains **after** the third retry under the default policy, **then** pause **and** report the remaining failures **to** the Operator. retry permission **must not** override the Task confidence threshold, governing-Atom approval rules, **or** other Operator constraints; those rules **may** require earlier escalation. a changed failure set **or** automatic next loop **must not** silently reset the retry budget.
