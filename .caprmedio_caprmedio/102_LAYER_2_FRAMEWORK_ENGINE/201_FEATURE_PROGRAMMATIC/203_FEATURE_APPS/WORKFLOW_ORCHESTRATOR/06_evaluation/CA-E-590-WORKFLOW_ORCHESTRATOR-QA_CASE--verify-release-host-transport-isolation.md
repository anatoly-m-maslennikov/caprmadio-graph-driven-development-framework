---
atom_id: CA-E-590
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-07 10:07:12 +0000"
subjects:
  governs: "Release Version/Host Executor/Evaluation"
  depends_on: [Release Version, Workflow Run, Operator, Permission, Queue, DBOS, Source, Carrier, Journal, Implementation]
relations:
  evaluation_for: [CA-R-1891, CA-M-347, CA-D-583]
---
# Summary

verify Release host transport isolation

## Scope

admission, dispatch **and** observation of Release Runs through the isolated Host Executor.

## Claim

the Evaluation **must** verify that the Host Executor executes **only** its exactly bound, source-admitted Release Runs without changing another executor's Queue **or** adopting its Runs.

## Details

- preserve a queued native Base Revise Run **and** an existing Docker Queue while admitting a fresh Release host Run; check that **only** the host Queue changes.
- reject a non-Release request, foreign Run ID, changed request digest, stale Source pin, changed preview receipt **or** mismatched manifest **before** scheduler admission **or** effects.
- reject missing **or** mismatched host worker readiness without Docker **or** native fallback.
- verify ordinary host readiness only after a listener published under the held singleton lock answers one fresh lowercase-64-hex nonce within its two-second monotonic deadline. require an initial non-admitted `worker.json` with exactly `pid`, `start_token`, `application_version`, `runtime_fingerprint`, `state: starting`; after initialization require `worker.json` and `worker.ready` with the same five keys and `state: ready`.
- require each request and reply to have exactly `nonce`, `deadline_monotonic`, `pid`, `start_token`, `application_version`, `runtime_fingerprint` and `state`; require finite numeric monotonic deadline no later than publication plus two seconds and exact `ready` identity equality. prove a valid fresh handshake admits despite a sandbox-denied legacy signal observation.
- reject an absent listener, missing, expired, replayed or wrong nonce, wrong identity, changed runtime fingerprint, unknown key, payload above 4096 bytes, symlink or malformed private health carrier. verify refusal occurs before child launch, Queue change, DBOS Workflow, Journal fact or effect.
- submit 65 simultaneous private health requests and verify the 65th fails closed; verify at most 64 pending requests. verify listener startup precedes ready publication and teardown joins it before state removal.
- verify explicit worker startup creates no Run **and** host dispatch independently checks the frozen Release route **and** transport binding.
- verify status **and** recovery require the retained binding; they do **not** adopt an earlier direct-host **or** Docker Run.
- distinguish mock scheduler tests from the actual Release gates. Unit tests, image checks, host end-to-end tests **and** promotion require their own real bound evidence.
