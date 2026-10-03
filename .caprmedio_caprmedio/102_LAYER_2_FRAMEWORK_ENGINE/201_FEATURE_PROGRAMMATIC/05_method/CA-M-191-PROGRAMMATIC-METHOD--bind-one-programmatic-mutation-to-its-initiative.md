---
cce_version: cce_1
cce_form: method
subjects:
  governs: "programmatic-mutation"
  depends_on:
    - "programmatic software"
version: 11
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1094
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Bind one programmatic mutation to its Initiative

## Applicable when

apply **before** accepting **or** dispatching a programmatic mutation governed by
CA-R-1094.

## Procedure

1. resolve **or** create **=1** sealed Initiative from the accepted human
   instruction. it **may** bind **to** a persisted Plan **or** Task **or** remain an ephemeral
   session task.
2. assign one stable action identity **and** preserve a short instruction-derived
   summary plus enough structured context **to** identify the instruction.
3. attach the Initiative **and** action identities **before** **any** Hook, queue, worker,
   retry, Git, Journal, **or** reconciliation handoff.
4. propagate both identities unchanged through **every** handoff. a process,
   thread, adapter, queue, **or** worker identity **may** be linked as execution
   context but **must not** replace them.
5. return an explicit blocked outcome **before** mutation **when** either identity is
   missing, ambiguous, changed, **or** bound **to** more than one Initiative.

## Outcome

**every** accepted mutation remains attributable **to** one human-origin Initiative
**and** one stable action across asynchronous execution **and** provenance systems.

## Failure or stop

stop **before** mutation **when** the Initiative is unsealed, the action identity is
absent **or** reused for another Initiative, **or** a handoff cannot preserve both
identities.

## Sources

- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
