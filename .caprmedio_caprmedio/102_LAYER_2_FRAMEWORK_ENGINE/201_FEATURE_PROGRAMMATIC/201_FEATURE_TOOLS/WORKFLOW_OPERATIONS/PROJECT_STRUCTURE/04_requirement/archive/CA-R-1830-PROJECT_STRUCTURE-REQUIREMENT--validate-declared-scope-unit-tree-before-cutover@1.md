---
atom_id: CA-R-1830
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 19:29:30 +0000"
subjects:
  governs: "Tool/PROJECT_STRUCTURE declaration validation"
  depends_on: [Tool, Scope Unit, Project Structure, Atom, Carrier]
relations:
  relates_to: [CA-R-1829, CA-O-012, CA-O-141]
---
# Summary

Validate declared Scope Unit tree before cutover

## Scope

Validation of the one proposed authoritative TOML tree delta selected by CA-O-139 and prepared by CA-O-140.

## Claim

The Tool **must** reject a proposal unless its resulting declarations form a valid acyclic parent tree and preserve the declared ordering and path constraints.

## Details

- Scope Unit identity is `scope_unit_name`; it is unique. Every non-root parent must resolve to a declared Scope Unit in the resulting tree; a unit cannot parent itself or any ancestor.
- `scope_unit_type` is exactly `Ordered` or `Unordered`. `local_order` is required and unique among siblings only for `Ordered` units, and is forbidden for `Unordered` units. `navigational_order_number` is presentation data and does not establish type or parent order.
- The resulting `authority_path` and `delivery_path` are explicit, nonempty, and reported separately. Existing folders, missing folders, and unlisted implementation paths are observations requiring disposition, never implicit declaration authority.
- The assessment enumerates affected Scope Unit identities, incoming Atom/Goal/reference links, declared authority paths, delivery/implementation paths, and observed Carrier paths. It reports unresolved or broken members rather than silently dropping them.
