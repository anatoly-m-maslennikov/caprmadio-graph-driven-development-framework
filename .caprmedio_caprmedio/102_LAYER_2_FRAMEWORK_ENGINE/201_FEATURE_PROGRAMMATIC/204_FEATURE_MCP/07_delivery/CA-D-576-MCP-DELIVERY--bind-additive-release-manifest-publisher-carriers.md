---
atom_id: CA-D-576
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-06 10:15:24 +0000"
subjects:
  governs: "MCP/additive Release manifest publisher carriers"
  depends_on: [MCP, Projection, Manifest, Workflow, Step, Action, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1882, CA-M-339]
---
# Summary

Bind additive Release manifest publisher carriers

## Scope

the canonical input/output Projection and trusted lifecycle carriers for initial additive Release publication and its narrow source-pin refresh.

## Claim

the publisher **must** use `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json` as its sole mutable Projection carrier and the existing MCP-owned lifecycle adapter for operation-specific authorization, pending-intent recovery and canonical Work Journal evidence.

## Details

1. initial input has fifteen routes and no Release admission; output has sixteen routes and **=1** source-defined Release admission. refresh input/output both have sixteen unchanged route rows. refresh replaces **only** a stale, schema-valid Release admission whose legal pin Versions/digests differ while identities, paths, schema and ordered structure still match current D572.
2. preserve `query_source_admissions` and selected-source registry fields and binding reference. use the existing algorithms for `selected_binding_digest` and `canonical_manifest_sha256`; do not create another Manifest or registry.
3. private entrypoints distinguish `plan_release_manifest_publish`/`publish_release_manifest` from `plan_release_manifest_refresh`/`refresh_release_manifest`. `authorize_operator_refresh` creates the refresh-specific trusted host context. `load_release_manifest_refresh_base` is the narrowly named pre-write input validator; the ordinary loader remains strict and is always used for published readback.
4. refresh plans, results and pending intent plans include `publication_operation: refresh`. initial plans retain their legacy schema without this member. existing `added_route` and `added_admission_route` fields identify `release_version` in both operations; the explicit refresh marker means replacement of its admission, not addition of a route.
5. the trusted context binds operation, registered Operator, root, exact input bytes, current source frontier and exact candidate bytes. the existing adapter stores the pending intent through the generic Work Journal, holds its carrier lock through final validation and replacement, and records recovered prior-state/completed change events with existing schema.
6. plan mode has no effect or lifecycle record. execute results contain observed input digest, candidate/published digest and actual readback/recording disposition. success requires exact atomic publication, strict readback and Journal finalization. interrupted or recording-required results retain exact evidence rather than claiming completion.
7. `recover_release_manifest_publish` remains a shared finalization-only entrypoint for a matching sealed initial or refresh intent. the operation marker is retained in refresh evidence; historical initial intent bytes and normalization remain valid. recovery has no replacement authority.
8. source Atoms, canonical Applicable Methodology, installed runtime N, Skills, containers, credentials and queues are not publication targets. Applicable Methodology remains at `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/`, not the obsolete extra Projection location.
