---
atom_id: CA-D-576
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:18:46 +0400"
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

The publisher **must** use `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` as its only mutable carrier and return a source-bound plan or truthful execute result.

## Details

The input and output carrier is the same canonical JSON file: `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`. Its input has exactly fifteen route rows and no Release route; its admitted output has exactly sixteen route rows with one `release_version` row and one D572-defined `release_source_admissions` record. Existing route-row values and `query_source_admissions` are preserved. `source_freshness` preserves its selected-source fields and binding reference; only its selected-binding digest is recalculated through the existing binding-digest algorithm. The existing canonical-manifest-digest algorithm remains the only manifest-digest algorithm. The canonical compiled Methodology carrier is `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`; `.caprmedio_caprmedio/_projection/APPLICABLE_METHODOLOGY` is refused.

The publisher result contains the mode, observed input digest, proposed or published output digest, exact added route/admission identity, loader readback outcome, and safe shared lifecycle/recording references when execute was requested. Plan mode contains no effect or lifecycle record. An execute result cannot claim success without successful atomic replacement and exact loader readback. A recording-unavailable result preserves the observed publication/readback evidence and reports recording as required; it does not claim Release execution, runtime installation, image proof, or full-release acceptance.

The publisher has no delivery authority over source Atoms, D572, P1622, O164, the canonical compiled Methodology, Journal contents, runtime packages, Skills, containers, credentials, or queues. It never creates a second manifest, executor, Run writer, or Journal writer.
