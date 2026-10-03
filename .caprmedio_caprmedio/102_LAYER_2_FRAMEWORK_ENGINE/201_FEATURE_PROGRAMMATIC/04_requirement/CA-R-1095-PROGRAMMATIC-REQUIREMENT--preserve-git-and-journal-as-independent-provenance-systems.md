---
subjects:
  governs: "provenance"
  depends_on: []
cce_version: cce_1
cce_form: obligation
version: 9
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve Git and Journal as independent provenance systems

PROGRAMMATIC **must** preserve Git **and** the Project Work Journal as two independent, intentionally redundant provenance **and** history systems. Git owns carrier bytes, tree state, commit identity, **and** ancestry. The Journal owns governed semantic action history, human-origin Initiative context, affected identities **and** revisions, **and** explicit cross-system bindings. **every** committed Journal carrier revision is independently recoverable through Git, but neither system substitutes for the other.

One sealed action **may** pass through `git_complete_journal_pending`, `journal_recorded_git_pending`, **and** `reconciled`. A real-change commit **may** complete **before** its canonical Journal record is appended; a Journal record **may** be prepared **before** that commit, but its canonical binding is complete **only** once the exact reachable real-change commit SHA is known. `reconciled` requires **=1** canonical action record, **=1** reachable real-change commit binding, **and** a later separate Git commit that versions the Journal carrier containing that record. The Journal record does **not** embed the SHA of the Git commit that **contains** that same record: reconciliation derives that Journal-to-Git binding from the exact carrier revision **and** reachable Git history, avoiding a self-referential digest cycle.

MCP admission **and** mutation, including draft promotion, **must not** wait for reconciliation of the action they create. A later release, promotion-dependent action, **or** other governed reliance on that action's provenance **must** require `reconciled`; ordinary later real-change commits **may** continue while another action is pending. Reconciliation **must** detect **and** repair from sealed durable state, **or** explicitly block, a real-change commit **without** its Journal event, a Journal event **without** a reachable real-change commit, duplicate bindings, revision **or** digest mismatches, **and** Journal-carrier commit watermark lag.
