---
atom_id: CA-P-1536
content_role: Plan
type: Plan
label: Task
work_sequence_number: 11
current_scope_unit: caprmedio
claim_target_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: "Bind Implementation Step-specific inputs"
  depends_on: [Implementation, Workflow, Action, Evaluation, Journal]
version: 1
updated_at: "2026-10-05 01:30:00 +0400"
relations:
  is_decomposition_of: [CA-P-1137]
  blocks: [CA-P-1517]
---
# Summary

Bind Implementation Step-specific inputs

## Objective

Within <=15 minutes, repair only O016 Step-specific parameter selection and retained state propagation in the existing graph executor.

## Details

Own selected_execution.py's Implementation adapter/state handoff and tests/test_selected_execution.py only. Read current P1517, D545, O016 and its Steps/Actions, plus IMPLEMENTATION_WORKFLOW/implementation_actions.py and source_bindings.json. Current adapter passes identical parameters to every Step although source requires Integrated/Isolated per Step; fix using manifest-selected Step-specific input with checked current M projection and R/D/E targets, carry performed outputs/evidence/retry state to the next actual Step, never add hardcoded successor policy. Test the real seven-Action prompt handlers through an injected mock Agent, not stand-ins bypassing packet validation; expected failing baseline then passing traversal and blocked/missing input. Preserve existing BaseRevise and all other native handlers. No Codex/HTTP transport, backend, MCP, source/RMED or actual Project mutation; later transport and image proof remain separate. You are not alone, preserve others and use apply_patch. Publish API and truthful remaining wiring.

### Definition of Done

The exact bounded result, changed files, source pins and actual verification are saved with truthful remainder. No broader implementation or immutable-image proof is implied.
