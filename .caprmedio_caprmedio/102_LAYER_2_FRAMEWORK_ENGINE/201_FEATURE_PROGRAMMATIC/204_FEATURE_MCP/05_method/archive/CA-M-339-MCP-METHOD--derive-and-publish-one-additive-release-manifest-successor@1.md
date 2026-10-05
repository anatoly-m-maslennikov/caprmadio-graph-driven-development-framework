---
atom_id: CA-M-339
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:18:46 +0400"
subjects:
  governs: "MCP/selected Release manifest publication"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  method_for: [CA-R-1882]
---
# Summary

Derive and publish one additive Release manifest successor

## Scope

The deterministic plan and authorized publication of the one Release route manifest successor.

## Claim

The publisher **must** derive, verify, and publish the exact admitted sixteen-route successor only from the current canonical fifteen-route manifest and current D572 source admission.

## Details

1. Load `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` through the existing loader. Reject a missing, malformed, stale, noncanonical, or non-fifteen-route input, an existing `release_version` route, or changed selected-source/query-source admissions.
2. Reopen D572@5 and its accepted P1622@2 frontier. Derive only the D572-declared `release_version` route and one `release_source_admissions` record. Reuse D572's pinned current O164 Workflow, ordered Steps, ordered Actions, and Release RMED frontier without substitution or inference.
3. Copy every existing route row and `query_source_admissions` value unchanged. Preserve `source_freshness.selected_source_registry_ref`, `.selected_source_registry_version`, `.selected_source_registry_digest`, and `.selected_binding_ref`; update only `.selected_binding_digest` through the existing binding-digest calculation. Add the derived Release values, then compute the canonical manifest SHA-256 with its self field omitted from that digest computation.
4. In plan mode, return the input binding, proposed successor digest, exact added values, and no effect. In execute mode, require exact current Operator authorization and unchanged input bindings.
5. Write the complete successor to a same-directory temporary regular file, atomically replace only the canonical manifest file, and reopen the exact published bytes through the existing loader. Accept publication only when that loader discovers exactly sixteen routes and the one admitted Release record.
6. Delegate execute lifecycle and canonical recording to the existing MCP operation support. If a write, readback, or shared recording does not complete, return the actual blocked or partial state with available evidence; do not replay publication, dispatch O164, or create a second executor, Run writer, or Journal writer.
