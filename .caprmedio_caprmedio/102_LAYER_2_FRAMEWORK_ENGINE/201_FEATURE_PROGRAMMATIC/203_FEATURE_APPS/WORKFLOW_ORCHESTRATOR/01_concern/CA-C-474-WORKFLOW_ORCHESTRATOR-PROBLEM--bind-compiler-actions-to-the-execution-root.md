---
atom_id: CA-C-474
content_role: Concern
type: Problem
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 18:22:01 +0000"
subjects:
  governs: "Compiler Action execution-root binding"
  depends_on: [Runtime, Workflow Run, Action, Project, Journal]
relations:
  concern_about: [CA-P-1714, CA-P-1624]
---
# Summary

Bind compiler Actions to the execution root

## Concern

The selected compiler adapter passes the frozen host Project root unchanged into an Action running in Docker, instead of using its trusted execution-visible Project root.

## Evidences

Run release-methodology-reconcile-20261005-1805 has DBOS scheduler status SUCCESS but its governed Workflow, first Step and first Action ended interrupted_pending. CA-O-004 reported request-project-root-invalid for /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework, while the Docker worker runs with Project root /project. The Action, Step and Workflow Journal records have empty effect references. No compiler publication receipt exists.

## Blast radius

Build Applicable Methodology through the selected Docker transport, and the fresh compiled-methodology prerequisite for first Framework N installation. This failure does not invalidate the already published sixteen-route manifest.

## Disposition

Repair the adapter by copying frozen parameters and replacing only project_root with the trusted executor context root. Preserve governed bindings and every other admitted parameter. Add host-versus-Docker regression tests before acceptance. Preserve the original interrupted Run; after the repaired runtime is loaded, submit a fresh normally admitted Run rather than replaying this one.
