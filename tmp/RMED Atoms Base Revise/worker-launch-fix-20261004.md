# Worker launch repair verification

- Workflow: RMED Atoms Base Revise.
- Codex mutable SQLite state and logs now live in each dispatch's `codex-state/` and `codex-logs/`, using documented per-invocation settings. Authentication and global Codex configuration are unchanged.
- Failed Actions retain a safe diagnostic cause in Coverage Gate questions and terminal Run reasons; detailed child output stays in local logs.
- The new tests failed before implementation and passed afterward: 19 orchestrator tests, including real DBOS queue/restart fixtures, subprocess mocks, incomplete-coverage interruption and failure-cause preservation. Lint passed.
- All 10 MCP protocol and hot-reload regression tests passed.
- A live launch smoke test passed the prior read-only database problem but was blocked by this session's network policy for `ab.chatgpt.com`. This was not a semantic Atom review.
- MCP implementation hot reload succeeded, active generation `eec0654e920e90bfc2362f83e1785a0c6182108f08b9a381a78ab1c1d50194b2`.
- The original pilot remains interrupted and unchanged. No new live Atom Run was enqueued, no selected Atom was edited, and no security policy was weakened.
- Restarting the worker requires the Operator's regular Terminal: the attempted stop of the previously started PID 57762 was denied by this session's permissions.

## Next step

From the repository root in your regular Terminal, stop the previously started worker (PID 57762), then run:

```sh
.caprmedio_tmp/implementation/rmed-workflow-mcp/venv/bin/python 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/orchestrator.py --project-root "$PWD" start-worker
```

After readiness is confirmed, enqueue a new explicitly authorized one-Atom pilot through MCP. The old terminal Run is immutable.
