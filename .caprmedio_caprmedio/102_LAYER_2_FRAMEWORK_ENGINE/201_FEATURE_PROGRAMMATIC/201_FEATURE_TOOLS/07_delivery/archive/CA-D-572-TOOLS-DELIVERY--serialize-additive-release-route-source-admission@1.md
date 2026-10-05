---
atom_id: CA-D-572
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 08:12:00 +0400"
subjects:
  governs: "Tool/RELEASE_VERSION/Additive selected-route source admission"
  depends_on: [Tool, Workflow, Action, Manifest, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1876, CA-R-1877, CA-R-1878, CA-R-1879, CA-M-331, CA-M-332]
---
# Summary

Serialize additive Release route source admission

## Scope

The one Release Version source-admission record which a successor canonical selected-workflow manifest needs before admitting `release_version`.

## Claim

A successor of `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` **must** admit `release_version` only through one `release_source_admissions` record carrying CA-P-1622@1 at `.caprmedio_caprmedio/03_plan/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/10-CA-P-1620-TASK--deliver-release-version-workflow/02-CA-P-1622-TASK--review-release-version-source-and-admission.md`, SHA-256 `8f5c04c5f850d37ce30fe259f3d0b80c7794d6230c3aec2cffe81c0b229bb578`, and exact current O164–O179 source pins with the accepted Release RMED frontier.

## Details

The record has route `release_version`; an `acceptance_frontier` object with that CA-P-1622 identity, version, safe path, and digest; one Workflow pin CA-O-164@2; ordered Step/Action pins CA-O-170/CA-O-165, CA-O-171/CA-O-165, CA-O-172/CA-O-166, CA-O-173/CA-O-166, CA-O-174/CA-O-168, CA-O-175/CA-O-167, CA-O-176/CA-O-168, CA-O-177/CA-O-168, CA-O-178/CA-O-169, and CA-O-179/CA-O-169; and the independent accepted Release RMED frontier of CA-R-1876 through CA-R-1880, CA-M-331 through CA-M-333, CA-E-571 through CA-E-574, and CA-D-560 through CA-D-567. Every pin is an Atom ID, positive Version, safe source path, and lowercase SHA-256 from the actual accepted source; D572 never pins itself. Duplicate, absent, stale, malformed, or digest-mismatched members reject before shared support.

The record is an additive source-admission serialization, not a new registry, Workflow graph, executor, permission, generic effect schema, or dispatch result. It preserves the original thirteen CA-A-1142@2 entries and the two query admissions unchanged. It is consumed only as part of one outer D527 `definition_manifest`, and explicit current route-bound Operator authorization plus D527 preview/currentness rechecks remain required for `execute`. It does not itself create a Run, queue intent, Journal Event, compiler result, package effect, or release completion.
