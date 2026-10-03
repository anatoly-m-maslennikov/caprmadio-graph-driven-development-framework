---
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Draft
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Tool/result envelope Carrier"
  depends_on:
    - "Carrier"
    - "Operator"
    - "Tool"
    - "compatibility-boundary"
version: 1
updated_at: "2026-09-23 19:20:45 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {"delivery_for": ["CA-R-1064"], "relates_to": ["CA-D-025", "CA-M-159", "CA-M-166"]}
---
# Summary

Serialize versioned Tool result envelopes

## Claim

the machine-readable output Carrier of a public Tool command **must** use a schema-versioned result envelope under the common CLI contract of CA-R-1064.

- represent capability **and** invocation identities, execution mode, completion outcome, result data, **and** diagnostics as distinguishable fields rather than one unstructured message.
- identify the envelope schema version **and** its declared interface boundary. map the command's governed exit outcome **without** selecting another exit-status policy **in** this Delivery.
- derive concise human explanations from the same result **without** changing its machine meaning **or** making free-form explanation the authoritative result.
- publish the schema alongside the declared Tool interface under CA-D-025. changes **must** be represented through the compatibility boundary governed by CA-M-166, **not** through a second independent version policy.
