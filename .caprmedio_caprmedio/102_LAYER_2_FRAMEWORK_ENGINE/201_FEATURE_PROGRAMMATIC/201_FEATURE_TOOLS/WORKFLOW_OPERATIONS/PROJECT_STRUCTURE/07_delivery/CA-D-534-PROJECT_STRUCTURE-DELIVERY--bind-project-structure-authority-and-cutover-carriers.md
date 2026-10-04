---
atom_id: CA-D-534
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:31 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE carrier boundaries"
  depends_on: [Tool, Scope Unit, Project Structure, Carrier, Journal]
relations:
  relates_to: [CA-R-1830, CA-R-1831]
---
# Summary

Bind PROJECT_STRUCTURE authority and cutover carriers

## Scope

Carrier placement and mutation boundaries for the reviewed structural Tool.

## Claim

Delivery **must** bind project structure declarations to the authoritative TOML and treat declared authority/delivery paths and filesystem observations as separate carriers.

## Details

- Only the selected TOML declaration delta and explicitly authorized reference/Carrier repairs are writable at cutover; implementation paths are reported as declared `delivery_path` values, not created or inferred by this Atom.
- The shared Events Journal remains the sole Run evidence source. This Delivery Atom carries references to its receipts, not a duplicate Journal format.
- A partial outcome records actual carrier changes and its authorized recovery boundary; it does not authorize broad deletion or unreported repair.
