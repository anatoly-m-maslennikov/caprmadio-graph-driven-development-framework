---
atom_id: CA-D-533
content_role: Delivery
type: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE request and result contract"
  depends_on: [Tool, Scope Unit, Project Structure, Implementation]
relations:
  relates_to: [CA-R-1829, CA-R-1832]
---
# Summary

Bind PROJECT_STRUCTURE Tool request and result

## Scope

The implementation-facing input/output boundary for one structural request; it does not designate an undeclared folder as a Scope Unit.

## Claim

Delivery **must** expose a typed request with `operation`, target identity, expected TOML revision, proposal delta, and optional authorized preservation/recovery disposition, and return the CA-R-1829/CA-R-1832 result envelope.

## Details

- The authoritative input carrier is `.caprmedio_caprmedio/project_structure.toml`; `authority_path`, `delivery_path`, and observed implementation/Carrier paths are separate output fields.
- The delivery result contains one of the declared outcome values, exact pre/post source revisions, affected/repaired/broken/preserved sets, actual effects, and available Run/Journal evidence references.
- The implementation path is to be bound by the implementation task only after independent RMED review; this Delivery Atom grants no write permission or code completion claim.
