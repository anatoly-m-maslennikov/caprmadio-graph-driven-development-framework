---
version: 5
updated_at: "2026-09-17 14:50:12 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"child_of":["CA-O-016"],"relates_to":["CA-O-061","CA-O-050","CA-M-295"]}
subjects:
  governs: "Implementation Retry Control"
  depends_on:
    - "Action"
    - "Operator"
    - "Implementation Process"
    - "Implementation Retry Limit"
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

1. resolve the effective Implementation Retry Limit under CA-M-295. **if** resolution fails, stop the retry decision **and** request Operator disposition.
2. **if** successful completion under CA-O-016 has been reached, stop **without** permitting another automatic repair retry.
3. **before** permitting a retry, check the applicable confidence threshold under CA-O-050, governing-Atom approval rules under CA-O-061, **and** **all** additional Operator constraints. an unmet gate requires the applicable earlier escalation even **when** retries remain; retry allowance does **not** create permission.
4. **if** failure remains **and** the consumed retry count has reached the effective Implementation Retry Limit, pause **and** report the remaining failures **to** the Operator.
5. **only** **when** failure remains, the gates permit recovery, **and** a retry remains, permit the next fix-and-evaluate retry through CA-O-016.

## accounting

- the initial failed Evaluation consumes **`=0`** retries.
- count **`=1`** retry **when** a permitted fix-and-evaluate round starts, **not** merely **when** its permission is checked. repeated gate checks **must not** double-count that round.
- retain the consumed count throughout the current execution. a changed failure set **or** an automatic next loop **must not** silently reset the budget.
