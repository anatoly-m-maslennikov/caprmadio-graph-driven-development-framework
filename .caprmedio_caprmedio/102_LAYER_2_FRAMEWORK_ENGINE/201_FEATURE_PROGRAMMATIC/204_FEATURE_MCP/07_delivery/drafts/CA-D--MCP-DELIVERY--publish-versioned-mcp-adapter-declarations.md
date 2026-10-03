---
content_role: Delivery
type: Delivery
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "MCP/adapter declaration Carrier"
  depends_on:
    - "Atom/Content Role: Implementation"
    - "Carrier"
    - "Tool"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1116"], "relates_to": ["CA-D-049", "CA-M-159", "CA-M-166", "CA-R-1111", "CA-R-1117", "CA-R-1118", "CA-R-1119"]}
---
# Summary

Publish versioned MCP adapter declarations

## Claim

an MCP adapter delivered within FRAMEWORK_ENGINE **must** carry a version-bound interface declaration at its declared MCP Delivery location.

- identify the supported protocol revision **and** admitted capability declarations owned by CA-R-1116; do **not** select another protocol revision here.
- bind the published request, response, **and** diagnostic representations **to** that interface version **and** the canonical Tool interfaces delegated **to** under CA-R-1111.
- represent admitted progress, cancellation, correlation, **and** resource-bound fields according **to** CA-R-1117 **and** preserve result meanings under CA-R-1119. this declaration does **not** redefine negotiation, scheduling, timeout, **or** failure behavior.
- represent authorization needs by non-secret references under CA-R-1118. credentials **must not** be embedded **in** the declaration, generated schemas, **or** published examples.

CA-D-049 owns the MCP Delivery binding; the version-bound declaration belongs **to** that adapter distribution rather than an independent FRAMEWORK_ENGINE-wide interface authority.
