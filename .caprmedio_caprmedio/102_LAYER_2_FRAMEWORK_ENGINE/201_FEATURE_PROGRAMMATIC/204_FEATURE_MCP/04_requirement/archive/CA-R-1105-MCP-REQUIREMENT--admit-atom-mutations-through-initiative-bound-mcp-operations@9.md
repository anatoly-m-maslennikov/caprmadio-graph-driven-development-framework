---
subjects:
  governs: "framework-engine-mcp"
  depends_on: []
cce_version: cce_1
cce_form: obligation
version: 9
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Admit Atom mutations through Initiative-bound MCP operations

Every CAPRMEDIO Markdown Atom mutation **must** enter through an authorized project-local MCP operation. MCP **must** identify the selected canonical Atom Tool, preserve the human-origin Initiative input **and** action request, **and** delegate **without** deciding the Atom operation's target set, preconditions, lifecycle meaning, mutation, recovery, **or** success state. The canonical Atom Tool owns those behaviors **and** seals one Initiative **and** stable action identity **before** its effect.

Search **and** read operations remain mutation-free. The canonical Tool for create, update, move, archive, promote, upgrade, replacement, **or** another atomic **or** bulk Atom operation **must** validate the current project frontier **and** **must** cause `COMMIT_TRIGGER` **to** receive durable intake acknowledgement **after** a successful mutation **and** **before** MCP reports success. MCP **may** return that Tool outcome but **must not** turn a failed, partial, blocked, **or** unacknowledged outcome into success.

An atomic operation selects exactly one Atom target. A bulk operation selects a finite target set of two **or** more Atom targets, freezes each target's identity, expected revision **or** digest, **and** canonical address **before** **any** write, **and** is all-or-nothing: **if** **any** target no longer satisfies its preconditions, it performs no target mutation **and** returns the exact per-target conflict result. A successful bulk operation neither widens nor silently replaces its sealed target set.

Multiple MCP service instances **and** sessions **may** operate concurrently. Every mutation of an existing Atom **must** carry its expected Atom Revision **or** carrier digest; a mismatch **must** reject that target rather than overwrite concurrent work. Promotion is an ordinary delegated Atom mutation that validates its pre-promotion input **and** seals a new action; it **must not** require the future Git **or** Journal reconciliation of that same new action. A direct **or** **otherwise** unowned Atom write outside this gateway is unadmitted **and** cannot be represented as a normal governed MCP mutation.
