---
atom_id: CA-E-400
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    continuant:
      - repository-reconciliation
    occurrent:
      - evaluation
  depends_on:
    continuant:
      - commit-automation
version: 1
updated_at: 2026-09-01 02:20:00 +0400
relations:
  evaluation_for:
    - CA-M-087
---
# Reconcile one missed external project change

## Claim checked

Repository reconciliation recovers one Git-admitted project change that has no
Codex Hook event without inventing session provenance or duplicating work.

## Test case

Create one admitted project change outside Codex Hook delivery, then run one
low-frequency reconciliation cycle twice against the resulting frontier.

## Acceptance criteria

Pass only when the first cycle creates one governed action, identifies
repository reconciliation as its observation source, advances the normal commit
pipeline once, and the second cycle produces no duplicate action.

## Failure disposition

Reject the reconciliation boundary when the change remains invisible, receives
invented Codex provenance, bypasses the normal pipeline, or is processed twice.

## Sources

- [Git documentation: porcelain v2](https://git-scm.com/docs/git-status#_porcelain_format_version_2)
- [CA-M-087 — Process one file change](../05_method/CA-M-087-TOOLS-CORE-IMPL_METHOD--process-one-file-change.md)
