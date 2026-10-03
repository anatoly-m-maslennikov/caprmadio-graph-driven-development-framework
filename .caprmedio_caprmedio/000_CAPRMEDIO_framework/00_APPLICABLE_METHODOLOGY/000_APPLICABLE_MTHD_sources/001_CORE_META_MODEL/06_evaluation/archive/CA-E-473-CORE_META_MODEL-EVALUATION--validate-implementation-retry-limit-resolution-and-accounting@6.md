---
version: 6
updated_at: "2026-09-22 14:41:44 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
    - CA-R-1488
    - CA-R-1489
    - CA-M-295
    - CA-D-447
    - CA-O-024
subjects:
  governs: "Implementation Retry Limit"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Implementation Retry Control"
    - "Implementation Workflow"
    - "Operator"
    - "Framework Instance Settings"
    - "Default Settings"
cce_version: cce_1
cce_form: evaluation
---
# Validate implementation retry-limit resolution and accounting

## test cases

1. provide distinct valid limits through direct Operator input, a Plan, nested Hubs, Framework Instance Settings, **and** Default Settings. successively omit higher-precedence values; check CA-M-295's precedence **and** nearest-Hub selection.
2. provide direct Operator input for one execution context **and** compare an unrelated execution. confirm that the input does **not** change the unrelated limit.
3. supply **`=0`** as an explicit higher-precedence value. confirm that it prevents retries **without** falling through **to** a nonzero lower-precedence value.
4. supply a negative, fractional, boolean, string, **or** ambiguous selected value; also omit **all** applicable values. confirm Operator escalation **without** an invented value **or** fallback past an invalid selected source.
5. omit Plan **and** Hub overrides, **then** change their inherited source. compare with an explicit override that previously equalled the inherited value; **only** the inheriting case follows the source change.
6. resolve the limit from the actual Default Settings Carrier **without** hard-coding its value **in** this Evaluation. confirm that the initial failed Evaluation consumes **`=0`** retries; **every** started fix-and-evaluate round consumes **`=1`** retry; repeated permission checks consume no additional retries; exhaustion prevents another retry **and** escalates.
7. change the failure set **or** revisit an Action. confirm that the consumed count is retained. an unmet confidence, approval, **or** permission gate **must** stop the retry even **when** allowance remains.


## Hub Carrier cases

- store explicit Hub limits **only** **in** the matching File Carrier of that same Plan under CA-D-447; a supplied file requires DoD.
- omit an inner Hub file **or** retry field while retaining a confidence field: inherit retry limits from the nearest outer explicit source.
- reject unrelated files, historical Revisions, duplicate Bundle identities, separate Objective overrides, **and** invalid reached sources **without** silent fallback.
- resolution **must not** create another Atom, settings file, **or** copied inherited override.

## acceptance criteria

**every** case **must** preserve the selected source, effective limit, inherited-versus-explicit distinction, **and** CA-O-024 accounting **without** changing source values **or** granting additional authority.

## failure disposition

stop the affected autonomous retry **and** report the failed condition **to** the Operator.
