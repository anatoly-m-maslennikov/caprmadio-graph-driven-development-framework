---
subjects:
  governs:
    continuant:
      - provenance
cce_version: cce_1
cce_form: obligation
version: 5
updated_at: 2026-08-30 16:44:07 +0400
---
# Preserve Git and Journal as independent provenance systems

PROGRAMMATIC MUST preserve Git and the Project Work Journal as two independent, intentionally redundant provenance and history systems. Git owns carrier bytes, tree state, commit identity, and ancestry. The Journal owns governed semantic action history, human-origin Initiative context, affected identities and revisions, and explicit cross-system bindings. Each committed Journal carrier revision is independently recoverable through Git, but neither system substitutes for the other.

One sealed action may pass through `git_complete_journal_pending`, `journal_recorded_git_pending`, and `reconciled`. A real-change commit MAY complete before its canonical Journal record is appended; a Journal record MAY be prepared before that commit, but its canonical binding is complete only once the exact reachable real-change commit SHA is known. `reconciled` requires exactly one canonical action record, exactly one reachable real-change commit binding, and a later separate Git commit that versions the Journal carrier containing that record. The Journal record does not embed the SHA of the Git commit that contains that same record: reconciliation derives that Journal-to-Git binding from the exact carrier revision and reachable Git history, avoiding a self-referential digest cycle.

MCP admission and mutation, including draft promotion, MUST NOT wait for reconciliation of the action they create. A later release, promotion-dependent action, or other governed reliance on that action's provenance MUST require `reconciled`; ordinary later real-change commits MAY continue while another action is pending. Reconciliation MUST detect and repair from sealed durable state, or explicitly block, a real-change commit without its Journal event, a Journal event without a reachable real-change commit, duplicate bindings, revision or digest mismatches, and Journal-carrier commit watermark lag.
