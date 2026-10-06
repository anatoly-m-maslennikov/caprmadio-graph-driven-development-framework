---
atom_id: CA-M-339
content_role: Method
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 18:02:02 +0400"
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

The publisher **must** derive and publish the exact admitted sixteen-route successor only through a trusted MCP lifecycle adapter that binds authorization, a closed publication intent, and canonical Journal evidence to the current canonical fifteen-route manifest and current D572 source admission.

## Details

1. Load `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` through the existing loader. Reject a missing, malformed, stale, noncanonical, or non-fifteen-route input, an existing `release_version` route, or changed selected-source/query-source admissions.
2. Derive only the current D572-declared `release_version` route and one `release_source_admissions` record through the source-owned admission parser. Reuse its accepted current frontier without copying stale literals, substitution, or inference.
3. Copy every existing route row and `query_source_admissions` value unchanged. Preserve `source_freshness.selected_source_registry_ref`, `.selected_source_registry_version`, `.selected_source_registry_digest`, and `.selected_binding_ref`; update only `.selected_binding_digest` through the existing binding-digest calculation. Add the derived Release values, then compute the canonical manifest SHA-256 with its self field omitted from that digest computation.
4. In plan mode, return the input binding, proposed successor digest, exact added values, and no effect. In execute mode, admit only a trusted host-created lifecycle context: it validates the named human Operator against `operators_registry`, and its grant binds the Project root, current manifest bytes, accepted source frontier, and candidate digest. A caller-supplied boolean, callback, or lifecycle record is not authorization.
5. Before replacement, the adapter seals and stores one closed publication intent through the existing Work Journal pending mechanism. The intent fixes the input and candidate digests, target carrier, human author, source frontier, and the exact Journal event payload; it is not a new Workflow, Run, or ledger.
6. Write the complete successor to a same-directory temporary regular file, atomically replace only the canonical manifest file, and reopen the exact published bytes through the existing loader. Accept publication only when that loader discovers exactly sixteen routes and the one admitted Release record.
7. The adapter records the prior state as existing recovered `governed_project_state` evidence when necessary, then records the successor as existing completed `governed_project_change` evidence linked to that prior event. The positive Journal `result.version` is the event-history carrier revision, not an Atom Version or Projection metadata; the projection itself remains versionless and has its completed-rebuild `updated_at`.
8. On restart or recording failure, inspect the exact target bytes before finalizing the sealed intent. If they match its candidate digest, finalize the exact pending Journal event without repeating the replacement. If they do not match, retain the evidence and report an ambiguous state; never replay an ambiguous mutation. The publisher itself does not write the Journal, dispatch O164, or create a second executor, Run writer, or Journal writer.
