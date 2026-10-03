---
content_role: Requirement
type: Requirement
current_scope_unit: GRAPH_UI
claim_target_scope_unit: GRAPH_UI
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "GRAPH_UI/keyboard interaction"
  depends_on:
    - "Atom/Content Role: Evaluation"
    - "Operator"
    - "Workflow"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-E-349", "CA-R-1076", "CA-R-1604", "CA-R-819"]}
---
# Summary

Make primary interface workflows keyboard-operable

## Claim

GRAPH_UI **must** make **every** primary Operator workflow usable by keyboard **without** requiring a pointer-only interaction.

the supported interaction boundary includes visible focus, understandable control names **and** roles, predictable traversal, perceivable status changes, **and** reachable error recovery under CA-E-349. this Requirement governs the optional GRAPH_UI; it does **not** make that interface a prerequisite for GRAPH_SERVER, Tools, **or** MCP.
