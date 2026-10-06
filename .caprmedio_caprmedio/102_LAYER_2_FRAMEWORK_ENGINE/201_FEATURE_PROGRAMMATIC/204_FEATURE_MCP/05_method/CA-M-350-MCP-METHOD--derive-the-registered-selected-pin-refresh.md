---
atom_id: CA-M-350
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 17:27:56 +0000"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Atom, Source Carrier]
relations:
  relates_to: [CA-P-1800, CA-D-588]
---
# Summary

Derive the registered selected pin refresh

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

**to** refresh the accepted selected source revision, derive the successor from the exact prior binding and the current registered source before applying the existing authorized publication lifecycle.

## Details

1. reopen the one CA-D-588-MCP-DELIVERY--register-the-prepared-successor-binding-refresh registration and its exact input binding, current sources and retained prior source bytes.
2. replace **only** its declared pin occurrences; verify their count and route ownership. retain every other field except the resulting binding and canonical digests.
3. validate the whole successor against current source pins and the existing selected-route schema. reject changes beyond the registration before writes.
4. seal the exact derived candidate under the existing trusted Operator context. rederive before intent and publication; record the actual write and exact-byte readback through the existing lifecycle.
5. retain pending publication or recording evidence for recovery. historical evidence and installed runtime remain unchanged.

