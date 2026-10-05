---
atom_id: CA-C-450
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 00:41:45 +0000"
subjects:
  governs: "Discovery authority source selection"
  depends_on: [Atom, Carrier, Projection, Tool, MCP]
relations:
  concern_about: [CA-P-1605, CA-P-1527]
---
# Summary

Distinguish source authority from projected carriers in discovery

## Concern

Live Tool discovery returns no FIND_AND_FETCH declarations and reports widespread ambiguous Atom identities. The integration must distinguish actual authority from derived carriers without hiding genuine conflicting source declarations.

## Evidences

The connected MCP discover_tools request with query FIND_AND_FETCH returned total 0 and 1054 coverage issues. Issues include a CarrierError under _projection, ambiguous CA-O-159 and CA-O-162, and hundreds of source Atom identities also present in Applicable Methodology copies. The MCP process remains available with zero in-flight calls. This is observed discovery failure, not an assumed true source duplication or image-execution failure.

## Blast radius

P1527's actual discovery integration remains incomplete even though native query contracts pass. CA-P-1605 owns bounded diagnosis and necessary catalog source-selection repair. Host test environment C449 and denied carrier relocation C447 remain distinct blockers and are not bypassed.
