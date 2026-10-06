---
atom_id: CA-C-473
content_role: Concern
type: Question
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-05 17:43:28 +0000"
subjects:
  governs: "Release prerequisite worker compatibility"
  depends_on: [Operator, Runtime, Workflow Run, Implementation, Journal]
relations:
  concern_about: [CA-P-1714, CA-P-1624]
---
# Summary

Reconcile the existing worker before Release prerequisites

## Concern

How should the existing host Worker be reconciled with the current Implementation while preserving its older queued Workflow Run?

## Evidences

A foreground Worker start refused the held lock at repository-root `.caprmedio_install/workflow_orchestrator/worker.lock`. The lock holder is Python PID 61257. Its readiness Carrier contains only `ready`, and its metadata has no current version or fingerprint. DBOS records the older `base-revise-v2-coverage` registration rather than current `base-revise-v5-selected-v1-docker-project-mount`. Run `base-revise-replacements-20261004-0305` remains ENQUEUED for `base-revise-v3-replacements`. The permission profile denied process-command inspection.

## Blast radius

The current Build Applicable Methodology queue prerequisite and subsequent first Framework Runtime installation. Manifest publication and focused fixture tests are already complete and are not evidence of Worker compatibility.

## Decision

Preserve the existing Worker, database and queued Run. Admit no current compiler Run until the executing Worker's current application version and fingerprint are proved. A restart needs safe reconciliation of that exact existing process and queued intent; it must neither replay the old Run nor relabel it as executed under the current Implementation. No restart, cancellation, queue migration or permission bypass has occurred.
