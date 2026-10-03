---
atom_id: CA-M-191
cce_version: cce_1
cce_form: method
subjects:
  governs:
    continuant:
      - programmatic-mutation
  depends_on:
    continuant:
      - programmatic software
version: 4
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1094
  derived_from:
    - CA-A-058
---
# Bind one programmatic mutation to its Initiative

## Applicable when

Apply before accepting or dispatching a programmatic mutation governed by
CA-R-1094.

## Procedure

1. Resolve or create exactly one sealed Initiative from the accepted human
   instruction. It may bind to a persisted Plan or Task or remain an ephemeral
   session task.
2. Assign one stable action identity and preserve a short instruction-derived
   summary plus enough structured context to identify the instruction.
3. Attach the Initiative and action identities before any Hook, queue, worker,
   retry, Git, Journal, or reconciliation handoff.
4. Propagate both identities unchanged through every handoff. A process,
   thread, adapter, queue, or worker identity may be linked as execution
   context but must not replace them.
5. Return an explicit blocked outcome before mutation when either identity is
   missing, ambiguous, changed, or bound to more than one Initiative.

## Outcome

Every accepted mutation remains attributable to one human-origin Initiative
and one stable action across asynchronous execution and provenance systems.

## Failure or stop

Stop before mutation when the Initiative is unsealed, the action identity is
absent or reused for another Initiative, or a handoff cannot preserve both
identities.

## Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
