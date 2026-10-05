---
atom_id: CA-C-450
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: resolved
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-05 01:11:43 +0000"
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

P1527's actual discovery integration remains incomplete even though native query contracts pass. CA-P-1605 completed bounded diagnosis. Current source catalog already excludes projected carriers; CA-P-1607 supplies the missing query discovery bindings. Host test environment C449 and denied carrier relocation C447 remain distinct blockers and are not bypassed.

## Diagnosis

Current source and development-worker catalogs resolve CA-O-159 and CA-O-162 once from canonical sources and exclude their projected copies. The 9 focused catalog tests pass. The observed live MCP catalog differs from current source; no new catalog repair was warranted. Existing CA-D-551 and CA-D-557 lacked [tool_binding] tables, so native query implementations alone did not provide discoverable Tool declarations. P1607 authors those bindings; current live-generation acceptance is still pending and client schema refresh is unconfirmed.

## Resolution

Actual existing MCP reload receipt ca-p-1527-query-discovery-20261005 reports reloaded, registry_changed=true, notification sent and active generation 677e2f34b80b3f6aa3637dcedea7cd0b8af05b633666fdfe2ec632c5d0d727b6. Current live discover_tools with FIND_AND_FETCH and availability=mcp returns exactly FIND_AND_FETCH_ARTIFACTS and FIND_AND_FETCH_JOURNAL_EVENTS. Coverage diagnostics fall from1054 to49, with no _projection/CA-O-159/CA-O-162 ambiguity. The old process drains; the current process serves with zero in-flight calls. Client schema refresh remains unconfirmed, and no Workflow/image execution is implied. C451 owns the separate revised Artifact source-order/admission remainder; C447/C449 remain unchanged.
