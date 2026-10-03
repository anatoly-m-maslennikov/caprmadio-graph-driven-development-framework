---
subjects:
  governs: "Atom/Content Role: Requirement"
  depends_on:
    - "Atom/Claim"
    - "Atom/Content Role"
    - "Atom/Content Role: Method"
    - "Atom/Content Role: Delivery"
    - "Atom/Content Role: Implementation"
    - "Atom/Content Role: Operations"
version: 21
updated_at: "2026-10-03 02:10:09 +0400"
relations: {}
atom_id: "CA-R-1694"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Requirement — Keep Requirements realization-agnostic

## Scope

Requirement claims and their internal realization.

## Claim

**every** Requirement **must** state its required outcome, obligation, permission, prohibition, **or** accepted external boundary **without** prescribing internal code **or** code organization merely as a construction choice.

- an accepted external interface, protocol, data shape, **or** host obligation **may** be required **when** conformance **to** that boundary is itself the required outcome. this does **not** prescribe an **otherwise** interchangeable internal realization.
- a programming language, library, algorithm, function, class, module, source-file organization, **or** another construction technique does **not** become a Requirement solely because it is normative; classify its primary contribution under CA-R-1531 **and** CA-R-1340.
- packaging, release, deployment, distribution, installation, migration, upgrade, **and** rollback are topics, **not** Content Role selectors. classify a Carrier representation **or** placement under CA-R-1342, reusable Action **or** Workflow behavior under CA-R-1530, **and** an actual realization under CA-R-1343. mentioning one of those topics does **not** turn a procedure into Delivery authority.
- a candidate that combines this independently replaceable outcome with an independently replaceable construction, Carrier, **or** operational Claim requires separate Atoms under the one-Claim authority; a composite Claim is **not** split merely because it has multiple clauses.

## Details

CA-R-1339 owns the Requirement Content Role definition. this Atom constrains realization prescription **without** duplicating the definitions of the other Content Roles.
