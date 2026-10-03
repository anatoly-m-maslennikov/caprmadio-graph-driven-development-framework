---
cce_version: cce_1
cce_form: concern_question
subjects:
  governs: "Atom/Content Role: Plan/Type: Task"
  depends_on:
    - "Operator"
    - "AI Agent"
    - "Actor"
    - "Atom"
    - "Artifact"
    - "Atom/Claim"
priority: medium
version: 2
updated_at: "2026-09-21 00:39:50 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
---
# Which unfinished session work requires a persisted Task?

which accepted persistence condition distinguishes session-only work from work that requires a persisted Task, **without** treating deferral, compaction, **or** session end as new mutation permission?

## Evidence

- the Operator explicitly permits ephemeral Tasks executed through proper Actions **and** Processes.
- CAPRMEDIO-META-REQU-145 distinguishes ephemeral session control from a persisted Plan Artifact.
- CAPRMEDIO-META-REQU-101 nevertheless requires a persisted Task Atom **before** a backlog candidate becomes active work.
- CAPRMEDIO-META-REQU-147 requires unfinished operative work **to** be reconciled into a governed Plan at deferral, blocking, topic change, compaction, session end, **or** partial completion.
- the active authority inspected does **not** supply the exact boundary that preserves these still-useful planning commitments **and** the accepted session-only case together.

## Principle check

CA-M-002 rejects duplicate plans; CA-M-005 rejects unnecessary compulsory artifacts; CA-R-1490 requires valuable information **to** remain recoverable; CA-R-1552 keeps mutation within active Operator delegation. none makes a session boundary itself permission **to** create a Task **or** permits losing valuable unfinished work.

## Disposition

preserve these source Claims **and** record the unresolved boundary rather than invent a mandatory Task, a new session Property, **or** an automatic persistence exception. obtain the missing policy decision **before** coordinated replacement; P Carriers remain outside this RMEDO repair frontier.
