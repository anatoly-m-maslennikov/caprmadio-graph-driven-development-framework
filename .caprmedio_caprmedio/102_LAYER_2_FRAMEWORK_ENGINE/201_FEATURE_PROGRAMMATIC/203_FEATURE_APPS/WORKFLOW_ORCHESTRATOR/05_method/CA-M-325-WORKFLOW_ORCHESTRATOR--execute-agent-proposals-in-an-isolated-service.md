---
atom_id: CA-M-325
content_role: Method
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Action/execution/Docker adapter"
  depends_on: [AI Agent, Action, Atom, Workflow Run, Implementation, Operator, Carrier]
relations:
  relates_to: [CA-R-1819, CA-M-321]
---
# Summary

execute Agent proposals **in** an isolated service

## Scope

the worker's replaceable Agent adapter **in** the Docker runtime.

## Claim

execute an Agentic Action by sending its bound context **to** the private Agent service **and** admitting the returned proposal through the existing worker boundary.

## Details

- use a bounded JSON request carrying context, check **or** fix phase **and** timeout; admit the existing AgentOutput schema.
- provide **only** the compiled context, not Project mounts. run Codex CLI **in** a fresh dispatch directory with no inherited user configuration **or** MCP registrations.
- the dedicated Agent container provides outer isolation; the CLI can use external isolation there. native execution retains its read-only CLI sandbox.
- allow **<=1** active Agent request initially. bound request bytes, response bytes **and** execution duration.
- preserve accepted output before effects. transport loss, timeout, invalid output **or** authentication failure interrupts rather than silently retrying.
- seed an absent private runtime authentication cache from an explicitly mounted credential file. do **not** overwrite an existing refreshed cache **or** print its contents.
