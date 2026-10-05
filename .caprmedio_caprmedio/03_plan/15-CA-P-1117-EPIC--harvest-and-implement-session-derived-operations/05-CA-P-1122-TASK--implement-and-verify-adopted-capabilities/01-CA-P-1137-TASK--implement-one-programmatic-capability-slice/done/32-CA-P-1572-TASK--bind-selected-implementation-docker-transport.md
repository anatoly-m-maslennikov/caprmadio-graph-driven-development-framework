---
atom_id: CA-P-1572
content_role: Plan
type: Plan
label: Task
work_sequence_number: 32
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Selected Implementation Docker transport binding"
  depends_on: [Workflow, Action, Operator, Implementation, Evaluation]
version: 3
updated_at: "2026-10-05 00:21:02 +0000"
relations:
  is_decomposition_of: [CA-P-1516]
  blocks: [CA-P-1516, CA-P-1519]
---
# Summary

Bind selected Implementation Docker transport

## Objective

Within <=15 minutes, verify and connect W09's admitted independent Agent callback to explicit Docker startup and its executable mock proof.

## Details

- Read accepted R1843/D544 and directly bound O016/E/M, backend.worker, SelectedNativeProviders, implementation_agent.py and current Docker runtime/Agent startup first. The Base Revise RemoteAgent transport is not evidence that selected Implementation uses it.
- Own only narrowly needed Docker startup/transport glue and a focused new transport test. Coordinate before changing backend.worker with root; own no selected executor, fixture, MCP, provider or source. Preserve existing Base Revise runtime and no-host-code mounts.
- A mock Runtime must not silently call a paid live CLI or claim a marker response as actual implementation. Reuse the existing explicit isolation boundary and source-bound callback if admitted. Prove the mock actually exercises one permitted disposable implementation/assertion path; label it mock-not-live-llm. No ambient grants, new arbitrary writer, authorization/configuration changes or live credential use.
- Real runtime startup must preserve the declared Agent/Project isolation and exact admitted workspace permissions. If the accepted source cannot safely connect that transport, return the precise boundary prerequisite without inventing authority or broadening this Task.
- Use apply_patch, preserve everyone, no Plans/Journal/commits or full image run. Root saves and owns image proof. Inherit 90%, no FPF, harvesting or live Project mutation.
- Actual focused boundary test: 2/2; independent Agent/provider regression: 10/10. No transport or permissions widened. Current prompt resolver uses immutable code ROOT instead of selected Project governance; W09 lacks explicit workspace and matching write capability; isolated Agent has no Project mount. P1575 source declaration and P1580 independent review gate the narrow resolver/mock transport continuation. No live CLI invoked, no full image or completion claim.

## Saved result

Saved the explicit Docker mock transport in backend.py, runtime_config.py, mock.compose.yaml and implementation_mock_agent.py. Original focused boundary tests passed 7/7; native ImplementationAgent regression passed 4/4. Actual disposable baseline failure, candidate creation and assertion pass are labelled mock-not-live-llm. P1597 independently accepted the source boundary; immutable-image proof remains separate.

## Definition of Done

The explicit selected Docker transport is source-bound with focused executable mock evidence, or its exact missing source/runtime prerequisite is retained unfinished.
