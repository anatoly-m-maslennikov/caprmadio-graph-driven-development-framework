---
cce_version: cce_1
cce_form: method
subjects:
  governs: "provenance"
  depends_on:
    - "programmatic software"
version: 10
updated_at: 2026-09-01 02:40:00 +0400
relations:
  method_for:
    - CA-R-1095
  derived_from:
    - CA-A-058
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Reconcile independent Git and Journal provenance

## Applicable when

apply **after** a sealed programmatic action changes Git-governed carriers, creates
**or** prepares its Journal record, **or** requires provenance **before** later reliance.

## Procedure

1. preserve one sealed durable action state independently of Git **and** Journal
   writes.
2. record whether the action is `git_complete_journal_pending`,
   `journal_recorded_git_pending`, **or** `reconciled`; do **not** treat either pending
   state as provenance loss.
3. bind **=1** canonical Journal action record **to** **=1** reachable
   real-change commit once that commit SHA is known.
4. commit the Journal carrier later **in** a separate Git commit. derive the
   Journal-carrier binding from its exact revision **and** reachable history; do
   **not** embed the SHA of the commit that **contains** the same record.
5. reconcile missing counterparts, duplicate bindings, revision **or** digest
   mismatches, **and** Journal-carrier watermark lag from sealed durable state.
6. do **not** block the mutation that creates an action on its own reconciliation.
   Require `reconciled` **before** a later release, promotion-dependent action, **or**
   other governed reliance on that provenance.
7. return an explicit blocked state **when** deterministic repair cannot establish
   one canonical record **and** one reachable real-change commit.

## Outcome

Git **and** Journal remain independent provenance systems while **every** sealed action
converges **to** one recoverable cross-system binding **without** a digest cycle.

## Failure or stop

stop reliance on the affected provenance **when** the sealed state is absent,
multiple canonical records **or** commits remain, the commit is unreachable, **or**
revision **and** digest mismatches cannot be repaired deterministically.

## Sources

- [Git documentation: commits](https://git-scm.com/docs/git-commit)
- [NDJSON specification](https://github.com/ndjson/ndjson-spec)
- [CA-A-058 — Validate PROGRAMMATIC Method and Evaluation closure](../02_analysis/CA-A-058-PROGRAMMATIC-ANALYSIS_RPRT--validate-programmatic-method-and-evaluation-closure.md)
