---
atom_id: CA-D-583
content_role: Delivery
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 10:07:12 +0000"
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
- the namespace contains its own database, worker lock, worker readiness, log, exact transport marker **and** private `health/requests/` and `health/replies/` Carriers.
- while holding the singleton worker lock, startup atomically publishes `worker.json` with exactly `pid`, lowercase-64-hex `start_token`, `application_version`, lowercase-64-hex `runtime_fingerprint` and `state: starting`; this state is not admitted. the health listener starts after DBOS initialization and before atomically publishing `worker.json` and `worker.ready` with those same five keys and `state: ready`. teardown stops and joins the listener before removing readiness.
- each health request and reply uses fixed `health/requests/<nonce>.json` and `health/replies/<nonce>.json` paths, where `nonce` is fresh lowercase-64-hex. both are atomic regular files no larger than 4096 bytes and have exactly `nonce`, `deadline_monotonic`, `pid`, `start_token`, `application_version`, `runtime_fingerprint` and `state`; `deadline_monotonic` is finite numeric monotonic time no later than request publication plus two seconds. symlinks, stale files and malformed content are rejected. request and reply bind the same seven values and `state: ready`.
- the channel permits at most 64 pending requests and fails closed beyond that bound. it is a private readiness Carrier only: it exposes no public Tool or HTTP endpoint and does not start workers, launch DBOS, schedule a Workflow, change a Queue, write Journal facts or execute effects.
- a per-Run binding carries the requested Run ID, frozen request digest **and** `release-host` transport identity.
- marker **and** binding publication are atomic; malformed, conflicting **or** symlinked state is rejected.
- the host scheduler has its own application **and** Queue identities. no existing Queue is copied **or** migrated.
- scheduler state remains transport evidence. actual Workflow, Step **and** Action facts remain in the existing canonical Journal.
