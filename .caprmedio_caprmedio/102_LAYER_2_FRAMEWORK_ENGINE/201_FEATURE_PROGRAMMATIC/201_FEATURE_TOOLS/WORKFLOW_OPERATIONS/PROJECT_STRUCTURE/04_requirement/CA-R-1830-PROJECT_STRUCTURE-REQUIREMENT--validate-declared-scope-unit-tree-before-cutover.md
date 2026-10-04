---
atom_id: CA-R-1830
content_role: Requirement
type: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-04 23:02:03 +0400"
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

The Tool **must** reject a proposal unless its resulting declarations form a valid acyclic parent tree and satisfy every authoritative `[[scope_units]]` declaration field and its ordering, path, and inherited-authority constraints.

## Details

- Every resulting table has one nonempty canonical `scope_unit_name`, one nonempty canonical `scope_unit_label`, and a `parent`: `PROJECT` denotes the Project-level root, otherwise the parent resolves to one declared Scope Unit. Names are unique; no unit parents itself or an ancestor; `structural_level` is an integer equal to the parent depth from Project level zero.
- `scope_unit_type` is exactly `Ordered` or `Unordered`. `local_order` is required and unique among siblings only for `Ordered` units and forbidden for `Unordered` units. `navigational_order_number` is a required nonnegative integer for every unit; it is presentation data, may not determine parentage/type/local order, and is not required to be unique.
- `authority_path` and `delivery_path` are separately required, nonempty repository-relative directory paths with forward slashes; absolute, traversing, escaping, or cross-project-control-root paths are invalid. Existing folders, missing folders, and unlisted implementation paths are observations requiring disposition, never implicit declaration authority.
- `authority_mode`, when present, is exactly `strict` or `casual`; when absent, the assessment resolves and reports the value inherited from current Framework Instance Settings. Absence is not replaced by a copied default in the declaration.
- The assessment enumerates affected Scope Unit identities, incoming Atom/Goal/reference links, declared authority and delivery paths, observed Carrier paths, and effective authority mode. For Create or Move it also records the direct-parent Active Goal coverage disposition: present coverage, a named missing-coverage gap with its authorized disposition, or a blocking/Operator-decision state. A missing Goal neither establishes identity nor silently removes, invents, or universally rejects an otherwise admitted declaration.

## Source bindings

This validation is pinned to CA-O-012v5, CA-R-1484v5, CA-R-926v18, and CA-D-442v6; it is prepared by CA-O-140v2 and assessed before CA-O-141's accepted decision.
