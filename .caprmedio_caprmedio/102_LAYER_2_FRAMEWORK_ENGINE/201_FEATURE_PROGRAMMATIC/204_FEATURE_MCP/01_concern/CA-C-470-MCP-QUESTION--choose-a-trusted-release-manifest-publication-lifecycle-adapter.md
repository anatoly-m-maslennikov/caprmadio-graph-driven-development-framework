---
atom_id: CA-C-470
content_role: Concern
type: Question
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:02:02 +0400"
subjects:
  governs: "MCP/Release manifest publication lifecycle adapter"
  depends_on: [MCP, Projection, Manifest, Operator, Journal, Runtime]
relations:
  concern_about: [CA-M-339, CA-E-582, CA-D-576]
---
# Summary

Choose a trusted lifecycle adapter for Release manifest publication

## Concern

The publisher currently accepts a lifecycle callback but no existing component can validate an Operator from `operators_registry`, bind that authorization to exact publication inputs, persist closed pre-effect evidence, and finalize canonical Journal evidence after interruption without introducing a Workflow Run or another ledger.

## Evidences

`release_manifest_publisher.py` delegates authorization and recording through an injected lifecycle callback. `direct_action_session.py` validates an Operator but creates Workflow-execution evidence and does not bind manifest publication inputs. `workflow_run_support.py` owns Workflow Run state. The existing Work Journal already supplies generic pending-event persistence and canonical `governed_project_state` and `governed_project_change` events, but callers must verify the physical carrier before finalizing a pending event.

## Blast Radius

Without a trusted adapter, a callback can self-grant publication or an interruption can leave replaced bytes with no truthful, resumable event evidence. Reusing Workflow Run support would wrongly create a second lifecycle authority for one MCP publication.

## Decision

Use one narrow MCP-owned `release_manifest_lifecycle.py` adapter. A trusted host constructs its context only after validating the named human Operator against `operators_registry`; its grant binds the Project root, observed manifest bytes, accepted source frontier, and candidate digest. The adapter seals the existing pending Journal intent before replacement and finalizes it only after exact target-byte inspection. It never replays an ambiguous mutation and does not create a Workflow, Workflow Run, Action Run, or ledger.
