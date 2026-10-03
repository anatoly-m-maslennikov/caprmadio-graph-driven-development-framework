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
  governs: "GRAPH_UI/untrusted-content rendering"
  depends_on:
    - "Atom/Content Role: Implementation"
    - "Operator"
    - "Project"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"relates_to": ["CA-E-351", "CA-M-222", "CA-R-1076"]}
---
# Summary

Render untrusted Project content only as data

## Claim

GRAPH_UI **must** render untrusted Project content as inspectable data **without** executing that content **or** granting it additional capabilities.

the boundary applies **in** **every** supported output context, including text, markup, links, styles, **and** control characters. displaying a value **must not** let that value escape its context **or** become executable authority. CA-E-351 supplies the existing adversarial rendering check; the choice of safe rendering technique remains Method-owned.
