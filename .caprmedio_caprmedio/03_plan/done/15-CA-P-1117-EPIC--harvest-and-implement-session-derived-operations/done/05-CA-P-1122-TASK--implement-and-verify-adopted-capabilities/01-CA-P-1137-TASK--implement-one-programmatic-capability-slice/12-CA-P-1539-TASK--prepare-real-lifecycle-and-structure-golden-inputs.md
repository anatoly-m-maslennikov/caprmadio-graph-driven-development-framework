---
atom_id: CA-P-1539
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: "Prepare real lifecycle and structure golden inputs"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 2
updated_at: "2026-10-04 21:59:34 +0000"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1519]
---
# Summary

Prepare real lifecycle and structure golden inputs

## Objective

Within <=15 minutes, test-first finish this bounded original-thirteen execution remainder under current accepted source/RMED.

## Details

Own tests/selected_workflows_docker_fixture.py and new tests/test_selected_golden_inputs.py in WORKFLOW_ORCHESTRATOR only. Current GoldenProject supplies generic JSON marker parameters for every selected route, not native valid Action inputs. For W01–W08 construct source-valid disposable Project settings, Operators registry, structure TOML, actual Atom carriers/status models/target frontiers, and native per-route parameters, expected effects and validators. Reuse current thirteen-route source-pinned manifest and existing lifecycle/ProjectStructure APIs. Test the request corpus against real native adapters in temporary Projects; passing preview or case labels do not prove functional inputs. Do not weaken no-host-implementation/no-real-Project constraints, borrow actual native Runs or modify test_selected_workflows_docker_e2e.py yet. Mock dispatch/evidence wrappers may prove corpus only, not actual image coverage. W09–W13 and query fixtures remain separately bound. Root saves result; each incomplete route is an explicit frontier.

Read current Epic/P1517/P1519, directly bound source/RMED and current active Method projection before edits. Inherit 90% confidence and mechanical save exception. You are not alone; preserve concurrent work and use apply_patch. No harvesting, FPF, paid Agent call, production authority mutation, external deployment or permission bypass. Root owns Plan writes/commits. Unfinished work retains an exact truthful frontier.

### Definition of Done

The bounded owned behavior has actual functional golden evidence, commands/results and exact changed files. No aggregate Docker/MCP/Agent proof is implied.

## Result

W01–W08 now have native valid Atom lifecycle and Project Structure inputs. The fixture supplies Project settings, registered Operator, actual carriers and target frontiers, and proves real disposable-Project filesystem effects from create/update/replace/status and create/rename/move/remove adapters. The initial structural fixture failed on missing authority_modes.default; the corrected settings preserve the contract rather than bypassing it. Create's intentionally absent initial carrier is represented correctly.

Changed files: WORKFLOW_ORCHESTRATOR/tests/selected_workflows_docker_fixture.py and tests/test_selected_golden_inputs.py.

Root independently reran:

`docker exec -w /project caprmedio-ea535e2c0d4e-worker-1 /opt/venv/bin/python -m unittest discover -s 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests -p test_selected_golden_inputs.py -v`

Result: 2 tests covering all eight native routes passed in 55.369 seconds. The worker also reported compilation and owned whitespace checks passing. GoldenProject.native_parameters() is the native payload API for queue/MCP fixtures.

This closes only the bounded W01–W08 corpus packet. W09–W13 remain generic fixture parameters; no complete queue/MCP/Run/Journal or fresh-image proof is implied.
