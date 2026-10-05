---
atom_id: CA-P-1710
content_role: Plan
type: Plan
label: Task
work_sequence_number: 22
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Active
subjects:
  governs: "Finish Release provider focused verification"
  depends_on: [Tool, Workflow, Action, Journal, Evaluation]
version: 1
updated_at: "2026-10-05 09:49:00 +0000"
relations:
  is_decomposition_of: [CA-P-1643]
  blocks: [CA-P-1708, CA-P-1644]
---
# Summary

Finish Release provider focused verification

## Objective

Within <=8 minutes, resume P1708's capacity-interrupted partial provider and save its bounded verified frontier.

## Details

Own only selected_native_providers.py and tests/test_release_native_providers.py, preserving the existing saved partial work. Source admission P1709 is independently accepted98%; P1701 ten-phase API and P1707 conditional retirement API are ready. Finish only the current provider/context and unchanged-fifteen focused tests, correcting concrete failures. Private default image backend remains an explicitly incomplete runtime binding when None; no fake availability, second Journal writer, caller phase/executor flag or receipt. Report actual shared-recording/restart proof as unfinished if not executed. No further feature, source/Plan/Git/manifest/registry/settings/image work. If model capacity repeats, retain exact files/frontier and switch only to independent ready work, not an unauthorized model override.

## Definition of Done

Save exact code/test hashes and genuine focused result/remaining coverage, without claiming public or complete Release dispatch.

## Result

The resumed subagent returned normally; model capacity no longer prevents this bounded work. Added sixteen focused tests in tests/test_release_native_providers.py: thirteen disposable provider/admission/lineage/phase/refusal checks and three pure result conversion checks.

Three pure checks pass. The initial fourteen-test fixture run returned fourteen cleanup PermissionErrors, first under /tmp/tmpe5spxd0y/.caprmedio_install/workflow_orchestrator/runs/fixture-workflow. Assertion-body execution without an assertion failure is not a passing test when cleanup failed. C449 owns this permission boundary; no suppressed cleanup or alternate-path rerun was used.

Exact working-tree SHA-256: provider 5e92cbac42579201015c56ffaef15eb1f39ec66fbcc9a0f012c2a5d2daff95b9; new tests 08c3fe104f341f2d8763f2ac71ec1ffb3ac9259496c62dd29e37b4fc7dc37945; release_actions.py ff5be691be5ba01073ae667347ce078849e357d1c3d72aaf60c156ce31e22180; release_source_admission.py 36b86ba82dfbccbffe1f33eac23dbefa4f746db5055211f227f658aa10991228.

This Task remains Active: unchanged-fifteen integration, actual shared Journal recording, fixture-based verification, durable restart, actual image and public Release dispatch are not proven. The new tests use explicit admission/phase/tracker doubles. P1712 separately corrects macOS fixture root aliases without weakening production checks.
