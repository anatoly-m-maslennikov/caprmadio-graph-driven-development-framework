---
atom_id: CA-C-441
content_role: Concern
type: Problem
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 22:09:50 +0000"
subjects:
  governs: "Prove query fixtures and consumption truth"
  depends_on: [Journal, Projection, Evaluation, Implementation]
relations:
  concern_about: [CA-P-1525, CA-P-1526, CA-P-1544, CA-P-1546, CA-P-1547, CA-P-1548]
---
# Summary

Prove query fixtures and consumption truth

## Concern

The Artifact golden corpus omits the same-spelling frontmatter/section namespace case; Journal token consumption reports UTF-8 bytes instead of parser tokens, and several required diagnostic/security fixtures are absent.

## Evidences

CA-P-1544 maps the missing cases to E569/E575/E577/E579. A three-token expression is reported as thirty bytes. CA-P-1546/1548 and the Journal repair own the bounded fixes; shared Run/E580 remains a separate integration gate.

## Blast radius

Neither query Tool is admitted to MCP until its current repair and independent acceptance gates are satisfied. No source write, real Run, image or aggregate Epic completion is inferred from the initial passing unit suites.

