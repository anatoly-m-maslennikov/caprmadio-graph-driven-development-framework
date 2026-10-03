---
subjects:
  governs: "scope-topology"
  depends_on: []
version: 9
updated_at: 2026-08-30 16:44:07 +0400
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Supply active TOOLS to MCP

TOOLS supplies MCP with the complete current set of active immediate Tool units **and** **every** Tool's machine-invocation contract. MCP **must** deterministically project **=1** callable endpoint for **every** valid active Tool, omit inactive **or** disabled Tools, report **every** invalid active Tool explicitly, **and** delegate execution **without** duplicating **or** changing Tool meaning **or** mechanics.
