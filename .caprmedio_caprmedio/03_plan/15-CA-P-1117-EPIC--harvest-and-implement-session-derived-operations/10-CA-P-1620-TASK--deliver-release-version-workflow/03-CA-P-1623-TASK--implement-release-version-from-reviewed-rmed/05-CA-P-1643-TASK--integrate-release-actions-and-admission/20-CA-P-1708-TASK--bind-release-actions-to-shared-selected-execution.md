---
atom_id: CA-P-1708
content_role: Plan
type: Plan
label: Task
work_sequence_number: 20
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Bind Release Actions to shared selected execution"
  depends_on: [Workflow, Action, Tool, Journal, Manifest, Evaluation]
version: 1
updated_at: "2026-10-05 07:41:51 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1644]
---
# Summary

Bind Release Actions to shared selected execution

## Objective

After P1706 source admission, integrate the accepted private ten-phase adapter into the existing selected native provider within <=15 minutes.

## Details

Own only WORKFLOW_ORCHESTRATOR/selected_native_providers.py and new tests/test_release_native_providers.py. Consume P1701 begin_release_action_run and execute_release_action, exact frozen D560 parameters, canonical source-admitted O164@2 and the actual shared Session context. Create per-dispatch private typed state from the actual Workflow Run identity; select phase only from current Step/Action pair, check frozen root/request/parent identities and refuse mismatches/unknown/unadmitted calls. Convert only actual phase effects/results into the existing shared recording path; do not add a Journal writer, caller receipt/phase flag or fake success.

Preserve every existing fifteen-route provider and construction-without-effects behavior. Image executor starts no image action at construction and is private native context, not a client override. Tests use only disposable Projects and explicit mocks; candidate source/compiled/suite/staging, same-Run continuity and shared actual Run/Action recording must be distinguished from actual image/Release proof. Stop on interrupted/pending/failed/unrecorded phases and never replay uncertain effects. Durable process-restart recording recovery is required later if this bounded provider only retains state within one dispatch; report it explicitly rather than claim complete Release integration.

No production manifest, public MCP registration, source/Plan/Git/settings values, actual image/container operation or C447/C449 workaround. Use only the designated development worker.

## Definition of Done

Save exact native provider/API/hashes and focused unchanged-fifteen plus Release context/recording/refusal outcomes. Actual public/queue/MCP/image and restart-recovery gates remain required.

### Interrupted frontier

Model capacity interrupted the Agent after a saved126-addition/two-removal provider delta and before a new test carrier or final verification result. C468/P1710 preserve and finish only that bounded current partial frontier. This Task remains Active; no source, image or prior test acceptance is substituted for its missing provider proof.
