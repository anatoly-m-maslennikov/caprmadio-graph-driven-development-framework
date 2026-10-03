---
subjects:
  - provenance
cce_version: cce_1
cce_form: obligation
version: 2
updated_at: 2026-08-23 15:33:04 +0400
---
# Preserve Git and Journal as independent provenance systems

PROGRAMMATIC MUST preserve Git and the Project Work Journal as two independent, intentionally redundant provenance and history systems. Git owns carrier bytes, tree state, commit identity, and ancestry. The Journal owns governed semantic action history, Initiative context, affected identities and revisions, and explicit cross-system bindings. Journal carriers are themselves versioned through Git, so Journal provenance flows into Git without making one system a substitute for the other.

A successful real-change commit MAY temporarily establish `git_complete_journal_pending`; later canonical Journal append and Journal-only Git commit establish `reconciled`. Programmatic release, promotion, or other governed reliance on that action MUST require `reconciled`, while ordinary later real-change commits MAY continue during the pending interval. Reconciliation MUST detect and repair or explicitly block a real-change commit without its Journal event, a Journal event without a reachable real-change commit, duplicate bindings, digest mismatches, and Journal-batch watermark lag.
