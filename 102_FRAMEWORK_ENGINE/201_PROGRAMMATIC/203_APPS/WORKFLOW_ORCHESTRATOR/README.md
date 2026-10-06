# Independent Workflow orchestrator

DBOS 2.31.1 schedules the existing **RMED Atoms Base Revise** Workflow.
Codex CLI is the initial replaceable Agent adapter. No other Workflow or harness
is silently assumed supported.

The optional [Docker runtime](docker/README.md) has an isolated Agent service,
explicit lifecycle commands, and its own persistent queue. The native adapter
instructions below remain separate; Docker does not alter host Codex permissions.

## Start the worker explicitly

From the repository root, install the declared runtime and start a detached worker:

```sh
uv run --group workflow-orchestrator python 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py --project-root "$PWD" start-worker
```

`start-worker` returns a PID and `starting`, not a claim that startup succeeded.
Check `.caprmedio_install/workflow_orchestrator/worker.log` and `worker.ready`.
The worker initializes the DBOS database. `worker` instead runs in the foreground.
No startup hook, auto-login service, listening port or automatic Run is installed.
The detached worker does not depend on the MCP or main session process lifetime.

Stop the particular PID returned by startup with SIGTERM. The foreground worker
also handles Ctrl-C. This is a trusted local service, not a multi-user RPC boundary.

## Release host worker

The isolated Docker worker deliberately has no host Docker client or socket.
For a source-admitted `release_version` selected Run that needs the host Release
gates, start the distinct host worker explicitly:

```sh
.caprmedio_runtime/host-tests/bin/python 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py --project-root "$PWD" start-release-worker
```

`start-release-worker` creates no Workflow Run. It starts only the dedicated
`release-host` DBOS application and publishes
`.caprmedio_install/workflow_orchestrator/release-host/transport.json`.
The host bridge requires that marker, its separate database, and matching
`worker.ready`; until all are present, selected Release admission fails closed.
It uses its own lock, log, queue, and per-Run immutable binding under
`.caprmedio_install/workflow_orchestrator/release-host/`; it neither imports nor
consumes native or Docker queue entries.

Only `enqueue_selected` requests whose sealed route is `release_version` can
select this transport. A bound Release Run's status and recovery remain on that
transport; a prior native or Docker Run is never adopted. Missing readiness or
binding does not fall back to either existing executor. The fixed host subprocess
sets its namespace only for itself and does not change the MCP process environment.

## Enqueue through MCP

Restart the MCP connection after updating the server. `workflow_orchestrator`
accepts this request shape:

```json
{
  "request": {
    "operation": "enqueue",
    "workflow_id": "CA-O-104",
    "run_id": "operator-chosen-run-id",
    "selection": [{"atom_id": "CA-R-1812", "path": "REPLACE_WITH_EXACT_SOURCE_PATH.md"}],
    "criteria_paths": ["REPLACE_WITH_CURRENT_RULE_PATH.md"],
    "author": "Anatoly Maslennikov",
    "journal_author": "anatoly-m-maslennikov",
    "scope": "WORKFLOW_ORCHESTRATOR",
    "confidence_threshold": 90.0,
    "allow_fixes": false,
    "allow_replacements": false,
    "agent_timeout_seconds": 600
  }
}
```

Paths in this example are placeholders; do not submit it unchanged. Selection and
criteria are explicit and frozen at admission. The existing Journal uses GitHub
usernames; `journal_author` is its compatibility Carrier, separate from the named
registered Operator. The caller must supply its truthful Journal identity.

Include the actual Operator registry, Project structure, and applicable Content
Role/Type Status declarations in `criteria_paths`, alongside the checking rules.
Their contents and hashes are bound and supplied to both reviewer and fixer;
examples in other Atoms do not establish registry membership or Status admission.
The check prompt provides the report layout and canonical per-check statuses:
`passed`, `failed`, `blocked`, `pending`. Findings use `id`; dispositions reference
that identity through `finding_id` or a zero-based `finding_index`. Raw malformed
results are rejected, not silently counted as completed checks.

For command-line admission, save the request object **without** the outer `request`
key, then use `--input REQUEST.json enqueue`. `status` accepts `run_id`.

The existing `get_execution_status`, `watch_execution`, and saved Markdown reports
observe execution. Scheduler success means the orchestrator returned; its result
may still be `interrupted`. Atom completion uses the existing Workflow predicates.

## Authority and recovery

The worker performs gather → check → fix. There is no recheck phase.
Coverage Gates follow each main phase and require 100% accounting of the explicit
selection, concluded checks, and finding dispositions. Incomplete coverage returns
`interrupted`, `coverage_gates`, and `operator_question` through status; the caller
presents the question to the Operator. Gates use saved evidence, not more Agent calls.
They are recorded in the existing Journal and full report, with no retry loop.

Native checks use
fresh read-only Codex CLI sessions; Docker uses its separate mount-isolated Agent.
Fix Agents return proposals; they do not edit
the Project. `allow_fixes: true` delegates selected same-identity,
same-Summary, same-Version corrections. Separately, `allow_replacements: true`
delegates Summary-changing replacement of selected Atoms: reserve a new Atom ID,
publish its complete candidate as Version 1, archive the predecessor, and record
both Carriers and confirmed shared-Journal receipts. The flag defaults to false
and requires `allow_fixes: true`. It does not authorize editing other Atoms or
asserting a post-fix semantic pass. Version-changing same-identity fixes still
require a governed history transition and pause without overwriting the source.
Undelegated replacement, retirement, stale authority, low confidence
or incomplete evidence interrupts the Run for Operator action.

Before an edit, the worker retains accepted output and checks source hashes. A
restarted worker acknowledges already-applied candidate bytes instead of applying
them again. Dispatch intent without accepted output is uncertain and is not
silently retried. Terminal Runs remain immutable; reconcile and authorize a new
Run where needed.

Replacement plans reserve the successor ID before mutation, record the original
state, and publish complete files without overwriting destinations. Recovery
reuses the saved ID and hashes; conflicting bytes interrupt rather than overwrite.
After changing executor code, explicitly restart the worker as well as reloading
the MCP implementation. MCP hot reload does not refresh the separate worker.
Enqueued Runs are pinned to the replacement-capable worker version, so an older
worker cannot consume requests containing the new permission.

Persistent SQLite/dispatch state is under `.caprmedio_install/workflow_orchestrator/`;
it is ignored by Git, not an Atom source or a replacement for the shared Journal.
Existing reports remain at `tmp/RMED Atoms Base Revise/<run_id>.md`.

Codex authentication must already be available. The adapter uses `codex exec`,
`--ephemeral`, `--ignore-user-config`, `--sandbox read-only` and `--output-schema`.
Each dispatch sets `sqlite_home` and `log_dir` to its own `codex-state/` and
`codex-logs/` directories. Authentication stays in the existing Codex home;
no credentials are copied and no global Codex configuration is changed.
It does not inherit user MCP registrations, shell hooks or broad execution settings.
CLI defaults select the model; later harness adapters can implement the same interface.

Start the worker from your regular Terminal when the calling session's sandbox
blocks Codex initialization or inference network access. A detached process retains
its launch restrictions; detaching it does not grant additional permissions.
Coverage interruption reports the original Action failure alongside the missing
work, with detailed diagnostics confined to the dispatch's local `stderr.log`.

## Tests

```sh
uv run --group workflow-orchestrator python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests
```

Tests use mock Agents and an actual DBOS SQLite queue, including separate client
and worker processes. They do not call a paid model or prove semantic judgment.
