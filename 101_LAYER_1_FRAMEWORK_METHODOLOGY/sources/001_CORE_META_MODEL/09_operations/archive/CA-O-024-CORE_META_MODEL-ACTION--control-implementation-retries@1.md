---
version: 1
updated_at: "2026-09-15 23:04:21 +0400"
relations:
  child_of:
    - CA-O-016
  relates_to:
    - CA-M-268
    - CA-M-130
subjects:
  governs: "Implementation Retry Control"
  depends_on:
    - "Action"
    - "Operator"
    - "Implementation Process"
    - "Atom/Content Role: Evaluation"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Task/Autonomous Confidence Threshold"
cce_version: cce_1
cce_form: definition
---
# Control implementation retries

Implementation Retry Control **means** the Action that determines whether the next fix-and-evaluate retry **may** start within the current implementation execution's retry allowance **and** governing permissions. repair **and** re-evaluation remain Actions **in** the Implementation Process under CA-O-016.

## execution

1. resolve the Operator-configured retry policy. **when** no override applies, allow **<=3** additional fix-and-evaluate retries **after** the initial failed Evaluation.
2. **if** successful completion under CA-O-016 has been reached, stop **without** permitting another automatic repair retry.
3. **before** permitting a retry, check the applicable confidence threshold under CA-M-130, governing-Atom approval rules under CA-M-268, **and** **all** additional Operator constraints. an unmet gate requires the applicable earlier escalation even **when** retries remain; retry allowance does **not** create permission.
4. **if** failure remains **and** the retry allowance is exhausted, pause **and** report the remaining failures **to** the Operator. under the default policy, this occurs **after** a failed third retry.
5. **only** **when** failure remains, the gates permit recovery, **and** a retry remains, permit the next fix-and-evaluate retry through CA-O-016.

## accounting

- the initial failed Evaluation consumes **=0** retries.
- count **=1** retry **when** a permitted fix-and-evaluate round starts, **not** merely **when** its permission is checked. repeated gate checks **must not** double-count that round.
- retain the consumed count throughout the current execution. a changed failure set **or** an automatic next loop **must not** silently reset the budget.
