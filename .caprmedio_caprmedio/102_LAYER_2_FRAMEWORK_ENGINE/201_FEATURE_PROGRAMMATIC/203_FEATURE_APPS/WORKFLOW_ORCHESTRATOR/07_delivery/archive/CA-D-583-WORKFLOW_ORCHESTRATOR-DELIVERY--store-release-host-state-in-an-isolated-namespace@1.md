---
atom_id: CA-D-583
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-06 01:01:23 +0000"
subjects:
  governs: "Release Version/Host Executor/Carrier"
  depends_on: [Carrier, Release Version, Workflow Run, Queue, DBOS, Journal, Implementation]
relations:
  delivery_for: [CA-R-1891, CA-M-347]
---
# Summary

store Release host state in an isolated namespace

## Scope

the Release Host Executor's scheduler **and** transport-state Carriers in WORKFLOW_ORCHESTRATOR.

## Claim

the Host Executor's mutable state Carriers **must** use `.caprmedio_install/workflow_orchestrator/release-host/`, separate from the native **and** Docker scheduler stores.

## Details

- the admitted runtime namespace value is `release-host`.
- the namespace contains its own database, worker lock, worker readiness, log **and** exact transport marker.
- a per-Run binding carries the requested Run ID, frozen request digest **and** `release-host` transport identity.
- marker **and** binding publication are atomic; malformed, conflicting **or** symlinked state is rejected.
- the host scheduler has its own application **and** Queue identities. no existing Queue is copied **or** migrated.
- scheduler state remains transport evidence. actual Workflow, Step **and** Action facts remain in the existing canonical Journal.
