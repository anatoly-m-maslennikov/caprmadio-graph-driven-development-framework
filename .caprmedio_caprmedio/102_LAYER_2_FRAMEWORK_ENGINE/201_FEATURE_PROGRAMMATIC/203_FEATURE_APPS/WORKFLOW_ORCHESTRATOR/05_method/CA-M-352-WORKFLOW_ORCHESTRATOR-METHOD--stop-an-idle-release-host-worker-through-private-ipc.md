---
atom_id: CA-M-352
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-07 13:56:09 +0000"
subjects:
  governs: "Release Version/Host Executor/Shutdown"
  depends_on: [Release Version, Workflow Run, Operator, Permission, Queue, DBOS, Carrier, Implementation]
relations:
  method_for: [CA-R-1896]
  relates_to: [CA-M-347, CA-D-583]
---
# Summary

stop an idle Release Host worker through private IPC

## Scope

the closed shutdown exchange and orderly termination of one explicit Release Host Executor.

## Claim

stop a Release Host worker only by matching its published ready identity through the private shutdown exchange, fencing an idle host Queue, and proving orderly termination before the requesting CLI reports `stopped`.

## Details

1. invoke the fixed host-local `stop-release-worker` command only for the release-host namespace. It reads the exact ready identity; it neither accepts a caller PID nor uses a signal, native/Docker transport or an arbitrary subprocess target. It uses the read-only health exchange only to authenticate matching ready and worker records through `probe_worker`, never to activate shutdown, and does not call `availability()` so current on-disk fingerprint drift cannot prevent management shutdown of the exact live worker.
2. atomically publish one request below the separate shutdown channel with a fresh lowercase-64-hex nonce and a finite monotonic deadline no later than thirty seconds after publication. Require the exact ready identity and reject a stale, malformed, oversized, symlinked, replayed or foreign carrier before any shutdown action.
3. the worker validates the exact request and, under one shared shutdown-admission fence also held by `enqueue_selected` and `recover_selected_release`, uses the public DBOSClient `list_workflows` API with statuses `[PENDING, ENQUEUED]`, release-host application and Queue identities, any application version, and bounded input/output loading. Any such host work, including active or conservatively unknown queued work, returns a closed busy refusal and leaves dispatch open; no DBOS cancellation or recovery is attempted.
4. only an idle fenced worker writes an `accepted` acknowledgement. `accepted` says only that orderly shutdown has begun; it is never a stopped receipt and permits no further dispatch.
5. after acceptance, atomically publish shutdown `state: stopping` metadata with the same identity, stop and join all private listeners, destroy DBOS, atomically replace it with `state: stopped`, then exit its foreground process. If listener join is unproven, preserve the stopping/unknown evidence, do not destroy DBOS and never publish stopped metadata. The requester waits for singleton-lock release, rechecks the stopped metadata, and only then writes and returns the final stopped receipt.
6. timeout or missing acknowledgement is a closed `pending` result after at most thirty seconds; a proved older unsupported protocol is `unsupported`. If acknowledgement was accepted but matching stopped metadata and singleton-lock release are not both proven by that deadline, return the same `pending` result without final receipt, retry or force. Do not fall back to a signal, PID liveness check, DBOS cancellation, recovery, new Run, replay, Journal gate or effect; upgrade the worker before retrying.
