---
atom_id: CA-E-538
content_role: Evaluation
type: QA Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 04:10:07 +0400"
subjects:
  governs: "Action/execution/isolation evaluation"
  depends_on: [AI Agent, Atom, Carrier, Implementation, Action, Operator]
relations:
  evaluation_for: [CA-R-1819, CA-M-325, CA-D-525]
---
# Summary

verify Agent container isolation

## Scope

the Docker Agent service's admission **and** filesystem boundaries.

## Claim

the Evaluation **must** verify that an isolated Agent can return proposals but cannot access host Project Carriers **or** runtime-control capabilities.

## Details

- inspect the resolved configuration: Agent has no Project, host-home **or** Docker socket mount, no published port, no privileged mode **and** no added capabilities.
- test rejected unknown fields, invalid phases, oversized requests, concurrent dispatch **and** invalid structured output.
- verify denied Project write probes **and** absence of credential files from image layers **and** public outputs.
- verify missing credentials produce an explicit readiness failure **without** starting a real Workflow.
