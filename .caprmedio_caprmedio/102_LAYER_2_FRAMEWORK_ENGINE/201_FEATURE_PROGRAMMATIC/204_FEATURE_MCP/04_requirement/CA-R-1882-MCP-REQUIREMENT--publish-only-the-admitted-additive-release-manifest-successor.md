---
atom_id: CA-R-1882
content_role: Requirement
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 10:15:24 +0000"
subjects:
  governs: "MCP/selected Release manifest publisher"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1847, CA-R-1848, CA-D-572, CA-P-1622]
---
# Summary

Publish only the admitted additive Release manifest successor

## Scope

the Project-local MCP capability that initially publishes the admitted additive Release manifest and narrowly refreshes that same sixteen-route Projection after accepted Release source-pin changes.

## Claim

MCP **must** provide plan-first, Operator-authorized publication of the exact admitted additive Release manifest through **only** the initial fifteen-to-sixteen operation **or** a guarded refresh of its stale Release admission, preserving the existing routes, query admissions and selected-source registry authority.

## Details

1. initial publication requires the current canonical fifteen-route Manifest with no Release admission. it appends `release_version` and its current D572-defined admission, preserving the existing fifteen rows and query admissions.
2. refresh requires the canonical sixteen-route Manifest with the same current Release route and **=1** stale, schema-valid Release admission. all non-Release routes, query admissions, registry authority, binding reference and existing digests **must** validate. within the old Release admission, **only** Version and digest at legal definition-pin positions may differ from the current admission; Atom identities, source paths, fields, roles and ordered occurrences **must** match. a changed route or source identity requires separate admission, not this refresh.
3. refresh replaces **only** the Release admission with the current source-owned D572 value and recomputes the derived digests. it does not append or remove any route. a current admission with no drift is refused **before** effects.
4. normal discovery, dispatch and Manifest loading remain strict. the narrowly named refresh-input validator admits no dispatch and exposes no caller-selected loose mode.
5. planning writes nothing. execution requires a trusted, operation-specific Operator context sealed to the Project root, exact observed input bytes, current source frontier and exact candidate bytes. initial and refresh grants cannot substitute for each other.
6. the existing lifecycle adapter seals a pending intent, holds the canonical carrier lock through the final freshness check and atomic replacement, strictly reopens the output and finalizes the existing Journal event. recovery records **only** matching already-published candidate bytes; it never replays a replacement.
7. this private source-projection capability does not execute the Release Workflow or change installed runtime N. actual Release dispatch remains through MCP with its full gates. the canonical Applicable Methodology location remains unchanged.
