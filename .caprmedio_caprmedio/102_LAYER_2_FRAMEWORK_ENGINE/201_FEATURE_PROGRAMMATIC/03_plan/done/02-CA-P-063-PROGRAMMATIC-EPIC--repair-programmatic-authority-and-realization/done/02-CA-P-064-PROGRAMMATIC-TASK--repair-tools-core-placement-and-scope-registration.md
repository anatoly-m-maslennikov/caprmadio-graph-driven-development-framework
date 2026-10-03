---
cce_version: cce_1
cce_form: obligation
subjects:
  - scope-topology
  - local-tier
  - tool-authority
version: 2
updated_at: 2026-08-23 15:25:06
autonomous_confidence_threshold: 98
---
# Repair TOOLS Core placement and Scope Unit registration

THE Assignee MUST make the active TOOLS Core Requirement carriers and the PROGRAMMATIC Scope Unit registrations express their actual owning Scope Units and canonical authority locations.

## Scope

`(Atom ID IN (CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology, CA-R-1084, CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope, CA-R-1048, CA-R-1049, CA-D-251, CA-D-025))`

## Definition of Done

THE Task is NOT DONE IF (ANY active TOOLS Core Requirement is carried by a descendant Tool Scope Unit OR ANY affected Scope Unit has a missing, duplicated, or contradictory registration OR ANY affected authority or Delivery path disagrees with structural ownership OR the exact Task Scope Resolution and validation result are not recorded).

## Details

Include `CA-R-1048`, `CA-R-1049`, the registrations for `PROGRAMMATIC` and `TOOLS`, and the directly affected Delivery-place bindings. Preserve Tool behavior claims while repairing only ownership, placement, Tier, and registration authority.

`CA-P-062` remains an independently admitted deferred BSEED Plan, not an execution dependency for this Task, under the Operator instruction to execute Tasks 2–7 sequentially.

## Task Scope Resolution

Project revision: Git `a3d2bcb4e37012bb8309a63741919ba8217b74e9`.

Frozen at: `2026-08-23 15:25:06 +04`.

The Task selector produced the following exact active Carrier set:

- `CA-R-1084-FR_ENGN-CORE-REQUIREMENT--define-programmatic-feature-scope` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/04_requirement/CA-R-1084-FR_ENGN-CORE-REQUIREMENT--define-programmatic-feature-scope.md` — `125b6fcee1ac0900db1de101480bff7b1b8a3e5b0d316bf6537061209ef8e09d`
- `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/04_requirement/CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope.md` — `9bc089ed9020921a466baee4017e630ef573a7c658cf32ea5659f21c79a58b02`
- `CA-R-1048-TOOLS-CORE-REQUIREMENT--migrate-one-sealed-atom-identity` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/MIGRATE_ATOM_IDENTITY/04_requirement/CA-R-1048-TOOLS-CORE-REQUIREMENT--migrate-one-sealed-atom-identity.md` — `bcbbecc1095a611c2b00927493c1c1e6902e004e0479f7fd77b9def269775ecc`
- `CA-R-1049-TOOLS-CORE-REQUIREMENT--rebind-one-active-atom-relation-set` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/REBIND_ATOM_RELATIONS/04_requirement/CA-R-1049-TOOLS-CORE-REQUIREMENT--rebind-one-active-atom-relation-set.md` — `0e0f5cfed1d56009cdbd2c6dc4e239a38217e8d579f432672f0ac32fda492c24`
- `CA-D-251-DELIVERY-PROGRAMMATIC--bind-programmatic-delivery-place` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/07_delivery/CA-D-251-DELIVERY-PROGRAMMATIC--bind-programmatic-delivery-place.md` — `eb0e16f879f98e5fa40452f000ab602c86bce964bfbcc1618dc5cd93f88a48ae`
- `CA-D-025-DELIVERY-TOOLS--bind-tools-delivery-place` — `.caprmedio/102_PROJECT_LAYER_2_FRAMEWORK_ENGINE/PROGRAMMATIC/TOOLS/07_delivery/CA-D-025-DELIVERY-TOOLS--bind-tools-delivery-place.md` — `24233b3f6b5b2f4960e18f40bc54dc56a04b63bec7ea189a8b40fb08922c6753`

`CAPRMEDIO-FRAMEWORK-ENGINE-REQU-700--define-framework-engine-feature-topology` has no active Carrier in the Task Scope. Its stale relation references are not changed by this Task and remain in the later cross-scope relation repair.

The `CA-R-1084` selector is resolved to the exact `FR_ENGN` Carrier above; the distinct BSEED Metamodel Carrier with the same short numeric token is outside this Task Scope.

## Execution Result

`CA-R-1048` and `CA-R-1049` moved from their descendant Tool Scope Units to the direct `TOOLS/04_requirement/` Current Scope. Each preserved its behavior claim and exact predecessor Carrier in its original local `archive/`, then advanced from version `1` to version `2` because the Current Scope and Local Tier changed.

`CA-R-1084` remains in `FRAMEWORK_ENGINE/04_requirement/`: it defines the non-Project `PROGRAMMATIC` Goal Claim Scope from that Scope Unit's direct parent. `CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702` remains in `PROGRAMMATIC/04_requirement/`: it defines the immediate `TOOLS` child Scope Unit.

`CA-D-251` binds `PROGRAMMATIC` relative to `FRAMEWORK_ENGINE` as `PROGRAMMATIC` for both authority and Delivery. `CA-D-025` binds `TOOLS` relative to `PROGRAMMATIC` as `TOOLS` for both authority and Delivery. Both bindings already match the materialized authority and Delivery directories, so neither needed a new Revision.

## Validation Result

PASS.

- Each active TOOLS Core Requirement in the Task Scope is directly carried by `PROGRAMMATIC/TOOLS/04_requirement/`, not by a descendant Tool Scope Unit.
- `PROGRAMMATIC` is the immediate unordered child of `FRAMEWORK_ENGINE`; `TOOLS` is its immediate unordered child at Structural level 3.
- The two Scope Unit Requirements and two Delivery bindings agree with those parent-relative authority and Delivery paths.
- Each moved Core Requirement has exactly one archived v1 predecessor and one active v2 Carrier with unchanged Markdown claim text.
