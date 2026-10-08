---
atom_id: CA-D-576
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-05 18:02:02 +0400"
subjects:
  governs: "MCP/additive Release manifest publisher carriers"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1882, CA-M-339]
---
# Summary

Bind additive Release manifest publisher carriers

## Scope

The canonical input/output Projection, source inputs, and result evidence for the Release manifest publisher.

## Claim

The publisher **must** use `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` as its only mutable Project carrier and use one MCP-owned lifecycle adapter for trusted authorization, pending-intent recovery, and existing Work Journal evidence.

## Details

1. The input and output carrier is the same canonical JSON file: `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`. Its input has exactly fifteen route rows and no Release route; its admitted output has exactly sixteen route rows with one `release_version` row and one source-defined `release_source_admissions` record. Existing route-row values and `query_source_admissions` are preserved. `source_freshness` preserves its selected-source fields and binding reference; only its selected-binding digest is recalculated through the existing binding-digest algorithm. The existing canonical-manifest-digest algorithm remains the only manifest-digest algorithm. The canonical compiled Methodology carrier is `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`; `.caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY` is refused.
2. `release_manifest_lifecycle.py` is the one MCP-owned injected lifecycle adapter. A trusted host constructs its context after validating the human Operator against `operators_registry`; the context grants exact Project root, current manifest bytes, accepted source frontier, and candidate digest. The publisher accepts neither a caller boolean nor an arbitrary callback as authority.
3. The adapter uses the existing Work Journal pending mechanism to persist one closed publication intent before replacement. It uses existing generic `recovered` `governed_project_state` and `completed` `governed_project_change` events for prior-state and successor evidence. It verifies exact target bytes before finalizing pending evidence after a restart, does not replay an ambiguous replacement, and treats positive `result.version` as the Journal carrier-history revision rather than Atom or Projection metadata.
4. The publisher result contains the mode, observed input digest, proposed or published output digest, exact added route/admission identity, loader readback outcome, and safe lifecycle/recording reference when execute was requested. Plan mode contains no effect or lifecycle record. An execute result cannot claim success without successful atomic replacement, exact loader readback, and Journal finalization. A recording-unavailable or ambiguous result preserves the observed evidence and does not claim Release execution, runtime installation, image proof, or full-release acceptance.
5. The publisher has no delivery authority over source Atoms, current admission sources, O164, the canonical compiled Methodology, Journal contents outside the adapter's existing generic event API, runtime packages, Skills, containers, credentials, or queues. It never creates a second manifest, executor, Workflow Run writer, or lifecycle ledger.
