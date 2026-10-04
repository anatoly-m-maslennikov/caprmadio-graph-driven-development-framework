# CAPRMEDIO workflow MCP — first local slice

Exposes caller-coordinated **RMED Atoms Base Revise** through
`rmed_atoms_base_revise`, plus discovery, context, status/results and notification helpers.
`workflow_orchestrator` enqueues explicitly authorized independent Runs through
a separately started DBOS worker and Codex CLI adapter.
It uses the official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk).

## Run

From the repository root, using Python 3.14:

```sh
uv run --group rmed-workflow-mcp python 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/server.py --project-root "$PWD"
```

Transport is local **stdio**; there is no listening port or background daemon.
The MCP host owns the process lifetime. This does not register the server with
Codex or any other host. The current file-lock implementation supports macOS and
Linux. The server is bound to one Project root at startup, not a client-supplied
root on each request. Project Settings must register the shared Journal.

For independent execution, also include `--group workflow-orchestrator` in the
runtime invocation. Start the worker explicitly using its
[README](../203_APPS/WORKFLOW_ORCHESTRATOR/README.md). The worker's lifetime is
independent of this stdio adapter. The MCP does not start it implicitly.

## Calls

## Hot reload

`server.py` is now a stable stdio gateway; `implementation_server.py` runs in a
separate local process per generation. Install this gateway with one initial MCP
reconnect. Afterward invoke `reload_mcp_implementation`:

```json
{"request":{"operation":"reload","request_id":"reload-001"}}
```

Use a new request ID for a new reload; repeating an ID returns its original receipt
within the gateway session. Call `get_mcp_reload_status` with `{"request":{}}`
to inspect the current generation and in-flight counts. It is a separate read-only
Tool and performs no reload or persistence. `reload_mcp_implementation` accepts
only `operation: reload` and is explicitly state-changing. No file watcher or
automatic reload runs. Annotations do not override Codex's permission policy;
reload may still need a client-side allow rule.

Candidate initialization/schema failure keeps the old implementation serving.
Already-admitted calls finish on their original process; no calls are replayed.
The gateway emits Tool-list-change notifications when the registry changes, but
reports Codex's cache refresh as unconfirmed. A client that does not refresh still
needs reconnecting. Changes to gateway code or its Python runtime also require
reconnect; installed dependencies are never changed by a reload.

Receipts live in `.caprmedio_install/mcp_hot_reload/`; they are not Atom authority.
The DBOS worker is independent and is not restarted by MCP reload.

Candidate startup is bounded to 20 seconds. Retired generations with calls still
running after 60 seconds are marked `drain_limit_reached`; they are not forcibly
killed or replayed. A generation's `process_available` reports observed lifecycle,
not successful completion of its calls. This first slice sends legacy negotiated
Tool-list-change notifications; modern subscription-based delivery is reported
unsupported rather than claimed available.

## Workflow calls

Every call has `{"request": {"operation": "…", …}}`. The advertised schema is
a discriminated union: unknown fields and invalid operations are rejected.

| Operation | Purpose |
|---|---|
| `describe` | Return the three short prompts and usage instructions; no writes |
| `start` | Record an Operator-authorized Run with its ID, request, Author, session, Scope Unit, and timezone |
| `gather` | Save the calling session's selected `{atom_id, path}` list, `criteria_paths`, exclusions, and blockers |
| `context` | Return one Atom, current bound criteria, and the `check` or `fix` prompt; use zero-based `ordinal` |
| `submit` | Save that Atom's check or fix report; fixes also supply `after_paths` |
| `status` | Return separate reported/checked/completed counts and recording blockers |
| `handoff` | Save remaining-work context under the same Run ID |
| `finish` | Record `completed`, `interrupted`, or `failed`; unfinished selections cannot be completed |
| `report` | Read the full Markdown report |
| `sync` | Retry report/Journal recording only; never replay checks or fixes |

The calling session gathers the scope and applicable criteria, runs agentic
checks, and performs authorized fixes. This server neither interprets the scope
request into a corpus selection nor decides or applies semantic corrections.
Run only on Operator instruction; the server's presence grants no execution
authority. Current completed checks cannot be submitted as a new recheck.

`start` needs an `author` accepted by the existing Journal partition convention
(GitHub username), `session: {app, uuid}`, and `scope`. Do not fabricate them.
Settings currently resolve through `.caprmedio_caprmedio/caprmedio_project_settings.toml`;
multi-Project settings discovery is not implemented in this first slice.

## Evidence

Full report: `tmp/RMED Atoms Base Revise/<run_id>.md`. Internal state and per-Atom
JSON reports live under `.caprmedio_tmp/rmed-base-revise/<run_id>/`. Execution
events go to the configured shared Project Journal. Current rules/source drift
blocks a new correction admission; old evidence is retained. For a stale input,
resolve the change and explicitly start a newly authorized Run; no automatic
recheck occurs. Handoffs continue a running Run; terminal Runs stay immutable.

An outcome of `fixed_not_rechecked` means the reported findings have dispositions,
not that a second semantic review passed. Recording failures retain work evidence
and appear as `recording_blockers`. Run mutations are serialized with a lock;
concurrent calls for the same Run may return busy and should retry the same call.
Report submission retries are idempotent; a duplicate `start` must use `status`
to recover the existing Run rather than overwrite it.

This local interface assumes a trusted calling session and cooperative filesystem
writers. It rejects traversal, secret-file paths, and symlinks. It is not a
multi-user authorization service. Stop writes to the same Atom by other agents
while an admitted fix is in progress.

## Tests

```sh
uv run --group rmed-workflow-mcp python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/tests
```

The test client uses the real stdio MCP protocol and a temporary mock Project.
It exercises gathering, checks, fixes, shared-Journal writes, full reports, and
invalid-input rejection. It does not claim to validate an LLM's semantic judgment.
